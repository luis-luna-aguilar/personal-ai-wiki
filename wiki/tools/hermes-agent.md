---
title: Hermes Agent
type: tool
domains: [agents]
subcategory: agent-framework
tags: [nousresearch, open-source, agentic]
as_of: 2026-09-01
sources: [ainews-2026-04-21, ainews-2026-04-22, hermes-openclaw-persistent-agents-2026-05-11, ainews-openai-agi-bar-2026-08-28, ainews-fal-h3-max-live-2026-09-01, shannholmberg-hermes-agent-operator-2026-05-18]
---

# Hermes Agent

NousResearch's open-source autonomous agent framework. Reached 100K+ GitHub stars in under two months, overtaking OpenClaw in weekly star growth. Runs as a persistent background agent with multi-layer memory, self-created skills, and multi-agent coordination.

**GitHub:** [NousResearch/hermes-agent](https://github.com/nousresearch/hermes-agent)

## Current status (as of 2026-09-01)

- **v0.21.0 (2026-09-01) is the latest release noted:** Bots Mode, agent-to-agent communication, persistent multi-gateway connections, subagent steering, and roughly 50% lower default context usage (see section below); builds on the v0.10.0 baseline of 118 bundled skills, multi-layer memory, and six messaging integrations (Telegram, Discord, Slack, WhatsApp, Signal, CLI)
- 100K+ GitHub stars; Hermes Workspace V2, Browser Use integrations, Scarf macOS GUI
- **Brain + muscle architecture:** Hermes separates reasoning ("brain") from execution ("muscle") into two distinct AI layers — the brain plans and delegates; the muscle executes actions — rather than a single monolithic agent loop
- **Kanban supervision dashboard:** a visual project-management view showing active tasks, in-progress work, and completed items; designed for running multiple long-horizon workflows simultaneously
- **Weekly automated skill pruning:** Hermes audits its own skill library on a weekly cadence, removing skills that were created but never called; prevents skill bloat in long-running deployments
- **Who owns the agent's memory?** The newsletter frames this as the defining open question for the persistent-agent category: Hermes's local-first approach keeps memory in the user's environment
- **Real-session browsing (August 2026):** Hermes Agent can browse using a managed copy of the user's real Chrome profile and logins — a notable usability escalation for browser-use agents that also collapses auth friction, raising the importance of scoped-permission design at the harness layer

## Key orchestration patterns

Three mechanisms from community usage for multi-agent coordination:

1. **Stateless ephemeral units** — set `skip_memory=True, skip_context_files=True` on sub-agents to isolate them from shared state and enable parallelism without context bleed.
2. **LLM-driven replanning over failure metadata** — pass structured failure data (`status`, `exit_reason`, `tool_trace`) back to the orchestrator for corrected planning instead of blind retries.
3. **Directory-local context injection** — `AGENTS.md` / `.cursorrules` files are surfaced only through tool results, not pre-loaded into every context.

## Operating a Hermes fleet

A practitioner setup from Shann Holmberg, who ran a one-person marketing operation on Hermes in May 2026 (when Hermes had about 150K GitHub stars and 123 bundled skills):

- **Agent anatomy.** Each agent is a folder: `MEMORY.md` (stable business facts) and `USER.md` (stable facts about the user) are injected at session start, past sessions sit in a full-text-searchable SQLite store, `SOUL.md` sets the personality, and the skills library grows as the agent writes skills from real work. Several agents can share one brain with different souls.
- **Control room apart from runtime.** A docs-only folder governs the fleet (agents, permissions, referenced credentials, runbooks; no raw secrets), while each agent's live state runs in its own container. The tool-agnostic pattern is on [Multi-agent coordination](../workflows/multi-agent-coordination.md).
- **Four levels.** One agent; several specialists you talk to directly; an orchestrator as an optional front door that reads the control room to learn what exists and what needs approval, with a task bus to the specialists; then cron-scheduled work (weekly reports, health checks, backup checks). Prove the specialists before adding an orchestrator.
- **When to add an agent.** Only when the work needs its own credentials, its own long-term memory, or is a separate recurring role. One mega-agent holding every credential and memory loses isolation and clean revocation.
- **Grow workflows, don't write them.** Run a new workflow two or three times on real work so the agent writes the skill, tighten it in a separate workspace, and deploy it on a schedule once it survives a week unattended. Keep a sequential pipeline (his 21-step SEO flow) in one container so later steps keep what earlier steps decided.

## Compared to OpenClaw

OpenClaw reached 345K GitHub stars and integration with dozens of messaging apps, briefly outpacing Hermes in star count. In May 2026, a coordinated supply chain attack planted 341 malicious entries in the OpenClaw registry — Microsoft issued an enterprise warning recommending customers avoid OpenClaw on work machines while the incident was investigated. The attack moved to an independent foundation when the creator joined OpenAI.

Hermes's local-first memory architecture is often cited as an advantage in this context: memory stays in the user's environment rather than a centralized service.

Architectural framing remains: Hermes is a four-layer memory system with periodic consolidation vs OpenClaw's "context window + RAG" approach.

## v0.21.0 release (as of 2026-09-01)

Hermes Agent shipped a large feature release aimed at persistent, multi-agent workflows: Bots Mode, agent-to-agent communication, persistent multi-gateway connections, and subagent steering, plus broader connector access. A follow-up release note says the update also cut default context usage by roughly 50% — a concrete instance of context-efficiency becoming a first-class systems concern for the framework, alongside the [context-editing research](../concepts/agent-memory.md) (WikiSkill/SKILL.state, ContextPilot) from the same week.

## Recent changes

- [2026-09-01] v0.21.0 ships Bots Mode, agent-to-agent comms, persistent multi-gateway connections, subagent steering, broader connector access; cuts default context usage ~50%.
- [2026-08-29] Real-session browsing added: agent can browse using a managed copy of the user's real Chrome profile and logins.
- [2026-05-18] Practitioner fleet setup (Shann Holmberg): agent control room kept apart from each agent's runtime, four setup levels, new-agent test, prototype-to-production path.
- [2026-05-13] Brain+muscle architecture documented: reasoning and execution separated into two distinct AI layers; Kanban dashboard and weekly automated skill pruning described
- [2026-05-11] OpenClaw security incident: 341 malicious registry entries planted in coordinated supply chain attack; Microsoft enterprise warning issued
- [2026-04-22] Recursive spawn depth support added; Scarf macOS GUI launched; Skillkit native support
- [2026-04-21] 100K stars milestone; v0.10.0 ships 118 bundled skills; Kimi K2.6 and Qwen3.6 both cite Hermes as a day-0 launch partner

## Sources

- [AINews — Moonshot Kimi K2.6, Hermes Agent, Codex Chronicle (2026-04-21)](../sources/newsletters/ainews-2026-04-21.md)
- [AINews — 2026-04-22 (GPT-Image-2, Hermes, Deep Research Max)](../sources/newsletters/ainews-2026-04-22.md)
- [Persistent coding agents — Hermes architecture and OpenClaw security incident](../sources/newsletters/hermes-openclaw-persistent-agents-2026-05-11.md)
- [AINews — OpenAI to reach AGI bar by end-2026](../sources/newsletters/ainews-openai-agi-bar-2026-08-28.md)
- [AINews — Fal's H3 Max Live breaks the infinite videogen barrier](../sources/newsletters/ainews-fal-h3-max-live-2026-09-01.md)
- [Shann Holmberg on X — How to Become a Hermes Agent Operator](../sources/tweets/shannholmberg-hermes-agent-operator-2026-05-18.md)
