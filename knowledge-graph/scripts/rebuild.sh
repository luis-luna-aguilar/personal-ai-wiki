#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
source "$SCRIPT_DIR/kg-env.sh"
ONTOLOGY_DIR="$KG_ONTOLOGY_DIR"
WIKI_DIR="$KG_WIKI_DIR"
BUILD_DIR="$KG_BUILD_DIR"
FUSEKI_URL="$KG_FUSEKI_URL"
# Consistency reasoner. HermiT = full OWL DL (catches disjointness, cardinality,
# functional, inverse/symmetric contradictions). Override with KG_REASONER=ELK
# for a faster, more tolerant (EL-only) pass during dev.
REASONER="${KG_REASONER:-hermit}"

echo "══════════════════════════════════════════════════════"
echo " $KG_PROJECT_NAME Knowledge Graph — Full Rebuild"
echo "══════════════════════════════════════════════════════"

rm -rf "$BUILD_DIR" && mkdir -p "$BUILD_DIR"

echo "▶ Step 1/7: Generating upstream extraction seeds from what our TTL actually uses"
python3 "$SCRIPT_DIR/gen-seeds.py"
# Regenerate the APE lexicon from lexicon-map.yaml so the deployed .ulex can never go
# stale relative to the vocabulary catalog (same treatment as the seeds — VCR-0018 round).
python3 "$SCRIPT_DIR/gen-ulex.py"

echo "▶ Step 2/7: Extracting upstream ontologies"
"$SCRIPT_DIR/extract-upstream.sh"
"$SCRIPT_DIR/filter-rl.sh"

echo "▶ Step 3/7: Merging TBox"
"$SCRIPT_DIR/merge-tbox.sh"

echo "▶ Step 4/7: Collecting ABox sidecars"
# wiki sidecars + the central country declarations (ontology/seeds/countries.ttl — instance
# data deliberately centralized out of entity sidecars by the 2026-06-19 audit; without this
# line the dbp:* countries are untyped and every bank fails BankShape) + the central
# legal-form declarations (ontology/seeds/legal-forms.ttl — same pattern, added VCR-0020,
# 2026-07-07: without this line fibo-be-le-lei:EntityLegalForm individuals are untyped) +
# the central sub-country jurisdiction declarations (ontology/seeds/administrative-areas.ttl
# — same pattern, added VCR-0020 Chunk-2 mapping, 2026-07-07: without this line dbp:Delaware
# is untyped and Delaware-jurisdiction entities fail their location shape) + the central
# activity-classification-code declarations (ontology/seeds/activity-codes.ttl — same
# pattern, added VCR-0020 Chunk-6 mapping, 2026-07-08: without this line the CAE-CR/CIIU
# skos:Concept individuals are untyped and fail ConceptShape).
# (the seed list itself now lives in kg.config.yaml → ontology.abox_seeds)
{ find "$WIKI_DIR" -name "*.ttl"; for s in "${KG_ABOX_SEEDS[@]}"; do echo "$s"; done; } > "$BUILD_DIR/abox-files.list"
abox_count=$(wc -l < "$BUILD_DIR/abox-files.list")
echo "  Found $abox_count ABox files"

echo "▶ Step 5/7: Concatenating into single graph"
GRAPH="$KG_GRAPH_FILE"
REASONED="$BUILD_DIR/graph.reasoned.ttl"
cat "$KG_MERGED_TBOX" > "$GRAPH"
while IFS= read -r f; do
  echo "" >> "$GRAPH"
  echo "# === $f ===" >> "$GRAPH"
  cat "$f" >> "$GRAPH"
done < "$BUILD_DIR/abox-files.list"

echo "▶ Step 6/7: Consistency check (reasoner: $REASONER) + materialization"
if ! "$SCRIPT_DIR/robot" reason \
  --reasoner "$REASONER" \
  --axiom-generators "SubClass ClassAssertion" \
  --include-indirect true \
  --input "$GRAPH" \
  --output "$REASONED"; then
  echo "✗ Reasoner detected a logical contradiction. Explanation:"
  "$SCRIPT_DIR/robot" explain \
    --input "$GRAPH" \
    --reasoner "$REASONER" \
    --mode inconsistency \
    --explanation "$BUILD_DIR/inconsistency-explanation.md" 2>/dev/null || true
  cat "$BUILD_DIR/inconsistency-explanation.md" 2>/dev/null || true
  exit 2
fi

# SHACL runs on the REASONED graph so inferred types (e.g. a swe:MonitoringTool
# realized as a schema:SoftwareApplication) participate in the constraints.
# This only holds with the ClassAssertion + include-indirect flags above: robot's
# default generators materialize subclass axioms only — no instance types at all,
# and without include-indirect no inherited (superclass) types.
echo "▶ Step 7/7: SHACL validation (on reasoned graph)"
"$SCRIPT_DIR/validate-shacl.sh" "$REASONED" \
  | tee "$BUILD_DIR/shacl-report.txt"
if grep -q "sh:Violation" "$BUILD_DIR/shacl-report.txt"; then
  echo "✗ SHACL violations detected — see $BUILD_DIR/shacl-report.txt"
  exit 3
fi

echo "▶ Loading into Fuseki at $FUSEKI_URL"
"$SCRIPT_DIR/load-fuseki.sh" "$GRAPH"

echo ""
echo "✓ Rebuild complete."
echo "  - $abox_count wiki pages ingested"
echo "  - SPARQL endpoint: $FUSEKI_URL/sparql"
