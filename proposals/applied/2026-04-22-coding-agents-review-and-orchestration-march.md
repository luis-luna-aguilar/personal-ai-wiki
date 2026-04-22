---
type: proposal
sources:
  - raw/newsletters/2026-03-10-anthropic-drops-claude-code-review.md
  - raw/articles/2026-03-11-developersopenaicom-codexlearnbest-practices.md
  - raw/tweets/2026-03-11-xcom-trq212status203150629669713135.md
status: pending
created: 2026-04-22
---

# Proposal: Coding agents shift toward review and concurrent supervision

## Summary

This early-March cluster matters less as a single feature drop than as a workflow inflection point. Claude Code Review made multi-agent PR review a first-class product, `/btw` made it easier to supervise active work without collapsing the main task thread, and OpenAI's Codex guide explicitly framed AGENTS.md, MCP, skills, review, and automations as the normal operating model rather than advanced tricks.

The wiki already reflects the later April version of this shift. This proposal backfills the March signal so the current pages show where that direction became legible.

## Intended changes

- [x] **Update** `wiki/tools/claude-code.md` — add the March Code Review and `/btw` signals as early evidence of the move from one-shot CLI assistance toward supervised concurrent workflows
  > See diff snippet below.

- [x] **Update** `wiki/tools/codex.md` — add the March best-practices guide as the clearest early statement of Codex's operating model: scoped prompting, durable repo guidance, MCP, skills, review, and automation
  > See diff snippet below.

- [x] **Create** `wiki/sources/newsletters/coding-agents-review-and-orchestration-march.md` — source summary page for the cluster
  > See full draft below.

## Page drafts

### wiki/tools/claude-code.md (updated snippet)

```markdown
## Current status (as of 2026-04-21)

- Terminal CLI agent with persistent project context via `CLAUDE.md`
- Supports subagents, hooks, and background/event-driven flows
- March 2026 already hinted at the later supervision direction: Code Review introduced a managed multi-agent PR-review system on Anthropic infrastructure, while `/btw` enabled side-chain conversations during active work instead of forcing users to interrupt the main thread
- Late-March rollout introduced cloud-following workflows from web/mobile sessions for PR auto-fix and comment-resolution tasks, a useful precursor to the later routines / multi-session-supervision story
- Claude Code Channels extended that direction: existing sessions could be messaged from Telegram or Discord, making the coding agent reachable from the phone without turning it into a separate product
```

### wiki/tools/codex.md (updated snippet)

```markdown
## Current status (as of 2026-04-21)

- Cloud coding agent accessible from ChatGPT and CLI
- OpenAI's March 2026 best-practices guide made the intended operating model unusually explicit: give Codex a clear goal/context/constraints/done-when structure, move durable repo guidance into `AGENTS.md`, connect live external systems with MCP, turn repeated work into skills, and automate workflows only after they are stable manually
- OpenAI now frames Codex as broader than code editing: it can use Mac apps, connect to more tools, create images, learn from prior actions, remember work preferences, and take on repeatable tasks
- Product direction increasingly overlaps with computer use and ongoing workflow automation, not just one-shot coding sessions

## Recent changes

- [2026-04-21] OpenAI reframes Codex around app use, memory/preferences, image creation, and repeatable tasks
- [2026-04-21] Codex Chronicle research preview — ambient screen memory; macOS Pro rollout
- [2026-03-11] Best-practices guide codified the AGENTS.md + MCP + skills + automation workflow as the default way to get better Codex results
- [2026-04-10] Page created from OpenAI Pro tier pricing announcement
```

### wiki/sources/newsletters/coding-agents-review-and-orchestration-march.md (new)

```markdown
---
title: Coding agents move toward review and concurrent supervision
type: source
source_type: newsletter
source_file: raw/newsletters/2026-03-10-anthropic-drops-claude-code-review.md
published: 2026-03-10
ingested: 2026-04-22
domains: [coding, agents]
---

# Coding agents move toward review and concurrent supervision

This source summary groups an early-March cluster on how coding-agent products were starting to change shape. The common signal is that the center of gravity was moving away from "ask for code in one thread" and toward supervised, concurrent, and reusable workflows: multi-agent review, side-channel supervision, and explicit operating guidance for durable agent setup.

## Influenced pages

- [[tools/claude-code]] — adds the March Code Review and `/btw` signals as early evidence of the product's supervision direction
- [[tools/codex]] — grounds the product's AGENTS.md / MCP / skills / automation framing in an earlier first-party guide

## Key claims extracted

- Claude Code Review launched as a managed multi-agent PR-review system that verifies findings and ranks them by severity
- Anthropic reported substantive PR comments increasing from 16% to 54% internally after adopting that workflow
- `/btw` introduced side-chain conversations during active Claude Code work, making supervision less serial
- OpenAI's Codex guide framed durable repo guidance, external context connections, skills, review, and automation as core workflow primitives rather than niche setup
```

## Open questions

- None.
