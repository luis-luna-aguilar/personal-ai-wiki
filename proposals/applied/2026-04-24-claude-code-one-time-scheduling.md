---
type: proposal
sources:
  - raw/tweets/2026-04-24-noahzweben-2047364243310416044.md
status: pending
created: 2026-04-24
---

# Proposal: Claude Code One-Time Scheduling

## Summary

This is a small but legitimate product increment: Claude Code now supports one-time scheduled tasks from the CLI or the Routines UI via a `Schedule -> Once` trigger. It does not justify a new page and probably does not need a state-of change on its own, but it is worth a lightweight update to `tools/claude-code` plus a small tweet source summary.

## Intended changes

- [x] **Update** `wiki/tools/claude-code.md` — add one-time scheduling detail; update `as_of`; prepend `Recent changes`
- [x] **Create** `wiki/sources/tweets/claude-code-one-time-scheduling.md` — short source summary

## Page drafts

### wiki/tools/claude-code.md (update — diff only)

> **Update frontmatter:**
> - `as_of: 2026-04-24`
> - append `claude-code-one-time-scheduling` to `sources`

> **Add to `## Current status`:**
> ```markdown
> - One-time scheduling is now available from the CLI and Routines UI via `Schedule -> Once`, extending the existing recurring-work story into delayed single-run tasks
> ```
>
> **Add to `## Recent changes` (prepend):**
> `- [2026-04-24] Added one-time scheduling from CLI / Routines UI via \`Schedule -> Once\`, extending Claude Code's scheduled-workflow support beyond recurring runs`

### wiki/sources/tweets/claude-code-one-time-scheduling.md (new)

````md
---
title: Claude Code one-time scheduling
type: source
source_type: tweet
source_file: raw/tweets/2026-04-24-noahzweben-2047364243310416044.md
url: https://x.com/noahzweben/status/2047364243310416044
published: 2026-04-24
ingested: 2026-04-24
domains: [coding, agents]
---

# Claude Code one-time scheduling

Small product update from Noah Zweben: Claude Code now supports delayed one-time scheduled tasks from the CLI or the Routines UI through a `Schedule -> Once` trigger.

## Influenced pages

- [[tools/claude-code]] — small current-status update

## Key claims extracted

- One-time scheduling is available from the CLI and Routines UI
- Feature is exposed as `Schedule -> Once`
- Example uses include delayed cleanup and deferred launch reports
````
