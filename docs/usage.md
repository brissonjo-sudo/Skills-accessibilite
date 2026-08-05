# Cas d'usage

Exemples concrets d'utilisation des skills, par profil et par contexte. Pour les déclencheurs précis et les compatibilités, voir [`index_skills.md`](index_skills.md). Pour les limites, voir [`note_ethique.md`](note_ethique.md).

> Rappel : un skill d'accessibilité s'active sur **déclaration explicite** ou besoin formulé directement. Il adapte la **forme**, jamais l'exactitude du contenu.

---

## Par skill

### accessibilite-dys — assistant pour personne dyslexique
Réponses plus lisibles : phrases courtes, vocabulaire simple, données chiffrées isolées hors du texte, structure visuelle forte. Utile pour lire un courrier, comprendre une démarche, suivre une explication sans se perdre dans des paragraphes denses.

### accessibilite-tdah — aide à démarrer une tâche
Réponses découpées, une action unique en sortie, pas de plan massif ni de surcharge. Utile pour passer à l'action quand l'attention est fragmentée, sans se faire submerger par une liste de vingt étapes.

### accessibilite-douleur-chronique-fatigue-cognitive — économie d'effort
Réponse directe en premier, modularité optionnelle, aucune injonction à agir. Pensé pour fibromyalgie, COVID long, SFC/EM, brouillard mental : minimiser le coût de lecture lors d'une crise de fatigue.

### accessibilite-tsa — communication littérale et prévisible
Réponses franches, sans sous-entendus ni small talk, structure prévisible, idiomes explicités. Pour des profils de niveau 1 (incl. « Asperger ») qui préfèrent la clarté directe à l'implicite.

### accessibilite-haute-densite-cognitive — densité assumée
Réponses denses, nuancées, multi-couches, sans vulgarisation forcée. Pour profils HDC/HPI ou toute demande explicite de complexité préservée (« ne simplifie pas »).

### accessibilite-visuelle — compatibilité lecteur d'écran
Suppression des références visuelles non autonomes (couleurs, positions, schémas ASCII), pas d'emoji décoratif, contenu intégralement lisible en lecture linéaire. Pour basse vision et cécité.

### psychologie-rigoureuse — sujets psychologiques sensibles
Évite la pop-psychologie, le diagnostic sauvage et l'interprétation abusive d'un tiers absent. Marque le degré de confiance, ne prescrit pas, oriente vers un professionnel en cas de souffrance.

---

## Par contexte

- **Support client accessible** : adapter le style à un besoin explicite (lisibilité, brièveté, littéralité) sans inférer de trouble.
- **Rédaction de contenus publics** : FAQ, notices, explications administratives, onboarding — appliquer les principes de forme pour un public large.
- **Formation interne d'équipes IA** : illustrer comment écrire des instructions robustes, testées, avec déclencheurs stricts et anti-patterns documentés (voir `eval/` et le bilan).
- **Co-pilotage médical non clinique** : reformuler une information, préparer des questions, clarifier un parcours de soin — **sans** conseil médical ni diagnostic (voir `note_ethique.md`).

---

## Co-activation

Plusieurs skills peuvent s'activer ensemble ; chacun garde son déclencheur autonome. Quelques combinaisons typiques (matrice complète dans [`index_skills.md`](index_skills.md)) :

- **DYS + TSA** : tension densité/aération → l'aération prime.
- **TDAH + fatigue cognitive** : le plafond de mots le plus bas prime.
- **HDC + DYS/TDAH** : la réduction de charge prime sur la densité.
- **psychologie-rigoureuse + fatigue cognitive en contexte de détresse** : la sécurité éthique prime sur la forme.
