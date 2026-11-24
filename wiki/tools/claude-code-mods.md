---
title: Claude Code Mods
type: tool
domains: [coding, agents]
subcategory: terminal-coding-agent
tags: [anthropic, cli, agentic]
as_of: 2026-10-26
sources: [latent-space-thariq-claude-code-next-era-2026-09-29, latent-space-claude-mods-2026-10-21, tamaratran-fast-jev-compaction]
---

# Claude Code Mods

Mods are [Claude Code](claude-code.md)'s plugin layer: TypeScript or JavaScript functions that run inside the CLI and desktop harness and react to prompts, tool calls and screen renders. Anthropic now builds parts of Claude Code itself this way.

## Current status (as of 2026-10-26)

- **Claude Mods:** in-process "function hooks" for the CLI and desktop harness. Unlike shell hooks, a mod sees turn/token counts and messages, can spawn forked subagents that reuse the prompt cache, parse structured output, change the UI, and register modes other mods compose with. Examples: end-of-turn quiz, assumption register, model router, next-steps supervisor. Function hooks are early access from Claude Code 2.1.274 and need `CLAUDE_CODE_ENABLE_FUNCTION_HOOKS=1`; third-party plugins already use them to replace built-in behaviour, for example [fast-jev-compaction](fast-jev-compaction.md), which hooks `session.compact` to swap the `/compact` summary for model-scored pruning (see [Context editing](../concepts/context-editing.md)).
- **Built-in mods:** Anthropic now builds parts of Claude Code as mods, listed under /plugin → Installed → Built-in: `agents-md` (loads AGENTS.md as project instructions), `diff` (the /diff pane), `plugin-authoring` (the skill Claude uses to write mods for you), `sec-default` (guards organization-managed settings from user-installed mods), `telemetry`, and `you-should-know`, the only one off by default: a side agent that flags things buried in the trace, such as about 45 files of uncommitted work before a discard. Third-party supervisor mods cost tokens: ModSmith's Next Steps Supervisor fired on 99 of 111 turns at about 5–6k input-equivalent tokens per check on a 50k-token session.

## Weaknesses / caveats

- Mods are not sandboxed: a loaded mod can read and write files, see every prompt, and spend usage, and built-in mods keep running under `--safe-mode`, so third-party mods need a code read before install

## Related

- [Claude Code](claude-code.md) — the parent tool page
- [fast-jev-compaction](fast-jev-compaction.md) — a third-party plugin built on function hooks
- [Harness (agent)](../concepts/harness.md) — what a harness is and how it is customized

## Recent changes

- [2026-11-24] Page created, split out of [Claude Code](claude-code.md): the Claude Mods and built-in mods bullets and the unsandboxed-mods caveat.
- [2026-10-26] Function hooks confirmed as early access (2.1.274+, opt-in env flag); the third-party [fast-jev-compaction](fast-jev-compaction.md) plugin uses them to replace the `/compact` summary with pruning.
- [2026-10-21] Six built-in mods documented (agents-md, diff, plugin-authoring, sec-default, telemetry, opt-in you-should-know side agent); mods are unsandboxed and built-ins run under `--safe-mode`.
- [2026-09-29] Thariq Shihipar (Latent Space) details Claude Mods: in-process function hooks with forked cache-sharing subagents, UI changes and composable modes.

## Sources

- [Latent Space — Claude Code's Next Era (Thariq Shihipar)](../sources/newsletters/latent-space-thariq-claude-code-next-era-2026-09-29.md)
- [Latent Space — Claude Mods: Flipping the Harness Inside Out](../sources/newsletters/latent-space-claude-mods-2026-10-21.md)
- [tamaratran/fast-jev-compaction (GitHub)](../sources/repos/tamaratran-fast-jev-compaction.md)
