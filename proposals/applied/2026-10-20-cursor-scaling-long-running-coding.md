---
type: proposal
source: raw/articles/2026-09-09-cursorcom-blog-scaling-agents.md
triage: proposals/triage/2026-10-19-raw-orphans-sweep.md
status: pending
created: 2026-10-20
---

# Proposal: Cursor — "Scaling long-running autonomous coding" (first-generation swarm post)

## Summary

### In short
Flat agent swarms fail even when the concurrency mechanics work: Cursor's first-generation post says replacing locks with optimistic writes made coordination simpler and more robust, but with no hierarchy agents turned risk-averse and churned, which is what forced the planner/worker split. The wiki already carries most of this post's lessons through Cursor's later recap, so the proposal only fills gaps on Long-running agent swarms: the optimistic-concurrency step, the scale of the runs, model choice by role, and the open problems Cursor admits. One reason to hesitate: the post carries no date, so the page date stays where it is.

[[#Open questions|Open questions: none.]]

- [ ] **Approve all** — checking this box approves every item in `## Intended changes` and `## Schema / vocabulary additions` below; the individual boxes may stay empty.

### The source
"Scaling long-running autonomous coding" is Cursor's first post on running hundreds of coding agents on one project for weeks; the later "Towards self-driving codebases", already in the wiki, builds on it.

The team first let equal agents coordinate through a shared file, claiming tasks under a lock. Agents held locks too long or forgot them, and twenty agents slowed to the throughput of two or three. Optimistic concurrency control, where a write fails if the state changed since it was read, was simpler and more robust, but with nobody in charge agents avoided hard tasks, made small safe changes, and churned. Splitting roles fixed it: planners create tasks and spawn sub-planners, workers grind on one task and push, and a judge decides at each cycle's end whether to continue.

The system built a web browser in close to a week (over a million lines across 1,000 files), migrated Cursor's codebase from Solid to React over three weeks, and made a video renderer 25x faster in Rust. Cursor found GPT-5.2 held focus better than Opus 4.5 and planned better than GPT-5.1-Codex, so it picks a model per role. It says prompts mattered more than harness or model, and lists open problems: planners should wake when tasks finish, agents sometimes run too long, and fresh starts are still needed.

### What changes
Long-running agent swarms already has the lock failure, the planner/worker topology and the freshness mechanisms, from the later post's recap.

- **Long-running agent swarms** adds the optimistic-concurrency step to the Topology bullet, run sizes to the intro, a "Model choice by role" bullet, and an open-problems sentence. One Recent-changes entry (4 entries, no spill). Page date stays 9 September.
- New source page.

### What to weigh
The post shows no date. It predates the later post, which the wiki dated by its 9 September fetch, so the Recent-changes entry uses that date and the page date is not freshened with older material. The model names are superseded, so that bullet is framed as a lesson about choosing models per role.

## Intended changes

- [ ] **Update** `wiki/workflows/long-running-agent-swarms.md` — extend the intro paragraph and the Topology bullet; add one sentence at the end of the freshness bullet; add one bullet under `## Design principles`; adds one Recent-changes entry dated 2026-09-09 (live list has 3, no spill); append source id and link; `as_of` stays 2026-09-09
    > See draft below

- [ ] **Create** `wiki/sources/articles/cursor-scaling-long-running-coding-2026-09-09.md` — source summary

## Page drafts

### wiki/workflows/long-running-agent-swarms.md (updated)

Frontmatter `sources:` (append one id; `as_of` unchanged):

```
sources: [cursor-self-driving-codebases-2026-09-09, cursor-agent-swarm-economics-2026-09-07, cursor-scaling-long-running-coding-2026-09-09]
```

Intro paragraph (replaces the first paragraph under the title):

```
Case-study lessons from running hundreds of coding agents together for days without human intervention, drawn from Cursor's two published swarm generations: a first-generation harness that built a web browser from scratch (over 1M lines across 1,000 files in close to a week, peaking at ~1,000 commits/hour across 10M tool calls) and a second-generation swarm that built SQLite from scratch in Rust from only its manual. The first-generation harness also ran a three-week in-place Solid-to-React migration of Cursor's own codebase (+266K/−193K lines, passing CI but still needing review) and rewrote a video renderer in Rust for a 25x speedup that was merged. The general topology and routing patterns these swarms instantiate live on [Multi-agent coordination](multi-agent-coordination.md); this page keeps the swarm-specific topology evolution, failure modes, and operating principles.
```

`## Topology` — the bullet's opening sentence changes as follows (rest of the bullet unchanged):

> **Before:** `- **Recursive planner/subplanner/worker topology.** Cursor's first-generation browser-building harness converged on three fixed roles after cycling through self-coordination (shared-file locking — failed: agents held locks too long, 20 agents throttled to 1-3x throughput), a planner/executor/judge split …`

```
- **Recursive planner/subplanner/worker topology.** Cursor's first-generation browser-building harness converged on three fixed roles after cycling through self-coordination (shared-file locking — failed: agents held locks too long, 20 agents throttled to 1-3x throughput; optimistic concurrency control, where a write fails if the state changed since it was read, was simpler and more robust but still failed for a deeper reason: with no hierarchy, agents became risk-averse, avoided hard tasks, made small safe changes, and churned without progress), a planner/executor/judge split …
```

`## Keeping long runs on track` — append one sentence to the end of the "Freshness mechanisms" bullet:

```
Cursor's first post lists what was still unsolved: planners should wake up when their tasks complete to plan the next step, agents occasionally run far too long, and periodic fresh starts are still needed to fight drift and tunnel vision. *Source: Cursor, "Scaling long-running autonomous coding"*
```

`## Design principles` — append one bullet:

```
- **Pick the model per role, and expect prompts to matter most.** In the first-generation runs, GPT-5.2 held focus over extended autonomous work better than Opus 4.5, which tended to stop early and take shortcuts, and planned better than the coding-tuned GPT-5.1-Codex; Cursor moved to the model best suited to each role instead of one model for all. Those specific models are now superseded; the durable lessons are to test models per role on long runs, and that coordination quality "comes down to how we prompt the agents" more than to harness or model. The right amount of structure sat in the middle: too little and agents conflict, duplicate, and drift; too much and the system turns fragile. *Source: Cursor, "Scaling long-running autonomous coding"*
```

`## Recent changes` — insert one entry between the 2026-10-19 and 2026-09-07 entries:

```
- [2026-09-09] Added detail from Cursor's first swarm post, "Scaling long-running autonomous coding": the optimistic-concurrency step and its risk-aversion failure, browser and migration run sizes, model choice by role, and open problems.
```

`## Sources` — append:

```
- [Cursor — Scaling long-running autonomous coding](../sources/articles/cursor-scaling-long-running-coding-2026-09-09.md)
```

### wiki/sources/articles/cursor-scaling-long-running-coding-2026-09-09.md (new)

```
---
title: Cursor — Scaling long-running autonomous coding
type: source
source_type: article
source_file: raw/articles/2026-09-09-cursorcom-blog-scaling-agents.md
url: https://cursor.com/blog/scaling-agents
ingested: 2026-10-20
domains: [agents, coding]
---

# Cursor — Scaling long-running autonomous coding

Cursor's first post on running hundreds of concurrent coding agents on one project for weeks; its later "Towards self-driving codebases" post builds on it. It covers why flat self-coordination failed (locks, then optimistic concurrency with risk-averse agents), the planner/worker/judge pipeline that replaced it, the browser, Solid-to-React and video-renderer runs, model choice by role, and open problems. The page shows no publication date; it predates the 9 September 2026 posts already in the wiki and was fetched on that date.

## Influenced pages

- [Long-running agent swarms](../../workflows/long-running-agent-swarms.md) — optimistic-concurrency failure, run sizes, model choice by role, open problems

## Key claims extracted

- Flat self-coordination through a shared file with locks: locks held too long or never released; 20 agents slowed to the throughput of 2–3; brittle failure modes
- Optimistic concurrency control was simpler and more robust, but with no hierarchy agents became risk-averse, avoided hard tasks, and churned without progress
- Planners explore and create tasks and can spawn sub-planners; workers complete one task and push; a judge decides at each cycle's end whether to continue; each cycle starts fresh
- Browser from scratch: close to a week, over 1M lines across 1,000 files, hundreds of concurrent workers pushing to one branch with minimal conflicts (github.com/wilsonzlin/fastrender)
- Solid-to-React migration in Cursor's codebase: 3+ weeks, +266K/−193K edits, passing CI and early checks, still needing review
- Video rendering made 25x faster with a Rust version; merged
- GPT-5.2 better than Opus 4.5 for extended autonomous work; Opus 4.5 stops earlier and takes shortcuts; GPT-5.2 a better planner than GPT-5.1-Codex; model chosen per role
- Removing the integrator role helped; the right structure is in the middle; prompts matter more than harness and models
- Open problems: planners should wake when tasks complete; agents sometimes run too long; periodic fresh starts still needed
```

## Open questions

(none)
