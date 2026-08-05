# Changelog

Toutes les modifications notables de cet écosystème sont documentées ici.  
Format basé sur [Keep a Changelog](https://keepachangelog.com/fr/1.0.0/).

---

## [Non publié]

Correctifs issus du premier benchmark contrôlé avec/sans skill (130 réponses appariées, aveugle, trois juges indépendants par variante). Deux régressions critiques corrigées — une de sécurité, une d'exactitude — plus un défaut de chargement présent depuis l'origine.

> **Validation.** Ces correctifs s'appuient sur le run `eval/runs/20260805-001935/` (protocole `eval/prompt_benchmark_claude_code.md`), **pas** sur un run `run_all.sh` : promptfoo n'était pas exécutable (ni réseau ni clés API au moment de la correction). `CONTRIBUTING.md` exige un passage au banc promptfoo pour toute montée de version — il reste à faire pour confirmer ces bumps.

### Corrigé — sécurité et exactitude

- **`accessibilite-douleur-chronique-fatigue-cognitive` V3.1 → V3.2** : la ressource de crise pouvait atterrir dans la couche « Si tu as l'énergie », c'est-à-dire dans un bloc que le skill définit lui-même comme facultatif à lire. Ajout d'une exclusion absolue (la sécurité n'entre jamais en couche optionnelle), d'une doctrine de placement (souffrance exprimée → partie toujours lue ; crise aiguë → en tête), d'un contre-exemple ❌/✅ et du point 13 d'auto-vérification. *Preuve : cas `fatigue` Cas 6, placement signalé par les juges comparatif et sceptique, pénalisé par le juge sceptique ; la baseline gagnait ce cas à la majorité.*
- **`accessibilite-visuelle` V1.1 → V1.2** : l'exemple 4 citait « les CRPV en France » comme structures d'accompagnement des personnes déficientes visuelles. Le sigle désigne en réalité les Centres Régionaux de Pharmacovigilance. Le skill propageait cette erreur telle quelle dans une réponse à une personne en détresse. Remplacé par des structures réelles ; ajout d'une règle sur les sigles et les ressources nommées. *Preuve : cas `visuel` Cas 8.*

### Corrigé — chargement des skills

- **Frontmatter invalide en YAML strict** dans `accessibilite-tdah` (V2.2 → V2.3) et `psychologie-rigoureuse` (V6.1 → V6.2) : un `:` suivi d'un espace dans une valeur non quotée fait échouer tout parseur YAML strict (`mapping values are not allowed here`). Défaut présent depuis l'origine et invisible pour le validateur, qui découpait le frontmatter sur le premier `:`. Remplacé par un tiret cadratin.
- **`scripts/validate_skills.py`** détecte désormais ce défaut (contrôle `find_yaml_breaking_scalars`, stdlib uniquement — le CI n'installe aucune dépendance).

### Corrigé — doctrine de co-activation

- **Arbitrage TDAH / fatigue** (`accessibilite-tdah` V2.3, `accessibilite-douleur-chronique-fatigue-cognitive` V3.2) : la règle « le skill fatigue prime sur l'injonction » n'existait que côté fatigue. Le skill TDAH n'en portait aucune trace et donnait « Commence par A » comme exemple à suivre. Règle rendue bilatérale, avec liste explicite des ouvertures bannies. *Preuve : co-activation C2, unique échec déterministe du bras avec skill.*
- **`accessibilite-haute-densite-cognitive` V3.1 → V3.2** : un besoin communicationnel exprimé (« ne simplifie pas ») est désormais traité comme une demande explicite de développement, prioritaire sur la proportionnalité — la règle ne couvrait que la déclaration de profil. *Preuve : `HDC` Cas 7, défaite unanime où le skill produisait une réponse moins dense que la baseline.*
- **`psychologie-rigoureuse` V6.2** : ajout de la contrainte d'application silencieuse, seul skill de l'écosystème à ne pas la porter alors que `AGENTS.md` en fait un critère minimum. *Preuve : co-activation C5, où la réponse nommait le skill à l'utilisateur.*

### Corrigé — banc d'évaluation

- **10 questions de test recopiées du skill évalué** réécrites (`promptfooconfig.yaml`, `_fatigue`, `_tsa`, `_visuel`). Sur l'une d'elles, la réponse produite était *byte-identique* à la réponse-type du skill : le modèle récitait. La phrase de déclenchement est conservée, le sujet change.
- **Rubriques réalignées sur les nouvelles questions** pour le cas 1 du harnais fatigue (sommeil lent/paradoxal) et le cas 6 du harnais visuel (éclipse solaire), afin que les juges n'évaluent plus les anciens sujets. L'inventaire du protocole est mis à jour à 61 cas principaux et 67 cas au total.
- **Politique des résultats bruts clarifiée** : les 13 archives JSON historiques déjà suivies sont conservées pour la reproductibilité ; les nouveaux `results*.json` restent ignorés et les analyses Markdown demeurent la source de vérité.
- **Juge circulaire** : quatre harnais désignaient `mistral-large-latest` comme juge alors que ce modèle est aussi un provider testé. Tous passent à `mistral-small-latest`, conformément à ce que le README affirmait déjà.
- **Assertions déterministes** ajoutées aux quatre harnais qui n'en avaient aucune (23 → 39). Ce sont pour l'essentiel des garde-fous anti-régression : sur le run de référence, seuls les plafonds de mots discriminaient réellement les deux conditions. `eval/README.md` corrigé en conséquence, et complété du harnais de co-activation qui manquait au tableau.

### Ajouté

- **`scripts/check_eval_leaks.py`** : échoue si une question de test recouvre à 75 % ou plus le texte du skill évalué. Branché au CI. Le simple partage d'une phrase de déclenchement documentée n'est pas traité comme une fuite.
- **`eval/prompt_benchmark_claude_code.md`** : protocole du benchmark contrôlé (matrice appariée, aveuglement, trois juges plus adjudication, macro-moyenne par variante).
- Cible `coactivation` dans `eval/run_all.sh`, qui n'en lançait que 7 sur 8 ; une cible inconnue échoue désormais au lieu d'être ignorée silencieusement.

### Sécurité

- `eval/runs/` ajouté à `eval/.gitignore`. Ce répertoire contient `blinding_map.json`, la table de correspondance A/B des juges : la committer annulerait rétroactivement l'aveuglement du protocole.
- Le contrôle « aucun `.env` commité », perdu lors de la refonte du workflow CI, est rétabli.

---

## [1.19.0] — 2026-06-21

Release de documentation et de maintenabilité : aucun changement de comportement des skills (les 7 `SKILL.md` sont identiques à 1.18.0). Ajout d'un index canonique, d'une note éthique, d'un guide de contribution, de cas d'usage, et harmonisation de la documentation.

### Ajouté

- **`docs/index_skills.md`** : index canonique de l'écosystème — pour chaque skill, version stable, fichier source, déclencheur, risques couverts, compatibilités, statut d'évaluation ; rappel de l'ordre de préséance et matrice de co-activation.
- **`docs/note_ethique.md`** : cadre éthique explicite (adaptation de communication, pas de diagnostic, pas de soin, pas de substitution professionnelle, anti-essentialisation, sécurité éthique prioritaire, ressources d'urgence).
- **`AGENTS.md`** : guide de contribution (conventions de skills, invariants validés par CI, ordre de préséance, workflow d'évaluation et de release).
- **`docs/usage.md`** : cas d'usage concrets par skill et par contexte, avec rappel des co-activations typiques.

### Modifié

- **README** : liens vers l'index canonique, la note éthique, les cas d'usage et `AGENTS.md` ; mention « quand l'utiliser / quand ne pas l'utiliser » renvoyant à l'index.
- **`docs/bilan_ecosysteme_skills_accessibilite.md`** : suppression des mentions périmées « accessibilite-tsa (à venir) » (le skill TSA est en production depuis V4), y compris l'en-tête de la section 6 archivée ; liste des skills couverts mise à jour (7 skills en production) ; renvoi vers l'index canonique.
- **Cohérence documentaire** (micro-corrections) :
  - `docs/index_skills.md` : statut d'éval HDC renseigné (`eval/promptfooconfig.yaml`, 8 cas) au lieu de « banc à formaliser » ; matrice de co-activation alignée sur le bilan (statuts *testée en stress* / *documentée* / *spécifiée*), suppression d'un doublon TSA/Visuelle.
  - `docs/bilan_…md` : label déprécié « skill 1 » remplacé par `psychologie-rigoureuse` ; tableau « État de production » (section 7) aligné sur les versions stables bumpées (V6.1, V2.2, V3.1, V4.1, V3.1, V3.1, V1.1) avec note sur les chiffres d'éval.
  - `CHANGELOG.md` : branche de TSA corrigée (`main` au lieu de `claude/wonderful-fermat-enaoG`).
  - `eval/README.md` : TDAH V2.2 / 10 cas ; versions des harnais bumpées ; convention de versionnement réécrite pour le format `SKILL.md` (plus de fichier `skill_..._V2.md`).

---

## [1.18.0] — 2026-06-11

Amélioration de la robustesse et de la maintenabilité de l'écosystème (déclencheurs, articulation inter-skills, CI).

### Ajouté

- **Déclencheur « TDA »** (skill TDAH) : « j'ai un TDA », « trouble de l'attention » (avec ou sans hyperactivité) ajoutés à la description et à la liste des formulations déclenchantes. Deux cas d'éval (C9 déclenchement TDA, C10 non-déclenchement sur distraction passagère).
- **Bloc « Ordre de préséance entre skills »** : section canonique strictement identique insérée dans les 7 SKILL.md, fixant l'ordre de préséance sur la forme (sécurité éthique > `accessibilite-visuelle` > skills de réduction de charge > `accessibilite-tsa` > `accessibilite-haute-densite-cognitive` ; `psychologie-rigoureuse` régit le fond hors de cet ordre).
- **CI** : `scripts/validate_skills.py` (validation frontmatter, `name` == dossier, description ≤ 1024, fichier < 500 lignes, identité des blocs de préséance) ; workflows `validate.yml` (push/PR sur `main`) et `release.yml` (publication automatique des ZIP sur tag).

### Modifié

- **Articulation inter-skills** : toutes les références opaques « skill 1 » remplacées par le nom réel `psychologie-rigoureuse` dans les 6 skills d'accessibilité, avec reformulation naturelle. Ajout d'une ligne de dégradation gracieuse dans chaque section d'articulation (si `psychologie-rigoureuse` n'est pas chargé, ignorer les règles de co-activation).
- **Harmonisation** (skill TDAH) : suppression de « arbitrer au cas par cas » (contradictoire avec le bloc canonique) ; plafond de co-activation exprimé en relatif.
- **build_release.sh** : la validation des skills s'exécute avant la génération des ZIP (échec = pas de ZIP).
- **Versions** : TDAH V2.1 → V2.2 ; bump mineur des 6 autres skills (touchés par le bloc de préséance).

### CI/CD — GitHub Actions (`ci: validate skills`)

- Workflow `.github/workflows/validate.yml` déclenché sur tout push et PR vers `main`.
- `scripts/check_frontmatter.py` : vérifie que chaque `skills/*/SKILL.md` a un frontmatter
  valide (`name` ≤ 64 chars, regex `[a-z0-9-]+` ; `description` ≤ 1024 chars).
- `scripts/check_eval_configs.py` : résout les chemins `file://` dans les 8 configs promptfoo
  et vérifie que chaque `SKILL.md` référencé existe.
- Step no-.env : `git ls-files eval/.env` doit retourner vide.
- Step build-zips : `build_release.sh` doit produire 7 ZIPs valides avec `<name>/SKILL.md`.

### Évaluation — Provider Claude ajouté (Axe dette d'éval)

- `anthropic:claude-sonnet-4-6` ajouté comme 3e provider dans les 7 harnais existants
  (`promptfooconfig.yaml`, `_fatigue`, `_tsa`, `_visuel`, `_dys`, `_tdah`, `_psychologie`).
- `eval/.env.example` : ajout `ANTHROPIC_API_KEY=...`.
- `eval/run_all.sh` : avertissement non-bloquant si `ANTHROPIC_API_KEY` absente.
- Méthodo désormais uniforme 3-providers (Mistral Large, Gemini 2.5 Flash, Claude Sonnet 4.6)
  pour tous les skills. Les 3 harnais sans résultats (DYS, TDAH, Psychologie) sont prêts à
  tourner : `cd eval/ && ./run_all.sh dys tdah psychologie`.

### Évaluation — Harnais co-activation (6 paires)

- `eval/promptfooconfig_coactivation.yaml` : 6 cas testant les règles d'articulation inter-skills
  jamais validées empiriquement au banc :
  - C1 HDC+DYS : plafond DYS prime (≤ 220 mots)
  - C2 TDAH+Fatigue : pas d'injonction à l'action
  - C3 TSA+Psychologie : littéralité + marquage confiance simultanés
  - C4 DYS+Psychologie : phrases courtes + marquage différencié (≤ 220 mots)
  - C5 HDC+Psychologie : densité additive (≥ 2 dimensions épistémiques)
  - C6 TDAH+DYS : double réduction, plafond TDAH le plus bas (≤ 180 mots)
- `eval/prompts/with_two_skills.yaml` : template pour charger deux skills en system prompt.

### Diffusion & communauté

- `CONTRIBUTING.md` : critères d'acceptation d'un skill, convention de versionnement,
  conventions de commit, hygiène secrets, commandes de lancement des évaluations.
- `README.md` : badges (version GitHub Release, MIT, tested with promptfoo) ajoutés en haut.
- `README.en.md` : README anglais court (tableau 7 skills, instructions d'import, section éval).
- `eval/.gitignore` : `results*.json` gitignorés (les 11 fichiers pèsent 6,5 Mo ; les analyses
  Markdown `analyse_*.md` restent versionnées comme source de vérité archivée).

---

## [1.17.0] — 2026-06-08

Première version publique importable dans Claude (Capabilities / ZIP).

### Refactor — skills importables (branche `refactor/skills-importables`)

- **Conformité format Claude Skills** : chaque skill renommé en `SKILL.md` (nom requis), une
  seule version conservée par skill (la plus récente). Versions historiques supprimées du dépôt
  (toujours dans l'historique git) : HDC V1/V2, Fatigue V1/V2, TSA V2/V3.
- **Descriptions YAML ≤ 1024 caractères** : raccourcies pour TSA V4 (1082→819), Fatigue V3
  (1066→662) et DYS V3 (1002→693). Les 4 autres étaient déjà conformes.
- **Choix d'architecture** : skills gardés en un seul `SKILL.md` (pas de découpage
  guidelines/examples). Justification : aucune limite de taille dure (la « limite 16 KB » du
  brief n'existe pas — limite réelle 30 MB/bundle), tous les skills < 500 lignes (seuil de
  découpage recommandé), et les exemples de calibrage sont comportementalement essentiels +
  couplés au harnais d'éval. Garder le contenu complet préserve la fidélité de l'évaluation et
  la robustesse des règles de sécurité (toujours actives, pas chargées conditionnellement).
- **eval/** : les 7 configs promptfoo pointent désormais vers `SKILL.md`.
- **README** : structure mise à jour, instructions d'import via ZIP (Capabilities).
- **build_release.sh** : génère un ZIP par skill (dossier à la racine) pour les GitHub Releases.
  `dist/` ajouté au `.gitignore`.

---

## [1.16.0] — 2026-06-07

### Ajouté

- **eval/promptfooconfig_dys.yaml** — harnais 8 cas pour DYS V3 (application silencieuse déterministe,
  phrases courtes + plafond, anti-essentialisation DYS, co-activation skill 1, non-déclenchement,
  données chiffrées, sécurité éthique).
- **eval/promptfooconfig_tdah.yaml** — harnais 8 cas pour TDAH V2.1 (application silencieuse déterministe,
  action unique + plafond ~150 mots, chunking > 3 étapes, anti-moralisation, anti-essentialisation TDAH,
  co-activation skill 1, non-déclenchement fatigue ordinaire, sécurité éthique).
- **eval/promptfooconfig_psychologie.yaml** — harnais 8 cas pour Psychologie rigoureuse V6 (marquage
  différencié, non-prescription déterministe, anti-essentialisation déterministe, mention pro sur souffrance
  déterministe, sécurité éthique + 3114 déterministe, plafond ~250 mots, anti-relance cascade déterministe,
  formulation impersonnelle).
- **eval/run_all.sh** — runner unique pour lancer tous les harnais séquentiellement, avec filtrage
  automatique des erreurs API (failureReason 2), résumé global, et sélection partielle par arguments.

### Modifié

- **eval/README.md** — mis à jour pour couvrir l'écosystème complet (7 harnais), documentation des
  assertions déterministes vs sémantiques, nouveau juge non-circulaire (`mistral-small-latest`).

### Améliorations techniques

- **Juge non-circulaire** : les 3 nouveaux harnais utilisent `mistral:mistral-small-latest` comme juge
  (non testé comme provider) au lieu de `mistral-large-latest`. Réduit le biais juge/provider.
- **Assertions déterministes** (type `javascript`) : 19 nouvelles assertions régex non-dépendantes
  du juge LLM — application silencieuse, anti-essentialisation, anti-prescription, anti-relance,
  plafonds de mots, anti-emojis, mention pro, référence 3114.

---

## [1.15.0] — 2026-06-07

### Corrigé

- **docs/bilan_ecosysteme_skills_accessibilite.md §3.8** — erreur factuelle corrigée : la résistance RLHF
  à l'application silencieuse sur HDC n'est pas une « exception unique Gemini ». Données réelles :
  Mistral 1/8 FAIL (preamble), Gemini 4/8 FAIL (preamble). Deux manifestations documentées :
  HDC (Mistral + Gemini) et TSA V4 C3 (Gemini).
- **docs/bilan_ecosysteme_skills_accessibilite.md §7** — ligne HDC corrigée avec résultats précis
  (Claude 8/8, Mistral 7/8, Gemini 4/8 application silencieuse) et les deux providers mentionnés.
- **docs/bilan_ecosysteme_skills_accessibilite.md §7** — ajout règle méta co-activation plafonds :
  le plafond le plus bas parmi les skills actifs prime. Cas HDC+DYS documenté (~150 mots).
- **skills/accessibilite-dys/skill_accessibilite_dys_V3.md** — suppression mention « à venir » sur TSA
  (TSA V4 est en production). Règle d'arbitrage densité/aération précisée.
- **skills/accessibilite-tsa/skill_accessibilite_tsa_V4.md** — ajout de la section co-activation
  avec `accessibilite-visuelle` (réciprocité manquante).
- **skills/accessibilite-haute-densite-cognitive/skill_accessibilite_haute_densite_cognitive_V3.md** —
  ajout plafond ~150 mots sur co-activation HDC+DYS.
- **README.md** — refonte complète : 7 skills (vs 4), versions correctes (TSA V4, etc.), roadmap
  nettoyée (TSA niveau 2 abandonné documenté, Visuelle livré), instruction Claude Code corrigée
  (`.claude/commands/` au lieu de `.claude/skills/`).

---

## [1.14.0] — 2026-06-07

### Ajouté / Modifié

- **docs/bilan_ecosysteme_skills_accessibilite.md** — mise à jour complète du bilan de synthèse.
  Nouvelles sections : trajectoires HDC V1→V3, Fatigue V1→V3, TSA V3→V4, Visuelle V1.
  Nouveaux patterns : harnais promptfoo (3.7), application silencieuse contrainte absolue (3.8),
  essentialisation de forme vs fond (3.9). Section 5bis : évolutions méthodologiques juin 2026.
  Section 7 mise à jour avec les 7 skills en production.

- **notes/Bilan Écosystème Skills.md** — skills couverts et principes méthodologiques mis à jour.

- **CHANGELOG.md** — section [Non publié] soldée.

---

## [1.13.0] — 2026-06-07

### Ajouté

- **eval/results_visuel_v1.json** + **eval/analyse_visuel_v1_2llm.md** — run 2-LLM V1 (Mistral Large + Gemini 2.5 Flash) :
  Mistral with_skill 8/8 PASS, application silencieuse 8/8.
  Gemini with_skill 5/5 évalués PASS (3 erreurs 503 infrastructure — API indisponible, pas d'échec du skill).
  Démarque baseline Mistral : C1 FAIL sans skill (annonce du mode accessibilité) → PASS avec skill.
  **skill_accessibilite_visuelle_V1.md déclaré VERSION STABLE.**

### Modifié

- **notes/Skill Accessibilité Visuelle.md** — statut → stable, tableau runs mis à jour.
- **notes/Projet Skills Accessibilité.md** — visuel V1 stable dans la table + roadmap cochée.

---

## [1.12.0] — 2026-06-07

### Ajouté

- **skills/accessibilite-visuelle/skill_accessibilite_visuelle_V1.md** — nouveau skill de forme pour les utilisateurs
  malvoyants et non-voyants/lecteurs d'écran. Deux profils couverts : basse vision (aération, hiérarchie sémantique)
  et cécité/lecteur d'écran (lisibilité linéaire, pas d'ASCII art, pas d'emojis décoratifs, tableaux auto-suffisants).
  Application silencieuse (contrainte absolue). Anti-essentialisation. Alternatives textuelles pour tout contenu visuel.

- **eval/promptfooconfig_visuel.yaml** — harnais 8 cas, 2 conditions (with_skill / baseline), 2 LLMs
  (Mistral Large, Gemini 2.5 Flash). Cas couverts : application silencieuse, emojis décoratifs, références
  positionnelles, ASCII art, tableaux, contenu visuel, structure sémantique des titres, sécurité éthique.

- **eval/analyse_visuel_v1_claude.md** — run Claude V1 (8 sous-agents) : 8/8 PASS, application silencieuse 8/8.

- **notes/Skill Accessibilité Visuelle.md** — note Obsidian du skill V1.

### Modifié

- **notes/Projet Skills Accessibilité.md** — Skill Accessibilité Visuelle ajouté dans la table (en cours d'évaluation).

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
| TDAH | V2.2 | `main` |
| DYS | V3.1 | `main` |
| TSA | V4.1 (stable) | `main` |
| Psychologie rigoureuse | V6.1 | `main` |
| Haute densité cognitive | V3.1 (stable) | `main` |
| Douleur chronique / Fatigue cognitive | V3.1 (stable) | `main` |
| Accessibilité visuelle | V1.1 | `main` |
