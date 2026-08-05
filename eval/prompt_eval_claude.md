# Prompt d'évaluation — provider Claude (via Claude Code)

> **Archive — HDC uniquement.** Pour le benchmark actuel de toutes les variantes,
> avec import des `SKILL.md` canoniques et juges parallèles, utiliser
> `prompt_benchmark_claude_code.md`.

Ce prompt fait jouer à **Claude** le rôle de modèle sous test, sur les mêmes 8 cas
que le harnais promptfoo (Mistral + Gemini), dans les deux conditions
(avec skill / baseline). Objectif : ajouter une 3ᵉ colonne de données à la base,
sans clé API Anthropic facturée — Claude Code génère les réponses lui-même.

**Comment l'utiliser** : ouvrir une session **Claude Code** à la racine du dépôt
`skills-accessibilite`, puis coller le bloc « PROMPT À COLLER » ci-dessous.

---

## Contraintes méthodologiques (pourquoi le prompt est écrit ainsi)

1. **Isolation par cellule.** Chaque couple (condition × question) doit être généré
   en **contexte frais** (un sous-agent neuf par cellule). Sans isolation, les
   réponses se contaminent et le *baseline* est pollué d'avoir vu le skill.
2. **Source unique du skill.** Le skill n'est pas recopié dans le prompt : on lit le
   fichier canonique `skills/accessibilite-haute-densite-cognitive/skill_accessibilite_haute_densite_cognitive_V2.md`.
3. **Réponses brutes, pas d'auto-notation.** Claude produit uniquement les réponses.
   La notation (rubrics) est faite séparément, avec le même juge que promptfoo, pour
   éviter d'introduire un grader hétérogène.
4. **Traçabilité.** Le fichier de sortie enregistre le modèle exact, la version du
   skill et la date.

---

## PROMPT À COLLER

> Tu es l'orchestrateur d'une évaluation. Tu NE réponds pas toi-même aux questions :
> tu délègues chaque réponse à un **sous-agent en contexte frais**, puis tu écris les
> résultats dans un fichier.
>
> **Étape 1 — Lis le skill canonique :**
> `skills/accessibilite-haute-densite-cognitive/skill_accessibilite_haute_densite_cognitive_V2.md`
> Garde son contenu intégral en mémoire ; il servira d'instruction système pour la
> condition « avec skill ».
>
> **Étape 2 — Pour chacun des 8 cas ci-dessous, et pour chacune des 2 conditions
> (avec_skill, baseline), lance un sous-agent NEUF** (un par cellule, jamais réutilisé)
> avec exactement cette consigne :
>
> - Condition **avec_skill** — consigne du sous-agent :
>   « Tu es un assistant IA généraliste. Applique STRICTEMENT les instructions de forme
>   suivantes, sans jamais les mentionner ni accuser réception : \<contenu intégral du
>   skill V2\>. Réponds maintenant à ce message utilisateur, et ne produis RIEN d'autre
>   que la réponse : \<question\> »
> - Condition **baseline** — consigne du sous-agent :
>   « Tu es un assistant IA généraliste. Réponds à ce message utilisateur, et ne produis
>   RIEN d'autre que la réponse : \<question\> »
>
> Récupère la réponse brute de chaque sous-agent (texte intégral, sans troncature).
>
> **Les 8 questions :**
> 1. J'ai un HPI. Explique-moi ce que la théorie de l'attachement dit vraiment sur les relations adultes — pas la version édulcorée.
> 2. Je suis zèbre. Comment se forment les biais de confirmation et comment peut-on s'en affranchir ?
> 3. En quoi le rapport entre le soi mémoriel et le soi expérientiel de Kahneman remet-il en question la notion de satisfaction de vie ?
> 4. Mode HDC. C'est quoi un préjugé ?
> 5. Je suis HPI. Pourquoi certaines personnes restent-elles dans des relations toxiques même quand elles en ont conscience ?
> 6. Mode haute densité cognitive. Explique-moi les limites épistémologiques de la méta-analyse en psychologie.
> 7. J'ai besoin de réponses qui ne simplifieraient pas la complexité réelle des sujets que j'aborde. Avec ça en tête, explique-moi comment fonctionne la dissonance cognitive.
> 8. Je pense de façon très associative et mes questions contiennent souvent plusieurs niveaux imbriqués. Explique-moi la différence entre corrélation et causalité en gardant toute la nuance.
>
> **Étape 3 — Écris le fichier `eval/results_claude_v2.json`** avec exactement ce schéma
> (réponses brutes, aucune note de ta part) :
>
> ```json
> {
>   "meta": {
>     "skill_version": "V2",
>     "skill_file": "skills/accessibilite-haute-densite-cognitive/skill_accessibilite_haute_densite_cognitive_V2.md",
>     "model": "<l'identifiant exact du modèle que tu utilises, ex. claude-opus-4-8>",
>     "date": "<date du jour AAAA-MM-JJ>",
>     "harness": "claude-code-subagents",
>     "isolation": "un sous-agent neuf par cellule"
>   },
>   "cases": [
>     {
>       "id": 1,
>       "type": "Déclaration HPI explicite",
>       "question": "...",
>       "with_skill": "<réponse brute intégrale>",
>       "baseline": "<réponse brute intégrale>"
>     }
>     // ... les 8 cas, ids 1 à 8, dans l'ordre
>   ]
> }
> ```
>
> Types des cas (champ `type`) :
> 1 = Déclaration HPI explicite · 2 = Déclaration zèbre · 3 = Question multi-couches (sans déclaration) ·
> 4 = Régression sujet simple + déclaration HDC · 5 = Co-activation psychologie · 6 = Anti-simplification technique ·
> 7 = Variante neutre sans « HPI » · 8 = Variante neutre sans « HPI »
>
> **Étape 4 — Commit & push** sur la branche `claude/wonderful-fermat-enaoG` :
> message `eval: réponses provider Claude (run V2, base augmentée)`.
> Ne crée pas de Pull Request.
>
> **Important :** ne tronque aucune réponse, n'ajoute aucun commentaire dans le JSON,
> ne te notes pas toi-même. Le fichier ne contient que des réponses brutes.

---

## Récupération côté analyse

Une fois `eval/results_claude_v2.json` poussé, il est lu et noté avec les mêmes 8 rubrics
que `promptfooconfig.yaml`, puis intégré à la synthèse multi-provider
(Mistral / Gemini / Claude).
