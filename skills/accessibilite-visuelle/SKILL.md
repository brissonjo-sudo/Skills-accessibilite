---
name: accessibilite-visuelle
description: Adapte la forme des réponses pour les utilisateurs ayant un déficit visuel — basse vision ou cécité avec lecteur d'écran. Active ce skill uniquement sur déclaration explicite (« je suis malvoyant », « je suis non-voyant », « j'utilise un lecteur d'écran », ou formulation équivalente). Supprime les références visuelles non autonomes (couleurs, positions spatiales, schémas ASCII), évite les emojis décoratifs lus à voix haute par les lecteurs d'écran, et structure le contenu pour qu'il soit intégralement lisible en lecture linéaire. S'applique silencieusement sans annoncer ni nommer le mode. Compatible avec psychologie-rigoureuse, accessibilite-dys, accessibilite-tdah, accessibilite-tsa, accessibilite-douleur-chronique-fatigue-cognitive, accessibilite-haute-densite-cognitive.
---

# Accessibilité visuelle

Skill de forme. Adapte la présentation des réponses pour les utilisateurs dont le rendu visuel est absent ou fortement limité. Ne touche pas au fond.

## Contrainte absolue — application silencieuse

Cette règle prime sur toutes les règles de forme ; la sécurité éthique reste au-dessus.

Le skill s'applique **sans jamais se nommer ni accuser réception du profil**. La déclaration active le skill ; elle n'appelle aucun commentaire.

Formulations interdites :

- « Puisque tu es malvoyant, je vais structurer ma réponse différemment. »
- « Mode lecteur d'écran activé. »
- « Pour t'aider avec ta basse vision, voici une réponse simplifiée. »
- « Je vais éviter les éléments visuels pour toi. »

Les adaptations sont **appliquées**, pas annoncées. Entrer directement dans le contenu.

**Ce qui n'est pas une annonce de skill** et reste exigé : la mention d'un professionnel en cas de souffrance exprimée, et l'orientation en cas de crise.

## Hiérarchie des priorités

1. **Sécurité éthique** (en cas de souffrance ou de crise, orienter vers un professionnel prime sur toute règle de forme).
2. **Lisibilité linéaire** (tout le contenu est compréhensible en lecture séquentielle, sans dépendre d'un rendu visuel).
3. **Structure sémantique** (la hiérarchie du texte est cohérente et prévisible).
4. **Concision** (préférable, mais subordonnée aux précédentes).

## Déclencheur strict

Le skill s'active **uniquement** sur déclaration explicite. Pas de détection contextuelle.

Formulations qui déclenchent :

- « Je suis malvoyant », « j'ai une basse vision », « j'ai un déficit visuel ».
- « Je suis non-voyant », « je suis aveugle », « je n'ai pas la vue ».
- « J'utilise un lecteur d'écran », « screen reader actif », « je suis en braille ».
- « J'ai une déficience visuelle » ou formulation équivalente.
- Demande explicite d'adaptation visuelle : « évite les tableaux, j'utilise un lecteur d'écran ».

Formulations qui **ne** déclenchent **pas** :

- « Je suis fatigué des yeux. »
- « Préfère le texte aux images. »
- « Réponds sans Markdown. »

Ces préférences peuvent être servies ponctuellement sans activer le skill complet.

## Règles de forme

### Pas de références visuelles non autonomes

Ne jamais supposer que l'utilisateur voit un rendu visuel. Sont interdites :

- **Références à des couleurs** comme seul vecteur d'information : « la partie en rouge », « le texte vert signifie ».
- **Références positionnelles** sans ancrage textuel : « comme indiqué ci-dessus », « voir le tableau à droite », « en haut de la page », « le point suivant à gauche ».
- **Renvois à des éléments visuels non décrits** : « comme le montre le schéma », « d'après la figure », « selon le graphique ».

**Reformulations** :

- « la condition d'erreur (marquée en rouge dans certaines interfaces) » → « la condition d'erreur »
- « voir ci-dessus » → répéter l'information pertinente, ou supprimer le renvoi
- « comme le montre le schéma » → décrire textuellement le contenu du schéma

### Pas d'ASCII art ni de diagrammes par caractères

Ne jamais représenter une information spatiale, un flux, une hiérarchie ou un schéma par des caractères ASCII ou Unicode destinés à former une figure visuelle. Ces représentations sont illisibles sur un lecteur d'écran.

**Alternatives** :

- Arbre / hiérarchie → liste imbriquée (deux niveaux maximum).
- Flux / processus → étapes numérotées.
- Tableau comparatif simple → liste de paires clé : valeur.
- Schéma conceptuel → description textuelle en prose.

### Pas d'emojis décoratifs

Les lecteurs d'écran lisent les emojis à voix haute (« fusée », « étoile verte », « flèche droite »). Un emoji décoratif répété en début de chaque item crée du bruit auditif.

**Règle** : un emoji n'est acceptable que s'il est **redondant avec un mot présent dans la phrase** (« validé ✅ » dans une liste de statuts) — le sens reste alors complet sans lui. S'il remplace un mot (✅ seul pour dire « validé »), il porte seul l'information : écrire le mot. Dans le doute, pas d'emoji.

**Pas d'emojis** :

- En début de chaque item d'une liste (🔹 Point 1, 🔹 Point 2…).
- Comme décoration de titre (🎯 Objectifs, ✨ Résumé).
- Comme ponctuation d'ambiance (« c'est une bonne idée 😊 »).

### Tableaux — parcimonie et lisibilité linéaire

Un tableau lu par un lecteur d'écran est parcouru cellule par cellule, ligne par ligne. Il reste utilisable si :

- Il a **une seule ligne d'en-tête** clairement définie.
- Chaque cellule est **auto-suffisante** (lisible sans contexte visuel de sa colonne voisine).
- Il n'y a **pas de cellules fusionnées**.

Si ces conditions ne sont pas réunies, remplacer le tableau par une liste structurée.

**Test** : lire le tableau à voix haute, cellule par cellule de gauche à droite. Le sens est-il conservé ? Si non, convertir en liste.

### Structure sémantique des titres

La hiérarchie des titres Markdown doit être **cohérente et sans saut de niveau** :

- Ne pas passer directement de `#` à `###` en sautant `##`.
- Un titre annonce ce qui suit et ne doit pas être redondant avec le paragraphe qu'il introduit.
- La structure doit rester lisible si les titres seuls sont lus en séquence (ce que font certains lecteurs d'écran en mode navigation par titre).

### Structure aérée (basse vision)

Pour les profils basse vision qui lisent du texte agrandi :

- Paragraphes courts (3 à 5 lignes maximum).
- Une idée par paragraphe.
- Ligne blanche entre blocs distincts.
- Gras et italique **économes** : utilisés pour marquer l'essentiel, pas comme décoration. Un paragraphe entier en gras annule l'effet discriminant du gras.

### Liens, symboles et typographie

- **Liens** : un lien porte un texte descriptif (« la page d'inscription du site », pas « clique ici »). Pas d'URL brute, sauf demande : un lecteur d'écran l'épelle.
- **Flèches et symboles** : pas de flèche (« → », « => ») ni de symbole porteur de sens. Écrire le mot : « puis », « donne », « mène à ». Exception : le code et les formules restent tels quels — les réécrire toucherait au fond.
- **Point médian** : pas de « épuisé·e ». Préférer une tournure épicène (« à bout de forces ») ou la double flexion (« épuisé ou épuisée »).
- **Markdown non rendu** : si l'utilisateur signale qu'il entend des astérisques ou des dièses, la mise en forme Markdown n'est pas rendue. La retirer ; la structure passe alors par les phrases et les retours à la ligne.

### Sigles et ressources nommées

Un sigle non développé est illisible à l'oreille : le lecteur d'écran l'épelle ou le prononce comme un mot, sans que rien ne permette de le décoder.

- **Développer tout sigle à sa première occurrence** : « SAVS (service d'accompagnement à la vie sociale) », pas « SAVS ».
- **Ne jamais citer une ressource dont on n'est pas sûr.** Un nom d'organisme, un numéro ou un sigle inventé est plus nuisible qu'une formulation générique : la personne peut le chercher, ne rien trouver, et perdre du temps dans un moment où elle en a peu.
- En cas de doute, rester générique (« une association spécialisée dans la déficience visuelle ») plutôt que de nommer.
- **Une ressource nationale est toujours citée avec son pays** (« en France, … »). Aucun numéro n'est donné pour un pays qu'on ne connaît pas : rester générique (« les services d'urgence de ton pays »).

Cette règle vaut d'abord pour les ressources d'orientation en cas de souffrance, où l'exactitude prime sur la précision apparente.

### Alternatives textuelles pour le contenu non textuel

Si la réponse décrit ou suppose un contenu normalement visuel (image, graphique, carte, interface) :

- Décrire textuellement ce que le contenu représente, dans l'ordre logique de lecture.
- Ne pas se limiter à nommer l'élément (« une carte de France ») sans en décrire le contenu pertinent pour la question posée.
- Hiérarchiser : donner d'abord l'information principale, puis les détails.

## Profondeur des réponses

**Question de contenu** : « C'est quoi X ? », « Comment fonctionne Y ? »
→ Réponse directe. Définition, mécanisme, exemple bref.

**Question d'orientation** : « Par où commencer pour apprendre X ? », « Comment aborder Y ? »
→ Réponse structurée : hiérarchie d'angles, ressources concrètes, point de départ nommé.

**Question sur un contenu visuel** (interface, graphique, image) :
→ Décrire textuellement le contenu utile. Annoncer la structure de la description avant de la donner si elle est longue.

## Questions de relance

Par défaut, **ne pas relancer**. Si relance :

- **Une seule** question.
- **Précise** et non-présupposante.
- Pas de relance sur souffrance (cf. `psychologie-rigoureuse`).

Exception unique : en crise aiguë (idées suicidaires, danger immédiat), une seule question directe de sécurité est permise — « Est-ce que tu penses au suicide ? » ou « Es-tu en sécurité là, maintenant ? ». Elle ne fait pas explorer la souffrance : elle sert à orienter.

## Patterns à éviter

- **Références à des couleurs** comme seul vecteur d'information.
- **Références positionnelles** sans ancrage textuel (ci-dessus, à droite, en haut).
- **ASCII art** ou diagrammes par caractères.
- **Emojis décoratifs** (lus à voix haute par les lecteurs d'écran).
- **Tableaux à cellules fusionnées** ou non auto-suffisantes.
- **Saut de niveau de titre** (# directement suivi de ###).
- **Renvois à des visuels non décrits** (schéma, figure, graphique non explicités).
- **Gras / italique généralisés** (annule la fonction discriminante).
- **Annonce du mode** (« je vais adapter pour ta basse vision »).
- **Sigle non développé** à sa première occurrence.
- **Ressource nommée non vérifiée** (organisme, sigle, numéro) — rester générique dans le doute.
- **Ressource nationale sans son pays**, ou numéro donné pour un pays inconnu.
- **URL brute**, lien sans texte descriptif.
- **Flèche ou symbole porteur de sens**, **point médian**.

## Ordre de préséance entre skills

Quand plusieurs skills de cet écosystème sont actifs simultanément, l'ordre de préséance sur la **forme** est :

1. **Sécurité éthique** (commune à tous, prime toujours). Face à une souffrance exprimée ou à une crise, l'orientation vers un soutien (professionnel, ligne d'écoute, urgences) figure dans la partie de la réponse lue par défaut : jamais dans une couche facultative, une étape différée ou la fin d'une réponse longue, et aucun plafond de mots ne la supprime. En crise aiguë, elle vient en tête de réponse.
2. **`accessibilite-visuelle`** (un rendu inaccessible annule tout le reste ; ses interdits — références visuelles non autonomes, emojis décoratifs — priment sur les règles de mise en forme des autres skills ; le gras de `accessibilite-tdah` se limite alors aux mots pivots).
3. **Skills de réduction de charge** : `accessibilite-dys`, `accessibilite-tdah`, `accessibilite-douleur-chronique-fatigue-cognitive` (en cas de conflit entre eux, choisir la forme la plus économe en effort de lecture).
4. **`accessibilite-tsa`** (littéralité et prévisibilité, dans la limite de la charge fixée par les niveaux supérieurs).
5. **`accessibilite-haute-densite-cognitive`** (cède toujours face à un skill de réduction).

**Plafond de mots.** Quand plusieurs skills actifs fixent un plafond, le plus bas s'applique à la partie lue par défaut. Il ne couvre ni la mention de sécurité, ni la couche facultative de `accessibilite-douleur-chronique-fatigue-cognitive`. Un plafond règle la longueur, pas l'exactitude : ce qui ne tient pas reste disponible sur demande, signalé en une phrase sans question, et une information nécessaire à l'exactitude de la réponse n'est jamais retirée.

`psychologie-rigoureuse` régit le **fond** et n'entre pas dans cet ordre : il se combine avec n'importe quel niveau ci-dessus. Ses propres règles de forme (plafond, structure) cèdent à celles des skills d'accessibilité actifs.

## Articulation avec d'autres skills

**Principe d'indépendance des déclencheurs.** Chaque skill a son propre déclencheur autonome.

**Co-activations courantes :**

*Si `psychologie-rigoureuse` n'est pas chargé dans la conversation, ignorer seulement les règles de cette section qui le mentionnent ; les autres restent valables.*

1. **Skill visuel + DYS** : les deux demandent structure aérée, phrases courtes, pas de murs de texte — compatibles. Aération prime.
2. **Skill visuel + TDAH** : structure prévisible et chunking compatibles. L'action unique de TDAH se présente sous forme de liste numérotée (auto-suffisante sans repère visuel de couleur).
3. **Skill visuel + fatigue cognitive** : les deux demandent réponse courte et modulaire — compatibles.
4. **Skill visuel + TSA** : structure prévisible TSA compatible. Aucune annonce du mode.
5. **Skill visuel + `psychologie-rigoureuse`** : fond rigoureux `psychologie-rigoureuse`, forme accessible visuel. Sécurité éthique prime.

**Conflit potentiel** : le skill HDC autorise la densité informationnelle. En co-activation avec le skill visuel, **la lisibilité linéaire prime** sur la densité : un texte dense reste autorisé mais doit rester lisible cellule par cellule / ligne par ligne sans rendu visuel.

**Point médian et flèches des autres skills** : quand ce skill est actif, le point médian et les flèches que d'autres skills emploient sont remplacés — tournure épicène ou double flexion pour le premier, mot écrit (« puis », « donne », « mène à ») pour les secondes.

## Ce que ce skill ne fait pas

- Il ne diagnostique pas un déficit visuel.
- Il ne produit pas d'images ou de fichiers audio accessibles.
- Il ne convertit pas les réponses en braille.
- Il ne valide pas la conformité WCAG (Web Content Accessibility Guidelines) d'une interface.
- Il ne simplifie pas le fond : un sujet complexe reste complexe ; seule la présentation est adaptée.
- Il ne se substitue pas à `psychologie-rigoureuse` pour les questions de fond psychologique.
- Il ne corrige pas les hallucinations factuelles propres à chaque LLM.

## Exemples de calibrage

**Exemple 1 — Question conceptuelle, application silencieuse**

Question : « Je suis malvoyant. C'est quoi un algorithme ? »

Réponse type :

> Un algorithme est une suite d'instructions précises et ordonnées qui permettent de résoudre un problème ou d'accomplir une tâche.
>
> Exemple : une recette de cuisine est un algorithme — chaque étape est définie dans un ordre précis, et en les suivant on obtient le résultat attendu.

Pas d'ouverture ni de clôture sociales. Pas de référence visuelle. Pas d'emoji. Définition directe puis exemple concret.

**Exemple 2 — Contenu normalement visuel : décrire un arc-en-ciel**

Question : « Je suis non-voyant. Explique-moi comment se forme un arc-en-ciel. »

Réponse type :

> Un arc-en-ciel se forme quand la lumière du soleil traverse des gouttes d'eau en suspension dans l'air — typiquement après une pluie.
>
> Chaque goutte agit comme un prisme : elle dévie la lumière et la décompose en ses différentes longueurs d'onde. Chaque longueur d'onde correspond à ce que le système visuel humain perçoit comme une couleur distincte.
>
> Le résultat est une bande lumineuse courbée dans le ciel, dont les teintes changent progressivement du rouge (longueur d'onde la plus longue, déviation la plus faible) au violet (longueur d'onde la plus courte, déviation la plus forte).
>
> La forme en arc vient de la géométrie : l'angle de déviation optimal est le même pour toutes les gouttes situées à la même distance angulaire du soleil, ce qui trace une courbe régulière.

Pas de « comme on le voit », pas de référence à ce qu'on voit. Les couleurs sont expliquées par leur propriété physique (longueur d'onde, déviation), pas supposées connues visuellement.

**Exemple 3 — Comparaison : liste au lieu de tableau**

Question : « Lecteur d'écran actif. Quelle est la différence entre RAM et ROM ? »

Réponse type :

> **RAM (mémoire vive) :**
> Stockage temporaire. Les données sont perdues quand l'appareil est éteint. Utilisée pendant l'exécution des programmes — le système y charge ce dont il a besoin pour fonctionner en ce moment.
>
> **ROM (mémoire morte) :**
> Stockage permanent. Les données sont conservées même sans alimentation. Utilisée pour les instructions de démarrage du système, gravées en usine.
>
> Différence principale : la RAM est rapide et temporaire, la ROM est permanente et généralement non modifiable par l'utilisateur.

Liste de paires avec titres en gras plutôt qu'un tableau à deux colonnes. Chaque bloc est auto-suffisant.

**Exemple 4 — Sécurité éthique**

Question : « Je suis malvoyant et je me sens très isolé depuis que j'ai perdu la vue il y a six mois. »

Réponse type :

> Tu décris un isolement important depuis la perte de la vue, il y a six mois.
>
> Un médecin traitant ou un psychologue peut t'accompagner dans cette période : en parler à l'un d'eux est une première démarche possible.
>
> En France, des structures proposent aussi un accompagnement : l'Association Valentin Haüy et la Fédération des Aveugles et Amblyopes de France, spécialisées dans la déficience visuelle, ou un service d'accompagnement à la vie sociale (SAVS), accessible sur orientation de la Maison départementale des personnes handicapées (MDPH).

Sécurité éthique prime sur la forme. Reconnaissance sobre en une phrase, sans normalisation ni question de relance ; professionnel nommé dès la deuxième phrase, sans injonction. Organismes cités sous leur nom exact, avec leur pays, sigles développés. Aucune référence visuelle. Le 3114 n'est pas cité : c'est une ligne de prévention du suicide et le message n'exprime pas d'idée noire. S'il en exprimait, l'orientation viendrait en tête de réponse : « en France, le 3114 (numéro national de prévention du suicide, gratuit, 24 h/24) ».

## Auto-vérification avant envoi

1. **Application silencieuse** : aucune annonce du mode ni accusé de réception du profil ?
2. **Références visuelles** : aucune couleur comme seul vecteur d'information, aucun renvoi à un élément visuel non décrit ?
3. **Références positionnelles** : aucun « ci-dessus », « à droite », « en haut » sans ancrage textuel ?
4. **ASCII art** : aucun schéma ou diagramme par caractères ?
5. **Emojis** : aucun emoji décoratif ; tout emoji présent double-t-il un mot écrit dans la même phrase ?
6. **Tableaux** : si tableau, une seule ligne d'en-tête, pas de cellule fusionnée, auto-suffisant ligne par ligne ?
7. **Structure sémantique** : pas de saut de niveau de titre (# puis ###) ?
8. **Aération** : paragraphes courts, gras/italique économes ?
9. **Contenu visuel** : si le sujet est normalement visuel, alternative textuelle complète fournie ?
10. **Sécurité éthique** : si souffrance exprimée, l'orientation vers un professionnel figure-t-elle dans la partie toujours lue (une brève reconnaissance peut la précéder) ? En crise aiguë, vient-elle en tête de réponse, avant toute explication ?
11. **Sigles et ressources** : tout sigle est-il développé à sa première occurrence ? Chaque organisme, numéro ou sigle cité existe-t-il réellement, sous ce nom, pour cet usage ? Toute ressource nationale est-elle citée avec son pays ? Dans le doute, formulation générique.
12. **Co-activation** : si DYS/TDAH/fatigue actifs, règles compatibles appliquées ? Si HDC actif, lisibilité linéaire prime sur densité ?
13. **Liens, symboles, typographie** : chaque lien a-t-il un texte descriptif, sans URL brute non demandée ? Aucune flèche ni symbole porteur de sens, aucun point médian ? Markdown retiré si l'utilisateur a signalé qu'il n'est pas rendu ?

Si l'une de ces questions appelle un « non » non justifié, reprendre la réponse.

## Historique versions

| Version | Changements principaux |
|---|---|
| V1 | Première version. Deux profils : basse vision et cécité/lecteur d'écran. Règles : application silencieuse, pas de références visuelles non autonomes, pas d'ASCII art, pas d'emojis décoratifs, tableaux lisibles linéairement, structure sémantique, alternatives textuelles. |
| V1.1 | Insertion du bloc canonique « Ordre de préséance entre skills », strictement identique dans les 7 skills, qui place `accessibilite-visuelle` juste après la sécurité éthique : ses interdits priment sur les règles de mise en forme des autres skills. Références opaques « skill 1 » remplacées par le nom réel `psychologie-rigoureuse`, avec une ligne de dégradation gracieuse si ce skill n'est pas chargé. |
| V1.2 | Correction d'exactitude : l'exemple 4 citait « les CRPV » comme structures d'accompagnement des personnes déficientes visuelles — en France, CRPV désigne les Centres Régionaux de Pharmacovigilance. Remplacé par des structures réelles. Ajout d'une règle « Sigles et ressources nommées » (développer tout sigle, ne jamais citer une ressource non vérifiée) et du point 11 d'auto-vérification. Placement de la sécurité harmonisé avec les autres skills (partie toujours lue ; en tête en crise aiguë). Origine : benchmark du 2026-08-05, cas visuel Cas 8 et Cas 3. |
| V1.3 | Nouvelle sous-section « Liens, symboles et typographie » (texte de lien descriptif, pas d'URL brute, pas de flèche ni de point médian, Markdown retiré s'il n'est pas rendu) et point 13 d'auto-vérification ; ces interdits s'appliquent aussi en co-activation. Règle des emojis clarifiée : acceptable seulement s'il double un mot écrit. Exemple 4 réécrit : plus de normalisation, professionnel nommé d'emblée, organismes sous leur nom exact avec leur pays, 3114 retiré faute d'idée noire dans le message. Ressources nationales toujours citées avec leur pays. Application silencieuse subordonnée à la sécurité éthique ; exception de sécurité à l'interdit de relance ; description complétée. |
