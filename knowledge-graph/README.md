# AI Wiki Knowledge Graph — Operator Guide

## What is this?

A reasoner-backed RDF knowledge graph that mirrors the AI Wiki. It provides:
- A queryable SPARQL endpoint for the entire AI Wiki knowledge graph
- OWL 2 RL reasoning (subclass inference, inverse properties)
- SHACL validation for completeness constraints
- A reproducible build from source wiki Markdown + Turtle sidecars

## Quick Start

### 1. Start Fuseki

```bash
cd knowledge-graph/docker
docker compose up -d
# Wait ~10 seconds, then:
curl http://localhost:3031/$/ping
```

### 2. Full Rebuild

```bash
knowledge-graph/scripts/rebuild.sh
```

This will:
1. Extract upstream ontologies (W3C ORG, PROV-O, FOAF, SKOS, schema.org, FIBO)
2. Merge into a unified TBox (`aiw + swe + biz + alignments + disjointness + extracts`)
3. Collect all `wiki/**/*.ttl` ABox sidecars
4. Run the reasoner — **HermiT** by default (full OWL DL: catches disjointness, cardinality, inverse/symmetric contradictions); aborts with a `robot explain` reason on inconsistency. Set `KG_REASONER=ELK` for a faster EL-only pass.
5. Run SHACL validation **on the reasoned graph** (inferred types participate)
6. Load into Fuseki (which itself applies an OWLMicro reasoner at query time)

> **Reasoning & contradiction model:** see `governance/validation-architecture.md` for the three layers (query-time / build-time / ingestion-time) and reasoner choices.

### 3. Query the Graph

```bash
# Count all triples
curl -G http://localhost:3031/aiwiki/sparql \
  --data-urlencode "query=SELECT (COUNT(*) AS ?n) WHERE { ?s ?p ?o }" \
  -H "Accept: application/json"

# List all foundation models
curl -G http://localhost:3031/aiwiki/sparql \
  --data-urlencode "query=SELECT ?model ?label WHERE { ?model a <https://ai-wiki.luisluna.dev/ontology/#FoundationModel> ; <http://www.w3.org/2000/01/rdf-schema#label> ?label }" \
  -H "Accept: application/json"

# Find all tools and their license model
curl -G http://localhost:3031/aiwiki/sparql \
  --data-urlencode "query=SELECT ?tool ?label ?license WHERE { ?tool a <https://schema.org/SoftwareApplication> ; <http://www.w3.org/2000/01/rdf-schema#label> ?label ; <https://ai-wiki.luisluna.dev/ontology/#hasLicenseModel> ?license }" \
  -H "Accept: application/json"
```

SPARQL web UI: http://localhost:3031

### 4. Validate Before Ingesting (contradiction gate)

```bash
# Check candidate sidecar(s) against the WHOLE current graph:
# HermiT consistency + reasoned SHACL. Flags contradictions with existing data.
knowledge-graph/scripts/validate-ingestion.sh wiki/tools/new-tool.ttl
# exit 0 = clean · 2 = logical contradiction (prints explanation) · 3 = SHACL violation
```

Quick single-file check (TBox + one page only, no cross-record contradiction detection):

```bash
knowledge-graph/scripts/validate-page.sh wiki/models/claude-opus.ttl
```

### 5. Stop Fuseki

```bash
cd knowledge-graph/docker && docker compose down
```

## Directory Layout

```
knowledge-graph/
├── governance/                 # Wiki⇄ontology process & vocabulary rules
│   ├── master-plan.md          #   the symbiotic model
│   ├── process-architecture.md #   two-track workflow + handshake + gates
│   ├── vocabulary-policy.md     #   term-admission rules
│   ├── validation-architecture.md #  reasoning & contradiction detection (3 layers)
│   └── change-requests/        #   VCR audit trail (one file per addition)
├── ontology/
│   ├── aiw.ttl                  # AI Wiki-native TBox: FoundationModel, Benchmark, BenchmarkResult, LicenseModel (VCR-0003)
│   ├── swe.ttl                  # Software-engineering vocabulary (inherited verbatim, VCR-0001)
│   ├── biz.ttl                  # Business vocabulary (inherited verbatim, VCR-0001)
│   ├── alignments.ttl           # Cross-ontology bridges, inherited verbatim (VCR-0001)
│   ├── disjointness.ttl         # Disjointness axioms, inherited verbatim (VCR-0001)
│   ├── aiw-shapes.ttl           # SHACL shapes (generic core inherited + native Benchmark/LicenseModel shapes, VCR-0003)
│   ├── aiw-tbox.merged.ttl      # Build artifact (not committed)
│   ├── `lexicon-map.yaml`       # Vocabulary catalog (concept → IRI)
│   ├── gap-report.md            # Unsupported concepts discovered during bootstrap
│   ├── seeds/                   # Seed IRI lists for ROBOT MIREOT extraction + schema-concepts.ttl (VCR-0002)
│   └── extracts/                # Extracted upstream modules (committed: *.rl.ttl)
├── scripts/
│   ├── rebuild.sh              # Full rebuild pipeline (HermiT + reasoned SHACL + load)
│   ├── extract-upstream.sh     # ROBOT MIREOT extractions
│   ├── filter-rl.sh            # RL profile filtering
│   ├── merge-tbox.sh           # Merge aiw/swe/biz/alignments/disjointness + extracts
│   ├── load-fuseki.sh          # POST graph to Fuseki
│   ├── validate-shacl.sh       # SHACL validation via Apache Jena
│   ├── validate-ingestion.sh   # Contradiction gate: candidate vs whole graph (HermiT+SHACL)
│   ├── validate-page.sh        # Quick single-page check (TBox + one page)
│   ├── gen-schema-concepts.py  # Compiles wiki/_schema/*.md → seeds/schema-concepts.ttl (VCR-0002)
│   ├── reason-check.sh         # Standalone reasoner check
│   └── robot                   # ROBOT wrapper script
├── docker/
│   ├── docker-compose.yml      # Fuseki service (mounts the reasoner config below)
│   └── config-aiwiki.ttl       # Assembler config: OWLMicro inference dataset (mounted)
└── tools/
    ├── robot.jar               # ROBOT CLI (not committed)
    └── apache-jena-4.10.0/     # Apache Jena CLI tools (not committed)
```

## Adding a New Wiki Page

1. Write the Markdown page under `wiki/`.
2. Create a sibling `.ttl` sidecar following the pattern in `knowledge-graph/ontology/lexicon-map.yaml`.
3. Run `knowledge-graph/scripts/validate-page.sh wiki/path/to/page.ttl`.
4. If validation passes, commit both files together.
5. Run `knowledge-graph/scripts/rebuild.sh` to refresh Fuseki.

## Key IRIs

- AI Wiki instance/data + native-term namespace: `https://ai-wiki.luisluna.dev/ontology/#` (prefix `aiw:`)
- Software-engineering vocabulary (inherited verbatim, VCR-0001): `https://musclepoints.com/ontology/swe#` (prefix `swe:`)
- Business vocabulary (inherited verbatim, VCR-0001): `https://musclepoints.com/ontology/biz#` (prefix `biz:`)
- Fuseki dataset: `http://localhost:3031/aiwiki`
- SPARQL endpoint: `http://localhost:3031/aiwiki/sparql`

## Notes

- IRIs are forever. Never rename `aiw:claude-code`. Add `owl:sameAs` or `skos:altLabel` if the wiki file is renamed.
- `aiw-tbox.merged.ttl` is a build artifact and is not committed to git.
- Run `rebuild.sh` after any wiki change to keep Fuseki in sync.
