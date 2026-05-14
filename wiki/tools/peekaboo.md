---
title: Peekaboo
type: tool
domains: [computer-use, agents]
subcategory: computer-use
tags: [open-source, cli, agentic]
as_of: 2026-05-11
sources: [peekaboo-repo-2026-05-13]
---

# Peekaboo

Peekaboo is an open-source macOS computer-use layer for AI agents. It ships as a native CLI plus optional MCP server, giving tools such as Claude Code, Codex, and Cursor a way to capture screens, detect UI elements, and execute GUI actions on macOS.

## Current status (as of 2026-05-11)

- Current GitHub release shown: v3.1.2, released 2026-05-11; v3.0.0 shipped the major computer-use refactor on 2026-05-09
- MIT-licensed, Swift-first repo; GitHub shows roughly 3.9k stars and 283 forks at ingest time
- Requires macOS 15+ plus Screen Recording and Accessibility permissions
- Supports pixel-accurate captures across windows, screens, menu bar, and Retina output
- Provides action-first UI automation: click, type, scroll, hotkey, menu, window, app, dock, Space, dialog, set-value, and perform-action
- Runs as a CLI or MCP server, with the same tool surface exposed to agent hosts
- Supports local and remote model providers for visual analysis, including OpenAI, Anthropic, xAI, Google, and Ollama models

## Why it matters

Peekaboo fills a different slot from hosted computer-use agents such as Perplexity Computer or Codex browser workflows. It is a local macOS action layer: a way for agent hosts to see and manipulate real desktop applications through structured commands and MCP.

Version 3 is especially relevant because it unifies screenshot and UI detection flows across CLI and MCP, adds action-first automation before synthetic input fallback, and returns structured JSON that agents can script against.

## Strengths

- Local, open-source, and MCP-compatible
- Strong fit for Claude Code / Codex / Cursor workflows that need to operate real macOS apps
- Structured command surface is more agent-friendly than raw screenshot-only computer use
- Action-first accessibility operations can be more reliable than coordinate-only clicking when apps expose usable accessibility metadata

## Weaknesses / caveats

- macOS-only; requires local Screen Recording and Accessibility permissions
- Automation reliability depends on target app accessibility support
- Local desktop automation has a larger safety surface than read-only screenshot capture, so it needs careful permission and workflow boundaries

## Related

- [State of Computer Use](../state-of/computer-use.md) - category dashboard for agents operating through real application UIs.
- [MCP](../concepts/mcp.md) - protocol layer used to expose Peekaboo to compatible agent hosts.

## Recent changes

- [2026-05-11] v3.1.2 latest release shown on GitHub; release automation fix
- [2026-05-09] v3.0.0: native action-first automation, shared screenshot/UI detection pipeline across CLI and MCP, structured diagnostics/JSON, and broader command refactor

## Sources

- [Peekaboo GitHub repo](../sources/repos/peekaboo-repo-2026-05-13.md)
