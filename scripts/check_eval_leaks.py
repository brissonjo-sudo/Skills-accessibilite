#!/usr/bin/env python3
# check_eval_leaks.py — Détecte les questions de test recopiées du skill évalué.
# Dépendance : PyYAML (voir requirements-ci.txt).
# Codes de sortie : 0 = conforme, 1 = recopie détectée, 2 = banque illisible.
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
# Les seuils portent donc sur la part de la QUESTION recouverte par le skill.
#
# Deux mesures complémentaires
# ----------------------------
# 1. La plus longue sous-chaîne commune : attrape la recopie d'un seul tenant.
# 2. L'alignement mot à mot avec chaque ligne du skill : attrape la recopie
#    retouchée (un mot remplacé au milieu), que la première mesure laisse passer.
#    La comparaison se fait ligne par ligne pour ne pas confondre une recopie
#    avec une question qui réunit deux phrases de déclenchement documentées.
#
# Limite connue : une question assemblée à partir de fragments pris à des
# endroits différents du skill n'est pas détectée.

import sys
import unicodedata
from difflib import SequenceMatcher
from pathlib import Path

import yaml

from _common import utf8_stdio

SCRIPT_DIR = Path(__file__).resolve().parent
ROOT = SCRIPT_DIR.parent

# Part de la question devant figurer d'un seul tenant dans le skill.
MAX_COVERAGE = 0.75
# Longueur minimale d'une sous-chaîne commune prise en compte (caractères normalisés).
MIN_LCS = 25
# Part des mots de la question pouvant s'aligner, dans l'ordre, sur une même
# ligne du skill. Seules les suites d'au moins MIN_RUN mots comptent : les mots
# isolés (« de », « la ») ne prouvent rien.
MAX_LINE_COVERAGE = 0.8
MIN_RUN = 2
# En dessous, une question est trop courte pour que la mesure ait un sens.
MIN_QUESTION_WORDS = 5


class BankError(Exception):
    """Banque de cas illisible ou incomplète."""


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


def line_coverage(question_words: list[str], skill_lines: list[list[str]]) -> float:
    """Meilleure part des mots de la question alignés sur une seule ligne du skill."""
    if len(question_words) < MIN_QUESTION_WORDS:
        return 0.0
    best = 0
    for line_words in skill_lines:
        matcher = SequenceMatcher(None, question_words, line_words, autojunk=False)
        matched = sum(
            block.size for block in matcher.get_matching_blocks() if block.size >= MIN_RUN
        )
        best = max(best, matched)
    return best / len(question_words)


def iter_cases(config: Path):
    """Extrait (question, [chemins de skill]) d'une banque YAML."""
    try:
        data = yaml.safe_load(config.read_text(encoding="utf-8"))
    except (OSError, yaml.YAMLError) as exc:
        detail = " ".join(str(exc).split())
        raise BankError(f"{config.name} : YAML illisible ({detail})") from exc
    if not isinstance(data, dict) or not isinstance(data.get("tests"), list):
        raise BankError(f"{config.name} : liste `tests` absente")

    def refs(vars_block: dict) -> list[str]:
        paths = []
        for key, value in vars_block.items():
            if (key == "skill" or (key.startswith("skill") and key[5:].isdigit())) \
                    and isinstance(value, str) and value.startswith("file://"):
                paths.append(str((config.parent / value[len("file://"):]).resolve()))
        return paths

    default_test = data.get("defaultTest")
    default_vars = default_test.get("vars") if isinstance(default_test, dict) else None
    default_skills = refs(default_vars) if isinstance(default_vars, dict) else []
    cases: list[tuple[str, list[str]]] = []
    for index, test in enumerate(data["tests"], start=1):
        vars_block = test.get("vars") if isinstance(test, dict) else None
        question = vars_block.get("question") if isinstance(vars_block, dict) else None
        if not isinstance(question, str) or not question.strip():
            raise BankError(f"{config.name} : cas #{index} sans `vars.question`")
        cases.append((question, refs(vars_block) or default_skills))
    return cases


def main() -> int:
    utf8_stdio()
    configs = sorted((ROOT / "eval").glob("promptfooconfig*.yaml"))
    if not configs:
        print("[ERREUR] Aucun fichier eval/promptfooconfig*.yaml trouvé")
        return 2

    skill_cache: dict[str, tuple[str, list[list[str]]]] = {}
    leaks: list[str] = []
    n_cases = 0

    print("=" * 60)
    print("Détection des questions de test recopiées des skills")
    print("=" * 60)

    for config in configs:
        try:
            cases = iter_cases(config)
        except BankError as exc:
            print(f"[ERREUR] {exc}")
            return 2
        for question, skills in cases:
            n_cases += 1
            q_norm = normalize(question)
            if not q_norm:
                continue
            q_words = q_norm.split()
            for skill_path in skills:
                if skill_path not in skill_cache:
                    p = Path(skill_path)
                    if not p.exists():
                        print(f"[ERREUR] skill introuvable : {skill_path}")
                        return 2
                    text = p.read_text(encoding="utf-8")
                    lines = [normalize(line).split() for line in text.splitlines()]
                    skill_cache[skill_path] = (
                        normalize(text),
                        [words for words in lines if len(words) >= MIN_RUN],
                    )
                s_norm, s_lines = skill_cache[skill_path]
                skill_label = f"{Path(skill_path).parent.name}/SKILL.md"

                frag = longest_common_substring(q_norm, s_norm, MIN_LCS)
                coverage = len(frag) / len(q_norm) if frag else 0.0
                aligned = line_coverage(q_words, s_lines)
                if coverage >= MAX_COVERAGE:
                    leaks.append(
                        f"{config.name} :: {question[:60]}…\n"
                        f"         {coverage:.0%} de la question figure d'un seul "
                        f"tenant dans {skill_label}\n"
                        f"         extrait : « {frag[:80]}… »"
                    )
                elif aligned >= MAX_LINE_COVERAGE:
                    leaks.append(
                        f"{config.name} :: {question[:60]}…\n"
                        f"         {aligned:.0%} des mots de la question s'alignent "
                        f"sur une même ligne de {skill_label}"
                    )

    print(f"cas analysés : {n_cases}")
    if leaks:
        print(f"\n[ERREUR] {len(leaks)} question(s) recopiée(s) du skill évalué :\n")
        for leak in leaks:
            print(f"  • {leak}\n")
        print("Réécrire la question : garder la phrase de déclenchement, changer le sujet.")
        return 1

    print(
        f"[OK]     aucune question ne dépasse {MAX_COVERAGE:.0%} de recouvrement "
        f"continu ni {MAX_LINE_COVERAGE:.0%} d'alignement sur une ligne du skill"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
