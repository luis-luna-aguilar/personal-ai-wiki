---
type: proposal
source: raw/articles/2026-04-21-tco-ubgb5izpnb.md
status: pending
created: 2026-04-21
---

# Proposal: Knowledge layer

## Summary

This article is unusually relevant to the vault itself. It argues that agents need a compiled knowledge layer plus a human-maintained rules / brand layer, rather than naive retrieval over raw files. The structure described is extremely close to this repository's architecture, making it worth capturing explicitly as a concept page instead of leaving it implicit.

## Intended changes

- [x] **Create** `wiki/concepts/knowledge-layer.md` — new concept page
  > See draft below.

- [x] **Update** `wiki/index.md` — add the concept page and refresh counts

- [x] **Create** `wiki/sources/articles/knowledge-layer-architecture.md` — source summary
  > See draft below.

## Page drafts

### wiki/concepts/knowledge-layer.md (new)

```md
---
title: Knowledge layer
type: concept
domains: [agents]
tags: [agentic]
as_of: 2026-04-21
sources: [knowledge-layer-architecture]
---

# Knowledge layer

A knowledge layer is a compiled, maintained context surface that sits between raw source material and the agents acting on it. Instead of forcing an agent to re-derive context from raw files at query time, the system continuously turns sources into structured wiki pages, indexes, entity pages, and syntheses that the agent can read directly.

## Current status (as of 2026-04-21)

- Framed as an answer to why agents often feel generic: they start from thin or unstructured context
- Contrasted with naive RAG: compile once, cross-reference, and maintain over time rather than repeatedly searching raw chunks
- Often paired with a separate human-maintained rules layer (voice, preferences, constraints, operating rules)
- Becomes more useful as outputs, queries, and new sources compound back into the same system

## Why it matters

The core claim is not just retrieval quality. A maintained knowledge layer changes the agent's starting point: from "guess from whatever I can find right now" to "act from a curated, versioned memory of this domain." This makes agent behavior more cumulative, more inspectable, and easier to improve over time.

## Caveats

- The strongest current source is a practitioner / creator essay, not an academic benchmark or vendor-neutral comparison
- The idea overlaps with context engineering, RAG, memory systems, and personal-knowledge-base workflows; boundaries are still fuzzy

## Sources

- [[sources/articles/knowledge-layer-architecture]]
```

### wiki/sources/articles/knowledge-layer-architecture.md (new)

```md
---
title: AI Knowledge Layer
type: source
source_type: article
source_file: raw/articles/2026-04-21-tco-ubgb5izpnb.md
url: https://t.co/ubgb5izPnB
ingested: 2026-04-21
domains: [agents]
---

# AI Knowledge Layer

Practitioner essay arguing that agents become materially more useful when they read from a compiled knowledge layer rather than raw-file retrieval. The source describes a two-layer system: a dynamic agent-maintained knowledge base plus a human-maintained foundation layer for rules, voice, and constraints.

## Key claims extracted

- Raw sources should be continuously compiled into structured wiki pages and indexes
- A separate static layer should preserve human-owned rules and identity constraints
- Compiled context is presented as more effective than naive query-time retrieval once source volume grows
- The architecture is positioned as useful for personal, team, and company-scale agent systems
```
