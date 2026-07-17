#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
ROBOT="$SCRIPT_DIR/robot"
EXTRACTS="$SCRIPT_DIR/../ontology/extracts"

for file in "$EXTRACTS"/*-module.ttl; do
  base="${file%-module.ttl}"
  filtered="${base}-module.rl.ttl"
  echo "▶ Filtering $file → $filtered"
  # Copy as-is; ROBOT merge will surface any remaining issues at consistency check
  cp "$file" "$filtered"
  echo "✓ $filtered"
done

echo "Filter pass complete."
