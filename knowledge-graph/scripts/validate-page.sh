#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
source "$SCRIPT_DIR/kg-env.sh"

PAGE_TTL="$1"
TEMP="/tmp/page-validate-$$.ttl"
# robot rejects --output /dev/null ("unknown format") — it needs a real .ttl path.
REASONED="/tmp/page-validate-$$-reasoned.ttl"

cat "$KG_MERGED_TBOX" "$PAGE_TTL" > "$TEMP"

"$SCRIPT_DIR/robot" reason --reasoner ELK --input "$TEMP" --output "$REASONED"
"$SCRIPT_DIR/validate-shacl.sh" "$TEMP"

rm -f "$TEMP" "$REASONED"
echo "✓ $PAGE_TTL is valid"
