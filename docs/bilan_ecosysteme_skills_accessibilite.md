# Bilan de synthèse — Écosystème des skills d'accessibilité

Document de référence consolidant trois cycles d'itération (skill 1 « psychologie-rigoureuse », skill TDAH « accessibilite-tdah », skill DYS « accessibilite-dys »). Sert d'ancrage avant l'ouverture du chantier suivant (skill TSA « accessibilite-tsa »).

## 1. Vue d'ensemble du projet

### Objectif

Construire un écosystème de skills modulaires permettant à un LLM de produire des réponses ajustées en fond (rigueur épistémique, sécurité éthique, non-prescription) et en forme (accessibilité cognitive et lexicale).

Chaque skill couvre un périmètre clair :

- **psychologie-rigoureuse** : règles de fond pour toute question relevant de la psychologie, de la cognition, de l'émotion ou de la lecture comportementale.
- **accessibilite-tdah** : adaptation de forme pour profils TDAH (chunking d'actions, action unique en sortie, gestion des digressions).
- **accessibilite-dys** : adaptation de forme pour profils DYS (phrases courtes, vocabulaire simple, données hors prose, structure visuelle).
- **accessibilite-tsa** (à venir) : adaptation pour profils du spectre autistique.

### Architecture

**Principe d'indépendance des déclencheurs.** Chaque skill a son propre déclencheur, autonome. Charger un skill ne le rend pas conditionnel à l'activation d'un autre. Plusieurs skills peuvent se co-activer dans une même conversation.

**Hiérarchie commune** quand plusieurs skills se rencontrent :

1. Sécurité éthique (skill 1) prime sur tout.
2. Règles de fond du skill 1 (marquage de confiance, non-prescription, anti-essentialisation) s'appliquent toujours, parallèlement aux règles de forme.
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
- V2 → V2.1 : défaut d'articulation — Gemini interprétait la co-activation comme un prérequis pour que le skill 1 fonctionne (Cas C). Patch : principe d'indépendance des déclencheurs + 4 cas d'écosystème explicites.

**Acquis stables V2.1** :

- Chunking (2 étapes max, ne présenter que les 2 premières si tâche > 3 étapes).
- Action unique en sortie, observable, courte (< 15 min), sans préalable.
- Plafond ~150 mots (seul), ~150 mots souple (co-activation skill 1).
- Anti-moralisation, anti-digression, anti-récapitulatif.
- Anti-essentialisation TDAH : 7 formulations interdites, test simple avant toute mention du TDAH.
- Articulation skill 1 : 4 cas d'écosystème, principe d'indépendance des déclencheurs.

**Défauts résiduels LLM-spécifiques** :

- ChatGPT : hachage excessif (aération forcée ligne par ligne), digressions pédagogiques, essentialisation TDAH plus marquée qu'en Gemini.
- Gemini : légère tendance à l'essentialisation en co-activation, moins bloquante.

**Tests d'articulation (Cas A/B/C/D) — verdict final** : « l'écosystème fonctionne ». Couple skill 1 V6 + skill TDAH V2.1 production-ready.

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

Sur deux skills (DYS, et probablement aussi sur le skill 1 entre certaines versions), le marquage de confiance oscille entre deux échecs symétriques :

- **Sous-marquage** : le LLM omet de marquer des affirmations inégalement validées, présentant tout comme également solide.
- **Sur-marquage** : le LLM marque chaque ligne `(solide)`, ce qui annule la fonction discriminante de l'outil.

**Solution stable trouvée** : combinaison critère qualitatif + plafond opérationnel + démotion de la règle hors de la hiérarchie de priorités. C'est le levier le plus efficace identifié.

**Risque latent** sur tout nouveau skill qui touche au fond : la règle de marquage est sensible à la formulation. Trop saillante = sur-application ; trop discrète = oubli.

### 3.2 Les relances : un défaut classique

Sur les trois skills, les relances apparaissent comme défaut récurrent sous plusieurs formes :

- **Cascade** : 2-3 questions enchaînées (« Veux-tu que je développe ? Sur quel point ? »). Observé sur skill 1 V4, skill DYS V1 P3, skill DYS V2 (chez Mistral).
- **Présupposante** : suppose que l'utilisateur veut continuer dans un cadre installé par la réponse. Observé sur skill DYS V1 P3, V2 P3, V3 P4 (Gemini).
- **Binaire forcée** : « préférez-vous A ou B ? » qui force un choix dans un espace mal défini.
- **Sur souffrance** : exploration intellectuelle qui désamorce la reconnaissance. Spécifiquement traitée en skill 1 V5.

**Solution stable** : par défaut, pas de relance. Si relance : une seule, ouverte, non-présupposante, jamais sur souffrance. Dispositif d'origine skill 1 V5, repris à l'identique en skill DYS V2.

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

Pattern observé à la fois sur skill 1 (V5→V6) et sur skill DYS (V2→V3, et probablement V3→V4 si on continuait). Chaque correction induit une régression ailleurs : on corrige un défaut central, on crée un défaut symétrique ou mineur.

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

## 6. ~~Recommandations pour skill `accessibilite-tsa` (à venir)~~

**Section archivée.** Le skill `accessibilite-tsa` V2 est en production (335 lignes, testé sur Gemini + Claude.ai). Les recommandations de cette section ont été appliquées lors de la rédaction des V1 et V2.

Pour le prochain skill à concevoir (profil à définir), reprendre la méthodologie de la section 5 et consulter les patterns de la section 3.

### 6.1 Patterns à anticiper

- **Marquage de confiance** : appliquer dès V1 le critère qualitatif + plafond opérationnel. Ne pas le découvrir en V2.
- **Relances** : intégrer dès V1 le dispositif skill 1 V5 (par défaut absente, contraintes si présente, pas sur souffrance).
- **Essentialisation TSA** : prévoir une section anti-essentialisation avec formulations interdites + règle anti-justification présupposante.
- **Hiérarchie de priorités** : laisser à 4 niveaux. Ne pas promouvoir « rigueur épistémique » au niveau 2.
- **Articulation inter-skills** : préciser dès V1 les cas d'écosystème (4 cas pour DYS, à transposer pour TSA).

### 6.2 Tensions anticipées avec DYS

Mentionné dans la V3 du skill DYS : « TSA peut accepter dense et précis ; DYS demande aéré. En cas de conflit non résoluble, l'aération prime. »

À arbitrer en rédaction TSA : le skill TSA doit-il **demander la densité** activement, ou seulement **autoriser la densité** quand DYS n'est pas co-actif ? Recommandation : seulement autoriser, pour éviter une collision frontale.

### 6.3 Tests recommandés dès V1

- 5 prompts de stress sur règles distinctives TSA (à concevoir).
- Tester sur Gemini + Claude.ai dès le premier cycle.
- Si possible un prompt sur sujet factuel dense (équivalent du P2 sommeil) pour mesurer le marquage.
- Un prompt de co-activation TSA + DYS pour vérifier la tension annoncée.

### 6.4 Cible de longueur V1

Viser 250-280 lignes maximum en V1. Le skill DYS V3 à 404 lignes est à la limite haute du gérable. Si on dépasse, consolider avant les tests.

## 7. État de production des skills

| Skill | Version stable | Lignes | Statut | Notes |
|---|---|---|---|---|
| psychologie-rigoureuse | V6 | 228 | production | référence d'écosystème |
| accessibilite-tdah | V2.1 | 216 | production | testée sur Gemini + ChatGPT + 4 cas articulation |
| accessibilite-dys | V3 | 404 | production | testée sur Gemini + Mistral + Claude.ai |
| accessibilite-tsa | V2 | 335 | production | testée sur Gemini + Claude.ai |

**Co-activations validées** :

- skill 1 + DYS : testé en V3 sur P5 deuil. Hiérarchie tient.
- skill 1 + TDAH : intégré dans les cycles TDAH.
- DYS + TDAH : non testé en stress direct, articulation prévue dans les fichiers.

**Co-activations à tester** lors de l'ouverture du TSA :

- TSA + DYS (tension densité vs aération).
- TSA + skill 1.
- TSA + TDAH.
- Triple co-activation skill 1 + TSA + DYS sur un prompt à fond psychologique.

---

*Document à mettre à jour à chaque clôture de cycle. Les sections 2.1, 2.2, 7 méritent un audit de précision par recoupement avec les fichiers sources si les détails comptent pour usage institutionnel.*
