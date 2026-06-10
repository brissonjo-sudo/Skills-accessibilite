#!/usr/bin/env python3
"""Check frontmatter of all skills/*/SKILL.md files."""

import re
import sys
from pathlib import Path

NAME_REGEX = re.compile(r'^[a-z0-9-]+$')
NAME_MAX = 64
DESCRIPTION_MAX = 1024

REPO_ROOT = Path(__file__).parent.parent


def extract_frontmatter(text):
    """Extract YAML frontmatter from markdown. Returns dict or None."""
    lines = text.splitlines()
    if not lines or lines[0].strip() != '---':
        return None
    end = None
    for i, line in enumerate(lines[1:], start=1):
        if line.strip() == '---':
            end = i
            break
    if end is None:
        return None
    fm_lines = lines[1:end]
    result = {}
    for line in fm_lines:
        if ':' in line:
            key, _, value = line.partition(':')
            result[key.strip()] = value.strip()
    return result


def check_skill(path):
    """Check a single SKILL.md. Returns list of violation strings."""
    violations = []
    rel = path.relative_to(REPO_ROOT)
    try:
        text = path.read_text(encoding='utf-8')
    except OSError as e:
        violations.append(f"[FAIL] {rel} : impossible de lire le fichier ({e})")
        return violations

    fm = extract_frontmatter(text)
    if fm is None:
        violations.append(f"[FAIL] {rel} : frontmatter YAML absent ou malformé")
        return violations

    # Check name
    if 'name' not in fm or not fm['name']:
        violations.append(f"[FAIL] {rel} : champ 'name' manquant")
    else:
        name = fm['name']
        if len(name) > NAME_MAX:
            violations.append(
                f"[FAIL] {rel} : name trop long ({len(name)} chars, max {NAME_MAX})"
            )
        if not NAME_REGEX.match(name):
            violations.append(
                f"[FAIL] {rel} : name invalide '{name}' (doit correspondre à ^[a-z0-9-]+$)"
            )

    # Check description
    if 'description' not in fm or not fm['description']:
        violations.append(f"[FAIL] {rel} : champ 'description' manquant")
    else:
        desc = fm['description']
        if len(desc) > DESCRIPTION_MAX:
            violations.append(
                f"[FAIL] {rel} : description trop longue ({len(desc)} chars, max {DESCRIPTION_MAX})"
            )

    return violations


def main():
    skill_files = sorted(REPO_ROOT.glob('skills/*/SKILL.md'))
    if not skill_files:
        print("[WARN] Aucun fichier skills/*/SKILL.md trouvé")
        sys.exit(0)

    all_violations = []
    for path in skill_files:
        all_violations.extend(check_skill(path))

    if all_violations:
        for v in all_violations:
            print(v)
        sys.exit(1)
    else:
        print(f"[OK] {len(skill_files)} skills valides")
        sys.exit(0)


if __name__ == '__main__':
    main()
