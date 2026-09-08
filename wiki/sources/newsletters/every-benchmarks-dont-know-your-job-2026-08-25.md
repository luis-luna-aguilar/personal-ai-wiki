---
title: Benchmarks Don't Know Your Job
type: source
source_type: newsletter
source_file: raw/newsletters/2026-08-25-benchmarks-dont-know-your-job.md
url: https://every.to/context-window/benchmarks-don-t-know-your-job
published: 2026-08-25
ingested: 2026-09-07
domains: [agents, training]
---

# Benchmarks Don't Know Your Job

Every's Context Window newsletter arguing companies need task-specific offline evals rather than public-benchmark comparisons to make AI buying decisions, using Every's own KateBench copyeditor as a worked example of a benchmark number that looked finished but wasn't, plus CentaurBench and Thinkingbox findings on reliability and helper-model selection.

## Influenced pages

- [Evals for workflow and task agents](../../training/evals-for-agentic-work.md) — new Evidence from practice and Recent changes sections

## Key claims extracted

- Mercor CEO Brendan Foody, Box CEO Aaron Levie: companies spend tens of millions on AI without offline evals (fixed real-task comparisons before live deployment)
- KateBench's 85-90% acceptance rate was inflated by a silent 40-suggestion cap that discarded suggestions past that point; acceptance rate is also noisy run-to-run
- CentaurBench: on 5 of 7 tasks, the model best at solo completion wasn't the best at improving a weaker model's first attempt
- Thinkingbox: strongest coding model's 65% single-attempt pass rate fell to 25% across 20 consecutive attempts
- Open-weight token share on Vercel's AI Gateway grew from 28% to 62% in two months (per Guillermo Rauch, cited in this piece)
- Legal-worker Codex adoption grew 108-fold since February (per Andreessen Horowitz "Charts of the Week," cited in this piece)
