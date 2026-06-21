# Skills Accessibilité & Psychologie

[![validate](https://github.com/brissonjo-sudo/Skills-accessibilite/actions/workflows/validate.yml/badge.svg)](https://github.com/brissonjo-sudo/Skills-accessibilite/actions/workflows/validate.yml)

Un écosystème de skills conçus pour Claude. Chaque skill programme le comportement du modèle pour répondre de façon adaptée aux personnes ayant des besoins cognitifs, sensoriels ou neurobiologiques spécifiques.

---

## Qu'est-ce qu'un skill ?

Un skill est un dossier contenant un fichier `SKILL.md` (instructions + métadonnées) que tu charges dans Claude pour modifier sa façon de répondre. Il n'y a pas besoin de coder.

---

## Skills disponibles

| Dossier | Skill | Version | Description |
|---|---|---|---|
| `skills/psychologie-rigoureuse/` | Psychologie rigoureuse | V6.1 | Cadre d'analyse psychologique non dogmatique, marquage du degré de confiance |
| `skills/accessibilite-tdah/` | TDAH | V2.2 | Communication adaptée aux profils TDAH : structure, ancrage, charge cognitive réduite |
| `skills/accessibilite-dys/` | DYS | V3.1 | Adaptation pour dyslexie, dysorthographie, dyspraxie, dyscalculie : lisibilité, reformulation |
| `skills/accessibilite-tsa/` | TSA | V4.1 | Communication adaptée aux personnes autistes : littéralité, prévisibilité, pas de sous-entendus |
| `skills/accessibilite-haute-densite-cognitive/` | Haute densité cognitive | V3.1 | Réponses denses et rigoureuses pour profils HDC/HPI : profondeur, rigueur épistémique |
| `skills/accessibilite-douleur-chronique-fatigue-cognitive/` | Douleur chronique / Fatigue cognitive | V3.1 | Adaptation pour fatigue cognitive et douleur persistante : économie cognitive, modularité |
| `skills/accessibilite-visuelle/` | Accessibilité visuelle | V1.1 | Adaptation pour basse vision et cécité : structure sémantique, alternatives textuelles, compatibilité lecteur d'écran |

Chaque dossier contient un fichier **`SKILL.md`** : un en-tête YAML (`name`, `description`) suivi des règles du skill.

Pour chaque skill — **version stable, déclencheur, quand l'utiliser / quand ne pas l'utiliser, compatibilités et statut d'évaluation** — voir l'index canonique : [`docs/index_skills.md`](docs/index_skills.md). Des cas d'usage concrets sont rassemblés dans [`docs/usage.md`](docs/usage.md). Les conventions de contribution sont décrites dans [`AGENTS.md`](AGENTS.md).

Le fichier `docs/bilan_ecosysteme_skills_accessibilite.md` présente la philosophie commune et l'historique d'itération entre skills.

---

## Comment importer un skill dans Claude

### Méthode recommandée — Upload du ZIP (Capabilities)

Chaque skill se télécharge sous forme de ZIP depuis la [page Releases](../../releases) du dépôt.

1. Dans Claude, ouvre **Paramètres → Capabilities**.
2. Clique sur **« + »** puis **Create skill**.
3. Choisis **Upload** et sélectionne le ZIP du skill (un ZIP = un skill).
4. Le skill devient disponible et s'active selon son déclencheur (voir la `description` de chaque skill).

> Un ZIP contient le dossier du skill à sa racine (`accessibilite-tsa/SKILL.md`, etc.). Importe un ZIP à la fois.

### Méthode alternative — Coller dans le prompt système

Si tu n'utilises pas la fonctionnalité Capabilities :

1. Ouvre le fichier `SKILL.md` du skill.
2. Copie tout le contenu (y compris l'en-tête entre `---`).
3. Colle-le dans le champ **« Instructions système »** / **System prompt**, ou au tout début de ta conversation.

---

## Structure du dépôt

```
skills-accessibilite/
├── README.md
├── CHANGELOG.md
├── .gitignore
├── skills/
│   ├── psychologie-rigoureuse/
│   │   └── SKILL.md
│   ├── accessibilite-tdah/
│   │   └── SKILL.md
│   ├── accessibilite-dys/
│   │   └── SKILL.md
│   ├── accessibilite-tsa/
│   │   └── SKILL.md
│   ├── accessibilite-haute-densite-cognitive/
│   │   └── SKILL.md
│   ├── accessibilite-douleur-chronique-fatigue-cognitive/
│   │   └── SKILL.md
│   └── accessibilite-visuelle/
│       └── SKILL.md
├── eval/                  # harnais d'évaluation promptfoo (multi-LLM)
│   ├── promptfooconfig*.yaml
│   ├── run_all.sh
│   └── README.md
└── docs/
    └── bilan_ecosysteme_skills_accessibilite.md
```

Chaque skill tient dans un unique `SKILL.md` (< 500 lignes, en deçà du seuil de découpage recommandé par Anthropic). Le contenu — règles, exemples de calibrage, historique — reste dans un seul fichier pour que le comportement soit complet dès le déclenchement.

---

## Évaluation

Le dossier `eval/` contient un harnais [promptfoo](https://promptfoo.dev) par skill : deux conditions (avec / sans skill), deux LLM (Mistral Large, Gemini 2.5 Flash), assertions déterministes et sémantiques. Voir `eval/README.md`.

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
