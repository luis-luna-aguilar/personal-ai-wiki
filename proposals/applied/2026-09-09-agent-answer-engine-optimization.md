---
type: proposal
source: raw/newsletters/2026-09-07-the-frontier-aeo-tracker-what-astra-chooses-and.md
status: pending
created: 2026-09-09
---

# Proposal: Agent answer-engine optimization (AEO)

## Summary

### The source

Latent Space built and published a "Frontier AEO tracker": six prompt variations run against seven frontier models (with search enabled) across 161 product and service categories, from coding agents to AI podcasts to managed databases, scored on a proprietary index that weights first-choice recommendations, alternative mentions, and — with negative weight — anti-recommendations. Two findings stand out. First, models are meaningfully self-biased when recommending tools: Fable and Opus favor Claude Code, Sol and Astra favor Codex, Grok favors Cursor, Muse favors Muse Code, and SWE-1.7 favors Devin — alongside 28 of the 161 categories (about a sixth) where every surveyed model converges on the same top choice regardless of vendor. Second, the labs differ in how they source answers: Anthropic's models cite noticeably more sources per answer than OpenAI's (Opus median 11, Fable median 15, versus Sol median 9, Astra median 5), and Astra in particular is unusually "sticky" — its answer rarely changes when a question is lightly paraphrased, which the authors argue raises the practical payoff of optimizing content specifically for it. The tracker's methodology is inspectable (every prompt/answer pair is published), though the project itself has an obvious commercial angle — AEO-as-a-service — that the wiki should note without treating as disqualifying.

### What changes

The wiki has no existing page for this phenomenon — the closest adjacent content is scattered tool-recommendation asides inside individual tool pages, not a named, measured concept.

- New page `wiki/concepts/agent-answer-engine-optimization.md`: what AEO is, the self-bias finding, the source-citation-behavior finding, and the methodology caveat.
- One new source page for the Latent Space piece.

### What to weigh

This is a single-source concept page from one outlet with a stated commercial interest in the category it's measuring (they explicitly solicit "business enquiries to develop this further"). The methodology is unusually transparent for a marketing-adjacent project (published prompt/answer pairs), which is why this is scoped as a lightweight ingest rather than skipped — but a second independent measurement of the same phenomenon would strengthen it considerably.

## Intended changes

- [x] **Approve all**

- [ ] **Create** `wiki/concepts/agent-answer-engine-optimization.md` — new concept page
    > See draft below

- [ ] **Create** `wiki/sources/newsletters/latent-space-aeo-tracker-2026-09-07.md` — source summary

## Page drafts

### wiki/concepts/agent-answer-engine-optimization.md (new)

````md
---
title: Agent answer-engine optimization (AEO)
type: concept
domains: [agents]
tags: [agentic]
as_of: 2026-09-07
sources: [latent-space-aeo-tracker-2026-09-07]
---

# Agent answer-engine optimization (AEO)

The practice — and the measurable phenomenon behind it — of optimizing content and positioning so AI models recommend a product or tool when a user asks an agent for a suggestion, the LLM-era successor to search-engine optimization. Latent Space's "Frontier AEO tracker" is the first published attempt to measure it directly: six prompt variations across seven frontier models and 161 product categories, scored on first-choice weight, alternative-mention weight, and negative weight for anti-recommendations.

## Current status (as of 2026-09-07)

- Models show meaningful self-bias recommending tools from their own ecosystem: Fable/Opus favor Claude Code, Sol/Astra favor Codex, Grok favors Cursor, Muse favors Muse Code, SWE-1.7 favors Devin
- 28 of 161 tracked categories have a genuinely universal top choice across all surveyed models — the rest are contested "AEO battlegrounds"
- Anthropic's models cite more sources per answer than OpenAI's (Opus median 11, Fable median 15, vs. Sol median 9, Astra median 5)
- Astra is unusually "sticky": its answer rarely flips when a question is lightly paraphrased, raising the practical value of optimizing specifically for it
- Methodology is inspectable — every prompt/answer pair is published — but the project has a stated commercial angle (AEO-as-a-service)

## Why it matters

As agents increasingly mediate product discovery, self-serving bias in tool recommendations becomes a competitive dynamic worth tracking in its own right, distinct from raw model capability — and a second independent measurement of the same effect would meaningfully strengthen this still single-source finding.

## Recent changes

- [2026-09-07] Page created from Latent Space's Frontier AEO tracker.

## Sources

- [Latent Space — The Frontier AEO Tracker](../sources/newsletters/latent-space-aeo-tracker-2026-09-07.md)
````

### wiki/sources/newsletters/latent-space-aeo-tracker-2026-09-07.md (new)

```md
---
title: "The Frontier AEO Tracker: What Astra Chooses (and every other frontier model, and what you can do about it)"
type: source
source_type: newsletter
source_file: raw/newsletters/2026-09-07-the-frontier-aeo-tracker-what-astra-chooses-and.md
url: https://www.latent.space/p/aeo
published: 2026-09-07
ingested: 2026-09-09
domains: [agents]
---

# The Frontier AEO Tracker

Latent Space measures self-bias in frontier-model tool recommendations across 161 categories and 7 models: labs favor their own coding agents, 28 categories have a universal top choice, and Anthropic's models cite more sources per answer than OpenAI's.

## Influenced pages

- [Agent answer-engine optimization (AEO)](../../concepts/agent-answer-engine-optimization.md) — new page

## Key claims extracted

- 6 prompt variations x 7 models x 161 categories, inspectable prompt/answer pairs
- Self-bias: Fable/Opus → Claude Code, Sol/Astra → Codex, Grok → Cursor, Muse → Muse Code, SWE-1.7 → Devin
- 28/161 categories have a universal top choice across all models
- Source-citation medians: Opus 11, Fable 15, Sol 9, Astra 5
- Astra's answers are unusually stable under paraphrasing
```

## Schema / vocabulary additions

None.

## Open questions

None beyond the sourcing noted above.
