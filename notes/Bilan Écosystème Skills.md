---
tags: [bilan, methodologie, ecosysteme]
date: 2026-05-27
---

# Bilan Écosystème Skills Accessibilité

Document de synthèse consolidant les cycles d'itération de l'écosystème.

## Fichier source complet

`docs/bilan_ecosysteme_skills_accessibilite.md`

## Skills couverts

- [[Skill Psychologie Rigoureuse]] — V1 à V6 (6 cycles)
- [[Skill TDAH]] — V1 à V2.1 (3 cycles)
- [[Skill DYS]] — V1 à V3 (3 cycles)
- [[Skill TSA]] — V1 à V4 (cycles manuels + promptfoo)
- [[Skill HDC]] — V1 à V3 (promptfoo)
- [[Skill Douleur Chronique Fatigue Cognitive]] — V1 à V3 (promptfoo)
- [[Skill Accessibilité Visuelle]] — V1 (promptfoo, stable au 1er cycle)

## Principes méthodologiques clés

1. **Itération V → V+1** sur prompts stressant les règles distinctives
2. **Tests multi-LLM** pour distinguer défauts du skill vs défauts d'un modèle
3. **Harnais promptfoo systématique** — YAML reproductible, baseline vs with_skill, juge Mistral
4. **Pas d'auto-déclaration** — application silencieuse (contrainte absolue depuis TSA V3)
5. **Challenge multi-sous-agents** pour valider les décisions architecturales avant rédaction
6. **Exemple de calibrage négatif** — montrer le pattern interdit, pas seulement le décrire

## Projet parent

→ [[Projet Skills Accessibilité]]
