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
| `eval/` | Banques de cas comportementaux et d'activation, protocole de validation en vagues (`prompt_benchmark_claude_code.md`). Les preuves assainies d'une vague sont versionnées sous `eval/evidence/` (aucune à ce jour). Les `analyse_*.md` et `results*.json` sont des archives de l'ancien outillage. |
| `scripts/validate_skills.py` | Validation structurelle des skills (CI). Dépend de PyYAML (`requirements-ci.txt`). |
| `scripts/check_*.py` | Contrôles des banques d'évaluation, des cas d'activation et des paquets de preuves (CI). |
| `.github/workflows/` | `validate.yml` (push/PR sur `main`), `release.yml` (publication des ZIP sur tag). |
| `build_release.sh` | Valide puis génère un ZIP par skill dans `dist/`. |
| `notes/` | Notes de travail (vault Obsidian), non normatif. |

## Invariants des skills (vérifiés par `validate_skills.py`)

1. **Frontmatter YAML** présent, fermé par `---` et lisible par un parseur YAML strict : `name` et `description`. Seules les clés acceptées à l'import dans claude.ai sont permises (`name`, `description`, `license`, `compatibility`, `metadata`, `allowed-tools`).
2. **`name` == nom du dossier** (ex. `accessibilite-tsa`), en minuscules, chiffres et tirets simples, 64 caractères au plus.
3. **`description` ≤ 1024 caractères** (contrainte format Claude Skills), mesurée sur la valeur lue par le parseur.
4. **Fichier < 500 lignes** (seuil de découpage recommandé par Anthropic).
5. **Un skill = un seul fichier** : le dossier ne contient que `SKILL.md`. Tout autre fichier partirait dans la distribution sans avoir été évalué.
6. **Bloc « Ordre de préséance entre skills » strictement identique** dans les 7 `SKILL.md` (comparé par hash sha256). Modifier ce bloc = le modifier à l'identique partout.

Toujours lancer la validation avant de committer un changement de skill :

```bash
python -m pip install -r requirements-ci.txt   # une fois
python scripts/validate_skills.py              # exit 0 = OK
```

Sous Linux et macOS, la commande est `python3`.

## Principes de conception (non négociables)

- **Déclencheurs stricts** : un skill d'accessibilité s'active sur **déclaration explicite** ou besoin formulé directement — jamais par inférence d'un trouble à partir de signaux faibles (fautes d'orthographe, mention de procrastination, fatigue ordinaire…).
- **Forme, pas fond** : les skills d'accessibilité changent la manière de répondre, pas l'exactitude ni la complétude du contenu.
- **Anti-essentialisation** : ne jamais imputer un comportement ou un ressenti à une catégorie (« les autistes… », « avec ton TDAH… »).
- **Sécurité éthique prioritaire** : face à une souffrance durable ou un risque, l'orientation vers un soutien professionnel prime sur toute règle de forme. Voir `docs/note_ethique.md`.

## Ordre de préséance (forme)

En co-activation, l'ordre canonique sur la forme est :

1. Sécurité éthique (commune à tous les skills) — prime sur tout
2. `accessibilite-visuelle`
3. Skills de réduction de charge (`accessibilite-dys`, `accessibilite-tdah`, `accessibilite-douleur-chronique-fatigue-cognitive`)
4. `accessibilite-tsa`
5. `accessibilite-haute-densite-cognitive`

Le **fond** est régi par `psychologie-rigoureuse`, hors de cet ordre. En co-activation, le **plafond de mots le plus bas** parmi les skills actifs prime.

## Évaluation

Il n'y a **pas de lanceur automatisé**. La validation se fait en **vagues** : une session
d'agents (Claude Code ou ChatGPT) exécute le protocole `eval/prompt_benchmark_claude_code.md`,
ouvert à la racine du dépôt.

Les `eval/promptfooconfig_<skill>.yaml` servent de **banque de cas comportementaux** —
question, assertions déterministes (`javascript`) et sémantiques (`llm-rubric`), et lien
vers le `SKILL.md` évalué. `eval/activation_cases.json` teste séparément la décision de
charger ou non chaque skill, sans injecter son corps.

Une vague commence par trois décisions de sélection indépendantes sur chaque cas
d'activation/non-déclenchement. Elle joue ensuite chaque cas comportemental **deux fois** —
avec et sans le skill, même question, contextes isolés — puis fait juger les paires **en
aveugle** par trois juges indépendants, dont un chargé de chercher les régressions. Couvrir
au minimum : cas nominaux, **co-activation**, **sécurité/éthique**. Les erreurs
d'infrastructure sont exclues des dénominateurs, jamais comptées comme échec du skill.

Les artefacts d'une vague vont dans `eval/runs/<horodatage>/`, ignoré par Git : `blinding_map.json`
y lève l'anonymat des juges et ne doit pas être commité. Une promotion, ou la modification d'un
skill en production, exige dans la même PR un paquet assaini suivi sous `eval/evidence/<horodatage>/`.
La CI vérifie sa présence, sa structure, et que le paquet porte sur la version du `SKILL.md`
présente dans la PR : une vague doit donc évaluer l'état final du skill.

## Versionnement & release

- **`CHANGELOG.md`** au format [Keep a Changelog](https://keepachangelog.com/fr/1.0.0/). Toute modification notable y est consignée (section `[Non publié]` en attendant un tag).
- **Versions par skill** (`V<major>.<minor>`) : la référence est `docs/index_skills.md`, reprise dans le README et dans le tableau « Historique versions » en fin de chaque `SKILL.md`. Le frontmatter ne porte pas de version (claude.ai refuse les clés inconnues à l'import). La version d'écosystème (`X.Y.Z`) est portée par les tags Git.
- **Une montée de version s'appuie sur une vague de validation** (voir « Évaluation » et `CONTRIBUTING.md` §2 et §5). Tant que la preuve manque, le skill reste au statut « candidat » dans l'index. Seule exception : un correctif sans changement de comportement (erreur factuelle, défaut de chargement), consigné comme tel dans le changelog.
- **Release** : pousser un tag `X.Y.Z`, **sans préfixe `v`** (ex. `1.19.1`), déclenche `release.yml`. Le workflow rejoue toute la validation (`validate.yml`), vérifie que le commit tagué est sur `main` ou sur une branche `hotfix/*`, puis exécute `build_release.sh` et publie un ZIP par skill. Un ZIP ne contient que `<nom>/SKILL.md`. Un tag `vX.Y.Z` ne déclenche rien.

## Workflow Git

- Développer sur une branche dédiée, jamais directement sur `main`.
- Avant tout commit, lancer les contrôles que la CI exécute (`python3` sous Linux et macOS) :

  ```bash
  python -m pip install -r requirements-ci.txt   # une fois
  python scripts/validate_skills.py
  python scripts/check_eval_configs.py
  python scripts/check_eval_leaks.py
  python scripts/check_activation_cases.py
  python scripts/check_evidence.py --base origin/main
  ```
- Messages de commit descriptifs ; mettre à jour `CHANGELOG.md` et, si pertinent, `docs/index_skills.md`.
- Ouvrir une PR vers `main` ; la CI `validate` doit être verte avant merge.
