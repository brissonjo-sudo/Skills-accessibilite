# Harnais d'évaluation — Écosystème Skills Accessibilité

Évalue chaque skill sur deux conditions (avec skill / baseline sans skill) et trois LLMs (Mistral Large, Gemini 2.5 Flash, Claude Sonnet 4.6).

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

### Benchmark complet via Claude Code

Ouvrir Claude Code à la racine du dépôt, puis copier-coller le bloc de
`prompt_benchmark_claude_code.md`. Il importe d’abord les `SKILL.md` canoniques à
jour, exécute les conditions avec/sans skill en contextes isolés et orchestre
trois juges aveugles en parallèle pour chaque variante.

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

Chaque run produit un fichier `results_<skill>.json`. Les nouveaux résultats bruts sont ignorés par Git
en raison de leur taille ; 13 archives historiques déjà suivies restent conservées pour la reproductibilité.
Ne pas ajouter de nouveau JSON brut : consigner les résultats synthétiques et les décisions dans un
fichier `analyse_*.md`, source de vérité archivée.

## Harnais disponibles

| Skill | Config | Cas | Skills testés |
|-------|--------|-----|---------------|
| Haute densité cognitive V3.2 | `promptfooconfig.yaml` | 8 | application silencieuse, profondeur, anti-essentialisation HDC, co-activation |
| Accessibilité visuelle V1.2 | `promptfooconfig_visuel.yaml` | 8 | application silencieuse, emojis, références positionnelles, ASCII art, tableaux, sécurité éthique |
| TSA V4.1 | `promptfooconfig_tsa.yaml` | 11 | application silencieuse, littéralité, prévisibilité, registre lisibilité, anti-essentialisation, sécurité |
| Douleur chronique / Fatigue V3.2 | `promptfooconfig_fatigue.yaml` | 8 | application silencieuse, front-loading, modularité, anti-injonction, exception question-définition |
| DYS V3.1 | `promptfooconfig_dys.yaml` | 8 | application silencieuse, phrases courtes, anti-essentialisation DYS, co-activation, sécurité éthique |
| TDAH V2.3 | `promptfooconfig_tdah.yaml` | 10 | application silencieuse, action unique, chunking, anti-moralisation, anti-essentialisation TDAH, déclencheur TDA, non-déclenchement |
| Psychologie rigoureuse V6.2 | `promptfooconfig_psychologie.yaml` | 8 | marquage différencié, non-prescription, anti-essentialisation, mention pro, sécurité éthique |
| Co-activation inter-skills | `promptfooconfig_coactivation.yaml` | 6 | arbitrage des plafonds, anti-injonction TDAH/fatigue, littéralité TSA, marquage sous DYS |

## Structure des assertions

Chaque harnais mélange deux types d'assertions. Répartition réelle (39 assertions
déterministes, 78 sémantiques) :

| Harnais | `javascript` | `llm-rubric` |
|---|--:|--:|
| `promptfooconfig.yaml` (HDC) | 2 | 9 |
| `promptfooconfig_visuel.yaml` | 6 | 16 |
| `promptfooconfig_tsa.yaml` | 4 | 12 |
| `promptfooconfig_fatigue.yaml` | 4 | 9 |
| `promptfooconfig_dys.yaml` | 5 | 8 |
| `promptfooconfig_tdah.yaml` | 5 | 10 |
| `promptfooconfig_psychologie.yaml` | 8 | 8 |
| `promptfooconfig_coactivation.yaml` | 5 | 6 |

**Déterministes (`javascript`)** — vérifiables par regex, pas de juge LLM :
- Application silencieuse : détection de formulations interdites (« mode DYS activ », « skill activ »…)
- Anti-essentialisation : détection de généralisations catégorielles
- Anti-prescription : détection de « tu devrais », « il faut que »
- Anti-injonction à l'effort : « commence par », « tu dois », « il suffit de » (fatigue, co-activation)
- Anti-relance cascade : comptage des `?` en fin de réponse
- Plafond ou bornes de mots : comptage simple
- Anti-emojis (DYS, Visuelle)
- Références positionnelles, ASCII art, hiérarchie des titres sans saut de niveau (Visuelle)
- Mention d'un professionnel ou d'une ligne d'écoute (Visuelle, Fatigue, Psychologie)

> **Nature de ces contrôles.** La plupart sont des **garde-fous anti-régression**, pas des
> discriminants : sur le run de référence, seuls les plafonds de mots séparaient nettement les
> deux conditions, les autres passaient déjà en baseline. Leur rôle est de faire échouer le
> harnais si une évolution du skill réintroduit un emoji, un schéma ASCII ou une injonction —
> pas de démontrer une valeur ajoutée.

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
| Anthropic | `claude-sonnet-4-6` | `ANTHROPIC_API_KEY` |

> Le **modèle juge** des assertions `llm-rubric` est `mistral:mistral-small-latest` (non-circulaire : ce modèle n'est pas dans les providers testés).

> Note historique :
> - Grok (xAI) retiré — compte sans crédits (HTTP 403).
> - Gemini 3.1 Pro Preview retiré — indisponible en tier gratuit (HTTP 429).

## Convention de versionnement

Chaque skill tient dans un unique `skills/<dossier>/SKILL.md` (pas de fichier versionné séparé ; l'historique des versions est dans Git). Lors d'une itération :
1. Modifier le `SKILL.md` du skill (et incrémenter la version mentionnée dans son contenu / l'index).
2. La ligne `skill:` du `defaultTest` pointe déjà vers `file://../skills/<dossier>/SKILL.md` — rien à changer.
3. Relancer `promptfoo eval` pour mesurer le delta, puis mettre à jour `CHANGELOG.md` et `docs/index_skills.md`.
