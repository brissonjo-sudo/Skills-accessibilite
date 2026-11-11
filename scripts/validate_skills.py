#!/usr/bin/env python3
# validate_skills.py — Valide la structure et la cohérence des skills.
# Dépendance : PyYAML (voir requirements-ci.txt).
# Peut être lancé depuis la racine du repo ou depuis scripts/.

import hashlib
import re
import sys
from collections import Counter
from pathlib import Path

from _common import utf8_stdio

try:
    import yaml
except ImportError:  # message clair plutôt qu'un traceback
    print(
        "[ERREUR] PyYAML est requis : pip install -r requirements-ci.txt",
        file=sys.stderr,
    )
    sys.exit(2)

# ── Résolution de la racine du repo ─────────────────────────────────────────
SCRIPT_DIR = Path(__file__).resolve().parent
ROOT = SCRIPT_DIR.parent  # scripts/ est un niveau sous la racine
SKILLS_DIR = ROOT / "skills"

MAX_LINES = 499
MAX_DESCRIPTION = 1024
MAX_NAME = 64
# Minuscules, chiffres et tirets simples : format accepté par Claude et par Codex.
NAME_RE = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*")
RESERVED_WORDS = ("anthropic", "claude")
# Fichiers créés par le système, déjà ignorés par Git.
OS_JUNK = {".DS_Store", "Thumbs.db", "desktop.ini"}
# Seules clés acceptées à l'import d'un skill dans claude.ai : toute autre clé
# y provoque un refus.
ALLOWED_KEYS = {
    "name", "description", "license", "compatibility", "metadata", "allowed-tools",
}

# ── Helpers ──────────────────────────────────────────────────────────────────

def split_frontmatter(lines: list[str]) -> tuple[list[str] | None, str | None]:
    """
    Isole les lignes du frontmatter YAML.
    Retourne (lignes, None) ou (None, message d'erreur).
    """
    i = 0
    while i < len(lines) and lines[i].strip() == "":
        i += 1
    if i >= len(lines) or lines[i].strip() != "---":
        return None, "frontmatter YAML introuvable (première ligne non vide doit être '---')"
    for j in range(i + 1, len(lines)):
        if lines[j].rstrip() == "---":
            return lines[i + 1:j], None
    return None, "frontmatter non fermé : ligne '---' fermante absente"


def find_yaml_breaking_scalars(fm_lines: list[str]) -> list[tuple[str, int, str]]:
    """
    Repère la cause la plus fréquente d'un frontmatter invalide.

    En YAML, un ': ' (deux-points suivi d'un espace) dans un scalaire *plain*
    (ni quoté, ni bloc '|' / '>') est lu comme un séparateur clé/valeur : le
    document devient invalide ('mapping values are not allowed here').

    Le verdict vient du parseur YAML ; cette fonction ne sert qu'à produire un
    message qui pointe la colonne fautive.

    Retourne une liste de (clé, colonne 1-based, extrait fautif).
    """
    problems: list[tuple[str, int, str]] = []
    for line in fm_lines:
        stripped = line.rstrip("\n").rstrip()
        key, sep, value = stripped.partition(":")
        if sep and not key.startswith(" ") and key.strip():
            v = value.strip()
            quoted = (len(v) >= 2 and v[0] == v[-1] and v[0] in "\"'")
            block = v.startswith(("|", ">"))
            if v and not quoted and not block:
                pos = v.find(": ")
                if pos != -1:
                    col = len(key) + 1 + (len(value) - len(value.lstrip())) + pos + 1
                    start = max(0, pos - 40)
                    problems.append((key.strip(), col, v[start:pos + 20]))
    return problems


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


def check_frontmatter(fm_lines: list[str], dir_name: str) -> list[str]:
    """Valide le frontmatter tel qu'un parseur YAML strict le lit."""
    errors: list[str] = []
    try:
        data = yaml.safe_load("".join(fm_lines))
    except yaml.YAMLError as exc:
        detail = " ".join(str(exc).split())
        errors.append(f"frontmatter invalide en YAML strict : {detail}")
        for key, col, extrait in find_yaml_breaking_scalars(fm_lines):
            errors.append(
                f"cause probable : ': ' dans la valeur non quotée de '{key}' "
                f"(colonne {col}). Remplacer par ' — ' ou ' ; ', ou quoter la "
                f"valeur. Extrait : …{extrait}…"
            )
        return errors

    if not isinstance(data, dict):
        return ["frontmatter : la racine doit être un objet YAML (clé: valeur)"]

    # YAML valide mais piégeux : ' #' ouvre un commentaire dans une valeur non
    # quotée, et tout ce qui suit disparaît sans erreur.
    for line in fm_lines:
        key, sep, value = line.rstrip().partition(":")
        v = value.strip()
        plain = v and v[0] not in "\"'|>"
        if sep and key.strip() and not key.startswith(" ") and plain and " #" in v:
            errors.append(
                f"' #' dans la valeur non quotée de '{key.strip()}' : YAML y voit "
                "un commentaire et ignore la suite. Quoter la valeur ou retirer le '#'."
            )

    unknown = sorted(str(key) for key in data if key not in ALLOWED_KEYS)
    if unknown:
        errors.append(
            f"clés de frontmatter non acceptées : {', '.join(unknown)} "
            f"(autorisées : {', '.join(sorted(ALLOWED_KEYS))})"
        )

    # Champ 'name'
    name = data.get("name")
    if name is None:
        errors.append("champ 'name' absent du frontmatter")
    elif not isinstance(name, str):
        errors.append(f"champ 'name' : chaîne attendue, reçu {type(name).__name__}")
    else:
        if name != dir_name:
            errors.append(
                f"champ 'name' ({name!r}) différent du nom du dossier ({dir_name!r})"
            )
        if len(name) > MAX_NAME or not NAME_RE.fullmatch(name):
            errors.append(
                f"champ 'name' ({name!r}) hors format : minuscules, chiffres et "
                f"tirets simples, {MAX_NAME} caractères au plus"
            )
        reserved = [word for word in RESERVED_WORDS if word in name]
        if reserved:
            errors.append(
                f"champ 'name' ({name!r}) contient un mot réservé : {', '.join(reserved)}"
            )

    # Champ 'description'
    description = data.get("description")
    if description is None:
        errors.append("champ 'description' absent du frontmatter")
    elif not isinstance(description, str):
        errors.append(
            f"champ 'description' : chaîne attendue, reçu {type(description).__name__}"
        )
    else:
        if not description.strip():
            errors.append("champ 'description' vide")
        if len(description) > MAX_DESCRIPTION:
            errors.append(
                f"'description' trop longue : {len(description)} caractères "
                f"(max {MAX_DESCRIPTION})"
            )
        if "<" in description or ">" in description:
            errors.append("'description' ne doit contenir ni '<' ni '>'")

    return errors


# ── Validation par skill ──────────────────────────────────────────────────────

def validate_skill(skill_dir: Path) -> tuple[list[str], list[str] | None]:
    """
    Valide un dossier de skill.
    Retourne (erreurs, bloc de préséance ou None).
    """
    errors: list[str] = []
    skill_md = skill_dir / "SKILL.md"

    if not skill_md.is_file():
        return ["SKILL.md absent"], None

    # Un skill tient en un seul fichier : tout autre fichier partirait dans la
    # distribution sans avoir été évalué.
    extra = sorted(
        item.name for item in skill_dir.iterdir()
        if item.name != "SKILL.md" and item.name not in OS_JUNK
    )
    if extra:
        errors.append(f"fichiers en trop dans le dossier du skill : {', '.join(extra)}")

    try:
        raw = skill_md.read_text(encoding="utf-8")
    except UnicodeDecodeError as exc:
        return [f"SKILL.md n'est pas en UTF-8 ({exc})"], None

    if raw.startswith("﻿"):
        errors.append("BOM UTF-8 en tête de fichier : à retirer")
        raw = raw.lstrip("﻿")

    lines = raw.splitlines(keepends=True)

    if len(lines) > MAX_LINES:
        errors.append(f"fichier trop long : {len(lines)} lignes (max {MAX_LINES})")

    fm_lines, fm_error = split_frontmatter(lines)
    if fm_lines is None:
        errors.append(fm_error)
    else:
        errors.extend(check_frontmatter(fm_lines, skill_dir.name))

    block = extract_precedence_block(lines)
    if block is None:
        errors.append("bloc '## Ordre de préséance' absent")

    return errors, block


# ── Programme principal ───────────────────────────────────────────────────────

def main() -> int:
    utf8_stdio()

    if not SKILLS_DIR.is_dir():
        print(f"[ERREUR] Dossier skills/ introuvable : {SKILLS_DIR}", file=sys.stderr)
        return 1

    skill_dirs = sorted(p for p in SKILLS_DIR.iterdir() if p.is_dir())

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
        errors, block = validate_skill(skill_dir)
        if block is not None:
            precedence_hashes[name] = block_hash(block)

        if not errors:
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
        manquants = [d.name for d in skill_dirs if d.name not in precedence_hashes]
        print(f"[ERREUR] Bloc absent dans : {', '.join(manquants)}")
        global_ok = False
    else:
        unique_hashes = set(precedence_hashes.values())
        if len(unique_hashes) == 1:
            print(
                f"[OK]     Tous les blocs sont identiques "
                f"(sha256={next(iter(unique_hashes))[:12]}…)"
            )
        else:
            global_ok = False
            # Le hash majoritaire sert de référence pour désigner les écarts.
            reference_hash = Counter(precedence_hashes.values()).most_common(1)[0][0]
            divergents = [
                sk for sk, h in precedence_hashes.items() if h != reference_hash
            ]
            print(
                f"[ERREUR] Blocs non identiques — skills divergents : "
                f"{', '.join(divergents)}"
            )
            for sk, h in sorted(precedence_hashes.items()):
                marker = "<- référence" if h == reference_hash else "<- DIFFÉRENT"
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
