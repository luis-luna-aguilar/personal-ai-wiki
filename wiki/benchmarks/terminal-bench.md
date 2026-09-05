---
title: Terminal-Bench
type: benchmark
domains: [agents, coding]
tags: [agentic, cli]
as_of: 2026-05-21
sources: [agents-evals-deep-research, terminal-bench-science-announcement, ainews-erdos-benchmarks-cluster-2026-05-21]
---

# Terminal-Bench

Terminal-Bench evaluates agents on real-world multi-step tasks in isolated container environments, focusing on CLI-based system administration, compilation workflows, and debugging. It tests capabilities that are invisible in text-only benchmarks: navigating a real terminal, managing system state, and debugging through command-line tools.

## Current status (as of 2026-05-21)

- 89 hard, real-world multi-step tasks in isolated container environments
- Frontier models score below 65% (as reported; verify against current leaderboard)
- Tasks cover system administration, compilation, and CLI-based debugging
- Evaluates agents in real shell environments, not simulated inputs
- Terminal-Bench Science extension announced 2026-05-21: 100+ planned natural-science workflow tasks, contributions open (see section below)

## Why it matters

Terminal-Bench is relevant for evaluating terminal-first coding agents, DevOps and system administration agents, and any agent that must operate through a CLI rather than a GUI or structured API.

The reported sub-65% frontier score on tasks that a competent systems engineer would often handle routinely reveals a meaningful gap between chat-style capability and real operational autonomy.

## Terminal-Bench Science (as of 2026-05-21)

Terminal-Bench Science (TB-Science) extends the Terminal-Bench franchise from software-engineering tasks into real computational workflows from the natural sciences: life, physical, earth, mathematical, and engineering sciences. It targets 100+ tasks, each scientifically grounded (drawn from real research), objectively verifiable via deterministic pytest-based checks, and calibrated toward a 10-20% solve rate at release so tasks remain genuinely hard rather than saturated on day one. Tasks are contributed by practicing scientists through a Propose → Build → Review pipeline (Harbor Task Format), hosted by Stanford University and the Laude Institute, with contributor co-authorship on the resulting paper. Task contributions were open as of the announcement.

## Caveats

- The benchmark is relatively new and has a small task set (89 tasks); statistical noise may affect individual model comparisons
- Specific scores are from a research synthesis report (April 2026); verify against the Terminal-Bench site or paper
- Container environments may differ from real production environments in ways that affect generalization

## Open questions

- Does Terminal-Bench distinguish between task types (compilation vs. admin vs. debugging)? A per-category breakdown would be useful for evaluating specialized agents.

## Recent changes

- [2026-05-21] Terminal-Bench Science extension announced: 100+ planned tasks across five scientific domains, contributor-sourced via the Harbor Task Format, targeting a 10-20% solve rate at release.

## Sources

- [Comprehensive operational framework for agentic AI evaluation](../sources/deep-research/agents-evals-deep-research.md)
- [Terminal-Bench Science announcement](../sources/articles/terminal-bench-science-announcement.md)
- [AINews — agent-benchmark cluster (InferenceBench, Terminal-Bench Science, MINTEval)](../sources/newsletters/ainews-erdos-benchmarks-cluster-2026-05-21.md)
