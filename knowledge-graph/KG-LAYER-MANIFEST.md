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
