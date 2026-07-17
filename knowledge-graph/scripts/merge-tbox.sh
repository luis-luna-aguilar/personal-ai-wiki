#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
source "$SCRIPT_DIR/kg-env.sh"
ROBOT="$SCRIPT_DIR/robot"
ONTOLOGY_DIR="$KG_ONTOLOGY_DIR"
EXTRACTS="$ONTOLOGY_DIR/extracts"
OUTPUT="$KG_MERGED_TBOX"

# Module list comes from kg.config.yaml → ontology.tbox_modules (order preserved).
INPUTS=()
for m in "${KG_TBOX_MODULES[@]}"; do
  INPUTS+=("--input" "$ONTOLOGY_DIR/$m")
done
for f in "$EXTRACTS"/*-module.rl.ttl; do
  INPUTS+=("--input" "$f")
done

echo "▶ Merging TBox from ${#INPUTS[@]} sources"
"$ROBOT" merge "${INPUTS[@]}" --output "$OUTPUT"

echo "✓ Merged TBox written to $OUTPUT"
