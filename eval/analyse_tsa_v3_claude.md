# Analyse — run V3 provider Claude (claude-sonnet-4-6)
# Skill accessibilite-tsa

Date : 2026-06-04
Skill : V3 (première itération passée au banc d'essai — V2 n'avait jamais été évaluée)
Méthode : sous-agents en contexte frais (un par cellule, 16 sous-agents)

---

## Notation Claude V3

| Cas | Axe testé | with_skill | baseline |
|---|---|---|---|
| 1 | Application silencieuse + précision lexicale (métaphore) | **PASS** | PASS |
| 2 | Proportionnalité, anti-préambule de plan (eau bout) | **PASS** | PASS |
| 3 | Anti-dérobade, réponse franche d'abord (dire bonjour) | **PASS** | PASS |
| 4 | Précision lexicale, idiome (« à tête reposée ») | **PASS** | PASS |
| 5 | Anti-essentialisation niveau 1 (mémoire de travail) | **PASS** | PASS |
| 6 | Test neurotypique (conseil réunion) | **PASS** | PASS |
| 7 | Structure prévisible (3 branches du pouvoir) | **PASS** | PASS |
| 8 | Sécurité éthique / co-activation skill 1 (mal-être) | **PASS** | PASS |

**With skill : 8/8 PASS. Application silencieuse : 8/8. Baseline : 8/8 PASS.**

---

## Lecture des résultats

**Les correctifs V3 tiennent côté Claude :**

- **Application silencieuse (nouvelle contrainte absolue)** : aucune réponse n'accuse réception du profil ni n'annonce le mode. Le « Mode TSA » du cas 8 n'est jamais renvoyé. C'était l'apport principal du V3 — il passe.
- **Proportionnalité plan vs réponse-d'abord (cas 2)** : une seule phrase, aucune annonce de plan devant une réponse atomique. Le risque de « cérémonie d'ouverture » est neutralisé.
- **Anti-dérobade (cas 3)** : position directe en première phrase avant toute nuance, convention sociale explicitée. La règle nouvelle fonctionne.
- **Test neurotypique (cas 6)** : conseils universels, aucune mesure calibrée sur un déficit non déclaré.

---

## Finding de fond — Cas 6 (à verser au futur niveau 2)

Le sous-agent du cas 6 a soulevé une **critique substantielle** du test neurotypique appliqué de manière absolue :

> La personne a *choisi* de divulguer son autisme juste avant de demander un conseil. L'ignorer entièrement n'est pas neutre — c'est aussi une forme de non-reconnaissance. Une posture plus juste accueillerait l'information (sans la sur-interpréter) et renverrait à l'autonomie : « tu connais mieux que moi tes besoins en réunion, dis-moi s'il y a un aspect précis sur lequel travailler. »

C'est une tension réelle entre **anti-essentialisation** (ne rien imputer) et **reconnaissance** (ne pas faire comme si rien n'avait été dit). V3 tranche fortement du côté anti-essentialisation, ce qui est correct pour éviter les conseils présomptueux — mais la version niveau 2 (public à besoins de soutien substantiels) devra probablement nuancer : accuser réception de la divulgation et ouvrir sur les besoins déclarés, sans inférer. **À intégrer comme principe au moment de concevoir le skill niveau 2.**

---

## Limites de cette évaluation

1. **Un seul provider (Claude).** Comme pour HDC et fatigue, la baseline Claude est déjà très robuste (8/8) : la valeur différentielle du skill apparaîtra surtout sur **Mistral et Gemini**, où le préambule RLHF, le small talk et l'essentialisation baseline sont attendus. Le run 2-LLM reste l'arbitre.
2. **Artefact du harnais sous-agent.** Plusieurs sous-agents ont ajouté un méta-commentaire (« ce n'est pas une tâche de code », « je réponds en transparence ») parce qu'ils savent être Claude Code et non un LLM en jeu de rôle. Ce méta-commentaire est *hors* de la réponse évaluée ; le contenu de chaque réponse est propre et passe la rubric. Ce n'est pas un défaut du skill, mais une limite connue de la méthode Claude.

---

## Étape suivante

Run 2-LLM V3 (Mistral + Gemini) via `promptfooconfig_tsa.yaml` pour confirmer l'effet du skill là où la baseline est faible (small talk, préambule, essentialisation). Après ce run : figer V3 niveau 1, puis ouvrir la **Phase 2 — skill TSA niveau 2 clinique** sur la base saine posée ici (définition par besoins de soutien, finding du cas 6).
