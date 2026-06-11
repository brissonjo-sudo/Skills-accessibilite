#!/usr/bin/env bash
# build_release.sh — Génère un ZIP par skill, prêt à attacher à une GitHub Release.
#
# Chaque ZIP contient le dossier du skill à sa racine (ex. accessibilite-tsa/SKILL.md),
# de sorte que l'import via Claude (Paramètres → Capabilities → Create skill → Upload)
# reconstitue la structure attendue.
#
# Usage :
#   ./build_release.sh
#   → produit dist/<nom-du-skill>.zip pour chaque dossier de skills/
#
# Prérequis : zip

set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$ROOT"

if ! command -v zip >/dev/null 2>&1; then
  echo "Erreur : 'zip' n'est pas installé." >&2
  exit 1
fi

mkdir -p dist
rm -f dist/*.zip

echo "Validation des skills…"
python3 scripts/validate_skills.py
echo ""

count=0
cd skills
for d in */; do
  name="${d%/}"
  # Un skill valide a un SKILL.md
  if [ ! -f "$d/SKILL.md" ]; then
    echo "[SKIP] $name : pas de SKILL.md"
    continue
  fi
  zip -rq "../dist/${name}.zip" "$d"
  echo "[OK]   dist/${name}.zip"
  count=$((count + 1))
done
cd ..

echo ""
echo "$count ZIP(s) généré(s) dans dist/."
echo "Vérifier une structure : unzip -l dist/<nom>.zip  (doit afficher <nom>/SKILL.md)"
