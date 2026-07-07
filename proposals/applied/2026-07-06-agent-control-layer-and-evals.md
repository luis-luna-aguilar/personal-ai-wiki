---
type: proposal
sources:
  - raw/newsletters/2026-07-03-aiewf-daily-dispatch-the-great-loops-debate-and-t.md
  - raw/newsletters/2026-07-02-ainews-not-much-happened-today.md
  - raw/tweets/2026-07-06-_avichawla-2073746091795960237.md
status: pending
created: 2026-07-06
---

# Proposal: Agent loops, live rollback, and eval infrastructure

## Summary

The approved agent-control topics point to the same operating problem: autonomous loops are useful, but teams still lack mature control layers, recovery primitives, and evaluation infrastructure. This proposal updates the orchestration, harness, and eval pages and adds Shepherd as a lightweight tool page for live agent checkpointing/rollback.

## Intended changes

- [x] **Update** `wiki/workflows/agentic-orchestration-patterns.md` - add control-layer-first loops, economic loop discipline, and live rollback/forking.
- [x] **Update** `wiki/concepts/harness.md` - add agent control layer and live-state recovery as harness concerns.
- [x] **Update** `wiki/concepts/agent-evals.md` - add agent eval infrastructure layer: Agent Arena, AA-AgentPerf, WorldModelGym, FLARE-AI.
- [x] **Create** `wiki/tools/shepherd.md` - Git-like rollback/forking for live agent runs.
- [x] **Create** source summaries:
    - `wiki/sources/newsletters/aiewf-loops-debate-2026-07-03.md`
    - `wiki/sources/tweets/shepherd-live-agent-rollback-2026-07-06.md`
- [x] **Update** `wiki/index.md` - add `tools/shepherd.md`.

## Page drafts

### wiki/workflows/agentic-orchestration-patterns.md (snippet)

```md
## Current patterns

- **Control layer before software factory.** The AI Engineer World Fair loops debate sharpened the current constraint: loops are already useful, but the field has not settled the control layer for permissions, cost ceilings, review bottlenecks, and recovery. Treat "software factory" as a destination, not a starting architecture.
- **Economic loop discipline.** Token usage is now a monitored production metric. Long-running loops should have task budgets, effort settings, stop conditions, and retry limits; teams cannot buy their way out of weak task decomposition with more tokens.
- **Live-state rollback and forking.** Tools such as Shepherd suggest a new primitive for agent work: checkpoint a run, rewind to a known-good state, fork an alternate trajectory, and keep the useful branch instead of restarting the whole session.

## Recent changes
- [2026-07-03] AI Engineer World Fair loop debate: agents are moving from hype to control-layer problems; surveys report widespread agent use but primitive controls and review bottlenecks.
- [2026-07-06] Shepherd proposal adds Git-like rollback/forking as a live-agent recovery primitive.
```

### wiki/concepts/harness.md (snippet)

```md
- **Control layer** - permissions, approvals, cost ceilings, stop conditions, recovery, and review routing around an agent loop. The 2026 AI Engineer Survey reported high agent adoption but primitive safeguards, making the control layer part of harness design rather than a product afterthought.
- **Live-run recovery** - checkpointing, rollback, and forking of agent state so a failed trajectory can be repaired without discarding all context.
```

### wiki/concepts/agent-evals.md (snippet)

```md
## Infrastructure layer (as of 2026-07-02)

Agent evaluation is splitting into several infrastructure problems:

- **Agent arenas** compare models or harnesses in agent mode, not only chat mode.
- **Systems efficiency metrics** such as AA-AgentPerf measure agents-per-megawatt, making inference and runtime efficiency part of agent evaluation.
- **World-model evals** such as WorldModelGym test whether a simulated world supports better decisions, not only plausible generations.
- **Incident reporting** efforts such as FLARE-AI aim to route AI flaws and safety incidents to the right developers and registries.

The pattern: evals are no longer only pass/fail task scores. They are becoming observability, incident intake, cost accounting, and system-capacity infrastructure.
```

### wiki/tools/shepherd.md (new)

```md
---
title: Shepherd
type: tool
domains: [agents, coding]
subcategory: agent-framework
tags: [open-source, agentic]
as_of: 2026-07-06
sources: [shepherd-live-agent-rollback-2026-07-06]
---

# Shepherd

Shepherd is an open-source tool described as Git-like version control for live AI agent runs. Its core idea is to let teams checkpoint, rollback, and fork agent trajectories while the agent is operating, rather than treating each run as an all-or-nothing transcript.

## Current status (as of 2026-07-06)
- Positioned around live agent recovery: save a run state, return to it, and branch from there.
- Relevant to long-running coding agents where a late bad decision can poison a session.
- Fits the broader shift from "loop forever" prompts toward explicit loop-control primitives.

## Strengths
- Makes failed or drifting agent trajectories easier to recover.
- Gives teams a concrete mental model: version-control semantics for agent state.

## Weaknesses / caveats
- Current source is a tweet-forward; fetch the repo or docs before applying any deep implementation claims.
- The wiki should treat it as an emerging tool, not a proven category leader.

## Recent changes
- [2026-07-06] Added as an emerging live-agent rollback/forking tool.

## Sources
- [Shepherd live agent rollback tweet](../sources/tweets/shepherd-live-agent-rollback-2026-07-06.md)
```

### Source summaries (new)

```md
---
title: AIEWF Daily Dispatch - loops debate
type: source
source_type: newsletter
source_file: raw/newsletters/2026-07-03-aiewf-daily-dispatch-the-great-loops-debate-and-t.md
published: 2026-07-03
ingested: 2026-07-06
domains: [agents, coding]
---

# AIEWF Daily Dispatch - loops debate

AINews summarizes the AI Engineer World Fair debate over autonomous loops and software factories, plus survey data showing high agent adoption but immature controls.

## Influenced pages
- [Agentic orchestration patterns](../../workflows/agentic-orchestration-patterns.md) - control-layer and loop discipline patterns
- [Harness](../../concepts/harness.md) - control layer as harness concern

## Key claims extracted
- Loops are useful but the discipline and controls lag the hype.
- AI costs regularly constrain ambitious agent use for many teams.
- Token usage is now a monitored production metric.
- Human approvals and permissions remain the dominant safeguards.
```

```md
---
title: Shepherd live agent rollback tweet
type: source
source_type: tweet
source_file: raw/tweets/2026-07-06-_avichawla-2073746091795960237.md
published: 2026-07-06
ingested: 2026-07-06
domains: [agents, coding]
---

# Shepherd live agent rollback tweet

Tweet-forward source describing Shepherd as Git-like version control for live AI agent runs, enabling rollback and forking of agent trajectories.

## Influenced pages
- [Shepherd](../../tools/shepherd.md) - new tool page
- [Agentic orchestration patterns](../../workflows/agentic-orchestration-patterns.md) - live-state rollback pattern

## Key claims extracted
- Shepherd offers checkpoint/rollback/fork semantics for live agent sessions.
- The tool targets recovery from bad agent trajectories without restarting from scratch.
```

## Open questions

- Shepherd should be verified against the actual repository before applying more than the lightweight emerging-tool page.
	- It comes from Stanford so lets accept the claim.
