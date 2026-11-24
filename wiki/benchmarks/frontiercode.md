---
title: FrontierCode
type: benchmark
domains: [coding]
tags: [cognition]
as_of: 2026-11-23
sources: [ainews-frontiercode-june-2026, ainews-fable5-june-2026, cognitioncom-blog-devin-fusion, the-code-spacexai-drops-grok-45-2026-07-09, openai-introducing-gpt-6-2-astra-sol, cognition-swe-2-2026-09-10]
---

# FrontierCode

FrontierCode is a coding benchmark released by Cognition (makers of Devin) in June 2026 that targets whether code is actually *mergeable* into a real production codebase — not just whether it passes unit tests. It was explicitly inspired by FrontierMath's approach of using saturation-resistant hard problems.

## What it measures

Standard coding benchmarks (SWE-bench-Verified, SWE-bench Pro) evaluate whether an agent's patch passes test suites. METR separately found that many SWE-bench-passing PRs would not actually be merged by maintainers. FrontierCode directly addresses this gap.

Evaluation dimensions per task:
- Regression safety
- Code cleanliness
- Scope adherence
- Test correctness
- Maintainability

Tasks were built in collaboration with open-source maintainers; each task took 40+ hours to construct. Benchmark design explicitly modeled on FrontierMath — focusing the hardest tier on problems that remain far from saturated.

## Tiers

FrontierCode has at least three tiers. The hardest public tier is **Diamond**.

## Current leaderboard (as of 2026-06-09)

| Model | FrontierCode Diamond |
|---|---|
| Claude Mythos 5 | 30.9% |
| Claude Fable 5 | 29.3% |
| Claude Opus 4.8 (prior best) | ~13.4% |

Pre-Fable 5: the best available model scored ~13.4% — well below the 50%+ scores common on SWE-bench-style evals. The gap signals that standard benchmarks overstate production-readiness.

## FrontierCode Extended (cost-aware, as of 2026-06-29)

Cognition also reports a separate "Extended" benchmark that pairs score with average cost per task, introduced alongside [Devin Fusion](../tools/devin.md):

| Configuration | Score | Avg. cost/task |
|---|---|---|
| Fusion + Fable 5* | 57.6 | $3.00 |
| Fable 5 (medium)* | 57.0 | $5.12 |
| Opus 4.8 (high) | 48.8 | $3.24 |
| Fusion | 47.9 | $2.38 |
| GPT-5.5 (high) | 44.8 | $3.64 |
| GLM-5.2 | 43.0 | $2.70 |

*Fable 5 access was suspended 2026-06-12 under a US government directive; the Fable 5 and Fusion+Fable 5 numbers reflect internal measurements taken before the suspension.

Scores here are not directly comparable to the Diamond-tier percentages above — Extended appears to be a distinct task set and scoring scale, introduced specifically to evaluate cost-aware multi-model harnesses like Devin Fusion.

## FrontierCode 1.1 (as of 2026-09-10)

Version 1.1 has a **Main** set (100 tasks, easy tasks excluded) and an **Extended** set (150 tasks). Scores are a weighted aggregate of rubric items; a solution that fails a blocking criterion scores 0, and cost is mean USD per rollout. Cognition's [SWE-2](../tools/devin.md) launch (2026-09-10) reported on Main:

| Model | FrontierCode 1.1 Main |
|---|---|
| GPT-6 Astra | 53.3% |
| Fable 5.1 | 50.9% |
| SWE-2 | 50.0% |
| Grok 4.6 | 48.0% |
| GPT-5.6 Sol | 47.5% |
| Kimi K3 | 44.2% |
| SWE-1.7 | 42.0% |

SWE-2 reached its score at 64% lower cost than Fable 5.1. Fusion results on 1.1 Extended are on the [Devin](../tools/devin.md) page. Version [2.0](#frontiercode-20-as-of-2026-11-23) has since appeared in OpenAI's GPT-6.2 launch.

## FrontierCode 2.0 (as of 2026-11-23)

OpenAI reports [GPT-6.2 Sol](../models/gpt-6-2-sol.md) within 0.5 points of [GPT-6.2 Astra](../models/gpt-6-2-astra.md) on Cognition's FrontierCode 2.0 at about a fifth of the cost, both at max effort. OpenAI describes 2.0 as testing whether changes to real codebases meet maintainers' standards for merging. No absolute scores were captured, and the post does not say how 2.0 relates to the Diamond and Extended results above.

## Why it matters

FrontierCode recalibrates what "good coding performance" means. A model that scores 80% on SWE-Bench Pro may still only produce mergeable code ~30% of the time on hard Diamond-tier tasks. This benchmark is now cited by Cognition and adopted by Anthropic as a primary launch benchmark for Fable 5.

The benchmark also serves as a feedback loop: Cognition integrates FrontierCode results into Devin's development, and good benchmarks are becoming training data targets rather than just static scoreboards.

## Recent changes

- [2026-11-23] FrontierCode 2.0 appears in OpenAI's GPT-6.2 launch: Sol within 0.5 points of Astra at about a fifth of the cost.
- [2026-09-10] FrontierCode 1.1 (Main 100 tasks, Extended 150) reported in Cognition's SWE-2 launch: GPT-6 Astra 53.3%, Fable 5.1 50.9%, SWE-2 50.0% on Main.
- [2026-07-09] Per The Code's recap, Cognition claims SWE-1.7 (Devin) matches GPT-5.5 within a point on FrontierCode at ~$2/task, with Opus 4.8 slightly ahead (secondhand, tier unspecified, no numeric score).
- [2026-06-29] Cognition introduced FrontierCode Extended (score + avg. cost/task) alongside Devin Fusion; Fusion+Fable5 leads the cost-adjusted comparison at 57.6/$3.00, while Fable5 alone scores marginally higher (57.0) at much higher cost ($5.12).
- [2026-06-10] Fable 5 launched with 29.3% Diamond, Mythos 5 at 30.9%
- [2026-06-09] Launched; Opus 4.8 scored ~13.4% on Diamond tier

## Sources

- [AINews — FrontierCode launch (June 9)](../sources/newsletters/ainews-frontiercode-june-2026.md)
- [AINews — Fable 5 FrontierCode Diamond score (June 10)](../sources/newsletters/ainews-fable5-june-2026.md)
- [Devin Fusion: Frontier Performance at 35% Lower Cost](../sources/articles/cognitioncom-blog-devin-fusion.md)
- [The Code - SpaceXAI drops Grok 4.5](../sources/newsletters/the-code-spacexai-drops-grok-45-2026-07-09.md)
- [OpenAI — Introducing GPT-6.2 Astra and Sol](../sources/articles/openai-introducing-gpt-6-2-astra-sol.md)
- [Cognition — Introducing SWE-2](../sources/articles/cognition-swe-2-2026-09-10.md)
