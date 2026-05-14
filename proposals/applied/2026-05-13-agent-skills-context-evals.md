---
type: proposal
sources:
  - raw/newsletters/2026-05-06-chatgpts-new-default-model-is-here.md
  - raw/newsletters/2026-05-06-chatgpts-new-default-model-just-dropped.md
  - raw/newsletters/2026-04-27-is-developer-burnout-looming.md
  - raw/articles/2026-05-13-tco-iwghr4tzj0.md
status: pending
created: 2026-05-13
---

# Proposal: Agent skills, progressive context, evals, and migration discipline

## Summary

The digest reinforces the newly created agent-skill methodology page: skills need progressive context loading, scoped references, clean subagent contexts, explicit evals, and regression testing when switching models.

## Intended changes

- [x] **Update** `wiki/training/agent-skill-methodology.md` — add model migration and progressive context guidance
    > Add to Proven patterns: `**Regression-test skills after model changes.** When a team switches default models, run the skill's positive and negative cases again. A skill that helped one model may be redundant, harmful, or under-specified for the next.`
    >
    > Add to Proven patterns: `**Use progressive disclosure for references.** Keep the trigger and core principle small; link deeper references, examples, schemas, and tool docs so they load only when the skill is invoked.`

- [x] **Create** `wiki/sources/newsletters/agent-skills-context-evals-2026-05-13.md`
    > See draft below

## Page drafts

### wiki/sources/newsletters/agent-skills-context-evals-2026-05-13.md (new)

```markdown
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
```

