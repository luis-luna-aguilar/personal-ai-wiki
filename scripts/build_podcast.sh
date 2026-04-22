#!/usr/bin/env bash
# Concatenate wiki pages into podcast-ready markdown files.
# One file per block, with a framing intro prepended for the podcast tool.
#
# Usage: scripts/build_podcast.sh <1|2|3|all>

set -euo pipefail

WIKI_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$WIKI_ROOT"

OUT_DIR="$WIKI_ROOT/podcast/out"
mkdir -p "$OUT_DIR"

build_one() {
  local n="$1"
  local slug
  local -a dirs

  case "$n" in
    1)
      slug="block-1-state-of-play"
      dirs=("wiki/state-of" "wiki/models" "wiki/benchmarks")
      ;;
    2)
      slug="block-2-tools-workflows"
      dirs=("wiki/tools" "wiki/workflows")
      ;;
    3)
      slug="block-3-concepts-trends-training"
      dirs=("wiki/concepts" "wiki/trends" "wiki/training")
      ;;
    *)
      echo "unknown block: $n" >&2
      exit 1
      ;;
  esac

  local intro="podcast/${slug}.md"
  local out="$OUT_DIR/${slug}.md"

  if [[ ! -f "$intro" ]]; then
    echo "missing intro file: $intro" >&2
    exit 1
  fi

  {
    cat "$intro"
    for d in "${dirs[@]}"; do
      [[ -d "$d" ]] || continue
      for f in "$d"/*.md; do
        [[ -e "$f" ]] || continue
        printf '\n\n---\n\n## Source: `%s`\n\n' "${f#"$WIKI_ROOT/"}"
        cat "$f"
      done
    done
  } > "$out"

  echo "wrote $out ($(wc -w < "$out" | tr -d ' ') words)"
}

case "${1:-}" in
  1|2|3)
    build_one "$1"
    ;;
  all)
    for n in 1 2 3; do
      build_one "$n"
    done
    ;;
  *)
    echo "Usage: $0 <1|2|3|all>"
    exit 1
    ;;
esac
