---
type: proposal
sources:
  - raw/newsletters/2026-03-24-claude-now-controls-your-computer.md
  - raw/newsletters/2026-03-24-claude-gets-new-powers.md
  - raw/newsletters/2026-03-26-ainews-the-biggest-claude-launch-of-all-time.md
  - raw/newsletters/2026-03-27-ainews-everything-is-cli.md
  - raw/newsletters/2026-03-31-anthropic-drops-claude-code-computer-use.md
  - raw/tweets/2026-03-24-xcom-claudeaistatus2036195789601374.md
status: pending
created: 2026-04-21
---

# Proposal: Claude computer use in late March

## Summary

This March cluster is now historically important even though the wiki has newer April coverage. It captures the moment Anthropic widened Claude from a terminal/browser coding agent into a remote computer operator and unattended cloud worker, which helps explain why later pages like [[tools/claude-cowork]] and April Claude Code workflow expansions took the shape they did.

## Intended changes

- [x] **Update** `wiki/state-of/computer-use.md` — add Anthropic's March computer-use push as a second major entry on the page
  > See snippet below.

- [x] **Update** `wiki/tools/claude-code.md` — add the late-March unattended cloud-workflow precursor
  > See snippet below.

- [x] **Create** `wiki/sources/newsletters/claude-computer-use-late-march.md` — grouped source summary page
  > See full draft below.

## Page drafts

### wiki/state-of/computer-use.md (updated snippet)

```markdown
## Subcategories

### Computer use

Autonomous agents that orchestrate models, connect to external services, and execute complex workflows through application interfaces.

- [[tools/claude-cowork]] — Anthropic's March 2026 computer-use push widened Claude from chat/terminal workflows into remote desktop control and unattended knowledge-work execution; later April Cowork / Live Artifacts moves now read as expansion of that direction rather than a separate product idea *(as of 2026-04-10 for current page state; March launch context added from 2026-03-24 to 2026-03-31 sources)*
- [[tools/perplexity-computer]] — Multi-model orchestration layer (19 models); connects to 400+ apps and 12,000+ financial institutions via Plaid; $200/mo Max tier *(as of 2026-04-10)*

## Recent changes

- [2026-04-10] Page created with [[tools/perplexity-computer]] as first entry after triaging Superhuman AI newsletter
- [2026-03-31] Backfilled March Anthropic computer-use signal: remote macOS control, phone-triggered delegation, and cloud-following Claude Code sessions
```

### wiki/tools/claude-code.md (updated snippet)

```markdown
## Current status (as of 2026-04-21)

- Terminal CLI agent with persistent project context via `CLAUDE.md`
- Supports subagents, hooks, and background/event-driven flows
- Late-March rollout introduced cloud-following workflows from web/mobile sessions for PR auto-fix and comment-resolution tasks, a useful precursor to the later routines / multi-session-supervision story
- Monitor tool wakes the agent on external events instead of token-expensive polling

## Recent changes

- [2026-04-21] Added architecture note from the early-April leak cluster: layered memory, repo-state injection, explicit permissions, and cache-efficient subagent parallelism now read as core Claude Code design choices
- [2026-04-21] Routines announced — scheduled / event-driven Claude Code workflows on Anthropic-hosted infrastructure
- [2026-04-10] Monitor tool announced — event-driven background scripts for Claude Code
- [2026-03-27] Claude Code gained unattended cloud-following workflows from web/mobile sessions for PR fixes and comment resolution
```

### wiki/sources/newsletters/claude-computer-use-late-march.md (new)

```markdown
---
title: Claude computer use in late March
type: source
source_type: newsletter
source_file: raw/newsletters/2026-03-24-claude-now-controls-your-computer.md
ingested: 2026-04-21
domains: [coding, agents]
---

# Claude computer use in late March

This source summary groups the late-March source cluster around Anthropic's computer-use expansion. The main takeaway is that Claude moved beyond browser or terminal-only interaction into remote control of real desktop software and unattended cloud-following coding workflows.

## Influenced pages

- [[state-of/computer-use]] — adds Anthropic's March computer-use push as an early major category signal
- [[tools/claude-code]] — adds the cloud-following PR-fix / comment-resolution precursor to later hosted workflow features

## Key claims extracted

- Anthropic positioned Claude as able to control a Mac through mouse, keyboard, and application interaction
- The launch was framed as meaningful because it let Claude work inside messy real software environments rather than only through APIs
- Claude Code also picked up unattended web/mobile-triggered workflows for PR-following auto-fix and comment resolution
- Late-April Cowork / Live Artifacts moves are easier to understand as expansion of this March product direction
```

