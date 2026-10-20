---
title: Helix Foundry
type: tool
domains: [agents]
subcategory: knowledge-platform
tags: [open-source, knowledge-cluster]
as_of: 2026-10-19
sources: [helixdb-helix-foundry-2026-10-19]
---

# Helix Foundry

Helix Foundry is HelixDB's open-source (Apache 2.0) local-first data workspace, built on the HelixDB graph database and DuckDB. It connects the systems a company runs on, suggests one connected model that matches the same customers and records across them, and answers questions with executed SQL. HelixDB markets that model as "one ontology"; in the wiki's vocabulary it is a knowledge graph over business records, not an [ontology](../concepts/ontology-agent-guardrails.md) in the guardrail sense (it carries no axioms or machine-checked rules). On the [Knowledge architectures](../concepts/knowledge-architectures.md) hub it is the local data-workspace variant of the [semantic layer](../concepts/semantic-layer.md): one person's governed view of an organization's data that copies and matches the records instead of only defining metrics over a warehouse in place.

## Also called

"One connected ontology" (HelixDB's marketing term), local-first data workspace.

## Current status (as of 2026-10-19)
- Connectors for Postgres, MySQL, Neon, Supabase, PlanetScale, Neo4j, Stripe, WorkOS, PostHog, REST APIs, S3-compatible storage, file uploads and an ingestion API; change capture on Postgres and MySQL where allowed, scheduled snapshots otherwise
- Suggested ontology matches records across sources and stores them as objects and relationships in HelixDB; the user confirms it during setup
- Data kept as immutable Parquet snapshots with profiles and schema-drift review; generated SQL runs in an isolated DuckDB executor with no internet access or credentials
- "Analyst" answers cite the executed SQL and the snapshot it ran on; AI-proposed changes are tested and wait for human review
- Local `qwen3:4b` through Ollama by default; Claude, OpenAI, Azure OpenAI, Bedrock or any OpenAI-compatible endpoint optional
- Installed by a coding agent: the README supplies a prompt for Claude Code, Codex or Cursor, and an AGENTS.md runbook covers preflight, setup, verification and when to ask before deleting data

## Strengths
- Nothing to host and no accounts; data and, by default, the model stay on the user's machine
- Answers are auditable: each one points to the SQL and the versioned snapshot behind it

## Weaknesses / caveats
- Built for one person: no sign-in, so anyone who can reach the app controls every workspace; must stay on localhost
- Backup, restore and upgrade scripts have only stub tests; Windows is untested; first run downloads several GB
- No dated release in the source; the HelixDB dependency is pinned at v0.0.12

## Recent changes
- [2026-10-19] Page created from the project's GitHub README (no dated release event in the source).

## Related
- [Knowledge architectures](../concepts/knowledge-architectures.md) — the hub row for the local data-workspace variant of the semantic layer, and the term-map entry for "one ontology"
- [Utopia](utopia.md) — the other self-hosted knowledge platform tracked: also entity resolution plus SQL over mounted databases, but built on formal ontology axioms and a bitemporal decision ledger
- [Semantic layer](../concepts/semantic-layer.md) — governs metric definitions over a warehouse without copying data; Helix Foundry is the variant that copies the data and matches records

## Sources
- [HelixDB/helix-foundry (GitHub)](../sources/repos/helixdb-helix-foundry-2026-10-19.md)
