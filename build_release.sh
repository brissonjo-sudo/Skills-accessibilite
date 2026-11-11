#!/usr/bin/env bash
# build_release.sh — Génère un ZIP par skill, prêt à attacher à une GitHub Release.
#
# Chaque ZIP contient uniquement <nom>/SKILL.md (ex. accessibilite-tsa/SKILL.md),
# de sorte que l'import via Claude (Paramètres → Capabilities → Create skill → Upload)
# reconstitue la structure attendue.
#
# Usage :
#   ./build_release.sh
#   → produit dist/<nom-du-skill>.zip pour chaque dossier de skills/
#
# Prérequis : Python 3 et PyYAML (pip install -r requirements-ci.txt).
# Pour imposer un interpréteur : PYTHON=/chemin/vers/python ./build_release.sh

set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$ROOT"

# Sous Windows, `python3` est souvent un alias qui n'exécute rien : on retient
# le premier interpréteur qui fonctionne réellement.
PY="${PYTHON:-}"
if [ -z "$PY" ]; then
  for candidat in python3 python; do
    if "$candidat" -c "import sys" >/dev/null 2>&1; then
      PY="$candidat"
      break
    fi
  done
fi
if [ -z "$PY" ]; then
  echo "Erreur : Python 3 est introuvable." >&2
  exit 1
fi

mkdir -p dist
rm -f dist/*.zip

echo "Validation des skills…"
"$PY" scripts/validate_skills.py
echo ""

count=0
cd skills
for d in */; do
  name="${d%/}"
  # Un skill valide a un SKILL.md
  if [ ! -f "$name/SKILL.md" ]; then
    echo "[SKIP] $name : pas de SKILL.md"
    continue
  fi
  # Seul SKILL.md est archivé : aucun fichier parasite (.DS_Store, brouillon…)
  # ne peut partir dans la distribution.
  "$PY" - "../dist/${name}.zip" "$name/SKILL.md" <<'PYEOF'
import sys
import zipfile

archive, member = sys.argv[1], sys.argv[2]
with zipfile.ZipFile(archive, "w", zipfile.ZIP_DEFLATED) as bundle:
    bundle.write(member, member)
PYEOF
  echo "[OK]   dist/${name}.zip"
  count=$((count + 1))
done
cd ..

echo ""
echo "$count ZIP(s) généré(s) dans dist/."
echo "Vérifier un contenu : unzip -Z1 dist/<nom>.zip  (doit afficher <nom>/SKILL.md)"
