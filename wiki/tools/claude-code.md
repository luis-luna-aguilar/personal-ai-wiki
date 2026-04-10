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
