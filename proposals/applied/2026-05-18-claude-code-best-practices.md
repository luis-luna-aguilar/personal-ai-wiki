---
type: proposal
source: raw/articles/2026-05-18-anthropiccom-engineering-claude-code-best-practices.md
status: pending
created: 2026-05-18
---

# Proposal: Claude Code best practices (Anthropic engineering blog)

## Summary

Anthropic's engineering blog published internal best practices for using Claude Code at scale. Core thesis: the context window is the #1 resource to manage. Key patterns: give Claude explicit verification criteria before starting, use explore-plan-code workflow with plan mode, use the Chrome extension for UI screenshot verification.

## Intended changes

- [x] **Update** `wiki/tools/claude-code.md` — update `as_of`, add source to frontmatter, add Best practices section, add Recent changes entry
    > **`as_of`:** `2026-05-13` → `2026-05-18`
    >
    > **Sources frontmatter:** add `anthropic-claude-code-best-practices-2026-05`
    >
    > **Add new section after `## Routines`:**
    >
    > ```md
    > ## Best practices (Anthropic engineering, May 2026)
    >
    > **Context window management**
    > - Context window is the #1 resource; performance degrades as it fills; the custom status line tracks context usage for exactly this reason
    > - Start a new session when context is full rather than continuing in a degraded state
    >
    > **Verification criteria**
    > - Always give Claude a way to verify its own work before reporting done: run the tests, take a screenshot, execute a command and check the output
    > - Without a verification criterion, Claude marks tasks complete based on code inspection alone — missing runtime failures
    >
    > **Explore-plan-code workflow**
    > - Step 1 (Explore): Claude reads relevant files in plan mode — no edits permitted
    > - Step 2 (Plan): Claude writes a plan doc; press Ctrl+G to open it in a text editor for review and editing before any code is written
    > - Step 3 (Code): Claude implements against the approved plan; commits after each logical unit
    > - Skip plan mode for small or clearly-scoped tasks — overhead is only worth it for multi-file or uncertain-approach work
    >
    > **UI verification**
    > - The Claude Chrome extension lets Claude take screenshots of the running app to verify visual output
    > - Closes the loop between a code change and the rendered result without requiring a human to look
    > ```
    >
    > **Add to Recent changes (top):**
    > `- [2026-05-18] Anthropic engineering best practices: context window as #1 constraint; verification-criteria pattern; explore-plan-code workflow (plan mode + Ctrl+G); Chrome extension for UI screenshot verification`

- [x] **Create** `wiki/sources/articles/anthropic-claude-code-best-practices-2026-05.md`
    > See draft below

## Page drafts

### wiki/sources/articles/anthropic-claude-code-best-practices-2026-05.md (new)

```md
---
title: Claude Code at scale — Anthropic engineering best practices
type: source
source_type: article
source_file: raw/articles/2026-05-18-anthropiccom-engineering-claude-code-best-practices.md
url: https://anthropic.com/engineering/claude-code-best-practices
published: 2026-05-18
ingested: 2026-05-18
domains: [coding]
---

# Claude Code at scale — Anthropic engineering best practices

Anthropic's engineering blog post on how they use Claude Code internally. Central thesis: the context window is the primary resource to manage; performance degrades as it fills. Recommends giving Claude explicit verification criteria before starting any task so it can self-verify rather than report done based on code inspection alone. Describes an explore-plan-code workflow: Claude reads files in plan mode (no edits), writes a plan doc that the human edits via Ctrl+G, then implements. Chrome extension lets Claude take screenshots of the running app for UI verification. Advises skipping plan mode for small-scope tasks.

## Influenced pages

- [Claude Code](../../tools/claude-code.md) — new Best practices section

## Key claims extracted

- Context window is the #1 resource; performance degrades as it fills
- Verification criteria pattern: give Claude tests, screenshots, or commands to confirm work is done before reporting complete
- Explore-plan-code: plan mode (no edits) → plan doc → Ctrl+G to edit in text editor → implement → commit
- Chrome extension for UI screenshot verification
- Skip plan mode for small/clear-scope tasks
```
