---
title: Hermes Agent
type: tool
domains: [agents, coding]
subcategory: agent-orchestration
tags: [open-source, agentic]
as_of: 2026-04-22
sources: [ainews-2026-04-21, ainews-2026-04-22]
---

# Hermes Agent

NousResearch's open-source autonomous agent framework. Reached 100K+ GitHub stars in under two months, overtaking OpenClaw in weekly star growth. Runs as a persistent background agent with multi-layer memory, self-created skills, and multi-agent coordination.

**GitHub:** [NousResearch/hermes-agent](https://github.com/nousresearch/hermes-agent)

## Current status (as of 2026-04-22)

- v0.10.0 (April 16, 2026): 118 bundled skills, multi-layer memory, six messaging integrations (Telegram, Discord, Slack, WhatsApp, Signal, CLI)
- 100K+ GitHub stars in under two months; framed in AINews as one of the fastest-growing open agent frameworks of 2026
- Native Ollama support; Copilot CLI integration via Ollama; cloud deployment templates
- Ecosystem: hermes-skill-factory, maestro, icarus-plugin, Hermes Workspace V2, Browser Use integrations
- Self-improving loop: creates reusable skills from experience (closed learning loop)
- Recursive spawn depth now supported (in addition to spawn width) — enables deeper hierarchical decomposition of long-horizon tasks into nested subagent trees
- macOS GUI: Scarf — desktop interface for local Hermes workflows
- Skillkit native support added

## Key orchestration patterns

Three mechanisms surfaced from community usage for multi-agent coordination:

1. **Stateless ephemeral units** — set `skip_memory=True, skip_context_files=True` on sub-agents to isolate them from shared state and enable parallelism without context bleed.
2. **LLM-driven replanning over failure metadata** — instead of blind retries, pass structured failure data (`status`, `exit_reason`, `tool_trace`) back to the orchestrator so it can generate a corrected plan.
3. **Directory-local context injection** — `AGENTS.md` / `.cursorrules` files are surfaced only through tool results, not pre-loaded into every context, which keeps context scoped to what each agent actually needs.

## Compared to OpenClaw

Described as a four-layer memory system with periodic consolidation vs OpenClaw's "context window + RAG" approach. The broader framing: capability increasingly lives outside model weights, in memory systems, tools, protocols, and harnesses.

## Recent changes

- [2026-04-22] Recursive spawn depth support added; Scarf macOS GUI launched; Skillkit native support
- [2026-04-21] 100K stars milestone; v0.10.0 ships 118 bundled skills; Kimi K2.6 and Qwen3.6 both cite Hermes as a day-0 launch partner

## Sources

- [[sources/newsletters/ainews-2026-04-21]]
- [[sources/newsletters/ainews-2026-04-22]]
