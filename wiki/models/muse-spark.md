---
title: Muse Spark
type: model
domains: [models, creative]
subcategory: frontier-model
tags: [closed-source, agentic, meta]
as_of: 2026-09-08
sources: [muse-spark, open-creative-workflows-2026-06, meta-muse-image-video-2026-07, superhuman-chatgpt-work-muse-spark-2026-07, the-code-databricks-coding-benchmark-2026-07-10, ainews-gpt-56-rollout-not-much-happened-2026-07-11, amd-acquires-taalas-2026-08-07, anthropic-riemann-hypothesis-2026-08-11, ainews-poolside-nvidia-2026-08-21, ainews-muse-spark-13-2026-09-03, ainews-navier-stokes-2026-09-09]
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

## Muse Spark 1.2 breaks into frontier benchmarks (as of 2026-08-07)

Muse Spark 1.2 moved from off-the-board to frontier-tier quickly. On the Vals Index, it entered the top 5 at $0.69/test — reportedly 3x cheaper than Kimi and 10x+ cheaper than Fable, Opus, and GPT-5.6 Sol — and became the first model to score above 60% on Finance Agent v2, at $0.77/test versus the prior #1 (Claude Opus 5) at $5.12/test and roughly half the latency. Artificial Analysis's v4.1.1 grading-update patch also gave Muse Spark 1.2 one of the largest score increases of any model that round.

Meta separately claimed gold-medal-level performance across five STEM Olympiads (APhO, IPhO — perfect theory scores — IMO, IChO, RMM), three submitted under live competition conditions and officially graded, using no external tools (no search, code execution, or calculator) and attributing part of the gain to multi-agent orchestration with parallel reasoning. The tool-free framing immediately fed into the ongoing "LLMs vs. harnesses vs. neurosymbolic" debate (François Chollet and others), since Meta's own explanation credits orchestration as much as raw model capability.

Further third-party numbers followed on 2026-08-21: Agent Arena reported a +2.1% net improvement (up from +0.9% in v1.1), with a particularly strong Bash Recovery gain of +11.4%, and DesignArena ranked it #1 for Video-to-Website, #2 for Image-to-HTML, and #3 for Image-to-Frontend, describing it as sitting on the price/quality Pareto frontier.

A smaller, architecturally distinct sibling, **Muse Glimmer** (30B dense, multimodal, Apache 2.0, designed for always-on local agents) shipped 2026-08-11 — see [Muse Glimmer](muse-glimmer.md). Alexandr Wang confirmed Muse Spark 1.2's own weights are coming "soon," a reversal from Spark 1.1's closed, metered-API-only launch.

## Muse Spark 1.3 closes the gap with GPT-5.6 Sol and Opus 5 (as of 2026-09-03)

Meta shipped Muse Spark 1.3, described by Meta's own team as the strongest model yet in the Spark line for agentic and coding work, with longer-horizon reliability and better complex-instruction compliance. Per Artificial Analysis Intelligence Index it now ranks #3 in the world, posting benchmark parity with GPT-5.6 Sol and Claude Opus 5 (not Fable) on several evals. Pricing discounts more than 90% for users who opt into allowing their data to be used for training.

Reddit commenters flagged a striking long-context claim (MRCR 512k–1m at 98.1%) and speculated the model is trillion-parameter scale — community reaction to a benchmark screenshot, not a Meta-confirmed spec. Open weights are promised "coming soon" but had not shipped as of this source, extending the "soon" timeline first given for Muse Spark 1.2's weights.

## Recent changes

- [2026-09-08] Muse Spark 1.3 now powers [Meta Muse](../tools/meta-muse.md), Meta's newly-launched consumer personal-agent product; day-one usage exceeded Meta's internal projections by 10x.
- [2026-09-03] Muse Spark 1.3 launches: AA Intelligence Index #3 in the world, parity with GPT-5.6 Sol/Opus 5 on several evals, 90%+ pricing discount for training opt-in, open weights still promised "coming soon."
- [2026-08-21] Additional third-party benchmarks: Agent Arena +2.1% net improvement (Bash Recovery +11.4%); DesignArena #1 Video-to-Website, #2 Image-to-HTML, #3 Image-to-Frontend.
- [2026-08-11] Muse Glimmer ships as a smaller, open-weight (Apache 2.0) sibling model; Muse Spark 1.2's own weights promised "soon" — a reversal from Spark 1.1's closed API-only launch.
- [2026-08-07] Muse Spark 1.2 breaks into frontier-tier benchmarks: Vals Index top 5 at $0.69/test, first model above 60% on Finance Agent v2, five STEM Olympiad gold-medal-level results under no-tool conditions.
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
- [AMD acquires Taalas](../sources/newsletters/amd-acquires-taalas-2026-08-07.md)
- [AINews — Anthropic's Riemann Hypothesis bound improvement](../sources/newsletters/anthropic-riemann-hypothesis-2026-08-11.md)
- [AINews — Poolside gets $12B reverse-execuhire to NVIDIA](../sources/newsletters/ainews-poolside-nvidia-2026-08-21.md)
- [AINews — OpenAI reports Navier-Stokes singularity find](../sources/newsletters/ainews-navier-stokes-2026-09-09.md)
