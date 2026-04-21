---
type: proposal
sources:
  - raw/tweets/2026-04-21-claudeai-2044095086460309790.md
  - raw/newsletters/2026-04-16-codenewsletterai-p-google-drops-gemini-3-1-flash-tts-anthrop.md
  - raw/newsletters/2026-04-16-youre-the-manager-now.md
  - raw/tweets/2026-04-21-openai-2044827705406062670.md
status: applied
created: 2026-04-21
---

# Proposal: Agentic coding UIs converge on supervision, not editing

## Summary

This week's coding-tool story is less about one vendor feature and more about interface convergence. Claude Code adds routines and a pane-based desktop workflow. OpenAI pitches Codex as an agent that can use apps, remember preferences, and take on repeatable tasks. Commentary across the batch argues that coding UI is moving toward supervising parallel agents and persistent workflows rather than only reading terminal logs or typing edits directly.

## Intended changes

- [x] **Update** `wiki/tools/claude-code.md` — add routines / scheduled tasks and the desktop redesign direction
  > See snippet below.

- [x] **Update** `wiki/tools/codex.md` — replace "stub page" language with a more current product-shape summary
  > Add computer-use, memory / preferences, image generation, and ongoing-task framing from the official OpenAI post.

- [x] **Update** `wiki/state-of/coding.md` — refresh `Terminal coding agent` wording to reflect the shift from CLI loop to supervised agent workspace
  > Add a new `Recent changes` line:
  > `- [2026-04-21] Claude Code routines and Codex ongoing-task/computer-use push reinforce a shift from single-loop CLI agents toward supervised, repeatable agent workflows`

- [x] **Create** `wiki/sources/tweets/claude-code-routines.md` — source summary
- [x] **Create** `wiki/sources/tweets/openai-codex-ongoing-tasks.md` — source summary

## Page drafts

### wiki/tools/claude-code.md (updated snippet)

```md
---
title: Claude Code
type: tool
domains: [coding, agents]
subcategory: terminal-coding-agent
tags: [anthropic, cli, agentic]
as_of: 2026-04-21
sources: [claude-code-monitor, claude-code-routines]
---

## Current status (as of 2026-04-21)

- Terminal CLI agent with persistent project context via `CLAUDE.md`
- Supports subagents, hooks, and background/event-driven flows
- Monitor tool wakes the agent on external events instead of token-expensive polling
- Routines let a workflow run on a schedule, from an API call, or in response to an event on Anthropic's infrastructure
- Desktop redesign pushes the product toward multi-session supervision rather than a single terminal loop

## Recent changes

- [2026-04-21] Routines announced — scheduled / event-driven Claude Code workflows on Anthropic-hosted infrastructure
- [2026-04-10] Monitor tool announced — event-driven background scripts for Claude Code
```

### wiki/tools/codex.md (updated snippet)

```md
---
title: Codex
type: tool
domains: [coding]
subcategory: terminal-coding-agent
tags: [openai, closed-source, agentic]
as_of: 2026-04-21
sources: [openai-pro-100, ainews-2026-04-21, openai-codex-ongoing-tasks]
---

## Current status (as of 2026-04-21)

- Cloud coding agent accessible from ChatGPT and CLI
- OpenAI now frames Codex as broader than code editing: it can use Mac apps, connect to more tools, create images, learn from prior actions, remember work preferences, and take on repeatable tasks
- Product direction increasingly overlaps with computer use and ongoing workflow automation, not just one-shot coding sessions
```

### wiki/sources/tweets/claude-code-routines.md (new)

```md
---
title: Claude Code routines launch
type: source
source_type: tweet
source_file: raw/tweets/2026-04-21-claudeai-2044095086460309790.md
url: https://x.com/claudeai/status/2044095086460309790
published: 2026-04-21
ingested: 2026-04-21
domains: [coding, agents]
---

# Claude Code routines launch

Anthropic announces routines in Claude Code. A routine packages a prompt, repo, and connectors into a workflow that can run on a schedule, via API call, or in response to an event, using Anthropic-hosted infrastructure.
```

### wiki/sources/tweets/openai-codex-ongoing-tasks.md (new)

```md
---
title: OpenAI — Codex for (almost) everything
type: source
source_type: tweet
source_file: raw/tweets/2026-04-21-openai-2044827705406062670.md
url: https://x.com/openai/status/2044827705406062670
published: 2026-04-21
ingested: 2026-04-21
domains: [coding, agents]
---

# OpenAI — Codex for (almost) everything

OpenAI reframes Codex as more than a coding loop: the official post highlights app use on Mac, broader tool connections, image creation, memory of previous actions, remembered work preferences, and ongoing/repeatable tasks.
```
