---
type: proposal
source: raw/repos/tamaratran-fast-jev-compaction.md
status: pending
created: 2026-10-26
---

# Proposal: fast-jev-compaction — compaction by deletion instead of summary

## Summary

### In short
Context compaction does not have to summarize: a public Claude Code plugin keeps every kept message verbatim and only deletes tool calls and results that a fast decision model scores as no longer needed, so exact paths, errors and constraints survive. It uses TypeSafe's Jev model and replaces Claude Code's built-in `/compact` summary through the new function hooks. The proposal adds the pattern to Agent memory's context-editing section, a function-hooks note to Claude Code, and one source page. Reason to hesitate: the repo carries no date, so the ingest date stands in.

[[#Open questions|Open questions: 2 to answer.]]

- [ ] **Approve all** — checking this box approves every item in `## Intended changes` and `## Schema / vocabulary additions` below; the individual boxes may stay empty.

### The source
The GitHub repository `tamaratran/fast-jev-compaction` is both an npm library and a Claude Code plugin. Its argument is that ordinary compaction, where a model summarizes old turns to free context, is lossy: a file path, an exact error message, a constraint or a command can disappear even though it matters later. This package never rewrites anything. It sends Jev, TypeSafe's decision model, the whole conversation so far, with every tool result replaced by a short size note, and asks two questions about each tool call: should the call itself stay, and should its output stay word for word. Each answer comes back as a keep probability.

Above a threshold (0.5 by default) the call and result stay; if only the call is worth keeping, the result is cut to its first 300 characters plus a note; otherwise both go. User and assistant text is never removed, and the first message and the newest six are pinned. The state is squeezed into about 25,000 tokens in stages and split into parallel requests under Jev's 32K request limit. The README is candid about limits: token counts are estimated from characters, and a probability is not proof a result is safe to delete, although the agent can always re-run the tool.

As a plugin it hooks Claude Code's `session.compact` through function hooks, an early-access feature from Claude Code 2.1.274 that must be switched on with an environment flag. After install, `/compact` and auto-compaction go through Jev, falling back to the built-in summary for short sessions, errors, or when too little would be removed.

### What changes
Agent memory has a section on agents editing their own context, all from August research, and Claude Code's page describes function hooks (Claude Mods) without saying they are gated or that third-party plugins already use them.

- **Agent memory** gains one bullet in "Context editing and persistent state" describing deletion-only, model-scored compaction and its fallback. Page date moves to 26 October.
- **Claude Code** gains one sentence on the Claude Mods bullet: function hooks are early access from 2.1.274 behind an opt-in flag, with this plugin as a worked example. The Recent-changes list is at its cap, so its oldest entry (Sonnet 5 arriving in Claude Code, 30 June) moves to history. Page date moves to 26 October.
- One new source page for the repository.

### What to weigh
The hub maps "context engineering" to Harness, and compaction is context engineering, so Harness is arguably the home; it is already at 110% of its ceiling, and Agent memory already holds the wiki's context-editing material, so the pattern goes there. Neither page reaches 110% after the change. The 26 October date is the ingest date, not a release date.

## Intended changes

- [ ] **Update** `wiki/concepts/agent-memory.md` — add one bullet at the end of the list in `## Context editing and persistent state`; Current-status stamp and `as_of` move to 2026-10-26; adds one Recent-changes entry dated 2026-10-26 (live list has 5, no spill); append one source id and link
    > See draft below

- [ ] **Update** `wiki/tools/claude-code.md` — append one sentence to the Claude Mods bullet in `## Mods, Projects, and cloud sessions`; Current-status stamp and `as_of` move to 2026-10-26; adds one Recent-changes entry dated 2026-10-26 (live list has 10, at the cap); append one source id and link
    > See draft below

- [ ] **Spill** `wiki/tools/claude-code.md` → `wiki/history/tools/claude-code.md` — the oldest Recent-changes entry (expected: [2026-06-30] Claude Sonnet 5 in Claude Code) moves to history
    > See draft below

- [ ] **Create** `wiki/sources/repos/tamaratran-fast-jev-compaction.md` — source summary

## Page drafts

### wiki/concepts/agent-memory.md (updated)

Frontmatter (changed fields):

```
as_of: 2026-10-26
sources: [agent-memory-without-vector-db, memory-vs-context-rot-february, agent-memory-systems-layer-2026-06, minteval-paper-2026-05, ainews-erdos-benchmarks-cluster-2026-05-21, ainews-openai-shuts-off-cursor-2026-08-29, ainews-fal-h3-max-live-2026-09-01, cognition-agent-memory-repo-2026-10, ainews-devin-dreaming-2026-10-06, tamaratran-fast-jev-compaction]
```

`## Current status` — heading stamp only:

```
## Current status (as of 2026-10-26)
```

`## Context editing and persistent state` — append one bullet after the "A persistent knowledge store carries much of the gain" bullet:

```
- **Compaction by deletion instead of summary.** The public `fast-jev-compaction` npm package (October 2026) replaces Claude Code's compaction summary with pruning. It sends TypeSafe's Jev decision model the whole conversation, with tool results shortened to size notes, and gets two keep probabilities per tool call: is the call still worth knowing about, and is its output still needed word for word. Below the threshold the output is cut to its first 300 characters or the call is removed with its result. User and assistant text, the first message, and the newest messages are never touched, and everything kept stays verbatim, so the file paths, exact errors, and constraints a summary can lose survive. It falls back to the built-in summary when it cannot remove enough. The author's caveat: a keep probability is not proof a result is safe to delete, though the agent can re-run the tool.
```

`## Recent changes` — insert one entry above the 2026-10-19 entry:

```
- [2026-10-26] Added deletion-only compaction (fast-jev-compaction): a decision model scores each tool call and result for keeping, and kept messages stay verbatim instead of being summarized.
```

`## Sources` — append:

```
- [tamaratran/fast-jev-compaction (GitHub)](../sources/repos/tamaratran-fast-jev-compaction.md)
```

### wiki/tools/claude-code.md (updated)

Frontmatter: `as_of: 2026-10-26`; append one id (`tamaratran-fast-jev-compaction`) to the live `sources:` list.

`## Current status` — heading stamp only:

```
## Current status (as of 2026-10-26)
```

`## Mods, Projects, and cloud sessions` — the Claude Mods bullet becomes:

```
- **Claude Mods:** in-process "function hooks" for the CLI and desktop harness. Unlike shell hooks, a mod sees turn/token counts and messages, can spawn forked subagents that reuse the prompt cache, parse structured output, change the UI, and register modes other mods compose with. Examples: end-of-turn quiz, assumption register, model router, next-steps supervisor. Function hooks are early access from Claude Code 2.1.274 and need `CLAUDE_CODE_ENABLE_FUNCTION_HOOKS=1`; third-party plugins already use them to replace built-in behaviour, for example `fast-jev-compaction`, which hooks `session.compact` to swap the `/compact` summary for model-scored pruning (see [Agent memory](../concepts/agent-memory.md)).
```

`## Recent changes` — insert one entry above the 2026-10-21 entry, then remove the oldest entry (see Spill):

```
- [2026-10-26] Function hooks confirmed as early access (2.1.274+, opt-in env flag); the third-party fast-jev-compaction plugin uses them to replace the `/compact` summary with pruning.
```

`## Sources` — append:

```
- [tamaratran/fast-jev-compaction (GitHub)](../sources/repos/tamaratran-fast-jev-compaction.md)
```

### wiki/history/tools/claude-code.md (updated — spill)

Append at the end of the file:

```

## Archived from current page on 2026-10-26

- [2026-06-30] Claude Sonnet 5 became available in Claude Code and via the API as `claude-sonnet-5`, alongside Claude Fable 5's return two days later — Claude Code's model lineup moved from a single fast-mode tier to multiple concurrently available models.
```

### wiki/sources/repos/tamaratran-fast-jev-compaction.md (new)

```
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
- [Agent memory](../../concepts/agent-memory.md) — deletion-only compaction added to the context-editing section
- [Claude Code](../../tools/claude-code.md) — function hooks gated as early access; third-party compaction plugin as an example

## Key claims extracted
- Summaries are lossy: paths, exact errors, constraints, and commands can disappear; this library only deletes tool calls and results
- Every `tool_use` is paired with its `tool_result`; calls in the first message and the newest `preserveRecentMessages` (default 6) are pinned
- State sent to Jev is fitted into ~25K estimated tokens in stages; requests stay under ~30K, below Jev's 32K request limit, and run concurrently
- Per call: keep result ≥ threshold (default 0.5) → keep both; else keep call ≥ threshold → keep call, truncate result to 300 characters plus a note; else remove both
- Token counts are estimated from characters, not a tokenizer; a probability is not proof a result is safe to delete
- Defaults: model `jev-latest`, endpoint `https://api.typesafe.ai/v1/systemone`
- Claude Code function hooks are early access (2.1.274+) and require `CLAUDE_CODE_ENABLE_FUNCTION_HOOKS=1`; installed via the repo as a plugin marketplace
- Falls back to Claude Code's built-in summary for short sessions, failures, or insufficient reduction
```

## Schema / vocabulary additions

None.

## Open questions

- Should the plugin get its own tool page, or is a pattern bullet plus the Claude Code mention enough (assumed enough)?
- TypeSafe's Jev now appears on Expand Fetch, ScaleDown, MedDecider-27B and here with no page of its own. Should a `models/jev.md` page be proposed later from a primary TypeSafe source?
