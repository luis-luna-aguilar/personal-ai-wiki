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
