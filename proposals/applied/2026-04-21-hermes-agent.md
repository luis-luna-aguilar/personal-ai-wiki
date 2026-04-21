---
type: proposal
sources:
  - raw/newsletters/2026-04-21-ainews-moonshot-kimi-k26-the-worlds-leading-o.md
status: pending
created: 2026-04-21
---

# Proposal: Hermes Agent — 100K Stars and Multi-Agent Orchestration Patterns

## Summary

NousResearch's Hermes Agent surpassed 100K GitHub stars in under two months, overtaking OpenClaw in weekly star growth. Beyond the milestone, AINews surfaced three practical multi-agent orchestration patterns from community usage that are directly relevant to the wiki's agents section: stateless ephemeral sub-agents for parallelism, LLM-driven replanning over structured failure metadata, and directory-local context injection.

## Intended changes

- [x] **Create** `wiki/tools/hermes-agent.md` — new tool page
    > See draft below

- [x] **Update** `wiki/state-of/agents.md` — add Hermes under `Agent orchestration`; bump `as_of`
    > **Frontmatter:** `as_of: 2026-04-21`, add `ainews-2026-04-21` to `sources:`
    >
    > **Under `### Agent orchestration`, add:**
    > ```
    > - [[tools/hermes-agent]] — NousResearch; open-source autonomous agent framework; 100K+ GitHub stars; four-layer memory with periodic consolidation; stateless sub-agent parallelism, LLM-driven replanning, directory-local context injection *(as of 2026-04-21)*
    > ```
    >
    > **Add to `## Recent changes` (prepend):**
    > ```
    > - [2026-04-21] Added [[tools/hermes-agent]] under `Agent orchestration`; 100K stars, substantive orchestration patterns from AINews breakdown
    > ```

- [x] **Update** `wiki/index.md` — add `[[tools/hermes-agent]]` under Tools; update page count
    > **Add under `## Tools`:**
    > ```
    > - [[tools/hermes-agent]] — NousResearch open-source agent framework; 100K+ stars; multi-layer memory, self-improving skills, stateless sub-agent parallelism *(as_of: 2026-04-21)*
    > ```

## Open questions

- Should the three orchestration patterns (stateless parallelism, failure metadata replanning, AGENTS.md injection) get their own `wiki/workflows/` page? They're practical enough to stand alone. Propose creating `wiki/workflows/hermes-orchestration-patterns.md` as a follow-on if you want depth here.
	-  let's give it its own space and keep it agnostic of the provider, like in workflows, but just agentic orchestration patterns. Let's keep track of them there and we can mention where they come from, but let's not close the door to adding in some other patterns

## Page drafts

### wiki/tools/hermes-agent.md (new)

````md
---
title: Hermes Agent
type: tool
domains: [agents, coding]
subcategory: agent-orchestration
tags: [open-source, agentic]
as_of: 2026-04-21
sources: [ainews-2026-04-21]
---

# Hermes Agent

NousResearch's open-source autonomous agent framework. Reached 100K+ GitHub stars in under two months, overtaking OpenClaw in weekly star growth. Runs as a persistent background agent with multi-layer memory, self-created skills, and multi-agent coordination.

**GitHub:** [NousResearch/hermes-agent](https://github.com/nousresearch/hermes-agent)

## Current status (as of 2026-04-21)

- v0.10.0 (April 16, 2026): 118 bundled skills, multi-layer memory, six messaging integrations (Telegram, Discord, Slack, WhatsApp, Signal, CLI)
- 100K+ GitHub stars in under two months — fastest-growing agent framework of 2026
- Native Ollama support; Copilot CLI integration via Ollama; cloud deployment templates
- Ecosystem: hermes-skill-factory, maestro, icarus-plugin, Hermes Workspace V2, Browser Use integrations
- Self-improving loop: creates reusable skills from experience (closed learning loop)

## Key orchestration patterns

Three mechanisms surfaced from community usage for multi-agent coordination:

1. **Stateless ephemeral units** — set `skip_memory=True, skip_context_files=True` on sub-agents to isolate them from shared state and enable true parallelism without context bleeding between agents
2. **LLM-driven replanning over failure metadata** — instead of blind retries, pass structured failure data (`status`, `exit_reason`, `tool_trace`) back to the orchestrator so it can generate a corrected plan rather than repeat the same failed approach
3. **Directory-local context injection** — `AGENTS.md` / `.cursorrules` files are surfaced only through tool results, not pre-loaded into every context; keeps context scoped to what each agent actually needs

## Compared to OpenClaw

Described as a four-layer memory system with periodic consolidation vs OpenClaw's "context window + RAG" approach. The broader framing: capability lives increasingly outside model weights — in memory systems, tools, protocols, and harnesses.

## Recent changes

- [2026-04-21] 100K stars milestone; v0.10.0 ships 118 bundled skills; Kimi K2.6 and Qwen3.6 both cite Hermes as day-0 launch partner

## Sources

- [[sources/newsletters/ainews-2026-04-21]]
````
