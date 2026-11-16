# Essais exploratoires du candidat accessibilite-numerique

Date : **16 novembre 2026**. Base de travail : `972effb` récupéré depuis `origin/main`.

Skill examiné : `skills/accessibilite-numerique/SKILL.md`, V0.1 candidate.
Empreinte SHA-256 :
`b0703ad696bccc88fc7e801410416dcd18ff084dc3ac4e6d34e6c336d081508e`.

## Portée

Ces essais servent à examiner des décisions et des livrables réalistes avant
revue. **Ce n'est pas une vague de validation** : pas de baseline appariée, pas
de sélection par trois agents neufs pour chaque cas, pas de jugement A/B en
aveugle. Ils n'appuient aucune promotion ni publication. Les 85 cas de la banque
ont été contrôlés structurellement ; ils n'ont pas tous été exécutés.

Trois agents distincts en contextes neufs ont reçu la demande et le ou les
skills nécessaires, sans recevoir les résultats attendus des banques. Leurs
sorties synthétiques sont conservées localement sous
`eval/runs/20261116-forward-numerique/`, ignoré par Git.

## Observations

| Essai | Résultat observé | Limites |
|---|---|---|
| Formulaire de réservation autonome | Fichier HTML complet, libellés associés, erreurs reliées aux champs, synthèse d'erreurs et confirmation locale explicitement distinguée d'une réservation réelle. | Inspection structurelle et vérifications locales du script ; aucun parcours navigateur ou lecteur d'écran validé. |
| Rapport annuel et demande de certification fondée sur un OCR | Source HTML structurée, tableaux avec en-têtes, données manquantes marquées sans invention. La remise refuse un taux RGAA et une certification PDF/UA non établis. | Aucun PDF produit ou inspecté, aucun audit RGAA ni contrôle PDF/UA. |
| Co-activation DYS et fiche de bénévoles complète | Fichier HTML complet et commentaire séparé de 174 mots. Informations absentes signalées ; formulaire de retour local sans transmission automatique. | Contrastes calculés, structure inspectée et logique du script simulée ; aucun téléchargement réel, parcours clavier, zoom ou lecteur d'écran validé. |

Les deux modèles de documents conservent les informations à compléter : ce sont
des sources de travail, pas des documents prêts à diffuser en l'état. Les
mesures de contraste sur les couleurs CSS ne prouvent pas le rendu de tous les
états et contextes. Un essai Chrome pour le formulaire a été borné après absence
de réponse et n'est pas compté comme un test réussi.

Le vérificateur local du formulaire rapporte 42 assertions réussies sur la
structure, les contrastes sélectionnés et les branches du script exécuté avec
une doublure DOM. Ce nombre inclut des préconditions et des répétitions : ce
ne sont ni 42 critères WCAG validés ni 42 scénarios indépendants. La simulation
ne vérifie pas les annonces d'une technologie d'assistance ou le focus réel.

Une quatrième lecture indépendante a examiné le diff, le nouveau skill, les
référentiels, les banques et les trois exemples. Aucun défaut bloquant n'a été
identifié ; une incohérence terminologique « plugin »/« skills individuels » a
été corrigée dans le document de recherche. Cette lecture n'a pas revérifié
les normes sur le web et ne constitue pas un audit d'accessibilité.

## Contrôles du dépôt

- `validate_skills.py` : huit skills valides, bloc canonique de préséance identique.
- `quick_validate.py` du skill-creator : nouveau skill valide.
- `check_eval_configs.py --require-node` : neuf banques, 85 cas, 49 assertions
  JavaScript compilables et 127 rubriques sémantiques.
- `check_eval_leaks.py` : aucune question au-dessus des seuils de recopie.
- `check_activation_cases.py` : 38 cas, couverture positive et négative des huit skills.
- `check_evidence.py --base origin/main` : candidat sans promotion ; aucune preuve
  de vague revendiquée. Le contrôle doit aussi être exécuté après commit, car
  son analyse des changements compare les commits et non l'arbre non commité.
- Build existant exécuté : huit ZIP ; chaque archive contient uniquement son
  `<nom>/SKILL.md`, dont les octets correspondent à la source.
- `git diff --check` : aucune erreur de blancs.

Les sept `SKILL.md` préexistants ne sont pas modifiés. Le build inclut les
candidats : une archive générée ne vaut pas autorisation de promotion ou preuve
de préparation à une release.

## Condition avant promotion

Exécuter le protocole `eval/prompt_benchmark_claude_code.md` sur l'état final,
avec sélection indépendante, conditions avec/sans skill, trois juges en aveugle
et recherche des régressions. Conserver les artefacts bruts localement et
versionner le paquet assaini requis dans `eval/evidence/`. Vérifier les parcours
réels et les formats finaux concernés ; aucun essai ciblé ne garantit
l'accessibilité de tous les livrables futurs.
