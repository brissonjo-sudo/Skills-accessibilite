# Contribuer au dépôt Skills Accessibilité & Psychologie

## 1. Soumettre un skill

### Critères minimum d'acceptation

**Fichier**
- Nommé `SKILL.md`, placé dans `skills/<nom-du-skill>/`
- Frontmatter YAML avec :
  - `name` : ≤ 64 caractères, uniquement `a-z0-9-`
  - `description` : ≤ 1024 caractères, résume le comportement et le déclencheur

**Déclencheur documenté**
- Le skill doit documenter explicitement les formulations qui l'activent
- Et les formulations qui ne l'activent pas (exemples de non-déclenchement)
- Un déclencheur trop large ou trop ambigu est un motif de refus

**Application silencieuse**
- Le skill ne s'annonce jamais lui-même (pas de « Je vais appliquer le skill X »)
- Il modifie le comportement sans métacommentaire

**Section auto-vérification**
- Minimum 8 points de contrôle que le modèle peut vérifier sur sa propre réponse
- Formulation actionnable (ex. : « Vérifie que chaque règle est appliquée »)

**Banque de cas**
- Fichier `eval/promptfooconfig_<nom>.yaml` dédié
- Minimum 6 cas de test (dont cas de non-déclenchement)
- Chaque cas porte au moins une assertion sémantique (`llm-rubric`) ; les assertions
  déterministes (`javascript`) s'ajoutent quand le critère est mécaniquement vérifiable
- Aucune question de test ne doit être recopiée du `SKILL.md` évalué (vérifié en CI
  par `scripts/check_eval_leaks.py`)

---

## 2. Convention de versionnement

- Un fichier `SKILL.md` par skill — pas de suffixe de version dans le nom du fichier
- `V → V+1` = nouvelle règle, correction empirique, ou reformulation validée par une vague
- **Chaque montée de version doit s'appuyer sur une vague de validation** (voir §5) :
  une comparaison avec/sans skill, en aveugle, sur les cas de la banque
- Le `CHANGELOG.md` documente ce qui a changé entre chaque version (règles ajoutées,
  supprimées, reformulées) et **cite le run qui l'appuie**

---

## 3. Convention de commit

| Préfixe | Usage |
|---|---|
| `feat(skill-name):` | Nouveau skill ou règle majeure |
| `eval(skill-name):` | Run ou analyse du harnais |
| `fix(axe-C):` | Correction dette documentaire ou bugs |
| `ci:` | Infrastructure CI/CD |
| `docs:` | README, CONTRIBUTING, bilan |

Exemple : `feat(accessibilite-tsa): ajout règle littéralité des négations`

---

## 4. Hygiène secrets

- Ne **jamais** committer `eval/.env` (clés API réelles)
- Seul `eval/.env.example` est tracké dans le dépôt
- Les nouveaux résultats JSON bruts (`results*.json`) ne sont pas commités (trop lourds) ; les archives historiques déjà suivies sont conservées pour la reproductibilité
- Les analyses Markdown (`eval/analyse_*.md`) sont la source de vérité archivée
- Pour générer les ZIPs de release : `bash build_release.sh`

---

## 5. Valider un skill — vague de validation

L'évaluation ne passe plus par un lanceur automatisé. Elle se fait **en vagues** : une
session d'agents (Claude Code ou ChatGPT) exécute le protocole de bout en bout.

**Protocole de référence** : `eval/prompt_benchmark_claude_code.md`. Le coller dans une
session ouverte à la racine du dépôt.

**Ce qu'une vague produit**, dans `eval/runs/<AAAAMMJJ-HHMMSS>/` (répertoire ignoré par Git) :

- `manifest.json` — commit, modèles, empreintes SHA-256 des skills testés, graines
- `raw_generations.jsonl` — une ligne par cellule, réponse intégrale conservée
- `judge_outputs/` — verdicts des juges, en aveugle
- `metrics.json` et `report.md` — agrégats et rapport

**Ce qui fait qu'une vague est recevable** :

1. **Deux conditions appariées** — chaque cas joué avec et sans le skill, sur la même
   question, dans des contextes isolés. Un agent ne juge jamais sa propre réponse.
2. **Aveuglement** — les réponses sont présentées aux juges en A/B, sans indiquer laquelle
   porte le skill. La correspondance n'est révélée qu'à l'agrégation.
3. **Trois juges indépendants** par variante, dont un chargé de chercher les régressions.
4. **Cas exclus signalés** — question recopiée du skill, cellule perdue sur erreur
   d'infrastructure, cas de non-déclenchement (inévaluable quand le skill est injecté
   de force).
5. **Fond et forme rapportés séparément.** Une régression de sécurité, d'exactitude, de
   non-diagnostic ou d'essentialisation interdit une conclusion positive, quels que
   soient les gains de forme.

**Limite à ne pas masquer** : injecter le texte intégral d'un skill mesure l'effet
d'instructions dans une session. Cela ne teste pas le mécanisme automatique de
déclenchement d'une skill sur les autres surfaces.

Les analyses et décisions sont consignées dans `eval/analyse_*.md`, source de vérité
archivée. Le `report.md` d'un run vit dans `eval/runs/` : le recopier hors de ce
répertoire s'il doit être partagé.
