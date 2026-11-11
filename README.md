# Skills Accessibilité & Psychologie

[![validate](https://github.com/brissonjo-sudo/Skills-accessibilite/actions/workflows/validate.yml/badge.svg)](https://github.com/brissonjo-sudo/Skills-accessibilite/actions/workflows/validate.yml)
[![GitHub Release](https://img.shields.io/github/v/release/brissonjo-sudo/skills-accessibilite?label=version)](https://github.com/brissonjo-sudo/skills-accessibilite/releases/latest)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

Un écosystème de skills conçus pour Claude. Chaque skill programme le comportement du modèle pour répondre de façon adaptée aux personnes ayant des besoins cognitifs, sensoriels ou neurobiologiques spécifiques.

*English summary: [README.en.md](README.en.md).*

---

## Qu'est-ce qu'un skill ?

Un skill est un dossier contenant un fichier `SKILL.md` (instructions + métadonnées) que tu charges dans Claude pour modifier sa façon de répondre. Il n'y a pas besoin de coder.

---

## Skills disponibles

| Skill (dossier dans `skills/`) | Version sur `main` | Statut | Publiée (1.19.1) | Description |
|---|---|---|---|---|
| Psychologie rigoureuse (`psychologie-rigoureuse`) | V6.3 | candidat | V6.1 | Cadre d'analyse psychologique non dogmatique, marquage du degré de confiance |
| TDAH (`accessibilite-tdah`) | V2.4 | candidat | V2.2 | Communication adaptée aux profils TDAH : structure, ancrage, charge cognitive réduite |
| DYS (`accessibilite-dys`) | V3.2 | production | V3.1 | Adaptation pour dyslexie, dysorthographie, dyspraxie, dyscalculie : lisibilité, reformulation |
| TSA (`accessibilite-tsa`) | V4.2 | production | V4.1 | Communication adaptée aux personnes autistes : littéralité, prévisibilité, pas de sous-entendus |
| Haute densité cognitive (`accessibilite-haute-densite-cognitive`) | V3.3 | candidat | V3.1 | Réponses denses et rigoureuses pour profils HDC/HPI : profondeur, rigueur épistémique |
| Douleur chronique / Fatigue cognitive (`accessibilite-douleur-chronique-fatigue-cognitive`) | V3.3 | candidat | V3.1 | Adaptation pour fatigue cognitive et douleur persistante : économie cognitive, modularité |
| Accessibilité visuelle (`accessibilite-visuelle`) | V1.3 | candidat | V1.1 | Adaptation pour basse vision et cécité : structure sémantique, alternatives textuelles, compatibilité lecteur d'écran |

**Lire ce tableau.** La colonne « Publiée » donne la version contenue dans les ZIP de la [dernière release](https://github.com/brissonjo-sudo/Skills-accessibilite/releases/latest) : c'est celle que tu installes. La colonne « Version sur `main` » donne l'état du dépôt, qui peut être en avance. Un skill « candidat » a été modifié depuis sa dernière validation ; il sera publié après une vague de validation indépendante. La release 1.19.1 corrige une erreur factuelle et un défaut de chargement de la 1.19.0, sans changer de numéro de version par skill.

Chaque dossier contient un fichier **`SKILL.md`** : un en-tête YAML (`name`, `description`) suivi des règles du skill.

Pour chaque skill — **version courante, déclencheur, quand l'utiliser / quand ne pas l'utiliser, compatibilités et statut d'évaluation** — voir l'index canonique : [`docs/index_skills.md`](docs/index_skills.md). Des cas d'usage concrets sont rassemblés dans [`docs/usage.md`](docs/usage.md). Les conventions de contribution sont décrites dans [`AGENTS.md`](AGENTS.md).

Le fichier `docs/bilan_ecosysteme_skills_accessibilite.md` présente la philosophie commune et l'historique d'itération entre skills.

---

## Comment importer un skill dans Claude

### Méthode recommandée — Upload du ZIP (Capabilities)

Chaque skill se télécharge sous forme de ZIP depuis la [page Releases](https://github.com/brissonjo-sudo/Skills-accessibilite/releases/latest) du dépôt.

1. Dans Claude, ouvre **Paramètres → Capabilities**.
2. Clique sur **« + »** puis **Create skill**.
3. Choisis **Upload** et sélectionne le ZIP du skill (un ZIP = un skill).
4. Le skill devient disponible et s'active selon son déclencheur (voir la `description` de chaque skill).

> Un ZIP contient uniquement le dossier du skill et son `SKILL.md` (`accessibilite-tsa/SKILL.md`, etc.). Importe un ZIP à la fois.

### Méthode alternative — Coller dans le prompt système

Si tu n'utilises pas la fonctionnalité Capabilities :

1. Ouvre le fichier `SKILL.md` du skill.
2. Copie tout le contenu (y compris l'en-tête entre `---`).
3. Colle-le dans le champ **« Instructions système »** / **System prompt**, ou au tout début de ta conversation.

---

## Structure du dépôt

```
skills-accessibilite/
├── README.md              # ce fichier
├── README.en.md           # résumé en anglais
├── AGENTS.md              # conventions et invariants, pour agents et contributeurs
├── CONTRIBUTING.md        # critères d'acceptation d'un skill, versionnement, vagues
├── CHANGELOG.md
├── LICENSE
├── build_release.sh       # génère un ZIP par skill dans dist/
├── requirements-ci.txt    # dépendance des scripts de validation
├── skills/                # un dossier par skill, un seul fichier SKILL.md
│   ├── psychologie-rigoureuse/
│   ├── accessibilite-tdah/
│   ├── accessibilite-dys/
│   ├── accessibilite-tsa/
│   ├── accessibilite-haute-densite-cognitive/
│   ├── accessibilite-douleur-chronique-fatigue-cognitive/
│   └── accessibilite-visuelle/
├── docs/
│   ├── index_skills.md    # index canonique : versions, déclencheurs, statuts
│   ├── note_ethique.md    # limites éthiques
│   ├── usage.md           # cas d'usage concrets
│   └── bilan_ecosysteme_skills_accessibilite.md   # historique d'itération
├── eval/                  # banques de cas + protocole de validation en vagues
│   ├── promptfooconfig*.yaml            # banques de cas comportementaux
│   ├── activation_cases.json            # cas de déclenchement et de non-déclenchement
│   ├── prompt_benchmark_claude_code.md  # protocole d'une vague
│   ├── README.md
│   └── analyse_*.md, results*.json      # archives de l'ancien outillage
├── scripts/               # contrôles exécutés par la CI
├── .github/               # workflows (validation, release, relecture automatique)
└── notes/                 # notes de travail, non normatives
```

Chaque skill tient dans un unique `SKILL.md` (< 500 lignes, en deçà du seuil de découpage recommandé par Anthropic). Le contenu — règles, exemples de calibrage, historique — reste dans un seul fichier pour que le comportement soit complet dès le déclenchement.

---

## Évaluation

Le dossier `eval/` contient une banque de cas par skill et le protocole de validation. Une **vague** joue chaque cas deux fois — avec et sans le skill, même question, contextes isolés — puis fait juger les paires en aveugle par trois juges indépendants. Voir `eval/README.md`.

---

## Feuille de route

- `accessibilite-tsa-niveau2/` — abandonné après analyse : le niveau DSM-5 n'est pas un paramètre communicationnel, et la simplification imposée sur déclaration clinique constitue une essentialisation de forme. Voir `docs/bilan_ecosysteme_skills_accessibilite.md` §2.6.

---

## Note éthique

Ces skills **adaptent la communication** ; ils ne posent pas de diagnostic, ne constituent pas un soin et ne remplacent aucun professionnel. Voir [`docs/note_ethique.md`](docs/note_ethique.md).

---

## Contribuer

Les suggestions, corrections et nouveaux skills sont les bienvenus. Ouvre une *Issue* ou une *Pull Request*.

---

## Licence

Ce projet est distribué sous licence **MIT**.  
Tu es libre de l'utiliser, le modifier et le redistribuer, y compris à des fins commerciales, à condition de conserver la mention de l'auteur original.

Voir [`LICENSE`](LICENSE) pour le texte complet.
