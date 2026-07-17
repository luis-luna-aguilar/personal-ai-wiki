#!/usr/bin/env bash
# package-layer.sh — emits a portable bundle of the knowledge-graph layer
# (pipeline scripts, docker setup, governance docs, generic authoring guides,
# sub-agent specs, templates) into a target directory, mirroring this repo's
# layout so the bundle can be copied onto a new wiki repo root.
#
# What is NOT packaged: wiki content, raw sources, VCR history, the
# domain-specific vocabulary modules (muscle.ttl, travel.ttl), domain
# authoring guides, and generated artifacts. See the emitted
# KG-LAYER-MANIFEST.md for the per-file adaptation checklist.
#
# Code is config-driven (kg.config.yaml); prose (governance docs, guides,
# agent specs) is deployment-specific and gets a one-time rewrite at deploy —
# the manifest lists every file needing it.
#
# Usage: package-layer.sh <target-dir>
set -euo pipefail

HERE="$(cd "$(dirname "$0")" && pwd)"
KG_ROOT="$(cd "$HERE/.." && pwd)"
REPO_ROOT="$(cd "$KG_ROOT/.." && pwd)"
TARGET="${1:?usage: package-layer.sh <target-dir>}"
mkdir -p "$TARGET"
TARGET="$(cd "$TARGET" && pwd)"

copy() { # copy <src-rel-to-repo> <dst-rel-to-target>
  local src="$REPO_ROOT/$1" dst="$TARGET/$2"
  mkdir -p "$(dirname "$dst")"
  cp "$src" "$dst"
}

# ---- pipeline scripts (config-driven; port as-is) --------------------------
SCRIPTS=(
  kg-env.sh kgconfig.py java-env.sh robot
  gen-ulex.py gen-seeds.py
  drs2ttl.py drs2ttl_v3.py drs2shacl.py drs2shacl_prod.py drs2swrl.py
  validate-ace.sh validate-page.sh validate-shacl.sh validate-ingestion.sh
  validate-sync.sh reason-check.sh coherence-check.py
  extract-upstream.sh filter-rl.sh merge-tbox.sh
  rebuild.sh load-fuseki.sh query-fuseki.sh
  find-undocumented-patterns.py reconcile-vocab.py
  package-layer.sh
)
for f in "${SCRIPTS[@]}"; do copy "knowledge-graph/scripts/$f" "knowledge-graph/scripts/$f"; done

# ---- docker (config-driven; assembler config + .env are generated at deploy) --
copy knowledge-graph/docker/docker-compose.yml knowledge-graph/docker/docker-compose.yml
copy knowledge-graph/docker/gen-config.sh      knowledge-graph/docker/gen-config.sh

# ---- governance (prose: adapt at deploy) -----------------------------------
GOV=(master-plan.md process-architecture.md vocabulary-policy.md sync-model.md validation-architecture.md)
for f in "${GOV[@]}"; do copy "knowledge-graph/governance/$f" "knowledge-graph/governance/$f"; done
mkdir -p "$TARGET/knowledge-graph/governance/change-requests"   # VCR numbering restarts at 0001

# ---- ontology starters (curate at deploy: prune to the new domain) ---------
ONTO=(swe.ttl biz.ttl alignments.ttl disjointness.ttl muscle-shapes.ttl lexicon-map.yaml)
for f in "${ONTO[@]}"; do copy "knowledge-graph/ontology/$f" "knowledge-graph/ontology/$f"; done
copy knowledge-graph/ontology/seeds/countries.ttl knowledge-graph/ontology/seeds/countries.ttl
copy knowledge-graph/README.md knowledge-graph/README.md
: > "$TARGET/knowledge-graph/ontology/gap-report.md"
printf '# Gap report — concepts/facts the TBox cannot express yet (append-only)\n' \
  > "$TARGET/knowledge-graph/ontology/gap-report.md"

# ---- config skeleton (REQUIRED edit at deploy) ------------------------------
cat > "$TARGET/knowledge-graph/kg.config.yaml" <<'EOF'
# kg.config.yaml — project identity for the knowledge-graph layer.
# EDIT EVERY VALUE before first use. IRIs and the prefix are PERMANENT once
# instance sidecars exist. See KG-LAYER-MANIFEST.md for the deploy checklist.
project:
  name: CHANGEME
  prefix: changeme
namespaces:
  data: "https://example.org/ontology/#"
  modules:
    biz: "https://example.org/ontology/biz#"
    swe: "https://example.org/ontology/swe#"
paths:
  wiki_root: wiki
ontology:
  tbox_modules: [swe.ttl, biz.ttl, alignments.ttl, disjointness.ttl]
  shapes_file: shapes.ttl
  lexicon_ulex: lexicon.ulex
  merged_tbox: tbox.merged.ttl
  abox_seeds: [seeds/countries.ttl]
compiler:
  named_aliases: {}
  fallback_class_prefix: biz
build:
  dir: /tmp/changeme-kg-build
fuseki:
  port: 3031
  dataset: changeme
  admin_password: changeme-dev-admin
  container_name: changeme-fuseki
  compose_project: changeme-kg
EOF

# ---- generic authoring guides (prose: adapt examples at deploy) -------------
GUIDES=(README.md controlled-english.md term-minting.md skos-concept.md entity.md
        enum-member-concept.md record-page.md numbered-process-steps.md org-role.md
        software-application.md large-source-ingestion.md)
for f in "${GUIDES[@]}"; do copy "system/authoring-guides/$f" "system/authoring-guides/$f"; done

# ---- prompts / templates / helper scripts -----------------------------------
copy system/prompts/auditor_agent.md      system/prompts/auditor_agent.md
copy system/templates/proposal_template.md system/templates/proposal_template.md
copy system/templates/entity.md            system/templates/entity.md
copy system/scripts/verify_links.py        system/scripts/verify_links.py

# ---- sub-agent specs + slash command (prose: adapt at deploy) ----------------
AGENTS=(ace-extractor.md query-orchestrator.md wiki-answerer.md kg-verifier.md)
for f in "${AGENTS[@]}"; do copy ".claude/agents/$f" ".claude/agents/$f"; done
copy .claude/commands/query.md .claude/commands/query.md

# ---- gitignore snippet -------------------------------------------------------
cat > "$TARGET/kg-layer.gitignore.snippet" <<'EOF'
# Knowledge Graph build artifacts (merge into the repo .gitignore; align the
# merged-tbox/ulex names with kg.config.yaml → ontology.*)
knowledge-graph/tools/robot.jar
knowledge-graph/tools/apache-jena-*/
knowledge-graph/ontology/tbox.merged.ttl
knowledge-graph/ontology/extracts/*-module.ttl
knowledge-graph/scripts/__pycache__/
knowledge-graph/scripts/lexicon.gen.ulex
knowledge-graph/docker/.env
tmp/
EOF

# ---- lineage + manifest ------------------------------------------------------
COMMIT="$(git -C "$REPO_ROOT" rev-parse HEAD 2>/dev/null || echo unknown)"
cat > "$TARGET/LINEAGE.md" <<EOF
# Layer lineage
Extracted from: $REPO_ROOT
Source commit:  $COMMIT
Packaged:       $(date -u +%Y-%m-%dT%H:%M:%SZ)
To diff against upstream fixes later: re-run package-layer.sh in the source
repo at its current commit and diff the two bundles.
EOF

cat > "$TARGET/KG-LAYER-MANIFEST.md" <<'EOF'
# KG-layer bundle — deploy checklist

## 1. Code (config-driven — do NOT edit, just configure)
- `knowledge-graph/scripts/*` — read `kg.config.yaml` via kgconfig.py / kg-env.sh.
- `knowledge-graph/docker/{docker-compose.yml,gen-config.sh}` — run gen-config.sh
  after editing kg.config.yaml, before `docker compose up -d`.

## 2. REQUIRED config edit
- `knowledge-graph/kg.config.yaml` — every CHANGEME value. Prefix/IRIs are
  permanent once the first sidecar is committed.

## 3. Prose needing one-time adaptation to the new wiki (grep for the source
##    project's name after editing — the deploy gate is a clean grep)
- `knowledge-graph/governance/*.md` (5 files)
- `knowledge-graph/README.md`
- `system/authoring-guides/*.md` (examples reference source-domain entities)
- `system/prompts/auditor_agent.md`, `system/templates/*.md`
- `.claude/agents/*.md`, `.claude/commands/query.md` (paths, prefix, example queries)

## 4. Vocabulary curation at deploy (VCR-0001 of the new repo)
- `knowledge-graph/ontology/{swe.ttl,biz.ttl,disjointness.ttl,alignments.ttl,muscle-shapes.ttl}`
  — inherit via a VCR; prune source-domain terms/shapes; rename shapes file per config.
- `knowledge-graph/ontology/lexicon-map.yaml` — triage: keep generic rows, drop
  source-domain entity rows; regen the ulex (gen-ulex.py).
- `knowledge-graph/governance/change-requests/` — empty; numbering restarts at 0001.

## 5. Operating manual
- The new wiki keeps its own AGENTS.md; graft a "Knowledge graph sidecars"
  section (sidecar convention, MD→ACE→TTL, IRI rule, VCR gate, validation gates).

## 6. Bookkeeping
- Merge `kg-layer.gitignore.snippet` into the repo `.gitignore`.
- Start a fresh INVENTORY-style index and system/log entry per the new repo's conventions.
EOF

echo "✓ layer packaged to $TARGET"
echo "  $(find "$TARGET" -type f | wc -l | tr -d ' ') files — see KG-LAYER-MANIFEST.md for the deploy checklist"
