---
tags: [skill, accessibilite, visuel, basse-vision, lecteur-ecran, forme]
version: V1
statut: en cours d'évaluation
---

# Skill Accessibilité Visuelle — V1

Skill de **forme** : adapte la communication pour les utilisateurs ayant un déficit visuel — **basse vision** (lecture de texte agrandi, contraste, aération) et **cécité / lecteur d'écran** (lecture linéaire cellule par cellule, pas de rendu visuel).

## Principes clés

- **Application silencieuse** (contrainte absolue) : ne jamais accuser réception du profil ni annoncer le mode
- Pas de références visuelles non autonomes (couleurs comme seul vecteur, positions spatiales sans ancrage)
- Pas d'ASCII art ni de diagrammes par caractères (illisibles sur lecteur d'écran)
- Pas d'emojis décoratifs (lus à voix haute par les lecteurs d'écran)
- Tableaux parcimonie et lisibilité linéaire (une ligne d'en-tête, pas de cellules fusionnées, auto-suffisant)
- Structure sémantique des titres (pas de saut de niveau)
- Structure aérée pour basse vision (paragraphes 3-5 lignes, gras/italique économes)
- Alternatives textuelles pour tout contenu normalement visuel
- Anti-essentialisation : les adaptations sont universelles, pas calibrées sur des déficits supposés

## Périmètre

Deux profils couverts :
- **Basse vision** : peut lire du texte agrandi ; bénéficie de l'aération et d'un balisage clair
- **Cécité / lecteur d'écran** : le rendu est entièrement linéaire ; les tableaux, schémas et emojis créent du bruit ou perdent le sens

## Fichier source

`skills/accessibilite-visuelle/skill_accessibilite_visuelle_V1.md`

## Harnais d'évaluation

`eval/promptfooconfig_visuel.yaml` — 8 cas, 2 conditions, 2 LLMs (Mistral Large, Gemini 2.5 Flash).

## Relations

- Part du socle → [[Skill Psychologie Rigoureuse]]
- Co-activable avec → [[Skill DYS]], [[Skill TDAH]], [[Skill TSA]], [[Skill HDC]]
- Projet parent → [[Projet Skills Accessibilité]]

## Statut empirique du run

| Provider | with_skill | Application silencieuse |
|---|---|---|
| Claude (sous-agents, 8 cas) | — | — |
| Mistral Large | — | — |
| Gemini 2.5 Flash | — | — |

## Historique versions

| Version | Changements principaux |
|---|---|
| V1 | Première version. Deux profils : basse vision et cécité/lecteur d'écran. Règles : application silencieuse, pas de références visuelles non autonomes, pas d'ASCII art, pas d'emojis décoratifs, tableaux lisibles linéairement, structure sémantique, alternatives textuelles. |
