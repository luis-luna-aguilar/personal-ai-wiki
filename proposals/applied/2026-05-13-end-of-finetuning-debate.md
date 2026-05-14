---
type: proposal
sources:
  - raw/newsletters/2026-05-13-ainews-the-end-of-finetuning.md
status: pending
created: 2026-05-13
---

# Proposal: "End of finetuning" debate — OpenAI deprecates finetuning APIs

## Summary

OpenAI is deprecating its finetuning APIs, sparking a debate about whether finetuning is still relevant for most AI engineers. The emerging consensus: for ~80% of use cases, long-context prompts and system prompts may be sufficient or superior. The counterpoint from the top tier: Cursor and Cognition (whose $25B valuation round is now publicly confirmed) have *increased* their open-model RLFT usage, treating weight-level specialization as central to their custom ASIC strategy.

## Intended changes

- [x] **Update** `wiki/state-of/models.md` — add finetuning debate note to Recent changes; update `as_of` and `sources`
    > See diff snippets below

- [x] **Update** `wiki/state-of/coding.md` — add Cognition $25B round note to Recent changes
    > **Append to Recent changes:**
    > `- [2026-05-13] Cognition $25B valuation round publicly confirmed; among top-tier coding shops increasing open-model RLFT investment (not decreasing) alongside OpenAI finetuning API deprecation`

- [x] **Create** `wiki/sources/newsletters/end-of-finetuning-debate-2026-05-13.md`
    > See draft below

## Page drafts

### wiki/state-of/models.md — diff snippets

**Frontmatter `as_of`:**
> **Before:** `as_of: 2026-05-05`
> **After:** `as_of: 2026-05-13`

**Frontmatter `sources` — append:**
> Add `end-of-finetuning-debate-2026-05-13`

**Recent changes — prepend:**
```
- [2026-05-13] "End of finetuning" debate: OpenAI deprecating finetuning APIs; consensus forming that long-context prompts suffice for ~80% of use cases; counterpoint from top tier (Cursor, Cognition $25B) is increased open-model RLFT, not decreased — weight specialization remains central to their custom-ASIC strategy
```

### wiki/sources/newsletters/end-of-finetuning-debate-2026-05-13.md (new)

```markdown
---
title: "End of finetuning" debate — OpenAI API deprecation and top-tier RLFT counter-trend
type: source
source_type: newsletter
source_file: raw/newsletters/2026-05-13-ainews-the-end-of-finetuning.md
published: 2026-05-13
ingested: 2026-05-13
domains: [models]
---

# "End of finetuning" debate — OpenAI API deprecation and top-tier RLFT counter-trend

AINews newsletter dated May 13, 2026. Covers the OpenAI finetuning API deprecation, the resulting debate, and the divergent behavior of top-tier AI coding shops.

## Influenced pages

- [State of Models](../../state-of/models.md) — finetuning debate added to Recent changes
- [State of Coding](../../state-of/coding.md) — Cognition $25B note added to Recent changes

## Key claims extracted

- OpenAI is deprecating its finetuning APIs (specific APIs not named in newsletter; refers to the existing finetuning endpoint suite)
- Emerging consensus among practitioners: for the median ~80% of use cases, long-context prompts and system-prompt engineering (e.g. Claude's Constitutional AI approach) are sufficient or superior to finetuning
- Claude's Constitution (Anthropic's system-prompt-as-spec pattern) is cited as evidence that weight-level finetuning may not be the default path for model customization
- Counter-trend at the top tier: Cursor and Cognition are among the shops **increasing** open-model RLFT (Reinforcement Learning from Fine-Tuning) investment, not decreasing it
- Top-tier thesis: custom open-model finetunes are central to their custom ASIC strategy; weight-level specialization still required for peak performance at that tier
- Cognition $25B valuation round now publicly confirmed this week (reported alongside this debate)
- Same newsletter also covers supply chain attacks and Qwen local benchmarks (separate proposals)
```

