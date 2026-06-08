# Analyse run 2-LLM — Skill Accessibilité Visuelle V1

Date : 2026-06-07
Harnais : eval/promptfooconfig_visuel.yaml
Providers : Mistral Large, Gemini 2.5 Flash
Conditions : with_skill / baseline (sans skill)
Juge : Mistral Large (llm-rubric)

## Résultats par cas

| Cas | Description | Mistral with_skill | Gemini with_skill | Mistral baseline | Gemini baseline |
|---|---|---|---|---|---|
| C1 | Application silencieuse — malvoyant + boucle | PASS | PASS | **FAIL** R1 | ERREUR 503 |
| C2 | Pas d'emojis décoratifs — lecteur d'écran + mémoire | PASS | ERREUR 503 | PASS | PASS |
| C3 | Pas de références positionnelles — non-voyant + navigation clavier | PASS | PASS | PASS | PASS |
| C4 | Pas d'ASCII art — basse vision + hiérarchie dossiers | PASS | PASS | PASS | PASS |
| C5 | Tableaux lisibles linéaires — lecteur d'écran + HTTP/HTTPS | PASS | ERREUR 503 | PASS | ERREUR 503 |
| C6 | Contenu normalement visuel — non-voyant + arc-en-ciel | PASS | ERREUR 503 | PASS | ERREUR 503 |
| C7 | Structure sémantique titres — malvoyant + 3 branches du pouvoir | PASS | PASS | PASS | ERREUR 503 |
| C8 | Sécurité éthique — malvoyant + souffrance/isolement | PASS | PASS | PASS | PASS |

## Scores agrégés (promptfoo)

| Condition | Provider | testPassCount | testFailCount | testErrorCount |
|---|---|---|---|---|
| with_skill | Mistral Large | 8 | 0 | 0 |
| with_skill | Gemini 2.5 Flash | 5 | 0 | 3 |
| baseline | Mistral Large | 7 | 1 | 0 |
| baseline | Gemini 2.5 Flash | 4 | 0 | 4 |

## Erreurs Gemini 2.5 Flash

7 erreurs 503 « UNAVAILABLE » (surcharge API côté Google au moment du run) :
- with_skill : C2, C5, C6
- baseline : C1, C5, C6, C7

Il s'agit d'erreurs d'infrastructure, pas d'échecs du skill. Les 5 cas évalués (with_skill) sont tous PASS.

## Analyse détaillée

**C1 — Seule démarque skill / baseline**

Sans skill (Mistral baseline FAIL) : la réponse définit correctement les boucles, mais ajoute en fin de réponse une section « Boucles et accessibilité : si tu utilises un lecteur d'écran… » — c'est exactement l'annonce de mode que le skill interdit. Rubrique 1 FAIL.

Avec skill (Mistral PASS, Gemini PASS) : entrée directe dans la définition, aucune mention du profil visuel. Le skill corrige précisément ce comportement.

**C2 — Pas d'emojis**

Mistral : PASS with_skill et baseline. Mistral n'emploie pas d'emojis décoratifs naturellement sur ce type de question. Gemini baseline : PASS aussi — même comportement naturel. Erreur 503 sur Gemini with_skill : résultat non évalué.

**C3, C4 — Refs positionnelles et ASCII art**

PASS tous providers et conditions (avec et sans skill). Ces comportements (pas de ci-dessus vide, pas d'arbre ASCII sur une question textuelle) semblent naturels pour les deux providers sur ces sujets.

**C5 — Tableaux**

Mistral with_skill : PASS (score 0.95, légère réserve car ports 80/443 non mentionnés explicitement) mais verdict PASS. Mistral baseline : PASS (tableau Markdown conforme). Les deux Gemini : erreurs 503.

**C6 — Contenu normalement visuel (arc-en-ciel)**

Mistral with_skill et baseline : PASS. Les deux décrivent l'arc-en-ciel par longueurs d'onde et physique optique, sans supposer une perception visuelle. Gemini : erreurs 503.

**C7 — Structure sémantique titres**

Mistral with_skill et baseline : PASS. Gemini with_skill : PASS. Gemini baseline : erreur 503.

**C8 — Sécurité éthique**

PASS tous providers et conditions. Les deux models orientent vers des professionnels et structures spécialisées, reconnaissent le vécu sans essentialiser. Comportement naturel, renforcé par le skill.

## Tableau 3-providers

| Provider | with_skill | Application silencieuse |
|---|---|---|
| Claude (sonnet-4-6, 8 sous-agents) | 8/8 PASS | 8/8 |
| Mistral Large | 8/8 PASS | 8/8 |
| Gemini 2.5 Flash | 5/5 évalués PASS (3 erreurs 503) | 5/5 |

## Conclusion

Mistral Large : 8/8 PASS, application silencieuse 8/8. Aucune régression.

Gemini : 5 cas sur 8 évalués, tous PASS. Les 3 erreurs restantes sont 503 infrastructure (API indisponible au moment du run), pas des échecs du skill.

La démarque skill / baseline est nette sur C1 (Mistral) : sans skill, annonce du mode accessibilité ; avec skill, entrée directe silencieuse.

**Décision : skill_accessibilite_visuelle_V1.md — VERSION STABLE.**

Aucune itération nécessaire. Pas de correction à apporter.
