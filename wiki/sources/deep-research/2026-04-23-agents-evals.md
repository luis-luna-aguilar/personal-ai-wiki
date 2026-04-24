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

- [[concepts/agent-improvement-loop]] — adds eval suite hygiene guidance: trace mining, holdout sets, refresh cadence, and stale-test retirement
- [[benchmarks/swe-bench]] — adds SWE-bench Verified contamination warning and reframes SWE-bench Pro as the more meaningful successor
- [[benchmarks/swe-polybench]] — adds methodology detail: 2,110 instances, 4 languages, execution plus CST metrics
- [[benchmarks/osworld]] — benchmark page for desktop computer-use evaluation across Ubuntu, Windows, and macOS
- [[benchmarks/webarena]] — benchmark page for stateful web navigation agents
- [[benchmarks/tau-bench]] — benchmark page for conversational policy adherence and pass^k reliability
- [[benchmarks/gaia]] — benchmark page for generalized multimodal agent capability
- [[benchmarks/toolbench]] — benchmark page for large-scale API-chaining and tool-use evaluation
- [[benchmarks/terminal-bench]] — benchmark page for real CLI and system-administration tasks
- [[training/evals-for-agentic-software-development]] — main synthesis source for coding-agent eval patterns
- [[training/evals-for-agentic-work]] — main synthesis source for workflow-agent eval patterns
- [[tools/braintrust]] — lightweight tool page seeded from the report's trace-to-dataset workflow coverage
- [[tools/promptfoo]] — lightweight tool page seeded from the report's assertion-based eval examples
- [[tools/langfuse]] — lightweight tool page seeded from the report's observability-tooling coverage

## Key claims extracted

- Agent evals should be split across capability, regression, trajectory, unit-level, and online/production categories
- Coding-agent evals should combine deterministic gates with agent-specific trajectory and judge-based checks
- Production traces should be mined back into regression datasets to prevent repeated failures
- Reliability for workflow agents should be measured across repeated runs rather than only one-shot success
- Braintrust, Promptfoo, and Langfuse are presented as notable tools for eval datasets, assertions, and observability
