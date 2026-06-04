# Changelog

Toutes les modifications notables de cet écosystème sont documentées ici.  
Format basé sur [Keep a Changelog](https://keepachangelog.com/fr/1.0.0/).

---

## [Non publié]

- Bilan de l'écosystème (`docs/bilan_ecosysteme_skills_accessibilite.md`) — à venir

---

## [1.5.0] — 2026-06-04

### Modifié

- **skill_accessibilite_douleur_chronique_fatigue_cognitive_V2.md** — correctif ciblé issu du run 2-LLM V1 (Mistral Large + Gemini 2.5 Flash, 7/8 chacun) :
  **Exception question-définition simple** ajoutée dans "Modularité optionnelle" et dans l'auto-vérification.
  Diagnostic : les deux providers ajoutaient une couche optionnelle sur des questions-définitions atomiques (« c'est quoi la mélatonine ? »), produisant de l'inflation même étiquetée. La règle : si la question demande la définition d'un concept unique sans sujet multi-niveaux, la réponse est 1 à 2 phrases — sans couche optionnelle.

- **eval/promptfooconfig_fatigue.yaml** — pointe vers V2.

---

## [1.4.0] — 2026-06-02

### Ajouté

- **skill_accessibilite_douleur_chronique_fatigue_cognitive_V1.md** (V1)
  6e skill de l'écosystème. Skill de forme pour douleur chronique, fatigue cognitive et brouillard
  mental (brain fog, fibromyalgie, SFC/EM, COVID long). Réduction de charge comme TDAH/DYS, mais
  angle distinct : économie d'un budget cognitif limité et fluctuant. Principes : réponse d'abord,
  modularité optionnelle, anti-injonction à l'effort (ne pousse pas à l'action), anti-minimisation /
  anti-positivité toxique, auto-suffisance (mémoire de travail), sécurité éthique prioritaire
  (comorbidité dépression). Déclencheur dual (déclaration OU besoin communicationnel d'économie).

- **eval/promptfooconfig_fatigue.yaml** — harnais d'évaluation dédié (8 cas, 2 conditions, 2 LLMs),
  config séparée du banc HDC.

- **eval/results_fatigue_claude_v1.json** + **eval/analyse_fatigue_v1_claude.md** — run provider
  Claude (16 sous-agents contexte frais) : with_skill 8/8 PASS, application silencieuse 8/8, aucune
  régression. Run 2-LLM (Mistral + Gemini) en attente côté utilisateur.

- **notes/Skill Douleur Chronique Fatigue Cognitive.md** — note Obsidian V1.

---

## [1.3.0] — 2026-06-01

### Modifié

- **skill_accessibilite_haute_densite_cognitive_V3.md** — **VERSION STABLE**
  Un seul ajout ciblé après analyse 3-providers (Mistral / Gemini / Claude) :
  **Contrainte absolue — application silencieuse** insérée en tête du skill, avant la
  hiérarchie des priorités. Règle nommée "absolue" et "prime sur toutes les autres",
  avec exemples de formulations interdites.

  Résultat du run V3 (Mistral + Gemini) : amélioration marginale sur le preamble
  (Mistral 0→1/8, Gemini 3→4/8). Confirmé : le preamble est un comportement RLHF
  structurel de Mistral et Gemini, non corrigeable par instruction seule. Documenté
  comme limitation de provider. **V3 déclaré version stable** — la contrainte reste
  (efficace sur Claude 8/8, partiellement sur Gemini).

- **eval/promptfooconfig.yaml** — pointe vers V3.

---

## [1.2.0] — 2026-06-01

### Modifié

- **skill_accessibilite_haute_densite_cognitive_V2.md**
  Deux correctifs ciblés issus du run d'évaluation multi-LLM V1 :
  1. **Application silencieuse** (nouveau) : règle interdisant tout préambule méta annonçant l'application du skill (« Voici une réponse en mode HDC »). Le skill s'applique sans se nommer.
  2. **Proportionnalité renforcée** : cas particulier explicite dans "Plafond souple" + formulation renforcée dans "Patterns à éviter" — la déclaration de profil n'induit pas de longueur sur les sujets simples.
  Structure inchangée (mode anti-noyade).

- **eval/promptfooconfig.yaml** — pointe désormais vers V2.

---

## [1.1.0] — 2026-06-01

### Ajouté

- **skill_accessibilite_haute_densite_cognitive_V1.md** (V1)
  Skill de forme pour utilisateurs à haute densité cognitive (HDC/HPI). Autorise et structure
  la profondeur informationnelle et la nuance. Déclencheur dual : déclaration explicite (HPI, zèbre)
  ou besoin communicationnel exprimé. Anti-édulcoration, questions multi-couches, structure navigable,
  tolérance à l'ambiguïté. Compatible avec les 4 skills existants.

- **eval/** — harnais d'évaluation promptfoo
  8 cas de test, 2 conditions (avec skill / baseline), 2 LLMs (GPT-5.5, Gemini 3.1 Pro).
  Source unique : pointe vers le fichier canonique dans `skills/`. `.env` exclu du dépôt.

- **notes/Skill HDC.md** — note Obsidian du skill V1 avec liaisons Graphify.

---

## [1.0.0] — 2026-05-27

### Ajouté

- **skill_accessibilite_tdah_V2_1.md** (V2.1)  
  Communication adaptée aux profils TDAH : réduction de la charge cognitive, structure explicite, ancrage fréquent, reformulations courtes.

- **skill_accessibilite_dys_V3.md** (V3)  
  Adaptation pour les troubles dys (dyslexie, dysorthographie, dyscalculie) : lisibilité renforcée, police conseillée, découpage syllabique optionnel, pas de justification de texte.

- **skill_accessibilite_tsa_V2.md** (V2)  
  Communication adaptée aux personnes autistes (TSA) : littéralité stricte, absence de sous-entendus, structure prévisible, gestion explicite des transitions.

- **skill_psychologie_rigoureuse_V6.md** (V6)  
  Cadre d'analyse psychologique non dogmatique : hiérarchie des priorités, marquage du degré de confiance scientifique, posture analytique sans interprétation déguisée.

- Structure modulaire du dépôt (un dossier par skill).
- README lisible par les non-techniciens.
- `.gitignore` pour OS et éditeurs courants.

---

## Versionnement des skills

| Skill | Version stable | Branche |
|---|---|---|
| TDAH | V2.1 | `main` |
| DYS | V3 | `main` |
| TSA | V2 | `main` |
| Psychologie rigoureuse | V6 | `main` |
| Haute densité cognitive | V3 (stable) | `claude/wonderful-fermat-enaoG` |
