---
title: 'Projects redesigned: from folder to conversation'
type: source
source_type: article
source_file: raw/articles/2026-10-26-claudecom-blog-projects-redesigned.md
url: https://claude.com/blog/projects-redesigned
published: 2026-09-17
ingested: 2026-10-26
domains: [coding, agents]
---

# Projects redesigned: from folder to conversation

Anthropic's launch post for the redesigned Projects in Claude Code. A project now has a coordinator chat that scopes a goal, routes work to parallel threads (each a Claude Code cloud session on its own branch), reviews the outputs and assembles the result, with a shared memory and a library that build up over time. The post has no date line; it says "starting today", and the same-day @claudeai thread is dated 2026-09-17.

## Influenced pages

- [Claude Code Projects](../../tools/claude-code-projects.md) — Projects mechanics, rollout, usage warning
- [Multi-agent coordination: evidence from practice](../../workflows/multi-agent-coordination-evidence.md) — Projects as shipped coordinator-specialist routing

## Key claims extracted

- Coordinator plus threads: you set a goal and repo/context; Claude suggests work, routes requests to new or existing threads, checks in, and follows through (PRs and tests for repos, drafts for documents)
- Each thread is a Claude Code cloud session on its own branch and repo copy; overlap between threads surfaces as a normal merge conflict; threads can further split work with subagents, loops and workflows
- Configurable per project: cloud environment, connectors, plugins, instructions, model; separate model and effort settings for the coordinator chat and worker threads
- Shared memory every thread adds to and draws from (e.g. "the release moved to Friday"); Claude also remembers working and communication style; a library collects added files and Claude-made artifacts
- Projects can reach usage limits faster; project-specific usage is visible
- Threads run in the cloud; running locally, alongside local tools and behind the user's network, is "coming very soon"
- Beta for select Pro/Max subscribers who use cloud sessions and have no existing projects on web/desktop; wider Claude Code access over the following week; then all of Claude and Team/Enterprise; waitlist for Pro/Max; existing projects keep working and will be upgraded as the rollout reaches chat and Cowork
