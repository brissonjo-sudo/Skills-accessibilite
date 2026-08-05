#!/usr/bin/env python3
"""Check that file:// paths in eval/promptfooconfig*.yaml exist."""

import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent
EVAL_DIR = REPO_ROOT / 'eval'

# Match skill:, skill1:, skill2: values starting with file://
SKILL_KEY_RE = re.compile(r'^\s*skill\d*:\s*"?(file://[^\s"]+)"?\s*$')


def check_config(yaml_path):
    """Check a single promptfooconfig*.yaml. Returns list of violation strings."""
    violations = []
    rel = yaml_path.relative_to(REPO_ROOT)
    try:
        text = yaml_path.read_text(encoding='utf-8')
    except OSError as e:
        violations.append(f"[FAIL] {rel} : impossible de lire le fichier ({e})")
        return violations

    for line in text.splitlines():
        m = SKILL_KEY_RE.match(line)
        if not m:
            continue
        file_ref = m.group(1)  # e.g. file://../skills/foo/SKILL.md
        rel_path = file_ref[len('file://'):]  # strip file://
        # Resolve relative to the yaml file's directory
        resolved = (yaml_path.parent / rel_path).resolve()
        if not resolved.exists():
            # Show path relative to repo root for readability
            try:
                display = resolved.relative_to(REPO_ROOT)
            except ValueError:
                display = resolved
            violations.append(f"[FAIL] {rel} : chemin introuvable {display}")

    return violations


def main():
    config_files = sorted(EVAL_DIR.glob('promptfooconfig*.yaml'))
    if not config_files:
        print("[WARN] Aucun fichier eval/promptfooconfig*.yaml trouvé")
        sys.exit(0)

    all_violations = []
    for path in config_files:
        all_violations.extend(check_config(path))

    if all_violations:
        for v in all_violations:
            print(v)
        sys.exit(1)
    else:
        print(f"[OK] {len(config_files)} configs eval valides")
        sys.exit(0)


if __name__ == '__main__':
    main()
