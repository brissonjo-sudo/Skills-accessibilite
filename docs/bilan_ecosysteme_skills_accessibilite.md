# Bilan de synthèse — Écosystème des skills d'accessibilité

Document de référence consolidant les cycles d'itération de l'écosystème. Initialement centré sur les trois premiers skills (« psychologie-rigoureuse », « accessibilite-tdah », « accessibilite-dys »), il couvre désormais les sept skills en production. Pour la vue d'ensemble synthétique (versions, déclencheurs, statuts), voir `docs/index_skills.md`.

## 1. Vue d'ensemble du projet

### Objectif

Construire un écosystème de skills modulaires permettant à un LLM de produire des réponses ajustées en fond (rigueur épistémique, sécurité éthique, non-prescription) et en forme (accessibilité cognitive et lexicale).

Chaque skill couvre un périmètre clair :

- **psychologie-rigoureuse** : règles de fond pour toute question relevant de la psychologie, de la cognition, de l'émotion ou de la lecture comportementale.
- **accessibilite-tdah** : adaptation de forme pour profils TDAH (chunking d'actions, action unique en sortie, gestion des digressions).
- **accessibilite-dys** : adaptation de forme pour profils DYS (phrases courtes, vocabulaire simple, données hors prose, structure visuelle).
- **accessibilite-tsa** (V4, production) : adaptation pour profils du spectre autistique à langage fonctionnel.
- **accessibilite-haute-densite-cognitive** (V3, production) : autorisation et structuration de la densité informationnelle pour profils HDC/HPI.
- **accessibilite-douleur-chronique-fatigue-cognitive** (V3, production) : économie cognitive pour douleur chronique et fatigue cognitive.
- **accessibilite-visuelle** (V1, production) : structure pour basse vision et lecteur d'écran.

### Architecture

**Principe d'indépendance des déclencheurs.** Chaque skill a son propre déclencheur, autonome. Charger un skill ne le rend pas conditionnel à l'activation d'un autre. Plusieurs skills peuvent se co-activer dans une même conversation.

**Hiérarchie commune** quand plusieurs skills se rencontrent :

1. Sécurité éthique (psychologie-rigoureuse) prime sur tout.
2. Règles de fond du psychologie-rigoureuse (marquage de confiance, non-prescription, anti-essentialisation) s'appliquent toujours, parallèlement aux règles de forme.
3. Règles de forme des skills d'accessibilité s'appliquent en parallèle (pas en tension) avec le fond.

### Méthodologie

**Itération par cycles V → V+1.** Chaque version est testée sur 5 prompts conçus pour stresser les règles distinctives du skill. Les défauts identifiés alimentent la rédaction de la version suivante.

**Tests multi-LLM.** Critère méthodologique apparu progressivement : tester sur au moins deux LLM de familles différentes pour distinguer les défauts du skill des défauts d'un LLM particulier.

**Prompts répliques exactes entre versions.** Pour mesurer le delta version par version, les prompts ne sont pas reformulés. Comparabilité directe.

**Pas d'auto-déclaration du skill.** Le LLM ne doit pas annoncer « skill activé » en en-tête. Le skill doit s'appliquer silencieusement.

## 2. Trajectoires par skill

### 2.1 psychologie-rigoureuse (V1 → V6)

Skill de fond. 6 versions, version stable V6 (228 lignes).

**Défauts traités au fil des cycles** (synthèse non exhaustive, ordre approximatif) :

- **V1-V2** : sur-prescription, ton thérapeutique non sollicité, absence de marquage de confiance.
- **V2-V3** : essentialisation des comportements (« les personnes anxieuses sont… »), formulations psychiatrisantes spontanées.
- **V3-V4** : sécurité éthique insuffisante sur la souffrance exprimée, plongée dans des techniques d'exploration sans reconnaissance préalable.
- **V4-V5** : relances en cascade, exploration intellectuelle de la souffrance (« qu'est-ce qui te fait penser ça ? », « quand cela a-t-il commencé ? »).
- **V5-V6** : ajustements de calibrage sur le marquage différencié, articulation entre marquage et formulation impersonnelle.

**Acquis stables V6** : marquage de confiance différencié (`solide`/`plausible`/`débattu`), formulation impersonnelle, mention pro sur souffrance, anti-essentialisation, plafond ~250 mots.

**Pattern méthodologique observé** : entre V5 et V6, rendements décroissants nets. Chaque correction induit une régression ailleurs. La V6 a été stabilisée non parce qu'elle est parfaite, mais parce que la prochaine itération aurait probablement osciller.

### 2.2 accessibilite-tdah (V1 → V2.1)

Skill de forme. 3 versions effectives (V1, V2, V2.1 patch). Version stable V2.1 (216 lignes).

**Cycles de test** : Gemini (5 prompts V1) + ChatGPT (5 prompts V1) + tests d'articulation Cas A/B/C/D (V2 + V2.1).

**Défauts traités au fil des cycles** :

- V1 → V2 : essentialisation TDAH en co-activation (« le vrai blocage TDAH vient de... »). Confirmé sur deux LLM (Gemini prompt 5, ChatGPT prompt 1). Section anti-essentialisation ajoutée avec liste explicite des formulations interdites et test simple.
- V2 → V2.1 : défaut d'articulation — Gemini interprétait la co-activation comme un prérequis pour que le psychologie-rigoureuse fonctionne (Cas C). Patch : principe d'indépendance des déclencheurs + 4 cas d'écosystème explicites.

**Acquis stables V2.1** :

- Chunking (2 étapes max, ne présenter que les 2 premières si tâche > 3 étapes).
- Action unique en sortie, observable, courte (< 15 min), sans préalable.
- Plafond ~150 mots (seul), ~150 mots souple (co-activation psychologie-rigoureuse).
- Anti-moralisation, anti-digression, anti-récapitulatif.
- Anti-essentialisation TDAH : 7 formulations interdites, test simple avant toute mention du TDAH.
- Articulation psychologie-rigoureuse : 4 cas d'écosystème, principe d'indépendance des déclencheurs.

**Défauts résiduels LLM-spécifiques** :

- ChatGPT : hachage excessif (aération forcée ligne par ligne), digressions pédagogiques, essentialisation TDAH plus marquée qu'en Gemini.
- Gemini : légère tendance à l'essentialisation en co-activation, moins bloquante.

**Tests d'articulation (Cas A/B/C/D) — verdict final** : « l'écosystème fonctionne ». Couple psychologie-rigoureuse V6 + skill TDAH V2.1 production-ready.

### 2.3 accessibilite-dys (V1 → V3)

Skill de forme. 3 versions, version stable V3 (404 lignes).

**Cycles testés sur Gemini, Mistral et Claude.ai.**

| Version | Lignes | LLM testés | Résultat |
|---|---|---|---|
| V1 | 254 | Gemini (5 prompts) | acquis stables 8/10, défauts identifiés : marquage qui disparaît, sur-marquage sur triades, relances présupposantes, compression excessive sur orientation, images générées non gérées, aplatissement des hiérarchies |
| V2 | 358 | Gemini (5 prompts), Mistral (2 prompts) | 4 correctifs validés (profondeur, relance, images, hiérarchie listes) ; 1 défaut systémique créé (sur-marquage généralisé sur les deux LLM) ; 2 défauts mineurs (jargon italique, micro-essentialisation) |
| V3 | 404 | Claude.ai (3 prompts), Gemini (3 prompts) | sur-marquage corrigé sur les deux LLM (réduction Gemini 11→2), critère qualitatif absorbé, anti-justification présupposante absorbée, profondeur orientation stable, anti-sur-marquage sur triade stable |

**Leçons spécifiques DYS** :

- Le défaut V1 « marquage qui disparaît sur sujet factuel » a été sur-corrigé en V2 par la promotion de « rigueur épistémique » au niveau 2 de la hiérarchie de priorités. La sur-correction a généré le défaut symétrique (sur-marquage).
- La V3 a corrigé par **démotion structurelle** (retour à 4 niveaux comme V1) + **critère qualitatif explicite** + **plafond opérationnel** (0-3 marquages par réponse). Combinaison fonctionnelle.

**Défauts résiduels acceptés en V3** :

- Différenciation du marquage plus fine sur Claude (utilise `plausible` et `débattu`) que sur Gemini (binaire `solide`/absent). LLM-spécifique.
- Relance Gemini à la limite sur P4 (présupposante mais conforme aux contraintes formelles).
- Angles morts : flèches `→` non traitées par règle TTS, vidéos générées non traitées par règle médias.

## 3. Patterns récurrents inter-skills

### 3.1 Le marquage de confiance comme défaut transversal

Sur deux skills (DYS, et probablement aussi sur le psychologie-rigoureuse entre certaines versions), le marquage de confiance oscille entre deux échecs symétriques :

- **Sous-marquage** : le LLM omet de marquer des affirmations inégalement validées, présentant tout comme également solide.
- **Sur-marquage** : le LLM marque chaque ligne `(solide)`, ce qui annule la fonction discriminante de l'outil.

**Solution stable trouvée** : combinaison critère qualitatif + plafond opérationnel + démotion de la règle hors de la hiérarchie de priorités. C'est le levier le plus efficace identifié.

**Risque latent** sur tout nouveau skill qui touche au fond : la règle de marquage est sensible à la formulation. Trop saillante = sur-application ; trop discrète = oubli.

### 3.2 Les relances : un défaut classique

Sur les trois skills, les relances apparaissent comme défaut récurrent sous plusieurs formes :

- **Cascade** : 2-3 questions enchaînées (« Veux-tu que je développe ? Sur quel point ? »). Observé sur psychologie-rigoureuse V4, skill DYS V1 P3, skill DYS V2 (chez Mistral).
- **Présupposante** : suppose que l'utilisateur veut continuer dans un cadre installé par la réponse. Observé sur skill DYS V1 P3, V2 P3, V3 P4 (Gemini).
- **Binaire forcée** : « préférez-vous A ou B ? » qui force un choix dans un espace mal défini.
- **Sur souffrance** : exploration intellectuelle qui désamorce la reconnaissance. Spécifiquement traitée en psychologie-rigoureuse V5.

**Solution stable** : par défaut, pas de relance. Si relance : une seule, ouverte, non-présupposante, jamais sur souffrance. Dispositif d'origine psychologie-rigoureuse V5, repris à l'identique en skill DYS V2.

### 3.3 L'essentialisation par catégorie clinique

Pattern transversal sur tous les skills d'accessibilité. Trois variantes identifiées :

- **Essentialisation directe** : « les dyslexiques ont du mal à… », « les personnes TDAH ont besoin de… ». Traitée explicitement dans chaque skill par une liste de formulations interdites.
- **Justification présupposante** (variante découverte en DYS V2 P4) : « consacrez 10 minutes pour éviter la fatigue visuelle ». La subordonnée causale essentialise tout en gardant une apparence neutre.
- **Pivot de sujet** : l'utilisateur demande X, le LLM répond sur « comment apprendre X quand on a un trouble Y ». Détournement de la question.

**Solution stable** : règles explicites + tests simples d'auto-vérification (« si je supprime la subordonnée causale, la phrase tient-elle ? Si oui, supprimer »).

### 3.4 La hiérarchie de priorités comme outil structurant

Présente dans tous les skills d'accessibilité. Structure générale :

1. Sécurité éthique > 2. Lisibilité > 3. Précision sémantique > 4. Concision.

**Leçon V2 → V3 du skill DYS** : promouvoir une règle au niveau 2 de la hiérarchie augmente sa saillance et provoque une sur-application. Mieux vaut nommer une règle hors de la hiérarchie (par exemple en note) que la promouvoir.

### 3.5 Rendements décroissants des itérations

Pattern observé à la fois sur psychologie-rigoureuse (V5→V6) et sur skill DYS (V2→V3, et probablement V3→V4 si on continuait). Chaque correction induit une régression ailleurs : on corrige un défaut central, on crée un défaut symétrique ou mineur.

**Symptômes** :

- Le compteur de défauts ne tombe jamais à zéro ; il se déplace.
- Les versions deviennent plus longues sans gain de stabilité proportionnel (DYS V1 254 lignes, V2 358, V3 404).
- Les défauts résiduels deviennent LLM-spécifiques ou hors-périmètre raisonnable.

**Critère de stabilisation** : on arrête d'itérer quand les défauts résiduels sont (a) mineurs, (b) LLM-spécifiques, ou (c) hors du périmètre fonctionnel du skill. Pas quand le skill est parfait — il ne l'est jamais.

### 3.6 Défauts du skill vs défauts du LLM

Distinction méthodologique fondamentale apparue en DYS V2 :

- Un défaut observé sur **un seul LLM** peut être LLM-spécifique.
- Un défaut observé sur **deux LLM de familles différentes** est dans le skill.

Tester systématiquement sur deux LLM avant de rédiger une nouvelle version permet d'éviter de modifier le skill pour corriger un comportement propre à un LLM (ce qui alourdit le skill sans bénéfice général).

## 4. Comportements LLM observés

### 4.1 Gemini

- **Forme calme** absorbée correctement (aération, gras, listes).
- **Tropisme aux triades** : structure spontanément ses explications en trois points, qui deviennent des cibles de sur-marquage.
- **Marquage binaire** : utilise `(solide)` ou n'utilise rien ; rarement `plausible` ou `débattu`.
- **Vouvoiement systématique** indépendamment du registre de l'utilisateur.
- **Génère images et vidéos spontanément** sur certains prompts à dominante pédagogique.
- **Pas d'auto-déclaration** du skill.

### 4.2 Mistral

- **Registre orné par défaut** : emojis, tableaux, sections numérotées, doubles séparateurs. Résistant à la consigne de forme calme.
- **Auto-déclaration explicite** des skills activés en en-tête (« Skill activé… »). Signature unique.
- **Tutoiement spontané** indépendamment du registre utilisateur.
- **Hallucinations factuelles** : invente des chiffres précis et des sources nominatives. Confirmé sur deux prompts.
- **Densité massive** : dépasse régulièrement les plafonds des skills.
- **Sur-marquage** comparable à Gemini en V2.

### 4.3 Claude.ai (Opus 4.7)

- **Profil de marquage économe** par défaut, compatible avec le critère qualitatif V3.
- **Marquage différencié** : utilise spontanément `plausible` et `débattue` là où Gemini reste binaire.
- **Ajoute des sources hypertextes** inline quand il fait de la recherche web. Friction TTS mineure.
- **Calibrage fin** des nuances. Sur les questions d'orientation, fournit des réponses plus complètes et structurées que Gemini.
- **Pas d'auto-déclaration** du skill.

### 4.4 ChatGPT

Non testé dans le cycle. À tester si l'occasion se présente. Comportement attendu : profil intermédiaire entre Gemini et Claude.ai.

## 5. Leçons méthodologiques

### 5.1 Indicateurs quantitatifs pour défauts systémiques

Pour les défauts dont l'occurrence est mesurable (marquage, longueur, nombre de questions de relance), un **compteur** vaut mieux qu'un jugement qualitatif. Le critère « 0-3 marquages par réponse » du skill DYS V3 est un exemple : il permet une auto-vérification objective par le LLM, et un diagnostic rapide par le testeur.

### 5.2 Démotion structurelle plutôt qu'ajout de règle

Quand une règle est sur-appliquée, deux solutions sont possibles :

- **Ajout d'une contre-règle** (« mais ne pas trop marquer non plus »). Risque : créer une oscillation entre les deux règles.
- **Démotion structurelle** : retirer la règle de la zone de forte saillance (par exemple : sortir de la hiérarchie de priorités) et la laisser comme règle de fond parmi d'autres. Effet : la règle continue de s'appliquer, mais ne déclenche plus de sur-application.

La V3 du skill DYS a utilisé la démotion structurelle avec succès. Pattern à privilégier sur les futurs skills.

### 5.3 Tests croisés économes

Tester sur 2 LLM × 2 prompts ciblés peut suffire à diagnostiquer un défaut systémique, plutôt que 1 LLM × 5 prompts. Économie de quota et de charge d'analyse.

### 5.4 Tolérance aux comportements LLM-spécifiques

Ne pas chercher à corriger dans le skill des comportements propres à un seul LLM. Exemples :

- Le registre orné de Mistral n'est pas un défaut du skill DYS, c'est un défaut Mistral.
- La génération spontanée d'images par Gemini est traitée par la règle V2 du skill DYS, mais la génération de vidéos pourrait être laissée en angle mort sans gravité.

Ajouter des règles pour chaque LLM-spécificité alourdit le skill sans bénéfice général.

### 5.5 Stabilisation par épuisement, pas par perfection

Une version est stable quand les défauts résiduels sont mineurs, LLM-spécifiques ou hors-périmètre. La poursuite d'une perfection complète mène à l'oscillation. Critère pratique : si la prochaine itération corrige X mais crée probablement Y de même magnitude, stabiliser ici.

## 6. Recommandations pour la conception d'un nouveau skill

**Section archivée — référence historique.** Cette section listait des recommandations pour le skill `accessibilite-tsa`, qui est en production depuis la V4. Les recommandations ont été appliquées dès la V1 ; la trajectoire V3→V4 est documentée en section 2.6. Le texte est conservé comme guide méthodologique réutilisable pour les futurs skills.

Pour tout nouveau skill à concevoir, reprendre la méthodologie de la section 5 et 5bis, et consulter les patterns de la section 3.

---

## 2.4 accessibilite-haute-densite-cognitive (V1 → V3)

Skill de forme. 3 versions, version stable V3. Skill déclenché sur déclaration HPI, HPE, haut potentiel, ou besoin explicite de densité cognitive.

**Contexte** : skill conçu à l'origine avec un déclencheur « HPI » mais rapidement élargi au besoin communicationnel (densité, profondeur, rigueur) indépendamment du label clinique.

**Défauts traités au fil des cycles** :

- V1 → V2 : longueur insuffisante, structures trop plates, absence de profondeur sur les sujets complexes.
- V2 → V3 : **pattern de preamble** découvert sur Gemini — introduction systématique avant d'entrer dans le contenu (ex : « Bien sûr, voici une réponse dense... »). Pattern identifié comme **limitation RLHF structurelle** : la contrainte de politesse de Gemini résiste à l'instruction d'application silencieuse. Solution : règle anti-preamble renforcée, mais résistance documentée comme LLM-spécifique, pas correctable par instruction.

**Acquis stables V3** : densité substantielle autorisée, pas de résumé d'ouverture, pas de conclusion, rigueur épistémique maintenue, co-activation compatible avec psychologie-rigoureuse.

**Pattern méthodologique apporté** : première utilisation du harnais promptfoo avec fichier YAML dédié, 8 cas de test, 2 conditions (with_skill / baseline), 3 providers (Claude, Mistral, Gemini). Modèle reproductible adopté pour tous les skills suivants.

### 2.5 accessibilite-douleur-chronique-fatigue-cognitive (V1 → V3)

Skill de forme. 3 versions, version stable V3. Déclenché sur déclaration de douleur chronique, fatigue cognitive, brain fog, fibromyalgie, SFC/EM, COVID long.

**Distinction avec TDAH** : le skill fatigue ne réduit pas les actions (logique TDAH), mais économise un budget cognitif limité et fluctuant — réponse d'abord, modularité optionnelle (couches additionnelles étiquetées, non imposées), anti-injonction à l'effort.

**Défauts traités** :

- V1 → V2 (Mistral + Gemini 7/8 chacun) : inflation conditionnelle sur questions-définitions simples — les deux providers ajoutaient une couche optionnelle même sur « c'est quoi la mélatonine ? », produisant du texte supplémentaire non demandé. Solution V2 : exception question-définition simple (réponse 1-2 phrases, sans couche optionnelle si la question est atomique).
- V2 → V3 : exception V2 insuffisante pour Mistral (7/8 → encore 1 FAIL sur cas mélatonine SFC). Diagnostic : règle permissive interprétée comme conditionnelle, pas comme absolue. Solution V3 : règle absolue + **exemple de calibrage négatif** (Exemple 1b) montrant explicitement le pattern à éviter. Mistral : 8/8 PASS en V3.

**Acquis stables V3** : réponse d'abord, modularité optionnelle étiquetée, exception question-définition absolue, anti-injonction, anti-minimisation.

**Pattern méthodologique apporté** : l'**exemple de calibrage négatif** (montrer explicitement le pattern interdit, pas seulement le décrire) s'est révélé plus efficace qu'une règle abstraite. Adopté comme outil standard.

### 2.6 accessibilite-tsa (V3 → V4)

Prolongement de la trajectoire V1→V2 documentée en section 2 (archivé). Cette section couvre le chantier V3→V4 ouvert en juin 2026.

**Chantier V3** : fiabilisation de la version niveau 1. Correctifs : application silencieuse érigée en **contrainte absolue** (en-tête de section, formulations interdites explicites), définition clinique DSM-5 corrigée (niveau ≠ DI), proportionnalité (pas de plan annoncé sur question simple), règle anti-dérobade (réponse franche d'abord). Harnais 8 cas. Claude 8/8, Mistral 8/8, Gemini 8/8. V3 stable.

**Chantier V4 — question architecturale** : la roadmap prévoyait un skill TSA niveau 2 séparé (DSM-5 niveau de soutien 2). Avant rédaction, analyse à 4 sous-agents indépendants (lentilles : clinique, architecture, anti-validisme, testabilité). Convergence : **pas de skill niveau 2 séparé**. Raisons :
1. Le niveau DSM-5 n'est pas un paramètre communicationnel — même profil clinique, besoin de langage différent selon le sujet.
2. Duplication 70% attendue avec V3.
3. Simplification par défaut = essentialisation de forme (imposer un langage simplifié sur déclaration clinique, sans besoin exprimé).
4. Non falsifiable (pas de critère de test qui ne soit pas circulaire).

**Solution V4 : registre de lisibilité adaptable.** Menu de format neutre déclenché par besoin exprimé (« j'ai du mal avec les longues réponses »), pas par déclaration clinique. La déclaration « je suis autiste niveau 2 » → entrée directe dans le contenu (pas de menu). La déclaration + besoin de format → menu proposé une fois, avec sortie non obligatoire. Harnais étendu à 11 cas (3 nouveaux : déclaration clinique seule, difficulté de format exprimée, adaptation appliquée). Claude 11/11, Mistral 11/11, Gemini 10/11 (Cas 3 anti-dérobade : limitation RLHF structurelle, non correctable par instruction). V4 stable.

**Pattern méthodologique apporté** : le **challenge multi-sous-agents** (4 agents indépendants avec lentilles différentes) comme outil de validation architecturale avant rédaction. A permis d'éviter un skill entier avec défauts structurels.

### 2.7 accessibilite-visuelle (V1)

Skill de forme. V1 stable au premier cycle. Deux profils couverts : basse vision (aération, structure sémantique des titres, gras économes) et cécité/lecteur d'écran (lisibilité entièrement linéaire).

**Règles distinctives** :
- Pas de références visuelles non autonomes (couleurs comme seul vecteur d'information, positions spatiales sans ancrage textuel).
- Pas d'ASCII art ni de diagrammes par caractères (illisibles sur lecteur d'écran).
- Pas d'emojis décoratifs (lus à voix haute : « fusée », « étoile verte »).
- Tableaux : une ligne d'en-tête, cellules auto-suffisantes, pas de cellules fusionnées. Si non respecté : convertir en liste de paires clé : valeur.
- Structure sémantique des titres : pas de saut de niveau (# directement suivi de ###).
- Alternatives textuelles pour tout contenu normalement visuel.

**Résultats** : Claude 8/8, Mistral 8/8, Gemini 5/5 évalués PASS (3 erreurs 503 infrastructure). Démarque baseline Mistral (C1) : sans skill, Mistral ajoute une section « boucles et accessibilité : si tu utilises un lecteur d'écran… » — annonce du mode corrigée silencieusement par le skill.

**Pattern méthodologique** : premier skill stable au premier cycle (V1), sans itération nécessaire. Hypothèse : les règles les plus spécifiques (pas d'ASCII art, pas d'emojis) sont suffisamment contra-intuitives pour être absentes du comportement par défaut, et suffisamment précises pour être correctement appliquées dès la première instruction.

---

## 3.7 Harnais promptfoo systématique (nouveau pattern)

**Avant** (cycles TDAH, DYS, TSA V1-V2) : tests manuels sur interface Claude.ai ou ChatGPT, 5 prompts par LLM, résultats saisis à la main.

**Après** (HDC, Fatigue, TSA V3-V4, Visuelle) : harnais YAML reproductible — `promptfooconfig_<skill>.yaml` par skill, `prompts/with_skill.yaml` + `prompts/baseline.yaml`, 2 conditions systématiques, 2+ providers, juge Mistral Large (`llm-rubric`), résultats en JSON exploitable.

**Avantages** :
- Reproductibilité : le même run peut être relancé à n'importe quel moment.
- Baseline systématique : comparaison with_skill / sans skill à chaque run, permettant de mesurer l'apport réel du skill.
- Isolation des variables : source unique du skill dans `skills/`, aucune copie dans `eval/`.
- Audit de régression : pour chaque version, on détecte si un correctif crée un nouveau défaut sur un cas précédemment PASS.

**Coût** : deux providers payants (Mistral, Gemini ou OpenAI), plus juge. Géré par clés dans `.env` non committé.

**Limite identifiée** : les erreurs 503 (surcharge API Gemini) produisent des résultats `null` indiscernables a priori des échecs de skill — distinguer par le champ `failureReason` (2 = erreur API, 1 = assertion fail).

### 3.8 Application silencieuse — contrainte absolue (nouveau pattern)

Pattern transversal apparu progressivement, érigé en contrainte absolue à partir de TSA V3.

**Définition** : le skill s'applique sans jamais nommer son mode d'activation, sans accuser réception du profil déclaré, et sans annoncer les adaptations produites.

**Formulations interdites (génériques)** :
- « Puisque tu es [profil], je vais… »
- « Mode [profil] activé. »
- « Pour m'adapter à [profil]… »
- « Je vais éviter [X] pour toi. »

**Avant** : les skills contenaient des règles implicites sur la discrétion, mais aucune formulation interdite explicite.

**Après** : chaque skill contient une section « Contrainte absolue — application silencieuse » en tête, avec une liste de formulations interdites. L'auto-vérification inclut un point explicite sur cette contrainte.

**Résultat empirique** : les trois LLMs passent systématiquement cette contrainte sur les skills récents (TSA V3-V4, Fatigue V3, Visuelle V1). Deux manifestations documentées de résistance RLHF :
- **HDC V3** : Mistral 1/8 (preamble « En mode HDC… ») et Gemini 4/8 (preamble « Bien sûr, voici une réponse dense… ») — limitation structurelle, non corrigeable par instruction.
- **TSA V4 C3** : Gemini (preamble résiduel sur question de communication autistique).

Ces résistances sont LLM-spécifiques, documentées, et ne constituent pas des défauts du skill.

### 3.9 Essentialisation de forme vs essentialisation de fond (nouveau pattern)

Distinction affinée en TSA V4 (challenge 4 sous-agents).

**Essentialisation de fond** (connue depuis V1) : « les personnes autistes ont tendance à… », « avec ton TDAH tu as besoin de… ». Traitée dans tous les skills par anti-essentialisation.

**Essentialisation de forme** (identifiée en V4) : adapter la présentation par défaut sur la base d'une déclaration clinique, sans besoin exprimé. Exemple : proposer des réponses simplifiées à quelqu'un qui a dit « je suis autiste niveau 2 » sans mentionner de difficulté de format. La simplification non demandée est une forme d'essentialisation — elle présuppose un déficit de traitement sans que l'utilisateur l'ait signalé.

**Solution** : le déclencheur du registre de lisibilité est le besoin exprimé, pas la déclaration clinique. Applicable à tout skill de forme.

---

## 5bis. Évolution méthodologique (juin 2026)

Trois évolutions majeures par rapport aux pratiques décrites en section 5 :

### 5bis.1 Harnais promptfoo *(abandonné)*

Voir section 3.7. A remplacé les tests manuels à partir du skill HDC, puis a été abandonné en août 2026 au profit de la validation en vagues (`eval/prompt_benchmark_claude_code.md`). Les `promptfooconfig_*.yaml` subsistent comme banque de cas.

### 5bis.2 Challenge multi-sous-agents

Avant de rédiger une version majeure ou un nouveau skill, soumettre la question architecturale à plusieurs agents indépendants avec des lentilles différentes (clinique, architecture, anti-validisme, testabilité). Convergence forte → décision. Divergence → identifier le vrai désaccord avant de trancher.

Appliqué en TSA V4 : 4 agents, convergence 4/4 sur « pas de skill niveau 2 séparé ».

### 5bis.3 Analyse par sous-agents isolés (auto-évaluation)

Pour le run Claude (contexte frais par cas), utiliser un sous-agent par cas de test. L'agent joue le LLM testé ET évalue sa propre réponse selon la rubrique. Avantage : contexte frais garanti, pas de contamination entre cas. Limite : l'agent évalue sa propre réponse — biais de complaisance possible, contrebalancé par le juge externe Mistral Large sur le run promptfoo.

---

## 7. État de production des skills (mis à jour juin 2026)

| Skill | Version stable | Statut | Méthode de test | Résultats |
|---|---|---|---|---|
| psychologie-rigoureuse | V6.2 | candidat | Gemini + ChatGPT + Claude.ai (manuel) ; promptfoo 8 cas | référence d'écosystème |
| accessibilite-tdah | V2.3 | candidat | Gemini + ChatGPT + 4 cas articulation (manuel) ; promptfoo 10 cas (C9 TDA / C10 non-déclenchement) | référence forme |
| accessibilite-dys | V3.1 | production | Gemini + Mistral + Claude.ai (manuel) ; promptfoo 8 cas | 3 cycles |
| accessibilite-tsa | V4.1 | production | promptfoo 11 cas — Claude 11/11, Mistral 11/11, Gemini 10/11 | V4 stable ; Gemini C3 RLHF documenté |
| accessibilite-haute-densite-cognitive | V3.2 | candidat | promptfoo 8 cas — Claude 8/8, Mistral 7/8, Gemini 4/8 applic. silencieuse | Gemini + Mistral preamble RLHF documenté |
| accessibilite-douleur-chronique-fatigue-cognitive | V3.2 | candidat | promptfoo 8 cas — Claude 8/8, Mistral 8/8, Gemini 8/8 | 3 cycles |
| accessibilite-visuelle | V1.2 | candidat | promptfoo 8 cas — Claude 8/8, Mistral 8/8, Gemini 5/5 évalués | stable au 1er cycle |

> **Les chiffres de la colonne « Méthode de test » sont historiques.** Ils proviennent de l'outillage promptfoo, abandonné depuis : la validation se fait désormais en vagues (voir `CONTRIBUTING.md` §5 et `eval/prompt_benchmark_claude_code.md`). Ils avaient de plus été mesurés sur la version mineure antérieure, avant l'insertion du bloc canonique « Ordre de préséance ».
>
> Les skills marqués **candidat** ont été modifiés après le benchmark contrôlé du 2026-08-05 et attendent une vague de validation indépendante. Vue synthétique et statuts faisant foi : `docs/index_skills.md`.

**Règle méta de co-activation — plafonds** : en co-activation, le plafond de mots le plus bas parmi les skills actifs prime. Exemples : DYS seul ~200 mots ; DYS + psychologie-rigoureuse ~150 mots ; DYS + TSA + psychologie-rigoureuse ~150 mots. HDC (pas de plafond fixe) adopte celui du skill le plus contraignant co-actif : HDC + DYS → ~150 mots.

**Co-activations validées dans les fichiers de skill** (non toutes testées en stress direct) :
- psychologie-rigoureuse + DYS / TDAH / TSA / HDC / Fatigue / Visuelle : prévues dans chaque skill.
- psychologie-rigoureuse + DYS : testé en stress (P5 deuil). Hiérarchie tient.
- psychologie-rigoureuse + TDAH : intégré dans les cycles TDAH.
- TSA + DYS : tension densité/aération documentée, aération prime.
- TSA + Visuelle : compatibilité forte, règles de forme orthogonales. Documenté dans TSA V4 et Visuelle V1.
- Visuelle + HDC : lisibilité linéaire prime sur densité en co-activation.

**Co-activations non encore testées en stress direct** :
- TSA + TDAH, TSA + Fatigue, DYS + Fatigue.
- Triple co-activation psychologie-rigoureuse + TSA + DYS sur prompt à fond psychologique.
- Visuelle + TSA (application silencieuse × 2, compatibles en principe).

---

*Document mis à jour au 7 juin 2026. Les sections 2.1–2.3 couvrent les cycles manuels (mai 2026). Les sections 2.4–2.7 et 3.7–3.9 couvrent les cycles promptfoo (juin 2026). Section 7 reflète l'état de production courant.*
