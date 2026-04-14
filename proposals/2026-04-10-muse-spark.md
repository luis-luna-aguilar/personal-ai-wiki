---
type: proposal
source: raw/articles/2026-04-10-aimetacom-blog-introducing-muse-spark-msl.md
status: pending
created: 2026-04-10
---

# Proposal: Muse Spark

## Summary

Meta introduces **Muse Spark** as a new multimodal model from its Superintelligence Labs effort. The captured source is mostly a scaling/efficiency post rather than a full launch doc: it emphasizes predictably scaling capability across pretraining, reinforcement learning, and test-time reasoning, and claims Muse Spark can reach prior Llama 4 Maverick-level capability with over an order of magnitude less training compute.

This is still strong enough to justify a first proper model-family page in the wiki beyond the existing Composer 2 stub. The main caveat is that the fetched source is thin on API, product, and benchmark specifics, so the page should stay concise and avoid overclaiming.

## Intended changes

- [x] **Create** `wiki/models/muse-spark.md` — new model page for Meta's Muse Spark
  > See full draft below.

- [x] **Update** `wiki/state-of/models.md` — replace the empty placeholder with a first real subcategory and add Muse Spark
  > See diff snippet below.

- [x] **Create** `wiki/sources/articles/muse-spark.md` — source summary page
  > See full draft below.

- [x] **Update** `wiki/index.md` — add the new model entry and refresh counts
  > See diff snippet below.

## Page drafts

### wiki/models/muse-spark.md (new)

```markdown
---
title: Muse Spark
type: model
domains: [models]
subcategory: frontier-multimodal-model
tags: [closed-source, agentic]
as_of: 2026-04-10
sources: [muse-spark]
---

# Muse Spark

Muse Spark is a new multimodal model from Meta's Superintelligence Labs effort. In the source captured here, Meta frames it less as a product with a detailed public surface and more as a scaling result: a model whose capability improves efficiently across pretraining, reinforcement learning, and test-time reasoning.

## Current status (as of 2026-04-10)

- Meta positions Muse Spark as part of its push toward "personal superintelligence"
- The captured source says Muse Spark's capabilities scale along three axes: pretraining, reinforcement learning, and test-time reasoning
- Meta says the rebuilt pretraining stack improved architecture, optimization, and data curation over the prior nine months
- Vendor claim: Muse Spark can reach prior Llama 4 Maverick-level capability with over an order of magnitude less training compute
- The source describes Muse Spark as acquiring multimodal understanding, reasoning, and coding ability during pretraining

## Why it matters

The strongest signal in this source is not a benchmark table. It is Meta claiming a materially more compute-efficient frontier training recipe than its prior generation. If that holds up, Muse Spark matters as a sign that scaling efficiency and test-time systems work are still moving quickly at the frontier.

## Weaknesses / caveats

- The captured source is brief and mostly about scaling philosophy, not full product documentation
- No public pricing, API details, weights, model sizes, or broader benchmark sweep are captured here
- The efficiency claim is Meta-reported and presented relative to its prior model

## Recent changes

- [2026-04-10] Page created from Meta's Muse Spark introduction post

## Sources

- [[sources/articles/muse-spark]]
```

### wiki/sources/articles/muse-spark.md (new)

```markdown
---
title: Introducing Muse Spark: Scaling Towards Personal Superintelligence
type: source
source_type: article
source_file: raw/articles/2026-04-10-aimetacom-blog-introducing-muse-spark-msl.md
url: https://ai.meta.com/blog/introducing-muse-spark-msl
ingested: 2026-04-10
domains: [models]
---

# Introducing Muse Spark: Scaling Towards Personal Superintelligence

Meta introduces Muse Spark as a multimodal model and uses the post mainly to argue that its frontier stack is becoming much more compute-efficient. The captured source focuses on scaling behavior across pretraining, reinforcement learning, and test-time reasoning rather than giving a detailed product or model-card style launch document.

## Influenced pages

- [[models/muse-spark]] — new model page for Muse Spark
- [[state-of/models]] — first populated model subcategory entry

## Key claims extracted

- Muse Spark is positioned as a multimodal model in Meta's push toward "personal superintelligence"
- Meta studies its scaling along pretraining, reinforcement learning, and test-time reasoning
- The source says pretraining gives Muse Spark its multimodal understanding, reasoning, and coding ability
- Meta says it rebuilt the pretraining stack over nine months with changes to architecture, optimization, and data curation
- Vendor claim: the new recipe reaches prior Llama 4 Maverick-level capability with over an order of magnitude less compute

## Caveats

- The fetched source is brief and does not capture a full product, API, or benchmark write-up
- No explicit `published:` date was visible in the saved raw file, so `ingested: 2026-04-10` is the date-of-record in this summary
- The compute-efficiency claim is vendor-reported and relative to Meta's own prior model
```

### wiki/state-of/models.md (updated snippet)

```markdown
---
title: State of Models
type: state-of
domains: [models]
tags: []
as_of: 2026-04-10
sources: [muse-spark]
---

# State of Models

Current state of foundation models — frontier and otherwise. Organized by subcategory. A subcategory can have multiple leaders.

## Subcategories

### Frontier multimodal models

General-purpose frontier models competing on broad multimodal capability rather than narrow specialization.

- [[models/muse-spark]] — Meta's new multimodal model; the captured launch source emphasizes scaling efficiency and claims Llama 4 Maverick-level capability with over an order of magnitude less training compute *(as of 2026-04-10)*

## Recent changes

- [2026-04-10] Added `frontier-multimodal-model` subcategory with [[models/muse-spark]]
- [2026-04-10] Gemini adds custom interactive visualizations in chat and notebooks (dedicated workspaces with grouped chats, file uploads, instructions); rolling out to paid accounts first
```

### wiki/index.md (updated snippet)

```markdown
## Models

- [[models/composer-2]] — Cursor's in-house frontier coding model; stub *(as_of: 2026-04-02)*
- [[models/muse-spark]] — Meta's new multimodal model; source emphasizes compute-efficient scaling vs prior Llama 4 Maverick generation *(as_of: 2026-04-10)*

## State of

- [[state-of/models]] — current state of foundation models *(as_of: 2026-04-10)*

## Page count

- state-of: 7 (6 populated, 1 skeleton)
- models: 2
- tools: 12
- benchmarks: 0
- workflows: 1
- concepts: 5
- trends: 3
- training: 1

**Total content pages: 31.** The wiki is still in the early stage, but no longer below the initial bootstrap threshold.
```

## Schema / vocabulary additions

- [x] Add subcategory `frontier-multimodal-model` to `wiki/_schema/subcategories.md`
  - Parent domain(s): `models`
  - Applies to types: `model`
  - Definition: General-purpose frontier models competing on broad multimodal capability rather than narrow specialization.

## Open questions

- The captured Meta source is thinner than a normal launch post. I kept the page intentionally concise and avoided unsupported claims from the newsletter blurb. If you want a fuller Muse Spark page, we likely need a richer primary source than the saved capture.
