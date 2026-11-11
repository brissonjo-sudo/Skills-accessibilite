#!/usr/bin/env python3
"""Valide les paquets de preuves et leur présence lors d'une promotion.

Codes de sortie : 0 = conforme, 1 = violation, 2 = contrôle impossible.
"""

import argparse
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path

from _common import utf8_stdio

ROOT = Path(__file__).resolve().parent.parent
EVIDENCE_ROOT = ROOT / "eval" / "evidence"
SKILLS_DIR = ROOT / "skills"
INDEX_PATH = ROOT / "docs" / "index_skills.md"
SHA_RE = re.compile(r"^[0-9a-f]{40}$")
SHA256_RE = re.compile(r"^[0-9a-f]{64}$")
REQUIRED_FILES = {
    "manifest.json",
    "activation_results.jsonl",
    "verdicts.jsonl",
    "metrics.json",
    "report.md",
}
# Champs exigés sur chaque ligne : sans eux, une ligne `{}` passerait pour une preuve.
JSONL_REQUIRED_FIELDS = {
    "activation_results.jsonl": ("case_id",),
    "verdicts.jsonl": ("judge_role", "config", "case_id"),
}
PRODUCTION = "production"
CANDIDATE_PREFIX = "candidat"


class CheckError(Exception):
    """Le contrôle ne peut pas être mené (dépôt, base de comparaison, index)."""


def git(*args: str) -> str:
    return subprocess.check_output(
        ["git", *args], cwd=ROOT, text=True, encoding="utf-8",
        stderr=subprocess.DEVNULL,
    ).strip()


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def known_skills() -> set[str]:
    return {
        item.name for item in SKILLS_DIR.iterdir()
        if item.is_dir() and (item / "SKILL.md").is_file()
    }


def skill_sha256(skill: str) -> str:
    """Empreinte du SKILL.md, fins de ligne ramenées à LF.

    La normalisation rend l'empreinte identique sous Windows (CRLF dans la
    copie de travail) et en CI (LF).
    """
    data = (SKILLS_DIR / skill / "SKILL.md").read_bytes().replace(b"\r\n", b"\n")
    return hashlib.sha256(data).hexdigest()


# ── Paquets de preuves ───────────────────────────────────────────────────────

def validate_jsonl(path: Path, violations: list[str]) -> None:
    rel = path.relative_to(ROOT).as_posix()
    required = JSONL_REQUIRED_FIELDS[path.name]
    lines = [line for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]
    if not lines:
        violations.append(f"{rel} : fichier JSONL vide")
        return
    for number, line in enumerate(lines, start=1):
        try:
            value = json.loads(line)
        except json.JSONDecodeError as exc:
            violations.append(f"{rel}:{number} : JSON invalide ({exc})")
            continue
        if not isinstance(value, dict):
            violations.append(f"{rel}:{number} : chaque ligne doit être un objet")
            continue
        missing = [
            field for field in required
            if not isinstance(value.get(field), str) or not value[field].strip()
        ]
        if missing:
            violations.append(
                f"{rel}:{number} : champs absents ou vides : {', '.join(missing)}"
            )


def validate_bundle(path: Path, violations: list[str]) -> dict[str, str]:
    """Valide un paquet. Retourne {skill validé: empreinte du SKILL.md évalué}."""
    rel = path.relative_to(ROOT).as_posix()

    # Le paquet est une liste fermée : tout autre fichier est refusé, en
    # particulier la table d'aveuglement et les réponses brutes.
    extra = sorted(item.name for item in path.iterdir() if item.name not in REQUIRED_FILES)
    if extra:
        violations.append(
            f"{rel} : fichiers interdits dans un paquet assaini : {', '.join(extra)}"
        )
    missing = sorted(name for name in REQUIRED_FILES if not (path / name).is_file())
    if missing:
        violations.append(f"{rel} : fichiers obligatoires absents : {', '.join(missing)}")
        return {}

    try:
        manifest = load_json(path / "manifest.json")
        metrics = load_json(path / "metrics.json")
    except (OSError, json.JSONDecodeError) as exc:
        violations.append(f"{rel} : JSON impossible à lire ({exc})")
        return {}

    if not isinstance(manifest, dict) or manifest.get("schema_version") != 1:
        violations.append(f"{rel}/manifest.json : schema_version doit valoir 1")
        manifest = {}
    if not isinstance(metrics, dict) or not metrics:
        violations.append(f"{rel}/metrics.json : la racine doit être un objet non vide")

    if manifest.get("run_id") != path.name:
        violations.append(f"{rel}/manifest.json : run_id doit correspondre au dossier")

    commit = manifest.get("commit")
    if not isinstance(commit, str) or not SHA_RE.fullmatch(commit):
        violations.append(f"{rel}/manifest.json : commit doit être un SHA Git complet")

    if manifest.get("protocol") != "eval/prompt_benchmark_claude_code.md":
        violations.append(f"{rel}/manifest.json : protocole canonique absent ou incorrect")

    validated = manifest.get("validated_skills")
    if (
        not isinstance(validated, list) or not validated
        or not all(isinstance(item, str) for item in validated)
    ):
        violations.append(
            f"{rel}/manifest.json : validated_skills doit être une liste non vide de noms"
        )
        validated = []

    skill_hashes = manifest.get("skill_sha256")
    if not isinstance(skill_hashes, dict):
        violations.append(
            f"{rel}/manifest.json : skill_sha256 absent (empreinte du SKILL.md "
            "évalué, pour chaque skill validé)"
        )
        skill_hashes = {}
    covered: dict[str, str] = {}
    for skill in validated:
        value = skill_hashes.get(skill)
        if not isinstance(value, str) or not SHA256_RE.fullmatch(value):
            violations.append(
                f"{rel}/manifest.json : skill_sha256 absent ou invalide pour {skill}"
            )
        else:
            covered[skill] = value

    hashes = manifest.get("source_artifact_sha256")
    required_hashes = {"raw_generations.jsonl", "blinding_map.json", "judge_outputs"}
    if not isinstance(hashes, dict) or not required_hashes.issubset(hashes):
        violations.append(
            f"{rel}/manifest.json : empreintes des artefacts bruts incomplètes"
        )
    elif any(
        not isinstance(value, str) or not SHA256_RE.fullmatch(value)
        for value in hashes.values()
    ):
        violations.append(f"{rel}/manifest.json : empreinte SHA-256 invalide")

    validate_jsonl(path / "activation_results.jsonl", violations)
    validate_jsonl(path / "verdicts.jsonl", violations)
    if not (path / "report.md").read_text(encoding="utf-8").strip():
        violations.append(f"{rel}/report.md : rapport vide")

    return covered


# ── Statuts de l'index ───────────────────────────────────────────────────────

def clean_cell(cell: str) -> str:
    """Retire la décoration Markdown et les symboles en bordure d'une cellule."""
    text = re.sub(r"[*`_~]", "", cell)
    return re.sub(r"^\W+|\W+$", "", text).strip()


def parse_statuses(text: str) -> dict[str, str] | None:
    """Lit le tableau de synthèse de l'index.

    Les colonnes sont repérées par leur en-tête (« Skill », « Statut »), pas par
    leur position. Retourne {skill: statut normalisé}, ou None si aucun tableau
    portant ces deux colonnes n'est trouvé.
    """
    statuses: dict[str, str] | None = None
    skill_col = status_col = -1
    for line in text.splitlines():
        stripped = line.strip()
        if not stripped.startswith("|"):
            skill_col = status_col = -1
            continue
        cells = [cell.strip() for cell in stripped.strip("|").split("|")]
        if skill_col < 0:
            headers = [clean_cell(cell).lower() for cell in cells]
            if "skill" in headers and "statut" in headers:
                skill_col, status_col = headers.index("skill"), headers.index("statut")
                statuses = {} if statuses is None else statuses
            continue
        if all(set(cell) <= set("-: ") for cell in cells):
            continue  # ligne de séparation
        if len(cells) <= max(skill_col, status_col):
            continue
        name = clean_cell(cells[skill_col])
        if name:
            statuses[name] = clean_cell(cells[status_col]).lower()
    return statuses


def status_kind(status: str | None) -> str | None:
    if status == PRODUCTION:
        return PRODUCTION
    if status and status.startswith(CANDIDATE_PREFIX):
        return CANDIDATE_PREFIX
    return None


def current_statuses(violations: list[str]) -> dict[str, str]:
    rel = INDEX_PATH.relative_to(ROOT).as_posix()
    try:
        statuses = parse_statuses(INDEX_PATH.read_text(encoding="utf-8"))
    except OSError as exc:
        raise CheckError(f"{rel} illisible ({exc})") from exc
    if statuses is None:
        raise CheckError(f"{rel} : tableau avec colonnes « Skill » et « Statut » introuvable")

    skills = known_skills()
    for name in sorted(skills - set(statuses)):
        violations.append(f"{rel} : skill absent du tableau de synthèse : {name}")
    for name in sorted(set(statuses) - skills):
        violations.append(f"{rel} : le tableau cite un skill inexistant : {name}")
    for name in sorted(skills & set(statuses)):
        if status_kind(statuses[name]) is None:
            violations.append(
                f"{rel} : statut non reconnu pour {name} : {statuses[name]!r} "
                f"(attendu : « {PRODUCTION} » ou « {CANDIDATE_PREFIX}… »)"
            )
    return statuses


# ── Base de comparaison ──────────────────────────────────────────────────────

def commit_exists(ref: str) -> bool:
    try:
        git("cat-file", "-e", f"{ref}^{{commit}}")
    except subprocess.CalledProcessError:
        return False
    return True


def resolve_base(base: str) -> str | None:
    """Retourne le commit de comparaison, ou None s'il n'y a rien à comparer.

    Une base absente, nulle ou introuvable ne désactive pas le contrôle : on se
    rabat sur le point de divergence avec origin/main.
    """
    if base and set(base) != {"0"} and commit_exists(base):
        return base
    if base:
        print(f"[INFO] base {base[:12]} introuvable ou nulle : repli sur origin/main")
    try:
        fallback = git("merge-base", "origin/main", "HEAD")
        head = git("rev-parse", "HEAD")
    except subprocess.CalledProcessError as exc:
        raise CheckError(
            "aucune base de comparaison : passer --base <commit>, ou rendre "
            "origin/main disponible (git fetch origin main)"
        ) from exc
    return None if fallback == head else fallback


def required_skills(base: str, statuses: dict[str, str]) -> tuple[set[str], set[str]]:
    """Skills exigeant une preuve, et skills simplement rétrogradés."""
    changed_files = git("diff", "--name-only", f"{base}...HEAD").splitlines()
    changed = {
        Path(name).parts[1] for name in changed_files
        if len(Path(name).parts) >= 3 and Path(name).parts[0] == "skills"
    }

    try:
        previous = parse_statuses(git("show", f"{base}:docs/index_skills.md")) or {}
    except subprocess.CalledProcessError:
        previous = {}

    def is_prod(table: dict[str, str], name: str) -> bool:
        return status_kind(table.get(name)) == PRODUCTION

    names = set(statuses) | set(previous) | changed
    promoted = {n for n in names if is_prod(statuses, n) and not is_prod(previous, n)}
    # Un skill en production avant ou après le changement : le rétrograder dans
    # la même PR que sa modification ne dispense pas de la preuve.
    modified = {n for n in changed if is_prod(statuses, n) or is_prod(previous, n)}
    demoted_only = {
        n for n in names
        if is_prod(previous, n) and not is_prod(statuses, n) and n not in changed
    }
    return (promoted | modified) & (known_skills() | changed), demoted_only


def new_bundle_ids(base: str) -> set[str]:
    added = git("diff", "--diff-filter=A", "--name-only", f"{base}...HEAD").splitlines()
    return {
        Path(name).parts[2] for name in added
        if len(Path(name).parts) == 4
        and Path(name).parts[:2] == ("eval", "evidence")
        and Path(name).name == "manifest.json"
    }


def main() -> int:
    utf8_stdio()
    parser = argparse.ArgumentParser()
    parser.add_argument("--base", default="", help="commit de base pour contrôler les promotions")
    args = parser.parse_args()

    violations: list[str] = []
    bundles: dict[str, dict[str, str]] = {}
    if EVIDENCE_ROOT.is_dir():
        for path in sorted(item for item in EVIDENCE_ROOT.iterdir() if item.is_dir()):
            bundles[path.name] = validate_bundle(path, violations)

    try:
        statuses = current_statuses(violations)
        base = resolve_base(args.base)
        required, demoted = (required_skills(base, statuses) if base else (set(), set()))
        fresh = new_bundle_ids(base) if base else set()
    except CheckError as exc:
        print(f"[ERREUR] {exc}")
        return 2

    if base is None:
        print("[WARN] HEAD est sur origin/main et aucune base n'est fournie : "
              "promotions non contrôlées")
    for name in sorted(demoted):
        print(f"[INFO] rétrogradation sans modification du skill : {name}")

    for skill in sorted(required):
        if not (SKILLS_DIR / skill / "SKILL.md").is_file():
            continue  # skill supprimé : rien à prouver
        expected = skill_sha256(skill)
        hashes = [bundles[run_id][skill] for run_id in fresh if skill in bundles.get(run_id, {})]
        if not hashes:
            violations.append(
                "promotion ou modification d'un skill en production sans nouveau "
                f"paquet de preuves couvrant : {skill}"
            )
        elif expected not in hashes:
            violations.append(
                f"le paquet de preuves couvrant {skill} porte sur une autre version "
                f"du SKILL.md (attendu skill_sha256={expected[:12]}…) : la vague doit "
                "évaluer l'état final du skill"
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
