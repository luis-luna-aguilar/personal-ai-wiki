---
title: Lessons from Anthropic on building effective human-agent teams
type: source
source_type: article
source_file: raw/articles/2026-10-20-claudecom-blog-building-effective-human-agent-teams.md
url: https://claude.com/blog/building-effective-human-agent-teams
ingested: 2026-10-20
domains: [agents, training]
---

# Lessons from Anthropic on building effective human-agent teams

A Claude blog post by Kristen Swanson (Anthropic Education team) on how Anthropic runs teams where "multiplayer agents" (agents with their own credentials, memory and skills, working with many people at once) sit in Slack alongside humans via Claude Tag. It gives four lessons from several months of internal use and five questions to ask before building such a team. No publication date appears in the article; it reached the wiki through a forward in the 1–10 October 2026 digest, so derived pages use 2026-10-10 as an upper bound.

## Influenced pages
- [Multiplayer AI](../../concepts/multiplayer-ai.md) — Anthropic's four norms as a lab's own operating account
- [Claude Tag](../../tools/claude-tag.md) — how Anthropic runs its own teams on the product
- [Agent autonomy and governance](../../training/agent-autonomy-and-governance.md) — per-task-type autonomy with verification and attention budgets

## Key claims extracted
- Work in public: for an agent, "if it's not written down and accessible, it doesn't exist." Anthropic sets access by a handful of workspace-wide security boundaries instead of per-item sharing, defaults channels to public, and writes meeting notes and artifacts for agents to find.
- Private work goes through a direct message to @Claude in Claude Tag, or Claude.ai and Cowork with personal MCP connectors.
- Teams keep one roster of humans and agents with named roles (data analysis, design standard, research synthesis), defined in skill files; one engineering team added a release-manager agent as its project grew. Without clear roles, people run side fleets of personal agents that duplicate work.
- Humans write a north star and choose which agents may proactively propose new work; an agent on an internal tools team proposed onboarding error-message copy changes that measurably raised onboarding success the next week.
- Trust is built per task type: manual review first, verification checklists, a separate verifier agent ("Doer-Verifier" harness), weekly "lessons & missteps" reports, and scope widened after repeated successes. Engineers have dispatched agents to handle 500 bug fixes independently.
- Agents are coached to treat human attention as scarce (batch questions, restate context, limit items per person); some teams cap agent work per day so review stays sustainable. Retest tasks when models change, since older guardrails can constrain a stronger model.
- Anthropic points to agent teams in Claude Code and to Claude Tag as the ways to start building multiplayer agents.
