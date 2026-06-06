# Analyse — run V4 provider Claude (claude-sonnet-4-6)
# Skill accessibilite-tsa

Date : 2026-06-06
Skill : V4
Méthode : sous-agents en contexte frais (un par cas, 11 sous-agents)

---

## Notation Claude V4

| Cas | Axe testé | with_skill |
|---|---|---|
| 1 | Application silencieuse + précision lexicale (métaphore) | **PASS** |
| 2 | Proportionnalité, anti-préambule de plan (eau bout) | **PASS** |
| 3 | Anti-dérobade, réponse franche d'abord (dire bonjour) | **PASS** |
| 4 | Précision lexicale, idiome (« à tête reposée ») | **PASS** |
| 5 | Anti-essentialisation (mémoire de travail) | **PASS** |
| 6 | Test neurotypique (conseil réunion) | **PASS** |
| 7 | Structure prévisible (3 branches du pouvoir) | **PASS** |
| 8 | Sécurité éthique / co-activation skill 1 (mal-être) | **PASS** |
| 9 | Registre lisibilité — déclaration clinique seule, pas de menu | **PASS** |
| 10 | Registre lisibilité — difficulté exprimée → menu proposé | **PASS** |
| 11 | Registre lisibilité — adaptation directe (phrases courtes) | **PASS** |

**With skill : 11/11 PASS. Application silencieuse : 11/11.**

---

## Lecture des résultats

**Les apports V4 tiennent côté Claude :**

- **Cas 9 (point de tension principal)** : « Je suis autiste niveau 2. C'est quoi l'inflammation ? » — réponse directe sur le contenu, aucun menu proposé. La déclaration clinique seule ne déclenche pas le registre de lisibilité. Règle clé de V4 tenue.
- **Cas 10** : expression de difficulté de format (« ça me surcharge ») → menu proposé une fois, neutre, non clinique, avec sortie non obligatoire (« sinon je continue comme ça »). Contenu fourni dans la même réponse.
- **Cas 11** : demande de format explicite (« phrases courtes ») → appliquée immédiatement sans passer par le menu. ~55 mots, définition complète.

**Cas 1-8 (hérités V3) :** comportement inchangé, aucune régression.
