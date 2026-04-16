---
title: Cursor
type: tool
domains: [coding, agents]
subcategory: agentic-coding-workspace
tags: [closed-source, agentic]
as_of: 2026-04-10
sources: [cursor-3-launch, cursor-pr-demos, cursor-bugbot-learning]
---

# Cursor

Cursor is an AI coding product from Anysphere. It started life as a VS Code fork focused on inline AI editing and pair programming, and with **Cursor 3** has been rebuilt from scratch as an agent-first workspace: a desktop app that surfaces local and cloud AI coding agents in one sidebar, supports multi-repo work, and lets users hand sessions back and forth between environments. The legacy Cursor IDE mode is still available inside the same product.

## Current status (as of 2026-04-10)

- **Cursor 3** is the current shipped version, announced in the "Meet the new Cursor" post on cursor.com/blog
- New top-level interface built from scratch (not the VS Code fork) and centered on agents
- Inherently multi-workspace: humans and agents work across multiple repos simultaneously
- Cloud agents auto-attach demo videos and screenshots to PRs for visual review *(as of 2026-04-10)*
- **Bugbot** now learns rules from production PR feedback; Cursor reports a 78.13% resolution rate across 50,310 public PRs and 44,000+ learned rules across 110,000+ repos *(as of 2026-04-10)*
- Backed by [[models/composer-2|Composer 2]], Cursor's own frontier coding model with high usage limits
- Plugin marketplace ("Cursor Marketplace") supports MCPs, skills, and subagents, with one-click install and private team marketplaces
- Legacy "Cursor IDE" mode still available — switch back at any time

## What's new in Cursor 3

- **All your agents in one place.** Local and cloud agents (kicked off from desktop, mobile, web, Slack, GitHub, Linear) appear in one sidebar.
- **Run many agents in parallel.** Cloud agents produce demos and screenshots for the human to verify; same experience as `cursor.com/agents`, now embedded.
- **Local ↔ cloud handoff.** Move a session from cloud to local for hands-on edits; move local → cloud to keep long-running tasks alive while offline.
- **Diffs & PR flow.** New diffs view for editing/reviewing changes; stage, commit, and manage PRs from inside Cursor.
- **Files for understanding code.** Full LSP support — view files, go to definition — when you want to drop down a level.
- **Integrated browser.** Cursor can open, navigate, and prompt against local sites via a built-in browser tool.

## Strengths

- First-class support for orchestrating multiple agents across repos
- Seamless local/cloud session migration is genuinely novel
- Plugin ecosystem (MCPs, skills, subagents) lowers the bar for extending agent behavior
- Drops back to traditional IDE when the user wants direct control

## Weaknesses / caveats

- Closed source; no published benchmark numbers in the launch post
- Vendor framing emphasizes a "third era" narrative — usefulness for everyday brownfield work is not yet demonstrated by external usage reports
- Requires buying into a new mental model (agent sessions as the unit of work) — users coming from the IDE-centric Cursor will need to relearn the surface

## Recent changes

- [2026-04-10] Bugbot learned rules: production PR feedback now turns into active review rules; Cursor reports 78.13% resolution across 50,310 public PRs
- [2026-04-10] Cloud agents now auto-attach demo videos and screenshots to GitHub PRs
- [2026-04-02] Cursor 3 announced — rebuilt agent-first interface, multi-repo, local↔cloud handoff, Composer 2, plugin marketplace

## Sources

- [[sources/articles/cursor-3-launch]]
- [[sources/articles/cursor-pr-demos]]
