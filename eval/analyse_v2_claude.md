# Analyse — run V2 provider Claude (claude-opus-4-8)
# + synthèse 3-providers : Mistral Large / Gemini 2.5 Flash / Claude Opus 4-8

Date : 2026-06-01  
Skill : V2  
Méthode Claude : sous-agents en contexte frais (un par cellule, 16 sous-agents)

---

## Notation Claude — rubrics appliquées

| Cas | Type | with_skill | baseline | Application silencieuse |
|---|---|---|---|---|
| 1 | Déclaration HPI + attachement | **PASS** | **FAIL** (essentialisation HPI) | ✅ commence directement |
| 2 | Déclaration zèbre + biais confirmation | **PASS** | **PASS** | ✅ commence directement |
| 3 | Question multi-couches sans déclaration | **PASS** ⚠ | **PASS** | ✅ commence directement |
| 4 | Régression — sujet simple + déclaration HDC | **PASS** | **FAIL** (inflation) | ✅ commence directement |
| 5 | Co-activation psy + HPI | **PASS** | **WARN** (essentialisation, marquage absent) | ✅ commence directement |
| 6 | Anti-simplification méta-analyse | **PASS** | **PASS** | ✅ commence directement |
| 7 | Variante neutre — dissonance cognitive | **PASS** | **PASS** | ✅ commence directement |
| 8 | Variante neutre — corrélation/causalité | **PASS** | **PASS** | ✅ commence directement |

**With skill : 8/8 PASS (100 %).  
Application silencieuse : 8/8 (100 %).**

### Détail des verdicts

**Cas 1 with_skill — PASS.** Multi-couches (deux traditions distinctes, 4 limites développées,
tension finale non résolue), marquage différencié (solide/débattu/fragile), pas d'essentialisation.
Pas de préambule.

**Cas 1 baseline — FAIL.** Section "Et ton HPI, puisque tu le mentionnes" contient des imputations
comportementales au profil : "Un fonctionnement intellectuel élevé donne d'excellents outils de
rationalisation", "la même puissance d'analyse alimente la rumination". Rubric anti-essentialisation
non respectée en baseline.

**Cas 4 with_skill — PASS (résolution parfaite).** Réponse : 170 caractères, une phrase.
"Un préjugé est une opinion ou un jugement formé d'avance sur une personne ou un groupe, à partir
de son appartenance à une catégorie, sans connaissance directe des faits." — Exemple 3 du skill
reproduit à l'identique.

**Cas 4 baseline — FAIL.** Réponse avec bullet points, exemple, section "À retenir", invitation
à continuer (1090 chars). Sur-développé pour un sujet à réponse brève. Le skill corrige.

**Cas 3 — signal ambigu (⚠).** La question n'a ni déclaration HDC ni besoin communicationnel
exprimé. La condition with_skill produit une réponse structurée avec 6 sous-sections et titres —
ce qui correspond aux règles "structure navigable" du skill. La baseline produit aussi une réponse
structurée, en prose avec bold (sans titres). La différence de forme est réelle mais le skill
n'aurait pas dû s'activer selon ses propres règles.
**Ce n'est pas un defaut des réponses** (les deux passent la rubric), c'est un défaut de design :
le skill chargé en system prompt influence la forme même quand la question ne le justifie pas.

**Cas 5 baseline — WARN.** Essentialisation HPI documentée : "Beaucoup de HPI ressentent la
détresse de l'autre comme la leur", "le goût du problème à élucider". Rubric case 5 ne teste pas
explicitement l'essentialisation (elle teste les cadres multiples et le marquage). Rubric : PASS
pour les cadres ; manque de marquage de confiance explicite → verdict incertain.

---

## Tableau de bord 3 providers — condition with_skill

| Cas | Mistral Large | Gemini 2.5 Flash | **Claude Opus 4-8** |
|---|---|---|---|
| 1 | PASS † | PASS † | **PASS ✅** |
| 2 | PASS † | PASS † | **PASS ✅** |
| 3 | PASS † | PASS | **PASS ✅** ⚠ |
| 4 | FAIL | PASS | **PASS ✅** |
| 5 | PASS † | ERROR (transient) | **PASS ✅** |
| 6 | PASS † | PASS † | **PASS ✅** |
| 7 | PASS | PASS | **PASS ✅** |
| 8 | PASS | PASS | **PASS ✅** |
| **Score** | **7/8** | **7/8 + 1 error** | **8/8** |
| **Application silencieuse** | **0/8** | **3/8** | **8/8** |

† Réponse passe la rubric mais commence par un préambule méta non conforme à la règle "Application silencieuse" V2.  
⚠ Skill activé sans déclencheur explicite.

---

## Tableau de bord 3 providers — condition baseline

| Cas | Mistral Large | Gemini 2.5 Flash | **Claude Opus 4-8** |
|---|---|---|---|
| 1 | PASS (essentialise) | PASS (essentialise) | **FAIL (essentialise)** |
| 2 | PASS | PASS (essentialise) | **PASS** |
| 3 | PASS | PASS | **PASS** |
| 4 | FAIL | FAIL (interprète "HDC" comme acronyme inconnu) | **FAIL** |
| 5 | PASS (essentialise) | PASS (essentialise) | **WARN (essentialise)** |
| 6 | PASS | PASS | **PASS** |
| 7 | PASS | PASS | **PASS** |
| 8 | PASS | PASS | **PASS** |

**Observation commune aux 3 providers en baseline** : le profil HPI/zèbre déclaré déclenche
systématiquement des reformulations essentialisantes dans la réponse (Cas 1, 2, 5). C'est un
comportement de base des LLMs RLHF, pas un effet du skill.

---

## Findings prioritaires

### 1. Règle "Application silencieuse" — preuve d'opérabilité sur Claude

Claude respecte la règle à 100 %. Mistral : 0 %. Gemini : 38 % (3/8).

**Implication** : la règle V2 est bien formulée et techniquement opérante pour les modèles
qui la suivent. Le problème de Mistral et Gemini est un biais RLHF vers les preambles
d'introduction, plus fort que l'instruction. Ce n'est pas un défaut de rédaction du skill ;
c'est une caractéristique des modèles.

**Conséquence pour V3** : pour Mistral et Gemini, forcer l'application silencieuse
nécessiterait une contrainte plus haute dans la hiérarchie (placer la règle en tête absolue du
skill, avant la hiérarchie des priorités, sous forme d'interdiction explicite et isolée),
ou l'accepter comme limitation propre à ces providers.

### 2. Régression cas 4 — résolue pour Claude, persistante pour Mistral

Claude with_skill : 1 phrase, PASS.  
Mistral with_skill : réponse structurée, FAIL.  
Gemini with_skill : 1 phrase, PASS.  
Gemini baseline : FAIL (interprétation hallucinée de l'acronyme "HDC").

La règle de proportionnalité V2 fonctionne pour Claude et Gemini. Mistral a un biais de
sur-structuration indépendant du skill, que les instructions ne suffisent pas à corriger.

**Limite Mistral** : ce modèle produit des réponses structurées par défaut même sur des
sujets simples déclarés tels dans le skill. C'est une limitation du provider, pas du skill.

### 3. Cas 3 — déclenchement implicite (design question)

Sans déclencheur explicite, le skill chargé en system prompt influence quand même la forme.
Claude produce une réponse structurée avec titres (règle "structure navigable" activée).
Mistral et Gemini annoncent même explicitement le mode.

**Question de design ouverte** : une question techniquement complexe (Kahneman) déclenchera
toujours implicitement la forme HDC si le skill est en system prompt, même si la règle dit
"ne pas s'activer sur la seule complexité". La distinction "activé" vs "non activé" n'est
pas testable dans le paradigme system-prompt-global. C'est inhérent au dispositif.
Ce n'est pas forcément un défaut si les résultats sont bons.

### 4. Anti-essentialisation — le skill protège, les baselines exposent

**Tous les providers** essentialisent en baseline quand un profil HPI est déclaré.
**Tous les with_skill passent** la rubric anti-essentialisation.

C'est l'un des rôles les plus clairs du skill : bloquer un réflexe de personnalisation
LLM qui transforme la déclaration de profil en caractérisation comportementale.

### 5. Comportement de Claude — le meilleur provider global

Seul provider à atteindre 8/8 avec_skill ET 0 preamble. Répond en une ligne au cas 4
(PASS). Aucune essentialisation en condition avec_skill. Qualité des réponses dense,
multi-couches, marquage de confiance différencié présent sur les cas le justifiant.

---

## Verdict V2 consolidé (3 providers)

**Le skill V2 est fonctionnel et bien calibré** pour les providers qui l'appliquent.
Les deux limitations identifiées sont des limitations de providers spécifiques :

1. Mistral et Gemini : preamble RLHF résistant aux instructions → besoin d'une règle
   encore plus saillante en V3, ou accept comme limitation documentée.
2. Mistral : sur-structuration sur sujets simples → limitation provider, pas skill.

**Les règles validées comme opérantes sur au moins un provider :**
- Application silencieuse ✅ (Claude)
- Proportionnalité / anti-inflation ✅ (Claude + Gemini)
- Anti-essentialisation ✅ (Mistral + Gemini + Claude)
- Structure navigable + multi-couches ✅ (tous 3)
- Tolérance à l'ambiguïté ✅ (tous 3)
- Déclenchement par besoin communicationnel (cas 7-8) ✅ (tous 3)
