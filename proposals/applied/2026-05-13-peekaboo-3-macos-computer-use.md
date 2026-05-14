---
type: proposal
sources:
  - https://github.com/openclaw/Peekaboo
  - raw/tweets/2026-05-13-steipete-2053114837698249190.md
status: pending
created: 2026-05-13
---

# Proposal: Peekaboo 3.0 macOS computer-use release

## Summary

The Peekaboo GitHub repo confirms the tweet's core claim. Peekaboo is an MIT-licensed macOS CLI and optional MCP server that gives agents high-fidelity screenshot capture, UI detection, and GUI automation. Version 3 adds native agent flows, action-first automation, shared screenshot/UI detection across CLI and MCP, structured JSON, and multi-screen automation; the current release shown on GitHub is v3.1.2 from 2026-05-11.

## Intended changes

- [x] **Create** `wiki/tools/peekaboo.md` — macOS computer-use action layer for agents
    > See draft below

- [x] **Update** `wiki/state-of/computer-use.md` — add Peekaboo under Computer use as a local macOS action layer
    > Add under `### Computer use`: `- [Peekaboo](../tools/peekaboo.md) — open-source macOS CLI + MCP server for agent screen capture, UI detection, and action-first GUI automation; v3.0 unified screenshot/UI detection across CLI and MCP and added native agent flows *(as of 2026-05-11)*`

- [x] **Update** `wiki/index.md` — add Peekaboo under Tools
    > Add: `- [tools/peekaboo](tools/peekaboo.md) — open-source macOS CLI and MCP server for agent screen capture, UI detection, and GUI automation *(as_of: 2026-05-11)*`

- [x] **Create** `wiki/sources/repos/peekaboo-repo-2026-05-13.md` — source summary
    > See draft below

## Page drafts

### wiki/tools/peekaboo.md (new)

```markdown
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

## Recent changes

- [2026-05-11] v3.1.2 latest release shown on GitHub; release automation fix
- [2026-05-09] v3.0.0: native action-first automation, shared screenshot/UI detection pipeline across CLI and MCP, structured diagnostics/JSON, and broader command refactor

## Sources

- [Peekaboo GitHub repo](../sources/repos/peekaboo-repo-2026-05-13.md)
```

### wiki/sources/repos/peekaboo-repo-2026-05-13.md (new)

```markdown
---
title: Peekaboo GitHub repo
type: source
source_type: repo
url: https://github.com/openclaw/Peekaboo
published: 2026-05-11
ingested: 2026-05-13
domains: [computer-use, agents]
---

# Peekaboo GitHub repo

Peekaboo is an open-source macOS CLI and optional MCP server for agent computer use. The repo describes high-fidelity screen capture, AI analysis, and GUI automation, with v3 adding native agent flows and multi-screen automation across CLI and MCP.

## Influenced pages

- [Peekaboo](../../tools/peekaboo.md) — new tool page
- [State of Computer Use](../../state-of/computer-use.md) — add local macOS computer-use action layer

## Key claims extracted

- Peekaboo is a macOS CLI plus optional MCP server for AI-agent screenshot capture, visual analysis, and GUI automation.
- v3 adds native agent flows and multi-screen automation across CLI and MCP.
- The tool surface includes screenshot/observation commands plus click, type, scroll, hotkey, menu, window, app, dock, Space, dialog, set-value, and perform-action actions.
- The MCP server is intended for Codex, Claude Code, Cursor, and similar agent hosts.
- The changelog says v3.0.0, released 2026-05-09, made action-first automation the default for supported UI controls and unified screenshot/UI detection flows across CLI and MCP.
- The current GitHub release shown is v3.1.2 from 2026-05-11.
```

