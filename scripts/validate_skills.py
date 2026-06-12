#!/usr/bin/env python3
# validate_skills.py — Valide la structure et la cohérence des skills.
# Stdlib uniquement (pas de dépendance externe).
# Peut être lancé depuis la racine du repo ou depuis scripts/.

import hashlib
import os
import sys
from pathlib import Path

# ── Résolution de la racine du repo ─────────────────────────────────────────
SCRIPT_DIR = Path(__file__).resolve().parent
ROOT = SCRIPT_DIR.parent  # scripts/ est un niveau sous la racine
SKILLS_DIR = ROOT / "skills"

# ── Helpers ──────────────────────────────────────────────────────────────────

def parse_frontmatter(lines: list[str]) -> dict[str, str] | None:
    """
    Parse le frontmatter YAML d'un fichier Markdown.
    Attend que la 1re ligne non vide soit '---', puis lit jusqu'au '---' suivant.
    Retourne un dict clé→valeur (split sur le premier ':') ou None si absent.
    """
    i = 0
    # Sauter les lignes vides initiales
    while i < len(lines) and lines[i].strip() == "":
        i += 1
    if i >= len(lines) or lines[i].strip() != "---":
        return None
    i += 1
    fm: dict[str, str] = {}
    while i < len(lines):
        stripped = lines[i].rstrip("\n").rstrip()
        if stripped == "---":
            break
        if ":" in stripped:
            key, _, value = stripped.partition(":")
            fm[key.strip()] = value.strip()
        i += 1
    return fm


def extract_precedence_block(lines: list[str]) -> list[str] | None:
    """
    Extrait le contenu du bloc '## Ordre de préséance' (toutes variantes de titre
    commençant par cette chaîne).
    Retourne les lignes ENTRE l'en-tête (exclu) et le prochain '## ' (exclu),
    ou None si le bloc est absent.
    Équivalent : awk '/^## Ordre de préséance/{f=1;next} f&&/^## /{f=0} f'
    """
    in_block = False
    block: list[str] = []
    for line in lines:
        if line.startswith("## Ordre de préséance"):
            in_block = True
            continue
        if in_block:
            if line.startswith("## "):
                break
            block.append(line)
    return block if in_block else None


def block_hash(block: list[str]) -> str:
    """Calcule le hash SHA-256 du contenu d'un bloc (liste de lignes)."""
    content = "".join(block).encode("utf-8")
    return hashlib.sha256(content).hexdigest()


# ── Validation par skill ──────────────────────────────────────────────────────

def validate_skill(skill_dir: Path) -> tuple[bool, list[str]]:
    """
    Valide un dossier de skill.
    Retourne (succès: bool, messages: list[str]).
    """
    name = skill_dir.name
    errors: list[str] = []
    skill_md = skill_dir / "SKILL.md"

    # Présence de SKILL.md
    if not skill_md.exists():
        errors.append(f"SKILL.md absent")
        return False, errors

    with open(skill_md, encoding="utf-8") as fh:
        lines = fh.readlines()

    # Nombre de lignes
    line_count = len(lines)
    if line_count >= 500:
        errors.append(f"fichier trop long : {line_count} lignes (max 499)")

    # Frontmatter
    fm = parse_frontmatter(lines)
    if fm is None:
        errors.append("frontmatter YAML introuvable (première ligne non vide doit être '---')")
        return False, errors

    # Champ 'name'
    if "name" not in fm:
        errors.append("champ 'name' absent du frontmatter")
    elif fm["name"] != name:
        errors.append(
            f"champ 'name' ({fm['name']!r}) différent du nom du dossier ({name!r})"
        )

    # Champ 'description'
    if "description" not in fm:
        errors.append("champ 'description' absent du frontmatter")
    else:
        desc_len = len(fm["description"])
        if desc_len > 1024:
            errors.append(
                f"'description' trop longue : {desc_len} caractères (max 1024)"
            )

    ok = len(errors) == 0
    return ok, errors


# ── Programme principal ───────────────────────────────────────────────────────

def main() -> int:
    if not SKILLS_DIR.is_dir():
        print(f"[ERREUR] Dossier skills/ introuvable : {SKILLS_DIR}", file=sys.stderr)
        return 1

    skill_dirs = sorted(
        p for p in SKILLS_DIR.iterdir() if p.is_dir()
    )

    if not skill_dirs:
        print("[ERREUR] Aucun sous-dossier trouvé dans skills/", file=sys.stderr)
        return 1

    global_ok = True
    precedence_hashes: dict[str, str] = {}  # nom_skill → hash du bloc

    print("=" * 60)
    print("Validation des skills")
    print("=" * 60)

    for skill_dir in skill_dirs:
        name = skill_dir.name
        ok, errors = validate_skill(skill_dir)

        # Extraction du bloc Ordre de préséance (indépendante des erreurs ci-dessus)
        skill_md = skill_dir / "SKILL.md"
        if skill_md.exists():
            with open(skill_md, encoding="utf-8") as fh:
                lines = fh.readlines()
            block = extract_precedence_block(lines)
            if block is None:
                errors.append("bloc '## Ordre de préséance' absent")
                ok = False
            else:
                precedence_hashes[name] = block_hash(block)

        if ok:
            print(f"[OK]     {name}")
        else:
            global_ok = False
            print(f"[ERREUR] {name}")
            for msg in errors:
                print(f"         • {msg}")

    # ── Vérification d'identité des blocs Ordre de préséance ────────────────
    print()
    print("-" * 60)
    print("Vérification : blocs 'Ordre de préséance' identiques")
    print("-" * 60)

    if len(precedence_hashes) < len(skill_dirs):
        manquants = [
            d.name for d in skill_dirs if d.name not in precedence_hashes
        ]
        print(
            f"[ERREUR] Bloc absent dans : {', '.join(manquants)}"
        )
        global_ok = False
    else:
        # Tous les skills ont un bloc ; vérifier l'unicité du hash
        unique_hashes = set(precedence_hashes.values())
        if len(unique_hashes) == 1:
            print(
                f"[OK]     Tous les blocs sont identiques "
                f"(sha256={next(iter(unique_hashes))[:12]}…)"
            )
        else:
            global_ok = False
            # Trouver le hash majoritaire (référence) pour identifier les outliers
            from collections import Counter
            hash_counts = Counter(precedence_hashes.values())
            reference_hash = hash_counts.most_common(1)[0][0]
            divergents = [
                sk for sk, h in precedence_hashes.items() if h != reference_hash
            ]
            print(
                f"[ERREUR] Blocs non identiques — skills divergents : "
                f"{', '.join(divergents)}"
            )
            for sk, h in sorted(precedence_hashes.items()):
                marker = "← référence" if h == reference_hash else "← DIFFÉRENT"
                print(f"         {sk:<55} sha256={h[:12]}… {marker}")

    # ── Récapitulatif ────────────────────────────────────────────────────────
    print()
    print("=" * 60)
    if global_ok:
        print("RÉCAPITULATIF : tous les contrôles sont passés. [OK]")
    else:
        print("RÉCAPITULATIF : au moins un contrôle a échoué. [ÉCHEC]")
    print("=" * 60)

    return 0 if global_ok else 1


if __name__ == "__main__":
    sys.exit(main())
