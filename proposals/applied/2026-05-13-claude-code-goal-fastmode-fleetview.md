---
type: proposal
sources:
  - raw/newsletters/2026-05-13-supply-chain-attacks-keep-hitting-ai.md
  - raw/newsletters/2026-05-12-the-fallacy-of-the-16-hour-agent.md
  - raw/newsletters/2026-05-13-googles-macbook-competitor.md
status: pending
created: 2026-05-13
---

# Proposal: Claude Code /goal command, Opus 4.7 fast mode, FleetView

## Summary

Three distinct Claude Code updates shipped in the week of May 7–13. `/goal` adds a native long-horizon loop primitive that keeps the agent running until an evaluator model confirms the target is met. Opus 4.7 fast mode enters research preview (2.5× faster, ~6× cost per Cursor's benchmarks). FleetView — "Agent View" — is a single supervision surface for multiple parallel Claude Code sessions.

## Intended changes

- [x] **Update** `wiki/tools/claude-code.md` — add /goal, fast mode, and FleetView to current status and recent changes; update `as_of` and `sources`
    > See diff snippets below

- [x] **Update** `wiki/state-of/coding.md` — update the Claude Code leader line in `Terminal coding agent`
    > **Before:** `- [Claude Code](../tools/claude-code.md) — Anthropic; terminal-first agent expanding toward supervised multi-session workflows: Monitor, Routines, /ultrareview, --worktree, Remote Control, and /autofix-pr all shipped since March; harness architecture increasingly treated as core competitive differentiator *(as of 2026-04-23)*`
    > **After:** `- [Claude Code](../tools/claude-code.md) — Anthropic; terminal-first agent expanding toward supervised multi-session workflows: /goal (autonomous loop until evaluator confirms done), Opus 4.7 fast mode (2.5× faster, ~6× cost), and FleetView (single view for parallel sessions) added May 2026 *(as of 2026-05-13)*`

- [x] **Create** `wiki/sources/newsletters/claude-code-goal-fastmode-fleetview-2026-05-13.md`
    > See draft below

## Page drafts

### wiki/tools/claude-code.md — diff snippets

**Frontmatter `as_of`:**
> **Before:** `as_of: 2026-05-05`
> **After:** `as_of: 2026-05-13`

**Frontmatter `sources` — append at end of list:**
> Add `claude-code-goal-fastmode-fleetview-2026-05-13`

**Current status — append after the last bullet before `## Monitor tool`:**
```
- `/goal` command (May 2026, research preview): set a target (e.g. "pass all tests in this folder") and Claude loops autonomously until an evaluator model confirms it is met — analogous to the `/goals` command OpenAI added to Codex; the first native long-horizon success-criterion primitive in Claude Code
- Opus 4.7 fast mode (May 2026, research preview via API and Claude Code): Cursor reports 2.5× faster output at approximately 6× the cost compared to standard Opus 4.7; adds a new latency/price tier above the standard frontier tier
- FleetView ("Agent View", May 2026, research preview): single supervision surface for multiple parallel Claude Code agents — shows status, finish state, and waiting state across sessions; `/bg` command sends a task to a new background session from the current one; framed as "the best way to level up from 1 agent to many"
```

**Recent changes — prepend three new entries before the existing `[2026-05-01]` line:**
```
- [2026-05-13] /goal command added (research preview): autonomous loop until evaluator model confirms target met — first native long-horizon success-criterion primitive in Claude Code
- [2026-05-13] Opus 4.7 fast mode added (research preview): 2.5× faster, ~6× cost per Cursor benchmarks; new latency/price tier
- [2026-05-13] FleetView / "Agent View" added (research preview): single view supervising multiple parallel sessions; /bg sends tasks to new background sessions
```

*(The three new entries push the oldest entries past the 5-entry cap. Spill `[2026-04-22] Added /recap...` and everything older than `[2026-04-22] Added --worktree...` to `wiki/history/tools/claude-code.md` at apply time.)*

### wiki/sources/newsletters/claude-code-goal-fastmode-fleetview-2026-05-13.md (new)

```markdown
---
title: Claude Code /goal, fast mode, and FleetView — May 2026
type: source
source_type: newsletter
source_file: raw/newsletters/2026-05-13-supply-chain-attacks-keep-hitting-ai.md
published: 2026-05-13
ingested: 2026-05-13
domains: [coding, agents]
---

# Claude Code /goal, fast mode, and FleetView — May 2026

Three Claude Code features shipped during the week of May 7–13. Coverage spread across multiple newsletters; the signals were consolidated into one entry.

## Influenced pages

- [Claude Code](../../tools/claude-code.md) — current status and recent changes updated
- [State of Coding](../../state-of/coding.md) — terminal-coding-agent leader line updated

## Key claims extracted

- `/goal` command: set a success criterion; Claude loops until an evaluator model confirms it is met; positioned as equivalent to OpenAI Codex's `/goals` primitive
- Opus 4.7 fast mode: in research preview via API and Claude Code; Cursor benchmarks: 2.5× faster output, ~6× cost vs standard Opus 4.7
- FleetView / "Agent View": research preview; single list of all parallel Claude Code sessions; columns include status, finish state, waiting state; `/bg` command sends a task to a new background session from the current one
- SpaceX/Colossus compute deal (220K+ GPUs) doubles Claude Code limits on paid plans (reported same week; captured in signal 8)
```

