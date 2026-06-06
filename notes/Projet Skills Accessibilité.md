---
tags: [projet, accessibilite, skills, LLM]
date_publication: 2026-05-27
statut: stable
---

# Projet Skills Accessibilité

Écosystème de skills Markdown pour adapter le comportement des LLMs aux besoins cognitifs et neurobiologiques spécifiques.

## Lien GitHub

> https://github.com/brissonjo-sudo/Skills-accessibilite

## Skills stables

| Skill | Version | Fichier | Statut |
|---|---|---|---|
| [[Skill Psychologie Rigoureuse]] | V6 | `skills/psychologie-rigoureuse/` | ✅ Stable |
| [[Skill TDAH]] | V2.1 | `skills/accessibilite-tdah/` | ✅ Stable |
| [[Skill DYS]] | V3 | `skills/accessibilite-dys/` | ✅ Stable |
| [[Skill TSA]] | V4 | `skills/accessibilite-tsa/` | ✅ Stable |
| [[Skill HDC]] | V3 | `skills/accessibilite-haute-densite-cognitive/` | ✅ Stable |
| [[Skill Douleur Chronique Fatigue Cognitive]] | V3 | `skills/accessibilite-douleur-chronique-fatigue-cognitive/` | ✅ Stable |

## Architecture

- **Fond** : [[Skill Psychologie Rigoureuse]] s'applique à toutes les questions psychologiques.
- **Forme** : [[Skill TDAH]], [[Skill DYS]], [[Skill TSA]] s'activent selon le profil de l'utilisateur.
- Les skills de forme sont **indépendants et co-activables**.
- En cas de conflit : Sécurité éthique > Exactitude > Forme.

## Bilan méthodologique

→ [[Bilan Écosystème Skills]]

## Feuille de route

- [x] Skill haute densité cognitive / HPI — V3 stable (harnais promptfoo, 3 providers testés)
- [x] [[Skill Douleur Chronique Fatigue Cognitive]] — V3 stable (Claude 8/8, Mistral 8/8, Gemini 8/8)
- [x] Skill TSA niveau 2 — recadré : couvert par [[Skill TSA]] V4 (registre de lisibilité adaptable, besoin exprimé, pas catégorie clinique)
- [ ] [[Skill Accessibilité Visuelle]]
- [x] Tests multi-LLM systématiques pour chaque nouveau skill — harnais promptfoo rodé et réutilisable

## Date de publication

27 mai 2026
