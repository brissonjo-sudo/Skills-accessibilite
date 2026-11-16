# Référentiels pour créer des livrables numériques accessibles

Recherche vérifiée le **16 novembre 2026** sur les sources officielles liées ci-dessous.

Ce document prépare l'extension de l'écosystème à l'accessibilité des créations :
interfaces, contenus, documents et médias. Il ne détermine pas l'assujettissement
juridique d'un organisme et ne constitue ni un audit ni une preuve de conformité.
Le comportement du skill reste défini par son `SKILL.md`.

## Choisir le référentiel selon le livrable

| Référentiel | État vérifié | Utilisation technique |
|---|---|---|
| [WCAG 2.2](https://www.w3.org/TR/WCAG22/) | Recommandation W3C, édition actuelle du 12 décembre 2024. | Cible de conception pour le web : niveaux A et AA, sauf objectif différent explicitement défini. |
| [WCAG 3](https://www.w3.org/WAI/standards-guidelines/wcag/wcag3-intro/) | Brouillon incomplet, susceptible de changements importants. | Veille ; aucune revendication de conformité WCAG 3. Le W3C conseille de satisfaire WCAG 2.2 dès maintenant. |
| [RGAA 4.1.2](https://accessibilite.numerique.gouv.fr/) | Version affichée par la DINUM, avec 106 critères de contrôle. | Méthode technique française pour les pages web ; conserver ses critères et leur numérotation lorsqu'un audit RGAA est demandé. |
| [RGAA 5](https://design.numerique.gouv.fr/articles/2026-03-02-rgaa5/) | En rédaction, publication annoncée fin 2026. | Anticipation, sans appliquer un contenu non publié ni retarder les améliorations actuelles. |
| [EN 301 549 V4.1.1](https://www.etsi.org/deliver/etsi_en/301500_301599/301549/04.01.01_60/en_301549v040101p.pdf) | Édition publiée en septembre 2026. | Exigences d'accessibilité des produits et services TIC ; chapitres 9 pour le web, 10 pour les documents hors web, 11 pour les logiciels. Cette édition utilise WCAG 2.2. |
| [WCAG2ICT](https://www.w3.org/TR/wcag2ict-22/) | Note de groupe W3C du 11 décembre 2025, informative et non normative. | Aide à l'interprétation des critères WCAG pour les documents et logiciels hors web ; pas de conformité autonome « WCAG2ICT ». |
| [PDF/UA-1, ISO 14289-1:2014](https://www.iso.org/standard/64599.html) | Norme publiée, toujours courante, confirmée en 2025. | Accessibilité des PDF fondés sur PDF 1.7. |
| [PDF/UA-2, ISO 14289-2:2024](https://www.iso.org/standard/82278.html) | Norme publiée en mars 2024. | Accessibilité des PDF fondés sur PDF 2.0 ; choisir selon les capacités de production et de lecture. |

Une nouvelle édition **publiée** n'est pas automatiquement la version de référence
**harmonisée et citée au JOUE pour un texte donné**. Ce document ne vérifie pas cette
citation ni les obligations d'un cas particulier. Une analyse juridique doit vérifier
séparément le texte applicable, la version citée, les dates et le périmètre concerné.
Ne pas déduire une conformité RGAA d'une seule vérification WCAG 2.2, ni l'inverse.

PDF/UA-2 ne remplace pas universellement PDF/UA-1 : leur socle PDF diffère. La
[table des normes de la PDF Association](https://pdfa.org/pdf-standards/) explicite
la correspondance entre éditions PDF/UA et versions PDF.

## Positionner l'écosystème comme aide à la création

Les [ATAG 2.0](https://www.w3.org/WAI/standards-guidelines/atag/) distinguent
l'accessibilité de l'outil lui-même, partie A, et son aide à la production de contenus
accessibles, partie B. Cette seconde intention correspond au nouveau besoin de
l'écosystème : proposer des choix accessibles, préserver les informations d'accessibilité
et aider l'auteur à repérer puis corriger les obstacles.

Ce rapprochement est un choix de conception du projet, sans revendication de
conformité ATAG de l'écosystème. Le dépôt distribue des skills individuels, sans
manifeste de plugin installable en bloc. L'accessibilité de l'interface hôte reste à évaluer
séparément. Les besoins du destinataire d'un livrable ne se déduisent pas du profil
de son auteur : les adaptations de la conversation et la qualité du livrable sont
deux périmètres distincts.

## Web et applications web

Le socle doit porter sur le livrable et ses parcours complets, y compris les états
d'erreur, chargement, ouverture et fermeture des composants.

- Employer une structure sémantique : régions, titres hiérarchisés et éléments
  correspondant aux actions. Les [conseils W3C sur la structure](https://www.w3.org/WAI/tutorials/page-structure/)
  expliquent le lien entre balisage et navigation assistée.
- Associer explicitement les cellules de données à leurs en-têtes ; une grille
  visuelle ne suffit pas. Voir le [tutoriel des tableaux](https://www.w3.org/WAI/tutorials/tables/).
- Vérifier les noms accessibles, alternatives des images, libellés et instructions
  de formulaire ; rendre les erreurs et changements de statut perceptibles.
  Contrôler l'accès clavier, l'ordre du focus et l'absence de piège. Les critères
  correspondants figurent dans [WCAG 2.2](https://www.w3.org/TR/WCAG22/).
- Mesurer le contraste du texte : **4,5:1**, ou **3:1** pour du grand texte, défini
  par au moins 18 points ou 14 points gras. Appliquer les exceptions du critère,
  notamment pour les logos et éléments inactifs. Voir [1.4.3](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html).
- Vérifier **3:1** pour les informations visuelles nécessaires à l'identification
  des composants, états et objets graphiques concernés, en tenant compte des
  exceptions : [1.4.11](https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast.html).
- Tester l'agrandissement du texte à **200 %** sans perte de contenu ou de fonction,
  selon les exceptions de [1.4.4](https://www.w3.org/WAI/WCAG22/Understanding/resize-text.html).
  Tester séparément le réagencement à **320 pixels CSS de largeur**, avec les
  exceptions pour les contenus dont la disposition bidimensionnelle est nécessaire :
  [1.4.10](https://www.w3.org/WAI/WCAG22/Understanding/reflow.html).
- Conserver un focus visible ; vérifier aussi qu'il n'est pas entièrement caché
  par un contenu créé par l'auteur, par exemple une barre fixe :
  [2.4.11](https://www.w3.org/WAI/WCAG22/Understanding/focus-not-obscured-minimum.html).
  Ne pas confondre cette exigence AA avec les exigences renforcées AAA de 2.4.13.
- Pour le pointeur, viser au moins **24 × 24 pixels CSS**, ou satisfaire une
  exception telle que l'espacement suffisant ou les liens intégrés au texte :
  [2.5.8](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html).
  Le seuil 44 × 44 appartient au critère renforcé AAA, pas au minimum AA universel.
- Pour l'authentification, permettre les mécanismes d'assistance pertinents,
  notamment gestionnaire de mots de passe et collage ; examiner les conditions
  et exceptions de [3.3.8](https://www.w3.org/WAI/WCAG22/Understanding/accessible-authentication-minimum.html).

Cette sélection sert à concevoir et à préparer les tests. Elle n'est pas une liste
exhaustive des critères nécessaires à une conformité A ou AA.

## Applications mobiles et logiciels hors web

Utiliser le chapitre 11 de l'EN 301 549 et la note WCAG2ICT pour le cadrage.
Appliquer ensuite les recommandations de la plateforme : noms, rôles, valeurs,
états, regroupements et actions doivent être exposés par ses mécanismes
d'accessibilité. Ne pas transposer mécaniquement des attributs HTML/ARIA dans
une interface native.

Les guides [Apple VoiceOver](https://developer.apple.com/design/human-interface-guidelines/voiceover)
et [Android Accessibility](https://developer.android.com/guide/topics/ui/accessibility/principles)
donnent des exemples de libellés, de sémantique et d'interactions. Vérifier les
parcours avec les technologies réellement visées, le réglage de taille du texte
et les modes d'entrée pris en charge. Un contrôle qui ressemble visuellement à
un bouton ne prouve pas qu'il est annoncé ou actionnable comme tel.

## Documents, PDF, présentations et tableurs

Le chapitre 10 de l'EN 301 549 et WCAG2ICT fournissent le cadrage hors web.
Les recommandations des éditeurs ci-dessous sont des aides de réalisation,
pas des certifications.

| Livrable | Prévoir lors de la création | Vérifier sur le fichier livré |
|---|---|---|
| Document texte | Styles de titre réels, ordre logique, liens explicites, tableaux avec en-têtes, alternatives pertinentes. | Navigation par titres, lecture linéaire, tableaux et images. [Guide Word](https://support.microsoft.com/fr-fr/accessibility/word/make-your-word-documents-accessible-to-people-with-disabilities). |
| Présentation | Titre identifiable pour chaque diapositive, ordre logique des objets, alternatives et contenus compréhensibles sans la seule couleur. | Ordre de lecture effectif, objets ignorés ou décoratifs et médias intégrés. [Volet Ordre de lecture PowerPoint](https://support.microsoft.com/fr-fr/powerpoint/make-slides-easier-to-read-by-using-the-reading-order-pane). |
| Tableur | Noms de feuilles explicites, tables simples avec en-têtes, structure sans fusions inutiles, descriptions des graphiques. | Parcours au clavier et au lecteur d'écran ; lecture des tables, libellés et informations des graphiques. [Guide Excel](https://support.microsoft.com/fr-fr/accessibility/excel/accessibility-best-practices-with-excel-spreadsheets). |
| PDF | Source structurée, export préservant les informations d'accessibilité, cible PDF/UA choisie selon la chaîne utilisée. | Balises sémantiques et ordre de lecture, y compris les éléments interactifs. [Technique W3C PDF3](https://www.w3.org/WAI/WCAG22/Techniques/pdf/PDF3.html). |

L'export doit être contrôlé séparément de la source : des informations peuvent
disparaître pendant la conversion. Microsoft distingue explicitement la préparation
du document et la préservation de son accessibilité lors de l'export
[Word vers PDF](https://learn.microsoft.com/fr-fr/office/pdf/word/wordpdfaccessibility)
ou [Excel vers PDF](https://learn.microsoft.com/fr-fr/office/pdf/excel/excelpdfaccessibility).

Un rendu correct à l'écran, la présence de texte sélectionnable ou un OCR réussi
ne démontrent pas la qualité du balisage et de l'ordre de lecture. Si l'outil ne
permet pas de produire ou d'inspecter ces éléments, déclarer la limite et proposer
un format complémentaire adapté ; ne pas annoncer « PDF/UA conforme ».

## Images, graphiques, audio et vidéo

Fournir une alternative qui restitue l'information utile dans son contexte ; pour
un graphique, rendre également accessibles les données ou relations nécessaires
à sa compréhension. Le guide [Apple VoiceOver](https://developer.apple.com/design/human-interface-guidelines/voiceover)
illustre aussi le traitement des graphiques et infographies interactifs.

Le [guide médias du W3C](https://www.w3.org/WAI/media/av/) distingue notamment
transcription, sous-titrage et description des informations visuelles. Choisir selon
le type de média, son caractère préenregistré ou direct et l'information déjà
présente dans la bande sonore. Des sous-titres doivent transmettre les informations
sonores utiles ; une transcription ne remplace pas systématiquement le sous-titrage
ou l'audiodescription exigés par la cible retenue.

Des sous-titres automatiques constituent un brouillon à relire. Un fichier image
seul ne porte pas nécessairement l'alternative dans son contexte de publication :
livrer le texte associé et indiquer où l'intégrer.

## Vérifier sans fabriquer une conformité

Le [W3C sur l'évaluation](https://www.w3.org/WAI/test-evaluate/) précise qu'aucun
outil seul ne peut déterminer l'accessibilité d'un site. La revue humaine reste
nécessaire. Le choix des outils dépend du format, du périmètre et des critères :
voir [sélectionner des outils d'évaluation](https://www.w3.org/WAI/test-evaluate/tools/selecting/).

Pour ce projet, une restitution utile associe chaque constat à son périmètre,
au référentiel et au critère, à une méthode, puis à une preuve observable :

| Nature du contrôle | Exemple de preuve ou de limite |
|---|---|
| Automatique exécuté | Outil et version, fichier ou page, règle, résultat et date. |
| Inspection humaine effectuée | Élément examiné et observation ; ne pas présenter une inspection statique comme un essai interactif. |
| Essai de parcours effectué | Environnement, technologie d'assistance, étapes et résultat réel. |
| À vérifier | Outil indisponible, lecteur d'écran non utilisé, contenu tiers ou état non testé. |
| Non applicable | Précondition absente, avec justification liée au critère. |

Exemples de contrôles complémentaires : mesure des contrastes, analyse de structure,
parcours clavier, lecture des alternatives et vérification de l'ordre de lecture.
Adapter l'échantillon et couvrir les parcours complets plutôt que la seule page
d'accueil. Un résultat sans erreur détectée ne vaut pas audit complet ; un score
d'outil ne se convertit pas en pourcentage global de conformité.

Les tests comportementaux du skill évaluent sa capacité à produire et vérifier
des livrables avec des limites honnêtes. Ils ne prouvent pas l'accessibilité de
tous ses futurs livrables. Recontrôler les versions des référentiels avant toute
revendication formelle, mise à jour normative ou préparation d'audit.
