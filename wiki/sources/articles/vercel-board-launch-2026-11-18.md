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
