# Personal Wiki Ontology

This directory contains local runtime state and documentation for compiling
Luis's curated AI Wiki into a Neo4j knowledge graph.

## Purpose

The ontology compiler digests `wiki/**/*.md` into graph-native knowledge:
entities, properties, relationships, actions, and workflows. It treats the
curated wiki as true knowledge and intentionally does not model claim-level
evidence, confidence, or `as_of` reasoning in v1.

The graph is meant to become a primary information source for
`use_personal_wiki`, especially for questions like:

- How are MCP, tools, and agents connected?
- What actions support safe infrastructure-agent operation?
- Which workflows depend on evals or browser verification?
- What models and tools compete in coding?

Markdown file search remains a fallback when the graph is unavailable, sparse,
or when long-form nuance is needed.

## Non-goals

- No vector database or chunk-level RAG.
- No source credibility scoring.
- No evidence-span or citation graph.
- No indexing of `wiki/history/**`, `raw/**`, `proposals/**`, or `personal/**`.
- No fixed closed ontology. New entity kinds, action kinds, workflow kinds,
  relationship types, and properties may emerge from the content.

## Neo4j setup

Run a local Neo4j instance and set:

```bash
export AGENTS_NEO4J_URI="bolt://localhost:7687"
export AGENTS_NEO4J_USER="neo4j"
export AGENTS_NEO4J_PASSWORD="..."
export AGENTS_NEO4J_DATABASE="neo4j"
```

The compiler writes only nodes and relationships with namespace
`ai-wiki-ontology`. Rebuilds clear that namespace, not the whole database.

## Extraction model

The default workflow is manual/Codex extraction. The CLI prepares JSON work
packets for dirty files, then Codex reads the packet content and fills the
structured extraction fields:

- `entities`: named things and open-ended kinds
- `relationships`: typed links between entities
- `actions`: operational or kinetic actions described by the wiki
- `workflows`: repeatable sequences or operating patterns

This avoids sending wiki content to an external model provider. The graph writer
and manifest still handle imports, cleanup, and dirty tracking.

There are two optional non-default modes:

- `--extractor llm` uses OpenRouter automation for the same JSON extraction
  shape.
- `--extractor heuristic` is only for offline smoke tests and is not intended to
  produce a useful ontology.

## Commands

```bash
agents-ontology status
agents-ontology prepare --limit 5
agents-ontology import agents/ontology/work
agents-ontology inspect wiki/concepts/mcp.md
agents-ontology query "MCP agents tools"
agents-ontology expand "MCP"
agents-ontology actions "safe infrastructure agents"
```

Default/manual flow:

1. Run `status` to see dirty, failed, and unprocessed files.
2. Run `prepare` to create work packets under
   `agents/ontology/work/`.
3. Codex fills each packet's `extracted` fields by reading the included section
   text.
4. Run `import` on one filled packet or the whole work directory.
5. The importer writes Neo4j, updates `manifest.json`, and marks files clean.

`rebuild` and `sync` are only direct extraction commands for non-manual
extractors.

## Dirty-file tracking

`manifest.json` is local runtime state and is ignored by git. Each processed
file record stores:

- path
- content hash
- last processed timestamp
- extractor prompt version
- extractor model
- graph batch ID
- status: `clean`, `failed`, or `deleted`

A file is dirty when it is new, changed, previously failed, deleted, or was
processed with an older prompt/model version.

## Reprocessing workflow

The default workflow reprocesses the whole changed file, not just the diff.
Wiki pages are compact synthesis documents, so a small edit can change the
meaning of an entire section or change relationships outside the edited lines.

For each dirty file in the manual workflow:

1. `prepare` writes a full-file work packet.
2. Codex fills all sections in the packet. It should process the whole file, not
   a line diff.
3. `import` rejects the packet if the source file changed since preparation.
4. On accepted import, previous graph relationships and batch mentions produced
   by that file are removed.
5. Canonical shared entities remain if other files still mention them.
6. New entities, relationships, actions, workflows, and discovered types are
   upserted.
7. The manifest record is marked `clean`.

For deleted files, the compiler removes that file's graph output and marks the
manifest record `deleted`.

Diff-based extraction can be added later, but full-file replacement is the
safer v1 behavior.

## Graph shape

The graph is intentionally open:

- `OntologyEntity` nodes hold `name`, `kind`, `aliases`, `summary`, and
  JSON-encoded properties.
- `OntologyAction` and `OntologyWorkflow` are labels added to relevant
  `OntologyEntity` nodes.
- `RELATES` relationships hold an open `rel_type` property such as
  `ENABLES`, `HAS_STEP`, `REQUIRES`, `COMPETES_WITH`, or newly discovered
  relationship types.
- `OntologyType` nodes register discovered entity and relationship types.
- `OntologyFile` and `OntologyBatch` nodes support sync bookkeeping.

The graph optimizes for useful knowledge traversal over strict ontology purity.
