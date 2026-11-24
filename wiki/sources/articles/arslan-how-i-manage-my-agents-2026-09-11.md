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
