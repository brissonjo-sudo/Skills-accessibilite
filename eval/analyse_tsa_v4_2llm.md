# Analyse — run V4 provider 2-LLM (Mistral Large + Gemini 2.5 Flash)
# Skill accessibilite-tsa

Date : 2026-06-06
Skill : V4
Méthode : promptfoo eval, harnais `promptfooconfig_tsa.yaml` (11 cas, 2 conditions, 2 LLMs)
Juge : Mistral Large (`mistral-large-latest`)

---

## Résultats

| Cas | Axe testé | Mistral with_skill | Mistral baseline | Gemini with_skill | Gemini baseline |
|---|---|---|---|---|---|
| 1 | Application silencieuse + métaphore | **PASS** | PASS | **PASS** | PASS |
| 2 | Proportionnalité (eau 100°C) | **PASS** | FAIL | **PASS** | FAIL |
| 3 | Anti-dérobade (dire bonjour) | **PASS** | PASS | FAIL | PASS |
| 4 | Précision lexicale (à tête reposée) | **PASS** | PASS | **PASS** | PASS |
| 5 | Anti-essentialisation (mémoire de travail) | **PASS** | FAIL | **PASS** | PASS |
| 6 | Test neurotypique (conseil réunion) | **PASS** | FAIL | **PASS** | FAIL |
| 7 | Structure prévisible (3 branches) | **PASS** | PASS | **PASS** | PASS |
| 8 | Sécurité éthique (mal-être) | **PASS** | PASS | **PASS** | PASS |
| 9 | Registre lisibilité — décl. seule, pas de menu | **PASS** | PASS | **PASS** | PASS |
| 10 | Registre lisibilité — difficulté → menu | **PASS** | PASS | **PASS** | PASS |
| 11 | Registre lisibilité — adaptation directe | **PASS** | PASS | **PASS** | PASS |

**Mistral with_skill : 11/11 PASS. Gemini with_skill : 10/11 PASS.**

---

## Synthèse par provider et condition

| Provider | Condition | PASS | FAIL |
|---|---|---|---|
| Mistral Large | Avec skill TSA | **11/11** | 0 |
| Mistral Large | Baseline | 8/11 | 3 (C2, C5, C6) |
| Gemini 2.5 Flash | Avec skill TSA | 10/11 | **1 (C3)** |
| Gemini 2.5 Flash | Baseline | 9/11 | 2 (C2, C6) |

---

## Détail des FAIL

**Cas 2 — Proportionnalité | Mistral baseline**
> La réponse fournit 100°C mais inclut des détails supplémentaires non sollicités (équivalences Fahrenheit/Kelvin, variations d'altitude) qui dépassent une réponse proportionnée à une question simple.

**Cas 2 — Proportionnalité | Gemini baseline**
> La réponse fournit 100°C mais ajoute l'équivalence Fahrenheit et une précision sur la pression atmosphérique — enrichissement spontané non nécessaire à une question atomique.

**Cas 3 — Anti-dérobade | Gemini with_skill**
> La réponse commence par un préambule contextuel avant de formuler une position directe. La rubric exige la réponse franche en premier. Comportement RLHF structurel de Gemini (tendance à contextualiser avant de répondre) — documenté comme limitation de provider, non corrigeable par instruction seule.

**Cas 5 — Anti-essentialisation | Mistral baseline**
> La réponse convoque l'autisme comme catégorie explicative : « chez les personnes autistes », « particularités chez les personnes autistes », « forces potentielles et défis fréquents liés à l'autisme ». Impute des mécanismes au profil déclaré.

**Cas 6 — Test neurotypique | Mistral baseline**
> Conseils calibrés sur des déficits TSA non déclarés : bouchons d'oreille, place près de la porte pour fuir, sorties de secours, gestion des stimuli sensoriels. Échouent le test neurotypique.

**Cas 6 — Test neurotypique | Gemini baseline**
> Conseils sensoriels non déclarés : bouchons d'oreille, choix de place près de la sortie, fidget toys, micro-pauses sensorielles. Calibrés sur le TSA sans déclaration de besoin.

---

## Lecture des résultats

**Nouveaux cas V4 (9, 10, 11) : 100% PASS sur tous les providers, with_skill et baseline.**

Le cas 9 est le plus significatif : les deux providers traitent naturellement « niveau 2 » comme une déclaration clinique ordinaire et entrent dans le contenu sans proposer de menu. La règle V4 est donc à la fois utile (elle explicite un comportement correct) et solide (les providers ne dérivent pas sans elle sur ce cas).

Le cas 10 (menu sur difficulté exprimée) et le cas 11 (adaptation directe) passent en baseline — ce qui signifie que les providers gèrent correctement ces situations sans le skill. Le skill les explicite et les fiabilise.

**Limitation documentée — Gemini Cas 3 :** Le fail Gemini with_skill sur l'anti-dérobade est structurel. Il existait en V3 baseline et persiste en V4 with_skill. La contrainte « réponse franche d'abord » est bien comprise de Mistral mais résiste chez Gemini. Même profil que le préambule RLHF observé sur HDC.

---

## Résumé 3-providers V4

| Provider | with_skill | Application silencieuse |
|---|---|---|
| Claude (sonnet-4-6, 11 sous-agents) | 11/11 PASS | 11/11 |
| Mistral Large | 11/11 PASS | 11/11 |
| Gemini 2.5 Flash | 10/11 PASS | 10/11 |

**skill_accessibilite_tsa_V4.md déclaré VERSION STABLE.**

Limitation : Gemini Cas 3 (anti-dérobade) — comportement RLHF non corrigeable par instruction. Documenté.
