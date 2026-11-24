---
type: proposal
source: raw/articles/2026-11-23-vercelcom-blog-introducing-vercel-board.md
status: pending
created: 2026-11-23
---

# Proposal: Vercel Board

## Summary

### In short
Coordinating many agents now needs its own shared task board rather than each agent's Markdown notes. Vercel turned that into an experimental product, Vercel Board. Agents from different tools claim tasks under time-limited leases, wait on dependencies, post schema-checked findings and sync with Slack and GitHub, all under per-board access rules. Vercel says the v0 software factory it rebuilt on Board now merges over half of v0's pull requests. The proposal adds a tool page, a leader line on State of Agents and one pattern on Multi-agent coordination. One reason to hesitate: Board is experimental, and the code samples in the fetched copy are cut off.

[[#Open questions|Open questions: 1 to answer.]]

- [x] **Approve all** — checking this box approves every item in `## Intended changes` and `## Schema / vocabulary additions` below; the individual boxes may stay empty.

### The source
On 18 November 2026 Vercel published "Introducing Vercel Board". It opens with a claim about where the field is going: development is moving from one agent doing one task to teams of agents on larger projects, and a single agent can track its own work in a Markdown file, but nothing purpose-built tracks tasks, delegation, status, logs and finished work across many agents and subagents. Vercel says it hit this problem on two internal projects. The first was a swarm of security agents that scan its codebases and push fixes. The second was v0's software factory, which Vercel rebuilt on Board and which now merges more than half of v0's pull requests.

Board is "headless": there is no app of its own. It is a message store that agents read and write through a CLI or a JavaScript SDK, with an installable skill that teaches an agent how to use it. Each board has channels and threads, with labels for details such as a PR link or status. An agent claims a ready task under a lease (a time limit it must renew), posts updates and completes the task with its result. Tasks can depend on each other, so a review opens only when its fix is done. "Watchers" wake an agent when a reply or label changes, and on Vercel's hosting that wakes a deployment, so no process has to stay running. Agents can also schedule their own follow-ups, such as "check CI in five minutes". Messages can carry schema-checked structured data, replies sync both ways with Slack and GitHub, and per-board grants control who may read or post, with every event recording who acted. Vercel names Claude Code, Codex, Pi, OpenCode, eve, Mastra and LangChain among the harnesses that can share one board. The page's animated demo is scripted: Vercel says no models ran and the people and results are illustrative.

### What changes
The wiki already covers agent-board products (Multica, Paperclip) and coordination patterns such as the shared memory-repo workspace, but nothing from Vercel on coordination.

- New page `tools/vercel-board.md`: what Board is, the claim/lease/dependency loop, sync, grants and the v0 figure, with the experimental status as a caveat.
- **State of Agents** gains a Board line under Agent orchestration and a Recent-changes entry. The oldest entry (Pi 1.0, 6 October) moves to history because the list is full. Page date moves to 18 November.
- **Multi-agent coordination** gains one Coordination-mechanics pattern, a shared task board as the coordination layer, contrasted with the memory-repo workspace already there. Its oldest Recent-changes entry (the control-room pattern, 18 May) moves to a new history file. Page date moves to 18 November.
- One new source page for the launch post.

### What to weigh
The fetched copy cuts every code sample short (route handlers, the sync setup and the sandbox example show only a few lines). The drafts describe what those samples do from the surrounding prose and do not quote API details beyond the full CLI lines. The page also calls Board a fit for "multi-agent reinforcement learning" without explaining it, so the drafts leave that out. v0's factory is kept on the tool page rather than added to Software factory. The open question asks whether it belongs there too.

## Intended changes

- [ ] **Create** `wiki/tools/vercel-board.md` — new tool page, subcategory `agent-orchestration`
    > See draft below

- [ ] **Update** `wiki/state-of/agents.md` — add Vercel Board leader line under Agent orchestration; adds one Recent-changes entry dated 2026-11-18; `as_of` 2026-10-28 → 2026-11-18; append source id `vercel-board-launch-2026-11-18`
    > See draft below

- [ ] **Spill** `wiki/state-of/agents.md` → `wiki/history/state-of/agents.md` — list is at the cap of 10; the oldest entry (2026-10-06, Pi) moves to history
    > See draft below

- [ ] **Update** `wiki/workflows/multi-agent-coordination.md` — add the "Shared task board" bullet at the end of Coordination mechanics; adds one Recent-changes entry dated 2026-11-18; one Related line; one Sources line; `as_of` 2026-10-13 → 2026-11-18; append source id
    > See draft below

- [ ] **Spill** `wiki/workflows/multi-agent-coordination.md` → `wiki/history/workflows/multi-agent-coordination.md` — list is at the cap of 10; the oldest entry (2026-05-18, control room) moves to a new history file
    > See draft below

- [ ] **Create** `wiki/sources/articles/vercel-board-launch-2026-11-18.md` — source summary

- [ ] **Update** `wiki/index.md` — add the new tool page under Tools; tool count +1

## Page drafts

### wiki/tools/vercel-board.md (new)

```md
---
title: Vercel Board
type: tool
domains: [agents, coding]
subcategory: agent-orchestration
tags: [agentic, collaboration, cli, beta]
as_of: 2026-11-18
sources: [vercel-board-launch-2026-11-18]
---

# Vercel Board

Vercel's experimental coordination primitive for fleets of agents: a headless message store and task board that agents from different harnesses read and write through a CLI (`vercel board`) or the `@vercel/board` JavaScript SDK. It replaces the per-agent Markdown task file with shared channels, threads and tasks that people and agents both see.

**Docs:** [vercel.com/docs/board](https://vercel.com/docs/board)

## Current status (as of 2026-11-18)

- Launched 2026-11-18 as an experimental primitive; installable agent skill via `npx skills add vercel/board`.
- Task loop: an agent claims a ready task (filtered by label), holds it under a renewable lease, posts updates and completes it with a result such as a PR link. Tasks can depend on other tasks, so a review opens only after its fix lands.
- Watchers wake an agent when a reply arrives or a label changes; on Vercel the event wakes the deployment, so nothing runs between events. Agents can schedule their own follow-ups (`vercel board schedule`, for example "check CI in 5 minutes").
- Two-way sync with Slack and GitHub mirrors replies, reactions, edits and deletions; `--no-sync` keeps internal notes on Board only. Messages can carry structured data validated against a versioned schema (for example `security-finding@1`).
- Grants set access per board for users, projects and environments; every event records who acted. Vercel Sandbox sessions get scoped board access with no credential inside the sandbox.
- Harness-agnostic: Vercel names [Claude Code](claude-code.md), [Codex](codex.md), [Pi](pi.md), OpenCode, [eve](eve.md), [Mastra](mastra.md) and [LangChain](langchain-langsmith.md) as able to share one board.

## Evidence from Vercel

- Runs Vercel's internal security-agent swarm, which scans its codebases and pushes fixes.
- v0's software factory was rebuilt on Board and now merges over 50% of v0's PRs.
- Ships two templates: a Slack-connected factory (bug report in Slack → agent task → GitHub PR) and a swarm backlog for parallel work such as codebase migrations.

## Weaknesses / caveats

- Experimental; no pricing or stability commitments in the launch post.
- The launch demo is a scripted board run; Vercel says no models ran and the people, agents and results are illustrative.
- Watchers waking a deployment is a Vercel-hosting feature; elsewhere an agent process has to listen.

## Related

- [Multi-agent coordination](../workflows/multi-agent-coordination.md) — the shared-task-board pattern Board implements
- [Multica](multica.md) and [Paperclip](paperclip.md) — agent-board products with their own UI, where Board is headless

## Recent changes

- [2026-11-18] Page created: Vercel Board launched as an experimental agent-coordination primitive.

## Sources

- [Vercel — Introducing Vercel Board](../sources/articles/vercel-board-launch-2026-11-18.md)
```

### wiki/state-of/agents.md (updated)

Frontmatter: `as_of: 2026-10-28` → `as_of: 2026-11-18`; append `vercel-board-launch-2026-11-18` to `sources:`.

Agent orchestration — insert after the Paperclip line:

```md
- [Vercel Board](../tools/vercel-board.md) — Vercel; experimental headless task board for agent fleets across harnesses: claims with leases, task dependencies, watchers, Slack/GitHub two-way sync, per-board grants; v0's factory on it merges over 50% of PRs *(as of 2026-11-18)*
```

Recent changes — insert at the top (newest first), then drop the 2026-10-06 Pi entry (spilled below):

```md
- [2026-11-18] Added [Vercel Board](../tools/vercel-board.md) to Agent orchestration: Vercel's experimental headless coordination layer where agents from different harnesses claim leased tasks, wait on dependencies and sync with Slack and GitHub.
```

### wiki/history/state-of/agents.md (updated)

Append at the end of the file:

```md
## Archived from current page on 2026-11-23

- [2026-10-06] Added [Pi](../../tools/pi.md) to Agent frameworks: Pi 1.0 and Pi Durable (checkpointed, crash-resuming harness on Bun or Cloudflare Durable Objects).
```

(If a `## Archived from current page on 2026-11-23` header already ends the file at apply time, append the entry under it instead of opening a new block.)

### wiki/workflows/multi-agent-coordination.md (updated)

Frontmatter: `as_of: 2026-10-13` → `as_of: 2026-11-18`; append `vercel-board-launch-2026-11-18` to `sources:`.

Coordination mechanics — append after the "Control room apart from runtime" bullet:

```md
- **Shared task board as the coordination layer.** When many agents across machines and harnesses work one backlog, give them a shared board instead of per-agent Markdown task files: an agent claims a ready task under a lease it must renew, so a stalled agent's work frees itself; tasks declare dependencies, so a review becomes claimable only when its fix completes while independent fixes run in parallel; and replies or label changes wake the agent that owns the thread. The board also holds the original report, findings and PR together, so another agent or a person can review the work, and it syncs with the Slack and GitHub threads people already use. Unlike the memory-repo workspace above, which lets writes collide and settles them at push time, the board assigns ownership before work starts. [Vercel Board](../tools/vercel-board.md) is the first packaged instance; Vercel runs its security-agent swarm and v0's software factory on it. *Source: Vercel (2026-11-18)*
```

Recent changes — insert below the 2026-11-23 split entry (date order, newest first), then drop the 2026-05-18 control-room entry (spilled below):

```md
- [2026-11-18] Added the shared-task-board pattern (leased claims, task dependencies, event watchers, sync with Slack and GitHub) with Vercel Board as its first packaged instance.
```

Related — append:

```md
- [Vercel Board](../tools/vercel-board.md) — packaged shared task board for agent fleets across harnesses
```

Sources — append:

```md
- [Vercel — Introducing Vercel Board](../sources/articles/vercel-board-launch-2026-11-18.md)
```

### wiki/history/workflows/multi-agent-coordination.md (new)

```md
# Multi-agent coordination — history

## Archived from current page on 2026-11-23

- [2026-05-18] Added the control-room pattern (docs-only fleet governance an orchestrator reads, kept apart from each agent's secrets and live state) from Shann Holmberg's Hermes Agent fleet.
```

### wiki/sources/articles/vercel-board-launch-2026-11-18.md (new)

```md
---
title: Vercel — Introducing Vercel Board
type: source
source_type: article
source_file: raw/articles/2026-11-23-vercelcom-blog-introducing-vercel-board.md
url: https://vercel.com/blog/introducing-vercel-board
published: 2026-11-18
ingested: 2026-11-23
domains: [agents, coding]
---

# Vercel — Introducing Vercel Board

Vercel's launch post for Board, an experimental headless message store and task board for coordinating agents and people across harnesses. Vercel built it for two internal projects, a security-agent swarm and v0's software factory, and now offers it through a CLI, a JavaScript SDK and an installable agent skill. The post walks through task claims with leases, dependencies, watchers, self-scheduled follow-ups, schema-validated structured messages, two-way Slack/GitHub sync, per-board grants and credential-free Sandbox access. The fetched copy truncates the code samples; the animated demo on the page is scripted, with no models running.

## Influenced pages
- [Vercel Board](../../tools/vercel-board.md) — new tool page
- [State of Agents](../../state-of/agents.md) — new Agent orchestration leader line
- [Multi-agent coordination](../../workflows/multi-agent-coordination.md) — shared-task-board pattern

## Key claims extracted
- Board launched 2026-11-18 as an experimental agentic primitive; harness-agnostic (Claude Code, Codex, Pi, OpenCode, eve, fx, Mastra, LangChain named)
- v0's software factory, rebuilt on Board, merges over 50% of v0's PRs; Vercel's security agents are tracked on Board
- Agents claim tasks with renewable leases; tasks support dependencies; watchers trigger agents on replies or label changes, waking Vercel deployments
- `vercel board schedule` lets an agent set its own follow-ups; `--no-sync` keeps notes internal
- Two-way sync with Slack and GitHub (replies, reactions, edits, deletions); structured messages validated against versioned schemas
- Grants per board for users, projects and environments; events record the actor; Sandbox access without in-sandbox credentials
- Templates: Slack-connected factory and agent swarm
```

### wiki/index.md (updated)

Under Tools, in alphabetical position:

```md
- [tools/vercel-board](tools/vercel-board.md) — Vercel's experimental headless task board for agent fleets across harnesses: leased claims, task dependencies, watchers, Slack/GitHub two-way sync, per-board grants; v0's factory on it merges over 50% of PRs *(as_of: 2026-11-18)*
```

Increment the Tools row under `## Page count` and the total content pages by one.

## Schema / vocabulary additions

None.

## Open questions

- Should v0's factory (over 50% of PRs merged, Slack-to-PR template) also get a sentence on [Software factory](../wiki/workflows/software-factory.md), next to the Vercel AI SDK factory already there? Assumed no; it stays on the tool page.
	- No
