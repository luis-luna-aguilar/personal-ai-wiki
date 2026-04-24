---
title: Terminal-Bench
type: benchmark
domains: [agents, coding]
tags: [agentic, cli]
as_of: 2026-04-23
sources: [agents-evals-deep-research]
---

# Terminal-Bench

Terminal-Bench evaluates agents on real-world multi-step tasks in isolated container environments, focusing on CLI-based system administration, compilation workflows, and debugging. It tests capabilities that are invisible in text-only benchmarks: navigating a real terminal, managing system state, and debugging through command-line tools.

## Current status (as of 2026-04-23)

- 89 hard, real-world multi-step tasks in isolated container environments
- Frontier models score below 65% (as reported; verify against current leaderboard)
- Tasks cover system administration, compilation, and CLI-based debugging
- Evaluates agents in real shell environments, not simulated inputs

## Why it matters

Terminal-Bench is relevant for evaluating terminal-first coding agents, DevOps and system administration agents, and any agent that must operate through a CLI rather than a GUI or structured API.

The reported sub-65% frontier score on tasks that a competent systems engineer would often handle routinely reveals a meaningful gap between chat-style capability and real operational autonomy.

## Caveats

- The benchmark is relatively new and has a small task set (89 tasks); statistical noise may affect individual model comparisons
- Specific scores are from a research synthesis report (April 2026); verify against the Terminal-Bench site or paper
- Container environments may differ from real production environments in ways that affect generalization

## Open questions

- Does Terminal-Bench distinguish between task types (compilation vs. admin vs. debugging)? A per-category breakdown would be useful for evaluating specialized agents.

## Sources

- [[sources/deep-research/2026-04-23-agents-evals]]
