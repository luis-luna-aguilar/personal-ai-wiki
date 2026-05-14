---
title: Agent skills, context loading, evals, and migration discipline
type: source
source_type: newsletter
source_file: raw/newsletters/2026-05-06-chatgpts-new-default-model-is-here.md
published: 2026-05-06
ingested: 2026-05-13
domains: [agents, coding]
---

# Agent skills, context loading, evals, and migration discipline

May 2026 coverage around SKILL.md-style workflows and Claude Code environment configuration points to a common operating pattern: small loaders, scoped references, clean subagent contexts, explicit evals, and regression testing when models change.

## Influenced pages

- [Agent skill methodology](../../training/agent-skill-methodology.md)

## Key claims extracted

- Skills should load context progressively rather than dumping all references into every run.
- Positive and negative test cases are useful for preserving trigger quality.
- Model changes require regression testing because the same skill can behave differently across models.
