#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
source "$SCRIPT_DIR/kg-env.sh"
# Jena 4.x needs Java 11+; java-env.sh exports JAVA, which Jena's bin scripts honor.
source "$SCRIPT_DIR/java-env.sh"
JENA_VERSION="4.10.0"
# Jena's own bin/ launcher scripts break (misparse their classpath/log4j-config
# argument) if JENA_HOME contains a space — a real failure hit deploying this
# layer under "~/Obsidian/AI Wiki". Installing to a shared, space-free cache
# dir side-steps that permanently AND lets every deployment of this layer on
# one machine reuse a single download instead of vendoring it per repo.
# Override with $KG_JENA_HOME if a specific install is required.
JENA_HOME="${KG_JENA_HOME:-$HOME/.cache/kg-layer/apache-jena-$JENA_VERSION}"

if [ ! -d "$JENA_HOME" ]; then
  echo "▶ Downloading Apache Jena $JENA_VERSION to $JENA_HOME"
  mkdir -p "$(dirname "$JENA_HOME")"
  curl -L -o "/tmp/jena.tar.gz" \
    "https://archive.apache.org/dist/jena/binaries/apache-jena-$JENA_VERSION.tar.gz"
  tar -xzf "/tmp/jena.tar.gz" -C "$(dirname "$JENA_HOME")/"
fi

DATA_FILE="${1:-$KG_GRAPH_FILE}"
SHAPES_FILE="$KG_SHAPES_FILE"

# Jena's own file-URI resolution does strict RFC 3987 IRI validation and
# rejects a raw space in the path (IRIException: WHITESPACE in PATH) — hit
# deploying this layer under "~/Obsidian/AI Wiki". Stage both inputs into a
# space-free temp dir before invoking Jena, regardless of where the repo
# (and therefore these files) actually live.
STAGE="$(mktemp -d -t validate-shacl-XXXXXX)"
trap 'rm -rf "$STAGE"' EXIT
cp "$DATA_FILE" "$STAGE/data.ttl"
cp "$SHAPES_FILE" "$STAGE/shapes.ttl"

"$JENA_HOME/bin/shacl" validate \
  --data "$STAGE/data.ttl" \
  --shapes "$STAGE/shapes.ttl"
