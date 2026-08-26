---
title: FrontierCode
type: benchmark
domains: [coding]
tags: [cognition, benchmark]
as_of: 2026-06-29
sources: [ainews-frontiercode-june-2026, ainews-fable5-june-2026, cognitioncom-blog-devin-fusion]
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

## Why it matters

FrontierCode recalibrates what "good coding performance" means. A model that scores 80% on SWE-Bench Pro may still only produce mergeable code ~30% of the time on hard Diamond-tier tasks. This benchmark is now cited by Cognition and adopted by Anthropic as a primary launch benchmark for Fable 5.

The benchmark also serves as a feedback loop: Cognition integrates FrontierCode results into Devin's development, and good benchmarks are becoming training data targets rather than just static scoreboards.

## Recent changes

- [2026-06-29] Cognition introduced FrontierCode Extended (score + avg. cost/task) alongside Devin Fusion; Fusion+Fable5 leads the cost-adjusted comparison at 57.6/$3.00, while Fable5 alone scores marginally higher (57.0) at much higher cost ($5.12).
- [2026-06-09] Launched; Opus 4.8 scored ~13.4% on Diamond tier
- [2026-06-10] Fable 5 launched with 29.3% Diamond, Mythos 5 at 30.9%

## Sources

- [AINews — FrontierCode launch (June 9)](../sources/newsletters/ainews-frontiercode-june-2026.md)
- [AINews — Fable 5 FrontierCode Diamond score (June 10)](../sources/newsletters/ainews-fable5-june-2026.md)
- [Devin Fusion: Frontier Performance at 35% Lower Cost](../sources/articles/cognitioncom-blog-devin-fusion.md)
