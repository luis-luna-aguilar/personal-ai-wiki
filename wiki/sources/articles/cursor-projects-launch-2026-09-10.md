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
