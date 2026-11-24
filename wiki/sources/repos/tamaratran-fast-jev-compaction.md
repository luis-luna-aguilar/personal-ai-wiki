---
title: tamaratran/fast-jev-compaction (GitHub)
type: source
source_type: repo
source_file: raw/repos/tamaratran-fast-jev-compaction.md
url: https://github.com/tamaratran/fast-jev-compaction
ingested: 2026-10-26
domains: [agents, coding]
---

# tamaratran/fast-jev-compaction (GitHub)

An npm library and Claude Code plugin that replaces summary-based context compaction with deletion. The whole conversation (tool results replaced by size notes) is sent to TypeSafe's Jev decision model, which returns two keep probabilities per tool call (keep the call; keep its output verbatim). Calls and results below a threshold are truncated or removed; user and assistant text, the first message, and the newest messages are never touched, and nothing kept is rewritten. The plugin hooks Claude Code's `session.compact` through early-access function hooks (2.1.274+) and falls back to the built-in summary on errors or insufficient reduction. The repository is undated.

## Influenced pages
- [fast-jev-compaction](../../tools/fast-jev-compaction.md) — new tool page
- [Context editing](../../concepts/context-editing.md) — deletion-only compaction (moved from Agent memory)
- [Knowledge term map](../../concepts/knowledge-term-map.md) — "compaction" mapped to Context editing
- [Claude Code Mods](../../tools/claude-code-mods.md) — function hooks gated as early access; third-party compaction plugin as an example
- [Jev](../../models/jev.md) — used as the keep/drop decision engine for context compaction

## Key claims extracted
- Summaries are lossy: paths, exact errors, constraints, and commands can disappear; this library only deletes tool calls and results
- Every `tool_use` is paired with its `tool_result`; calls in the first message and the newest `preserveRecentMessages` (default 6) are pinned
- State sent to Jev is fitted into ~25K estimated tokens in stages; requests stay under ~30K, below Jev's 32K request limit, and run concurrently
- Per call: keep result ≥ threshold (default 0.5) → keep both; else keep call ≥ threshold → keep call, truncate result to 300 characters plus a note; else remove both
- Token counts are estimated from characters, not a tokenizer; a probability is not proof a result is safe to delete
- Defaults: model `jev-latest`, endpoint `https://api.typesafe.ai/v1/systemone`
- Claude Code function hooks are early access (2.1.274+) and require `CLAUDE_CODE_ENABLE_FUNCTION_HOOKS=1`; installed via the repo as a plugin marketplace
- Falls back to Claude Code's built-in summary for short sessions, failures, or insufficient reduction
