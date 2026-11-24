---
title: Pi
type: tool
domains: [agents]
subcategory: agent-framework
tags: [agentic]
as_of: 2026-10-06
sources: [ainews-pi-10-pi-durable-2026-10-02, ainews-pi-durable-harness-rl-2026-10-06, latent-space-alex-zhang-rlm-2026-10-02, databricks-benchmarking-coding-agents-2026-07, anthropic-riemann-hypothesis-2026-08-11, flue-2-react-for-agents-2026-08-15, primeintellect-prime-agent-2026-08-05]
---

# Pi

Pi is an open-source minimal coding-agent harness, now developed under the company Earendil. It is the unopinionated base layer other projects build on ([Flue](flue.md), Prime Intellect's Prime Agent), and it keeps turning up as the cheapest harness in cost comparisons. Pi Durable is a sibling rewrite that turns the same loop into a crash-proof server process.

## Current status (as of 2026-10-06)

- **Pi 1.0 (October 2026):** "code mode" with native support for MCP, Jev and image models; extension support for virtual models; deferred tool loading; prompt-cache warming for Anthropic models; mid-conversation system messages that change prompts and tools based on the transcript; full-screen TUI by default.
- **Pi Durable:** a ~15K-line TypeScript port built on a small task-based workflow engine. Every step is a checkpointed task, so agents and subagents resume from their last state after a crash or restart. Pluggable storage (memory, SQLite, JSONL); runs on Node, Bun or Cloudflare Durable Objects; control is separated from local or remote execution environments.
- Pi Durable also runs parallel branching conversations in one harness, stores app state (such as a to-do list) beside the transcript so several users or UIs can watch and steer one agent, compacts old messages in the background, and hot-swaps tool and extension code mid-run. The authors skipped Effect.ts because it does not provide durability.
- **Cost evidence:** Databricks found the same model at the same effort cost more than 2x as much through Claude Code or Codex as through Pi, because Pi sent about 3x less context per turn; Composio found Pi the cheapest and best-performing of four harnesses running DeepSeek V4 Flash (both mid-2026).

## Why it matters

Pi is the reference point for the "thin harness" position: MIT's Alex Zhang uses it as his baseline because "all other harnesses are basically just Pi". Pi Durable is the clearest open-source example of the split described on [Agent runtime platforms](../concepts/agent-runtime-platforms.md), where the loop, its state and its execution environment become separately managed parts.

## Recent changes

- [2026-10-06] Pi Durable design details: ~15K lines of TypeScript, SQLite/JSONL storage, Bun or Cloudflare Durable Objects, control separated from execution.
- [2026-10-02] Pi 1.0 released (code mode, deferred tool loading, cache warming, mid-conversation system messages) alongside Pi Durable.

## Related

- [Flue](flue.md) — agent framework built on Pi
- [Harness vs model](../concepts/harness-vs-model.md) — the harness-swap measurements Pi appears in
- [Harness-model co-evolution](../concepts/harness-model-co-evolution.md) — HarnessTax cost gap and the same-loop dissent Pi appears in
- [Agent runtime platforms](../concepts/agent-runtime-platforms.md) — durable and cloud-native harnesses

## Sources

- [AINews — Pi 1.0 and Pi Durable](../sources/newsletters/ainews-pi-10-pi-durable-2026-10-02.md)
- [AINews — Pi Durable design and multi-harness RL](../sources/newsletters/ainews-pi-durable-harness-rl-2026-10-06.md)
- [Latent Space — Alex Zhang, MIT (RLMs and harnesses)](../sources/newsletters/latent-space-alex-zhang-rlm-2026-10-02.md)
- [Databricks — Benchmarking coding agents](../sources/articles/databricks-benchmarking-coding-agents-2026-07.md)
- [AINews — Anthropic's Riemann Hypothesis bound improvement (Composio harness bake-off)](../sources/newsletters/anthropic-riemann-hypothesis-2026-08-11.md)
- [Flue 2 — React for agents](../sources/newsletters/flue-2-react-for-agents-2026-08-15.md)
- [Prime Intellect — Prime Agent](../sources/tweets/primeintellect-prime-agent-2026-08-05.md)
