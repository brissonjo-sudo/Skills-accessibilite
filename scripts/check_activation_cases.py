#!/usr/bin/env python3
"""Valide la banque JSON des cas de sélection et de non-déclenchement.

Chaque cas vise un skill (`target_skill`) et dit s'il doit être sélectionné
(`expected_activation`). Deux champs facultatifs décrivent les autres skills :
`also_expected` (à sélectionner aussi) et `must_not_activate` (à ne pas
sélectionner). Ils servent aux cas de co-activation et aux faux positifs croisés.
"""

import json
import re
import sys
from pathlib import Path

from _common import utf8_stdio

ROOT = Path(__file__).resolve().parent.parent
CASES_PATH = ROOT / "eval" / "activation_cases.json"
SKILLS_DIR = ROOT / "skills"
ID_RE = re.compile(r"^[a-z0-9-]+$")
ALLOWED_KEYS = {
    "id", "description", "target_skill", "expected_activation", "question",
    "also_expected", "must_not_activate",
}


def fail(message: str) -> None:
    print(f"[FAIL] {message}")


def check_skill_list(test: dict, field: str, skill_names: set[str], label: str) -> list[str]:
    """Valide un champ facultatif contenant une liste de noms de skills."""
    if field not in test:
        return []
    value = test[field]
    if (
        not isinstance(value, list) or not value
        or not all(isinstance(item, str) for item in value)
    ):
        return [f"{label} : {field} doit être une liste non vide de noms de skills"]
    violations = []
    unknown = sorted(set(value) - skill_names)
    if unknown:
        violations.append(f"{label} : {field} cite des skills inconnus : {', '.join(unknown)}")
    if len(set(value)) != len(value):
        violations.append(f"{label} : {field} contient des doublons")
    return violations


def main() -> int:
    utf8_stdio()
    violations: list[str] = []

    try:
        data = json.loads(CASES_PATH.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        fail(f"{CASES_PATH.relative_to(ROOT).as_posix()} : lecture JSON impossible ({exc})")
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
    seen_questions: set[str] = set()

    for index, test in enumerate(tests, start=1):
        label = f"activation_cases.json : test #{index}"
        if not isinstance(test, dict):
            violations.append(f"{label} doit être un objet")
            continue

        unknown_keys = sorted(str(key) for key in test if key not in ALLOWED_KEYS)
        if unknown_keys:
            violations.append(f"{label} : clés inconnues : {', '.join(unknown_keys)}")

        case_id = test.get("id")
        if not isinstance(case_id, str) or not ID_RE.fullmatch(case_id):
            violations.append(f"{label} : id absent ou invalide")
        elif case_id in seen_ids:
            violations.append(f"{label} : id dupliqué {case_id}")
        else:
            seen_ids.add(case_id)

        target = test.get("target_skill")
        if not isinstance(target, str) or target not in skill_names:
            violations.append(f"{label} : target_skill inconnu {target!r}")
            target = None

        expected = test.get("expected_activation")
        if not isinstance(expected, bool):
            violations.append(f"{label} : expected_activation doit être un booléen")
        elif target is not None:
            coverage[target].add(expected)

        for field in ("also_expected", "must_not_activate"):
            violations.extend(check_skill_list(test, field, skill_names, label))
        also = test.get("also_expected") if isinstance(test.get("also_expected"), list) else []
        never = (
            test.get("must_not_activate")
            if isinstance(test.get("must_not_activate"), list) else []
        )
        hashable = [item for item in also + never if isinstance(item, str)]
        if target is not None and target in hashable:
            violations.append(
                f"{label} : target_skill ne doit pas figurer dans also_expected "
                "ni dans must_not_activate"
            )
        overlap = sorted(
            set(item for item in also if isinstance(item, str))
            & set(item for item in never if isinstance(item, str))
        )
        if overlap:
            violations.append(
                f"{label} : skills à la fois attendus et interdits : {', '.join(overlap)}"
            )

        for field in ("description", "question"):
            value = test.get(field)
            if not isinstance(value, str) or not value.strip():
                violations.append(f"{label} : {field} absent ou vide")

        question = test.get("question")
        if isinstance(question, str) and question.strip():
            if question in seen_questions:
                violations.append(f"{label} : question dupliquée")
            seen_questions.add(question)

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
