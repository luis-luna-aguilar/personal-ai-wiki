---
title: Terminal-Bench
type: benchmark
domains: [agents, coding]
tags: [agentic, cli]
as_of: 2026-07-09
sources: [agents-evals-deep-research, terminal-bench-science-announcement, ainews-erdos-benchmarks-cluster-2026-05-21, ainews-fable5-june-2026, ainews-glm-52-june-2026, google-io-2026-search-blog, gpt-5-6-sol-preview-launch-2026-06, cohere-command-a-plus-launch]
---

# Terminal-Bench

Terminal-Bench evaluates agents on real-world multi-step tasks in isolated container environments, focusing on CLI-based system administration, compilation workflows, and debugging. It tests capabilities that are invisible in text-only benchmarks: navigating a real terminal, managing system state, and debugging through command-line tools.

## Current status (as of 2026-05-21)

- 89 hard, real-world multi-step tasks in isolated container environments
- Tasks cover system administration, compilation, and CLI-based debugging
- Evaluates agents in real shell environments, not simulated inputs
- Terminal-Bench Science extension announced 2026-05-21: 100+ planned natural-science workflow tasks, contributions open (see section below)

## Current leaderboard (as of 2026-07-09)

Terminal-Bench has multiple non-comparable variants (2.0, 2.1, Hard); scores below are grouped by variant and should only be compared within the same row group. All numbers are vendor-reported on the linked model/tool page unless noted.

| Model | Variant | Score | As of |
|---|---|---|---|
| [Claude Fable 5](../models/claude-fable-5.md) | 2.1 | 88.0% | 2026-07-02 |
| [GLM-5.2](../models/glm-5-2.md) | 2.1 | 81.0% | 2026-06-17 |
| [Gemini 3.5 Flash](../tools/gemini.md) | 2.1 | 76.2% | 2026-05-20 |
| GPT-5.6 Sol | 2.1 | OpenAI claims a new state of the art; exact score not recoverable from the launch post | 2026-07-09 |
| [MiniMax M3](../models/minimax-m3.md) | 2.1 | 66.0% | 2026-06-02 |
| [GPT-5.5](../models/gpt-5-5.md) | 2.0 | 82.7% | 2026-05-06 |
| [Qwen 3.6 27B](../models/qwen-3-6-27b.md) | 2.0 | 59.3% | 2026-05-01 |
| [Composer 2](../history/models/composer-2.md) (historical) | 2.0 | 61.7% | 2026-03-23 |
| [Claude Opus 4.8](../history/models/claude-opus-4-8.md) (historical, superseded by [Claude Opus 5](../models/claude-opus-5.md)) | Hard | gains reported; no exact score published | 2026-06-04 |
| [Cohere Command A+](../models/cohere-command-a-plus.md) | Hard | 3% → 25% (vs. Command A Reasoning) | 2026-05-21 |

## Why it matters

Terminal-Bench is relevant for evaluating terminal-first coding agents, DevOps and system administration agents, and any agent that must operate through a CLI rather than a GUI or structured API.

Even the strongest frontier scores (Fable 5 at 88.0% on the 2.1 variant) leave meaningful room short of full reliability on tasks that a competent systems engineer would often handle routinely — a gap between chat-style capability and real operational autonomy that has narrowed since this page's original April synthesis but hasn't closed.

## Terminal-Bench Science (as of 2026-05-21)

Terminal-Bench Science (TB-Science) extends the Terminal-Bench franchise from software-engineering tasks into real computational workflows from the natural sciences: life, physical, earth, mathematical, and engineering sciences. It targets 100+ tasks, each scientifically grounded (drawn from real research), objectively verifiable via deterministic pytest-based checks, and calibrated toward a 10-20% solve rate at release so tasks remain genuinely hard rather than saturated on day one. Tasks are contributed by practicing scientists through a Propose → Build → Review pipeline (Harbor Task Format), hosted by Stanford University and the Laude Institute, with contributor co-authorship on the resulting paper. Task contributions were open as of the announcement.

## Caveats

- The benchmark is relatively new and has a small task set (89 tasks); statistical noise may affect individual model comparisons
- Specific scores are from a research synthesis report (April 2026); verify against the Terminal-Bench site or paper
- Container environments may differ from real production environments in ways that affect generalization

## Open questions

- Does Terminal-Bench distinguish between task types (compilation vs. admin vs. debugging)? A per-category breakdown would be useful for evaluating specialized agents.

## Recent changes

- [2026-09-06] Repointed Claude Opus 4.8 to its archived page after Claude Opus 5 superseded it; score unchanged, link/label fix only.
- [2026-07-09] Rebuilt the current-leaderboard section from model pages already citing Terminal-Bench scores, replacing the stale "frontier models below 65%" line with a table grouped by variant (2.0/2.1/Hard).
- [2026-05-21] Terminal-Bench Science extension announced: 100+ planned tasks across five scientific domains, contributor-sourced via the Harbor Task Format, targeting a 10-20% solve rate at release.

## Sources

- [Comprehensive operational framework for agentic AI evaluation](../sources/deep-research/agents-evals-deep-research.md)
- [Terminal-Bench Science announcement](../sources/articles/terminal-bench-science-announcement.md)
- [AINews — agent-benchmark cluster (InferenceBench, Terminal-Bench Science, MINTEval)](../sources/newsletters/ainews-erdos-benchmarks-cluster-2026-05-21.md)
- [AINews — Fable 5 returns](../sources/newsletters/ainews-fable5-june-2026.md)
- [AINews — GLM-5.2](../sources/newsletters/ainews-glm-52-june-2026.md)
- [Google I/O 2026 — Search blog](../sources/articles/google-io-2026-search-blog.md)
- [OpenAI — Previewing GPT-5.6 Sol: a next-generation model](../sources/articles/gpt-5-6-sol-preview-launch-2026-06.md)
- [Introducing Command A+](../sources/articles/cohere-command-a-plus-launch.md)
