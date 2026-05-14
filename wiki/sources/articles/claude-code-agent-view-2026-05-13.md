---
title: Claude Code Agent View docs
type: source
source_type: article
url: https://code.claude.com/docs/en/agent-view
published: 2026-05-13
ingested: 2026-05-13
domains: [coding, agents]
---

# Claude Code Agent View docs

Claude Code's official docs describe Agent View as a terminal screen for dispatching and managing many background Claude Code sessions. It opens with `claude agents`, groups sessions by state, lets users peek and reply without opening the full transcript, and supports attaching to a session when full interaction is needed.

## Influenced pages

- [Claude Code](../../tools/claude-code.md) - replace thin FleetView wording with official Agent View details
- [State of Coding](../../state-of/coding.md) - use official Agent View naming in the Claude Code leader line

## Key claims extracted

- Agent View is opened with `claude agents` and is one screen for background sessions.
- It shows what is running, what needs input, and what is done.
- Users can dispatch new sessions from Agent View, background an existing session with `/bg`, or start one from the shell with `claude --bg`.
- Users can peek/reply, attach/detach, pin, rename, reorder, stop, and delete sessions from the view.
- Background sessions keep running without a terminal attached through a supervisor process; state persists on disk through auto-updates and supervisor restarts.
- Editable background sessions are isolated in git worktrees under `.claude/worktrees/` when possible.
- Agent View is in research preview and requires Claude Code v2.1.139 or later.
