---
title: Claude Code scheduled tasks and `/loop`
type: source
source_type: newsletter
source_file: raw/newsletters/2026-03-09-claude-code-now-runs-while-you-sleep.md
published: 2026-03-09
ingested: 2026-04-22
domains: [coding, agents]
---

# Claude Code scheduled tasks and `/loop`

This source cluster captures the moment Claude Code stopped looking like only an interactive terminal session and started looking like a recurring background workflow tool. The key additions were local scheduled tasks and `/loop`, which let the agent keep checking on work instead of waiting for the user to restart it manually.

## Influenced pages

- [[tools/claude-code]] — earlier product evidence for recurring automation
- [[state-of/coding]] — strengthens the terminal-agent → workflow-engine story

## Key claims extracted

- Claude Code desktop added local scheduled tasks that run while the machine is awake
- `/loop` allows recurring prompts for up to three days
- Example uses included PR babysitting, CI follow-up, and Slack summary workflows
- These features predate and help explain the later routines / supervision direction
