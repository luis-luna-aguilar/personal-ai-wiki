---
title: fast-jev-compaction
type: tool
domains: [agents, coding]
subcategory: agent-framework
tags: [agentic]
as_of: 2026-10-26
sources: [tamaratran-fast-jev-compaction]
---

# fast-jev-compaction

A public npm library and [Claude Code](claude-code.md) plugin that compacts an agent's context by deleting instead of summarizing. It asks TypeSafe's [Jev](../models/jev.md) decision model which tool calls and results are still needed, drops or truncates the rest, and keeps everything else verbatim, so file paths, exact errors, constraints and commands a summary might lose survive. The pattern is described on [Context editing](../concepts/context-editing.md).

## Current status (as of 2026-10-26)

- Jev sees the whole conversation (tool results replaced by size notes, fitted into about 25K estimated tokens in stages) and returns two keep probabilities per tool call: keep the call, and keep its output word for word.
- At the default 0.5 threshold: keep both; keep the call and cut the result to its first 300 characters plus a note; or remove the pair. User and assistant text, the first message and the newest six messages are never touched.
- Questions are split into parallel requests under Jev's 32K request limit; the default model is `jev-latest` and a TypeSafe API key is required.
- As a plugin it hooks `session.compact` through Claude Code's early-access [function hooks](claude-code-mods.md) (2.1.274+, `CLAUDE_CODE_ENABLE_FUNCTION_HOOKS=1`), so `/compact` and auto-compaction go through Jev, falling back to the built-in summary for short sessions, errors, or too little reduction.
- Installed by adding the repo as a plugin marketplace; the library's building blocks are exported for other harnesses.

## Weaknesses / caveats

- Token counts are estimated from characters, not a tokenizer.
- A keep probability is not proof that a result is safe to delete, though the agent can re-run the tool.
- The full state is resent with every request, so long histories cost several requests per compaction.
- Depends on a gated Claude Code feature and a paid third-party API; the repository is undated.

## Recent changes

- [2026-10-26] Page created from the public repository: deletion-only compaction scored by Jev, shipped as an npm library and a Claude Code function-hook plugin.

## Sources

- [tamaratran/fast-jev-compaction (GitHub)](../sources/repos/tamaratran-fast-jev-compaction.md)
