---
type: proposal
source: raw/articles/2026-04-10-xcom-noahzweben-status-2042332268450963774.md
status: pending
created: 2026-04-10
---

# Proposal: Claude Code Monitor tool

## Summary

Anthropic shipped a Monitor tool for Claude Code that lets the agent create background scripts which wake it up when an event occurs (log error, failing test, PR status change). Saves tokens by replacing polling with event-driven triggers.

## Intended changes

- [x] **Create** `wiki/tools/claude-code.md` — new tool page for Claude Code; includes Monitor tool as a key feature
    > See draft below

- [x] **Update** `wiki/state-of/coding.md` — add new subcategory `terminal-coding-agent` with Claude Code
    > **Add after the "Agentic DevOps" section:**
    > ```
    > ### Terminal coding agent
    >
    > CLI-based AI coding agents that run in the terminal, operating autonomously across file editing, shell commands, and tool use without a graphical IDE.
    >
    > - [[tools/claude-code]] — Anthropic; terminal-first agent with background Monitor tool for event-driven wakeups *(as of 2026-04-10)*
    > ```
    > **Add to Recent changes:**
    > `- [2026-04-10] Added `terminal-coding-agent` subcategory with [[tools/claude-code]] after Monitor tool announcement`

- [x] **Create** `wiki/sources/articles/claude-code-monitor.md` — source summary

## Page drafts

### wiki/tools/claude-code.md (new)

```
---
title: Claude Code
type: tool
domains: [coding, agents]
subcategory: terminal-coding-agent
tags: [anthropic, cli, agentic]
as_of: 2026-04-10
sources: [claude-code-monitor]
---

# Claude Code

Anthropic's terminal-first AI coding agent. Runs in the shell, operates autonomously on files, shell commands, and tool calls. Part of the Claude product family.

## Current status (as of 2026-04-10)

- Terminal CLI agent — no IDE required
- Supports subagents, hooks, and persistent project context via CLAUDE.md
- New **Monitor tool** lets Claude create background scripts that wake the agent on events instead of polling — saves tokens
- Monitor use cases: follow logs for errors, poll PR status via script, watch dev server health, track failing tests

## Monitor tool

The Monitor tool (announced 2026-04-10) lets Claude Code create background scripts that run independently and wake the agent only when a relevant event occurs. This replaces token-expensive polling loops with event-driven triggers. The agent can set monitors for:

- Dev server errors or crashes
- Test suite failures
- PR status changes (via script)
- Production launch health over extended periods

## Strengths

- Terminal-native — fits into existing shell workflows
- Event-driven monitoring reduces token waste vs polling
- Extensible via hooks, MCPs, skills, and subagents

## Weaknesses / caveats

- Requires comfort with CLI workflows
- Monitor tool is new; real-world patterns still emerging

## Recent changes

- [2026-04-10] Monitor tool announced — event-driven background scripts for Claude Code

## Sources

- [[sources/articles/claude-code-monitor]]
```

### wiki/sources/articles/claude-code-monitor.md (new)

```
---
title: Claude Code Monitor tool announcement
type: source
source_type: tweet
source_file: raw/articles/2026-04-10-xcom-noahzweben-status-2042332268450963774.md
url: https://x.com/noahzweben/status/2042332268450963774
published: 2026-04-10
ingested: 2026-04-10
domains: [coding, agents]
---

# Claude Code Monitor tool announcement

Noah Zweben (Anthropic) announces the Monitor tool for Claude Code: background scripts that wake the agent on events instead of polling. Saves tokens and supports log following, PR polling, and similar use cases.

## Influenced pages

- [[tools/claude-code]] — new page created
- [[state-of/coding]] — added terminal-coding-agent subcategory

## Key claims extracted

- Monitor tool lets Claude create background scripts that wake the agent when needed
- Replaces polling in the agent loop — big token saver
- Can follow logs for errors, poll PRs via script, and more
```

## Schema / vocabulary additions

- [x] Add new subcategory `terminal-coding-agent` to `wiki/_schema/subcategories.md`:
    ```
    ### terminal-coding-agent
    - **Parent domain(s):** coding, agents
    - **Applies to types:** tool
    - **Definition:** CLI-based AI coding agents that run in the terminal, operating autonomously across file editing, shell commands, and tool use without a graphical IDE.
    - **Examples:** [[tools/claude-code]]
    ```

## Open questions

- Should Codex (OpenAI) also go under `terminal-coding-agent`? It's a cloud agent accessed via CLI. Can add later when ingesting a dedicated Codex source.
	- Yes, it should.

## Comments

-  some of these tools I already use in Claude Code and Codex. Let's make use of my personal space outside the wiki and start collecting stuff that's useful for me. For me this monitor tool in Claude Code is very relevant. Let's add it there as a paragraph summary with a link to this page as the tools that I should be using inside Claude Code 