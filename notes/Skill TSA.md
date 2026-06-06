---
tags: [skill, accessibilite, tsa, forme]
version: V4
statut: stable
---

# Skill Accessibilité TSA — V4

Skill de **forme** : adapte la communication pour les personnes autistes à **langage fonctionnel** (profils dits « de niveau 1 », incluant le diagnostic historique « Asperger »).

## Principes clés

- **Application silencieuse** (contrainte absolue) : ne jamais accuser réception du profil ni annoncer le mode
- Littéralité stricte : aucun sous-entendu, aucune figure de style non expliquée
- **Réponse franche d'abord** : littéralité ≠ noyade de hedging
- Structure prévisible, **proportionnée** (pas de plan annoncé sur une question simple)
- Pas d'ironie, pas de sarcasme ; formulations directes, sans ambiguïté
- Anti-essentialisation (test neurotypique)
- **Registre de lisibilité adaptable** : menu de format proposé sur expression d'un besoin de format (pas sur déclaration clinique)

## Périmètre clinique (précisé en V3, tenu en V4)

Les niveaux 1/2/3 du DSM-5 décrivent un **besoin de soutien**, **spécifié séparément** de la déficience intellectuelle. On peut relever du niveau 2 sans DI. Ce skill se cale sur le **langage fonctionnel**, pas sur un « niveau » pris comme synonyme d'absence de DI. Les adaptations de format (longueur, simplicité, concrétude) s'activent sur **besoin exprimé**, jamais sur catégorie présumée.

## Fichier source

`skills/accessibilite-tsa/skill_accessibilite_tsa_V4.md`

## Harnais d'évaluation

`eval/promptfooconfig_tsa.yaml` — 11 cas, 2 conditions, 2 LLMs (Mistral Large, Gemini 2.5 Flash).

## Relations

- Part du socle → [[Skill Psychologie Rigoureuse]]
- Co-activable avec → [[Skill TDAH]], [[Skill DYS]]
- Projet parent → [[Projet Skills Accessibilité]]

## Statut empirique du run

| Provider | with_skill | Application silencieuse |
|---|---|---|
| Claude (sonnet-4-6, 11 sous-agents) | 11/11 PASS | 11/11 |
| Mistral Large | 11/11 PASS | 11/11 |
| Gemini 2.5 Flash | 10/11 PASS | 10/11 |

Limitation documentée : Gemini Cas 3 (anti-dérobade) — comportement RLHF structurel, contextualise avant de répondre directement. Non corrigeable par instruction.

## Historique versions

| Version | Changements principaux |
|---|---|
| V1 | Première version |
| V2 | Approfondissement littéralité, gestion transitions. Jamais passée au banc promptfoo. |
| V3 | Itération anti-noyade : application silencieuse (contrainte absolue), définition clinique corrigée (niveau ≠ DI), proportionnalité, anti-dérobade, auto-vérification réparée. Run Claude 8/8, Mistral 8/8, Gemini 8/8. STABLE. |
| V4 | Registre de lisibilité adaptable : menu de format neutre déclenché par besoin exprimé (pas par catégorie clinique). Adaptations sur demande uniquement. Anti-essentialisation préservée. Harnais étendu à 11 cas. Run Claude 11/11, Mistral 11/11, Gemini 10/11. VERSION STABLE. |
