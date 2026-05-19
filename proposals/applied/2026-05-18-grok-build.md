---
type: proposal
source: raw/newsletters/2026-05-15-you-can-now-access-codex-on-phone.md
status: pending
created: 2026-05-18
---

# Proposal: xAI Grok Build — new CLI coding agent (lightweight)

## Summary

xAI launched Grok Build, a CLI coding agent in early beta for SuperGrok Heavy subscribers. Install via curl. Features: plan mode (review each step before diffs are applied) and parallel subagents in isolated git worktrees for large tasks — essentially the same worktree-parallelism pattern as Claude Code. New entrant from a well-funded lab with first-mover feature parity.

## Intended changes

- [x] **Create** `wiki/tools/grok-build.md` — new stub tool page
    > See draft below

- [x] **Update** `wiki/state-of/coding.md` — add Grok Build to Terminal coding agent subcategory; add to Recent changes
    > **Add to "Terminal coding agent" section:**
    > `- **Grok Build** — xAI; early beta CLI coding agent; plan mode (step-by-step diff review); parallel subagents in isolated git worktrees; SuperGrok Heavy subscribers only *(as of 2026-05-15)*`
    >
    > **Add to Recent changes:**
    > `- [2026-05-15] xAI Grok Build enters the terminal coding agent category: plan mode + parallel worktree subagents at feature parity with Claude Code's core agent patterns; early beta, SuperGrok Heavy only`

- [x] **Create** `wiki/sources/newsletters/grok-build-may-2026.md` — source summary (lightweight; main source already captured in codex-mobile-may-2026)

## Page drafts

### wiki/tools/grok-build.md (new)

```markdown
---
title: Grok Build
type: tool
domains: [coding]
subcategory: terminal-coding-agent
tags: [xai, agentic, cli]
as_of: 2026-05-15
sources: [grok-build-may-2026]
---

# Grok Build

xAI's CLI coding agent. Early beta, available to SuperGrok Heavy subscribers via a curl install. Designed for "high-level professional work."

## Current status (as of 2026-05-15)

- Early beta; install via `curl` command; SuperGrok Heavy subscribers only
- **Plan mode**: review and adjust each step before diffs are applied — prevents runaway changes on large tasks
- **Parallel subagents in worktrees**: delegates massive tasks to parallel subagents, each in their own git worktree — same isolation pattern as Claude Code's `--worktree` flag
- No public benchmark data at launch

## Weaknesses / caveats

- Early beta, gated to SuperGrok Heavy subscription tier
- No publicly verified benchmark or real-world performance data yet

## Recent changes

- [2026-05-15] Launched as early beta CLI coding agent

## Sources

- [Grok Build launch — The Code, May 2026](../sources/newsletters/grok-build-may-2026.md)
```

### wiki/sources/newsletters/grok-build-may-2026.md (new)

```markdown
---
title: "Grok Build launch — xAI CLI coding agent (May 2026)"
type: source
source_type: newsletter
source_file: raw/newsletters/2026-05-15-you-can-now-access-codex-on-phone.md
published: 2026-05-15
ingested: 2026-05-18
domains: [coding]
---

# Grok Build launch — xAI CLI coding agent (May 2026)

The Code newsletter reported xAI's release of Grok Build, an early-beta CLI coding agent for SuperGrok Heavy subscribers. Key features: plan mode for step-by-step diff review and parallel subagents in isolated worktrees.

## Influenced pages

- [Grok Build](../../tools/grok-build.md) — new tool page created
- [State of Coding](../../state-of/coding.md) — added to Terminal coding agent subcategory

## Key claims extracted

- Install: `curl` command; SuperGrok Heavy subscribers only
- Plan mode: review/adjust every step before diffs applied
- Parallel subagents in own git worktrees for large tasks
- Framed as "high-level professional work" tool
```
