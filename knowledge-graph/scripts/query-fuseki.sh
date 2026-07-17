#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
source "$SCRIPT_DIR/kg-env.sh"
FUSEKI_URL="${FUSEKI_URL:-$KG_FUSEKI_URL}"
QUERY="${1:?usage: query-fuseki.sh '<SPARQL query>'}"

# 1. Reachability guard — fail loudly if Fuseki is down.
# 2. Freshness guard — the store is in-memory; a restart wipes it but queries keep "working"
#    against reasoner-bootstrap triples (confidently wrong answers). load-fuseki.sh stamps a
#    sentinel triple on every real load; if it is missing, refuse to answer.
#    Set KG_SKIP_FRESHNESS=1 to bypass (e.g. when inspecting an intentionally empty store).
#    (MUSCLE_SKIP_FRESHNESS is honored as a legacy alias.)
if [[ "${KG_SKIP_FRESHNESS:-${MUSCLE_SKIP_FRESHNESS:-0}}" != "1" ]]; then
  SENTINEL=$(curl -sf -G "$FUSEKI_URL/sparql" \
    --data-urlencode "query=ASK { <urn:${KG_PREFIX}:graph-build-info> ?p ?o }" \
    -H "Accept: application/sparql-results+json" \
    || { echo "✗ Fuseki unreachable at $FUSEKI_URL — is docker compose up? (knowledge-graph/docker)" >&2; exit 1; })
  if ! grep -q '"boolean" *: *true' <<<"$SENTINEL"; then
    echo "✗ Fuseki store is stale/empty (no build sentinel) — the in-memory dataset was wiped by a restart." >&2
    echo "  Re-run: knowledge-graph/scripts/rebuild.sh   (or load-fuseki.sh if a build already exists)" >&2
    exit 2
  fi
fi

curl -sf -G "$FUSEKI_URL/sparql" \
  --data-urlencode "query=$QUERY" \
  -H "Accept: application/sparql-results+json" \
|| { echo "✗ Fuseki unreachable at $FUSEKI_URL — is docker compose up? (knowledge-graph/docker)" >&2; exit 1; }
