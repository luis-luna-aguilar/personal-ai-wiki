#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
source "$SCRIPT_DIR/kg-env.sh"
GRAPH_FILE="${1:-$KG_GRAPH_FILE}"

echo "▶ Running ELK reasoner on $GRAPH_FILE"
# robot rejects --output /dev/null ("unknown format") — it needs a real .ttl path.
OUT_FILE="$(mktemp -t reason-check-XXXXXX).ttl"
trap 'rm -f "$OUT_FILE"' EXIT
"$SCRIPT_DIR/robot" reason \
  --reasoner ELK \
  --input "$GRAPH_FILE" \
  --output "$OUT_FILE"

echo "✓ No inconsistencies detected."
