---
type: proposal
source: raw/articles/2026-11-24-cursorcom-blog-projects.md
sources:
  - raw/articles/2026-11-24-cursorcom-blog-projects.md
  - raw/articles/2026-11-23-arslanio-2026-09-11-how-i-manage-my-agents.md
  - raw/newsletters/2026-09-12-ainews-deepseek-v41-flash-763b-p8b-d16b-novel.md
status: pending
created: 2026-11-24
---

# Proposal: Cursor Projects — long-running coordinator agents, and a plans-in-git way to run them

## Summary

### In short
Cursor now sells the coordinator as the product: with Projects, a developer talks to one long-lived agent that never writes code, only dispatches workers, keeps shared context, and wakes itself on PR, Slack or schedule events. Cursor says heavy Projects users merge six times as many PRs. A Cursor engineer's field report adds the operating discipline: plans and coordinator notes kept in git, so a broken coordinator can be rebuilt in one turn. The proposal adds a Projects section to **Cursor**, a pattern to **Multi-agent coordination**, an instance to its evidence page, and refreshes the **State of Coding** Cursor line. Hesitation: the launch date is inferred.

[[#Open questions|Open questions: none.]]

- [x] **Approve all** — checking this box approves every item in `## Intended changes` and `## Schema / vocabulary additions` below; the individual boxes may stay empty.

### The source
Cursor's launch post, "Introducing Projects," announces a beta rolling out to all users. A Project is meant for work that outlives one chat: a multi-PR feature, a migration, or never-ending upkeep. You steer it by chatting with a coordinator agent that delegates rather than executes, so it is never blocked. It runs on its own cloud computer and spins up a local agent only when something must be tested on your machine; it keeps shared files that every agent reads and adds to; and it holds subscriptions, waking on a Slack channel, a schedule, or your PRs to fix CI and act on merges. Cursor says new users merge 30% more PRs, and one engineer's design-system Project adds a lint rule whenever it sees the same mistake twice, on track for 20 to 100 PRs a day.

The post carries no date. Fatih Arslan, a Cursor engineer, wrote on 11 September that Projects was announced "yesterday," and described how he runs it. Every piece of work is a markdown plan in a git repo that moves through folders: a high-reasoning model turns a draft into a plan an agent can implement without design questions, a fast model on a cloud agent executes it, and a sync step files it as done or discarded once the PR merges. Coordinators per area (billing, storage, fleet) sit under a Hub. They cannot message each other, so they leave inbox files in git, each headed From, To, Date and Why. Each coordinator commits its notes every turn, and when a beta bug trapped one in an error loop after about 460 messages, a fresh Project rebuilt its state from the repo in one turn.

### What changes
The wiki covers Cursor's cloud agents and its research swarms, and has Claude Code's own Projects as a coordinator product, but nothing on Cursor Projects or on coordinators that wake on events.

- **Cursor** gains a "Projects" section and a Current-status bullet; one Recent-changes entry dated 10 September, and the oldest entry (Cursor SDK, 30 April) moves to history. Page date moves to 10 September.
- **Multi-agent coordination** gains a "coordinator hub with state in git" pattern, set against the mayor-plus-polecats pattern it extends; its oldest Recent-changes entry (Agentic MapReduce expansion, 14 July) moves to history. The page goes from 101% to about 110% of its ceiling, inside the warning band, so no split is offered.
- **Multi-agent coordination: evidence from practice** gains Cursor Projects as a shipped instance beside Claude Code Projects.
- **State of Coding** updates the Cursor leader line to mention Projects; the oldest Recent-changes entry (Cursor iOS, 30 June) moves to history.
- Two new source pages: the Cursor launch post and Arslan's post.

### What to weigh
The launch date of 10 September is inferred from Arslan's "yesterday" and the AINews issue, since the Cursor page shows none. The AINews summary adds nothing beyond the launch post, so it gets no source page of its own.

## Intended changes

- [ ] **Update** `wiki/tools/cursor.md` — new "Projects" section; Current-status bullet and heading date; `as_of` 2026-09-09 → 2026-09-10; adds `cursor-projects-launch-2026-09-10` and `arslan-how-i-manage-my-agents-2026-09-11` to frontmatter `sources:` and `## Sources`; adds one Recent-changes entry dated 2026-09-10 at the top
- [ ] **Spill** `wiki/tools/cursor.md` → `wiki/history/tools/cursor.md` — list is at its cap of 10; spills the oldest entry (2026-04-30, Cursor SDK)
- [ ] **Update** `wiki/workflows/multi-agent-coordination.md` — new pattern under "Coordination mechanics"; adds `arslan-how-i-manage-my-agents-2026-09-11` and `cursor-projects-launch-2026-09-10` to sources; adds one Recent-changes entry dated 2026-09-11 (between 2026-10-06 and 2026-09-09); `as_of` stays 2026-11-18
- [ ] **Spill** `wiki/workflows/multi-agent-coordination.md` → `wiki/history/workflows/multi-agent-coordination.md` — spills the oldest entry (2026-07-14, Agentic MapReduce expansion; the 2026-06-29 Sidekick entry already spilled today)
- [ ] **Update** `wiki/workflows/multi-agent-coordination-evidence.md` — new "Shipped products" bullet; adds the two source ids; adds one Recent-changes entry dated 2026-09-10 (between 2026-09-17 and 2026-09-09); `as_of` stays 2026-10-12
- [ ] **Update** `wiki/state-of/coding.md` — Cursor leader line; adds `cursor-projects-launch-2026-09-10` to sources; adds one Recent-changes entry dated 2026-09-10 (between 2026-10-12 and 2026-08-03); `as_of` stays 2026-11-23
    > **Before:** `- [Cursor](../tools/cursor.md) — Cursor 3 rebuilt as a cloud-agent orchestration platform; acquired by SpaceX ($60B, June 2026), with Cursor Origin and the jointly-trained Grok 4.5/4.6 models *(as of 2026-08-29)*`
    > **After:** `- [Cursor](../tools/cursor.md) — Cursor 3 rebuilt as a cloud-agent orchestration platform; Projects (beta) adds long-running coordinator agents that dispatch workers and wake on PR, Slack or schedule events; acquired by SpaceX ($60B, June 2026), with Cursor Origin and the jointly-trained Grok models *(as of 2026-09-10)*`
- [ ] **Spill** `wiki/state-of/coding.md` → `wiki/history/state-of/coding.md` — spills the oldest entry (2026-06-30, Cursor iOS beta)
- [ ] **Create** `wiki/sources/articles/cursor-projects-launch-2026-09-10.md` — source summary
- [ ] **Create** `wiki/sources/articles/arslan-how-i-manage-my-agents-2026-09-11.md` — source summary

## Page drafts

### wiki/tools/cursor.md (updated)

Frontmatter changes:

```
as_of: 2026-09-10
sources: [...existing..., cursor-projects-launch-2026-09-10, arslan-how-i-manage-my-agents-2026-09-11]
```

`## Current status` heading and new bullet (appended after the existing bullets):

```
## Current status (as of 2026-09-10)

- **Projects** (beta, 2026-09-10): long-lived coordinator agents that dispatch cloud and local workers, keep shared context, and act on PR, Slack or schedule events — see section below
```

New section, inserted after `## The third era thesis`:

```
## Projects (as of 2026-09-10)

Projects, in beta for all users since 2026-09-10, is Cursor's concrete version of the third-era thesis. A Project is a long-lived thread for work that outlives one chat (a multi-PR feature, a migration, ongoing upkeep). The user chats with a **coordinator agent** that writes no code and delegates to worker agents, so it is never blocked.

- **Cloud by default, local when needed:** the Project runs on its own computer; it can also dispatch agents to the user's machine (remote workers) or a remote box they own.
- **Shared context:** a Project Context (a coordinator-written `notes.md`, docs, agent scratch) syncs to every agent; a global User Context holds `preferences.md`, read only by coordinators, and synced skills.
- **Subscriptions:** the coordinator follows PRs, Slack channels or schedules and wakes on CI results, review comments and merges.
- Cursor reports new users merge 30% more PRs and Projects-heavy users six times as many; a design-system "gardening" Project adds a lint rule whenever it sees the same mistake twice.

Cursor engineer Fatih Arslan's plans-in-git operating model for Projects is on [Multi-agent coordination](../workflows/multi-agent-coordination.md).
```

`## Recent changes` — insert one entry at the top; remove the oldest (2026-04-30) per the Spill item:

```
- [2026-09-10] Projects launched in beta: long-running coordinator agents that dispatch cloud/local workers, keep shared Project and User Context, and subscribe to PRs, Slack channels and schedules; Cursor reports Projects-heavy users merge 6x as many PRs.
```

`## Sources` — append:

```
- [Cursor — Introducing Projects](../sources/articles/cursor-projects-launch-2026-09-10.md)
- [Fatih Arslan — How I manage my agents](../sources/articles/arslan-how-i-manage-my-agents-2026-09-11.md)
```

### wiki/history/tools/cursor.md (updated)

Append:

```
## Archived from current page on <apply date>

- [2026-04-30] Cursor SDK released: TypeScript SDK exposes the Cursor agent runtime headlessly for CI, automations, cloud VMs, MCP servers, model swapping, and embedded product agents; marks transition from IDE seat product toward agent infrastructure platform
```

### wiki/workflows/multi-agent-coordination.md (updated)

Frontmatter change:

```
sources: [...existing..., cursor-projects-launch-2026-09-10, arslan-how-i-manage-my-agents-2026-09-11]
```

New bullet at the end of `### Coordination mechanics`:

```
- **Coordinator hub with state in git.** A long-lived coordinator per area of work writes no code: it turns plans into dispatched workers and wakes on events (CI results, review comments, merges, Slack alerts, a schedule) instead of waiting to be prompted. Work is a markdown plan moving through folders in a dedicated repo (`drafts/` → `next/` → `open/` → `done/` or `discarded/`): a high-reasoning model writes the plan until a worker can implement it without design questions, and a fast model executes it. Coordinators cannot message each other, so they leave inbox files in git, each headed From/To/Date/Why, and only a Hub writes into an area's file. Each coordinator commits its notes every turn, which makes it replaceable: after a platform bug looped one coordinator at about 460 messages, a fresh one rebuilt its state from the repo in one turn. It extends mayor + polecats with event subscriptions and git-held state. *Source: Fatih Arslan running [Cursor](../tools/cursor.md) Projects (September 2026)*
```

`## Recent changes` — insert one entry between 2026-10-06 and 2026-09-09; remove the oldest (2026-07-14) per the Spill item:

```
- [2026-09-11] Added the coordinator-hub-with-state-in-git pattern (plan lifecycle folders, event-woken coordinators, git inbox files between coordinators) from a Cursor engineer's Projects workflow.
```

`## Related` — append:

```
- [Cursor](../tools/cursor.md) — Projects, the coordinator product the git-state pattern runs on
```

`## Sources` — append:

```
- [Fatih Arslan — How I manage my agents](../sources/articles/arslan-how-i-manage-my-agents-2026-09-11.md)
- [Cursor — Introducing Projects](../sources/articles/cursor-projects-launch-2026-09-10.md)
```

### wiki/history/workflows/multi-agent-coordination.md (updated)

Append to the existing `## Archived from current page on 2026-11-24` block at the end of the file (or a new block with the apply date if that differs):

```
- [2026-07-14] Expanded Agentic MapReduce from a passing mention into a full pattern entry: deterministic Plan/Shard/Map/Reduce (+Verify for Security Swarm) architecture, sourced from Cognition's engineering writeup (its three supporting research citations are now on the evidence page).
```

### wiki/workflows/multi-agent-coordination-evidence.md (updated)

Frontmatter change:

```
sources: [...existing..., cursor-projects-launch-2026-09-10, arslan-how-i-manage-my-agents-2026-09-11]
```

New bullet in `### Shipped products`, after the Claude Code Projects bullet:

```
- Cursor's Projects (beta, 2026-09-10) ship the same coordinator shape with event subscriptions: the coordinator delegates and never codes, workers run in the cloud or on the user's machine, and the coordinator wakes on PRs, Slack or a schedule. Cursor reports users who mostly work in Projects merge six times as many PRs, and a design-system Project that adds a lint rule on any repeated mistake is on track for 20 to 100 PRs a day. A Cursor engineer's account shows the operating cost: plans and coordinator notes kept in git so a looping coordinator could be replaced in one turn.
```

`## Recent changes` — insert one entry between 2026-09-17 and 2026-09-09:

```
- [2026-09-10] Added Cursor Projects as a second shipped coordinator product, with event subscriptions and Cursor's PR-throughput numbers.
```

`## Sources` — append:

```
- [Cursor — Introducing Projects](../sources/articles/cursor-projects-launch-2026-09-10.md)
- [Fatih Arslan — How I manage my agents](../sources/articles/arslan-how-i-manage-my-agents-2026-09-11.md)
```

### wiki/state-of/coding.md (updated)

Frontmatter change:

```
sources: [...existing..., cursor-projects-launch-2026-09-10]
```

`### Agentic coding workspace` — Cursor line:

```
- [Cursor](../tools/cursor.md) — Cursor 3 rebuilt as a cloud-agent orchestration platform; Projects (beta) adds long-running coordinator agents that dispatch workers and wake on PR, Slack or schedule events; acquired by SpaceX ($60B, June 2026), with Cursor Origin and the jointly-trained Grok models *(as of 2026-09-10)*
```

`## Recent changes` — insert one entry between 2026-10-12 and 2026-08-03; remove the oldest (2026-06-30) per the Spill item:

```
- [2026-09-10] Cursor launched Projects (beta): long-running coordinator agents that delegate to cloud and local workers and subscribe to PRs, Slack channels and schedules.
```

### wiki/history/state-of/coding.md (updated)

Append:

```
## Archived from current page on <apply date>

- [2026-06-30] Cursor iOS beta adds mobile launch/control for always-on cloud agents and desktop agents.
```

### wiki/sources/articles/cursor-projects-launch-2026-09-10.md (new)

```
---
title: Cursor — Introducing Projects
type: source
source_type: article
source_file: raw/articles/2026-11-24-cursorcom-blog-projects.md
url: https://cursor.com/blog/projects
published: 2026-09-10
ingested: 2026-11-24
domains: [coding, agents]
---

# Cursor — Introducing Projects

Cursor's launch post for Projects, in beta and rolling out to all users. A Project takes on a feature, migration or full app over months: the user chats with a coordinator agent that directs other agents instead of writing code. The post names three capabilities (cloud by default with local agents when needed, shared context files synced to every agent, and subscriptions to Slack, schedules and PRs) and three internal usage patterns (feature work, migrations, gardening). The page carries no date; 2026-09-10 is inferred from a Cursor engineer's 2026-09-11 post saying it was announced "yesterday" and AINews coverage on 2026-09-12.

## Influenced pages
- [Cursor](../../tools/cursor.md) — new Projects section
- [Multi-agent coordination: evidence from practice](../../workflows/multi-agent-coordination-evidence.md) — shipped coordinator instance
- [Multi-agent coordination](../../workflows/multi-agent-coordination.md) — supports the coordinator-hub pattern
- [State of Coding](../../state-of/coding.md) — Cursor leader line

## Key claims extracted
- The coordinator delegates rather than executes, so it is "never blocked"; it can direct thousands of subagents
- A Project runs on its own computer; a local agent is started when something needs testing on the user's machine
- Shared context files sync across every cloud and local machine the Project's agents use
- Subscriptions: watch a Slack channel, run on a schedule, or follow all PRs, fixing CI and acting on open/merge
- New users merge 30% more PRs; users who primarily use Projects merge six times as many
- A design-system Project scans every new PR, extracts components, adds a lint rule when it sees the same mistake twice; on track for 20–100 PRs a day
- Migrations: review each PR closely early, then less as fixes hold up
```

### wiki/sources/articles/arslan-how-i-manage-my-agents-2026-09-11.md (new)

```
---
title: Fatih Arslan — How I manage my agents
type: source
source_type: article
source_file: raw/articles/2026-11-23-arslanio-2026-09-11-how-i-manage-my-agents.md
url: https://arslan.io/2026/09/11/how-i-manage-my-agents/
published: 2026-09-11
ingested: 2026-11-24
domains: [agents, coding]
---

# Fatih Arslan — How I manage my agents

A Cursor engineer's workflow for running a fleet of agents through markdown plans in a dedicated git repo, now driven by Cursor Projects coordinators. Plans move through `drafts/`, `next/`, `open/`, `done/` and `discarded/` via skills (`/plan-add`, `/plan-write` with a high-reasoning model, `/plan-dispatch` with a fast model, `/plan-sync`, `/plan-status`, `/plan-retro`). Area coordinators under a Hub pass messages through git inbox files and commit their notes every turn. He deliberately does not publish the skills and offers a prompt that has an agent write them from the user's own history instead.

## Influenced pages
- [Multi-agent coordination](../../workflows/multi-agent-coordination.md) — coordinator hub with state in git pattern
- [Cursor](../../tools/cursor.md) — Project Context, User Context, remote workers, subscriptions detail
- [Multi-agent coordination: evidence from practice](../../workflows/multi-agent-coordination-evidence.md) — coordinator rebuilt from repo

## Key claims extracted
- Cursor announced Projects on 2026-09-10 ("yesterday" relative to the post)
- A coordinator doesn't write code; it directs agents that do
- Projects can dispatch to a fresh cloud agent, the user's MacBook (remote workers, even from iPhone) or a remote Linux box
- Project Context: coordinator-written `notes.md`, `docs/` and `media/` for humans, `internal/` for agent scratch; User Context: `preferences.md` (read by coordinators each turn, not passed to agents) and synced `skills/`
- Coordinators subscribe to every PR their workers open and send workers back on CI failures or review comments
- Coordinators cannot message each other or read each other's Context; inbox files in git start with From/To/Date/Why; only the Hub writes into an area's file
- After a beta bug looped a coordinator at ~460 messages, a fresh Project rebuilt its notes from the repo in one turn
- `/plan-retro` reads done/discarded plans and transcripts and proposes edits to the skills
```

## Schema / vocabulary additions

None.

## Open questions

None.
