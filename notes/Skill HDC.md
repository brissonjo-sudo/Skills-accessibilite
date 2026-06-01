---
tags: [skill, accessibilite, hdc, hpi, forme]
version: V2
statut: en évaluation
---

# Skill Accessibilité Haute Densité Cognitive — V2

Skill de **forme** : autorise et structure la profondeur informationnelle pour les utilisateurs à haute densité cognitive (HDC/HPI/zèbre).

## Principe clé

Inverse fonctionnel des skills DYS/TDAH/TSA : là où ceux-ci réduisent la charge, ce skill refuse de réduire la complexité réelle.

## Déclencheur dual

- Déclaration explicite : « j'ai un HPI », « je suis zèbre », « mode HDC »
- Besoin communicationnel exprimé : « ne simplifie pas », « garde toute la nuance », « mes questions sont multi-niveaux »

## Principes clés

- Anti-édulcoration — pas de vulgarisation non sollicitée
- Questions multi-couches traitées distinctement, pas aplaties
- Structure navigable (titres, gras, listes) même pour les réponses denses
- Tolérance à l'ambiguïté — pas de résolution forcée
- Plafond souple — proportionnel à la complexité réelle du sujet
- Anti-essentialisation HDC/HPI (mêmes règles que pour les autres profils)

## Fichier source

`skills/accessibilite-haute-densite-cognitive/skill_accessibilite_haute_densite_cognitive_V2.md`

## Harnais d'évaluation

`eval/promptfooconfig.yaml` — 8 cas de test, 2 conditions (avec/sans skill), 2 LLMs (Mistral Large, Gemini 2.5 Flash)

## Relations

- Part du socle → [[Skill Psychologie Rigoureuse]]
- Co-activable avec → [[Skill DYS]], [[Skill TDAH]], [[Skill TSA]]
- Projet parent → [[Projet Skills Accessibilité]]

## Note sur le statut empirique du HPI

Le HPI est une catégorie **débattue** empiriquement. Le skill ne le valide pas comme consensus clinique. Toute question sur le HPI mobilise le skill 1 avec marquage approprié.

## Historique versions

| Version | Changements principaux |
|---|---|
| V1 | Première version — déclencheur dual (déclaration + besoin communicationnel), anti-édulcoration, structure navigable |
| V2 | Correctif application silencieuse (anti-preamble) + renforcement proportionnalité sur sujets simples |
