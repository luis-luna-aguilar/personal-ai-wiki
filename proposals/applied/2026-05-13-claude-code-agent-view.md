---
type: proposal
sources:
  - raw/tweets/2026-05-13-claudeai-2053940934736228454.md
  - https://code.claude.com/docs/en/agent-view
status: pending
created: 2026-05-13
---

# Proposal: Claude Code Agent View

## Summary

Claude Code's official Agent View docs describe `claude agents` as one screen for dispatching, monitoring, peeking into, replying to, and attaching to many background Claude Code sessions. Agent View is in research preview, requires Claude Code v2.1.139 or later, and supports session dispatch from the view, from inside a session with `/bg`, or from the shell with `claude --bg`.

## Intended changes

- [x] **Update** `wiki/tools/claude-code.md` — replace the thin FleetView / Agent View wording with docs-backed Agent View details
    > Add source id `claude-code-agent-view-2026-05-13` to frontmatter `sources`.
    >
    > Replace the existing FleetView bullet with: `Agent View (research preview, Claude Code v2.1.139+): \`claude agents\` opens one terminal screen for dispatching and supervising background Claude Code sessions. Sessions are grouped by state, can be peeked/replied to without opening the full transcript, attached/detached for full conversation, and launched from Agent View, \`/bg\`, or \`claude --bg\`; editable background sessions are isolated in git worktrees under \`.claude/worktrees/\` when possible.`

- [x] **Update** `wiki/state-of/coding.md` — update Claude Code leader line if Agent View wording is currently FleetView-only
    > Mention Agent View by its official docs name, not FleetView, and keep the May 2026 multi-session-supervision claim.

- [x] **Create** `wiki/sources/articles/claude-code-agent-view-2026-05-13.md`
    > See draft below

## Page drafts

### wiki/sources/articles/claude-code-agent-view-2026-05-13.md (new)

```markdown
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

- [Claude Code](../../tools/claude-code.md) — replace thin FleetView wording with official Agent View details
- [State of Coding](../../state-of/coding.md) — use official Agent View naming in the Claude Code leader line

## Key claims extracted

- Agent View is opened with `claude agents` and is one screen for background sessions.
- It shows what is running, what needs input, and what is done.
- Users can dispatch new sessions from Agent View, background an existing session with `/bg`, or start one from the shell with `claude --bg`.
- Users can peek/reply, attach/detach, pin, rename, reorder, stop, and delete sessions from the view.
- Background sessions keep running without a terminal attached through a supervisor process; state persists on disk through auto-updates and supervisor restarts.
- Editable background sessions are isolated in git worktrees under `.claude/worktrees/` when possible.
- Agent View is in research preview and requires Claude Code v2.1.139 or later.
```
