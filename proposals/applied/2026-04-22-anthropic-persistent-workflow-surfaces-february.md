---
type: proposal
sources:
  - raw/newsletters/2026-02-27-anthropic-drops-claude-code-memory.md
  - raw/newsletters/2026-02-26-perplexity-worked-in-silence-then-dropped-this.md
  - raw/newsletters/2026-03-02-how-should-the-military-use-ai.md
status: pending
created: 2026-04-22
---

# Proposal: Anthropic persistent workflow surfaces in late February

## Summary

This batch strengthens an existing direction already visible in the wiki: Anthropic was turning both Claude Code and Claude Cowork into persistent workflow surfaces before the later April supervision push became obvious. The useful additions are auto-memory, Cowork scheduled tasks, and the `/batch` / `/simplify` framing for repeatable operational work.

## Intended changes

- [x] **Update** `wiki/tools/claude-code.md` — add late-February auto-memory and `/batch` / `/simplify` context
- [x] **Update** `wiki/tools/claude-cowork.md` — add scheduled-tasks context as an earlier persistence primitive
- [x] **Create** `wiki/sources/newsletters/anthropic-persistent-workflow-surfaces-february.md` — source summary page

## Page drafts

### wiki/tools/claude-code.md (updated snippet)

```markdown
## Current status (as of 2026-04-21)

- Late-February expanded Claude Code's persistence story further: auto-memory writes project-local `MEMORY.md` plus topic files, while Boris Cherny previewed `/batch` and `/simplify` as built-in commands for parallel migrations and post-change cleanup
...

## Recent changes

- [2026-02-27] Claude Code added auto-memory for project-local recall of commands, preferences, and architecture context
- [2026-02-28] Boris previewed `/batch` and `/simplify` as built-in primitives for parallel migrations and automated cleanup
...
```

### wiki/tools/claude-cowork.md (updated snippet)

```markdown
## Current status (as of 2026-04-21)

- Scheduled tasks arrived in late February, letting Cowork run recurring briefs, spreadsheet updates, and similar automations on a cadence while the desktop app stayed open
...

## Recent changes

- [2026-02-25] Cowork added scheduled tasks, making recurring delegated work first-class before the later Dispatch / Channels / Live Artifacts expansion
...
```

### wiki/sources/newsletters/anthropic-persistent-workflow-surfaces-february.md (new)

```markdown
---
title: Anthropic persistent workflow surfaces in late February
type: source
source_type: newsletter
source_file: raw/newsletters/2026-02-27-anthropic-drops-claude-code-memory.md
published: 2026-02-27
ingested: 2026-04-22
domains: [coding, agents]
---

# Anthropic persistent workflow surfaces in late February

This source cluster shows Anthropic moving from one-shot sessions toward persistent, repeatable workflows across products. Claude Code gained auto-memory and more explicit operational primitives, while Cowork added recurring scheduled tasks for delegated knowledge work.

## Influenced pages

- [[tools/claude-code]] — adds late-February persistence and built-in workflow primitives
- [[tools/claude-cowork]] — adds scheduled-task context

## Key claims extracted

- Claude Code auto-memory stores project-local context in `MEMORY.md` and topic files
- `/batch` and `/simplify` frame Claude Code as a migration / cleanup workflow engine, not only a chat loop
- Cowork scheduled tasks make recurring delegated knowledge-work automation first-class
- Anthropic's broader product direction is persistence across sessions, devices, and repeated work
```

## Open questions

- None.
