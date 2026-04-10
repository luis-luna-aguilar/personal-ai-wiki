---
type: proposal
source: raw/articles/2026-04-10-everyto-playtesting-the-market-for-making-ai-better.md
status: applied
created: 2026-04-10
---

# Proposal: Every / Playtesting - The Market for Making AI Better

## Summary

This Every essay argues that the market for improving AI models is shifting from a pure scale-and-compute story toward a more distributed market around **proprietary data**, **task-specific evaluation**, and **domain-specialized model training**. The substantive claims are not about one product launch; they are about where value is accumulating: companies with high-quality, continuously growing operational data, and teams that can turn real work into evals and training loops.

The strongest wiki-worthy signal is strategic, not tactical. The piece claims that frontier labs are increasingly buying access to non-public datasets, that narrow models trained on small volumes of expert examples can outperform most frontier models on specific professional tasks, and that current benchmark coverage is badly skewed toward code and math relative to the real economy. That makes this a better fit for a new **trend page** than for updating any existing tool page.

## Intended changes

- [x] **Create** `wiki/trends/proprietary-data-becomes-model-moat.md` — new trend page on proprietary enterprise data, domain evals, and specialized training loops as a competitive moat for AI quality
  > See full draft below.

- [x] **Create** `wiki/sources/articles/market-for-making-ai-better.md` — source summary page
  > See full draft below.

- [x] **Update** `wiki/index.md` — add the new trend entry and refresh counts
  > See diff snippet below.

## Schema / vocabulary additions

- None proposed.

## Why not update existing pages

- **`wiki/trends/agents-reshape-organizations.md`** is adjacent, but that page is specifically about background agents shifting leverage from individual workers to organizations. This source is more about **data markets, domain evals, and model specialization** than about autonomous agents changing org design.
- **`wiki/state-of/models.md`** is a dashboard for model cohorts and leaders. This source does not identify stable leaders or add a model-specific comparison set; it is better as a trend that can later inform model pages.
- **Existing tool pages** would be the wrong target because the source is not primarily about Cursor, Harvey, Mercor, or another one product already in the wiki.

## Page drafts

### wiki/trends/proprietary-data-becomes-model-moat.md (new)

```markdown
---
title: Proprietary data becomes model moat
type: trend
domains: [models]
tags: []
as_of: 2026-04-10
sources: [market-for-making-ai-better]
---

# Proprietary data becomes model moat

The trend: as frontier model quality converges, more of the advantage may come from **non-public, continuously refreshed data** and the ability to turn that data into domain-specific evals and training loops. Instead of assuming scale and compute alone determine quality, this view says that the next edge often comes from owning real examples of economically valuable work.

This is not only about selling data to labs. The same company can license its data externally, fine-tune an internal model with it, or do both. The strongest position is a flywheel: production work generates proprietary traces, those traces become training/eval data, and the resulting model becomes cheaper or better for that company's own use case.

## Current status (as of 2026-04-10)

- AI labs and intermediaries are actively seeking non-public operational data, not just public web corpora
- The highest-value datasets tend to be both **high quality** and **continuously growing**
- Programming and math remain overrepresented in benchmark coverage relative to the distribution of paid work in the real economy
- The next scarce asset may be less "more text" and more **good task definitions plus ground-truth data** for domain work
- Small or open-base models can reportedly beat most frontier models on narrow professional tasks when trained on the right expert examples

## Why it matters

If this trend holds, "best model" stops being a single global ranking and becomes more local to a workflow or industry. A company with years of support tickets, decision logs, matter histories, analyst notes, or other expert traces may have a stronger path to useful AI than a company that only consumes generic frontier APIs.

The bottleneck also shifts upstream from model access to **measurement**. Teams that define credible evals for real work first get to decide what "good" means in that domain, which shapes training demand and product direction.

## Signals in this source

- Data licensors such as Reddit, Shutterstock, and News Corp are framed as direct beneficiaries of AI-training demand
- Enterprise data providers and intermediaries are actively buying or brokering proprietary operational data
- A cited Applied Compute case study claims a small model trained on fewer than 2,000 expert examples beat all but the top frontier models on corporate legal work
- Carnegie Mellon / Stanford research is cited to argue that current benchmarks map poorly to the actual economy, leaving large pockets of unmeasured work
- Companies such as Cursor, Shopify, Pinterest, and Cognition are cited as training specialized models on top of open foundations

## Caveats

- This is an editorial essay by the CEO of Good Start Labs, a company that sells data/environments to AI companies, so the source has clear commercial alignment with the thesis
- Several headline claims rely on linked external sources or company statements rather than firsthand reporting in the essay itself
- The page should be treated as a directional market trend, not as settled proof that proprietary-data strategies will dominate scale strategies

## Open questions

- Which domains beyond coding and legal will produce the first widely accepted "economically valuable work" eval suites?
- Will the durable moat be the underlying proprietary dataset, the evaluation framework built on top of it, or the production loop that keeps refreshing both?
- How much of this market stays with frontier labs versus shifting to companies training narrower models on open bases?

## Recent changes

- [2026-04-10] Trend opened from Every's "The Market for Making AI Better" essay

## Sources

- [[sources/articles/market-for-making-ai-better]]
```

### wiki/sources/articles/market-for-making-ai-better.md (new)

```markdown
---
title: The Market for Making AI Better
type: source
source_type: article
source_file: raw/articles/2026-04-10-everyto-playtesting-the-market-for-making-ai-better.md
url: https://every.to/playtesting/the-market-for-making-ai-better
ingested: 2026-04-10
domains: [models]
---

# The Market for Making AI Better

Every publishes an editorial essay by Alex Duffy arguing that the emerging market for improving AI is increasingly organized around proprietary, continuously refreshed data and domain-specific measurement, not only around frontier-scale training. The piece frames enterprise workflow data as strategically valuable both for licensing to labs and for training narrower in-house models that can outperform general models on specific tasks.

## Influenced pages

- [[trends/proprietary-data-becomes-model-moat]] — new trend page capturing the thesis that proprietary operational data and domain evals are becoming an AI moat

## Key claims extracted

- AI labs and data intermediaries are actively buying proprietary operational data from companies
- High-value datasets tend to be both high quality and continuously growing
- Current model-improvement demand is concentrated around software engineering and math, partly because those domains recursively help build better AI
- Labs are widening interest toward "economically valuable work" in fields like healthcare, professional services, and defense
- A cited Applied Compute case study claims that a small model trained on fewer than 2,000 expert examples beat all but the best frontier models on corporate legal tasks
- Carnegie Mellon / Stanford research is cited to argue that benchmark coverage is badly skewed toward programming and math relative to the real economy
- Companies with proprietary internal data have two strategic options: license it externally or use it to train internal specialized models
- The source argues that production usage itself can become a moat by generating more training data over time

## Caveats

- Editorial essay written by the CEO of Good Start Labs, a company aligned with the thesis
- Several concrete examples in the essay are second-order references to linked external reporting or case studies
- The source is useful for framing the market direction, but not for precise market sizing or neutral competitive rankings
```

### wiki/index.md (updated snippet)

```markdown
## Trends

- [[trends/agents-reshape-organizations]] — leverage moves from individual to org as autonomous agents take coordination work *(as_of: 2026-04-02)*
- [[trends/ai-in-science]] — AI as force-multiplier for researchers; NASA anomalies, brain MRI, AlphaFold *(as_of: 2026-04-10)*
- [[trends/proprietary-data-becomes-model-moat]] — proprietary operational data, domain evals, and narrow training loops may become a stronger moat as model quality converges *(as_of: 2026-04-10)*

## Page count

- state-of: 7 (5 populated, 2 skeleton)
- models: 1
- tools: 11
- benchmarks: 0
- workflows: 1
- concepts: 5
- trends: 3

**Total content pages: 28.** The wiki is in the bootstrap phase (<30 pages) — categorization discipline is relaxed.
```
