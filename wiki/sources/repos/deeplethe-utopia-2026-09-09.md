---
title: "deeplethe/utopia (GitHub)"
type: source
source_type: repo
source_file: raw/repos/deeplethe-utopia.md
url: https://github.com/deeplethe/utopia
ingested: 2026-09-09
domains: [agents]
---

# deeplethe/utopia (GitHub)

README for Utopia, DeepLethe's open-source (Apache-2.0) bitemporal knowledge graph and ontology engine, marketed as an "enterprise world model": deployable air-gapped as one Rust binary plus Postgres, with a built-in agent harness (also exposed over MCP), ontology-driven cold-start, forward-chaining derivation, dual conflict detection, an ontology-to-SQL mapper, and an append-only decision ledger.

## Influenced pages

- [Utopia](../../tools/utopia.md) — new tool page
- [Ontologies as agent guardrails](../../concepts/ontology-agent-guardrails.md) — concrete implementation example
- [Knowledge architectures](../../concepts/knowledge-architectures.md) — ontology-row example and world-model marketing-alias note now link to the tool page
- [State of Agents](../../state-of/agents.md) — new line under Knowledge platforms

## Key claims extracted

- Bitemporal knowledge graph: every fact carries both when it was true and when the system believed it; corrections close-and-link rather than overwrite
- Deployment: one Rust binary + Postgres (Tantivy full-text, pgvector, job queue as a table); fully air-gapped behind any OpenAI-compatible endpoint
- Built-in agent harness + identical read-only MCP tools: document search, graph-as-of-any-date, mounted-database queries
- Ontology-driven cold start: 5 bundled packs (schema.org, W3C Org, PROV-O, FOAF, IOF Core)
- Forward-chaining derivation from ontology axioms (transitivity, symmetry, inverses, relation hierarchy), off by default; asserted facts always beat contradicting derived facts
- Three-stage entity resolution (exact match → embedding similarity → model judgment), every merge reversible, review queue for uncertain cases
- Dual conflict detection: fact-vs-fact and fact-vs-ontology-axiom, ontology checked first
- Ontology2SQL: maps a mounted database onto the ontology for chat queries; submitted BIRD Mini-Dev result (SQLite/PostgreSQL)
- Append-only decision ledger; outlives the object or knowledge base it belonged to
- v0.1 — schema migrations only roll forward, no rollback
- Roadmap: execution gate (checks agent calls against ontology rules), business rules compiled to derived facts, decision reasoning/replay, more connectors, agent memory over MCP, enterprise features (SSO, backup/restore)
- "Enterprise world model" is the vendor's own framing; the README also explicitly declines the "open-source Palantir" framing
