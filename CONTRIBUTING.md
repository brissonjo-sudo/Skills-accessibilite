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

**Harnais d'évaluation**
- Fichier `eval/promptfooconfig_<nom>.yaml` dédié
- Minimum 6 cas de test (dont cas de non-déclenchement)
- 2 providers validés avec score ≥ 6/8 (assertions passantes)

---

## 2. Convention de versionnement

- Un fichier `SKILL.md` par skill — pas de suffixe de version dans le nom du fichier
- `V → V+1` = nouvelle règle, correction empirique, ou reformulation validée par le harnais
- Chaque montée de version doit s'accompagner d'un run du harnais (`run_all.sh`)
- Le `CHANGELOG.md` documente ce qui a changé entre chaque version (règles ajoutées, supprimées, reformulées)

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
- Les résultats JSON bruts (`results*.json`) ne sont pas commités (trop lourds)
- Les analyses Markdown (`eval/analyse_*.md`) sont la source de vérité archivée
- Pour générer les ZIPs de release : `bash build_release.sh`

---

## 5. Lancer les évaluations

**Prérequis**
- Node.js LTS
- `npm install -g promptfoo`
- Fichier `eval/.env` renseigné (voir `eval/.env.example`)

**Commande**

```bash
cd eval/
./run_all.sh                      # tous les skills
./run_all.sh tdah                 # un skill spécifique
./run_all.sh tdah dys tsa         # plusieurs skills
```

Les résultats apparaissent dans le terminal. Les analyses sont conservées dans `eval/analyse_*.md`.
