---
title: Latent Space — Claude Code's Next Era (Thariq Shihipar)
type: source
source_type: newsletter
source_file: raw/newsletters/2026-09-29-claude-codes-next-era-thariq-shihipar-anthropi.md
url: https://www.latent.space/p/thariq
published: 2026-09-29
ingested: 2026-10-20
domains: [coding, agents]
---

# Latent Space — Claude Code's Next Era (Thariq Shihipar)

Interview with Anthropic's Thariq Shihipar on where the Claude Code harness is heading: artifacts as the interface, a cloud "brain" with local or remote "hands", Projects as single-user Claude Tag, and Claude Mods for rewriting the harness itself. This page covers the product half; the agent-security half of the episode is not ingested here.

## Influenced pages

- [Claude Code](../../tools/claude-code.md) — Mods, Projects, cloud-brain direction, CLAUDE.md guidance
- [Agent runtime platforms](../../concepts/agent-runtime-platforms.md) — "cloud brain, local hands"

## Key claims extracted

- Claude Mods customise both the execution loop and the UI of Claude Code (CLI and desktop); internally first called "function hooks"; run in-process with access to turn/token counts and messages
- Mods can spawn forked subagents that reuse the prompt cache, parse structured output, and register modes other mods compose with; built with someone from the Bun team
- Example mods: end-of-turn quiz, assumption register, model router, next-steps supervisor, dashboard mod
- Projects: Claude Tag-like supervising agent on Claude's own products, single-player first, without Tag's admin setup
- Direction: separate surface (artifact with its own database), inference (cloud), and hands (local or remote sandbox)
- CLAUDE.md "goes away in the limit"; start new projects without one and add only repeated failure modes; Anthropic will support AGENTS.md
