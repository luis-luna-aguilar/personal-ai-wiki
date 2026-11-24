---
type: proposal
source: raw/articles/2026-11-23-claudecom-resources-articles-building-agents-when-to-fold-su.md
status: pending
created: 2026-11-24
---

# Proposal: Anthropic Applied AI — fold subagents back into one agent loop with skills and tool search

## Summary

### In short
For many enterprise agents, a subagent per team is now the problem, not the solution. Anthropic's Applied AI team reports that one agent with skills often beat both a single giant prompt and an orchestrator with specialist subagents on quality, often at lower cost and latency. One customer's single loop ran about twice as fast. The proposal adds a "Folding subagents into one loop" section to Agent loop design, with the target design, the 30–50 tool ceiling and the step-by-step migration. It also adds a pointer on Multi-agent coordination. The reason to hesitate is the date: the guide has none, so it is dated from the forward.

[[#Open questions|Open questions: none.]]

- [x] **Approve all** — checking this box approves every item in `## Intended changes` and `## Schema / vocabulary additions` below; the individual boxes may stay empty.

### The source
The source is a Claude guide, "Building agents: When to fold subagents into your main agent loop," from Anthropic's Applied AI team. It was forwarded around 24 October 2026. Subagents have their own context window, tools and instructions, and a coordinator directs them. The guide says they remain useful for verification, parallel work and separate permissions. But across enterprise deployments, the team kept seeing agents built the way the company is organized. Each team ships its own subagent and a platform team puts an orchestrator on top, which is Conway's law at work. The costs it names are subagent sprawl, a "Frankenprompt" where every team adds its own sentence to the system prompt, evals tuned to subtasks that nobody owns end to end, lossy handoffs, and added latency.

Its alternative is one model and one context window running an open tool loop. The harness sets turn and cost budgets and write gates. The model writes the plan and carries it out, so it can change course mid-task. Procedure moves into skills, which are loaded only when needed. Hard limits, approvals and per-user permissions move into tools that return refusals the model can read. Tools are grouped by user intent, because tool choice degrades past 30–50 definitions, and tool search loads them on demand. A small central team owns the system prompt and an end-to-end eval set, and 10 golden examples are enough to start.

Migration happens one subagent at a time, most-used and most tightly coupled first. The team then compares which tasks flipped, not only the total score, and runs each task more than once. In a sample support agent, one fold broke a working process in only one run out of two. Subagents stay only for context bloat, parallel throwaway contexts or tool-selection conflicts. Anthropic ships a migration kit and Claude API skills (`build-eval`, `prompt-audit`, `hillclimb`, `cost-optimize`), plus `/skill-doctor`.

### What changes
Agent loop design covers how one agent's loop is triggered, stopped and paced, but not when to merge several agents back into one. Multi-agent coordination describes how to split work and has no vendor guidance on undoing a split.

- **Agent loop design** gains the new section. One Recent-changes entry is added, and the page date moves from 9 September to 24 October.
- **Multi-agent coordination** gains a "fold before you split" bullet that points to it. Its Recent-changes list is at its cap, so the oldest entry (29 June, Sidekick) moves to history. The page date stays 18 November.
- The index line for Agent loop design names the new section.
- One new source page.

### What to weigh
The 24 October date comes from when the guide was forwarded, not from the page itself.

## Intended changes

- [ ] **Update** `wiki/workflows/agent-loop-design.md` — new `## Folding subagents into one loop` section after "Claude Code loop taxonomy"; one Related line; adds one Recent-changes entry dated 2026-10-24 at the top (list goes from 6 to 7, no spill); append source id and Sources line; `as_of` 2026-09-09 → 2026-10-24
    > See draft below

- [ ] **Update** `wiki/workflows/multi-agent-coordination.md` — one bullet added at the top of "Topology and routing"; adds one Recent-changes entry dated 2026-10-24, inserted between the 2026-11-18 and 2026-10-19 entries; append source id and Sources line; `as_of` stays 2026-11-18
    > See draft below

- [ ] **Spill** `wiki/workflows/multi-agent-coordination.md` → `wiki/history/workflows/multi-agent-coordination.md` — list is at its cap of 10, so the oldest entry (2026-06-29, Sidekick harness) spills
    > See draft below

- [ ] **Update** `wiki/index.md` — refresh the agent-loop-design description and date
    > See draft below

- [ ] **Create** `wiki/sources/articles/claude-fold-subagents-single-loop-2026-10.md` — source summary

## Page drafts

### wiki/workflows/agent-loop-design.md (updated)

Frontmatter: `as_of: 2026-09-09` → `as_of: 2026-10-24`; append `claude-fold-subagents-single-loop-2026-10` to `sources:`.

Insert after `## Claude Code loop taxonomy` (and its two closing paragraphs), before `## Where these patterns surfaced`:

```md
## Folding subagents into one loop

Anthropic's Applied AI team (October 2026) reports that across several enterprise deployments, a single agent with skills frequently beat both one big prompt and an orchestrator with specialist subagents on quality, often at lower cost and latency; one customer's single loop ran about 2x faster than its multi-agent harness. The failure it names is Conway's law: each team ships its own subagent, so the architecture copies the org chart. That brings subagent sprawl, a "Frankenprompt" of conflicting rules added by every team, subtask evals nobody owns end to end, and lossy handoffs.

The target design:

- One model and one context window run an open tool loop. The harness sets turn and cost budgets and write gates; the model batches tool calls, which run in parallel, and decides the next step from raw results.
- The model writes its plan on the first turn and revises it as results arrive, so the planner is also the executor.
- Procedure and ordering go into skills. Hard limits, approvals and per-user permissions go into tools, which return refusals or instructions the model can read. Group tools by user intent, since tool choice degrades past 30–50 definitions, and use tool search with deferred loading.
- One small central team owns the system prompt and an end-to-end eval set (10 golden examples are enough to start); each team ships small evals with its skills.

Migrate one subagent at a time, starting with the most-used, tightly coupled pairs, by turning its prompt into a skill and its API calls into tools. Compare which tasks flipped, not only the score, and run each task more than once: in Anthropic's sample support agent, one fold broke a working process in only one run of two. Keep a subagent only for measured context bloat, parallel throwaway contexts, or tool-selection conflicts, and split by context, not by problem type. Anthropic ships a migration kit, the `/claude-api build-eval`, `prompt-audit` (flags rules written for older models), `hillclimb` and `cost-optimize` skills, and `/skill-doctor` (cost and usage per skill).
```

Related: append:

```md
- [Automated harness optimization](../concepts/automated-harness-optimization.md) — `/claude-api hillclimb`, used to compare a folded subagent against the original
```

Recent changes: insert at the top:

```md
- [2026-10-24] Added "Folding subagents into one loop": Anthropic Applied AI's single-agent-with-skills design, the 30–50 tool ceiling with tool search, and one-at-a-time migration with flipped-task diffs.
```

Sources: append:

```md
- [Claude — Building agents: When to fold subagents into your main agent loop](../sources/articles/claude-fold-subagents-single-loop-2026-10.md)
```

### wiki/workflows/multi-agent-coordination.md (updated)

Frontmatter: append `claude-fold-subagents-single-loop-2026-10` to `sources:`. `as_of` unchanged.

Insert as the first bullet under `### Topology and routing`:

```md
- **Fold before you split.** Anthropic's Applied AI team finds that one agent with skills and tool search often beats orchestrator-plus-specialist designs in enterprise deployments. Keep subagents for context bloat, parallel throwaway contexts, or tool-selection conflicts, and divide them by context, not by problem type or owning team. The fold-back recipe is on [Agent loop design](agent-loop-design.md#folding-subagents-into-one-loop).
```

Recent changes: insert between the 2026-11-18 and 2026-10-19 entries:

```md
- [2026-10-24] Added "fold before you split": Anthropic Applied AI's case for folding subagents back into one loop, with the conditions for keeping them.
```

Remove the oldest entry (spilled, see below):

```md
- [2026-06-29] Added Sidekick multi-model harness pattern: persistent frontier + cheaper sidekick agents, cache-aware mid-session model switching at compaction boundaries; contrasted with per-call advisor/smart-friend escalation.
```

Sources: append:

```md
- [Claude — Building agents: When to fold subagents into your main agent loop](../sources/articles/claude-fold-subagents-single-loop-2026-10.md)
```

### wiki/history/workflows/multi-agent-coordination.md (updated)

Append at the end of the file:

```md

## Archived from current page on <apply date>

- [2026-06-29] Added Sidekick multi-model harness pattern: persistent frontier + cheaper sidekick agents, cache-aware mid-session model switching at compaction boundaries; contrasted with per-call advisor/smart-friend escalation.
```

### wiki/index.md (updated)

Replace the agent-loop-design line:

```md
- [workflows/agent-loop-design](workflows/agent-loop-design.md) — patterns for a single agent's own loop: loop-first design, the Claude Code loop-taxonomy table, tempo, stop criteria, the compound engineering loop, and folding subagents back into one loop (Anthropic Applied AI) *(as_of: 2026-10-24)*
```

### wiki/sources/articles/claude-fold-subagents-single-loop-2026-10.md (new)

```md
---
title: 'Claude — Building agents: When to fold subagents into your main agent loop'
type: source
source_type: article
source_file: raw/articles/2026-11-23-claudecom-resources-articles-building-agents-when-to-fold-su.md
url: https://claude.com/resources/articles/building-agents-when-to-fold-subagents-into-your-main-agent-loop
ingested: 2026-11-24
domains: [agents]
---

# Claude — Building agents: When to fold subagents into your main agent loop

Anthropic Applied AI guide arguing that many enterprise agents built as an orchestrator over team-owned specialist subagents do better as one agent loop with skills (progressive disclosure of procedure) and tool search (progressive disclosure of tools). It names the org-chart failure modes, describes the target single-loop design, and gives a staged migration: build a small end-to-end eval, fold subagents in one at a time, keep a subagent only when the folded version scores worse. The page carries no date; the wiki dates it 2026-10-24 from the forward.

## Influenced pages
- [Agent loop design](../../workflows/agent-loop-design.md) — new "Folding subagents into one loop" section
- [Multi-agent coordination](../../workflows/multi-agent-coordination.md) — "Fold before you split" bullet

## Key claims extracted
- Across several enterprise deployments, a single agent with skills frequently beat one-prompt and subagent designs on quality, often at lower cost and latency per task; one customer saw roughly 2x faster runtime
- One company's dozen specialist subagents made a consistent on-brand experience hard and added latency
- Org-chart failure modes: context management across agents, subagent sprawl, the Frankenprompt, unvetted localized evals, latency
- Keep subagents when there is measurable context-bloat degradation, parallel discardable contexts, or tool-selection / instruction conflicts
- Target loop: one model, one context, open tool loop with harness budgets and write gates; parallel tool batches; plan written and revised by the same model
- Skills hold procedure; tools hold hard limits, approvals, per-user permissions and mid-conversation lookups
- Tool choice tends to degrade past 30–50 tool definitions; group tools by user intent and use tool search with deferred loading
- Central team owns system prompt and end-to-end evals; 10 golden examples suffice to start; each team ships evals with its skills
- Fold by shared context starting with the most-used subagents; merge tightly coupled pairs; compare flipped tasks and run each task more than once
- Claude Code reduced its system prompt for advanced models by over 80%, partly through progressive disclosure
- Tooling: single-agent-loop migration kit; `/claude-api build-eval`, `prompt-audit`, `hillclimb`, `cost-optimize`; `/skill-creator`; `/skill-doctor`
```

## Schema / vocabulary additions

None.

## Open questions

None.
