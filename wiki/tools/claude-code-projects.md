---
title: Claude Code Projects
type: tool
domains: [coding, agents]
subcategory: terminal-coding-agent
tags: [anthropic, cli, agentic]
as_of: 2026-09-29
sources: [claude-projects-redesigned-2026-09-17, claudeai-projects-one-conversation-2026-09-17, ainews-claude-code-cloud-sessions-projects-2026-09-24, latent-space-thariq-claude-code-next-era-2026-09-29]
---

# Claude Code Projects

Projects is [Claude Code](claude-code.md)'s multi-thread mode: one coordinator chat takes a goal and runs the work as parallel cloud sessions. It is a shipped case of coordinator-specialist routing; see [Multi-agent coordination evidence](../workflows/multi-agent-coordination-evidence.md).

## Current status (as of 2026-09-29)

- **Projects:** a Claude Tag-style supervising agent for individual users without Slack admin setup. You set a goal and connect repos or documents; a coordinator chat scopes the request and routes it to parallel threads, each a full cloud session on its own branch and repo copy that opens PRs and runs tests, with overlapping edits resolved as ordinary merge conflicts. Threads share one project memory, and a library keeps added files and Claude's artifacts (each artifact with its own database several agents can read and write). Coordinator and workers take separate model and effort settings, and projects reach usage limits faster. Beta since 2026-09-17 for select Pro/Max cloud-session users (waitlist); chat, Cowork, Team and Enterprise follow. Single-player; threads were cloud-only at launch, and local runs followed.

## Related

- [Claude Code](claude-code.md) — the parent tool page; cloud sessions are covered there
- [Multi-agent coordination evidence](../workflows/multi-agent-coordination-evidence.md) — Projects as coordinator-specialist routing, with Ethan Mollick's 18-thread run

## Recent changes

- [2026-11-24] Page created, split out of [Claude Code](claude-code.md): the Projects bullet.
- [2026-09-23] Projects launched alongside cloud sessions GA and now also run locally.
- [2026-09-17] Projects redesigned (beta, select Pro/Max cloud-session users): one coordinator chat routes work to parallel threads, each a cloud session on its own branch; shared project memory and a file/artifact library; model and effort set separately for coordinator and workers.

## Sources

- [Projects redesigned: from folder to conversation](../sources/articles/claude-projects-redesigned-2026-09-17.md)
- [Claude (@claudeai) — Projects now run from one conversation](../sources/tweets/claudeai-projects-one-conversation-2026-09-17.md)
- [AINews — Claude Code cloud sessions GA and local Projects](../sources/newsletters/ainews-claude-code-cloud-sessions-projects-2026-09-24.md)
- [Latent Space — Claude Code's Next Era (Thariq Shihipar)](../sources/newsletters/latent-space-thariq-claude-code-next-era-2026-09-29.md)
