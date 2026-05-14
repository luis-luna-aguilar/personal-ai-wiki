---
title: Hermes Agent
type: tool
domains: [agents]
subcategory: agent-framework
tags: [open-source, agentic]
as_of: 2026-05-13
sources: [ainews-2026-04-21, ainews-2026-04-22, hermes-openclaw-persistent-agents-2026-05-11]
---

# Hermes Agent

NousResearch's open-source autonomous agent framework. Reached 100K+ GitHub stars in under two months, overtaking OpenClaw in weekly star growth. Runs as a persistent background agent with multi-layer memory, self-created skills, and multi-agent coordination.

**GitHub:** [NousResearch/hermes-agent](https://github.com/nousresearch/hermes-agent)

## Current status (as of 2026-05-13)

- v0.10.0 baseline: 118 bundled skills, multi-layer memory, six messaging integrations (Telegram, Discord, Slack, WhatsApp, Signal, CLI)
- 100K+ GitHub stars; Hermes Workspace V2, Browser Use integrations, Scarf macOS GUI
- **Brain + muscle architecture:** Hermes separates reasoning ("brain") from execution ("muscle") into two distinct AI layers — the brain plans and delegates; the muscle executes actions — rather than a single monolithic agent loop
- **Kanban supervision dashboard:** a visual project-management view showing active tasks, in-progress work, and completed items; designed for running multiple long-horizon workflows simultaneously
- **Weekly automated skill pruning:** Hermes audits its own skill library on a weekly cadence, removing skills that were created but never called; prevents skill bloat in long-running deployments
- **Who owns the agent's memory?** The newsletter frames this as the defining open question for the persistent-agent category: Hermes's local-first approach keeps memory in the user's environment

## Key orchestration patterns

Three mechanisms from community usage for multi-agent coordination:

1. **Stateless ephemeral units** — set `skip_memory=True, skip_context_files=True` on sub-agents to isolate them from shared state and enable parallelism without context bleed.
2. **LLM-driven replanning over failure metadata** — pass structured failure data (`status`, `exit_reason`, `tool_trace`) back to the orchestrator for corrected planning instead of blind retries.
3. **Directory-local context injection** — `AGENTS.md` / `.cursorrules` files are surfaced only through tool results, not pre-loaded into every context.

## Compared to OpenClaw

OpenClaw reached 345K GitHub stars and integration with dozens of messaging apps, briefly outpacing Hermes in star count. In May 2026, a coordinated supply chain attack planted 341 malicious entries in the OpenClaw registry — Microsoft issued an enterprise warning recommending customers avoid OpenClaw on work machines while the incident was investigated. The attack moved to an independent foundation when the creator joined OpenAI.

Hermes's local-first memory architecture is often cited as an advantage in this context: memory stays in the user's environment rather than a centralized service.

Architectural framing remains: Hermes is a four-layer memory system with periodic consolidation vs OpenClaw's "context window + RAG" approach.

## Recent changes

- [2026-05-13] Brain+muscle architecture documented: reasoning and execution separated into two distinct AI layers; Kanban dashboard and weekly automated skill pruning described
- [2026-05-11] OpenClaw security incident: 341 malicious registry entries planted in coordinated supply chain attack; Microsoft enterprise warning issued
- [2026-04-22] Recursive spawn depth support added; Scarf macOS GUI launched; Skillkit native support
- [2026-04-21] 100K stars milestone; v0.10.0 ships 118 bundled skills; Kimi K2.6 and Qwen3.6 both cite Hermes as a day-0 launch partner

## Sources

- [AINews — Moonshot Kimi K2.6, Hermes Agent, Codex Chronicle (2026-04-21)](../sources/newsletters/ainews-2026-04-21.md)
- [AINews — 2026-04-22 (GPT-Image-2, Hermes, Deep Research Max)](../sources/newsletters/ainews-2026-04-22.md)
- [Persistent coding agents — Hermes architecture and OpenClaw security incident](../sources/newsletters/hermes-openclaw-persistent-agents-2026-05-11.md)
