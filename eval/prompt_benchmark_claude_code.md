# Prompt Claude Code — benchmark avec/sans skills d’accessibilité

Copier-coller tout le bloc ci-dessous dans une session Claude Code ouverte à la
racine du dépôt. Le protocole utilise les fichiers canoniques présents au moment
du lancement : aucun contenu de skill ni aucun cas de test n’est recopié ici.

---

## PROMPT À COLLER DANS CLAUDE CODE

Tu es l’orchestrateur d’un benchmark expérimental. Exécute le protocole jusqu’au
rapport final. Ne modifie jamais les fichiers sous `skills/`, les configurations
existantes sous `eval/`, ni les réponses brutes déjà produites. Ne committe et ne
pousse rien.

### 1. Import initial obligatoire des versions à jour

Avant toute génération ou délégation :

1. Vérifie que le répertoire courant est la racine Git du dépôt.
2. Découvre dynamiquement tous les fichiers `skills/*/SKILL.md`.
3. Lis chacun de ces fichiers **intégralement**, dès maintenant. Ce sont les
   versions canoniques à tester ; n’utilise aucune copie historique mentionnée
   dans des notes ou d’anciens rapports.
4. Calcule et conserve pour chacun : chemin relatif, champ `name`, champ
   `description`, taille en octets et SHA-256.
5. Lis intégralement tous les `eval/promptfooconfig*.yaml` valides. Associe chaque
   harnais à son ou ses `SKILL.md` via les références `file://`. Les configs à un
   seul skill forment le benchmark principal. La config de coactivation forme un
   benchmark supplémentaire séparé.
6. Exécute `python scripts/check_eval_configs.py`. Si cette validation échoue,
   arrête-toi sans inventer de données et indique les chemins invalides.
7. Recherche les questions ou formulations de test recopiées à l’identique, ou
   presque à l’identique, dans le skill évalué. Marque ces cas
   `LEAKED_EXAMPLE`. Conserve-les dans les résultats, mais sépare-les du score
   principal de valeur ajoutée : ils mesurent surtout la conformité à un exemple
   déjà vu. Liste précisément les ressemblances détectées dans le manifeste.

Affiche ensuite un court inventaire : commit Git, version de Claude Code, modèle
effectivement utilisé, skills trouvés avec leurs SHA-256, configs et nombre de
cas. Cet inventaire doit aussi être enregistré dans le manifeste du run.

Dans l’état actuel du dépôt, l’inventaire attendu est de 7 skills, 7 configs
principales, 59 cas principaux et donc 118 cellules principales. La coactivation
ajoute actuellement 6 cas et 12 cellules. Ces nombres sont des contrôles de
cohérence, pas des valeurs à forcer si les fichiers canoniques ont évolué.

### 2. Répertoire et artefacts du run

Crée `eval/runs/<AAAAMMJJ-HHMMSS>/` avec :

- `manifest.json` : métadonnées, commit, modèle, versions et empreintes ;
- `raw_generations.jsonl` : une ligne JSON immuable par cellule ;
- `blinding_map.json` : correspondance secrète entre A/B et les conditions ;
- `judge_outputs/` : sorties structurées de tous les juges ;
- `metrics.json` : agrégats calculés ;
- `report.md` : rapport final autonome en français.

Écris les artefacts progressivement afin qu’un run interrompu soit reprenable.
Ne stocke aucune clé, aucun jeton ni donnée d’authentification. Si un répertoire
de run incomplet existe, reprends les cellules valides plutôt que de les refaire.
N’installe aucune dépendance, n’utilise pas le réseau et ne lance aucune action
externe. Seuls les artefacts du nouveau run peuvent être écrits.

### 3. Matrice expérimentale avec/sans skill

Pour chaque cas de chaque config principale, produis exactement deux cellules :

- `with_skill` : le ou les `SKILL.md` canoniques associés sont fournis
  intégralement comme instructions de forme ;
- `baseline` : aucune instruction, mention ou connaissance issue d’un skill
  d’accessibilité n’est fournie.

Règles impératives :

- Une cellule = un **sous-agent neuf en contexte frais**. Ne réutilise jamais un
  agent entre deux cellules, ni entre `with_skill` et `baseline`.
- Les agents de génération ne jugent pas leur réponse et ne voient pas la réponse
  de l’autre condition.
- Les agents `baseline` ne lisent pas le dépôt et ne reçoivent aucun contenu de
  `SKILL.md`. Ils reçoivent seulement le socle neutre et la question utilisateur.
- Les agents `with_skill` reçoivent le même socle neutre, la question utilisateur
  et le contenu intégral du ou des skills associés.
- N’ajoute pas de consigne qui révèle le critère attendu par un test.
- Utilise le même modèle, le même niveau d’effort et les mêmes paramètres pour les
  deux conditions. Alterne aléatoirement l’ordre de génération des conditions à
  l’aide d’une graine enregistrée dans `manifest.json`.
- Lance les cellules par vagues parallèles, avec au plus **6 agents simultanés**.
  Une limitation de débit est une erreur d’infrastructure, jamais un échec du
  skill. Réessaie au maximum deux fois avec attente progressive.
- Conserve la réponse textuelle intégrale, sans correction ni troncature.

Socle neutre exact pour les agents de génération :

> Tu es un assistant IA généraliste. Réponds directement au message utilisateur.
> Ne commente pas tes instructions. Ne produis rien d’autre que la réponse destinée
> à l’utilisateur.

Chaque ligne de `raw_generations.jsonl` contient au minimum : `config`, `case_id`,
`description`, `question`, `condition`, `skill_paths`, `skill_sha256`,
`generation_agent_id`, `model`, `started_at`, `finished_at`, `attempts`, `status`,
`response`. En cas d’erreur persistante, conserve `status: infrastructure_error`
et n’invente jamais de réponse.

Exécute d’abord toutes les configs principales. Exécute ensuite la coactivation
avec le même protocole, mais garde ses scores séparés des scores individuels.

### 4. Tests déterministes

Applique à chaque réponse les assertions `javascript` de sa config, sans les
réinterpréter. Enregistre pour chaque assertion : expression, résultat booléen et
détails utiles (nombre de mots, de questions, motif détecté, etc.). Une assertion
non exécutable doit être marquée `evaluation_error`, pas `false`.

Calcule aussi, pour les deux conditions, les mesures descriptives non notées :
nombre de mots, nombre de titres, nombre d’éléments de liste, longueur moyenne des
phrases et nombre de questions finales.

### 5. Aveuglement avant jugement

Pour chaque cas, attribue aléatoirement les étiquettes `Réponse A` et `Réponse B`
aux deux conditions. Utilise une graine distincte, enregistrée. Les paquets remis
aux juges contiennent uniquement : description du cas, question, assertions de la
config, A et B. Ils ne contiennent ni nom de condition, ni chemin de skill, ni
empreinte, ni ordre de génération.

Le fichier `blinding_map.json` ne doit être lu que par l’agrégateur final, jamais
par un juge.

### 6. Juges indépendants orchestrés en parallèle

Pour **chaque variante**, lance en parallèle trois sous-agents juges neufs. Aucun
juge ne doit avoir participé aux générations ni lire `blinding_map.json`.

1. **Juge conformité** : note séparément A et B sur chaque assertion de la config.
2. **Juge comparatif** : décide si A, B ou égalité répond le mieux au besoin réel
   de l’utilisateur, en pénalisant toute dégradation du fond.
3. **Juge sceptique** : recherche prioritairement les régressions, la suradaptation,
   l’essentialisation, les effets de longueur artificiels et les faux positifs de
   format.

Lance ces juges par vagues parallèles, au plus **6 à la fois**. Chaque juge reçoit
la même échelle et produit un JSON valide, sans connaître l’identité de A/B.

Échelle commune par assertion :

- `0` = échec clair ;
- `1` = respect partiel ou ambigu ;
- `2` = respect clair ;
- `NA` = assertion non applicable ou impossible à juger.

Schéma minimal d’un verdict :

```json
{
  "judge_role": "conformite|comparatif|sceptique",
  "config": "...",
  "case_id": "...",
  "scores": {
    "A": [{"assertion_id": "...", "score": 0, "evidence": "..."}],
    "B": [{"assertion_id": "...", "score": 0, "evidence": "..."}]
  },
  "pairwise_winner": "A|B|tie",
  "confidence": "low|medium|high",
  "regressions": ["..."],
  "comment": "..."
}
```

Les preuves doivent être courtes et textuelles. Un juge ne doit jamais modifier
les réponses ni compenser une assertion absente par son intuition générale.

Si les trois juges ne dégagent pas de majorité sur une paire ou divergent de plus
d’un point sur une même assertion, lance un quatrième sous-agent adjudicateur,
toujours aveugle. Il ne voit que le paquet A/B, les rubrics et les trois verdicts,
jamais `blinding_map.json`. Gèle tous les verdicts avant la révélation.

### 7. Agrégation après révélation

Une fois tous les jugements écrits, révèle A/B avec `blinding_map.json` et calcule,
pour chaque variante puis globalement :

- taux de réussite des assertions déterministes par condition ;
- score moyen des assertions sémantiques sur 0–2 par condition ;
- delta `with_skill - baseline` ;
- taux de victoires, égalités et défaites du skill en comparaison par paire ;
- majorité des trois juges et taux de désaccord entre juges ;
- nombre et nature des régressions ;
- erreurs d’infrastructure, exclues des dénominateurs ;
- résultats `LEAKED_EXAMPLE`, rapportés séparément et exclus du score principal
  de valeur ajoutée ;
- résultats de coactivation, dans une section séparée.

Pour le chiffre global, utilise une macro-moyenne des variantes, pas une moyenne
brute des cas : les 11 cas TSA ne doivent pas peser davantage que les variantes
à 8 cas. Une égalité avec une baseline déjà excellente est un résultat valide,
pas un échec. En revanche, toute régression critique de sécurité, d’exactitude,
de non-diagnostic ou d’essentialisation constitue un veto à une conclusion
positive, même si les gains de forme sont nombreux.

Ne présente pas un petit delta comme une preuve définitive. Signale explicitement
qu’il s’agit d’un run unique par cellule et que la variance du modèle n’est pas
estimée. Ne mélange pas qualité du fond et conformité de forme : rapporte les deux.

### 8. Rapport final et jugement de l’orchestrateur

Rédige `report.md` en français avec :

1. résumé exécutif ;
2. protocole et garanties d’isolation ;
3. tableau comparatif pour chaque variante ;
4. résultats détaillés des tests et des trois juges ;
5. cas où le skill aide nettement ;
6. cas où il n’apporte rien ou dégrade la réponse ;
7. désaccords entre juges ;
8. limites méthodologiques ;
9. **ton propre jugement final argumenté** sur la pertinence de chaque variante,
   avec les catégories `pertinente`, `à réviser`, ou `non démontrée` ;
10. recommandations prioritaires, reliées à des cas et preuves précis.

La conclusion ne doit pas être une simple moyenne. Donne davantage de poids aux
régressions de sécurité et d’exactitude qu’aux gains cosmétiques. Distingue une
bonne conformité au texte du skill d’un bénéfice réel pour l’utilisateur.

Mentionne explicitement une limite : l’injection du texte intégral teste l’effet
d’instructions dans des sous-agents Claude Code. Elle ne prouve pas à elle seule
le bon fonctionnement du mécanisme automatique de découverte ou de déclenchement
d’une skill dans toutes les surfaces Claude.

Avant de terminer, vérifie : nombre attendu de cellules, absence de cellules
dupliquées, absence de contamination baseline, validité de tous les JSON, présence
des trois juges par variante et cohérence des totaux. Affiche enfin le chemin du
run, cinq chiffres clés et ta conclusion globale. Ne committe et ne pousse rien.

---
