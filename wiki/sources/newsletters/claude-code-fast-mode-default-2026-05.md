---
title: Claude Code Fast mode becomes default + spec-drift logging
type: source
source_type: newsletter
published: 2026-05-19
ingested: 2026-05-19
domains: [coding]
---

# Claude Code Fast mode becomes default + spec-drift logging

Coverage from AINews and The Code newsletter (2026-05-19): Anthropic promoted Fast mode (Opus 4.7) from research preview to the default for Claude Code. Also: prompt cache diagnostics added to Claude Console. Secondary: an Anthropic Claude Code engineer (@trq212) shared the spec-drift logging pattern — append a prompt to any implementation request to make Claude maintain `implementation-notes.html` with its design decisions and deviations.

## Influenced pages

- [Claude Code](../../tools/claude-code.md) — Fast mode default; prompt cache diagnostics
- [Anti-autopilot review friction](../../training/anti-autopilot-review-friction.md) — spec-drift logging pattern

## Key claims extracted

- Fast mode (Opus 4.7) is now default in Claude Code — was research preview
- Claude Console gains prompt cache diagnostics (hit/miss rate visibility)
- Spec-drift logging: implementation-notes.html prompt forces agent to document its decisions as it works; readable once complete before reviewing code
