---
type: proposal
source: raw/newsletters/2026-03-09-claude-code-now-runs-while-you-sleep.md
status: pending
created: 2026-04-22
---

# Proposal: Claude Code scheduled tasks and `/loop`

## Summary

This March source cluster gives an earlier and more concrete version of the "Claude Code becomes a repeatable workflow engine" story already present in the wiki. The important addition is that recurring local automation and `/loop` were explicit product primitives before the later routines/Channels expansion.

## Intended changes

- [x] **Update** `wiki/tools/claude-code.md` — add March scheduled-tasks and `/loop` context
- [x] **Update** `wiki/state-of/coding.md` — strengthen the `Terminal coding agent` line for Claude Code
- [x] **Create** `wiki/sources/newsletters/claude-code-scheduled-tasks-march.md` — source summary page

## Page drafts

### wiki/tools/claude-code.md (updated snippet)

```markdown
## Current status (as of 2026-04-21)

- Terminal CLI agent with persistent project context via `CLAUDE.md`
- Early March introduced two practical automation primitives before the later routines/platform push: local scheduled tasks on desktop and `/loop`, a recurring-prompt command that could keep watching PRs, Slack notifications, or other long-running work for up to three days
...

## Recent changes

- [2026-03-07] Claude Code added local scheduled tasks plus `/loop`, giving the terminal agent an explicit recurring-work primitive before the later hosted-routines layer
- [2026-04-21] Added late-March Channels / recurring-tasks context: phone-triggered continuation and scheduled workflows strengthen the multi-session supervision direction
...
```

### wiki/state-of/coding.md (updated snippet)

```markdown
### Terminal coding agent

- [[tools/claude-code]] — Anthropic; terminal-first agent whose March scheduled tasks and `/loop` features made recurring background work first-class before the later Monitor / routines expansion pushed it further toward supervised workflow automation *(as of 2026-03-07)*
```

### wiki/sources/newsletters/claude-code-scheduled-tasks-march.md (new)

```markdown
---
title: Claude Code scheduled tasks and `/loop`
type: source
source_type: newsletter
source_file: raw/newsletters/2026-03-09-claude-code-now-runs-while-you-sleep.md
published: 2026-03-09
ingested: 2026-04-22
domains: [coding, agents]
---

# Claude Code scheduled tasks and `/loop`

This source cluster captures the moment Claude Code stopped looking like only an interactive terminal session and started looking like a recurring background workflow tool. The key additions were local scheduled tasks and `/loop`, which let the agent keep checking on work instead of waiting for the user to restart it manually.

## Influenced pages

- [[tools/claude-code]] — earlier product evidence for recurring automation
- [[state-of/coding]] — strengthens the terminal-agent → workflow-engine story

## Key claims extracted

- Claude Code desktop added local scheduled tasks that run while the machine is awake
- `/loop` allows recurring prompts for up to three days
- Example uses included PR babysitting, CI follow-up, and Slack summary workflows
- These features predate and help explain the later routines / supervision direction
```

## Open questions

- None.
