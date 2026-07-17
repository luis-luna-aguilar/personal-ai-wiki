#!/usr/bin/env bash
# validate-ingestion.sh — the ingestion-time Rules & Contradiction gate.
#
# Validates the WHOLE prospective graph: merged TBox + every current wiki
# ABox sidecar + any extra candidate .ttl files passed as arguments. This
# catches contradictions BETWEEN the incoming facts and the existing graph,
# not just within a single page (which is all validate-page.sh checks).
#
# Steps: merge TBox (offline, no re-extract) → reason (HermiT) → on
# inconsistency, emit a human-readable explanation → SHACL on the reasoned
# graph. Non-zero exit = a contradiction or constraint violation to resolve.
#
# Usage:
#   scripts/validate-ingestion.sh [candidate1.ttl candidate2.ttl ...]
#   KG_REASONER=ELK scripts/validate-ingestion.sh   # faster, EL-only fallback
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
source "$SCRIPT_DIR/kg-env.sh"
WIKI_DIR="$KG_WIKI_DIR"
ROBOT="$SCRIPT_DIR/robot"
REASONER="${KG_REASONER:-hermit}"
BUILD="/tmp/${KG_PREFIX}-kg-ingestion-$$"
mkdir -p "$BUILD"
trap 'rm -rf "$BUILD"' EXIT

echo "▶ Merging TBox (offline — uses committed extracts)"
bash "$SCRIPT_DIR/merge-tbox.sh" >/dev/null

echo "▶ Assembling prospective graph (TBox + current ABox + ${#@} candidate file(s))"
cp "$KG_MERGED_TBOX" "$BUILD/graph.ttl"
# wiki sidecars + central seed declarations (kg.config.yaml → ontology.abox_seeds;
# see rebuild.sh for each seed's rationale) + candidates
{ find "$WIKI_DIR" -name "*.ttl"; for s in "${KG_ABOX_SEEDS[@]}"; do echo "$s"; done; printf '%s\n' "$@"; } | sort -u | while IFS= read -r f; do
  [ -n "$f" ] && [ -f "$f" ] || continue
  printf '\n# === %s ===\n' "$f" >> "$BUILD/graph.ttl"
  cat "$f" >> "$BUILD/graph.ttl"
done

echo "▶ Consistency / contradiction check (reasoner: $REASONER)"
if ! "$ROBOT" reason --reasoner "$REASONER" \
     --axiom-generators "SubClass ClassAssertion" --include-indirect true \
     --input "$BUILD/graph.ttl" --output "$BUILD/reasoned.ttl" 2>"$BUILD/reason.log"; then
  echo "✗ CONTRADICTION: the incoming facts are logically inconsistent with the graph."
  "$ROBOT" explain --input "$BUILD/graph.ttl" --reasoner "$REASONER" \
     --mode inconsistency --explanation "$BUILD/explanation.md" >/dev/null 2>&1 || true
  echo "----- explanation -----"
  cat "$BUILD/explanation.md" 2>/dev/null || tail -5 "$BUILD/reason.log"
  echo "-----------------------"
  echo "Paste the above into the proposal's 'Rules & Contradiction Check' section and resolve before approval."
  exit 2
fi

echo "▶ SHACL validation (on reasoned graph)"
"$SCRIPT_DIR/validate-shacl.sh" "$BUILD/reasoned.ttl" > "$BUILD/shacl.txt" 2>&1
if grep -q "sh:Violation" "$BUILD/shacl.txt"; then
  echo "✗ SHACL violations — incoming facts break a constraint:"
  grep -E "sh:focusNode|sh:resultMessage|sh:resultPath" "$BUILD/shacl.txt"
  exit 3
fi

echo "✓ Ingestion is consistent and conforms — no contradictions or constraint violations."
