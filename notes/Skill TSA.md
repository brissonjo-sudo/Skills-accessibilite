---
tags: [skill, accessibilite, tsa, forme]
version: V3
statut: stable
---

# Skill Accessibilité TSA — V3

Skill de **forme** : adapte la communication pour les personnes autistes à **langage fonctionnel** (profils dits « de niveau 1 », incluant le diagnostic historique « Asperger »).

## Principes clés

- **Application silencieuse** (contrainte absolue) : ne jamais accuser réception du profil ni annoncer le mode
- Littéralité stricte : aucun sous-entendu, aucune figure de style non expliquée
- **Réponse franche d'abord** : littéralité ≠ noyade de hedging
- Structure prévisible, **proportionnée** (pas de plan annoncé sur une question simple)
- Pas d'ironie, pas de sarcasme ; formulations directes, sans ambiguïté
- Anti-essentialisation (test neurotypique)

## Périmètre clinique (précisé en V3)

Les niveaux 1/2/3 du DSM-5 décrivent un **besoin de soutien**, **spécifié séparément** de la déficience intellectuelle. On peut relever du niveau 2 sans DI. Ce skill se cale sur le **langage fonctionnel**, pas sur un « niveau » pris comme synonyme d'absence de DI. → Le niveau 2 clinique fera l'objet d'un **skill distinct** (Phase 2).

## Fichier source

`skills/accessibilite-tsa/skill_accessibilite_tsa_V3.md`

## Harnais d'évaluation

`eval/promptfooconfig_tsa.yaml` — 8 cas, 2 conditions, 2 LLMs (Mistral Large, Gemini 2.5 Flash).

## Relations

- Part du socle → [[Skill Psychologie Rigoureuse]]
- Co-activable avec → [[Skill TDAH]], [[Skill DYS]]
- Projet parent → [[Projet Skills Accessibilité]]

## Statut empirique du run

| Provider | with_skill | Application silencieuse |
|---|---|---|
| Claude (sonnet-4-6, 16 sous-agents) | 8/8 PASS | 8/8 |
| Mistral Large | 8/8 PASS | 8/8 |
| Gemini 2.5 Flash | 8/8 PASS | 8/8 |

## Historique versions

| Version | Changements principaux |
|---|---|
| V1 | Première version |
| V2 | Approfondissement littéralité, gestion transitions. Jamais passée au banc promptfoo. |
| V3 | Itération anti-noyade : application silencieuse (contrainte absolue), définition clinique corrigée (niveau ≠ DI), proportionnalité, anti-dérobade, auto-vérification réparée. Run Claude 8/8. Run Mistral 8/8. Run Gemini 8/8. VERSION STABLE. |
