# AGENTS.md

Guide de contribution pour agents (Claude Code, Codex) et humains travaillant sur ce dépôt. Décrit les conventions, les invariants à ne pas casser, et le workflow de validation/release.

> Branche de référence : `main`. Toute analyse ou contribution doit partir d'un clone à jour (`git pull`) — le dépôt évolue par versions (voir `CHANGELOG.md`).

---

## Nature du projet

Écosystème de **skills** pour LLM (Claude en priorité) qui adaptent la **forme** des réponses à des besoins cognitifs, sensoriels ou neurobiologiques, et encadrent le **fond** des questions psychologiques. Aucun code applicatif : le livrable est un ensemble de fichiers `SKILL.md` versionnés, évalués et packageables.

## Cartographie

| Chemin | Rôle |
|---|---|
| `skills/<nom>/SKILL.md` | Un skill = un dossier = un `SKILL.md` (frontmatter + règles). Source de vérité du comportement. |
| `docs/index_skills.md` | Index canonique : version stable, déclencheur, compatibilités, statut d'éval par skill. |
| `docs/bilan_ecosysteme_skills_accessibilite.md` | Historique d'itération, méthodologie, décisions d'architecture. |
| `docs/note_ethique.md` | Limites éthiques (pas de diagnostic, pas de soin, pas de substitution). |
| `docs/usage.md` | Cas d'usage concrets par skill. |
| `eval/` | Harnais [promptfoo](https://promptfoo.dev) : un `promptfooconfig_<skill>.yaml` par skill, `run_all.sh`, résultats JSON. |
| `scripts/validate_skills.py` | Validation structurelle (CI + pré-commit). Stdlib uniquement. |
| `.github/workflows/` | `validate.yml` (push/PR sur `main`), `release.yml` (publication des ZIP sur tag). |
| `build_release.sh` | Valide puis génère un ZIP par skill dans `dist/`. |
| `notes/` | Notes de travail (vault Obsidian), non normatif. |

## Invariants des skills (vérifiés par `validate_skills.py`)

1. **Frontmatter YAML** présent : `name` et `description`.
2. **`name` == nom du dossier** (ex. `accessibilite-tsa`).
3. **`description` ≤ 1024 caractères** (contrainte format Claude Skills).
4. **Fichier < 500 lignes** (seuil de découpage recommandé par Anthropic ; les skills tiennent volontairement en un seul fichier).
5. **Bloc « Ordre de préséance entre skills » strictement identique** dans les 7 `SKILL.md` (comparé par hash sha256). Modifier ce bloc = le modifier à l'identique partout.

Toujours lancer la validation avant de committer un changement de skill :

```bash
python3 scripts/validate_skills.py   # exit 0 = OK
```

## Principes de conception (non négociables)

- **Déclencheurs stricts** : un skill d'accessibilité s'active sur **déclaration explicite** ou besoin formulé directement — jamais par inférence d'un trouble à partir de signaux faibles (fautes d'orthographe, mention de procrastination, fatigue ordinaire…).
- **Forme, pas fond** : les skills d'accessibilité changent la manière de répondre, pas l'exactitude ni la complétude du contenu.
- **Anti-essentialisation** : ne jamais imputer un comportement ou un ressenti à une catégorie (« les autistes… », « avec ton TDAH… »).
- **Sécurité éthique prioritaire** : face à une souffrance durable ou un risque, l'orientation vers un soutien professionnel prime sur toute règle de forme. Voir `docs/note_ethique.md`.

## Ordre de préséance (forme)

En co-activation, l'ordre canonique sur la forme est :

1. Sécurité éthique (`psychologie-rigoureuse`) — prime sur tout
2. `accessibilite-visuelle`
3. Skills de réduction de charge (`accessibilite-dys`, `accessibilite-tdah`, `accessibilite-douleur-chronique-fatigue-cognitive`)
4. `accessibilite-tsa`
5. `accessibilite-haute-densite-cognitive`

Le **fond** est régi par `psychologie-rigoureuse`, hors de cet ordre. En co-activation, le **plafond de mots le plus bas** parmi les skills actifs prime.

## Évaluation

```bash
cd eval/
cp .env.example .env        # renseigner MISTRAL_API_KEY et GOOGLE_API_KEY
./run_all.sh                # tous les harnais
./run_all.sh dys tsa        # harnais ciblés
```

Chaque harnais teste deux conditions (avec / sans skill) sur ≥ 2 providers (Mistral Large, Gemini 2.5 Flash), avec un juge `llm-rubric`. Couvrir au minimum : cas nominaux, cas de **non-déclenchement**, cas de **co-activation**, cas de **sécurité/éthique**. Les erreurs API (503) sont exclues du score, pas comptées comme échec.

## Versionnement & release

- **`CHANGELOG.md`** au format [Keep a Changelog](https://keepachangelog.com/fr/1.0.0/). Toute modification notable y est consignée (section `[Non publié]` en attendant un tag).
- **Versions par skill** (`V<major>.<minor>`) suivies dans le frontmatter/README/index ; la version d'écosystème (`1.x.0`) est portée par les tags Git.
- **Release** : pousser un tag `vX.Y.Z` déclenche `release.yml`, qui exécute `build_release.sh` (validation → ZIP par skill) et publie les ZIP. Un ZIP = un skill, dossier à la racine (`accessibilite-tsa/SKILL.md`).

## Workflow Git

- Développer sur une branche dédiée, jamais directement sur `main`.
- Lancer `python3 scripts/validate_skills.py` avant tout commit touchant un skill.
- Messages de commit descriptifs ; mettre à jour `CHANGELOG.md` et, si pertinent, `docs/index_skills.md`.
- Ouvrir une PR vers `main` ; la CI `validate` doit être verte avant merge.
