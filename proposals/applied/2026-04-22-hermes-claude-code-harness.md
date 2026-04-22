---
type: proposal
sources:
  - raw/newsletters/2026-04-22-ainews-openai-launches-gpt-image-2.md
  - raw/newsletters/2026-04-22-elon-musk-might-buy-cursor.md
  - raw/newsletters/2026-04-21-the-ai-coding-race-is-heating-up.md
status: pending
created: 2026-04-22
---

# Proposal: Hermes Agent expansion + Claude Code recap + harness additions

## Summary

Three small but coherent updates that all touch the harness layer. (1) Hermes Agent now supports recursive spawn depth in addition to spawn width, ships a macOS GUI called Scarf, and Skillkit native support. (2) Claude Code adds /recap (session gap summaries) and /fewer-permission-prompts skill. (3) The harness concept benefits from two new patterns: agent-friendly CLI design (non-interactive by default, documented flags) and the DSPy 3.2 toolchain entry.

## Intended changes

- [x] **Update** `wiki/tools/hermes-agent.md` — add recursive spawn depth, Scarf GUI, Skillkit; update as_of
    > **Add to `## Current status (as of 2026-04-21)`:**
    > ```
    > - Recursive spawn depth now supported (in addition to spawn width) — enables deeper hierarchical decomposition of long-horizon tasks into nested subagent trees
    > - macOS GUI: Scarf — desktop interface for local Hermes workflows
    > - Skillkit native support added
    > ```
    > **Update `as_of` to `2026-04-22`** in frontmatter.
    >
    > **Add to `## Recent changes`:**
    > ```
    > - [2026-04-22] Recursive spawn depth support added; Scarf macOS GUI launched; Skillkit native support
    > ```

- [x] **Update** `wiki/tools/claude-code.md` — add /recap and /fewer-permission-prompts skill; update as_of
    > **Add to `## Current status (as of 2026-04-21)`:**
    > ```
    > - `/recap`: auto-generates a one-line summary of the last session after 3+ turns of inactivity — triggered only once per gap, never back-to-back, also available on demand via `/recap`
    > - `/fewer-permission-prompts` skill (Boris Cherny): scans session history to identify safe bash and MCP commands that repeatedly trigger permission prompts, then produces an allowlist to approve them once permanently; best run after a few days of work so there's enough history to pull from
    > ```
    > **Update `as_of` to `2026-04-22`** in frontmatter.
    >
    > **Add to `## Recent changes`:**
    > ```
    > - [2026-04-22] Added /recap (session gap summaries after inactivity) and /fewer-permission-prompts skill (history-based allowlist generator)
    > ```

- [x] **Update** `wiki/concepts/harness.md` — add agent-friendly CLI design principle and DSPy 3.2 note
    > **Append to `## What good harness engineering looks like`:**
    > ```
    > - **Agent-friendly CLI design.** Tools built for human interactive use break agent pipelines: interactive prompts stall agents, undocumented flags require inference, and missing non-interactive modes force workarounds. Agent-facing CLI tools should be non-interactive by default, expose all behaviors through explicit flags, and document internal conventions. This applies equally to the tools the agent calls and to the CLIs agents themselves expose. (Source: Cursor engineer Eric Zakariasson, relayed by The Code newsletter.)
    > - **DSPy 3.2** (April 2026) as a harness engineering toolchain: adds Reinforced Language Model (RLM) improvements, optimizer chaining, and LiteLLM decoupling. Relevant for teams iterating on harness prompts and orchestration logic using programmatic optimization.
    > ```
    > **Add to `## Sources`:**
    > ```
    > - [[sources/newsletters/ainews-2026-04-22]]
    > ```

- [x] **Create** `wiki/sources/newsletters/thecode-april-22-2026.md` — source summary
    > See draft below

## Page drafts

### wiki/sources/newsletters/thecode-april-22-2026.md (new)

````md
---
title: The Code newsletter — 2026-04-22 (Cursor/SpaceX, Claude Code recap, CLI design)
type: source
source_type: newsletter
source_file: raw/newsletters/2026-04-22-elon-musk-might-buy-cursor.md
published: 2026-04-22
ingested: 2026-04-22
domains: [coding, agents]
---

# The Code newsletter — 2026-04-22

The Code newsletter for April 22, 2026. Lead story: SpaceX option to acquire Cursor for $60B (or $10B Colossus compute deal). Secondary: Claude Code /recap feature, /fewer-permission-prompts skill, agent-friendly CLI design principles (Eric Zakariasson), Anthropic Mythos leak (Bloomberg), GPT-Image-2 thinking mode.

## Influenced pages

- [[tools/claude-code]] — /recap and /fewer-permission-prompts skill
- [[concepts/harness]] — agent-friendly CLI design principle

## Key claims extracted

- Claude Code /recap: auto-generates one-line session summary after 3+ turns of inactivity; available on demand
- /fewer-permission-prompts: Boris Cherny skill that scans history and produces a bash/MCP allowlist
- CLI-for-agents: agents stall on interactive prompts; need non-interactive flags; Trevin Chow published 7 principles
- SpaceX Cursor option: $60B acquisition or $10B Colossus compute partnership (not applied per triage)
````
