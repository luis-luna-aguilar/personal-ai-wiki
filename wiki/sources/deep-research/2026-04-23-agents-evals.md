---
title: Comprehensive operational framework for agentic AI evaluation
type: source
source_type: deep-research
source_file: raw/deep-research/2026-04-23 Agents Evals.md
published: 2026-04-23
ingested: 2026-04-24
domains: [agents, coding]
---

# Comprehensive operational framework for agentic AI evaluation

Deep-research synthesis covering eval design for coding agents and general workflow agents. It is useful as a map of patterns, benchmarks, and tooling, but should be treated as secondary synthesis rather than a canonical product or benchmark source.

## Influenced pages

- [Agent evals](../../concepts/agent-evals.md) — new concept page for agent eval taxonomy and the trajectory-vs-result distinction
- [Agent improvement loop](../../concepts/agent-improvement-loop.md) — adds eval suite hygiene guidance: trace mining, holdout sets, refresh cadence, and stale-test retirement
- [SWE-bench](../../benchmarks/swe-bench.md) — adds SWE-bench Verified contamination warning and reframes SWE-bench Pro as the more meaningful successor
- [SWE-PolyBench](../../benchmarks/swe-polybench.md) — adds methodology detail: 2,110 instances, 4 languages, execution plus CST metrics
- [OSWorld](../../benchmarks/osworld.md) — benchmark page for desktop computer-use evaluation across Ubuntu, Windows, and macOS
- [WebArena](../../benchmarks/webarena.md) — benchmark page for stateful web navigation agents
- [tau-bench](../../benchmarks/tau-bench.md) — benchmark page for conversational policy adherence and pass^k reliability
- [GAIA](../../benchmarks/gaia.md) — benchmark page for generalized multimodal agent capability
- [ToolBench](../../benchmarks/toolbench.md) — benchmark page for large-scale API-chaining and tool-use evaluation
- [Terminal-Bench](../../benchmarks/terminal-bench.md) — benchmark page for real CLI and system-administration tasks
- [Evals for agentic software development](../../training/evals-for-agentic-software-development.md) — main synthesis source for coding-agent eval patterns
- [Evals for workflow and task agents](../../training/evals-for-agentic-work.md) — main synthesis source for workflow-agent eval patterns
- [Company-wide AI enablement](../../training/company-wide-ai-enablement.md) — adds an autonomy ladder for eval-gated permission expansion across organization-wide agents
- [Anti-autopilot review friction](../../training/anti-autopilot-review-friction.md) — adds escalation evals as a design-time forcing function for human handoff boundaries
- [Braintrust](../../tools/braintrust.md) — lightweight tool page seeded from the report's trace-to-dataset workflow coverage
- [Promptfoo](../../tools/promptfoo.md) — lightweight tool page seeded from the report's assertion-based eval examples
- [Langfuse](../../tools/langfuse.md) — lightweight tool page seeded from the report's observability-tooling coverage

## Key claims extracted

- Agent evals should be split across capability, regression, trajectory, unit-level, and online/production categories
- Coding-agent evals should combine deterministic gates with agent-specific trajectory and judge-based checks
- Production traces should be mined back into regression datasets to prevent repeated failures
- Reliability for workflow agents should be measured across repeated runs rather than only one-shot success
- Braintrust, Promptfoo, and Langfuse are presented as notable tools for eval datasets, assertions, and observability
