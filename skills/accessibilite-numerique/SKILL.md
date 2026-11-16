---
name: accessibilite-numerique
description: >-
  Concevoir, créer, modifier ou examiner l'accessibilité d'un livrable numérique
  destiné à être lu ou utilisé par des personnes : site, interface d'application,
  formulaire, document, PDF, présentation, tableur, graphique ou média.
  S'applique à ces tâches même sans demande explicite d'accessibilité et sans
  déclaration de handicap. Guide la réalisation selon WCAG, RGAA et les
  référentiels adaptés au format, puis distingue contrôles effectués et limites.
  Ne s'active pas pour une simple explication sans livrable, une adaptation de la
  conversation seule, un backend sans interface ni contenu utilisateur, ou
  l'accessibilité au sens du prix ou du transport. N'infère aucun profil personnel
  et ne certifie jamais la conformité sur la seule base d'une génération.
---

# Accessibilité des créations numériques

Rendre le livrable utilisable par ses publics, en conservant son contenu utile,
ses fonctions et les choix de l'utilisateur. Ce skill porte sur la structure et
les interactions du livrable ; les autres skills adaptent la conversation.

## Déclenchement et application

Appliquer silencieusement lors d'une création, modification ou revue d'un
livrable numérique destiné à des personnes. Une demande ordinaire de page web,
de formulaire, de diaporama ou de document suffit : aucun handicap n'est requis.
Une revue explicitement consacrée à l'accessibilité entre également dans ce périmètre.

Une question de définition, une explication technique, une opération purement
serveur ou une préférence de réponse courte ne déclenchent pas ce skill seules.
Une déclaration de handicap peut déclencher un autre skill, pas celui-ci à elle seule.
Ne jamais demander un diagnostic, inférer un trouble ou collecter un profil
médical pour choisir une mise en forme. Demander plutôt les contraintes utiles
du livrable lorsqu'elles ne sont pas connues.

## Cadrer sans bloquer la création

Identifier le format, le public, les parcours et le support final, à partir de
la demande et des fichiers disponibles. Conserver la stack et les outils choisis.
Demander une précision seulement si son absence empêche un choix pertinent ;
sinon avancer avec une hypothèse indiquée brièvement.

Intégrer l'accessibilité dans le résultat demandé. Une liste de recommandations
ne remplace pas un fichier ou une correction que l'environnement permet de produire.
Pour une modification ciblée, corriger ce périmètre et signaler les problèmes
observés ailleurs sans imposer une refonte générale.

## Choisir le référentiel

Socle technique vérifié le **16 novembre 2026** ; revérifier les versions et le
statut des textes avant une demande de conformité formelle ou une évolution normative.

- **Web** : viser les critères applicables des niveaux A et AA de
  [WCAG 2.2](https://www.w3.org/TR/WCAG22/), sauf cible contractuelle explicite
  différente. Une sélection de règles ci-dessous ne couvre pas tous les critères.
- **Audit RGAA demandé** : utiliser les critères, tests et modalités du
  [RGAA 4.1.2](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/).
  WCAG 2.2 ne remplace pas cette méthode. RGAA 5 annoncé et WCAG 3 en brouillon
  ne sont pas des référentiels publiés à substituer au RGAA en vigueur.
- **Logiciels et documents hors web** : sélectionner les exigences pertinentes
  d'[EN 301 549](https://www.etsi.org/deliver/etsi_en/301500_301599/301549/04.01.01_60/en_301549v040101p.pdf),
  V4.1.1 publiée en septembre 2026, notamment chapitres 10 et 11.
  [WCAG2ICT](https://www.w3.org/TR/wcag2ict-22/) aide à interpréter WCAG hors web ;
  c'est une note informative, pas une norme de conformité autonome.
- **PDF** : choisir PDF/UA-1 (ISO 14289-1, PDF 1.7) ou PDF/UA-2
  (ISO 14289-2:2024, PDF 2.0) selon la chaîne d'export et les lecteurs cibles.
  Ne pas changer de format uniquement parce qu'une édition est plus récente.
- **Outil de création** : [ATAG 2.0](https://www.w3.org/WAI/standards-guidelines/atag/)
  distingue l'accès à l'outil (partie A) et son aide à la production de contenus
  accessibles (partie B). Préserver les alternatives lors des conversions et éditions.

Distinguer version publiée, référence contractuelle et éventuelle référence
juridique applicable. Ne pas déduire l'assujettissement d'une organisation à partir
de sa seule activité, ni déclarer une conformité réglementaire sans vérification
du contexte et des textes officiels pertinents.

## Web et interfaces

Choisir le HTML natif approprié avant ARIA. Un bouton exécute une action, un lien
navigue. Conserver noms, rôles, états et valeurs accessibles ; un attribut ARIA ne
crée ni comportement clavier ni gestion du focus. Ne pas masquer un contrôle
interactif aux technologies d'assistance. Pour une application native, utiliser
les composants et API d'accessibilité de sa plateforme et tester leur exposition.

- Structurer titres, régions, listes et tableaux selon leur sens ; définir la
  langue principale et les changements de langue utiles. Donner aux liens un
  intitulé compréhensible dans leur contexte. Associer les en-têtes aux cellules.
- Prévoir une alternative pertinente pour une image informative ; une image
  purement décorative a une alternative vide dans le HTML. Pour un graphique,
  fournir les conclusions utiles et un accès aux données ou leur équivalent.
  Ne pas inventer les données ou le contenu d'une image non inspectée.
- Permettre tous les parcours au clavier, avec ordre logique, focus visible,
  absence de piège et focus non entièrement masqué. Prévoir un moyen de contourner
  les blocs répétés. Pour une boîte de dialogue, traiter entrée, sortie et retour
  du focus ; une apparence de modale ne suffit pas.
- Associer un libellé persistant à chaque champ ; le placeholder ne le remplace
  pas. Relier aides et erreurs aux champs, décrire les corrections et conserver
  les valeurs déjà saisies. Exposer les messages de statut sans déplacement de
  focus inutile. Ne pas faire reposer l'authentification sur un test cognitif sans
  alternative ou mécanisme d'assistance satisfaisant le critère applicable.
- Mesurer le contraste du texte : **4,5:1**, ou **3:1** pour du grand texte
  (au moins 18 points, ou 14 points en gras), avec les exceptions de 1.4.3.
  Pour les composants et objets graphiques concernés par 1.4.11, viser **3:1**
  entre les couleurs adjacentes pertinentes ; pas pour toute décoration.
  Ne jamais transmettre une information uniquement par la couleur.
- Vérifier texte agrandi à **200 %**, réagencement à **320 pixels CSS de largeur**
  pour les contenus concernés et espacement personnalisé sans perte de contenu.
  Les tableaux ou cartes nécessitant deux dimensions ont des exceptions ; elles
  ne dispensent pas le reste de la page de se réagencer.
- Pour 2.5.8, prévoir des cibles d'au moins **24 × 24 pixels CSS**, ou satisfaire
  son espacement ou une autre exception applicable. **44 × 44** est une cible
  renforcée, pas un minimum AA universel. Offrir une alternative au glisser-déposer.
- Permettre de suspendre les animations et contenus en mouvement concernés ;
  respecter les préférences de réduction des mouvements. Éviter les flashs à
  risque. Ne pas présenter la préférence de mouvement comme couvrant à elle seule
  toutes les exigences sur les animations et limites de temps.

## Documents, présentations et tableurs

Créer une structure réelle, conservée dans le format final, plutôt que simuler
des titres ou colonnes avec du gras et des espaces. Définir titre et langue du
document quand le format le permet. Utiliser liens explicites, listes natives,
contrastes suffisants et alternatives adaptées aux images.

- **Texte et PDF** : styles de titres hiérarchisés, tableaux avec en-têtes et
  ordre de lecture cohérent. Exporter un PDF balisé, puis vérifier les balises,
  alternatives, langue, ordre de lecture et navigation dans le fichier exporté.
  Une capture, un OCR ou un texte sélectionnable ne suffisent pas à prouver
  l'accessibilité. Si l'outil ne conserve pas les balises, fournir une source
  structurée accessible et signaler que le PDF nécessite une remédiation.
- **Diaporama** : titre distinct et pertinent par diapositive, ordre de lecture
  des objets contrôlé, texte réel plutôt qu'image de texte lorsque possible,
  informations des graphiques disponibles autrement que par la couleur.
  Vérifier à nouveau les propriétés après conversion en PDF.
- **Tableur** : noms explicites des feuilles, tableaux de données identifiables,
  en-têtes cohérents, navigation compréhensible, unités et erreurs explicites.
  Éviter les cellules fusionnées et les lignes vides utilisées pour dessiner une
  structure dans les zones de données. Ne pas casser les formules pour simplifier
  la présentation. Associer aux graphiques une description et les données utiles.

## Médias et contenus éditoriaux

Choisir les alternatives selon le média et son contenu : sous-titres synchronisés
incluant les sons utiles pour la vidéo avec audio, transcription pour l'audio,
et audiodescription des informations visuelles indispensables non données dans
la bande sonore lorsque le critère applicable l'exige. Une transcription seule
ne remplace pas les sous-titres synchronisés d'une vidéo préenregistrée.
Vérifier aussi commandes du lecteur, clavier et absence de lecture automatique
gênante. Si les médias sources sont absents, préparer le dispositif et nommer les
éléments restant à produire sans inventer de transcription.

Rendre les textes compréhensibles : consignes explicites, intitulés prévisibles,
erreurs utiles. Préserver la précision et le contenu demandé. Le langage clair
est une aide ; ne pas promettre qu'il satisfait tous les besoins cognitifs ni
appeler un texte « FALC validé » sans le processus de validation adapté.

## Vérifier le résultat et rendre compte

Adapter les contrôles au format et à l'outillage réellement disponible. Ne pas
installer un outil, transmettre un document ou modifier un service externe sans
l'autorisation pertinente. Aucun accès à un compte ni envoi de données de santé
n'est nécessaire par principe pour appliquer ces règles.

Combiner quand possible analyse automatique, inspection structurelle et essais
humains : parcours clavier, zoom/réagencement, mesure des contrastes et parcours
avec technologies d'assistance. Vérifier le livrable final, pas seulement son code
source ou un aperçu visuel. Pour un audit, documenter le périmètre, les pages,
états et parcours examinés, le référentiel et les exclusions justifiées.

Associer chaque constat à une localisation, un impact, une règle applicable et
une correction concrète. Séparer **contrôlé** (méthode et résultat), **à vérifier**
(méthode proposée), **non applicable** (raison) et **limite d'outil**. Ne pas
présenter une inspection de code comme un essai au clavier ou lecteur d'écran.

Un score automatique, zéro erreur détectée, ou un fichier généré ne prouvent pas
la conformité globale. Ne pas inventer un taux RGAA, une certification PDF/UA,
une déclaration d'accessibilité auditée ou un résultat de test non exécuté.
Fournir au besoin un modèle portant clairement les champs restant à vérifier.

## Co-activation : conversation et livrable

Les adaptations personnelles régissent l'explication et la remise du travail.
Les critères techniques régissent le livrable destiné à son public. Ne pas
tronquer un formulaire, supprimer les alternatives d'un graphique ou retirer
des informations nécessaires d'un document pour tenir un plafond de réponse.

Quand un plafond personnel est actif, remettre si possible le livrable complet
dans un fichier, avec un commentaire court respectant ce plafond. Si aucun
fichier ne peut être remis et que le contenu complet dépasse le plafond,
proposer un découpage ou demander le format de remise avant de prétendre livrer
l'ensemble. Ne pas cacher les limites de validation dans une couche facultative.
Un besoin personnel de lecture linéaire n'interdit pas un graphique destiné à
un autre public : conserver son équivalent textuel et une remise accessible.

## Ordre de préséance entre skills

Quand plusieurs skills de cet écosystème sont actifs simultanément, l'ordre de préséance sur la **forme** est :

1. **Sécurité éthique** (commune à tous, prime toujours).
2. **`accessibilite-visuelle`** (un rendu inaccessible annule tout le reste ; ses interdits — références visuelles non autonomes, emojis décoratifs — priment sur les règles de mise en forme des autres skills, y compris le gras de `accessibilite-tdah`).
3. **Skills de réduction de charge** : `accessibilite-dys`, `accessibilite-tdah`, `accessibilite-douleur-chronique-fatigue-cognitive` (en cas de conflit entre eux, choisir la forme la plus économe en effort de lecture).
4. **`accessibilite-tsa`** (littéralité et prévisibilité, dans la limite de la charge fixée par les niveaux supérieurs).
5. **`accessibilite-haute-densite-cognitive`** (cède toujours face à un skill de réduction).

`psychologie-rigoureuse` régit le **fond**, jamais la forme : il se combine avec n'importe quel niveau ci-dessus sans entrer dans cet ordre.

## Auto-vérification avant remise

1. Le déclencheur est une tâche sur un livrable, sans inférence de handicap.
2. Le format, le périmètre et la cible normative sont identifiés sans surpromesse.
3. Le contenu, les fonctions et la stack demandés sont préservés.
4. Les structures, noms et alternatives sont présents dans le format final.
5. Les parcours interactifs ont un traitement clavier et focus pertinent.
6. Couleurs, contrastes, agrandissement et mouvements ont été examinés si applicables.
7. Les exports, données et médias conservent leurs alternatives utiles.
8. Les résultats observés sont séparés des vérifications restant à faire.
9. Aucun diagnostic, collecte médicale ou transfert externe gratuit n'est demandé.
10. La remise adaptée à l'utilisateur ne tronque pas le livrable complet.
11. Aucun statut de conformité ni test exécuté n'est inventé.
