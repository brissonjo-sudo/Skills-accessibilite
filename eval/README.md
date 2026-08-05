# Banque de cas et validation — Écosystème Skills Accessibilité

Ce répertoire contient les **cas de test** de chaque skill et le **protocole de validation**.
Il n'y a pas de lanceur automatisé : la validation se fait en **vagues**, dans une session
d'agents (Claude Code ou ChatGPT).

## Lancer une vague

Ouvrir une session à la racine du dépôt et coller le contenu de
[`prompt_benchmark_claude_code.md`](prompt_benchmark_claude_code.md).

Le protocole teste d'abord la sélection avec trois agents ne voyant que les métadonnées des
skills. Il joue ensuite chaque cas comportemental **deux fois** — avec et sans le skill,
même question, contextes isolés — puis fait juger les paires **en aveugle** par trois juges
indépendants par variante.

Les artefacts bruts vont dans `eval/runs/<AAAAMMJJ-HHMMSS>/`, **ignoré par Git** :
`blinding_map.json` y contient la correspondance A/B → condition. Toute promotion produit
aussi un paquet assaini et suivi sous `eval/evidence/<AAAAMMJJ-HHMMSS>/`, avec manifeste,
résultats de sélection, verdicts résolus, métriques et rapport. La CI exige ce paquet pour
chaque skill modifié ou nouvellement marqué `production`.

Les `results*.json` historiques (13 archives, issues de l'ancien outillage) restent suivis
pour la reproductibilité. Ne pas en ajouter de nouveaux.

## Banques de cas

| Skill | Fichier | Cas |
|---|---|---|
| Haute densité cognitive V3.2 | `promptfooconfig.yaml` | 8 |
| Accessibilité visuelle V1.2 | `promptfooconfig_visuel.yaml` | 8 |
| TSA V4.1 | `promptfooconfig_tsa.yaml` | 11 |
| Douleur chronique / Fatigue V3.2 | `promptfooconfig_fatigue.yaml` | 8 |
| DYS V3.1 | `promptfooconfig_dys.yaml` | 8 |
| TDAH V2.3 | `promptfooconfig_tdah.yaml` | 10 |
| Psychologie rigoureuse V6.2 | `promptfooconfig_psychologie.yaml` | 8 |
| Co-activation inter-skills | `promptfooconfig_coactivation.yaml` | 6 |

**67 cas au total.** Les noms de fichiers sont un héritage de l'ancien outillage ; leur
contenu est désormais une simple banque de cas — description, question, assertions, et lien
vers le `SKILL.md` évalué.

`activation_cases.json` ajoute **14 cas de sélection** : un déclenchement et un
non-déclenchement pour chacun des 7 skills. Chaque cas est soumis à trois sélecteurs neufs,
soit 42 décisions indépendantes. `scripts/check_activation_cases.py` contrôle cette couverture.

## Structure des assertions

39 assertions déterministes, 78 sémantiques.

| Banque | `javascript` | `llm-rubric` |
|---|--:|--:|
| `promptfooconfig.yaml` (HDC) | 2 | 9 |
| `promptfooconfig_visuel.yaml` | 6 | 16 |
| `promptfooconfig_tsa.yaml` | 4 | 12 |
| `promptfooconfig_fatigue.yaml` | 4 | 9 |
| `promptfooconfig_dys.yaml` | 5 | 8 |
| `promptfooconfig_tdah.yaml` | 5 | 10 |
| `promptfooconfig_psychologie.yaml` | 8 | 8 |
| `promptfooconfig_coactivation.yaml` | 5 | 6 |

**Déterministes (`javascript`)** — une expression JavaScript sur la variable `output`,
évaluable sans juge :

- Application silencieuse : formulations interdites (« mode DYS activ », « skill activ »…)
- Anti-essentialisation : généralisations catégorielles
- Anti-prescription : « tu devrais », « il faut que »
- Anti-injonction à l'effort : « commence par », « tu dois », « il suffit de » (fatigue, co-activation)
- Anti-relance cascade : comptage des `?`
- Plafond ou bornes de mots
- Anti-emojis (DYS, Visuelle)
- Références positionnelles, ASCII art, hiérarchie des titres sans saut de niveau (Visuelle)
- Mention d'un professionnel ou d'une ligne d'écoute (Visuelle, Fatigue, Psychologie)

> **Nature de ces contrôles.** La plupart sont des **garde-fous anti-régression**, pas des
> discriminants : sur le run de référence, seuls les plafonds de mots séparaient nettement les
> deux conditions, les autres passaient déjà en baseline. Leur rôle est de faire échouer la
> vague si une évolution du skill réintroduit un emoji, un schéma ASCII ou une injonction —
> pas de démontrer une valeur ajoutée.

Un bloc multi-lignes est autorisé : la **dernière expression** est la valeur retournée.

**Sémantiques (`llm-rubric`)** — jugées par les trois juges de la vague : qualité du fond
(profondeur, nuance, rigueur), cohérence de la forme, co-activations.

## Erreurs d'infrastructure

Limite de session, coupure réseau, agent qui ne rend pas de réponse : ce sont des erreurs
**d'infrastructure**, à exclure des dénominateurs. Elles ne comptent jamais comme un échec du
skill. Le protocole les enregistre en `status: infrastructure_error` et n'invente jamais de
réponse à la place.

## Source unique du skill

Chaque banque pointe vers le fichier canonique dans `skills/` via `file://../skills/...`.
**Aucune copie du skill dans `eval/`.** Pour changer de version, rien à modifier ici : le
lien suit le fichier.

## Règles à tenir sur les cas

- **Aucune question recopiée du `SKILL.md` évalué.** Un modèle qui a l'exemple sous les yeux
  récite au lieu de raisonner — c'est arrivé, avec une réponse *byte-identique* à celle du
  skill. Vérifié en CI par `scripts/check_eval_leaks.py`. Partager la **phrase de
  déclenchement** documentée reste nécessaire et n'est pas une fuite.
- **Déclenchement et non-déclenchement** : les tester dans `activation_cases.json`, avant
  toute injection du corps d'un skill.
- **Chaque cas porte au moins une assertion sémantique.** Les assertions déterministes
  s'ajoutent quand le critère est mécaniquement vérifiable.

## Convention de versionnement

1. Modifier le `SKILL.md` et incrémenter sa version.
2. Rien à changer dans la banque de cas : le lien `skill:` suit déjà le fichier.
3. Passer une **vague de validation**, ajouter son paquet sous `eval/evidence/`, puis mettre
   à jour `CHANGELOG.md` en citant le `report.md` suivi et `docs/index_skills.md`.
