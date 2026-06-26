---
type: proposal
sources:
  - raw/newsletters/2026-06-17-copilot-cowork-becomes-generally-available.md
  - raw/newsletters/2026-06-17-ainews-glm-52-the-top-frontend-coding-model-in.md
status: pending
created: 2026-06-17
---

# Proposal: Databricks summit — Genie One, Unity AI Gateway, Lakebase

## Summary

At their annual summit, Databricks announced three interconnected products: Genie One (agentic coworker for business teams), Unity AI Gateway (enterprise AI governance with MCP auth), and Lakebase (serverless Postgres with branching for agent workloads). Together they position Databricks as the data-first enterprise AI platform connecting governance, agent infrastructure, and cost controls. No Databricks page exists in the wiki.

## Intended changes

- [x] **Create** `wiki/tools/databricks.md` — new tool page
- [x] **Create** `wiki/sources/newsletters/databricks-summit-june-2026.md` — source summary

## Page drafts

### wiki/tools/databricks.md (new)

````md
---
title: Databricks
type: tool
domains: [agents]
subcategory: ai-assistant
tags: [enterprise, closed-source]
as_of: 2026-06-17
sources: [databricks-summit-june-2026]
---

# Databricks

Data and AI platform for enterprises. Historically focused on data engineering (Delta Lake, Apache Spark). In June 2026, announced three new products that position it as enterprise AI infrastructure: Genie One (agentic coworker), Unity AI Gateway (AI governance layer), and Lakebase (agent-native Postgres).

## Current status (as of 2026-06-17)

**Genie One** — agentic coworker for business teams
- Automates workplace tasks across apps, documents, and chat
- Runs on Genie Ontology: a self-improving context layer with 4.5M ontology snippets that Databricks builds and maintains; claimed to understand business-specific semantics automatically

**Unity AI Gateway** — enterprise AI governance
- Budget limits, guardrails, and MCP auth controls across all AI spend in the organization
- Single governance layer across multiple AI tools and models
- The MCP auth angle is notable: companies building on MCP need something at the org layer to enforce authentication, access limits, and cost policies

**Lakebase** — agent-native Postgres
- Serverless Postgres with git-style branching designed for agent workloads
- Branching enables agents to work in isolated environments without affecting production data
- Delta/Iceberg format unification also announced: standardizes the data layer beneath all three products

## Strengths

- Unique position: data platform that can wrap AI governance, context, and compute in one place for enterprises already on Databricks
- Unity AI Gateway with MCP auth addresses a real gap for companies with multi-tool AI deployments
- Genie Ontology's self-improving context layer is a distinctive approach to enterprise context problems

## Weaknesses / caveats

- All details from secondary newsletter coverage; primary Databricks documentation not yet fetched
- Enterprise-first; not relevant for teams without existing Databricks investment

## Recent changes

- [2026-06-17] Genie One, Unity AI Gateway, and Lakebase announced at annual summit; Iceberg/Delta unification

## Sources

- [Databricks summit announcements — June 2026](../sources/newsletters/databricks-summit-june-2026.md)
````

### wiki/sources/newsletters/databricks-summit-june-2026.md (new)

````md
---
title: Databricks Data + AI Summit announcements (June 2026)
type: source
source_type: newsletter
source_file: raw/newsletters/2026-06-17-copilot-cowork-becomes-generally-available.md
published: 2026-06-17
ingested: 2026-06-17
domains: [agents]
---

# Databricks Data + AI Summit announcements (June 2026)

## Influenced pages

- [Databricks](../../tools/databricks.md) — new page

## Key claims extracted

- Genie One: agentic coworker running on Genie Ontology (4.5M ontology snippets for self-improving context)
- Unity AI Gateway: budget limits, guardrails, MCP auth for enterprise AI governance
- Lakebase: serverless Postgres with branching for agent workloads
- Iceberg/Delta format unification
- Source: Superhuman and AINews secondary coverage; primary Databricks docs not yet fetched
````
