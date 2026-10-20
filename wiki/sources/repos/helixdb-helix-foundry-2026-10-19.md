---
title: 'HelixDB/helix-foundry (GitHub)'
type: source
source_type: repo
source_file: raw/repos/helixdb-helix-foundry.md
url: https://github.com/HelixDB/helix-foundry
ingested: 2026-10-19
domains: [agents]
---

# HelixDB/helix-foundry (GitHub)

README for Helix Foundry, HelixDB's open-source (Apache 2.0) local-first data workspace built on HelixDB and DuckDB. It connects a company's databases, SaaS tools and files, suggests one connected "ontology" that matches the same records across sources, keeps data as versioned Parquet snapshots, and answers questions with executed SQL cited to those snapshots. Setup is delegated to a coding agent through a pasted prompt and an AGENTS.md runbook. The README gives no release date; the capture date (2026-10-19) is used.

## Influenced pages

- [Helix Foundry](../../tools/helix-foundry.md) — new tool page
- [State of Agents](../../state-of/agents.md) — new line under Knowledge platforms
- [Knowledge architectures](../../concepts/knowledge-architectures.md) — new local data-workspace variant row under the semantic layer; "one ontology" mapped to it in the term map
- [Semantic layer](../../concepts/semantic-layer.md) — Related link to the data-workspace variant

## Key claims extracted

- Tagline: "Your company's data, connected into one ontology, on your own computer"; no accounts, nothing to host, AI local by default
- Connectors: Neon, Supabase, PlanetScale, PostgreSQL, MySQL, Neo4j, Stripe, WorkOS, PostHog, REST APIs, S3-compatible storage, CSV/JSON/JSONL/Parquet uploads, ingestion API
- Automatic sync via native Postgres/MySQL change capture where allowed, scheduled snapshot refreshes otherwise
- Suggested ontology matches the same customers and records across sources, stored as objects and relationships in HelixDB; confirmed by the user in guided setup (AI → Data → Ontology)
- Immutable Parquet snapshots with profiles, schema-drift review and history; queried by isolated DuckDB processes with no internet, no credentials, no Linux capabilities
- Home shows key metrics; Analyst answers are backed by executed SQL with snapshot citations
- Default model `qwen3:4b` via Ollama; Claude, OpenAI, Azure OpenAI, Amazon Bedrock or custom OpenAI-compatible endpoints optional; AI-proposed changes are tested and wait for review
- Coding-agent install: paste a prompt into Claude Code, Codex or Cursor; the agent follows AGENTS.md and asks before deleting data or stopping running services; credentials are entered by the user in the browser, never given to the agent
- Built for one person on one computer: no sign-in, localhost only, API rejects foreign hosts and origins with 403; credentials encrypted with a local key
- Developer access: OpenAPI, TypeScript SDK, scoped read-only-by-default API tokens, backup/restore/upgrade scripts (only stub Docker tests so far)
- Validated on macOS Apple Silicon, CI on Linux, Windows untested; HelixDB pinned at v0.0.12
