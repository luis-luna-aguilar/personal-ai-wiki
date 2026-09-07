---
title: "The Code — Databricks' real-PR coding-agent cost benchmark"
type: source
source_type: newsletter
source_file: raw/newsletters/2026-07-10-gpt-56-beats-fable-5-on-coding.md
url: https://codenewsletter.ai/p/openai-unveils-gpt-5-6-meta-debuts-its-first-paid-ai-model
published: 2026-07-10
ingested: 2026-09-06
domains: [training, coding]
---

# The Code — Databricks' real-PR coding-agent cost benchmark

The Code's July 10 "Insight" section covers a Databricks benchmark built from real pull requests completed in Databricks' own multi-million-line codebase, graded against the original PRs' tests. This newsletter recap named Claude Code and Pi only as examples of what a harness is, without saying which was cheaper in the actual comparison — that detail was confirmed by fetching Databricks' own primary post directly (see [the companion source page](../articles/databricks-benchmarking-coding-agents-2026-07.md)): Pi was the more efficient harness on this workload. This same issue's lead item covered GPT-5.6's coding benchmarks (handled elsewhere) and also carried a shorter item on Meta's Muse Spark 1.1 launch, used here for that model page.

## Influenced pages

- [Cost-aware AI task routing](../../training/cost-aware-ai-task-routing.md) — added a new evidence bullet citing all three findings
- [Muse Spark](../../models/muse-spark.md) — Muse Spark 1.1 specs and positioning

## Key claims extracted

- Databricks graded coding agents on real PRs from its own codebase using the original PR's tests as the grader — a private, uncontaminated benchmark
- Open-source GLM 5.2 performed as well as Claude Opus 4.8 while costing about 30% less per task
- The same model run through different harnesses can double the cost with no meaningful quality change; the efficient harness sent less context per turn and needed fewer runs (this newsletter did not name which harness was cheaper — see the primary source for that detail)
- In this benchmark, Sonnet 5 cost $2.09 per completed task and Opus 4.8 cost $1.94, despite Sonnet's lower per-token pricing, because Sonnet took longer and re-read more context
- Databricks argues teams' own merged PRs (with passing tests) are an untapped, model-agnostic eval source; the post outlines a method: pick the right PRs, rewrite their intent into prompts, hold out the tests for scoring
- Muse Spark 1.1 shipped alongside the Meta Model API, moving Meta from open-weight Llama releases to hosted, per-token pricing
- Built for long agentic tasks: plans across parallel subagents and manages a 1M-token context window
- Positioned to help "big projects finish faster"
