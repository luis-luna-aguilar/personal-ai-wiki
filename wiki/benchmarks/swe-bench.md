---
title: SWE-bench
type: benchmark
domains: [coding, models]
tags: []
as_of: 2026-04-23
sources: [amazon-swe-polybench, kimi-k2-6-blog, ainews-2026-04-22, late-march-small-coding-models, agents-evals-deep-research]
---

# SWE-bench

SWE-bench is the de facto standard benchmark for evaluating AI software engineering capability on real GitHub issues. Models are scored on their ability to resolve issues in open-source Python repositories by generating a patch that passes the test suite.

## Variants

- **SWE-bench Verified** — a human-curated subset of ~500 tasks where the issue and test suite are confirmed to be well-formed; considered the most reliable variant
- **SWE-bench Pro / SWE-Pro** — harder task set with more complex multi-file and cross-repo issues
- **SWE-bench Multilingual** — extends the benchmark beyond Python to multiple programming languages

## Data contamination and SWE-bench Pro

SWE-bench Verified has faced a significant credibility problem: OpenAI explicitly deprecated their internal use of it due to severe data contamination. Models absorbed the evaluation repository code into their pre-training data, meaning high scores reflected memorization rather than autonomous problem-solving ability.

The successor addressing this is **SWE-bench Pro**, which evaluates against private, proprietary codebases and strictly copyleft-licensed repositories. SWE-bench Pro scores should be treated as the more meaningful measure of real engineering capability going forward.

**Practical implication:** When comparing agents on SWE-bench Verified, treat scores with skepticism, especially for models with large and recent pre-training corpora. SWE-bench Pro and SWE-bench Multilingual scores are better proxies for generalizable capability.

## Current leaderboard (as of 2026-04-23)

Scores are % of issues resolved. Higher is better.

| Model | Variant | Score | As of |
|---|---|---|---|
| [Qwen 3.6 27B](../models/qwen-3-6-27b.md) | SWE-bench Verified | 77.2% | 2026-04-23 |
| [Qwen 3.6 27B](../models/qwen-3-6-27b.md) | SWE-bench Pro | 53.5% | 2026-04-23 |
| [Composer 2](../models/composer-2.md) | SWE-bench Multilingual | 73.7% | 2026-03-23 |
| [MiniMax M2.7](../models/minimax-m2-7.md) | SWE-Pro | 56.22% | 2026-03-22 |
| [Kimi K2.6](../models/kimi-k2-6.md) | SWE-bench (various) | SOTA claims | 2026-04-22 |

*Note: claims are vendor-reported unless otherwise noted. Independent replication is not always available.*

## Why it matters

SWE-bench is the most widely cited benchmark for comparing coding model and coding agent performance. It provides a concrete proxy for whether a model can resolve real engineering problems, not just generate syntactically correct code.

## Caveats

- Results vary significantly depending on scaffolding (harness, tools, retry budget) — model scores and agent-system scores are not directly comparable
- Vendor-reported scores may not reflect reproducible independent runs
- Task distribution skews toward Python and well-maintained open-source repos; multilingual and brownfield enterprise work may behave differently
- See also [SWE-PolyBench](swe-polybench.md) for a multilingual extension of the SWE-bench idea from Amazon Science

## Recent changes

- [2026-04-24] Added contamination warning for SWE-bench Verified; reframed SWE-bench Pro as the more meaningful successor
- [2026-04-23] Page created; compiled leaderboard from model pages referencing SWE-bench scores

## Sources

- [Kimi K2.6 — Advancing Open-Source Coding](../sources/articles/kimi-k2-6-blog.md)
- [Late-March small coding models](../sources/newsletters/late-march-small-coding-models.md)
- [AINews — 2026-04-22 (GPT-Image-2, Hermes, Deep Research Max)](../sources/newsletters/ainews-2026-04-22.md)
- [Comprehensive operational framework for agentic AI evaluation](../sources/deep-research/2026-04-23-agents-evals.md)
