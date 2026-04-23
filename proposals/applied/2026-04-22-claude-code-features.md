---
type: proposal
sources:
  - raw/tweets/2026-04-22-bcherny-2025007393290272904.md
  - raw/tweets/2026-04-22-noahzweben-2041654973491245509.md
  - raw/tweets/2026-04-22-noahzweben-2032533699116355819.md
  - raw/tweets/2026-04-22-claudeai-2046328619249684989.md
status: pending
created: 2026-04-22
---

# Proposal: Claude Code features batch — worktrees, /autofix-pr CLI, Remote Control

## Summary

Several Claude Code and Cowork feature updates in this batch. Most significant: built-in `--worktree` flag for parallel isolated agents. Also: `/autofix-pr` now triggerable from CLI, Remote Control session spawning from mobile. Note: Cowork live artifacts were already on the existing page (as_of 2026-04-21) so no update needed there.

## Intended changes

- [x] **Update** `wiki/tools/claude-code.md` — add worktrees, /autofix-pr CLI, Remote Control
    > **Add to `## Current status`** (insert before `## Monitor tool` section):
    > ```markdown
    > - Built-in `--worktree` flag: run `claude --worktree` to give each Claude Code session its own isolated git worktree, enabling multiple agents to work in parallel without interfering with each other's file changes; Boris Cherny (Claude Code creator) announced; Matt Pocock calls it "my new default"
    > - `/autofix-pr` now triggerable from CLI: run `/autofix-pr` after finishing a PR, and it sends your session to the cloud so the PR autofixer has full context to address CI failures and reviewer comments
    > - Remote Control: `claude remote-control` spawns a new local Claude Code session from the mobile app (available on Max, Team, and Enterprise plans at version ≥2.1.74); lets you kick off sessions from your phone
    > ```
    >
    > **Update `as_of: 2026-04-22` in frontmatter.**
    > **Add to `## Recent changes`:**
    > ```
    > - [2026-04-22] Added --worktree flag (built-in parallel isolated git worktrees), /autofix-pr CLI trigger, and Remote Control mobile session spawning
    > ```

- [x] **Create** `wiki/sources/tweets/claude-code-worktree-autofix.md` — source summary
    > See draft below

## Page drafts

### wiki/sources/tweets/claude-code-worktree-autofix.md (new)

```md
---
title: Claude Code — worktrees, /autofix-pr CLI, Remote Control
type: source
source_type: tweet
source_file: raw/tweets/2026-04-22-bcherny-2025007393290272904.md
url: https://x.com/bcherny/status/2025007393290272904
published: 2026-04-22
ingested: 2026-04-22
domains: [coding, agents]
---

# Claude Code — worktrees, /autofix-pr CLI, Remote Control

Three Claude Code feature announcements in this batch. (1) Boris Cherny: built-in `--worktree` flag so parallel agents work in isolated git worktrees. (2) Noah Zweben: `/autofix-pr` now runs from CLI, sends session context to cloud. (3) Noah Zweben: `claude remote-control` spawns local sessions from mobile app (Max/Team/Enterprise ≥2.1.74).

Note: Cowork live artifacts were already on the wiki from a previous ingest.

## Influenced pages

- [[tools/claude-code]] — worktrees, /autofix-pr CLI, Remote Control added

## Key claims extracted

- `--worktree`: built-in; each agent gets own worktree; no interference
- `/autofix-pr` from CLI: sends full session context to cloud autofixer for CI failures + review comments
- `claude remote-control`: spawns new local session from mobile; Max/Team/Enterprise ≥2.1.74; GH required (relaxing soon)
```
