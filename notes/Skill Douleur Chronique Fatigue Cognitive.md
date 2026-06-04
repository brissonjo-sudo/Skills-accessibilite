---
tags: [skill, accessibilite, douleur-chronique, fatigue-cognitive, brain-fog, forme]
version: V3
statut: en évaluation (run V3 à lancer)
---

# Skill Accessibilité Douleur Chronique / Fatigue Cognitive — V3

Skill de **forme** : économise le budget cognitif (lecture et traitement) des utilisateurs dont la capacité d'attention, de concentration et de mémoire de travail est réduite et **fluctuante**.

## Principe clé

Skill de réduction de charge, comme [[Skill TDAH]] et [[Skill DYS]], mais avec un angle distinct : **l'économie d'un budget cognitif limité**. Différence centrale avec TDAH : il **ne pousse pas à l'action** — la personne peut être dans l'incapacité d'agir, voire de finir de lire.

## Public visé

Douleur chronique, fatigue cognitive, brouillard mental (brain fog), fibromyalgie, syndrome de fatigue chronique (SFC/EM), COVID long, épuisement cognitif situationnel déclaré.

## Déclencheur dual

- Déclaration explicite : « j'ai une fibromyalgie », « COVID long », « brouillard mental », « mode économie d'énergie »
- Besoin communicationnel : « je n'ai pas l'énergie de lire long », « fais court mais complet », « je suis en crise de fatigue »

## Principes clés

- **Réponse d'abord** — l'essentiel en 1 à 3 phrases, avant tout développement
- **Modularité optionnelle** — couches que l'utilisateur peut choisir de ne pas lire (« Si tu as l'énergie »)
- **Anti-injonction à l'effort** — proposer, jamais enjoindre ; légitimité de ne rien faire
- **Anti-minimisation / anti-positivité toxique** — pas de « tout le monde est fatigué », « ça va aller », « as-tu essayé le yoga »
- **Auto-suffisance** — ne pas exiger de tenir plusieurs éléments en mémoire de travail
- **Anti-essentialisation** — mêmes règles que les autres skills
- **Sécurité éthique prioritaire** — comorbidité forte avec dépression et idées suicidaires

## Fichier source

`skills/accessibilite-douleur-chronique-fatigue-cognitive/skill_accessibilite_douleur_chronique_fatigue_cognitive_V3.md`

## Harnais d'évaluation

`eval/promptfooconfig_fatigue.yaml` — 8 cas de test, 2 conditions (avec/sans skill), 2 LLMs (Mistral Large, Gemini 2.5 Flash). Config séparée du banc HDC.

## Relations

- Part du socle → [[Skill Psychologie Rigoureuse]]
- Co-activable avec → [[Skill DYS]], [[Skill TDAH]], [[Skill TSA]]
- Tension avec → [[Skill HDC]] (le skill de réduction prime)
- Projet parent → [[Projet Skills Accessibilité]]

## Statut empirique du run

| Provider | with_skill | Application silencieuse |
|---|---|---|
| Claude (sonnet-4-6, 16 sous-agents) | 8/8 PASS | 8/8 |
| Mistral Large | _run 2-LLM à lancer_ | — |
| Gemini 2.5 Flash | _run 2-LLM à lancer_ | — |

## Historique versions

| Version | Changements principaux |
|---|---|
| V1 | Première version — déclencheur dual, réponse d'abord, modularité optionnelle, anti-injonction, anti-positivité toxique, sécurité éthique prioritaire. Run Claude 8/8. Run 2-LLM : Mistral 7/8, Gemini 7/8. |
| V2 | Correctif ciblé : exception question-définition simple (1-2 phrases, sans couche optionnelle). Diagnostic run 2-LLM V1 : inflation sur définitions atomiques même étiquetées optionnelles. Run 2-LLM : Gemini 8/8 ✅, Mistral 7/8 (cas mélatonine résistant). |
| V3 | Renforcement règle absolue : aucune couche optionnelle même brève/conditionnelle sur définition atomique ; exemple de calibrage négatif ajouté. |
