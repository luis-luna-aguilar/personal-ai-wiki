---
title: Muse Spark
type: model
domains: [models, creative]
subcategory: frontier-model
tags: [closed-source, agentic, meta]
as_of: 2026-07-09
sources: [muse-spark, open-creative-workflows-2026-06, meta-muse-image-video-2026-07, superhuman-chatgpt-work-muse-spark-2026-07, the-code-databricks-coding-benchmark-2026-07-10, ainews-gpt-56-rollout-not-much-happened-2026-07-11]
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

## Muse Image / Muse Video (as of 2026-07-08)

Meta Superintelligence Labs launched Muse Image inside Meta AI, Instagram Stories, and WhatsApp, with Facebook planned, and previewed Muse Video. Superhuman reports Muse Image reached #2 on Arena's text-to-image leaderboard behind GPT-Image-2.

The more important architecture signal is agentic generation: AINews describes Muse Image/Video as using planning, web search, tool use, code execution, and self-refinement before rendering, with Meta saying quality improves with scaled test-time compute.

## Muse Spark 1.1 — Meta's first paid model (as of 2026-07-09)

Meta shipped Muse Spark 1.1 on a new "Meta Model API" — the first Meta model with per-token pricing rather than open weights, a pivot from its usual Llama approach. Superhuman reports AI chief Alexandr Wang called the pricing "very aggressive and attractive" against other frontier models; the pivot lands as Wall Street pressures Meta to justify its AI infrastructure spend.

- Positioned for agentic tasks, coding, and computer use; 1M-token context window (per The Code)
- Pricing: $1.25 / $4.25 per million input/output tokens; median speed ~114 tok/s (per Artificial Analysis, via AINews)
- Artificial Analysis Intelligence Index: 51, up 8 points from Muse Spark 1.0 — roughly level with GLM-5.2/GPT-5.4/GPT-5.6 Luna, behind Grok 4.5/GPT-5.6 Sol/Claude Fable 5 (per Artificial Analysis, via AINews)
- Arena: #9 on Code Arena: Frontend, with reported strength in instruction-following and longer-query categories (per Artificial Analysis, via AINews)
- Meta's own claims (unverified independently): competitive with GPT-5.5 and Opus 4.8 on agentic evals; strong on Harvey's Legal Bench, TaxEval, and MedScribe (per Superhuman/AINews relaying Meta)

## Recent changes

- [2026-07-09] Muse Spark 1.1 launches on the new Meta Model API — Meta's first paid, metered model; AA Intelligence Index 51 (+8 vs 1.0); Arena #9 Code Arena: Frontend.
- [2026-07-08] Muse Image launches in Meta AI, Instagram Stories, and WhatsApp; Muse Video previewed; AINews describes an agentic planning/tool-use/self-refinement generation loop.
- [2026-06-24] Superhuman reports Meta Glasses launched with Muse Spark built in; secondary coverage only.
- [2026-04-10] Page created from Meta's Muse Spark introduction post

## Sources

- [Introducing Muse Spark: Scaling Towards Personal Superintelligence](../sources/articles/muse-spark.md)
- [Open creative workflows and vibe directing](../sources/newsletters/open-creative-workflows-2026-06.md)
- [Meta Muse Image and Muse Video](../sources/newsletters/meta-muse-image-video-2026-07.md)
- [Superhuman — ChatGPT gets a work-focused agent (Muse Spark 1.1)](../sources/newsletters/superhuman-chatgpt-work-muse-spark-2026-07.md)
- [The Code — Databricks' real-PR coding-agent cost benchmark (Muse Spark 1.1 detail)](../sources/newsletters/the-code-databricks-coding-benchmark-2026-07-10.md)
- [AINews — GPT-5.6 rollout, not much happened today (Muse Spark 1.1 benchmarks)](../sources/newsletters/ainews-gpt-56-rollout-not-much-happened-2026-07-11.md)
