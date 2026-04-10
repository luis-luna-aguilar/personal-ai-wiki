---
title: My Claude Code toolkit
type: personal
as_of: 2026-04-10
---

# My Claude Code toolkit

Features and patterns I'm actively using or should adopt inside Claude Code. Linked to wiki pages for context.

## Monitor tool

Background scripts that wake Claude up when an event occurs — instead of polling, Claude sleeps until something goes wrong.

Practical uses for me:
- Watch dev server for errors during long agent runs
- Poll a PR for status changes (CI pass/fail, review comments)
- Track failing tests during a refactor without burning tokens on idle loops

See: [[tools/claude-code]]

## To explore

- Hooks (SessionStart, pre/post tool) — auto-load git context, enforce patterns
- Subagents — parallel work on independent tasks
- MCP servers — extend Claude Code with custom tools
