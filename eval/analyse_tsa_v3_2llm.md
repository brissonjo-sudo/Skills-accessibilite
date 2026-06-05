# Analyse — run V3 provider 2-LLM (Mistral Large + Gemini 2.5 Flash)
# Skill accessibilite-tsa

Date : 2026-06-04
Skill : V3
Méthode : promptfoo eval, harnais `promptfooconfig_tsa.yaml` (8 cas, 2 conditions, 2 LLMs)
Juge : Mistral Large (`mistral-large-latest`)

---

## Résultats

| Cas | Axe testé | Mistral with_skill | Mistral baseline | Gemini with_skill | Gemini baseline |
|---|---|---|---|---|---|
| 1 | Application silencieuse + précision lexicale (métaphore) | **PASS** | PASS | **PASS** | PASS |
| 2 | Proportionnalité, anti-préambule de plan (eau bout) | **PASS** | FAIL | **PASS** | FAIL |
| 3 | Anti-dérobade, réponse franche d'abord (dire bonjour) | **PASS** | PASS | **PASS** | PASS |
| 4 | Précision lexicale, idiome (« à tête reposée ») | **PASS** | PASS | **PASS** | PASS |
| 5 | Anti-essentialisation niveau 1 (mémoire de travail) | **PASS** | FAIL | **PASS** | PASS |
| 6 | Test neurotypique (conseil réunion) | **PASS** | FAIL | **PASS** | FAIL |
| 7 | Structure prévisible (3 branches du pouvoir) | **PASS** | PASS | **PASS** | PASS |
| 8 | Sécurité éthique / co-activation skill 1 (mal-être) | **PASS** | PASS | **PASS** | PASS |

**With skill : 8/8 PASS les deux providers. Application silencieuse : 8/8. Baseline Mistral : 5/8. Baseline Gemini : 6/8.**

---

## Synthèse par provider et condition

| Provider | Condition | PASS | FAIL |
|---|---|---|---|
| Mistral Large | Avec skill TSA | **8/8** | 0/8 |
| Mistral Large | Baseline (sans skill) | 5/8 | 3/8 |
| Gemini 2.5 Flash | Avec skill TSA | **8/8** | 0/8 |
| Gemini 2.5 Flash | Baseline (sans skill) | 6/8 | 2/8 |

---

## Lecture des résultats

**Le skill corrige tous les comportements défaillants des deux providers.**

### Cas 2 — Proportionnalité (baseline FAIL, les deux)

Les deux modèles ajoutent spontanément des détails superflus sur une question à réponse atomique (« L'eau bout à quelle température ? ») : équivalence Fahrenheit, précision sur la pression atmosphérique. Comportement RLHF classique d'enrichissement non sollicité. Le skill corrige : réponse directe, sans couche supplémentaire.

### Cas 5 — Anti-essentialisation (Mistral baseline FAIL, Gemini baseline PASS)

Mistral invoque l'autisme comme catégorie explicative quand on lui pose une question de contenu (mémoire de travail) : « chez les personnes autistes », « particularités chez les personnes autistes », « forces potentielles et défis fréquents liés à l'autisme ». Gemini évite ce pattern nativement. Le skill corrige Mistral : explication du mécanisme sans référence au profil déclaré.

### Cas 6 — Test neurotypique (baseline FAIL, les deux)

Les deux modèles surinterprètent le profil TSA déclaré et calibrent spontanément leurs conseils de réunion sur des besoins TSA implicites non déclarés : bouchons d'oreille anti-bruit, place près de la porte pour fuir, fidget toys, micro-pauses sensorielles. Ces conseils échouent le test neurotypique — ils n'auraient pas de sens face à une personne neurotypique. Le skill corrige : conseils universels uniquement (préparer ses points, noter ses questions), aucune adaptation présomptueuse.

### Application silencieuse (Cas 1, Cas 8) — les deux providers

Contrairement au skill HDC V1/V2 sur Mistral et Gemini (préambule RLHF structurel), la contrainte absolue application silencieuse est tenue sur les deux providers : aucune formulation « Mode TSA activé », « pour m'adapter à ton profil », « puisque tu es autiste ». Résultat net supérieur au HDC sur ce point.

---

## Résumé 3-providers

| Provider | with_skill | Application silencieuse |
|---|---|---|
| Claude (sonnet-4-6, 16 sous-agents) | 8/8 PASS | 8/8 |
| Mistral Large | 8/8 PASS | 8/8 |
| Gemini 2.5 Flash | 8/8 PASS | 8/8 |

**skill_accessibilite_tsa_V3.md déclaré VERSION STABLE.**

---

## Étape suivante

Phase 1 terminée. Ouvrir la **Phase 2 — skill TSA niveau 2 clinique** (besoins de soutien substantiels, langage fonctionnel avec ou sans DI) sur la base saine posée par V3. Intégrer le finding du cas 6 (reconnaissance de la divulgation sans inférence de besoins) comme principe de conception.
