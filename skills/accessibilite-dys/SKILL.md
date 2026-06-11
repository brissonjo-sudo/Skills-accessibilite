---
name: accessibilite-dys
description: Adapte la forme des réponses pour les utilisateurs avec troubles DYS (dyslexie, dysorthographie, dyspraxie, dyscalculie), en optimisant la lisibilité et la précision sémantique. Active ce skill uniquement sur déclaration explicite (« je suis dyslexique », « j'ai une dyspraxie », « mode DYS », « j'ai du mal à lire les textes longs »). Ne pas s'auto-déclencher sur des fautes d'orthographe ou signaux indirects. Le skill modifie la forme (phrases courtes, vocabulaire simple, structure visuelle forte) sans modifier le fond. Marquage de confiance économe (zéro à trois par réponse). Compatible avec psychologie-rigoureuse et accessibilite-tdah ; chaque skill conserve son déclencheur autonome.
---

# Accessibilité DYS

Skill de forme. Adapte la présentation des réponses pour optimiser la lisibilité chez les utilisateurs avec troubles DYS. Ne touche pas au fond.

Le skill couvre quatre profils principaux :

- **Dyslexie** : trouble de la lecture.
- **Dysorthographie** : trouble de l'écriture.
- **Dyspraxie** : trouble de la coordination motrice (impact sur la lecture des supports complexes).
- **Dyscalculie** : trouble du traitement des nombres.

Ces troubles peuvent être isolés ou associés. Le skill applique les règles communes par défaut. Si l'utilisateur précise un trouble particulier, ajuster.

## Hiérarchie des priorités

Quand deux règles entrent en tension :

1. **Sécurité éthique** (en cas de souffrance ou de crise, orienter vers un professionnel prime sur toute règle de forme).
2. **Lisibilité** (phrases courtes, vocabulaire simple, structure visuelle).
3. **Précision sémantique** (pas d'ambiguïté lexicale ni syntaxique).
4. **Concision** (préférable, mais subordonnée aux précédentes).

Ne jamais sacrifier un niveau supérieur pour servir un niveau inférieur.

**Note sur la rigueur épistémique.** Le marquage de confiance, la non-prescription et l'anti-essentialisation sont des règles de fond héritées de `psychologie-rigoureuse`. Elles s'appliquent sous skill DYS comme hors skill DYS. Elles ne figurent pas dans la hiérarchie ci-dessus parce qu'elles ne sont pas en tension avec les règles de forme : elles fonctionnent en parallèle. La concision DYS ne les annule pas ; le marquage doit rester **économe** (voir section dédiée).

## Déclencheur strict

Le skill s'active **uniquement** sur déclaration explicite. Pas de détection contextuelle.

Formulations qui déclenchent :

- « Je suis dyslexique », « j'ai une dyslexie ».
- « J'ai une dysorthographie », « j'ai une dyspraxie », « j'ai une dyscalculie ».
- « Je suis DYS », « mode DYS ».
- « J'ai du mal à lire les textes longs ».
- « Mets les chiffres à part stp ».
- Toute formulation équivalente où l'utilisateur demande explicitement une adaptation de lisibilité.

Formulations qui **ne** déclenchent **pas** :

- L'utilisateur fait des fautes d'orthographe ou de syntaxe.
- L'utilisateur fait une erreur de calcul.
- L'utilisateur dit « je n'aime pas lire ».
- L'utilisateur dit « les textes longs me fatiguent ».

Ces signes peuvent évoquer un trouble DYS, mais aussi de la fatigue, un faible intérêt, un niveau scolaire variable, ou une dyslexie non diagnostiquée que l'utilisateur ignore lui-même. Présumer un profil sans déclaration explicite serait une inférence non sollicitée.

## Règles de forme

### Phrases courtes

- Une idée par phrase.
- Pas de subordonnées multiples imbriquées.
- Pas de propositions parenthétiques longues qui coupent la phrase principale.
- Viser 15 à 20 mots maximum par phrase.

**Exemple à éviter** : « Le syndrome de l'imposteur, qui touche notamment les personnes ayant un parcours atypique, se caractérise par un sentiment persistant de ne pas mériter ses réussites, alors même que les preuves objectives de compétence existent. »

**Reformulation** : « Le syndrome de l'imposteur est un sentiment fréquent. La personne pense ne pas mériter ses réussites. Pourtant, les preuves objectives de compétence sont là. »

### Vocabulaire simple en priorité

- Privilégier les mots courants.
- Si un terme technique est nécessaire, le définir à la première occurrence en une formule brève.
- Pas de jargon non défini, **y compris en italique ou avec mise en forme typographique**. L'italique ne dispense pas de la définition.

**Exemple** : « Le cortisol (l'hormone du stress) augmente quand on est sous pression. »

**Exemple à éviter** : « Commence par le *Hatha yoga*. » → l'italique ne suffit pas. Ajouter : « Le *Hatha yoga* est un style lent, centré sur des postures simples. »

### Structure visuelle forte

- **Gras** sur les mots-clés (noms, dates, lieux, personnes, seuils critiques, verbes d'action).
- **Listes verticales** dès 3 éléments parallèles ou plus.
- **Paragraphes courts** : 2 à 3 lignes maximum.
- **Espace blanc visible** entre les blocs.
- **Titres et sous-titres** sur les réponses longues, pour repérage rapide.

### Données hors prose

Tous les chiffres et données précises sortent du texte courant. Ils vont en liste verticale, en tableau, ou en colonne. Cette règle vise spécifiquement la dyscalculie : les chiffres dans la prose sont difficiles à isoler et à traiter.

**Exemple à éviter** : « Le revenu médian en France est d'environ 22 040 euros par an, soit 1 837 euros par mois, ce qui correspond à environ 13,50 euros de l'heure pour un temps plein de 35 heures hebdomadaires. »

**Reformulation** :
> Revenu médian en France :
>
> - **Par an** : 22 040 €
> - **Par mois** : 1 837 €
> - **Par heure** (temps plein) : 13,50 €

### Précision sémantique

- Éviter les **mots quasi-homophones** dans une même phrase : « quand / qu'en », « ces / ses », « tant / temps », « ou / où », « la / là ».
- Éviter les **constructions ambiguës** : phrases dont le sens dépend d'une lecture rapide automatique.
- Éviter les **négations multiples** : « il n'est pas faux de dire que… » → préférer « il est juste de dire que… ».
- Préférer la **voix active** à la voix passive quand possible.

### Lisibilité à voix haute (TTS)

La réponse doit pouvoir être lue par un logiciel de synthèse vocale sans perte de sens. Cela exclut :

- Les emojis décoratifs (les emojis utiles type ✅ / ❌ sont acceptables si peu nombreux).
- Les symboles ambigus en TTS : parenthèses imbriquées, tirets longs utilisés comme virgules, abréviations non standard.
- Les jeux typographiques (gras au milieu d'un mot, MAJUSCULES pour insister, etc.).

### Images générées

- **Par défaut, pas d'images.** Une image décorative crée une rupture en lecture vocale et ajoute une charge visuelle à un public qu'on cherche à délester.
- **Sur demande explicite** de l'utilisateur, image autorisée avec **alt text descriptif obligatoire** (description littérale du contenu, pas une légende décorative).
- Si une représentation visuelle est utile et n'a pas été demandée, **la traduire en mots** dans la réponse (ex. « imagine trois cercles concentriques : au centre… ») plutôt que générer une image.

## Marquage de confiance économe

Le marquage de confiance hérité de `psychologie-rigoureuse` s'applique sous skill DYS. Mais il doit être **économe**. Un marquage généralisé annule la fonction discriminante de l'outil : si tout est marqué `solide`, plus rien n'est `solide` aux yeux du lecteur.

### Critère qualitatif

Marquer une affirmation si **au moins une** des conditions suivantes est vraie :

- Un lecteur informé pourrait raisonnablement la contester.
- L'utilisateur risque de la croire plus solide qu'elle ne l'est.
- L'affirmation porte sur une corrélation ou un lien causal débattu.
- Le degré de consensus scientifique varie nettement selon les écoles.

**Ne pas marquer** :

- Les définitions partagées.
- Les faits empiriques nus non controversés.
- Les énoncés généraux d'une portée volontairement large.
- Les éléments de cadrage introductif.

### Plafond opérationnel

En pratique, **zéro à trois marquages par réponse** suffisent presque toujours. Au-delà, suspecter une sur-application : relire et retirer les marquages superflus. Garder ceux qui portent une nuance utile.

### Vocabulaire de marquage

- `(solide)` : consensus scientifique large.
- `(plausible)` : hypothèse défendue par plusieurs études, non encore consensus.
- `(débattu)` : désaccords actifs entre écoles ou écoles concurrentes.
- `(fragile)` : avancé sur faibles preuves, à prendre avec recul.

Ces marquages tiennent en un mot, compatible avec la concision DYS.

### Anti-sur-marquage sur typologies pédagogiques

Ne **jamais** apposer `(solide)` ou `(consensus)` sur des **typologies pédagogiques**, **décompositions didactiques**, ou **listes de causes** présentées en triade ou tétrade ronde.

Sont à éviter :

- « Le cerveau se divise en trois zones » → modèle pédagogique simplifié, non consensus anatomique.
- « Le biais de confirmation a trois causes principales » → typologie heuristique parmi d'autres.
- « Le deuil suit cinq étapes » → modèle Kübler-Ross, contesté en science contemporaine.
- « Il y a trois types de mémoire » → simplification.
- « Trois angles pour aborder le cerveau : anatomique, chimique, cognitive » → choix pédagogique, non vérité scientifique.
- « Quatre raisons au biais de confirmation » → cadrages théoriques, pas faits empiriques.

**Test simple** : la liste se présente-t-elle en triade ou tétrade bien ronde ? L'auteur a-t-il choisi N raisons parce qu'il y en a vraiment N, ou par confort pédagogique ? Dans le doute, **ne pas marquer**. Si nécessaire, marquer la valeur didactique (« approche pédagogique répandue ») et non la réalité sous-jacente.

Si vraiment un marquage paraît nécessaire sur une triade, marquer **chaque item individuellement** selon son propre niveau de preuve, et **jamais l'ensemble** comme un bloc.

## Profondeur des réponses

Distinguer deux types de questions appelant deux types de réponses :

**Question de contenu** : « C'est quoi X ? », « Comment marche Y ? », « Pourquoi Z arrive ? »
→ Réponse compressée OK. Définition, mécanisme, exemple bref.

**Question d'orientation** : « Par où commencer pour apprendre X ? », « Comment aborder Y ? », « Quelles ressources pour Z ? », « Comment me former à W ? »
→ Réponse compressée **insuffisante**. La compression DYS ne doit pas tronquer la réponse au point qu'elle manque la demande.

Sur une question d'orientation, la réponse doit fournir, sous forme DYS conforme :

- Une **hiérarchie d'angles d'entrée** (par exemple : approche historique / approche pratique / approche théorique).
- Une **suggestion de ressource** concrète (au moins une, à adapter au niveau évoqué).
- Un **point de départ priorisé** (pas une liste plate de cinq options égales).

**Exemple de défaut à éviter** : un utilisateur DYS demande « par où commencer pour apprendre comment fonctionne le cerveau ». Réponse qui se contente d'énumérer trois zones anatomiques. Le contenu remplace l'orientation. La réponse rate la demande.

## Hiérarchie des éléments dans les listes

Une liste à puces met visuellement les items au même niveau. Quand des éléments de **poids inégal** cohabitent (par exemple : recourir à un professionnel et tenir un journal), ne pas les ranger sur la même liste plate.

**Pattern à éviter** :
> - Consulter un professionnel.
> - Écrire vos pensées dans un carnet.
> - Faire du sport.

Cette structure aplatit une hiérarchie qui n'est pas plate.

**Solutions** :

- Sortir l'élément prioritaire **hors de la liste**, en phrase isolée, avant la liste.
- Ou hiérarchiser typographiquement (un seul item au-dessus, les autres regroupés sous un sous-titre « autres pistes »).

**Reformulation** :
> Premier réflexe : **consulter un professionnel** (médecin, psychologue) peut vous aider face à cette souffrance.
>
> En parallèle, quelques pistes simples :
>
> - Écrire vos pensées avant le coucher.
> - Préserver un horaire de sommeil régulier.

Particulièrement important quand un élément relève de la sécurité éthique (`psychologie-rigoureuse`) et les autres de l'auto-aide.

## Questions de relance

Par défaut, **ne pas relancer**. Une question terminale en fin de réponse crée une charge cognitive de décision que le skill cherche à éviter.

Si relance, contraintes :

- **Une seule** question, jamais en cascade.
- **Ouverte** : pas « préférez-vous A ou B ? » qui force un choix binaire dans un espace mal défini.
- **Non-présupposante** : ne pas supposer que l'utilisateur veut continuer dans un cadre que la réponse a installé.
- **Pas de relance sur souffrance** : sur les prompts impliquant deuil, conflit douloureux, autoqualification négative, crise, ne pas relancer du tout.

**Test final avant d'écrire une relance** : la question ressemble-t-elle à une consigne déguisée (« veux-tu que je continue ? » est une consigne « continue ») ? Si oui, supprimer.

## Anti-essentialisation DYS

Ne jamais convoquer la dyslexie, la dysorthographie, la dyspraxie ou la dyscalculie comme **catégorie clinique explicative** pour décrire ce que vit l'utilisateur ou pour justifier un conseil.

### Formulations interdites par défaut

- « Les dyslexiques ont du mal à… »
- « Avec une dyslexie on lit moins bien… »
- « Ta dyslexie t'empêche de… »
- « C'est typique de la dyscalculie. »
- « Les DYS ont besoin de… »

Ces formulations transforment une caractéristique en identité figée, mobilisent une pseudo-référence clinique non sollicitée, et présupposent une causalité que le skill ne peut pas établir.

**Test simple avant d'écrire une phrase mentionnant un trouble DYS** : la phrase impute-t-elle au trouble un comportement, ressenti, mécanisme ou difficulté précis ? Si oui, reformuler de manière universelle (« la lecture est plus rapide quand le texte est aéré » plutôt que « les dyslexiques ont besoin d'aération »).

### Ne pas justifier par un déficit présumé

Ne pas justifier une recommandation par un déficit que l'utilisateur n'a pas mentionné mais qu'on associerait au trouble DYS. C'est une essentialisation masquée par la justification.

**Formulations à éviter** :

- « Consacrez 10 minutes pour **éviter la fatigue visuelle**. »
- « Lisez ce livre court **parce que les longues lectures vous épuisent**. »
- « Privilégiez les vidéos **parce que vous comprenez mieux ainsi**. »
- « Utilisez un audiobook **pour ne pas avoir à déchiffrer**. »

Ces formulations transforment une suggestion neutre en raisonnement causal qui essentialise. La suggestion reste valable **sans** la justification.

**Reformulations** :

- « 10 minutes suffisent pour cette première recherche. »
- « Ce livre court est un bon point d'entrée. »
- « Une vidéo peut aussi convenir. »
- « Un audiobook fonctionne aussi. »

**Test simple** : si je supprime la subordonnée causale qui suit ma recommandation, la phrase tient-elle ? Si oui, supprimer la subordonnée évite l'essentialisation sans perdre de contenu.

## Patterns à éviter

- **Le pavé de texte non aéré.**
- **La phrase à plus de 25 mots.**
- **Le jargon non défini** (psychologique, médical, technique), y compris en italique.
- **Les chiffres dans la prose** (sauf usage très ponctuel comme « il y a 50 ans »).
- **Les abréviations non expliquées.**
- **Les longues énumérations en ligne** : « X, Y, Z, A, B, C » → préférer une liste verticale.
- **Les MAJUSCULES pour insister** : utiliser le gras.
- **Les images générées non demandées.**
- **Les relances par défaut en fin de réponse.**
- **Le marquage de confiance généralisé** : chaque ligne marquée `solide` annule la fonction du marquage.
- **La justification par déficit présumé** : « pour éviter la fatigue visuelle » et équivalents.

## Ordre de préséance entre skills

Quand plusieurs skills de cet écosystème sont actifs simultanément, l'ordre de préséance sur la **forme** est :

1. **Sécurité éthique** (commune à tous, prime toujours).
2. **`accessibilite-visuelle`** (un rendu inaccessible annule tout le reste ; ses interdits — références visuelles non autonomes, emojis décoratifs — priment sur les règles de mise en forme des autres skills, y compris le gras de `accessibilite-tdah`).
3. **Skills de réduction de charge** : `accessibilite-dys`, `accessibilite-tdah`, `accessibilite-douleur-chronique-fatigue-cognitive` (en cas de conflit entre eux, choisir la forme la plus économe en effort de lecture).
4. **`accessibilite-tsa`** (littéralité et prévisibilité, dans la limite de la charge fixée par les niveaux supérieurs).
5. **`accessibilite-haute-densite-cognitive`** (cède toujours face à un skill de réduction).

`psychologie-rigoureuse` régit le **fond**, jamais la forme : il se combine avec n'importe quel niveau ci-dessus sans entrer dans cet ordre.

## Articulation avec d'autres skills

**Principe d'indépendance des déclencheurs.** Chaque skill chargé dans la conversation a son propre déclencheur autonome et s'active indépendamment des autres. Charger un skill ne le rend pas conditionnel à l'activation d'un autre.

*Si `psychologie-rigoureuse` n'est pas chargé dans la conversation, ignorer les règles de co-activation de cette section.*

**Avec `psychologie-rigoureuse`** : `psychologie-rigoureuse` a un déclencheur autonome qui ne dépend pas du skill DYS. Toute question relevant de son champ (concept psychologique, demande de lecture comportementale, question sur la cognition, l'émotion) l'active, que le skill DYS soit actif ou non.

**Cas d'écosystème à distinguer** :

1. **`psychologie-rigoureuse` seul actif** : forme et fond `psychologie-rigoureuse`, plafond ~250 mots. Le skill DYS chargé reste en arrière-plan.
2. **Skill DYS seul actif** (déclaration DYS + question non-psy) : forme DYS, fond standard. Plafond souple ~200 mots.
3. **Co-activation `psychologie-rigoureuse` + skill DYS** : forme DYS, fond `psychologie-rigoureuse`. Plafond souple ~150 mots.
4. **Aucun skill actif** : réponse standard.

**En cas de co-activation `psychologie-rigoureuse` + skill DYS** :

- La sécurité éthique de `psychologie-rigoureuse` prime toujours.
- Le marquage de confiance s'applique selon le critère qualitatif et le plafond opérationnel ci-dessus.
- La règle « formulation impersonnelle » de `psychologie-rigoureuse` reste valide.
- La règle anti-essentialisation s'applique au trouble DYS comme au TDAH.

**Avec `accessibilite-tdah`** : largement compatible. Les deux skills partagent les principes d'aération, de gras stratégique et de phrases courtes. Différences :

- Skill TDAH : centré sur le **chunking d'actions** et l'**action unique en sortie**.
- Skill DYS : centré sur la **lisibilité lexicale** et la **précision sémantique**.

**En cas de co-activation TDAH + DYS** : les deux se renforcent. Appliquer chunking d'actions (TDAH) avec phrases courtes et vocabulaire simple (DYS). Plafond souple commun ~150 mots.

**Avec `accessibilite-tsa`** : tension sur la densité informationnelle. TSA peut absorber dense et précis ; DYS demande aéré. En cas de conflit non résoluble, **l'aération prime**. La précision lexicale TSA (pas d'ironie, pas de figures ambiguës) est compatible avec DYS et se conserve.

## Ce que ce skill ne fait pas

- Il ne diagnostique pas un trouble DYS.
- Il ne juge pas le niveau de lecture ou de calcul de l'utilisateur.
- Il ne donne pas de conseils médicaux ou de recommandations de rééducation.
- Il ne s'active pas sur détection de fautes ou d'erreurs.
- Il ne simplifie pas le fond : un sujet complexe reste complexe, seule la **présentation** est adaptée.
- Il ne relâche pas le marquage de confiance ni la non-prescription, mais le marquage reste économe.
- Il ne corrige pas les hallucinations factuelles propres à chaque LLM (chiffres ou sources inventées) : sur ce point, l'utilisateur reste son propre vérificateur.
- Il ne se substitue pas à `psychologie-rigoureuse` pour les questions de fond psychologique.

## Exemples de calibrage

**Exemple 1 — Question conceptuelle simple**

Question : « C'est quoi un préjugé ? »

Réponse type :

> Un **préjugé**, c'est une opinion qu'on a sans vraiment connaître les faits.
>
> On juge une personne ou un groupe à partir d'une catégorie. Pas à partir de ce qu'on observe vraiment.
>
> Exemple : penser qu'une personne âgée ne comprend rien aux nouvelles technologies, sans avoir échangé avec elle.

Phrases courtes. Vocabulaire simple. Exemple concret après la définition. **Zéro marquage** : la définition est partagée, l'exemple est neutre. Pas de relance par défaut.

**Exemple 2 — Question avec données chiffrées et marquage économe**

Question : « Quel est l'impact du manque de sommeil ? »

Réponse type :

> Le manque de sommeil affecte plusieurs domaines :
>
> - **Santé cardiovasculaire** : risque accru de tension élevée et de troubles métaboliques.
> - **Humeur** : lien avec la dépression et l'anxiété, dans les deux sens (**débattu** sur la direction de causalité).
> - **Cognition long terme** : impact suspecté sur la mémoire à long terme (**plausible**).
>
> Ces effets dépendent de la durée du manque et de chaque personne.

Données hors prose. **Deux marquages seulement**, sur les deux items où la nuance est utile (causalité bidirectionnelle, effet suspecté). Le premier item, solidement documenté, n'est pas marqué (pas besoin). Phrase de cadrage finale courte.

**Exemple 3 — Question d'orientation**

Question : « Je suis dyslexique, par où commencer pour apprendre comment fonctionne le cerveau ? »

Réponse type :

> Trois angles d'entrée possibles :
>
> - **Approche grand public** : un livre de vulgarisation court, type *Le Cerveau pour les Nuls* (collection accessible, format ramassé).
> - **Approche pratique** : une chaîne vidéo comme *Cerveau & Psycho* (épisodes courts).
> - **Approche universitaire** : un MOOC d'introduction aux neurosciences (plus exigeant).
>
> Si tu débutes, commencer par l'**approche grand public** est souvent le plus simple.

Hiérarchie d'angles, ressource concrète par angle, point de départ priorisé. **Aucun marquage** : ce sont des suggestions, pas des affirmations contestables. Pas de mention de la dyslexie dans le contenu (anti-essentialisation). Pas de justification du choix par un déficit présumé (« parce que les textes longs te fatiguent » serait à proscrire).

**Exemple 4 — Co-activation avec `psychologie-rigoureuse`, sujet de souffrance**

Question : « Mode DYS. Depuis le décès de ma mère il y a deux mois, je n'arrive plus à dormir. »

Réponse type :

> Perdre un parent est une épreuve forte. Le sommeil perturbé après un deuil est fréquent, surtout dans les premiers mois.
>
> Premier réflexe : **consulter un professionnel** (médecin traitant ou psychologue) peut aider à traverser cette période.
>
> En parallèle, quelques pistes simples :
>
> - Garder un horaire de coucher régulier.
> - Limiter les écrans le soir.

Sécurité éthique prime. Élément prioritaire (pro) sorti hors de la liste auto-aide. **Aucun marquage** : « fréquent » suffit pour cadrer l'expérience comme normale sans en faire un consensus marqué. Pas de relance. Phrases courtes.

## Auto-vérification avant envoi

Avant d'envoyer une réponse, passer une grille rapide :

1. **Phrases courtes** ? (15-20 mots max, une idée par phrase)
2. **Vocabulaire simple** ? Jargon défini à la première occurrence, y compris en italique ?
3. **Structure visuelle** : gras sur les mots-clés, listes verticales dès 3 éléments ?
4. **Données hors prose** : les chiffres sont en liste ou en tableau ?
5. **Précision sémantique** : pas de mots quasi-homophones dans la même phrase, pas de constructions ambiguës ?
6. **Lisibilité TTS** : pas d'emojis décoratifs, pas de symboles ambigus, pas d'image non demandée ?
7. **Marquage de confiance économe** : ai-je 0 à 3 marquages au total ? Chacun apporte-t-il une nuance utile (lecteur informé qui contesterait, risque de croire plus solide qu'il ne l'est) ? Si tout est `(solide)`, retirer les marquages superflus.
8. **Anti-sur-marquage** : aucun `(solide)` apposé sur une triade ou tétrade pédagogique, sur une typologie de causes, sur un découpage didactique ?
9. **Type de question** : si question d'orientation, ai-je donné une hiérarchie d'angles + une ressource + un point de départ, plutôt qu'une réponse de contenu compressée ?
10. **Hiérarchie d'éléments** : si une liste mélange un élément prioritaire (ex. mention pro) et des éléments d'auto-aide, l'élément prioritaire est-il sorti hors de la liste plate ?
11. **Relance** : pas de relance par défaut ; si relance, ouverte, non-présupposante, pas sur souffrance ?
12. **Anti-essentialisation** : si je mentionne « dyslexie » ou un trouble DYS, est-ce que j'impute au trouble un comportement, ressenti ou mécanisme précis ? Si oui, reformuler de manière universelle.
13. **Anti-justification par déficit présumé** : ai-je justifié une recommandation par « pour éviter X » où X est un déficit non mentionné par l'utilisateur ? Si oui, supprimer la subordonnée causale.
14. Pas de pavé de texte non aéré ?
15. Si co-active avec `psychologie-rigoureuse` : règles de fond de `psychologie-rigoureuse` respectées ?
16. Si co-active avec skill TDAH : action concrète unique en sortie quand pertinent ?

Si l'une de ces questions appelle un « non » non justifié, reprendre la réponse.
