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
| `eval/` | Banques de cas comportementaux et d'activation, protocole de validation en vagues (`prompt_benchmark_claude_code.md`) et preuves assainies versionnées. |
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
y lève l'anonymat des juges et ne doit pas être commité. Une promotion exige dans la même PR
un paquet assaini suivi sous `eval/evidence/<horodatage>/` ; la CI vérifie sa présence et sa structure.

## Versionnement & release

- **`CHANGELOG.md`** au format [Keep a Changelog](https://keepachangelog.com/fr/1.0.0/). Toute modification notable y est consignée (section `[Non publié]` en attendant un tag).
- **Versions par skill** (`V<major>.<minor>`) suivies dans le frontmatter/README/index ; la version d'écosystème (`1.x.0`) est portée par les tags Git.
- **Release** : pousser un tag `vX.Y.Z` déclenche `release.yml`, qui exécute `build_release.sh` (validation → ZIP par skill) et publie les ZIP. Un ZIP = un skill, dossier à la racine (`accessibilite-tsa/SKILL.md`).

## Workflow Git

- Développer sur une branche dédiée, jamais directement sur `main`.
- Lancer `python3 scripts/validate_skills.py` avant tout commit touchant un skill.
- Messages de commit descriptifs ; mettre à jour `CHANGELOG.md` et, si pertinent, `docs/index_skills.md`.
- Ouvrir une PR vers `main` ; la CI `validate` doit être verte avant merge.
