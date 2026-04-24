---
title: Agentrial
type: tool
domains: [agents, coding]
subcategory: agent-eval-tooling
tags: [open-source, cli, agentic]
as_of: 2026-04-24
sources: [qa-tooling-for-software-agents-deep-research]
---

# Agentrial

Agentrial is an open-source statistical evaluation framework for AI agents. Its differentiator is that it treats single-run agent success as an unreliable signal and instead runs repeated trials, measures confidence intervals, and compares passing and failing trajectories to find where behavior diverges.

## Current status (as of 2026-04-24)

- Official README positions Agentrial as a local-first statistical eval framework for agents
- Supports multi-trial evaluations with Wilson confidence intervals
- Uses Fisher exact test for step-level failure attribution
- Supports CI-style regression detection and exits nonzero to block a pull request when reliability drops
- Focuses on consistency, cost, latency, and trajectory quality rather than only one-shot accuracy

## Strengths

- Makes agent reliability measurable instead of anecdotal
- Strong complement to existing benchmark and deterministic-test workflows
- Especially useful for coding agents and workflow agents where repeated-run consistency matters

## Weaknesses / caveats

- Claims about cost efficiency or composite scoring should be treated as tool-defined methodology, not universal eval standards
- The tool is strongest as a runner and analyzer; teams still need to supply meaningful tasks and assertions

## Sources

- [[sources/deep-research/2026-04-24-qa-tooling-for-software-agents]]
