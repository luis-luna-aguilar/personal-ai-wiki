#!/usr/bin/env bash
# validate-sync.sh — ACE→TTL drift guard (STRICT gate).
#
# For each wiki page with both a .ace and a .ttl sidecar, recompile the .ace via
# drs2ttl.py into a temp file and compare the result graph-isomorphically with the
# committed .ttl. Reports DRIFT / IN-SYNC / COMPILE-FAIL per page.
#
# STRICT by default (since 2026-07-06: the ACE→TTL migration is complete — 20/20 pages
# in-sync): any drift, compile failure, or missing .ttl is a failing gate (exit 1).
# Set ADVISORY=1 to only report (the pre-migration behavior), e.g. while iterating locally.
#
# Two sanctioned, permanent hand-authored exemptions (content with no ACE form to
# recompile from) are stripped from both graphs before comparison, so neither is ever
# reported as drift — only genuine ACE/TTL divergence is:
#   1. Blank-node facts — reified structured values ACE's flat grammar can't express
#      (schema:MonetaryAmount, schema:PropertyValue, schema:PostalAddress, etc. — see
#      AGENTS.md §2). drs2ttl_v3.py's own merge_from_canon skips any triple touching a
#      blank node for the same reason (no stable identity to de-dupe across recompiles).
#   2. xsd:gYearMonth / xsd:gYear literals — a source gives only year-month or year
#      granularity for a property whose confirmed lexicon datatype is day-precision
#      xsd:date, and the coarser datatype has no ACE form under that mapping (see
#      lexicon-map.yaml's own comment on the `date-created` row).
# See sync-model.md "Edge: hand-authored blank-node enrichment" for the full rationale.
#
# Usage: validate-sync.sh [page.ace ...]        (no args = every wiki .ace)
#        ADVISORY=1 validate-sync.sh            (report only, always exit 0)
set -uo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
source "$SCRIPT_DIR/kg-env.sh"
REPO_ROOT="$KG_REPO_ROOT"
WORK="$(mktemp -d -t validate-sync-XXXXXX)"
trap 'rm -rf "$WORK"' EXIT

if [ "$#" -gt 0 ]; then FILES=("$@"); else
  FILES=(); while IFS= read -r f; do FILES+=("$f"); done < <(find "$KG_WIKI_DIR" -name "*.ace" | sort)
fi

in_sync=0; drift=0; nottl=0; cfail=0
for ace in "${FILES[@]}"; do
  ttl="${ace%.ace}.ttl"
  rel="${ace#"$REPO_ROOT"/}"
  if [ ! -f "$ttl" ]; then echo "NO-TTL      $rel"; nottl=$((nottl+1)); continue; fi
  out="$WORK/$(basename "${ace%.ace}").recompiled.ttl"
  if ! python3 "$SCRIPT_DIR/drs2ttl.py" "$ace" "$out" >/dev/null 2>&1; then
    echo "COMPILE-FAIL $rel"; cfail=$((cfail+1)); continue
  fi
  if python3 - "$ttl" "$out" << 'EOF' >/dev/null 2>&1
import sys
from rdflib import Graph, BNode, Literal
from rdflib.namespace import XSD
from rdflib.compare import to_isomorphic

COARSE_DATE_TYPES = {XSD.gYearMonth, XSD.gYear}

def strip_exempt_triples(g):
    out = Graph()
    for prefix, ns in g.namespaces():
        out.bind(prefix, ns)
    for s, p, o in g:
        if isinstance(s, BNode) or isinstance(o, BNode):
            continue
        if isinstance(o, Literal) and o.datatype in COARSE_DATE_TYPES:
            continue
        out.add((s, p, o))
    return out

a = Graph(); a.parse(sys.argv[1], format='turtle')
b = Graph(); b.parse(sys.argv[2], format='turtle')
sys.exit(0 if to_isomorphic(strip_exempt_triples(a)) == to_isomorphic(strip_exempt_triples(b)) else 1)
EOF
  then echo "IN-SYNC     $rel"; in_sync=$((in_sync+1))
  else
    # quantify the drift for the report (same exemptions as the gate check)
    python3 - "$ttl" "$out" << 'EOF'
import sys
from rdflib import Graph, BNode, Literal
from rdflib.namespace import XSD
from rdflib.compare import to_isomorphic, graph_diff

COARSE_DATE_TYPES = {XSD.gYearMonth, XSD.gYear}

def strip_exempt_triples(g):
    out = Graph()
    for prefix, ns in g.namespaces():
        out.bind(prefix, ns)
    for s, p, o in g:
        if isinstance(s, BNode) or isinstance(o, BNode):
            continue
        if isinstance(o, Literal) and o.datatype in COARSE_DATE_TYPES:
            continue
        out.add((s, p, o))
    return out

a = Graph(); a.parse(sys.argv[1], format='turtle')
b = Graph(); b.parse(sys.argv[2], format='turtle')
_, only_committed, only_recompiled = graph_diff(to_isomorphic(strip_exempt_triples(a)), to_isomorphic(strip_exempt_triples(b)))
print(f"DRIFT       {sys.argv[1].split('wiki/')[-1] if 'wiki/' in sys.argv[1] else sys.argv[1]} — committed-only: {len(only_committed)} triple(s), recompiled-only: {len(only_recompiled)} triple(s)")
EOF
    drift=$((drift+1))
  fi
done

echo "────────────────────────────────────────────────"
mode="strict"; [ "${ADVISORY:-0}" = "1" ] && mode="advisory"
echo "sync report: $in_sync in-sync · $drift drift · $cfail compile-fail · $nottl missing .ttl ($mode mode)"
if [ "$mode" = "strict" ] && [ $((drift+cfail+nottl)) -gt 0 ]; then
  echo "✗ ACE→TTL sync gate FAILED — regenerate the .ttl from the .ace (drs2ttl.py), never hand-edit." >&2
  exit 1
fi
exit 0
