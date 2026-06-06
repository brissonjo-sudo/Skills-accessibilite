# Changelog

Toutes les modifications notables de cet écosystème sont documentées ici.  
Format basé sur [Keep a Changelog](https://keepachangelog.com/fr/1.0.0/).

---

## [Non publié]

- Bilan de l'écosystème (`docs/bilan_ecosysteme_skills_accessibilite.md`) — à venir

---

## [1.11.0] — 2026-06-06

### Ajouté

- **eval/results_tsa_v4.json** + **eval/analyse_tsa_v4_2llm.md** — run 2-LLM V4 (Mistral Large + Gemini 2.5 Flash) :
  Mistral with_skill 11/11 PASS, Gemini with_skill 10/11 PASS (Cas 3 anti-dérobade : limitation RLHF structurelle documentée).
  Nouveaux cas 9/10/11 (registre lisibilité) : 100% PASS tous providers, with_skill et baseline.
  **skill_accessibilite_tsa_V4.md déclaré VERSION STABLE.**

- **eval/analyse_tsa_v4_claude.md** — run Claude V4 (11 sous-agents) : 11/11 PASS, application silencieuse 11/11.

### Modifié

- **notes/Skill TSA.md** — V3 → V4, statut stable, tableau runs mis à jour (11 cas).
- **notes/Projet Skills Accessibilité.md** — TSA mis à jour V4 dans la table des skills stables.

---

## [1.10.0] — 2026-06-06

### Ajouté

- **skill_accessibilite_tsa_V4.md** — itération registre de lisibilité adaptable.
  Conclusion de l'analyse à 4 sous-agents (lentilles clinique, architecture, anti-validisme, testabilité) :
  pas de skill TSA niveau 2 séparé (duplication 70%, essentialisation de forme, non falsifiable).
  Delta net de V3 : **registre de lisibilité adaptable** — menu de format neutre déclenché par besoin
  exprimé (pas par déclaration clinique). Adaptations sur demande uniquement (≤120 mots, mots courants,
  exemples concrets, étape à la fois). Anti-essentialisation préservée intacte. Délégation aux skills
  DYS/fatigue co-actifs. Point 13 d'auto-vérification. Harnais étendu à 11 cas (3 nouveaux : C9, C10, C11).

---

## [1.9.0] — 2026-06-04

### Ajouté

- **eval/results_tsa_v3.json** + **eval/analyse_tsa_v3_2llm.md** — run 2-LLM V3 (Mistral Large + Gemini 2.5 Flash) :
  with_skill 8/8 PASS les deux providers, application silencieuse 8/8 les deux providers.
  Baseline Mistral 5/8 (Cas 2, 5, 6), Gemini 6/8 (Cas 2, 6) — le skill corrige tous les comportements défaillants.
  **skill_accessibilite_tsa_V3.md déclaré VERSION STABLE.** Résumé 3-providers : Claude 8/8, Mistral 8/8, Gemini 8/8.

### Modifié

- **notes/Skill TSA.md** — statut → stable, tableau runs mis à jour (Mistral 8/8, Gemini 8/8).
- **notes/Projet Skills Accessibilité.md** — TSA mis à jour V3 dans la table des skills stables.

---

## [1.8.0] — 2026-06-04

### Ajouté / Modifié

- **skill_accessibilite_tsa_V3.md** — itération anti-noyade du skill TSA (Phase 1 « fiabiliser le niveau 1 »).
  Correctifs issus de l'analyse des lacunes du V2 :
  1. **Contrainte absolue — application silencieuse** en tête (modèle HDC V3) : interdiction d'accuser
     réception du profil (« puisque tu es autiste… »).
  2. **Définition clinique corrigée** : niveau DSM-5 ≠ déficience intellectuelle ; calage sur le langage
     fonctionnel (on peut relever du niveau 2 sans DI).
  3. **Proportionnalité** plan vs réponse-d'abord (pas d'annonce de plan sur une question simple).
  4. **Règle anti-dérobade** (réponse franche d'abord, littéralité ≠ noyade de hedging).
  5. **Auto-vérification réparée et resserrée** (double « 13 » corrigé, 12 points).
  6. **Collision terminologique « niveau 2 »** supprimée dans la section essentialisation.

- **eval/promptfooconfig_tsa.yaml** — harnais dédié TSA (8 cas, 2 conditions, 2 LLMs). Le TSA n'avait
  jamais été évalué au banc promptfoo.

- **eval/results_tsa_claude_v3.json** + **eval/analyse_tsa_v3_claude.md** — run Claude V3 (16 sous-agents) :
  with_skill 8/8 PASS, application silencieuse 8/8, baseline 8/8. Finding cas 6 (test neurotypique vs
  reconnaissance) versé au futur niveau 2. Run 2-LLM en attente.

---

## [1.7.0] — 2026-06-04

### Ajouté

- **eval/analyse_fatigue_v3_2llm.md** — run 2-LLM V3 (Mistral + Gemini) : 8/8 PASS les deux providers.
  Cas mélatonine (SFC) corrigé sur Mistral (V1 : 0/8, V2 : 0/8, V3 : PASS).
  **skill_accessibilite_douleur_chronique_fatigue_cognitive_V3.md déclaré VERSION STABLE.**
  Résumé 3-providers : Claude 8/8, Mistral 8/8, Gemini 8/8.

- **eval/results_fatigue_claude_v3.json** + **eval/analyse_fatigue_v3_claude.md** — run Claude V3 (16 sous-agents) : 8/8 PASS, silencieux 8/8.

### Modifié

- **notes/Skill Douleur Chronique Fatigue Cognitive.md** — statut → stable, tableau runs mis à jour.
- **notes/Projet Skills Accessibilité.md** — skill V3 ajouté dans la table des skills stables, roadmap cochée.

---

## [1.6.0] — 2026-06-04

### Modifié

- **skill_accessibilite_douleur_chronique_fatigue_cognitive_V3.md** — renforcement ciblé issu du run 2-LLM V2 (Gemini 8/8 ✅, Mistral 7/8 — cas mélatonine résistant) :
  Règle "question-définition simple" renforcée en **règle absolue** : aucune couche optionnelle même brève/conditionnelle, aucun dosage/précaution/recommandation dans une couche secondaire, déclaration de condition ne justifie pas de conseils supplémentaires.
  Ajout d'un **exemple de calibrage négatif** (Exemple 1b) montrant explicitement le pattern d'inflation conditionnelle à éviter.
  Auto-vérification point 2 renforcé en conséquence.

- **eval/promptfooconfig_fatigue.yaml** — pointe vers V3.

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
| TSA | V4 (stable) | `claude/wonderful-fermat-enaoG` |
| Psychologie rigoureuse | V6 | `main` |
| Haute densité cognitive | V3 (stable) | `main` |
| Douleur chronique / Fatigue cognitive | V3 (stable) | `main` |
