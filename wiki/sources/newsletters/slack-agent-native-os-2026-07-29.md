---
title: "What If Slack Was Your AI Command Center"
type: source
source_type: newsletter
source_file: raw/newsletters/2026-07-29-what-if-slack-was-your-ai-command-center.md
url: https://every.to/context-window/what-if-slack-was-your-ai-command-center
published: 2026-07-29
ingested: 2026-09-07
domains: [agents, training]
---

# What If Slack Was Your AI Command Center

Every profiles Nityesh Agarwal's "Luo Ji," a personal Slack bot wired to Claude Code that maps top-level channel messages to new agent sessions and thread replies to resumed sessions, turning Slack into a project dashboard with per-channel model routing; he open-sourced the pattern as "Claude Home Base." The same issue notes Block shipped Buzz, an independently-built open-source shared workspace for humans and AI agents with a similar channel/thread shape.

## Influenced pages

- [Company-wide AI enablement](../../training/company-wide-ai-enablement.md) — new "thread-per-task chat orchestration" proven pattern, plus an evidence-from-practice line

## Key claims extracted

- Nityesh Agarwal (Every) built "Luo Ji," a Slack bot connected to Claude Code; top-level channel messages start new Claude Code sessions, thread replies resume the same session
- Per-channel model routing: most channels default to Opus; a dedicated channel is reserved for Fable, with CLAUDE.md instructions to delegate execution to Opus subagents
- Open-sourced the pattern as "Claude Home Base" (github.com/nityeshaga/claude-home-base)
- Block (Jack Dorsey) released Buzz on 2026-07-21: an open-source "shared workspace where humans and AI agents work together"; described by an early tester as "a Slack clone with a different color"
- Early Buzz test: agents started Codex tasks with self-written prompts and posted results into a shared thread
