# Skills Accessibilité & Psychologie

Un écosystème de skills Markdown conçus pour les LLMs (grands modèles de langage). Chaque skill programme le comportement du modèle pour répondre de façon adaptée aux personnes ayant des besoins cognitifs, sensoriels ou neurobiologiques spécifiques.

---

## Qu'est-ce qu'un skill ?

Un skill est un fichier texte (`.md`) que tu charges dans ton assistant IA (Claude, GPT, etc.) pour modifier sa façon de répondre. Il n'y a pas besoin de coder : il suffit de copier-coller le contenu dans le contexte système ou au début d'une conversation.

---

## Skills disponibles

| Dossier | Skill | Version | Description |
|---|---|---|---|
| `skills/psychologie-rigoureuse/` | Psychologie rigoureuse | V6 | Cadre d'analyse psychologique non dogmatique, marquage du degré de confiance |
| `skills/accessibilite-tdah/` | TDAH | V2.1 | Communication adaptée aux profils TDAH : structure, ancrage, charge cognitive réduite |
| `skills/accessibilite-dys/` | DYS | V3 | Adaptation pour dyslexie, dysorthographie, dyscalculie : lisibilité, reformulation |
| `skills/accessibilite-tsa/` | TSA | V4 | Communication adaptée aux personnes autistes : littéralité, prévisibilité, pas de sous-entendus |
| `skills/accessibilite-haute-densite-cognitive/` | Haute densité cognitive | V3 | Réponses denses et rigoureuses pour profils HDC/HPI : profondeur, rigueur épistémique |
| `skills/accessibilite-douleur-chronique-fatigue-cognitive/` | Douleur chronique / Fatigue cognitive | V3 | Adaptation pour fatigue cognitive et douleur persistante : économie cognitive, modularité |
| `skills/accessibilite-visuelle/` | Accessibilité visuelle | V1 | Adaptation pour basse vision et cécité : structure sémantique, alternatives textuelles, compatibilité lecteur d'écran |

Le fichier `docs/bilan_ecosysteme_skills_accessibilite.md` présente la philosophie commune et les complémentarités entre skills.

---

## Comment utiliser un skill

### Option 1 — Coller dans le prompt système (recommandé)

1. Ouvre le fichier `.md` du skill dans n'importe quel éditeur de texte.
2. Copie tout le contenu.
3. Dans ton interface IA (Claude, ChatGPT…), colle ce contenu dans le champ **"Instructions système"** ou **"System prompt"**.
4. Commence ta conversation : le modèle applique le skill automatiquement.

### Option 2 — Coller en début de conversation

Si tu n'as pas accès au prompt système, colle le contenu du skill au tout début de ta première message, avant ta question.

### Option 3 — Plateforme Claude Code (Anthropic)

Dépose le fichier `.md` dans ton dossier `.claude/commands/` et il sera disponible via la commande `/nom-du-fichier`.

---

## Structure du dépôt

```
skills-accessibilite/
├── README.md
├── CHANGELOG.md
├── .gitignore
├── skills/
│   ├── psychologie-rigoureuse/
│   │   └── skill_psychologie_rigoureuse_V6.md
│   ├── accessibilite-tdah/
│   │   └── skill_accessibilite_tdah_V2_1.md
│   ├── accessibilite-dys/
│   │   └── skill_accessibilite_dys_V3.md
│   ├── accessibilite-tsa/
│   │   └── skill_accessibilite_tsa_V4.md
│   ├── accessibilite-haute-densite-cognitive/
│   │   └── skill_accessibilite_haute_densite_cognitive_V3.md
│   ├── accessibilite-douleur-chronique-fatigue-cognitive/
│   │   └── skill_accessibilite_douleur_chronique_fatigue_cognitive_V3.md
│   └── accessibilite-visuelle/
│       └── skill_accessibilite_visuelle_V1.md
├── eval/
│   ├── promptfooconfig.yaml
│   ├── promptfooconfig_visuel.yaml
│   ├── prompts/
│   └── README.md
└── docs/
    └── bilan_ecosysteme_skills_accessibilite.md
```

Chaque skill est dans son propre dossier pour faciliter l'ajout de variantes (ex. `V2`, version "enfant", etc.).

---

## Feuille de route

Skills en cours de développement :
- `accessibilite-tsa-niveau2/` — la roadmap TSA niveau 2 a été abandonnée après analyse : le niveau DSM-5 n'est pas un paramètre communicationnel, et la simplification imposée sur déclaration clinique constitue une essentialisation de forme. Voir `docs/bilan_ecosysteme_skills_accessibilite.md` §2.6.

Skills envisagés :
- Harnais promptfoo pour les 3 skills fondateurs (TDAH, DYS, Psychologie rigoureuse)

---

## Contribuer

Les suggestions, corrections et nouveaux skills sont les bienvenus. Ouvre une *Issue* ou une *Pull Request* sur ce dépôt.

---

## Licence

Ce projet est distribué sous licence **MIT**.  
Tu es libre de l'utiliser, le modifier et le redistribuer, y compris à des fins commerciales, à condition de conserver la mention de l'auteur original.

Voir [`LICENSE`](LICENSE) pour le texte complet.
