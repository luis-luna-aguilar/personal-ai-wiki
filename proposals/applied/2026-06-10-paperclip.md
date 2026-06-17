---
type: proposal
source: raw/articles/2026-06-10-papercliping.md
status: pending
created: 2026-06-10
---

# Proposal: Paperclip — agent management platform

## Summary

Paperclip is an open-source (MIT), self-hosted platform that frames running AI agents as managing a company: you are the board, agents are employees with titles, budgets, goals, and reporting lines. Distinct from coding-first agent frameworks; the unit of work is a business objective, not a pull request.

## Intended changes

- [x] **Create** `wiki/tools/paperclip.md` — new tool page
    > See draft below

- [x] **Create** `wiki/sources/articles/papercliping.md` — source summary
    > See draft below

- [x] **Update** `wiki/state-of/agents.md` — add Paperclip to Agent orchestration subcategory
    > **Before:**
    > ```
    > - [Multica](../tools/multica.md) — open-source; vendor-neutral managed agents platform; assign GitHub-style issues to agent CLIs (Claude Code, Codex, Copilot, and 8 others); Squads for leader-delegated routing; reusable skill compounding *(as of 2026-05-18)*
    > ```
    > **After:** (add below Multica)
    > ```
    > - [Paperclip](../tools/paperclip.md) — open-source (MIT), self-hosted; org-chart model: agents get titles, reporting lines, monthly budgets, and heartbeat schedules; governance keeps humans as the board of directors; 69.9k GitHub stars *(as of 2026-06-10)*
    > ```
    > Also update `as_of` in frontmatter to `2026-06-10` and add `papercliping` to the sources list.

- [x] **Update** `wiki/index.md` — add tools/paperclip entry
    > Add under Tools section (alphabetical near multica):
    > `- [tools/paperclip](tools/paperclip.md) — open-source MIT agent management platform; org-chart metaphor with heartbeats, per-agent budgets, and board-of-directors governance; 69.9k stars *(as_of: 2026-06-10)*`

## Page drafts

### wiki/tools/paperclip.md (new)

````md
---
title: Paperclip
type: tool
domains: [agents]
subcategory: agent-orchestration
tags: [open-source, agentic, self-hosted]
as_of: 2026-06-10
sources: [papercliping]
---

# Paperclip

Open-source (MIT), self-hosted platform for managing AI agents as a company. The core framing: you are the board of directors; agents are employees with titles, reporting lines, monthly budgets, and scheduled heartbeats. You hire, approve strategy, set goals, and override at any time.

## Current status (as of 2026-06-10)

- 69.9k GitHub stars; installed via `npx paperclipai onboard --yes`
- Model-agnostic: Claude, Codex, Gemini, Cursor, Hermes, OpenClaw, and others can all be "hired" into the same org chart
- Core primitives: Org Chart (hierarchies, roles, titles), Goal Alignment (every task traces to a mission via SKILL.md), Heartbeats (agents wake on a schedule), Cost Control (hard monthly spend limits per agent), Ticket System (full tool-call trace + append-only audit log), Governance (board-approval for new hires and strategy)
- Self-hosted; no Paperclip account required to run; MIT licensed

## Strengths

- "Company of agents" mental model is well-designed and more opinionated than generic orchestration platforms — good for cross-functional work (dev + marketing + ops under one goal)
- Hard budget limits per agent are unusual and practically useful; prevent runaway spend without manual monitoring
- Complete audit trail: every tool call, decision, and conversation is immutable and traceable

## Weaknesses / caveats

- Product page only — no benchmark data, independent reviews, or post-launch coverage; all claims and testimonials are from the homepage
- Positioning relative to Multica (issue-tracker metaphor) and Hermes (persistent coding agent) is not yet clear from the source alone

## Recent changes

- [2026-06-10] Fetched from homepage; product in general availability with docs, blog, and Discord

## Sources

- [Paperclip homepage](../sources/articles/papercliping.md)
````

### wiki/sources/articles/papercliping.md (new)

````md
---
title: Paperclip homepage
type: source
source_type: article
source_file: raw/articles/2026-06-10-papercliping.md
url: https://paperclip.ing/
ingested: 2026-06-10
domains: [agents]
---

# Paperclip homepage

Homepage of Paperclip, an open-source MIT-licensed self-hosted platform for managing AI agents as a company org chart. Tagline: "A team of agents for every person." The page covers the product concept, feature breakdown, testimonials, and a quickstart command.

## Influenced pages

- [Paperclip](../../tools/paperclip.md) — new tool page
- [State of Agents](../../state-of/agents.md) — added to Agent orchestration subcategory

## Key claims extracted

- Open source, MIT license; self-hosted via `npx paperclipai onboard --yes`
- 69.9k GitHub stars at time of fetch
- Org-chart model: CEO, CTO, CMO, COO, engineers, designers, etc. — any agent, any provider
- Goal Alignment: every task traces to mission; agents use SKILL.md for context discovery
- Heartbeats: agents wake on schedule and act; delegation flows up/down the org chart
- Cost Control: monthly hard budget per agent; auto-stop at limit
- Ticket System: structured tickets with full tool-call tracing and append-only audit log
- Governance: board-approval required for agent hires and strategy execution
- Compatible agents: Claude, Codex, Gemini, Cursor, Hermes, OpenClaw, Pi, OpenCode
````

## Open questions

- Is there a clearer differentiator between Paperclip and Multica worth surfacing in the state-of entry? Both are open-source agent management platforms; Multica uses project-board/issue-tracker framing, Paperclip uses company/org-chart framing — currently noted in the Weaknesses section but could be made more explicit.
	- Yes, the differentiator is that we can use Kubernetes to host the agents that its orchestrating.
