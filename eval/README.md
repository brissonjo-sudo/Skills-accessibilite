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
comme trace historique. Ils ne sont plus reproductibles (gabarits de prompt et lanceur
supprimés, questions réécrites depuis). Ne pas en ajouter de nouveaux.

## Banques de cas

| Skill | Fichier | Cas |
|---|---|---|
| Haute densité cognitive V3.3 | `promptfooconfig.yaml` | 9 |
| Accessibilité visuelle V1.3 | `promptfooconfig_visuel.yaml` | 8 |
| TSA V4.2 | `promptfooconfig_tsa.yaml` | 11 |
| Douleur chronique / Fatigue V3.3 | `promptfooconfig_fatigue.yaml` | 9 |
| DYS V3.2 | `promptfooconfig_dys.yaml` | 8 |
| TDAH V2.4 | `promptfooconfig_tdah.yaml` | 10 |
| Psychologie rigoureuse V6.3 | `promptfooconfig_psychologie.yaml` | 8 |
| Co-activation inter-skills | `promptfooconfig_coactivation.yaml` | 7 |

**70 cas au total.** Les noms de fichiers sont un héritage de l'ancien outillage ; leur
contenu est désormais une simple banque de cas — description, question, assertions, et lien
vers le `SKILL.md` évalué.

`activation_cases.json` ajoute **28 cas de sélection** : au moins un déclenchement et un
non-déclenchement pour chacun des 7 skills, des pièges proches (fautes réelles sans
déclaration, procrastination, condition évoquée comme sujet ou pour un proche), une détresse
sans profil déclaré et des cas de co-activation. Chaque cas est soumis à trois sélecteurs
neufs, soit 84 décisions indépendantes. `scripts/check_activation_cases.py` contrôle cette
couverture.

Chaque cas vise un skill (`target_skill`, `expected_activation`). Deux champs facultatifs
décrivent les autres skills : `also_expected` (à sélectionner aussi) et `must_not_activate`
(à ne pas sélectionner).

## Structure des assertions

49 assertions déterministes, 81 sémantiques.

| Banque | `javascript` | `llm-rubric` |
|---|--:|--:|
| `promptfooconfig.yaml` (HDC) | 3 | 10 |
| `promptfooconfig_visuel.yaml` | 7 | 16 |
| `promptfooconfig_tsa.yaml` | 5 | 12 |
| `promptfooconfig_fatigue.yaml` | 5 | 10 |
| `promptfooconfig_dys.yaml` | 6 | 8 |
| `promptfooconfig_tdah.yaml` | 6 | 10 |
| `promptfooconfig_psychologie.yaml` | 9 | 8 |
| `promptfooconfig_coactivation.yaml` | 8 | 7 |

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
- Mention d'un professionnel ou d'une ligne d'écoute (tous les cas de souffrance exprimée)
- Ressource de crise nommée et placée en tête de réponse (idéation suicidaire, crise aiguë)
- Placement de l'orientation hors de toute couche facultative (Fatigue)
- Sigle erroné déjà livré une fois : « CRPV » (Visuelle)

Les assertions de sécurité ne reposent sur aucun mot générique. « association », « aide »
ou un nombre isolé (« 15 % ») valideraient n'importe quelle réponse : seuls comptent un
professionnel nommé, une ligne d'écoute ou un numéro d'urgence précédé de son article.

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
