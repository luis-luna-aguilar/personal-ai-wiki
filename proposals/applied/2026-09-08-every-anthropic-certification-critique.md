---
type: proposal
source: raw/newsletters/2026-08-31-what-we-learned-from-15-hours-of-anthropic-certifi.md
status: pending
created: 2026-09-08
---

# Proposal: Every's critique of Anthropic's certification training

## Summary

### The source

Every had roughly 10 staff complete Anthropic's new certification program — four courses (Introduction to Agent Skills, Building with Claude API, Introduction to MCP, Claude Code in Action) taking 10-15 hours per person — to formalize a year-plus partnership as alpha testers. Their conclusion: the courses are useful mainly for establishing a shared vocabulary (what Anthropic itself means by "skill," "MCP," "API") rather than teaching workflow transformation, and Anthropic's own documentation is "the gold standard" for anyone who actually wants depth. Two concrete weaknesses stood out: the content is already stale in places (the API course uses a Sonnet model no longer available via the API; the MCP course doesn't mention Anthropic's own MCP-builder skill), and the courses are one-size-fits-all with no role-based tailoring or prior-knowledge assessment — reactions from the 10 test-takers split sharply by role, from "largely unnecessary" (a non-technical team member who'd already shipped apps via vibe coding) to "should be part of onboarding" (a growth engineer who found the API course's system-design and prompt-evaluation sections unusually well compacted).

### What changes

`training/ai-engineering-skills.md` currently covers only Andrew Ng's four-skill taxonomy from his DeepLearning.AI relaunch — a different but adjacent take on what practitioners need to learn. This proposal adds a first "Evidence from practice" section documenting Every's certification review as a second, competing data point on how the field is currently trying to formalize AI-engineering education, bumps `as_of` to 2026-08-31, and adds a second Recent-changes entry (the page currently has only one, from its creation).

### What to weigh

This content could also have gone on `training/company-wide-ai-enablement.md`, which is the wiki's general-purpose adoption-guidance page — but that page is already very large, and this proposal treats the certification review as thematically closer to `ai-engineering-skills.md`'s specific focus on how the field is defining and teaching AI-engineering competence, not general org-wide adoption. This is a reasonable but non-obvious placement call.

## Intended changes

- [x] **Approve all** — checking this box approves every item below; the individual boxes may stay empty.

- [ ] **Update** `wiki/training/ai-engineering-skills.md` — add "Evidence from practice" section, bump `as_of`, add Recent-changes entry
    > See draft below

- [ ] **Create** `wiki/sources/newsletters/every-anthropic-certification-critique-2026-08-31.md` — source summary

## Page drafts

### wiki/training/ai-engineering-skills.md (updated)

```md
---
as_of: 2026-08-31
sources: [ainews-andrew-ng-ai-engineering-2026-08-25, every-anthropic-certification-critique-2026-08-31]
---

## Evidence from practice

- **Every's review of Anthropic's certification program (August 2026):** roughly 10 Every staff completed Anthropic's new 4-course certification (Agent Skills, Claude API, MCP, Claude Code — 10-15 hours total). Conclusion: the courses mainly succeed at establishing shared vocabulary (what Anthropic means by "skill," "MCP," "API") rather than teaching workflow transformation, and Anthropic's own documentation is "the gold standard" for anyone who wants real depth. Weaknesses: content already stale in places (a deprecated Sonnet API model used in examples, no mention of Anthropic's own MCP-builder skill), and one-size-fits-all delivery with no role-based tailoring — reactions split sharply by role, from "largely unnecessary" to "should be part of onboarding."

## Open questions

(... existing bullets unchanged ...)

## Recent changes

- [2026-08-31] Added Every's practitioner review of Anthropic's certification program as a first "Evidence from practice" section: useful mainly for shared vocabulary, not workflow transformation; stale content and no role-based tailoring were the main weaknesses cited.
- [2026-08-25] Page created from Andrew Ng's DeepLearning.AI relaunch around four AI Engineering skills, based on a 10,000+ job-posting analysis plus hiring-manager interviews.
```

### wiki/sources/newsletters/every-anthropic-certification-critique-2026-08-31.md (new)

```md
---
title: "What We Learned From 15 Hours of Anthropic Certification Training"
type: source
source_type: newsletter
source_file: raw/newsletters/2026-08-31-what-we-learned-from-15-hours-of-anthropic-certifi.md
url: https://every.to/p/what-we-learned-from-15-hours-of-anthropic-certification-training
published: 2026-08-31
ingested: 2026-09-08
domains: [training]
---

# What We Learned From 15 Hours of Anthropic Certification Training

Every's Natalia Quintero reviews Anthropic's new 4-course certification program (Agent Skills, Claude API, MCP, Claude Code), based on ~10 staff completing it, concluding it's most useful for shared vocabulary rather than workflow transformation.

## Influenced pages

- [AI Engineering skills](../../training/ai-engineering-skills.md) — first "Evidence from practice" section

## Key claims extracted

- 4 courses, 10-15 hours total: Agent Skills, Claude API, MCP, Claude Code in Action
- Main value: shared vocabulary/definitions, not workflow transformation; Anthropic's own docs are "the gold standard" for depth
- Stale content: deprecated Sonnet API model used, no mention of Anthropic's own MCP-builder skill
- One-size-fits-all delivery, no role-based tailoring; reactions split sharply by role
```
