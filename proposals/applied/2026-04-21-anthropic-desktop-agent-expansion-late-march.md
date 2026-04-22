---
type: proposal
sources:
  - raw/newsletters/2026-03-17-why-anthropic-thinks-ai-should-have-its-own-comput.md
  - raw/newsletters/2026-03-19-minimax-m27-rivals-top-models.md
  - raw/newsletters/2026-03-23-anthropic-ships-openclaw-rival.md
status: pending
created: 2026-04-21
---

# Proposal: Anthropic desktop-agent expansion in late March

## Summary

This late-March cluster sharpens a transition the wiki only partially captures today: Anthropic was not just adding isolated Claude features, it was widening Claude into a persistent delegated desktop coworker. The durable signal is the combination of VM-backed local-first execution, longer-horizon planning for ambiguous knowledge work, and phone-triggered continuation through Dispatch and Claude Code Channels.

## Intended changes

- [ ] **Update** `wiki/state-of/computer-use.md` — make Anthropic's entry more explicit about Cowork, Dispatch, and phone-triggered delegation
  > See snippet below.

- [x] **Update** `wiki/tools/claude-cowork.md` — add the late-March product framing that makes Cowork more than an April artifact surface
  > See snippet below.

- [x] **Update** `wiki/tools/claude-code.md` — add Channels / recurring-task context as part of the supervised multi-session story
  > See snippet below.

- [x] **Create** `wiki/sources/newsletters/anthropic-desktop-agent-expansion-late-march.md` — grouped source summary page
  > See full draft below.

## Page drafts

### wiki/state-of/computer-use.md (updated snippet)

```markdown
### Computer use

Autonomous agents that orchestrate models, connect to external services, and execute complex workflows through application interfaces.

- [[tools/claude-cowork]] — Anthropic's late-March push made Claude feel less like a chat product and more like a delegated desktop coworker: VM-backed execution, longer-horizon planning for ambiguous knowledge work, persistent Dispatch sessions, and phone-triggered follow-up through Claude Code Channels *(as of 2026-03-23 for this specific expansion signal; later Cowork / Live Artifacts updates remain reflected on the tool page)*
- [[tools/perplexity-computer]] — Multi-model orchestration layer (19 models); connects to 400+ apps and 12,000+ financial institutions via Plaid; $200/mo Max tier *(as of 2026-04-10)*

## Recent changes

- [2026-03-23] Anthropic's late-March Cowork / Dispatch / Channels cluster clarified the category: delegated desktop work, persistent sessions, and phone-triggered continuation now look like one coherent product direction
```

### wiki/tools/claude-cowork.md (updated snippet)

```markdown
## Current status (as of 2026-04-21)

- Desktop-first agent that works where most knowledge work happens: local files, folders, and everyday applications
- Late-March source material frames Cowork as a more user-friendly, VM-backed superset of Claude Code for non-terminal-native users rather than as a separate narrow productivity toy
- Anthropic explicitly tied Cowork to local-first agent workflows: the VM acts as both safety boundary and capability unlock, letting Claude install tools, run scripts, and operate more independently without the dead-end UX of approving every command
- Dispatch, introduced in March, made Cowork persistent: users could assign work from their phone and return later to a still-running desktop conversation
- Anthropic also tuned Cowork differently from Claude Code: longer planning horizons, heavier use of planning / clarification tools, and evaluation against messy knowledge-work tasks rather than only SWE tasks

## Why it matters

Cowork now reads less like a one-off desktop shell around Claude and more like Anthropic's bet on a general delegated-computer workflow. The same week introduced persistent sessions and then Channels, which suggests the real product is not "desktop app" versus "terminal app" but a continuous agent that can move between local computer, remote session, and mobile supervision.

## Recent changes

- [2026-04-21] Added late-March framing: Cowork is positioned as a VM-backed, local-first delegated desktop workflow, not only an April artifact surface
- [2026-04-21] Added earlier April precursor: Claude for Word beta signaled Anthropic's move into in-app document workflows before Cowork / Live Artifacts
```

### wiki/tools/claude-code.md (updated snippet)

```markdown
## Current status (as of 2026-04-21)

- Terminal CLI agent with persistent project context via `CLAUDE.md`
- Supports subagents, hooks, and background/event-driven flows
- Late-March rollout introduced cloud-following workflows from web/mobile sessions for PR auto-fix and comment-resolution tasks, a useful precursor to the later routines / multi-session-supervision story
- Claude Code Channels extended that direction: existing sessions could be messaged from Telegram or Discord, making the coding agent reachable from the phone without turning it into a separate product
- Recurring tasks, announced alongside Channels, reinforced the shift from one-off terminal loops toward repeatable delegated workflows

## Recent changes

- [2026-04-21] Added late-March Channels / recurring-tasks context: phone-triggered continuation and scheduled workflows strengthen the multi-session supervision direction
- [2026-04-21] Added architecture note from the early-April leak cluster: layered memory, repo-state injection, explicit permissions, and cache-efficient subagent parallelism now read as core Claude Code design choices
```

### wiki/sources/newsletters/anthropic-desktop-agent-expansion-late-march.md (new)

```markdown
---
title: Anthropic desktop-agent expansion in late March
type: source
source_type: newsletter
source_file: raw/newsletters/2026-03-17-why-anthropic-thinks-ai-should-have-its-own-comput.md
ingested: 2026-04-21
domains: [agents, coding, computer-use]
---

# Anthropic desktop-agent expansion in late March

This source cluster captures the week Anthropic's agent story widened from "Claude can code in a terminal" to "Claude can hold delegated work open across a desktop session, a VM, and the phone." The common thread is continuity: local-first execution, persistent sessions, and lightweight mobile supervision.

## Influenced pages

- [[state-of/computer-use]] — clarifies Anthropic's place in the category as delegated desktop work, not just UI control
- [[tools/claude-cowork]] — adds the VM-backed local-first and longer-planning-horizon framing
- [[tools/claude-code]] — adds Channels / recurring tasks as part of the supervised multi-session direction

## Key claims extracted

- Cowork is framed as a more user-friendly, VM-backed cousin or superset of Claude Code for messy knowledge work
- Anthropic treats the VM as both a capability unlock and a safety boundary, instead of relying on "approve every command" UX forever
- Dispatch introduced persistent desktop sessions you could leave running and revisit later
- Claude Code Channels extended existing sessions into Telegram / Discord, making phone-triggered continuation a first-class workflow
- Anthropic describes Cowork and Claude Code as differently optimized harnesses: coding-heavy evals for Claude Code, knowledge-work evals plus heavier planning / clarification for Cowork
- Skills are treated as a portable text-native abstraction layer for reusable workflows across agent surfaces
```

## Comments

* Computer use is about the usage of apps and the browser, and that's not something that I'm seeing in the content that we are adding. Computer use is not just using any computer; using BMS is specifically controlling the computer or the browser so the first Computer Use block is not accurate.