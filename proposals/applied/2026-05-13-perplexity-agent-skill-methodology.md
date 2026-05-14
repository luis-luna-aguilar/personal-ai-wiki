---
type: proposal
sources:
  - raw/newsletters/2026-05-12-the-fallacy-of-the-16-hour-agent.md
status: pending
created: 2026-05-13
---

# Proposal: Perplexity agent skill methodology — write evals first, not procedures

## Summary

Perplexity published its internal methodology for building agent skills that don't rot in production. Five principles: (1) write 5–10 test cases before writing the skill, including negative examples. (2) Use natural user language for triggers, not technical phrases. (3) Write the skill body as principles, not step-by-step procedures. (4) Codify production failures as standing instructions in the skill file. (5) Cut every line the agent would get right without it.

## Intended changes

- [x] **Create** `wiki/training/agent-skill-methodology.md` — new training page
    > See draft below

- [x] **Create** `wiki/sources/newsletters/perplexity-agent-skill-methodology-2026-05-12.md`
    > See draft below

- [x] **Update** `wiki/index.md` — add entry for `training/agent-skill-methodology`

## Page drafts

### wiki/training/agent-skill-methodology.md (new)

```markdown
---
title: Agent skill methodology
type: training
tags: [agents, evals, coding]
as_of: 2026-05-12
sources: [perplexity-agent-skill-methodology-2026-05-12]
---

# Agent skill methodology

How to build agent skills that work reliably in production and stay maintainable over time. Based on Perplexity's published internal methodology.

## Current guidance

The core problem: skills written as step-by-step procedures become stale, redundant, or broken as the underlying model improves or the task changes. Perplexity's answer is an evals-first, principles-based approach.

## Proven patterns

**1. Write test cases before writing the skill**
Write 5–10 test cases *before* writing the skill body. Include:
- Positive cases: queries that should invoke this skill
- Negative cases: queries that look similar but should NOT invoke this skill (prevents over-triggering)

**2. Use natural user language for triggers**
Phrase triggers the way users actually talk, not the way engineers think about the task:
- Good: `"babysit a PR"`, `"watch CI until it passes"`
- Bad: `"monitor_ci_pipeline"`, `"pull_request_surveillance_mode"`

**3. Write principles, not procedures**
The model already knows how to use tools — it needs direction, not instructions it would follow anyway:
- Good: `"When CI fails, investigate the root cause before retrying. Prioritize actionable errors."`
- Bad: `"Step 1: run git status. Step 2: check the CI logs. Step 3: ..."`

**4. Codify production failures as standing instructions**
When the agent fails in production, add a corrective instruction directly to the skill file. This turns each failure into a durable improvement rather than a temporary fix.
- Example: `"Do not close the PR if tests are still running. Wait for a definitive pass or fail."`

**5. Cut every line the agent would get right without it**
Before shipping, delete every line that the model would follow correctly on its own. Bloated skill files add noise, slow iteration, and make failures harder to diagnose.
- Test: would a senior engineer reading this for the first time think "obviously"? Cut it.

## Failure modes

- **Procedure rot**: step-by-step instructions become wrong as the model or environment changes; principles are more durable
- **Trigger overlap**: skills that fire on the wrong queries; negative test cases catch this early
- **Skill bloat**: skills accumulate instructions without pruning; weekly pruning cycles (as in [Hermes Agent](../tools/hermes-agent.md)) address this at the framework level

## Evidence from practice

- Perplexity reports this methodology was developed from internal production failures and adopted as a company-wide skill-writing standard
- The 5-step cycle (test cases → triggers → principles → failure codification → pruning) is documented in a public Perplexity research post

## Open questions

- Does this methodology generalize beyond coding/DevOps skills to content-generation or research-retrieval skills?
- What's the right cadence for the "cut redundant lines" review — weekly, per-release, or per-model-upgrade?

## Sources

- [Perplexity agent skill methodology](../sources/newsletters/perplexity-agent-skill-methodology-2026-05-12.md)
```

### wiki/sources/newsletters/perplexity-agent-skill-methodology-2026-05-12.md (new)

```markdown
---
title: Perplexity agent skill methodology — evals-first, principles over procedures
type: source
source_type: newsletter
source_file: raw/newsletters/2026-05-12-the-fallacy-of-the-16-hour-agent.md
published: 2026-05-12
ingested: 2026-05-13
domains: [agents]
---

# Perplexity agent skill methodology — evals-first, principles over procedures

Newsletter "The Fallacy of the 16-Hour Agent" (May 12) covers Perplexity's published methodology alongside the METR benchmark analysis. Primary URL: https://research.perplexity.ai/articles/designing-refining-and-maintaining-agent-skills-at-perplexity

## Influenced pages

- [Agent skill methodology](../../training/agent-skill-methodology.md) — new training page created

## Key claims extracted

1. Write 5–10 test cases before writing the skill, including negative examples (queries that must NOT trigger the skill)
2. Phrase triggers in natural user language ("babysit a PR") not technical phrases ("monitor_ci_pipeline")
3. Write skill body as principles and direction, not step-by-step procedures — the model knows commands, it needs intent
4. When the agent fails in production, codify the failure as a standing instruction in the skill file
5. After review: cut every line the agent would get right without it — reduce noise, improve diagnosability
- Source: Perplexity internal production methodology, published as a research article
- Context in newsletter: cited alongside METR benchmark data as an example of the "reliability is engineered, not assumed" theme
```

## Feedback

- I like a lot this training material, but we need to train non-technical people and a software development example across the article is awful, please document it with a friendlier example