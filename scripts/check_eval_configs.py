#!/usr/bin/env python3
"""Valide la syntaxe et le schéma des banques de cas YAML.

Vérifie aussi que chaque skill a exactement une banque dédiée, et que la
syntaxe des assertions JavaScript est correcte (si `node` est disponible).
"""

import argparse
import json
import shutil
import subprocess
import sys
from pathlib import Path

import yaml

from _common import utf8_stdio

REPO_ROOT = Path(__file__).resolve().parent.parent
EVAL_DIR = REPO_ROOT / "eval"
SKILLS_DIR = (REPO_ROOT / "skills").resolve()
COACTIVATION_CONFIG = "promptfooconfig_coactivation.yaml"
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


class ConfigReport:
    """Résultat du contrôle d'une banque."""

    def __init__(self) -> None:
        self.violations: list[str] = []
        self.tests = 0
        self.javascript = 0
        self.rubrics = 0
        self.default_skill: str | None = None  # skill évalué par la banque
        self.js_assertions: list[tuple[str, str]] = []  # (étiquette, code)


def skill_name_of(config_path: Path, reference: object) -> str | None:
    """Nom du skill visé par une référence `file://…/skills/<nom>/SKILL.md`."""
    if not nonempty_string(reference) or not reference.startswith("file://"):
        return None
    resolved = (config_path.parent / reference[len("file://"):]).resolve()
    try:
        parts = resolved.relative_to(SKILLS_DIR).parts
    except ValueError:
        return None
    return parts[0] if len(parts) == 2 and parts[1] == "SKILL.md" else None


def check_config(path: Path) -> ConfigReport:
    report = ConfigReport()
    rel = path.relative_to(REPO_ROOT).as_posix()
    violations = report.violations
    try:
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
    except (OSError, yaml.YAMLError) as exc:
        violations.append(f"{rel} : YAML invalide ({' '.join(str(exc).split())})")
        return report

    if not isinstance(data, dict):
        violations.append(f"{rel} : la racine doit être un objet YAML")
        return report

    unknown_root = invalid_keys(data, ALLOWED_ROOT_KEYS)
    if unknown_root:
        violations.append(f"{rel} : clés racine interdites : {', '.join(unknown_root)}")
    if not nonempty_string(data.get("description")):
        violations.append(f"{rel} : description absente ou vide")

    is_coactivation = path.name == COACTIVATION_CONFIG
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
            report.default_skill = skill_name_of(path, reference)

    tests = data.get("tests")
    if not isinstance(tests, list):
        violations.append(f"{rel} : tests doit être une liste")
        return report
    if len(tests) < 6:
        violations.append(f"{rel} : au moins 6 cas sont requis")

    report.tests = len(tests)
    descriptions: set[str] = set()

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
                report.javascript += 1
                if nonempty_string(assertion.get("value")):
                    report.js_assertions.append((assertion_label, assertion["value"]))
            elif assertion_type == "llm-rubric":
                semantic_count += 1
                report.rubrics += 1

        if semantic_count == 0:
            violations.append(f"{label} : au moins une assertion llm-rubric est requise")

    return report


# Compile chaque assertion sans l'exécuter : d'abord comme expression, puis
# comme corps de fonction (assertions sur plusieurs lignes avec `return`).
NODE_SYNTAX_CHECK = r"""
const items = JSON.parse(require('fs').readFileSync(0, 'utf8'));
const errors = [];
for (const [label, code] of items) {
  try { new Function('output', 'context', 'return (' + code + '\n);'); continue; } catch (e) {}
  try { new Function('output', 'context', code); } catch (e) { errors.push([label, String(e.message)]); }
}
process.stdout.write(JSON.stringify(errors));
"""


def check_javascript_syntax(assertions: list[tuple[str, str]]) -> list[str] | None:
    """Retourne les erreurs de syntaxe, ou None si `node` est indisponible."""
    node = shutil.which("node")
    if node is None:
        return None
    result = subprocess.run(
        [node, "-e", NODE_SYNTAX_CHECK], input=json.dumps(assertions),
        capture_output=True, text=True, encoding="utf-8", check=True,
    )
    return [
        f"{label} : JavaScript invalide ({message})"
        for label, message in json.loads(result.stdout)
    ]


def check_bank_coverage(reports: dict[str, ConfigReport]) -> list[str]:
    """Chaque skill a exactement une banque dédiée, plus la banque de coactivation."""
    violations: list[str] = []
    if COACTIVATION_CONFIG not in reports:
        violations.append(f"banque absente : {COACTIVATION_CONFIG}")

    banks_by_skill: dict[str, list[str]] = {}
    for name, report in sorted(reports.items()):
        if name != COACTIVATION_CONFIG and report.default_skill:
            banks_by_skill.setdefault(report.default_skill, []).append(name)

    skills = sorted(
        item.name for item in SKILLS_DIR.iterdir()
        if item.is_dir() and (item / "SKILL.md").is_file()
    )
    for skill in skills:
        banks = banks_by_skill.get(skill, [])
        if not banks:
            violations.append(
                f"aucune banque de cas ne vise le skill {skill} "
                "(defaultTest.vars.skill)"
            )
        elif len(banks) > 1:
            violations.append(
                f"plusieurs banques visent le skill {skill} : {', '.join(banks)}"
            )
    return violations


def main() -> int:
    utf8_stdio()
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--require-node", action="store_true",
        help="échouer si node est absent (syntaxe JavaScript non vérifiable)",
    )
    args = parser.parse_args()

    config_paths = sorted(EVAL_DIR.glob("promptfooconfig*.yaml"))
    reports = {path.name: check_config(path) for path in config_paths}

    violations: list[str] = []
    for report in reports.values():
        violations.extend(report.violations)
    violations.extend(check_bank_coverage(reports))

    js_assertions = [item for report in reports.values() for item in report.js_assertions]
    js_errors = check_javascript_syntax(js_assertions)
    if js_errors is None:
        message = "node introuvable : syntaxe des assertions JavaScript non vérifiée"
        if args.require_node:
            violations.append(message)
        else:
            print(f"[WARN] {message}")
    else:
        violations.extend(js_errors)

    if violations:
        for violation in violations:
            print(f"[FAIL] {violation}")
        return 1

    print(
        f"[OK] {len(reports)} banques YAML valides — "
        f"{sum(r.tests for r in reports.values())} cas, "
        f"{sum(r.javascript for r in reports.values())} assertions JavaScript, "
        f"{sum(r.rubrics for r in reports.values())} rubriques"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
