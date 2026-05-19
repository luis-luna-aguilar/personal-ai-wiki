---
type: proposal
sources:
  - raw/newsletters/2026-05-19-ainews-how-to-land-a-job-at-a-frontier-lab-on-p.md
  - raw/newsletters/2026-05-19-the-ai-boom-divides-silicon-valley.md
status: pending
created: 2026-05-19
---

# Proposal: Claude Code Fast mode now default + spec-drift logging pattern

## Summary

Two updates: (1) Anthropic shipped Fast mode (Opus 4.7) as the default for Claude Code rather than research preview, and added prompt cache diagnostics in Claude Console. (2) An Anthropic Claude Code engineer shared a spec-drift logging pattern: appending a prompt to any implementation request that asks Claude to maintain a running `implementation-notes.html` file documenting every design decision, deviation, and tradeoff as it works.

## Intended changes

- [x] **Update** `wiki/tools/claude-code.md` — note Fast mode as now default (was research preview); add Claude Console prompt cache diagnostics; update `as_of`
    > See diff below

- [x] **Update** `wiki/training/anti-autopilot-review-friction.md` — add spec-drift logging pattern as a proven review friction technique
    > See diff below

- [x] **Create** `wiki/sources/newsletters/claude-code-fast-mode-default-2026-05.md` — source summary

## Page drafts

### wiki/tools/claude-code.md — update to `## Current status`

Replace the fast mode bullet:

> **Before:** `- Opus 4.7 fast mode (May 2026, research preview via API and Claude Code): Cursor reports 2.5× faster output at approximately 6× the cost compared to standard Opus 4.7; adds a new latency/price tier above the standard frontier tier`

> **After:** `- Opus 4.7 fast mode (now default, as of 2026-05-19): was research preview; now the default mode for Claude Code; Cursor reports 2.5× faster output at approximately 6× the cost compared to standard Opus 4.7`

Add a new bullet after that:

```md
- Claude Console prompt cache diagnostics (May 2026): developers can now see cache hit/miss rates for their Claude Code sessions in Claude Console; useful for debugging context reuse and cost efficiency in multi-agent setups
```

Update `as_of` in frontmatter to `2026-05-19`.

Add to `## Recent changes`:

```
- [2026-05-19] Fast mode promoted from research preview to default for Claude Code; Claude Console gains prompt cache diagnostics
```

### wiki/training/anti-autopilot-review-friction.md — add to `## Proven patterns`

```md
- **Spec-drift logging (implementation-notes.html).** Append this to any implementation request to force the agent to document its own decision-making as it works:

  ```
  As you work, maintain a running implementation-notes.html file that captures:
  - Design decisions: choices you made where the spec was ambiguous
  - Deviations: places where you intentionally departed from the spec, and why
  - Tradeoffs: alternatives you considered and why you picked what you did
  - Open questions: anything you'd want me to confirm or revise
  ```

  Reading the file once the task is finished tells you exactly which decisions were made and why before you dive into the code — converting invisible inference into a reviewable artifact. Source: Anthropic Claude Code engineer (@trq212, May 2026). See also [agent-generated HTML artifacts](../workflows/agent-generated-html-artifacts.md) for the broader rationale for HTML over Markdown in agent-produced outputs.
```

Update `as_of` in frontmatter to `2026-05-19`.

Add to `## Recent changes`:

```
- [2026-05-19] Spec-drift logging pattern: append implementation-notes.html prompt to expose Claude's design decisions, deviations, and tradeoffs as a reviewable artifact (Anthropic engineer, @trq212)
```

### wiki/sources/newsletters/claude-code-fast-mode-default-2026-05.md (new)

```md
---
title: Claude Code Fast mode becomes default + spec-drift logging
type: source
source_type: newsletter
url: https://twitter.com/ClaudeDevs
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
```
