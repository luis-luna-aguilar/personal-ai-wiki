---
type: proposal
sources:
  - raw/newsletters/2026-05-07-elons-new-alliance.md
  - raw/articles/2026-05-07-platformclaudecom-docsenmanaged-agentsdefine-out.md
status: pending
created: 2026-05-13
---

# Proposal: Anthropic/SpaceX compute deal + Claude Managed Agents "Dreams" self-improvement

## Summary

Two Anthropic signals from the same week. (1) Anthropic signed a compute deal with SpaceX's Colossus 1 data center — 220,000+ NVIDIA GPUs — and immediately doubled Claude Code limits on paid plans. Timing is notable given the ongoing Musk vs. Altman court battle. (2) Claude Managed Agents added a "Dreams" feature: agents periodically reflect on past sessions to identify long-term patterns invisible in a single session (recurring mistakes, shared user preferences, stale assumptions), producing a consolidated memory store for future sessions. Available in research preview.

## Intended changes

- [x] **Update** `wiki/tools/claude-managed-agents.md` — add Dreams feature to current status and recent changes; update `as_of` and `sources`
    > See diff snippets below

- [x] **Update** `wiki/state-of/models.md` — add Anthropic infrastructure note to Recent changes
    > **Append to Recent changes:**
    > `- [2026-05-07] Anthropic signs compute deal with SpaceX Colossus 1: 220K+ NVIDIA GPUs; doubled Claude Code limits on paid plans immediately; notable context: Musk vs. Altman court battle ongoing`

- [x] **Update** `wiki/tools/claude-code.md` — note doubled limits (add to existing recent changes entry or as a standalone bullet in current status)
    > **Append to Current status section:**
    > `- Paid plan limits doubled (May 2026) following SpaceX/Colossus 1 compute deal (220K+ NVIDIA GPUs)`

- [x] **Create** `wiki/sources/newsletters/anthropic-spacex-dreams-2026-05-07.md`
    > See draft below

## Page drafts

### wiki/tools/claude-managed-agents.md — diff snippets

**Frontmatter `as_of`:**
> **Before:** `as_of: 2026-04-24`
> **After:** `as_of: 2026-05-07`

**Frontmatter `sources` — append:**
> Add `anthropic-spacex-dreams-2026-05-07`

**Current status — append after the last bullet in the existing `## Current status` block:**
```
- **Dreams feature** (May 2026, research preview): agents periodically reflect on past sessions to identify long-term patterns that no single session can surface — recurring mistakes, shared user preferences, stale assumptions. The reflection produces a cleaned-up, consolidated memory store that improves future session performance. Available in research preview; request access via Claude's form.
```

**Recent changes — prepend:**
```
- [2026-05-07] Dreams feature added (research preview): periodic session reflection producing consolidated memory stores for long-term pattern recognition across sessions; available via research preview access request
- [2026-04-24] Built-in memory launched in public beta: file-backed stores, scoped sharing, audit logs, rollback/redaction controls
```

### wiki/sources/newsletters/anthropic-spacex-dreams-2026-05-07.md (new)

```markdown
---
title: Anthropic SpaceX compute deal and Claude Managed Agents Dreams feature
type: source
source_type: newsletter
source_file: raw/newsletters/2026-05-07-elons-new-alliance.md
published: 2026-05-07
ingested: 2026-05-13
domains: [agents, models]
---

# Anthropic SpaceX compute deal and Claude Managed Agents Dreams feature

Superhuman AI newsletter (May 7) covers the SpaceX/Colossus 1 deal and Claude Managed Agents Dreams in the same issue. The Anthropic platform docs article for "Define outcomes" was also forwarded this week but was a stub with minimal content.

## Influenced pages

- [Claude Managed Agents](../../tools/claude-managed-agents.md) — Dreams feature added
- [State of Models](../../state-of/models.md) — Anthropic infrastructure note
- [Claude Code](../../tools/claude-code.md) — doubled limits note

## Key claims extracted

### SpaceX / Colossus 1 deal
- Anthropic signed a compute access agreement with SpaceX's Colossus 1 data center
- Access: 220,000+ NVIDIA GPUs
- Immediate effect: doubled Claude Code limits on paid plans
- Context: Elon Musk (SpaceX) and Sam Altman (OpenAI) are simultaneously in court; SpaceX now powers Anthropic (an OpenAI competitor)

### Dreams feature (Claude Managed Agents)
- Feature name: Dreams
- Mechanism: agents periodically reflect on past sessions (not just the current one) to identify patterns that accumulate across many sessions — recurring mistakes, shared user preferences, assumptions that have gone stale
- Output: a cleaned-up, consolidated memory store that replaces or supplements the prior raw accumulated memory
- Purpose: self-improvement over time without requiring human curation of the memory store
- Status: research preview; access via request form on claude.com
```

