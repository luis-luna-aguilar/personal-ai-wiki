---
title: "Building a semantic layer: What it is and how we did it at PostHog"
type: source
source_type: tweet
source_file: raw/tweets/2026-09-09-posthog-2090858894419693598.md
url: https://x.com/posthog/status/2090858894419693598
published: 2026-08-21
ingested: 2026-09-09
domains: [agents]
---

# Building a semantic layer: What it is and how we did it at PostHog

PostHog's own account (Lizzie Epton, Thiago Rocha Salvatore) of building a governed metric/definition catalog into its "context warehouse" after three different AI tools gave three different answers to the same MRR question. Covers the "AI generated, human owned" approve/drift governance model, the snapshot-not-live-pointer mechanism that makes drift detection possible, four rejected architecture alternatives, and beta success targets.

## Influenced pages

- [Semantic layer](../../concepts/semantic-layer.md) — new concept page
- [Knowledge architectures](../../concepts/knowledge-architectures.md) — new semantic-layer row and two term-map rows
- [Ontologies as agent guardrails](../../concepts/ontology-agent-guardrails.md) — `## Also called` now links the metric-definition sense of "semantic layer"

## Key claims extracted

- Motivating failure: Claude, Cursor, and PostHog AI gave 3 different MRR numbers from 3 different queries against the same underlying data
- Semantic layer = governed catalog sitting on top of existing data, describing (not copying) it: metric definitions, trusted tables, join logic
- Stored as ordinary SQL tables — a metric is a table — so any SQL-capable agent can already read the whole catalog
- Governance: "AI generated, human owned" — agents draft, humans approve; editing an approved metric reverts it to "proposed"; editing the underlying insight flags the metric "drifted" (live check, not background)
- Canonical rule for agents: `status = 'approved' AND is_drifted = false`; everything else is non-canonical
- Metrics built from an "insight" snapshot that insight's query server-side (not a live pointer) so the metric and the funnel/trend engine stay in lockstep and drift becomes detectable
- Four rejected alternatives: all-SQL metrics, plain-English-only definitions, live-pointer-to-insight, full dbt-style semantic query language (deferred as unearned complexity)
- "Context warehouse" is PostHog's name for the store the semantic layer sits on
- In beta via MCP tools, UI, and SQL; success targets (not yet-reported results): ≥80% accuracy on golden questions vs. no-catalog baseline, approved-metric-usage rate, catalog growth through everyday use
