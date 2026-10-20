---
title: Semantic layer
type: concept
domains: [agents]
tags: [agentic, knowledge-cluster]
as_of: 2026-08-21
sources: [posthog-semantic-layer-2026-08-21, helixdb-helix-foundry-2026-10-19]
---

# Semantic layer

A semantic layer is a governed catalog of definitions — what a metric means, which tables to trust, how data sources join together — that sits on top of an existing data warehouse without copying or moving any data. Agents and humans both read from the same catalog instead of each reinventing a metric's definition from scratch on every query, which is why the same question ("what was our MRR last month?") can otherwise get a different, equally plausible-sounding, wrong answer from every tool that's asked. In the [Knowledge architectures](knowledge-architectures.md) matrix it is the store of *definitions* over an organization's data: agents propose, humans approve, and it holds no documents and no episodic memory.

## Also called

Metrics layer, governed metric catalog. "Context warehouse" is PostHog's product name for the store the layer sits on, not a synonym. Neo4j's Emil Eifrem uses "semantic layer" for a shared ontology substrate; that usage belongs to [Ontologies as agent guardrails](ontology-agent-guardrails.md), not here.

## Current status (as of 2026-08-21)

- Concretely: the catalog is stored as ordinary SQL tables (a metric is a table), so any agent that can run SQL can already read the entire layer — discovery is a query, not a bespoke integration.
- Governance model: "AI generated, human owned." Agents draft metric definitions, canonical-table suggestions, and join proposals, but nothing an agent creates is canonical until a human promotes it from "proposed" to "approved."
- Approval isn't a one-time gate: editing an approved metric's definition immediately reverts it to "proposed," and if a metric was built from an existing dashboard object that later gets edited independently, the metric is flagged "drifted" on every read (a live check, not a background job) — so the operative rule for any agent is `status = 'approved' AND is_drifted = false`, and everything else is treated as non-canonical.
- PostHog's implementation snapshots a metric's underlying query (rather than pointing live at a mutable dashboard object) specifically so drift can be detected and approval can't be silently invalidated by someone else's edit.
- Deliberately deferred: a full semantic query language (dbt-style) for composing metrics — treated as "complexity not yet earned" until usage data shows it's needed; SQL-backed metrics instead reuse an existing "saved view" primitive.

## Why it matters

Agent hallucination on business metrics is a governance problem, not a model-capability problem — a smarter model still has to invent an answer if the definition genuinely doesn't exist anywhere machine-readable. A semantic layer is the concrete fix: give every agent (and human) exactly one place to check whether a governed answer already exists before it derives its own.

## Related

- [Knowledge architectures](knowledge-architectures.md) — the hub that places this page against knowledge layers, agent memory, company brains, and ontologies
- [Knowledge layer](knowledge-layer.md) — compiles raw documents into LLM-maintained pages for reading; a semantic layer governs metric and data-source *definitions* over an existing warehouse and copies no data
- [Ontologies as agent guardrails](ontology-agent-guardrails.md) — another governed-ground-truth mechanism, formalized as classes and axioms rather than a metrics catalog
- [Company brain](company-brain.md) — the organization-scope system a semantic layer can sit under as the definitions its agents read from
- [Helix Foundry](../tools/helix-foundry.md) — the hub's local data-workspace variant: one person's workspace that copies the organization's records into snapshots and matches them across sources, rather than defining metrics over a warehouse in place

## Recent changes

- [2026-10-19] Linked the local data-workspace variant (Helix Foundry) now recorded under this row on the Knowledge architectures hub.
- [2026-08-21] Page created from PostHog's account of building a semantic layer into its context warehouse.

## Sources

- [PostHog — Building a semantic layer](../sources/tweets/posthog-semantic-layer-2026-08-21.md)
- [HelixDB/helix-foundry (GitHub)](../sources/repos/helixdb-helix-foundry-2026-10-19.md)
