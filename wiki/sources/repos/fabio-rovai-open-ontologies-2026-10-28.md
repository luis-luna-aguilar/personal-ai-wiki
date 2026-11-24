---
title: "fabio-rovai/open-ontologies (GitHub)"
type: source
source_type: repo
source_file: raw/repos/fabio-rovai-open-ontologies.md
url: https://github.com/fabio-rovai/open-ontologies
ingested: 2026-10-28
domains: [agents]
---

# fabio-rovai/open-ontologies (GitHub)

README for Open Ontologies, an MIT-licensed Rust engine (one binary, MCP server) for planning, applying and rolling back changes to a production ontology. It reports a semantic blast radius rather than a text diff, and writes derivation certificates that a separate Lean 4 checker with a soundness theorem re-verifies offline, refusing forged conclusions. Maintained by Fabio Rovai; a hosted version is sold by Tesseract Semantics. The README carries no release date; the ingest date is used.

## Influenced pages

- [Open Ontologies](../../tools/open-ontologies.md) — new tool page
- [Ontologies as agent guardrails](../../concepts/ontology-agent-guardrails.md) — change control for the ontology itself as a new status bullet
- [State of Agents](../../state-of/agents.md) — new line under Knowledge platforms
- [Knowledge architectures](../../concepts/knowledge-architectures.md) — Open Ontologies added to the ontology row's tracked examples

## Key claims extracted

- Terraform-style loop for ontologies: plan, apply, monitor, drift, certify, rollback; plan reports added/removed classes, blast radius, risk score, locked IRIs, conservativity
- Example: adding `ex:hasParent rdfs:domain ex:Person` affects 0 triples and changes no classes, yet adds 901 consequences under the OWL RL rule table (0.04s)
- Certificates are two TSV files (asserted, derivations); a core Lean 4 checker (`oo-cert`, theorem `OOCert.certificate_sound`) shares no code with the engine and exits 1 on a forged line, naming the rule
- User-supplied rules (SWRL, RIF Core, Horn table) yield the verdict `entailed_under_supplied_rules` instead of `entailed`
- Figure on ies-core.ttl: 426 asserted, 259 certified by one certificate, 1 forged line rejected
- HQDM audit: the RDFS file has 23 undeclared class terms and 12 ranges naming a relation; the OWL file has 39 unsatisfiable classes, the same 39 HermiT reports
- No guarantee on unsatisfiability answers, stated by the tool
- Also: SHACL validation, finite-model satisfiability, SSSOM crosswalk certification and `crosswalk-probe`, entailment preservation for RAG retrieval slices, locality-module extraction (pizza ontology: 238 of 1,345 axioms, zero conclusions lost)
- MCP server for Claude Code, Claude Desktop, Cursor, Windsurf, Zed, VS Code; loads CSV, JSON, XML, YAML, XLSX, Parquet, PostgreSQL, DuckDB into RDF
- Caveats in the README: not an editor (use Protégé); in-memory storage by default; Python and Rust engines are not independent; published binaries omit eight feature-gated tools; a certificate digest binds to bytes, not world state
- Stack: Rust 2024, Oxigraph 0.5, rmcp, SQLite, Lean 4 v4.33.1 (no Mathlib); papers arXiv:2605.09184 and arXiv:2605.09168 (CIVeX)
