#!/usr/bin/env python3
"""Valide les paquets de preuves et leur présence lors d'une promotion."""

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
EVIDENCE_ROOT = ROOT / "eval" / "evidence"
INDEX_PATH = ROOT / "docs" / "index_skills.md"
SHA_RE = re.compile(r"^[0-9a-f]{40}$")
REQUIRED_FILES = {
    "manifest.json",
    "activation_results.jsonl",
    "verdicts.jsonl",
    "metrics.json",
    "report.md",
}


def git(*args: str) -> str:
    return subprocess.check_output(
        ["git", *args], cwd=ROOT, text=True, encoding="utf-8"
    ).strip()


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def validate_jsonl(path: Path, violations: list[str]) -> None:
    lines = [line for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]
    if not lines:
        violations.append(f"{path.relative_to(ROOT)} : fichier JSONL vide")
        return
    for number, line in enumerate(lines, start=1):
        try:
            value = json.loads(line)
        except json.JSONDecodeError as exc:
            violations.append(
                f"{path.relative_to(ROOT)}:{number} : JSON invalide ({exc})"
            )
            continue
        if not isinstance(value, dict):
            violations.append(
                f"{path.relative_to(ROOT)}:{number} : chaque ligne doit être un objet"
            )


def validate_bundle(path: Path, violations: list[str]) -> set[str]:
    rel = path.relative_to(ROOT)
    missing = sorted(name for name in REQUIRED_FILES if not (path / name).is_file())
    if missing:
        violations.append(f"{rel} : fichiers obligatoires absents : {', '.join(missing)}")
        return set()

    try:
        manifest = load_json(path / "manifest.json")
        metrics = load_json(path / "metrics.json")
    except (OSError, json.JSONDecodeError) as exc:
        violations.append(f"{rel} : JSON impossible à lire ({exc})")
        return set()

    if not isinstance(manifest, dict) or manifest.get("schema_version") != 1:
        violations.append(f"{rel}/manifest.json : schema_version doit valoir 1")
        manifest = {}
    if not isinstance(metrics, dict):
        violations.append(f"{rel}/metrics.json : la racine doit être un objet")

    run_id = manifest.get("run_id")
    if run_id != path.name:
        violations.append(f"{rel}/manifest.json : run_id doit correspondre au dossier")

    commit = manifest.get("commit")
    if not isinstance(commit, str) or not SHA_RE.fullmatch(commit):
        violations.append(f"{rel}/manifest.json : commit doit être un SHA Git complet")

    if manifest.get("protocol") != "eval/prompt_benchmark_claude_code.md":
        violations.append(f"{rel}/manifest.json : protocole canonique absent ou incorrect")

    known_skills = {
        item.name for item in (ROOT / "skills").iterdir()
        if item.is_dir() and (item / "SKILL.md").is_file()
    }
    validated = manifest.get("validated_skills")
    if not isinstance(validated, list) or not validated:
        violations.append(f"{rel}/manifest.json : validated_skills doit être une liste non vide")
        validated_skills: set[str] = set()
    else:
        validated_skills = set(validated)
        unknown = sorted(validated_skills - known_skills)
        if unknown:
            violations.append(
                f"{rel}/manifest.json : skills inconnus : {', '.join(unknown)}"
            )

    hashes = manifest.get("source_artifact_sha256")
    required_hashes = {"raw_generations.jsonl", "blinding_map.json", "judge_outputs"}
    if not isinstance(hashes, dict) or not required_hashes.issubset(hashes):
        violations.append(
            f"{rel}/manifest.json : empreintes des artefacts bruts incomplètes"
        )
    elif any(
        not isinstance(value, str) or not re.fullmatch(r"[0-9a-f]{64}", value)
        for value in hashes.values()
    ):
        violations.append(f"{rel}/manifest.json : empreinte SHA-256 invalide")

    validate_jsonl(path / "activation_results.jsonl", violations)
    validate_jsonl(path / "verdicts.jsonl", violations)
    if not (path / "report.md").read_text(encoding="utf-8").strip():
        violations.append(f"{rel}/report.md : rapport vide")

    return validated_skills


def parse_statuses(text: str) -> dict[str, str]:
    statuses: dict[str, str] = {}
    for line in text.splitlines():
        if not line.startswith("|"):
            continue
        cells = [cell.strip() for cell in line.strip("|").split("|")]
        if len(cells) >= 4 and cells[0].startswith(("accessibilite-", "psychologie-")):
            statuses[cells[0]] = cells[3].lower()
    return statuses


def promoted_skills(base: str) -> set[str]:
    if not base or set(base) == {"0"}:
        return set()
    try:
        git("cat-file", "-e", f"{base}^{{commit}}")
    except subprocess.CalledProcessError:
        return set()

    changed = set(git("diff", "--name-only", f"{base}...HEAD").splitlines())
    changed_skills = {
        Path(name).parts[1]
        for name in changed
        if len(Path(name).parts) == 3
        and Path(name).parts[0] == "skills"
        and Path(name).name == "SKILL.md"
    }

    current = parse_statuses(INDEX_PATH.read_text(encoding="utf-8"))
    try:
        previous = parse_statuses(git("show", f"{base}:docs/index_skills.md"))
    except subprocess.CalledProcessError:
        previous = {}

    newly_production = {
        name for name, status in current.items()
        if status == "production" and previous.get(name) != "production"
    }
    changed_in_production = {
        name for name in changed_skills if current.get(name) == "production"
    }
    return newly_production | changed_in_production


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--base", default="", help="SHA de base pour contrôler les promotions")
    args = parser.parse_args()

    violations: list[str] = []
    bundles: dict[str, set[str]] = {}
    if EVIDENCE_ROOT.is_dir():
        for path in sorted(item for item in EVIDENCE_ROOT.iterdir() if item.is_dir()):
            bundles[path.name] = validate_bundle(path, violations)

    required = promoted_skills(args.base)
    if required:
        added = set(
            git("diff", "--diff-filter=A", "--name-only", f"{args.base}...HEAD").splitlines()
        )
        new_bundle_ids = {
            Path(name).parts[2]
            for name in added
            if len(Path(name).parts) == 4
            and Path(name).parts[:2] == ("eval", "evidence")
            and Path(name).name == "manifest.json"
        }
        covered = set().union(*(bundles.get(run_id, set()) for run_id in new_bundle_ids))
        missing = sorted(required - covered)
        if missing:
            violations.append(
                "promotion ou modification d'un skill en production sans nouveau "
                f"paquet de preuves couvrant : {', '.join(missing)}"
            )

    if violations:
        for violation in violations:
            print(f"[FAIL] {violation}")
        return 1

    print(
        f"[OK] {len(bundles)} paquet(s) de preuves valide(s)"
        + (f" — promotions contrôlées : {', '.join(sorted(required))}" if required else "")
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
