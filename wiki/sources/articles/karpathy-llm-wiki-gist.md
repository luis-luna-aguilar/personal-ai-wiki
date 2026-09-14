---
title: "LLM Wiki (gist)"
type: source
source_type: article
source_file: raw/articles/2026-09-09-gistgithubcom-karpathy-442a6bf555914893e9891c11519de94f.md
url: https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f
published: 2026-04-04
ingested: 2026-09-09
domains: [agents]
---

# LLM Wiki (gist)

Andrej Karpathy's original "idea file" describing the LLM Wiki pattern: an LLM-maintained personal knowledge base compiled from raw sources, structured as three layers (raw sources, wiki, schema) with three operations (ingest, query, lint). Meant to be pasted directly to an LLM agent as a starting brief for instantiating the pattern in any domain. No publish-date byline is visible on the fetched gist page itself; 2026-04-04 is corroborated by multiple independent references within the raw content (including a secondary article quoting Karpathy's own dated follow-up tweet), not a direct byline.

## Influenced pages

- [Knowledge layer](../../concepts/knowledge-layer.md) — primary-source treatment of the LLM Wiki pattern, previously only cited via a secondary example

## Key claims extracted

- Three-layer architecture: raw sources (immutable), the wiki (LLM-owned markdown), the schema (CLAUDE.md/AGENTS.md-style, co-evolved with the user)
- Three operations: Ingest (a source can touch 10-15 pages), Query (answers should be filed back into the wiki as new pages), Lint (contradictions, staleness, orphan pages, missing cross-references)
- index.md is content-oriented (catalog, read first, works to ~100 sources without embeddings); log.md is chronological/append-only and grep-able with a consistent line prefix
- Recommends `qmd` (local hybrid BM25/vector markdown search, CLI + MCP server) once scale outgrows the index file
- Framed as a realized Vannevar Bush Memex (1945): the maintenance problem Bush never solved is handled by the LLM
- Explicitly abstract/idea-only — meant to be co-instantiated by the user and their LLM agent for their own domain
- Gist has 5,000+ stars/forks and a large comment thread of independent implementations and variants
