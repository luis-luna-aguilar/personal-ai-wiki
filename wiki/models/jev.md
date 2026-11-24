---
title: Jev
type: model
domains: [models]
subcategory: decision-model
tags: [closed-source]
as_of: 2026-11-24
sources: [latent-space-jev-diogo-almeida-2026-09-21, every-how-to-get-most-out-of-jev-2026-09-23, ainews-jev-judge-clm-critique-2026-09-25, cloudflare-clef-decision-models-2026-10-02, ainews-decisions-api-beta-vals-jev-2026-10-07, ainews-decision-models-product-category-2026-10-10, ainews-aa-decision-index-2026-10-14, ainews-liquid-d1-ultra-pplx-decider-2026-10-17, tamaratran-fast-jev-compaction, typesafe-docs-images-2026-11-24, typesafe-docs-use-case-map-2026-11-23]
---

# Jev

TypeSafe's API-only decision model, released 2026-09-15 and marketed as a "System One" model. Jev answers questions about text, structured input and (experimentally) images instead of generating text. A Noulli question returns the probability that a statement is true, a Choice question returns probabilities over a set of options, a Score question places the input on a scale, and a Box question returns where something is in an image. TypeSafe CEO Diogo Almeida, a co-author of InstructGPT, maps the first three to an if statement, a switch statement and a sort. It is the reference point for the [decision models](../concepts/decision-models.md) category.

## Current status (as of 2026-11-24)

- Price: $0.042 per 1M input tokens, output free; 32K context per Cloudflare's comparison. Images are an opt-in experiment ("Dreamer-ready", behind a `TypeSafe-Danger-Zone-Images: true` header): Jev 1.13 and 1.14 accept them in the state, instructions or criteria of any question, and Jev 1.14 adds Box questions that return a bounding box with a confidence. TypeSafe's examples read scanned records, check OCR fields on invoice photos and label video frames one at a time.
- Trained with RLCD (reinforcement learning for calibrated decisions), an unpublished method that rewards honest probabilities rather than rater-preferred answers.
- TypeSafe publishes no benchmark scores, never refuses a request, and freezes each version once it ships (current versions 1.13 and 1.14).
- Artificial Analysis Decision Index: Jev 1.13 led at 58 at launch (2026-10-14); Liquid d1-ultra now leads at 65, with Jev 1.14 at 57.
- AINews reports TypeSafe passed $100M ARR at a $7.5B valuation three weeks after launch.

## Independent results

- Jev-as-a-judge paper: $0.044 per 1K judgments at 152 ms median, about 277x cheaper than GPT-6. Within 3 points on RewardBench and HaluEval, 14.5 points behind on JudgeBench. Escalating only low-confidence calls to GPT-6 Astra keeps 99% of accuracy at 57% of the cost.
- Vals: matched GPT-6 Astra's 97.5% on claim verification at about 1/500th the cost; ranked last on LegalBench.
- Cloudflare's own table: Jev leads Clef on When2Call and BRIGHT but trails on most other rows, at 524 ms median latency against Clef's 209 ms.
- A small-embedding-plus-logistic-regression baseline beat it on Banking77 (93.3% vs 83.2%).

## Weaknesses / caveats

- No public benchmarks from TypeSafe, so comparisons come from rivals and third parties that use different indices.
- Weaker and overconfident on knowledge and reasoning questions, per Artificial Analysis.
- Image input is not production-ready by TypeSafe's own label: the request format and limits may change between releases, and a Box question always returns a box, even when the target is absent, so it needs a companion yes/no question.

## Recent changes

- [2026-11-24] TypeSafe's docs now document experimental image input on Jev 1.13 and 1.14 and a new Box question type (Jev 1.14) that locates a target in an image; the "no image input" caveat is replaced.
- [2026-10-26] Used as the keep-or-drop engine in [fast-jev-compaction](../tools/fast-jev-compaction.md), a Claude Code plugin that prunes stale tool calls and results instead of summarizing context; it calls `jev-latest` and splits requests to stay under Jev's 32K request limit.
- [2026-10-17] Page created: launch (2026-09-15), pricing, independent results, and its fall to second on Artificial Analysis's Decision Index.

## Sources

- [Latent Space — Jev: System One models for Prod, not God (Diogo Almeida)](../sources/newsletters/latent-space-jev-diogo-almeida-2026-09-21.md)
- [Every — How to Get the Most Out of Jev](../sources/newsletters/every-how-to-get-most-out-of-jev-2026-09-23.md)
- [AINews — Jev as a judge, CLM, and the classifier critique](../sources/newsletters/ainews-jev-judge-clm-critique-2026-09-25.md)
- [Cloudflare — Introducing Clef decision models](../sources/articles/cloudflare-clef-decision-models-2026-10-02.md)
- [AINews — Decisions API beta, pplx-decider, and Vals on Jev](../sources/newsletters/ainews-decisions-api-beta-vals-jev-2026-10-07.md)
- [AINews — Decision models become a product category](../sources/newsletters/ainews-decision-models-product-category-2026-10-10.md)
- [AINews — Artificial Analysis launches a Decision Index](../sources/newsletters/ainews-aa-decision-index-2026-10-14.md)
- [AINews — Liquid d1-ultra tops the Decision Index; pplx-decider v1.2](../sources/newsletters/ainews-liquid-d1-ultra-pplx-decider-2026-10-17.md)
- [tamaratran/fast-jev-compaction (GitHub)](../sources/repos/tamaratran-fast-jev-compaction.md)
- [TypeSafe docs — Images](../sources/articles/typesafe-docs-images-2026-11-24.md)
- [TypeSafe docs — Use cases](../sources/articles/typesafe-docs-use-case-map-2026-11-23.md)
