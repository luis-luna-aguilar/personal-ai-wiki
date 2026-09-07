---
type: proposal
source: raw/newsletters/2026-08-11-ainews-muse-glimmer-and-spark-open-weights-retu.md
status: pending
created: 2026-09-07
---

# Proposal: Anthropic Claude improves a Riemann Hypothesis critical-line bound

## Summary

### The source

Anthropic announced that an unreleased internal research variant of Claude was set loose on the Riemann Hypothesis, one of mathematics' most famous open problems — a conjecture about where the "zeros" of a particular function must fall, which underlies much of what is known about the distribution of prime numbers. The model did not solve the conjecture, but it did move a decades-old partial result: the proven share of zeta-function zeros known to lie on the "critical line" (the property the full conjecture claims for every zero) rose from 41.6% to 67.2%, per Anthropic's own announcement summarized in AINews. Commentator Jarred Sumner added that the model reached this through repeated retries and large-scale exploration spanning roughly 31 million output tokens, rather than a single clean derivation. Reactions quoted in the source, including from mathematician @jdlichtman, read it less as "the Riemann Hypothesis has been cracked" and more as a vivid example of AI-assisted theorem search and iterative proof refinement.

### What changes

`trends/ai-in-science.md` currently documents domain-specific scientific-reasoning wins mostly in biology and drug discovery, plus one prior pure-math example (OpenAI's Erdős unit-distance disproof).

- **AI in Science** gains a second pure-math signal — this time from Anthropic rather than OpenAI, showing the pattern isn't lab-specific: a new Current-status bullet and a matching Recent-changes entry dated 2026-08-11, explicitly framed as a lab-reported, not-yet-independently-verified claim. Page date moves to 11 August. One new source id.
- New source page for the AINews issue this came from.

### What to weigh

This entire signal traces to a single Anthropic announcement, summarized secondhand by AINews with one supporting reaction tweet — there is no independent mathematician confirmation of the bound itself, and Anthropic disclosed no model name or verification methodology beyond the headline percentages. The draft below frames this the same way the wiki already frames the earlier OpenAI Erdős result: as a disclosed lab claim, not a peer-verified result.

## Intended changes

- [x] **Approve all** — checking this box approves every item in `## Intended changes` and `## Schema / vocabulary additions` below; the individual boxes may stay empty.

- [ ] **Update** `wiki/trends/ai-in-science.md` — new Current-status bullet, Recent-changes entry, as_of bump, new source id
    > See draft below

- [ ] **Create** `wiki/sources/newsletters/anthropic-riemann-hypothesis-2026-08-11.md` — source summary

## Page drafts

### wiki/trends/ai-in-science.md (updated)

```md
---
title: AI in Science
type: trend
domains: [science]
tags: []
as_of: 2026-08-11
sources: [noetik-cancer-trials, gpt-rosalind-launch, self-driving-lab-radical-ai, claude-science-beta-2026-07-06, every-tale-of-two-models-2026-07-05, claude-science-workbench-2026-07, esmfold2-protein-world-model-2026-05, openai-erdos-unit-distance-2026-05, lila-sciences-automated-wet-lab-2026-07-16, xaira-x-cell-causal-virtual-cell-2026-07-21, anthropic-riemann-hypothesis-2026-08-11]
---

## Current status (as of 2026-08-11)

<!-- existing bullets unchanged, append this one at the end of the list -->
- The domain-specific-reasoning pattern is not limited to biology: an OpenAI general-purpose reasoning model (not a math-specialized or scaffolded system) disproved the 1946 Erdős planar unit-distance conjecture, verified by external mathematicians. OpenAI discloses no model name, runtime, or cost; the "<32 hours / <$1,000 / GPT-5.6" figures in secondary coverage are speculation — see [State of Science](../state-of/science.md).
- Anthropic reported a second pure-math signal: an unreleased internal research Claude variant improved a longstanding Riemann Hypothesis-related bound — the proven share of zeta-function zeros on the critical line rose from 41.6% to 67.2% — reached via large-scale retries and exploration (~31M output tokens) rather than a single clean proof. Engineers framed it as theorem-search progress, not a solved conjecture, and it is not yet independently verified by outside mathematicians.

<!-- Recent changes: insert as the newest entry -->
## Recent changes

- [2026-08-11] Anthropic reported an unreleased research Claude variant improved a Riemann Hypothesis-related bound (proportion of zeta zeros proven on the critical line: 41.6% → 67.2%), via ~31M output tokens of retries/exploration — a second pure-math signal alongside OpenAI's Erdős disproof; not yet independently verified.
- [2026-07-21] Added Xaira Therapeutics' X-Cell/X-Atlas as a causal counterpoint to correlational RNA-expression virtual-cell models
```

### wiki/sources/newsletters/anthropic-riemann-hypothesis-2026-08-11.md (new)

```md
---
title: AINews — Anthropic's Riemann Hypothesis bound improvement
type: source
source_type: newsletter
source_file: raw/newsletters/2026-08-11-ainews-muse-glimmer-and-spark-open-weights-retu.md
url: https://www.latent.space/p/ainews-muse-glimmer-and-spark-open
published: 2026-08-11
ingested: 2026-09-07
domains: [science]
---

# AINews — Anthropic's Riemann Hypothesis bound improvement

AINews recap of an Anthropic announcement: an unreleased internal research Claude variant, tasked with the Riemann Hypothesis, improved a longstanding lower bound on the proportion of non-trivial zeta-function zeros proven to lie on the critical line, from 41.6% to 67.2%, via large-scale retries and exploration (~31M output tokens per commentary from Jarred Sumner). Framed by engineers as AI-assisted theorem search/proof iteration, not a solved conjecture; not yet independently verified by outside mathematicians.

## Influenced pages

- [trends/ai-in-science](../../trends/ai-in-science.md) — new Current-status bullet and Recent-changes entry: second pure-math autoresearch signal alongside OpenAI's Erdős disproof

## Key claims extracted

- Unreleased Anthropic research Claude variant did not solve the Riemann Hypothesis
- Improved the proven lower bound of zeta zeros on the critical line from 41.6% to 67.2%
- Reached via repeated retries and large-scale exploration over ~31M output tokens
- Engineers and observers (including mathematician @jdlichtman) characterized it as theorem-search progress, not conjecture resolution
```

## Open questions

- Please split the science page and create one custom for mathematics. Theres a lot of advanced in this field.
