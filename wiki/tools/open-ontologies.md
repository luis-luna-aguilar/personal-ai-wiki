---
title: Open Ontologies
type: tool
domains: [agents]
subcategory: knowledge-platform
tags: [open-source, knowledge-cluster]
as_of: 2026-10-28
sources: [fabio-rovai-open-ontologies-2026-10-28]
---

# Open Ontologies

Open Ontologies is an open-source (MIT) engine, written in Rust and shipped as one binary, for changing a production ontology safely. It borrows Terraform's loop (plan, apply, watch for drift, roll back), but the plan is semantic: it reports what a change makes the ontology *entail*, not which lines moved. Its second job is proof: each reasoning run writes a certificate that a separate, formally verified Lean 4 checker re-checks without the engine. In the [Knowledge architectures](../concepts/knowledge-architectures.md) matrix it sits on the ontology row. Fabio Rovai maintains it; Tesseract Semantics sells a hosted version.

## Current status (as of 2026-10-28)
- Plan reports added and removed classes, blast radius, risk score, locked IRIs, and whether a change adds consequences over existing names. The README's example: one added `rdfs:domain` line, zero triples affected, 901 new inferences
- A certificate is two tab-separated files (assertions; each derived step with rule and premises). The Lean checker shares no code with the engine, refuses a forged conclusion with exit 1 and names the rule, and gives a different verdict when the rules were user-supplied
- Also: OWL/RDFS reasoning, SHACL validation, satisfiability with checked finite models, crosswalk checks that downgrade unsupported `exactMatch` mappings, and per-claim checks that a RAG retrieval slice still supports its answer
- Runs as an MCP server for Claude Code, Claude Desktop and Cursor; loads CSV, JSON, XML, XLSX, Parquet, PostgreSQL and DuckDB into RDF

## Weaknesses / caveats
- Not an ontology editor; the README points to Protégé for authoring
- Unsatisfiability answers carry no guarantee, and the tool says so
- Storage is in-memory by default, so a `load` then `reason` without persistent mode certifies nothing; the warning is easy to miss
- The pure-Python second engine runs the same algorithm as the Rust one, so their agreement is weak evidence against a shared misreading of a rule; the Lean checker is the independent leg
- Published binaries omit eight feature-gated tools (embeddings, plugins, SQL backends)

## Recent changes
- [2026-10-28] Page created from the project's GitHub README (no dated release in the source).

## Related
- [Ontologies as agent guardrails](../concepts/ontology-agent-guardrails.md) — the concept this tool serves, applied to change control of the ontology itself
- [Utopia](utopia.md) — the other ontology-row engine tracked; Utopia governs facts extracted from documents, Open Ontologies governs changes to the rules
- [Knowledge architectures](../concepts/knowledge-architectures.md) — the hub that places this tool on the ontology row

## Sources
- [fabio-rovai/open-ontologies (GitHub)](../sources/repos/fabio-rovai-open-ontologies-2026-10-28.md)
