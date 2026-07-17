#!/usr/bin/env bash
# T6 / C2 — APE validation gate. Parses an .ace file (or stdin sentences) through APE
# using the generated lexicon. Exit 0 if all sentences parse; non-zero + readable message on rejection.
# Usage: validate-ace.sh <file.ace> [lexicon.ulex]
set -euo pipefail
HERE="$(cd "$(dirname "$0")" && pwd)"
source "$HERE/kg-env.sh"
# APE is an external built tool (SWI-Prolog saved state). Locate via $APE_HOME, else sibling ./APE,
# else the repo's built copy under tmp. Build: clone Attempto/APE && make install (see scripts README).
APE="${APE_HOME:-$HERE/APE}"
[ -f "$APE/ape.exe" ] || APE="$HERE/../../tmp/cnl-experiment/APE"
ACE_FILE="${1:?usage: validate-ace.sh <file.ace> [lexicon.ulex]}"
# default lexicon: generated .ulex in the ontology dir (real tree), else sibling generated file
ULEX="${2:-$KG_ULEX}"
[ -f "$ULEX" ] || ULEX="$HERE/lexicon.gen.ulex"

[ -f "$APE/ape.exe" ] || { echo "ERROR: APE not built. Set APE_HOME=<dir with ape.exe> or build per scripts README (clone Attempto/APE && make install)."; exit 2; }
[ -f "$ULEX" ] || { echo "ERROR: lexicon not found ($ULEX). Run gen-ulex.py."; exit 2; }

fail=0; n=0
# one sentence per line; ignore blank lines and # comments
while IFS= read -r line; do
  [ -z "${line// }" ] && continue
  case "$line" in \#*) continue;; esac
  n=$((n+1))
  out=$(swipl -x "$APE/ape.exe" -- -text "$line" -ulexfile "$ULEX" -solo drs 2>/dev/null || true)
  if printf '%s' "$out" | grep -q 'importance="error"'; then
    bad=$(printf '%s' "$out" | grep -oE 'value="[^"]*"' | tail -1)
    echo "REJECTED: $line"
    echo "          $bad"
    fail=$((fail+1))
  elif ! printf '%s' "$out" | grep -q '^drs('; then
    echo "NO-PARSE: $line"; fail=$((fail+1))
  fi
done < "$ACE_FILE"

if [ "$fail" -gt 0 ]; then echo "FAIL: $fail/$n sentence(s) did not parse in $ACE_FILE"; exit 1; fi
echo "OK: $n/$n sentence(s) parsed in $ACE_FILE"
