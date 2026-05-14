---
type: proposal
sources:
  - raw/newsletters/2026-05-13-supply-chain-attacks-keep-hitting-ai.md
  - raw/newsletters/2026-05-11-hermes-agent-is-the-next-big-thing-for-devs.md
status: pending
created: 2026-05-13
---

# Proposal: Persistent coding agents — Hermes Agent update + OpenClaw security incident

## Summary

Two updates to the persistent/always-on coding agent category. Hermes Agent (Nous Research) published a detailed architecture piece this week: "brain + muscle" separation (two distinct AI layers for reasoning vs. execution), a Kanban-style supervision dashboard, and weekly automated skill pruning. OpenClaw — the viral 345K-star rival framework — was hit by a coordinated supply chain attack planting 341 malicious entries in its registry, prompting a Microsoft enterprise warning.

## Intended changes

- [x] **Update** `wiki/tools/hermes-agent.md` — add brain+muscle architecture detail, Kanban dashboard, skill pruning, and OpenClaw incident; update `as_of` and `sources`
    > See diff snippets below

- [x] **Update** `wiki/state-of/agents.md` — add `Persistent coding agents` subcategory note and update Recent changes
    > See diff snippets below

- [x] **Create** `wiki/sources/newsletters/hermes-openclaw-persistent-agents-2026-05-11.md`
    > See draft below

## Page drafts

### wiki/tools/hermes-agent.md — diff snippets

**Frontmatter `as_of`:**
> **Before:** `as_of: 2026-04-22`
> **After:** `as_of: 2026-05-13`

**Frontmatter `sources` — append:**
> Add `hermes-openclaw-persistent-agents-2026-05-11`

**Current status — replace the existing `## Current status (as of 2026-04-22)` block:**

```markdown
## Current status (as of 2026-05-13)

- v0.10.0 baseline: 118 bundled skills, multi-layer memory, six messaging integrations (Telegram, Discord, Slack, WhatsApp, Signal, CLI)
- 100K+ GitHub stars; Hermes Workspace V2, Browser Use integrations, Scarf macOS GUI
- **Brain + muscle architecture:** Hermes separates reasoning ("brain") from execution ("muscle") into two distinct AI layers — the brain plans and delegates; the muscle executes actions — rather than a single monolithic agent loop
- **Kanban supervision dashboard:** a visual project-management view showing active tasks, in-progress work, and completed items; designed for running multiple long-horizon workflows simultaneously
- **Weekly automated skill pruning:** Hermes audits its own skill library on a weekly cadence, removing skills that were created but never called; prevents skill bloat in long-running deployments
- **Who owns the agent's memory?** The newsletter frames this as the defining open question for the persistent-agent category: Hermes's local-first approach keeps memory in the user's environment
```

**Replace `## Key orchestration patterns` section with an updated version:**

```markdown
## Key orchestration patterns

Three mechanisms from community usage for multi-agent coordination:

1. **Stateless ephemeral units** — set `skip_memory=True, skip_context_files=True` on sub-agents to isolate them from shared state and enable parallelism without context bleed.
2. **LLM-driven replanning over failure metadata** — pass structured failure data (`status`, `exit_reason`, `tool_trace`) back to the orchestrator for corrected planning instead of blind retries.
3. **Directory-local context injection** — `AGENTS.md` / `.cursorrules` files are surfaced only through tool results, not pre-loaded into every context.
```

**Replace `## Compared to OpenClaw` section:**

```markdown
## Compared to OpenClaw

OpenClaw reached 345K GitHub stars and integration with dozens of messaging apps, briefly outpacing Hermes in star count. In May 2026, a coordinated supply chain attack planted 341 malicious entries in the OpenClaw registry — Microsoft issued an enterprise warning recommending customers avoid OpenClaw on work machines while the incident was investigated. The attack moved to an independent foundation when the creator joined OpenAI.

Hermes's local-first memory architecture is often cited as an advantage in this context: memory stays in the user's environment rather than a centralized service.

Architectural framing remains: Hermes is a four-layer memory system with periodic consolidation vs OpenClaw's "context window + RAG" approach.
```

**Recent changes — prepend new entries:**
```
- [2026-05-13] Brain+muscle architecture documented: reasoning and execution separated into two distinct AI layers; Kanban dashboard and weekly automated skill pruning described
- [2026-05-11] OpenClaw security incident: 341 malicious registry entries planted in coordinated supply chain attack; Microsoft enterprise warning issued
- [2026-04-22] Recursive spawn depth support added; Scarf macOS GUI launched; Skillkit native support
- [2026-04-21] 100K stars milestone; v0.10.0 ships 118 bundled skills; Kimi K2.6 and Qwen3.6 both cite Hermes as a day-0 launch partner
```

### wiki/state-of/agents.md — diff snippets

**Frontmatter `as_of`:**
> **Before:** `as_of: 2026-05-05`
> **After:** `as_of: 2026-05-13`

**Frontmatter `sources` — append:**
> Add `hermes-openclaw-persistent-agents-2026-05-11`

**Add a new subcategory section between `### Agent frameworks` and `### Deep research tools`:**

```markdown
### Persistent coding agents

Always-on background coding services that maintain memory across months, can initiate contact (Telegram, Discord, etc.), and manage their own skill libraries. Distinct from session-scoped coding agents.

- [Hermes Agent](../tools/hermes-agent.md) — NousResearch; open-source; brain+muscle architecture (separate reasoning and execution layers); Kanban supervision dashboard; weekly automated skill pruning; local-first memory *(as of 2026-05-13)*
- **OpenClaw** — viral open-source framework (345K stars); deep messaging-app integrations; **security advisory (May 2026):** 341 malicious registry entries planted in coordinated attack; Microsoft recommends enterprise customers avoid on work machines *(as of 2026-05-13)*
```

**Recent changes — prepend:**
```
- [2026-05-13] Added `Persistent coding agents` subcategory: always-on agents with long-term memory, self-initiated contact, and self-pruning skill libraries; Hermes Agent and OpenClaw (with security advisory) are the first entries
- [2026-05-11] OpenClaw supply chain attack (341 malicious registry entries); Microsoft enterprise warning; reinforces the memory-ownership question for persistent-agent deployments
```

### wiki/sources/newsletters/hermes-openclaw-persistent-agents-2026-05-11.md (new)

```markdown
---
title: Persistent coding agents — Hermes architecture and OpenClaw security incident
type: source
source_type: newsletter
source_file: raw/newsletters/2026-05-11-hermes-agent-is-the-next-big-thing-for-devs.md
published: 2026-05-11
ingested: 2026-05-13
domains: [agents]
---

# Persistent coding agents — Hermes architecture and OpenClaw security incident

Two newsletters: "Hermes Agent Is the Next Big Thing for Devs" (May 11) and "Supply Chain Attacks Keep Hitting AI" (May 13). Combined because both address the persistent-agent category in the same week.

## Influenced pages

- [Hermes Agent](../../tools/hermes-agent.md) — brain+muscle architecture, Kanban dashboard, skill pruning, OpenClaw comparison updated
- [State of Agents](../../state-of/agents.md) — new `Persistent coding agents` subcategory added

## Key claims extracted

### Hermes Agent (May 2026 update)
- Brain + muscle architecture: two distinct AI layers — one for planning/reasoning, one for execution; not a single monolithic loop
- Kanban dashboard: visual supervision surface for multiple simultaneous long-horizon workflows
- Weekly automated skill pruning: Hermes audits and removes skills that were created but never invoked; prevents skill library bloat
- Framing from newsletter: "the defining question for persistent agents is who owns the memory"
- Hermes's local-first stance: memory stays in user's environment

### OpenClaw security incident (May 2026)
- Previous peak: 345K GitHub stars, integrations across dozens of messaging apps
- Attack: coordinated supply chain attack planted 341 malicious entries in the OpenClaw registry
- Response: creator joined OpenAI; project moved to an independent foundation
- Microsoft advisory: enterprise customers warned to avoid OpenClaw on work machines while incident is investigated
- This incident is covered more fully in the supply chain attacks proposal (see separate file)
```

