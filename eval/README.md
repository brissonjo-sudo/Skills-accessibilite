# Harnais d'évaluation — Écosystème Skills Accessibilité

Évalue chaque skill sur deux conditions (avec skill / baseline sans skill) et deux LLMs (Mistral Large, Gemini 2.5 Flash).

## Prérequis

- Node.js LTS
- promptfoo installé globalement : `npm install -g promptfoo`
- Clés API renseignées dans `eval/.env`

## Installation

```bash
cd eval/
cp .env.example .env
# Renseigner MISTRAL_API_KEY et GOOGLE_API_KEY dans .env
```

## Lancement

### Tous les harnais (runner unique)

```bash
cd eval/
./run_all.sh
```

### Un harnais spécifique

```bash
cd eval/
promptfoo eval --config promptfooconfig_dys.yaml --output results_dys.json
promptfoo view
```

Chaque run produit un fichier `results_<skill>.json`. Le pousser sur la branche pour analyse partagée.

## Harnais disponibles

| Skill | Config | Cas | Skills testés |
|-------|--------|-----|---------------|
| Haute densité cognitive V3 | `promptfooconfig.yaml` | 8 | application silencieuse, profondeur, anti-essentialisation HDC, co-activation |
| Accessibilité visuelle V1 | `promptfooconfig_visuel.yaml` | 8 | application silencieuse, emojis, références positionnelles, ASCII art, tableaux, sécurité éthique |
| TSA V4 | `promptfooconfig_tsa.yaml` | 11 | application silencieuse, littéralité, prévisibilité, registre lisibilité, anti-essentialisation, sécurité |
| Douleur chronique / Fatigue V3 | `promptfooconfig_fatigue.yaml` | 8 | application silencieuse, front-loading, modularité, anti-injonction, exception question-définition |
| DYS V3 | `promptfooconfig_dys.yaml` | 8 | application silencieuse, phrases courtes, anti-essentialisation DYS, co-activation, sécurité éthique |
| TDAH V2.1 | `promptfooconfig_tdah.yaml` | 8 | application silencieuse, action unique, chunking, anti-moralisation, anti-essentialisation TDAH |
| Psychologie rigoureuse V6 | `promptfooconfig_psychologie.yaml` | 8 | marquage différencié, non-prescription, anti-essentialisation, mention pro, sécurité éthique |

## Structure des assertions

Chaque harnais mélange deux types d'assertions :

**Déterministes (`javascript`)** — vérifiables par regex, pas de juge LLM :
- Application silencieuse : détection de formulations interdites (« mode DYS activ », « skill activ »…)
- Anti-essentialisation : détection de généralisations catégorielles
- Anti-prescription : détection de « tu devrais », « il faut que »
- Anti-relance cascade : comptage des `?` en fin de réponse
- Plafond de mots : comptage simple
- Anti-emojis (pour DYS, Visuelle)

**Sémantiques (`llm-rubric`)** — évalués par le juge LLM (`mistral:mistral-small-latest`) :
- Qualité du fond (profondeur, nuance, rigueur)
- Cohérence de la forme (structure, aération)
- Co-activations

> **Juge** : `mistral:mistral-small-latest` (non testé comme provider) — évite la circularité avec `mistral-large-latest`.

## Erreurs API (503, 429)

Les erreurs d'infrastructure (Gemini 503, quota dépassé) produisent des résultats avec `failureReason: 2`.
À distinguer des échecs de skill (`failureReason: 1`). Le script `run_all.sh` exclut ces erreurs du score.

## Source unique du skill

Chaque config pointe directement vers le fichier canonique dans `skills/` via `file://..skills/...`.
**Aucune copie du skill dans `eval/`.** Pour changer de version, mettre à jour uniquement la ligne `skill:` du `defaultTest`.

## Providers actifs

| Provider | Modèle | Clé |
|----------|--------|-----|
| Mistral AI | `mistral-large-latest` | `MISTRAL_API_KEY` |
| Google AI Studio | `gemini-2.5-flash` | `GOOGLE_API_KEY` |
| Mistral AI (juge) | `mistral-small-latest` | `MISTRAL_API_KEY` |

> Note historique :
> - Grok (xAI) retiré — compte sans crédits (HTTP 403).
> - Gemini 3.1 Pro Preview retiré — indisponible en tier gratuit (HTTP 429).

## Convention de versionnement

Lors d'une itération V1 → V2 :
1. Créer le fichier `skills/<dossier>/skill_..._V2.md`
2. Mettre à jour la ligne `skill:` dans le fichier de config correspondant
3. Relancer `promptfoo eval` pour mesurer le delta
