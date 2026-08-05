#!/usr/bin/env python3
# check_eval_leaks.py — Détecte les questions de test recopiées du skill évalué.
# Stdlib uniquement (pas de dépendance externe : le CI n'installe rien).
#
# Pourquoi ce contrôle existe
# ---------------------------
# Une question de test dont le texte figure déjà dans le SKILL.md ne mesure plus
# l'effet du skill : le modèle récite la réponse-type qu'il a sous les yeux. Le
# benchmark du 2026-08-05 a montré un cas où la réponse produite était
# byte-identique à l'exemple du skill.
#
# Ce qui n'est PAS une fuite : partager la phrase de déclenchement documentée
# (« je suis non-voyant », « mode HDC »). C'est nécessaire pour activer le skill.
# Le seuil porte donc sur la part de la QUESTION recouverte par le skill.

import re
import sys
import unicodedata
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
ROOT = SCRIPT_DIR.parent

# Part de la question devant figurer dans le skill pour parler de recopie.
MAX_COVERAGE = 0.75
# Longueur minimale d'une sous-chaîne commune prise en compte (caractères normalisés).
MIN_LCS = 25


def normalize(text: str) -> str:
    """Minuscules, accents supprimés, ponctuation -> espace, espaces compressés."""
    out = []
    prev_space = True
    for ch in text:
        base = "".join(
            c for c in unicodedata.normalize("NFD", ch) if not unicodedata.combining(c)
        ).lower()
        for c in base:
            if c.isalnum():
                out.append(c)
                prev_space = False
            elif not prev_space:
                out.append(" ")
                prev_space = True
    return "".join(out).strip()


def longest_common_substring(needle: str, haystack: str, floor: int) -> str | None:
    """Plus longue sous-chaîne de `needle` présente dans `haystack` (>= floor)."""
    for length in range(len(needle), floor - 1, -1):
        for start in range(0, len(needle) - length + 1):
            frag = needle[start:start + length]
            if frag in haystack:
                return frag
    return None


def iter_cases(config: Path):
    """Extrait (question, [chemins de skill]) de chaque cas d'une config promptfoo.

    Parsing volontairement littéral (pas de PyYAML) : on ne lit que les lignes
    `question:` et `skill*: "file://..."`, ce que la structure des configs permet.
    """
    default_skills: list[str] = []
    cases: list[tuple[str, list[str]]] = []
    current_skills: list[str] = []
    question: str | None = None
    in_tests = False

    for raw in config.read_text(encoding="utf-8").splitlines():
        if re.match(r"^tests:\s*$", raw):
            in_tests = True
            continue

        m_skill = re.match(r'^\s*skill\d*:\s*"?(file://[^\s"]+)"?\s*$', raw)
        if m_skill:
            rel = (config.parent / m_skill.group(1)[len("file://"):]).resolve()
            (current_skills if in_tests else default_skills).append(str(rel))
            continue

        if re.match(r"^\s*-\s+description:", raw):
            if question:
                cases.append((question, current_skills or default_skills))
            question, current_skills = None, []
            continue

        m_q = re.match(r'^\s*question:\s*"(.*)"\s*$', raw)
        if m_q:
            question = m_q.group(1).replace('\\"', '"')

    if question:
        cases.append((question, current_skills or default_skills))
    return cases


def main() -> int:
    configs = sorted((ROOT / "eval").glob("promptfooconfig*.yaml"))
    if not configs:
        print("[WARN] Aucun fichier eval/promptfooconfig*.yaml trouvé")
        return 0

    skill_cache: dict[str, str] = {}
    leaks: list[str] = []
    n_cases = 0

    print("=" * 60)
    print("Détection des questions de test recopiées des skills")
    print("=" * 60)

    for config in configs:
        for question, skills in iter_cases(config):
            n_cases += 1
            q_norm = normalize(question)
            if not q_norm:
                continue
            for skill_path in skills:
                if skill_path not in skill_cache:
                    p = Path(skill_path)
                    if not p.exists():
                        print(f"[ERREUR] skill introuvable : {skill_path}")
                        return 1
                    skill_cache[skill_path] = normalize(p.read_text(encoding="utf-8"))

                frag = longest_common_substring(q_norm, skill_cache[skill_path], MIN_LCS)
                if not frag:
                    continue
                coverage = len(frag) / len(q_norm)
                if coverage >= MAX_COVERAGE:
                    leaks.append(
                        f"{config.name} :: {question[:60]}…\n"
                        f"         {coverage:.0%} de la question figure dans "
                        f"{Path(skill_path).parent.name}/SKILL.md\n"
                        f"         extrait : « {frag[:80]}… »"
                    )

    print(f"cas analysés : {n_cases}")
    if leaks:
        print(f"\n[ERREUR] {len(leaks)} question(s) recopiée(s) du skill évalué :\n")
        for leak in leaks:
            print(f"  • {leak}\n")
        print("Réécrire la question : garder la phrase de déclenchement, changer le sujet.")
        return 1

    print(f"[OK]     aucune question ne dépasse {MAX_COVERAGE:.0%} de recouvrement")
    return 0


if __name__ == "__main__":
    sys.exit(main())
