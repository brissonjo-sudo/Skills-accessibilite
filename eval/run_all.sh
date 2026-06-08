#!/usr/bin/env bash
# run_all.sh — Lance tous les harnais promptfoo de l'écosystème
#
# Usage :
#   cd eval/
#   ./run_all.sh                  # lance tous les harnais
#   ./run_all.sh dys tdah         # lance uniquement les harnais indiqués
#
# Chaque run produit un fichier results_<skill>.json dans le répertoire eval/.
# Les résultats filtrés (erreurs 503 exclues) sont résumés dans STDOUT.
#
# Prérequis : promptfoo installé globalement (npm install -g promptfoo)
#             Variables d'environnement : MISTRAL_API_KEY, GOOGLE_API_KEY

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

# Chargement du .env si présent
if [ -f ".env" ]; then
  set -o allexport
  source .env
  set +o allexport
fi

# Couleurs
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m'

# Mapping skill → fichier config
declare -A CONFIGS=(
  ["hdc"]="promptfooconfig.yaml"
  ["fatigue"]="promptfooconfig_fatigue.yaml"
  ["tsa"]="promptfooconfig_tsa.yaml"
  ["visuel"]="promptfooconfig_visuel.yaml"
  ["dys"]="promptfooconfig_dys.yaml"
  ["tdah"]="promptfooconfig_tdah.yaml"
  ["psychologie"]="promptfooconfig_psychologie.yaml"
)

# Sélection des harnais à lancer
if [ $# -gt 0 ]; then
  TARGETS=("$@")
else
  TARGETS=("hdc" "fatigue" "tsa" "visuel" "dys" "tdah" "psychologie")
fi

PASS_TOTAL=0
FAIL_TOTAL=0
ERROR_TOTAL=0
SKIPPED_CONFIGS=()

for TARGET in "${TARGETS[@]}"; do
  CONFIG="${CONFIGS[$TARGET]:-}"
  if [ -z "$CONFIG" ]; then
    echo -e "${YELLOW}[SKIP]${NC} Harnais inconnu : $TARGET"
    continue
  fi
  if [ ! -f "$CONFIG" ]; then
    echo -e "${YELLOW}[SKIP]${NC} Fichier absent : $CONFIG"
    SKIPPED_CONFIGS+=("$TARGET")
    continue
  fi

  RESULTS_FILE="results_${TARGET}.json"
  echo ""
  echo -e "${YELLOW}━━━ Lancement : $TARGET ($CONFIG) ━━━${NC}"

  if promptfoo eval --config "$CONFIG" --output "$RESULTS_FILE" 2>&1; then
    echo -e "${GREEN}[OK]${NC} Run terminé → $RESULTS_FILE"
  else
    echo -e "${RED}[ERR]${NC} Run échoué pour $TARGET (voir messages ci-dessus)"
    continue
  fi

  # Lecture du résumé depuis results JSON
  if command -v node &>/dev/null && [ -f "$RESULTS_FILE" ]; then
    node -e "
const fs = require('fs');
const data = JSON.parse(fs.readFileSync('$RESULTS_FILE', 'utf8'));
const results = data.results || {};
let pass = 0, fail = 0, err = 0;
for (const r of (results.results || [])) {
  for (const s of (r.testCase?.assert || [])) { /* noop */ }
  const score = r.score;
  const fr = r.failureReason;
  if (fr === 2) { err++; continue; }  // Erreur API (503 etc.) — exclue du score
  if (r.success) pass++; else fail++;
}
console.log('  PASS:', pass, '  FAIL:', fail, '  ERREUR-API (exclus):', err);
process.exit(fail > 0 ? 1 : 0);
" 2>/dev/null && {
      PASS_TOTAL=$((PASS_TOTAL + 1))
    } || {
      FAIL_TOTAL=$((FAIL_TOTAL + 1))
    }
  fi
done

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo -e "Résumé : ${#TARGETS[@]} harnais ciblés"
if [ ${#SKIPPED_CONFIGS[@]} -gt 0 ]; then
  echo -e "${YELLOW}Skippés${NC} : ${SKIPPED_CONFIGS[*]}"
fi
echo -e "${GREEN}Sans échec${NC} : $PASS_TOTAL   ${RED}Avec échec${NC} : $FAIL_TOTAL"
echo ""
echo "Lancez 'promptfoo view' dans ce répertoire pour l'interface web."
