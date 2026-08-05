#!/usr/bin/env python3
"""Valide la syntaxe et le schéma des banques de cas YAML."""

import sys
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
EVAL_DIR = REPO_ROOT / "eval"
SKILLS_DIR = (REPO_ROOT / "skills").resolve()
EXPECTED_CONFIGS = {
    "promptfooconfig.yaml",
    "promptfooconfig_coactivation.yaml",
    "promptfooconfig_dys.yaml",
    "promptfooconfig_fatigue.yaml",
    "promptfooconfig_psychologie.yaml",
    "promptfooconfig_tdah.yaml",
    "promptfooconfig_tsa.yaml",
    "promptfooconfig_visuel.yaml",
}
ALLOWED_ROOT_KEYS = {"description", "defaultTest", "tests"}
ALLOWED_DEFAULT_TEST_KEYS = {"vars"}
ALLOWED_TEST_KEYS = {"description", "vars", "assert"}
ALLOWED_ASSERT_KEYS = {"type", "value"}
ALLOWED_ASSERT_TYPES = {"javascript", "llm-rubric"}


def nonempty_string(value) -> bool:
    return isinstance(value, str) and bool(value.strip())


def invalid_keys(mapping: dict, allowed: set[str]) -> list[str]:
    return sorted(
        (repr(key) for key in mapping if not isinstance(key, str) or key not in allowed),
        key=str,
    )


def resolve_skill_ref(config_path: Path, reference: object, label: str) -> list[str]:
    violations: list[str] = []
    if not nonempty_string(reference) or not reference.startswith("file://"):
        return [f"{label} : référence skill invalide {reference!r}"]

    resolved = (config_path.parent / reference[len("file://"):]).resolve()
    try:
        resolved.relative_to(SKILLS_DIR)
    except ValueError:
        violations.append(f"{label} : chemin hors de skills/ ({resolved})")
        return violations

    if not resolved.is_file() or resolved.name != "SKILL.md":
        violations.append(f"{label} : SKILL.md introuvable ({resolved})")
    return violations


def skill_refs(vars_block: dict) -> list[tuple[str, object]]:
    return [
        (key, value) for key, value in vars_block.items()
        if isinstance(key, str)
        and (key == "skill" or (key.startswith("skill") and key[5:].isdigit()))
    ]


def check_config(path: Path) -> tuple[list[str], int, int, int]:
    rel = path.relative_to(REPO_ROOT)
    violations: list[str] = []
    try:
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
    except (OSError, yaml.YAMLError) as exc:
        return [f"{rel} : YAML invalide ({exc})"], 0, 0, 0

    if not isinstance(data, dict):
        return [f"{rel} : la racine doit être un objet YAML"], 0, 0, 0

    unknown_root = invalid_keys(data, ALLOWED_ROOT_KEYS)
    if unknown_root:
        violations.append(f"{rel} : clés racine interdites : {', '.join(unknown_root)}")
    if not nonempty_string(data.get("description")):
        violations.append(f"{rel} : description absente ou vide")

    is_coactivation = path.name == "promptfooconfig_coactivation.yaml"
    default_vars: dict = {}
    default_test = data.get("defaultTest")
    if is_coactivation:
        if default_test is not None:
            violations.append(f"{rel} : defaultTest est interdit pour la coactivation")
    elif not isinstance(default_test, dict) or not isinstance(default_test.get("vars"), dict):
        violations.append(f"{rel} : defaultTest.vars doit être un objet")
    else:
        unknown_default = invalid_keys(default_test, ALLOWED_DEFAULT_TEST_KEYS)
        if unknown_default:
            violations.append(
                f"{rel} : clés defaultTest interdites : {', '.join(unknown_default)}"
            )
        default_vars = default_test["vars"]
        unknown_default_vars = invalid_keys(default_vars, {"skill"})
        if unknown_default_vars:
            violations.append(
                f"{rel} : clés defaultTest.vars interdites : "
                f"{', '.join(unknown_default_vars)}"
            )
        refs = skill_refs(default_vars)
        if len(refs) != 1 or refs[0][0] != "skill":
            violations.append(f"{rel} : defaultTest.vars doit contenir exactement skill")
        for key, reference in refs:
            violations.extend(resolve_skill_ref(path, reference, f"{rel} : {key}"))

    tests = data.get("tests")
    if not isinstance(tests, list):
        violations.append(f"{rel} : tests doit être une liste")
        return violations, 0, 0, 0
    if len(tests) < 6:
        violations.append(f"{rel} : au moins 6 cas sont requis")

    descriptions: set[str] = set()
    javascript_count = 0
    rubric_count = 0

    for index, test in enumerate(tests, start=1):
        label = f"{rel} : cas #{index}"
        if not isinstance(test, dict):
            violations.append(f"{label} doit être un objet")
            continue

        unknown_test = invalid_keys(test, ALLOWED_TEST_KEYS)
        if unknown_test:
            violations.append(f"{label} : clés interdites : {', '.join(unknown_test)}")

        description = test.get("description")
        if not nonempty_string(description):
            violations.append(f"{label} : description absente ou vide")
        elif description in descriptions:
            violations.append(f"{label} : description dupliquée")
        else:
            descriptions.add(description)

        vars_block = test.get("vars")
        if not isinstance(vars_block, dict):
            violations.append(f"{label} : vars doit être un objet")
            vars_block = {}
        if not nonempty_string(vars_block.get("question")):
            violations.append(f"{label} : question absente ou vide")

        refs = skill_refs(vars_block)
        allowed_vars = {"question"}
        if is_coactivation:
            allowed_vars.update(key for key, _ in refs)
        unknown_vars = invalid_keys(vars_block, allowed_vars)
        if unknown_vars:
            violations.append(f"{label} : clés vars interdites : {', '.join(unknown_vars)}")
        if is_coactivation and len(refs) < 2:
            violations.append(f"{label} : au moins deux skills sont requis")
        if not is_coactivation and refs:
            violations.append(f"{label} : le skill principal doit rester dans defaultTest.vars")
        for key, reference in refs:
            violations.extend(resolve_skill_ref(path, reference, f"{label} : {key}"))

        assertions = test.get("assert")
        if not isinstance(assertions, list) or not assertions:
            violations.append(f"{label} : assert doit être une liste non vide")
            continue

        semantic_count = 0
        for assertion_index, assertion in enumerate(assertions, start=1):
            assertion_label = f"{label}, assertion #{assertion_index}"
            if not isinstance(assertion, dict):
                violations.append(f"{assertion_label} doit être un objet")
                continue
            unknown_assertion = invalid_keys(assertion, ALLOWED_ASSERT_KEYS)
            if unknown_assertion:
                violations.append(
                    f"{assertion_label} : clés interdites : {', '.join(unknown_assertion)}"
                )
            assertion_type = assertion.get("type")
            if assertion_type not in ALLOWED_ASSERT_TYPES:
                violations.append(f"{assertion_label} : type inconnu {assertion_type!r}")
            if not nonempty_string(assertion.get("value")):
                violations.append(f"{assertion_label} : value absent ou vide")
            if assertion_type == "javascript":
                javascript_count += 1
            elif assertion_type == "llm-rubric":
                semantic_count += 1
                rubric_count += 1

        if semantic_count == 0:
            violations.append(f"{label} : au moins une assertion llm-rubric est requise")

    return violations, len(tests), javascript_count, rubric_count


def main() -> int:
    config_paths = sorted(EVAL_DIR.glob("promptfooconfig*.yaml"))
    actual_names = {path.name for path in config_paths}
    violations: list[str] = []

    missing = sorted(EXPECTED_CONFIGS - actual_names)
    unexpected = sorted(actual_names - EXPECTED_CONFIGS)
    if missing:
        violations.append(f"configs absentes : {', '.join(missing)}")
    if unexpected:
        violations.append(f"configs inattendues : {', '.join(unexpected)}")

    total_tests = total_javascript = total_rubrics = 0
    for path in config_paths:
        found, tests, javascript, rubrics = check_config(path)
        violations.extend(found)
        total_tests += tests
        total_javascript += javascript
        total_rubrics += rubrics

    if violations:
        for violation in violations:
            print(f"[FAIL] {violation}")
        return 1

    print(
        f"[OK] {len(config_paths)} banques YAML valides — {total_tests} cas, "
        f"{total_javascript} assertions JavaScript, {total_rubrics} rubriques"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
