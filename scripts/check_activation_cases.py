#!/usr/bin/env python3
"""Valide la banque JSON des cas de sélection et de non-déclenchement."""

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CASES_PATH = ROOT / "eval" / "activation_cases.json"
SKILLS_DIR = ROOT / "skills"
ID_RE = re.compile(r"^[a-z0-9-]+$")


def fail(message: str) -> None:
    print(f"[FAIL] {message}")


def main() -> int:
    violations: list[str] = []

    try:
        data = json.loads(CASES_PATH.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        fail(f"{CASES_PATH.relative_to(ROOT)} : lecture JSON impossible ({exc})")
        return 1

    if not isinstance(data, dict) or data.get("schema_version") != 1:
        violations.append("activation_cases.json : schema_version doit valoir 1")

    tests = data.get("tests") if isinstance(data, dict) else None
    if not isinstance(tests, list):
        violations.append("activation_cases.json : tests doit être une liste")
        tests = []

    skill_names = {
        path.name for path in SKILLS_DIR.iterdir()
        if path.is_dir() and (path / "SKILL.md").is_file()
    }
    coverage = {name: set() for name in skill_names}
    seen_ids: set[str] = set()

    for index, test in enumerate(tests, start=1):
        label = f"activation_cases.json : test #{index}"
        if not isinstance(test, dict):
            violations.append(f"{label} doit être un objet")
            continue

        case_id = test.get("id")
        if not isinstance(case_id, str) or not ID_RE.fullmatch(case_id):
            violations.append(f"{label} : id absent ou invalide")
        elif case_id in seen_ids:
            violations.append(f"{label} : id dupliqué {case_id}")
        else:
            seen_ids.add(case_id)

        target = test.get("target_skill")
        if target not in skill_names:
            violations.append(f"{label} : target_skill inconnu {target!r}")

        expected = test.get("expected_activation")
        if not isinstance(expected, bool):
            violations.append(f"{label} : expected_activation doit être un booléen")
        elif target in coverage:
            coverage[target].add(expected)

        for field in ("description", "question"):
            value = test.get(field)
            if not isinstance(value, str) or not value.strip():
                violations.append(f"{label} : {field} absent ou vide")

    for skill_name, outcomes in sorted(coverage.items()):
        if outcomes != {False, True}:
            violations.append(
                f"activation_cases.json : {skill_name} doit avoir au moins "
                "un cas positif et un cas négatif"
            )

    if violations:
        for violation in violations:
            fail(violation)
        return 1

    print(
        f"[OK] {len(tests)} cas d'activation valides — "
        f"{len(skill_names)} skills, positif + négatif pour chacun"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
