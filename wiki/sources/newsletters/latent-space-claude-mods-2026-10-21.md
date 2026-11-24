---
title: 'Latent Space — Claude Mods: Flipping the Harness Inside Out'
type: source
source_type: newsletter
source_file: raw/newsletters/2026-10-21-claude-mods-flipping-the-harness-inside-out.md
url: https://www.latent.space/p/claude-mods
published: 2026-10-21
ingested: 2026-11-24
domains: [coding, agents]
---

# Latent Space — Claude Mods: Flipping the Harness Inside Out

An essay arguing that Claude Mods turn the harness from an agent-to-machine interface into an "Attention Interface" toward the human. It lists the mods Anthropic ships built in, walks through you-should-know and the author's open-source Next Steps Supervisor (ModSmith), and counts the costs.

## Influenced pages
- [Claude Code Mods](../../tools/claude-code-mods.md) — built-in mods bullet, AGENTS.md loader, mod-trust caveat, Recent-changes entry

## Key claims extracted
- A mod is a Claude Code plugin of TypeScript/JavaScript functions that run inside Claude Code (CLI and Desktop), react to events such as prompts, tool calls and renders, and can observe, re-render or replace the default handling
- Six built-in mods under /plugin → Installed → Built-in: agents-md (loads AGENTS.md as project instructions), diff, plugin-authoring, sec-default, telemetry, you-should-know (the only one off by default)
- you-should-know is a side agent that flags important things buried in the trace. In the author's example it caught about 45 files of uncommitted work before a discard
- Next Steps Supervisor (ModSmith) runs after turns that edit files, run commands or make 8+ tool calls: 99 of 111 turns since 2026-10-15. Its README estimates about 5–6k input-equivalent tokens per check on a 50k-token session
- Per Anthropic's docs, mods aren't sandboxed: a loaded mod can read and write files, see every prompt and spend usage. Built-in mods keep running under `--safe-mode`
