# Changelog

Toutes les modifications notables de cet écosystème sont documentées ici.  
Format basé sur [Keep a Changelog](https://keepachangelog.com/fr/1.0.0/).

---

## [Non publié]

- Bilan de l'écosystème (`docs/bilan_ecosysteme_skills_accessibilite.md`) — à venir

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
| Haute densité cognitive | V1 (en évaluation) | `claude/wonderful-fermat-enaoG` |
