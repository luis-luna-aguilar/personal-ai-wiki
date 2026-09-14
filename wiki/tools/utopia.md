---
title: Utopia
type: tool
domains: [agents]
subcategory: knowledge-platform
tags: [open-source, knowledge-cluster]
as_of: 2026-09-09
sources: [deeplethe-utopia-2026-09-09]
---

# Utopia

Utopia is an open-source (Apache-2.0) bitemporal knowledge graph and ontology engine built by DeepLethe, which markets it as an "enterprise world model". In the wiki's vocabulary that phrase is a marketing alias: the product occupies the ontology row of the [Knowledge architectures](../concepts/knowledge-architectures.md) matrix (domain-scope classes, relations, and axioms used as machine-checked rules), not the physical or video-prediction sense the wiki reserves for "world model". Companies can deploy it air-gapped on their own hardware. Every extracted fact carries both when it was true in the world and when the system came to believe it — correcting a fact closes the old version and links the new one rather than overwriting, so a decision reviewed later can reproduce the exact grounds it rested on. The project explicitly positions itself as a different route to enterprise intelligence than Palantir-style systems: built bottom-up from knowledge governance toward trustworthy decisions, not top-down from an existing data platform.

## Also called

Enterprise world model (DeepLethe's marketing term), bitemporal knowledge graph, ontology engine.

## Current status (as of 2026-09-09)
- Ships as one Rust binary plus Postgres (Tantivy full-text search embedded, pgvector for vectors, job queue is a table) — runs fully air-gapped behind any OpenAI-compatible endpoint
- Ingests PDF/DOCX/PPTX/XLSX/CSV/Markdown/HTML/plain text, plus scheduled sync from web pages, RSS, GitHub, Jira, Notion, WebDAV, and S3-compatible buckets
- Built-in agent harness (and the same read-only tools over MCP) can search documents, walk the graph as of any date, and query a mounted database
- Ontology axioms (transitivity, symmetry, inverses, relation hierarchy) compile into forward-chaining derivation rules, off by default; a derived fact never overrides an asserted one it contradicts
- Three-stage entity resolution (exact match → embedding similarity → model judgment), every merge reversible, uncertain cases go to a review queue
- **Ontology2SQL** maps a mounted database's tables onto the ontology so chat can query structured data alongside documents; reported state-of-the-art on BIRD Mini-Dev (SQLite/PostgreSQL)
- Append-only decision ledger records every confirm/reject/merge/revert/rebuild, outliving the object or knowledge base it belonged to
- Still v0.1 — schema migrations only roll forward, no rollback; version pinning and backups recommended before upgrading

## Strengths
- Bitemporal design plus an append-only decision ledger gives a genuine audit trail for "why did the system believe this at the time," not just current-state search
- Fully air-gapped deployment (one binary, one Postgres, any OpenAI-compatible endpoint) suits regulated or on-prem-only environments
- Conflict detection treats ontology violations and fact clashes as separate, explicit decision points rather than silently overwriting data

## Weaknesses / caveats
- Early-stage (v0.1); no rollback path on schema migrations
- Source is the project's own README — no independent benchmark or production case study beyond the cited BIRD Mini-Dev submission for Ontology2SQL specifically

## Recent changes
- [2026-09-09] Page created from the project's GitHub README (no dated release event in the source).

## Related
- [Knowledge architectures](../concepts/knowledge-architectures.md) — the hub that places this product on the ontology row and pins "enterprise world model" as a marketing alias
- [Ontologies as agent guardrails](../concepts/ontology-agent-guardrails.md) — the formal-ontology-as-guardrail concept this tool implements concretely, including a working "execution gate" roadmap item that checks agent calls against ontology rules
- [Company brain](../concepts/company-brain.md) — Zep/Graphiti's "knowledge graph with a clock" in the company-brain survey is the same bitemporal idea at a different scope

## Sources
- [deeplethe/utopia (GitHub)](../sources/repos/deeplethe-utopia-2026-09-09.md)
