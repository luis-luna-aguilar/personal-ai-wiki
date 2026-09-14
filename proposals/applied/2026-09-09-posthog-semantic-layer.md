---
type: proposal
source: raw/tweets/2026-09-09-posthog-2090858894419693598.md
status: pending
created: 2026-09-09
---

# Proposal: PostHog — "Building a semantic layer: What it is and how we did it at PostHog" (2026-08-21)

## Summary

### The source

On August 21, 2026, PostHog's engineering team (Lizzie Epton and Thiago Rocha Salvatore) published an account of a concrete failure that's becoming common as agents touch business data directly: asked "what was our MRR last month?", Claude, Cursor, and PostHog's own AI each returned a different SQL query and a different number — one summed the wrong Stripe table, one summed a different Stripe table, one tried to reconstruct recurring revenue from raw events and got the proration wrong. Every answer was plausible; there was no way to tell which was correct. The root cause is that what "MRR" means, which table holds it, and how it's calculated all live only in people's heads, so every agent session reinvents the definition slightly differently — and unlike a human analyst who might ask around, an agent answers confidently and hallucinates to fill the gap. Their fix is a **semantic layer**: a governed catalog of definitions — what a metric is, which tables to trust, how sources join — that sits on top of existing data without copying or moving any of it. Implementation detail that matters: the catalog is stored as ordinary SQL tables (a metric is a table), so there's no bespoke API for an agent to learn — if it can already run SQL, it can already read the whole layer. The governance model is explicitly named "AI generated, human owned": agents draft metric definitions, canonical-table suggestions, and joins, but nothing an agent creates is canonical until a human promotes it from "proposed" to "approved" — and approval isn't a one-time gate, since editing an approved metric's definition immediately reverts it to "proposed," and a metric built from a dashboard "insight" gets flagged "drifted" the moment someone edits that insight underneath it (checked live on every read, not in the background). The resulting rule for any agent is simple: a result is canonical only when `status = 'approved' AND is_drifted = false`. The post also walks through four architecture choices they deliberately rejected — all-SQL metrics (a hand-written SQL funnel can silently diverge from PostHog's actual funnel engine, so metrics instead snapshot an insight's underlying query and run it through the same engine); plain-English-only definitions (partially supported, but too non-deterministic alone); pointing metrics live at mutable insight objects (can't enforce "editing resets approval" on something anyone can edit at will, so a metric snapshots the query instead); and a full dbt-style semantic query language (deliberately deferred as "complexity we haven't earned" until usage data shows it's needed). PostHog calls the store the layer sits on its "context warehouse." The feature is in beta, reachable via MCP tools, the UI, and SQL, and PostHog is measuring toward (not yet reporting) three success bars: ≥80% accuracy on a fixed set of golden questions versus a no-catalog baseline, whether agents actually use an approved metric instead of deriving their own, and whether the catalog keeps growing through everyday use rather than only at setup.

### What changes

The wiki's [Knowledge architectures](../wiki/concepts/knowledge-architectures.md) hub (created 9 September) has four canonical rows — knowledge layer, agent memory, company brain, ontology — and notes in its term map that the data-warehouse sense of "semantic layer" is a different idea with no page yet. Per the hub's own rule, a new canonical page adds its row in the same proposal. This proposal adds the fifth row.

- New page `wiki/concepts/semantic-layer.md`, tagged into the knowledge cluster, with an `## Also called` line (metrics layer, governed metric catalog; context warehouse as the vendor term for the store beneath it) and Related lines that match the hub.
- **Knowledge architectures** gains a semantic-layer row in its canonical-pages table (organization's-data scope, holds metric and data-source definitions only, agents propose and humans approve), two term-map rows ("context warehouse" as PostHog's vendor term for the underlying store; "metrics layer, governed metric catalog" as aliases), "metric and data-source definitions" added to the "what it holds" axis, the Neo4j row's "no page yet" note replaced by a link, the PostHog source id, and a Recent-changes entry. Page date is unchanged: the hub's date tracks the newest claim among its canonical pages and 21 August is older than the current 7 September.
- **Ontologies as agent guardrails** gets the phrase in its `## Also called` line that says the data-warehouse sense "has no wiki page yet" replaced by a link to the new page. No date change, since no new claim lands on that page.
- **Wiki index** gains one new line under Concepts; the concepts and total-page counts each move up by one.
- One new source page is created for the PostHog post.

### What to weigh

This is a strong, clean, first-party engineering account with a concrete motivating failure case and specific mechanics (snapshot-not-live-pointer, live drift detection, four named rejected alternatives). The only thing worth flagging is that the ≥80%-accuracy and usage-growth figures are beta success *targets* PostHog is measuring toward, not results it has reported achieving — the draft below states them as targets, not accomplishments. This proposal was rewritten on 9 September against the terminology reorganization; the drafts assume the hub page and the reorganized ontology page as they now stand.

## Intended changes

- [x] **Approve all** — checking this box approves every item in `## Intended changes` below; the individual boxes may stay empty.

- [ ] **Create** `wiki/concepts/semantic-layer.md` — new concept page
    > See draft below

- [ ] **Update** `wiki/concepts/knowledge-architectures.md` — add the semantic-layer row to the canonical-pages table, add 2 term-map rows, extend axis 2, link the Neo4j row's note, append the source id, add 1 Recent-changes entry; no `as_of` change
    > See draft below

- [ ] **Update** `wiki/concepts/ontology-agent-guardrails.md` — replace the "no wiki page yet" phrase in `## Also called` with a link; no other change
    > See draft below

- [ ] **Update** `wiki/index.md` — add 1 line under Concepts, bump `concepts:` and `Total content pages:` counts by 1 each
    > See draft below

- [ ] **Create** `wiki/sources/tweets/posthog-semantic-layer-2026-08-21.md` — source summary; no existing page covers this URL

## Page drafts

### wiki/concepts/semantic-layer.md (new)

```md
---
title: Semantic layer
type: concept
domains: [agents]
tags: [agentic, knowledge-cluster]
as_of: 2026-08-21
sources: [posthog-semantic-layer-2026-08-21]
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

## Recent changes

- [2026-08-21] Page created from PostHog's account of building a semantic layer into its context warehouse.

## Sources

- [PostHog — Building a semantic layer](../sources/tweets/posthog-semantic-layer-2026-08-21.md)
```

### wiki/concepts/knowledge-architectures.md (updated)

Frontmatter: append `posthog-semantic-layer-2026-08-21` to `sources:`. `as_of` unchanged (2026-09-07 is newer than this source).

In `## The three axes`, change item 2 to:

```
2. **What it holds.** Compiled documents, episodic facts extracted from sessions, metric and data-source definitions, formal classes and rules, or a mix.
```

In the `## Canonical pages` table, insert this row between the Company brain row and the Ontologies row:

```
| [Semantic layer](semantic-layer.md) | the organization's data | definitions only: what each metric means, which tables to trust, how sources join, on top of an existing warehouse with no data copied | agents propose, humans approve; edits reset approval | PostHog semantic layer |
```

Change the sentence below the table to:

```
The rows are not rivals. A company brain typically contains a knowledge layer and agent memory; a semantic layer or an ontology can sit under any of them as the governed definitions or rules the others read from.
```

In the `## Term map` table, insert two rows after the "ghost memory" row:

```
| context warehouse | Semantic layer | PostHog's product name for the store its semantic layer sits on; a vendor term, not a concept |
| metrics layer, governed metric catalog | Semantic layer | aliases |
```

and change the Neo4j row's note to:

```
Emil Eifrem uses "semantic layer" for a shared ontology substrate that agents consume. It is not the metric-definition [semantic layer](semantic-layer.md) above; the collision is noted on both pages
```

Add to `## Recent changes`, as the newest entry:

```
- [2026-08-21] Added the semantic-layer row (governed metric and data-source definitions over an existing warehouse) from PostHog's account, plus "context warehouse" and "metrics layer" term-map rows.
```

Add to `## Sources`:

```
- [PostHog — Building a semantic layer](../sources/tweets/posthog-semantic-layer-2026-08-21.md)
```

### wiki/concepts/ontology-agent-guardrails.md (updated)

In `## Also called`, change:

```
that is a different idea from the data-warehouse sense of "semantic layer" (a governed catalog of metric definitions), which has no wiki page yet; the hub page keeps the two apart.
```

to:

```
that is a different idea from the data-warehouse sense of the term, the metric-definition [semantic layer](semantic-layer.md); the hub page keeps the two apart.
```

No frontmatter or Recent-changes change.

### wiki/index.md (updated)

Add under `## Concepts`, directly after the `concepts/knowledge-layer` line:

```
- [concepts/semantic-layer](concepts/semantic-layer.md) — governed catalog of metric and data-source definitions agents and humans both read from, sitting on top of an existing warehouse without copying data; also called metrics layer *(as_of: 2026-08-21)*
```

In `## Page count`, change `- concepts: 24` → `- concepts: 25` and `**Total content pages: 213.**` → `**Total content pages: 214.**` (re-derive from the live counts at apply time if other pages have landed).

### wiki/sources/tweets/posthog-semantic-layer-2026-08-21.md (new)

```md
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
```
