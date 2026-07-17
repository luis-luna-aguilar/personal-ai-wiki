#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
source "$SCRIPT_DIR/kg-env.sh"
FUSEKI_URL="${FUSEKI_URL:-$KG_FUSEKI_URL}"
FUSEKI_USER="${FUSEKI_USER:-admin}"
FUSEKI_PASS="${FUSEKI_PASS:-$KG_FUSEKI_PASS}"
GRAPH_FILE="${1:-$KG_GRAPH_FILE}"

echo "▶ Loading $GRAPH_FILE into Fuseki at $FUSEKI_URL"

# Clear existing default graph first
curl -s -u "$FUSEKI_USER:$FUSEKI_PASS" -X POST \
  -H "Content-Type: application/sparql-update" \
  --data "CLEAR DEFAULT" \
  "$FUSEKI_URL/update" || true

# Load the new graph
curl -s -u "$FUSEKI_USER:$FUSEKI_PASS" -X POST \
  -H "Content-Type: text/turtle" \
  --data-binary "@$GRAPH_FILE" \
  "$FUSEKI_URL/data?default"

# Freshness sentinel: the store is in-memory (assembler config: ja:MemoryModel), so any
# container restart silently wipes it back to reasoner-bootstrap triples. This triple marks
# "a real load happened"; query-fuseki.sh refuses to answer if it is absent.
# urn: IRI on purpose — build metadata, never part of the project vocabulary or data.
LOADED_AT="$(date -u +%Y-%m-%dT%H:%M:%SZ)"
curl -s -u "$FUSEKI_USER:$FUSEKI_PASS" -X POST \
  -H "Content-Type: application/sparql-update" \
  --data "INSERT DATA { <urn:${KG_PREFIX}:graph-build-info> <http://purl.org/dc/terms/modified> \"$LOADED_AT\"^^<http://www.w3.org/2001/XMLSchema#dateTime> ; <http://purl.org/dc/terms/source> \"$GRAPH_FILE\" }" \
  "$FUSEKI_URL/update"

echo "✓ Graph loaded (sentinel stamped $LOADED_AT)."
