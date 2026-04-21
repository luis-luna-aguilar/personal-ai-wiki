---
type: proposal
sources:
  - raw/newsletters/2026-03-26-introducing-plus-one-one-click-openclaw-agents-by.md
  - raw/newsletters/2026-03-27-ainews-everything-is-cli.md
  - raw/newsletters/2026-03-28-china-straps-openclaw-to-robots.md
  - raw/newsletters/2026-03-31-ainews-the-last-4-jobs-in-tech.md
  - raw/tweets/2026-03-27-xcom-mattpocockukstatus203746351702.md
  - raw/tweets/2026-03-27-xcom-mattpocockukstatus203759134083.md
status: pending
created: 2026-04-21
---

# Proposal: Open-agent orchestration in late March

## Summary

The later April wiki already captures orchestration patterns and agent supervision. This late-March batch backfills an earlier phase of the same shift: one-click hosted agents, CLI-first execution, worktree coordination, and the idea that open-agent stacks are maturing around repeatable orchestration rather than chat wrappers.

## Intended changes

- [x] **Update** `wiki/workflows/agentic-orchestration-patterns.md` — add late-March open-stack patterns
  > See snippet below.

- [x] **Update** `wiki/state-of/agents.md` — add a recent-change note on the open-agent orchestration stack
  > See snippet below.

- [x] **Create** `wiki/sources/newsletters/open-agent-orchestration-late-march.md` — grouped source summary page
  > See full draft below.

## Page drafts

### wiki/workflows/agentic-orchestration-patterns.md (updated snippet)

```markdown
## Current patterns

- **CLI-first execution.** For many serious agent workflows, the command line remains the most composable surface because permissions, files, worktrees, and logs stay legible
- **Worktree-based parallelism.** Isolate concurrent agent work in separate branches/worktrees so supervision, diff review, and rollback stay manageable
- **Hosted packaging for repeatable agents.** One-click or prepackaged agents can make a reusable workflow distributable across a team without each user rebuilding the harness from scratch

## Where these patterns surfaced

- Late-March OpenClaw / Plus One coverage reinforced CLI-first execution, one-click packaging, and worktree-style coordination as practical open-agent product directions before the later April orchestration wave
```

### wiki/state-of/agents.md (updated snippet)

```markdown
## Recent changes

- [2026-04-21] Added [[tools/orca]] under `Agent orchestration UIs`; worktree-first desktop supervision layer for Claude Code, Codex, and similar agents
- [2026-03-31] Backfilled late-March signal: open-agent stacks were already converging on CLI-first execution, worktree coordination, and packaged reusable agents before the April orchestration/control-plane wave became clearer
- [2026-04-21] Added earlier Anthropic productivity-surface precursor: Claude for Word beta helps explain Cowork / Live Artifacts as expansion of an existing direction
```

### wiki/sources/newsletters/open-agent-orchestration-late-march.md (new)

```markdown
---
title: Open-agent orchestration in late March
type: source
source_type: newsletter
source_file: raw/newsletters/2026-03-27-ainews-everything-is-cli.md
ingested: 2026-04-21
domains: [agents, coding]
---

# Open-agent orchestration in late March

This source summary groups a late-March cluster on open-agent orchestration. The shared signal is that open stacks were maturing around CLI-first execution, worktree coordination, and packaged repeatable agents instead of thin chat wrappers.

## Influenced pages

- [[workflows/agentic-orchestration-patterns]] — adds CLI-first, worktree-based, and packaged-agent patterns
- [[state-of/agents]] — records the late-March open-stack precursor to the clearer April orchestration wave

## Key claims extracted

- CLI remains the most practical surface for many serious agent workflows
- Worktree or branch isolation is becoming a standard way to supervise concurrent agent work
- One-click / prepackaged agents make reusable workflows easier to share across teams
- Open-agent products were already converging on orchestration and environment control in late March
```

