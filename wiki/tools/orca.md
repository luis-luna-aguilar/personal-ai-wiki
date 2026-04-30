---
title: Orca
type: tool
domains: [coding, agents]
subcategory: agentic-coding-workspace
tags: [open-source, agentic]
as_of: 2026-04-21
sources: [orca-homepage]
---

# Orca

Orca is an open-source desktop IDE for supervising multiple AI coding agents across isolated git worktrees. The product is positioned less as a single chat/terminal loop and more as a command center: parallel worktree cards, Ghostty-inspired terminal panes, built-in file and markdown editing, diff review, CI/PR visibility, and agent status reporting in one window.

## Current status (as of 2026-04-21)

- Homepage positions Orca as "the worktree IDE for AI coding agents"
- Runs Claude Code, Codex, OpenCode, and similar agents side by side in isolated worktrees
- Ships on macOS, Windows, and Linux
- Open-source under the MIT License
- Homepage shows 1.5k GitHub stars
- New built-in browser + design mode is highlighted on the landing page

## Strengths

- Explicitly built around parallel branch / worktree supervision rather than one active agent at a time
- Puts terminals, diffs, file previews, markdown, PDFs, and images in the same review surface
- Agent status reporting reduces the need to babysit terminal sessions
- Open-source positioning makes it a plausible orchestration layer around third-party agents, not only a closed vendor stack

## Weaknesses / caveats

- The source is marketing copy from the homepage, so comparative performance or adoption claims are thin
- No benchmark, pricing, or enterprise workflow detail on the fetched page
- Positioning overlaps with Cursor's agent-workspace story, but the differentiator here is worktree-centric supervision rather than local↔cloud agent handoff

## Recent changes

- [2026-04-21] Added built-in browser + design mode to the homepage hero
- [2026-04-21] Homepage emphasizes live agent status reporting, worktree cards, diff review, and CI visibility as the core workflow

## Sources

- [Orca homepage / product overview](../sources/articles/orca-homepage.md)
