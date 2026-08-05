# Index canonique des skills

Page de référence unique : pour chaque skill, sa version stable, son fichier source, son déclencheur, les risques qu'il couvre, ses compatibilités et son statut d'évaluation.

> Source de vérité du **comportement** : le fichier `SKILL.md` de chaque skill.
> Source de vérité de l'**historique d'itération** : `docs/bilan_ecosysteme_skills_accessibilite.md`.
> En cas de divergence, le `SKILL.md` prime sur cet index.

Dernière mise à jour : 2026-06-21 (écosystème v1.18.0).

---

## Tableau de synthèse

| Skill | Version | Fichier source | Statut | Banc d'éval |
|---|---|---|---|---|
| psychologie-rigoureuse | V6.1 | `skills/psychologie-rigoureuse/SKILL.md` | production | `eval/promptfooconfig_psychologie.yaml` (8 cas) |
| accessibilite-tdah | V2.2 | `skills/accessibilite-tdah/SKILL.md` | production | `eval/promptfooconfig_tdah.yaml` (10 cas) |
| accessibilite-dys | V3.1 | `skills/accessibilite-dys/SKILL.md` | production | `eval/promptfooconfig_dys.yaml` (8 cas) |
| accessibilite-tsa | V4.1 | `skills/accessibilite-tsa/SKILL.md` | production | `eval/promptfooconfig_tsa.yaml` (11 cas) |
| accessibilite-haute-densite-cognitive | V3.1 | `skills/accessibilite-haute-densite-cognitive/SKILL.md` | production | `eval/promptfooconfig.yaml` (8 cas) |
| accessibilite-douleur-chronique-fatigue-cognitive | V3.1 | `skills/accessibilite-douleur-chronique-fatigue-cognitive/SKILL.md` | production | `eval/promptfooconfig_fatigue.yaml` (8 cas) |
| accessibilite-visuelle | V1.1 | `skills/accessibilite-visuelle/SKILL.md` | production | `eval/promptfooconfig_visuel.yaml` (8 cas) |

---

## Fiches par skill

### psychologie-rigoureuse — V6.1

- **Périmètre** : fond. Cadre d'analyse psychologique rigoureux et non dogmatique.
- **Déclencheur** : toute question touchant un concept psy (biais, attachement, motivation, personnalité, trouble, mécanisme de défense…), citation d'un auteur du champ, demande de lecture comportementale/émotionnelle, question sur les relations, le développement, la cognition, l'émotion ou la santé mentale. Se déclenche même si la demande n'est pas formulée comme « psychologique ».
- **Risques couverts** : pop-psychologie, diagnostic sauvage, interprétation abusive d'un tiers absent, prescription non sollicitée, sur-confiance non marquée.
- **Quand NE PAS l'utiliser** : il ne se substitue pas à un professionnel ; il ne pose pas de diagnostic. Voir `docs/note_ethique.md`.
- **Compatibilités** : régit le **fond** ; se combine avec tous les skills de forme sans tension.

### accessibilite-tdah — V2.2

- **Périmètre** : forme.
- **Déclencheur** : déclaration explicite uniquement (« j'ai un TDAH », « j'ai un TDA », « trouble de l'attention », « mode TDAH », « réponds-moi de manière TDAH-friendly », « je suis facilement débordé », « j'ai du mal à suivre les longues réponses »).
- **Ne se déclenche PAS sur** : mention de procrastination, surcharge, oubli, difficulté à finir — ces signaux ne suffisent pas à présumer un profil.
- **Effet** : chunking, aération, action unique en sortie, gestion des digressions. Ne touche pas au fond.
- **Compatibilités** : `psychologie-rigoureuse` (fond), DYS, TSA, Fatigue, Visuelle.

### accessibilite-dys — V3.1

- **Périmètre** : forme.
- **Déclencheur** : déclaration explicite uniquement (« je suis dyslexique », « j'ai une dyspraxie », « mode DYS », « j'ai du mal à lire les textes longs »).
- **Ne se déclenche PAS sur** : fautes d'orthographe ou signaux indirects.
- **Effet** : phrases courtes, vocabulaire simple, données hors prose, structure visuelle forte. Ne touche pas au fond.
- **Compatibilités** : `psychologie-rigoureuse`, TDAH, TSA (tension densité/aération : aération prime), Visuelle.

### accessibilite-tsa — V4.1

- **Périmètre** : forme. Profils autistes à langage fonctionnel (« niveau 1 », incl. diagnostic historique « Asperger »).
- **Déclencheur** : déclaration explicite uniquement (« je suis autiste », « j'ai un TSA », « je suis Asperger », « je suis sur le spectre », « mode TSA »).
- **Ne se déclenche PAS sur** : signes indirects (goût des routines, franc-parler, intérêt intense…).
- **Effet** : précision lexicale, structure prévisible, pas de small talk, littéralité. Application **silencieuse**. Menu de format neutre proposé une fois si l'utilisateur exprime une difficulté de format.
- **Compatibilités** : `psychologie-rigoureuse`, DYS, TDAH, Visuelle.

### accessibilite-haute-densite-cognitive — V3.1

- **Périmètre** : forme. Profils HDC/HPI/« zèbre ».
- **Déclencheur** : déclaration explicite (« j'ai un HPI », « je suis zèbre », « mode HDC », « je pense de façon associative ») OU besoin explicite de densité (« ne simplifie pas », « garde toute la nuance »).
- **Ne se déclenche PAS sur** : la seule complexité de la question posée.
- **Effet** : autorise et structure la profondeur, la nuance, l'exploration multi-couches. Ne touche pas au fond.
- **Compatibilités** : `psychologie-rigoureuse` et les autres skills. **En co-activation avec un skill de réduction (DYS, TDAH), la réduction prime sur la forme.**

### accessibilite-douleur-chronique-fatigue-cognitive — V3.1

- **Périmètre** : forme. Douleur chronique, fatigue cognitive, brouillard mental (fibromyalgie, SFC/EM, COVID long).
- **Déclencheur** : déclaration explicite (« fibromyalgie », « SFC/EM », « COVID long », « brouillard mental », « mode économie d'énergie ») OU besoin direct d'économie d'effort (« je n'ai pas l'énergie de lire long », « je suis en crise de fatigue »).
- **Ne se déclenche PAS sur** : une fatigue ordinaire (« j'ai mal dormi »).
- **Effet** : réponse d'abord, modularité optionnelle, anti-injonction à l'effort. Ne touche pas au fond.
- **Compatibilités** : `psychologie-rigoureuse` ; les autres skills d'accessibilité.

### accessibilite-visuelle — V1.1

- **Périmètre** : forme. Basse vision, cécité avec lecteur d'écran.
- **Déclencheur** : déclaration explicite (« je suis malvoyant », « je suis non-voyant », « j'utilise un lecteur d'écran »).
- **Effet** : supprime les références visuelles non autonomes (couleurs, positions, schémas ASCII), évite les emojis décoratifs, structure pour la lecture linéaire. Application **silencieuse**.
- **Compatibilités** : `psychologie-rigoureuse`, DYS, TDAH, TSA.

---

## Ordre de préséance (rappel)

Quand plusieurs skills se co-activent, l'ordre canonique sur la **forme** est :

1. **Sécurité éthique** (`psychologie-rigoureuse`) — prime sur tout.
2. `accessibilite-visuelle`
3. Skills de réduction de charge (`accessibilite-dys`, `accessibilite-tdah`, `accessibilite-douleur-chronique-fatigue-cognitive`)
4. `accessibilite-tsa`
5. `accessibilite-haute-densite-cognitive`

Le **fond** est régi par `psychologie-rigoureuse`, hors de cet ordre. Le bloc canonique « Ordre de préséance entre skills » est inséré à l'identique dans les 7 `SKILL.md`.

En co-activation, le **plafond de mots le plus bas** parmi les skills actifs prime.

---

## Matrice de co-activation

Trois niveaux de statut, alignés sur le bilan (§7) : **testée en stress** (cas adverse joué), **documentée** (compatibilité établie dans les fichiers de skill, sans test de stress dédié), **spécifiée** (règle prévue mais non encore testée en stress direct).

| Combinaison | Statut | Note |
|---|---|---|
| `psychologie-rigoureuse` + DYS | testée en stress | stress P5 (deuil) ; la hiérarchie fond/forme tient |
| `psychologie-rigoureuse` + TDAH | testée en stress | intégrée aux cycles de test TDAH |
| TSA + DYS | documentée | tension densité/aération : aération prime |
| TSA + Visuelle | documentée | compatibilité forte, règles orthogonales (TSA V4 + Visuelle V1) ; non testée en stress direct |
| Visuelle + HDC | documentée | lisibilité linéaire prime sur densité |
| HDC + DYS / TDAH | spécifiée | la réduction de charge prime sur la densité |
| TDAH + Fatigue | spécifiée | plafond de mots le plus bas prime |
| HDC + Fatigue | spécifiée | HDC adopte le plafond du skill le plus contraignant |
| TSA + TDAH, TSA + Fatigue, DYS + Fatigue | spécifiée | non encore testées en stress direct |
| `psychologie-rigoureuse` + TSA + DYS (fond psy) | spécifiée | triple co-activation, non encore testée en stress direct |
