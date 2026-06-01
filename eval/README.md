# Harnais d'évaluation — skill accessibilite-haute-densite-cognitive V1

Évalue le skill HDC sur deux conditions (avec / sans) et deux LLMs (GPT-5.5, Gemini 3.1 Pro).

## Prérequis

- Node.js LTS
- promptfoo installé globalement : `npm install -g promptfoo`
- Clés API OpenAI et Google AI Studio

## Installation

```bash
cd eval/
cp .env.example .env
# Renseigner MISTRAL_API_KEY, GOOGLE_API_KEY et XAI_API_KEY dans .env
```

## Lancement

Depuis le dossier `eval/` :

```bash
promptfoo eval -o results.json
promptfoo view
```

`results.json` contient les résultats bruts. Le pousser sur la branche pour analyse partagée.

## Structure des tests

| Cas | Type | Objet |
|-----|------|-------|
| 1 | Déclaration explicite HPI | Théorie de l'attachement — profondeur |
| 2 | Déclaration explicite zèbre | Biais de confirmation — mécanismes |
| 3 | Question multi-couches (sans déclaration) | Soi mémoriel vs expérientiel (Kahneman) |
| 4 | Régression — sujet simple + déclaration HDC | Définition d'un préjugé |
| 5 | Co-activation skill 1 (psychologie) | Relations toxiques — multi-cadres |
| 6 | Anti-simplification technique | Limites épistémologiques des méta-analyses |
| **7** | **Variante neutre sans « HPI »** | **Dissonance cognitive — déclenchement par besoin** |
| **8** | **Variante neutre sans « HPI »** | **Corrélation vs causalité — déclenchement par besoin** |

**Les cas 7 et 8 sont prioritaires** : ils valident que le skill se déclenche sur le besoin communicationnel exprimé seul, sans le mot « HPI ».

## Source unique du skill

Le fichier `promptfooconfig.yaml` pointe directement vers le skill canonique :

```
../skills/accessibilite-haute-densite-cognitive/skill_accessibilite_haute_densite_cognitive_V1.md
```

Pour changer de version (ex. V1 → V2), mettre à jour uniquement la ligne `skill:` du `defaultTest` dans `promptfooconfig.yaml`. Aucune copie du skill dans `eval/`.

## Providers actifs

| Provider | Modèle | Clé |
|----------|--------|-----|
| Mistral AI | `mistral-large-latest` | `MISTRAL_API_KEY` |
| Google AI Studio | `gemini-3.1-pro-preview` | `GOOGLE_API_KEY` |
| xAI | `grok-3` | `XAI_API_KEY` |

## Analyse des résultats

Priorités d'analyse (dans l'ordre) :

1. **Cas 7 et 8** : le skill se déclenche-t-il sans le mot « HPI » ? Les réponses avec-skill sont-elles plus denses/nuancées que baseline ?
2. **Régressions** (cas 4) : le skill n'induit-il pas de sur-développement sur des sujets simples ?
3. **Co-activation skill 1** (cas 5) : le marquage de confiance et la formulation impersonnelle sont-ils respectés ?
4. **Différences inter-LLM** : un LLM produit-il plus d'essentialisation HDC ? Plus de vulgarisation forcée ?

## Convention de versionnement

Lors d'une itération du skill V1 → V2 :
1. Créer `skills/accessibilite-haute-densite-cognitive/skill_accessibilite_haute_densite_cognitive_V2.md`
2. Mettre à jour la ligne `skill:` dans `promptfooconfig.yaml`
3. Relancer `promptfoo eval` pour mesurer le delta
