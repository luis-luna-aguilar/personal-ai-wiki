#!/usr/bin/env bash
# kg-env.sh — loads kg.config.yaml into KG_* environment variables.
#
# Source this from any pipeline script that needs project identity (prefix,
# namespaces, artifact paths, Fuseki coordinates). The single implementation
# lives in kgconfig.py (--env); this shim just evals its output, so bash and
# Python can never disagree about the config.
#
# Override the config file location with $KG_CONFIG (used by package-layer.sh
# smoke tests and by any caller working against a different deployment).

_KG_HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
if ! _kg_env_exports="$(python3 "$_KG_HERE/kgconfig.py" --env)"; then
  echo "✗ kg-env.sh: failed to load kg.config.yaml (see kgconfig.py)" >&2
  return 1 2>/dev/null || exit 1
fi
eval "$_kg_env_exports"
unset _kg_env_exports _KG_HERE
