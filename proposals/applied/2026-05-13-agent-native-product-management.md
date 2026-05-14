---
type: proposal
sources:
  - raw/articles/2026-05-13-everyto-guides-ai-product-management-guide.md
  - raw/newsletters/2026-05-03-codex-goes-to-work.md
status: pending
created: 2026-05-13
---

# Proposal: Agent-native product management workflows

## Summary

Every's guide describes Claude/Codex-style product-management commands such as `/ce:strategy` and `/ce:product-pulse` that turn strategy interviews and analytics review into persistent product memory. This updates existing product-building guidance and Claude Code's non-engineering workflow coverage.

## Intended changes

- [x] **Update** `wiki/training/ai-native-product-building.md` — add agent-native PM command pattern
    > Add to Current guidance: `Agent-native product management workflows increasingly look like commandable rituals: strategy interviews, product-pulse reviews, roadmap synthesis, issue generation, and memory updates that persist across planning cycles.`

- [x] **Update** `wiki/tools/claude-code.md` — connect product-management workflows to command packs
    > Add to Current status near product-management bullet: `Every's product-management guide adds command-pack examples such as strategy interviews and product-pulse reviews, reinforcing Claude Code as a product workflow surface, not only a code editor.`

- [x] **Create** `wiki/sources/articles/agent-native-product-management-2026-05-13.md`
    > See draft below

## Page drafts

### wiki/sources/articles/agent-native-product-management-2026-05-13.md (new)

```markdown
---
title: Agent-native product management guide — Every
type: source
source_type: article
source_file: raw/articles/2026-05-13-everyto-guides-ai-product-management-guide.md
published: 2026-05-13
ingested: 2026-05-13
domains: [agents, coding]
---

# Agent-native product management guide — Every

Every's guide describes agent-native product-management workflows using Claude/Codex-style commands such as `/ce:strategy` and `/ce:product-pulse`. The workflows convert strategy interviews, analytics review, product memory, and roadmap decisions into persistent context for future planning cycles.

## Influenced pages

- [AI-native product building](../../training/ai-native-product-building.md)
- [Claude Code](../../tools/claude-code.md)

## Key claims extracted

- Product-management work can be packaged as repeatable agent commands.
- Strategy, analytics review, and product memory are persistent artifacts, not one-off chats.
- Roadmaps remain high-judgment artifacts even when agents help gather context and draft options.
```

