---
type: proposal
source: raw/newsletters/2026-07-16-the-case-against-skills.md
status: pending
created: 2026-09-06
---

# Proposal: SWE-Skills-Bench — a second, independent skills benchmark

## Summary

### The source

Every's "The Case Against Skills" newsletter (16 July) argues that most agent skills are dead weight now that frontier models have absorbed the workarounds they used to encode, and points to a specific paper as the receipts: SWE-Skills-Bench (arXiv 2603.15401, submitted 16 March by a team including Tingxu Han and Lijie Hu). It's a different, independent benchmark from the SkillsBench study already on this page — similarly named, easy to conflate, but a distinct piece of research. SWE-Skills-Bench pairs 49 public software-engineering skills with real GitHub repositories pinned to fixed commits and requirement documents carrying explicit acceptance criteria, yielding about 565 task instances across six SE subdomains, each scored by execution-based tests rather than a judge model. Run with and without each skill: 39 of the 49 produced zero measurable pass-rate improvement, and the average gain across all 49 was only +1.2%. Token overhead ranged from modest savings up to a 451% increase, often with no pass-rate change to show for it. Only 7 skills produced real gains (up to +30%) — every one supplying specialized knowledge the model couldn't otherwise have, like financial-risk formulas or traffic-management rules. Three skills actively hurt performance (up to -10%), specifically because their guidance was mismatched to the project's actual code version. The newsletter frames the takeaway as a shelf-life problem: a skill that patches a model's blind spot becomes redundant, or actively wrong, the moment a newer model closes that gap or the project moves past what the skill assumes — and closes with a concrete 3-step audit: keep skills supplying private/proprietary context, retest ones compensating for a general model weakness, retire ones that don't demonstrably help.

### What changes

`training/agent-skill-methodology.md` already has a "What the benchmarks say" section built around SkillsBench (self-written skills score worse than none, short beats exhaustive, loading everything underperforms a few relevant skills). This proposal adds a second, distinct benchmark next to it, plus one new audit heuristic.

- **Training — agent skill methodology** gains a new "What the benchmarks say" entry naming SWE-Skills-Bench explicitly as separate from SkillsBench, with its own numbers (49 skills, 565 tasks, 39 flat, +1.2% average, 7 real winners up to +30%, 3 regressions up to -10% from version-mismatched guidance). It also gains a new Proven-patterns entry for the newsletter's 3-step audit triage (keep / retest / retire). One new Recent-changes entry, dated 16 July; page date moves to 16 July.
- Two new source pages: one for the newsletter and one for the SWE-Skills-Bench paper's abstract (the arXiv abstract page — sufficient detail for the numbers above; the full PDF wasn't needed).

### What to weigh

The paper is drawn from its arXiv abstract page rather than the full PDF — sufficient for the headline numbers used here, but methodology detail beyond the abstract (which specific skills, which six subdomains) isn't captured. Nothing else beyond the sourcing already noted above.

## Intended changes

- [x] **Approve all** — checking this box approves every item in `## Intended changes` and `## Schema / vocabulary additions` below; the individual boxes may stay empty.

- [ ] **Update** `wiki/training/agent-skill-methodology.md` — new "What the benchmarks say" entry for SWE-Skills-Bench, new Proven-patterns audit-triage entry, one new Recent-changes entry, `as_of` moves to 2026-07-16, merge two new source ids
    > See draft below

- [ ] **Create** `wiki/sources/newsletters/case-against-skills-2026-07-16.md` — source summary

- [ ] **Create** `wiki/sources/papers/swe-skills-bench-2026-07.md` — source summary for the SWE-Skills-Bench paper abstract

## Page drafts

### wiki/training/agent-skill-methodology.md (updated)

```md
---
title: Agent skill methodology
type: training
domains: [agents]
tags: [perplexity, agentic]
as_of: 2026-07-16
sources: [perplexity-agent-skill-methodology-2026-05-12, agent-html-artifacts-2026-05-13, agent-skills-context-evals-2026-05-13, skill-engineering-impeccable-2026-07-02, vercel-agents-new-software-2026-07-03, autoresearch-agent-recipes-2026-07, powerpoint-agent-skill-failure-mode-2026-06, gpt-56-raising-concerns-2026-07-15, case-against-skills-2026-07-16, swe-skills-bench-2026-07]
---

## Proven patterns

(add as a new numbered pattern, after pattern 7 "Regression-test skills after model changes":)

**8. Run a keep/retest/retire audit**
When reviewing an existing skill library, sort every skill into one of three buckets:
- **Keep** — skills that supply private context, custom tool access, personal taste, or a specific company workflow the model has no way to know on its own.
- **Retest** — skills that exist to compensate for a general model weakness or quirk; these have a shelf life as models improve, and may already be doing nothing or actively hurting on the current model.
- **Retire** — skills that don't demonstrably improve results when tested with and without them (a favorite AI agent can run the comparison directly).

## What the benchmarks say

(add as a new bullet, after the existing "Polish hides the damage" bullet:)

- **A second, independent benchmark points the same direction — with a caution.** SWE-Skills-Bench (arXiv 2603.15401, March 2026) is a distinct study from SkillsBench above, despite the similar name. It pairs 49 public software-engineering skills with real GitHub repos and requirement documents carrying explicit, execution-tested acceptance criteria — about 565 task instances across six SE subdomains. Result: 39 of 49 skills produced zero measurable pass-rate improvement, and the average gain across all 49 was only +1.2%. Token overhead ran as high as +451% independent of any accuracy gain. Only 7 skills helped (up to +30%) — all supplying specialized knowledge the model couldn't otherwise have. Three actively hurt performance (up to -10%), specifically because their guidance was mismatched to the project's actual code version — a concrete, named failure mode for the "procedure rot" entry above.

## Recent changes

(insert as the new first entry, newest-first:)

- [2026-07-16] Added SWE-Skills-Bench (distinct from SkillsBench): 49 skills tested against real repos, 39 with zero effect, average +1.2% gain, 7 real winners (up to +30%), 3 regressions (up to -10%) from version-mismatched guidance. Added a keep/retest/retire skill-audit pattern.
- [2026-07-15] Added SkillsBench findings: self-written skills score worse than no skills; short skills beat exhaustive documentation; loading every available skill underperforms a few relevant ones; skill regressions are invisible without a head-to-head comparison ("polish hides the damage").
(...remaining existing entries unchanged...)

## Sources

(append two new lines:)

- [The Case Against Skills](../sources/newsletters/case-against-skills-2026-07-16.md)
- [SWE-Skills-Bench: Do Agent Skills Actually Help in Real-World Software Engineering?](../sources/papers/swe-skills-bench-2026-07.md)
```

### wiki/sources/newsletters/case-against-skills-2026-07-16.md (new)

```md
---
title: The Case Against Skills
type: source
source_type: newsletter
source_file: raw/newsletters/2026-07-16-the-case-against-skills.md
published: 2026-07-16
ingested: 2026-09-06
domains: [agents]
---

# The Case Against Skills

Every newsletter (Laura Entis, 16 July) arguing most agent skills are now dead weight for frontier models, built around the SWE-Skills-Bench findings and a 3-step keep/retest/retire audit process. Also profiles OpenClaw's open-source "autoreview" skill (a second-model code review step) as a rare durable exception.

## Influenced pages

- [Training — Agent skill methodology](../../training/agent-skill-methodology.md) — SWE-Skills-Bench benchmark entry, keep/retest/retire audit pattern

## Key claims extracted

- SWE-Skills-Bench: 49 skills tested, 39 no effect, 3 made results worse, worst token overhead +451%, only 7 improved outcomes
- Audit heuristic: keep skills with private/proprietary context, retest ones compensating for a general model weakness, retire the rest
```

### wiki/sources/papers/swe-skills-bench-2026-07.md (new)

```md
---
title: "SWE-Skills-Bench: Do Agent Skills Actually Help in Real-World Software Engineering?"
type: source
source_type: paper
source_file: raw/papers/2026-09-06-arxivorg-abs-260315401.md
url: https://arxiv.org/abs/2603.15401
published: 2026-03-16
ingested: 2026-09-06
domains: [agents]
---

# SWE-Skills-Bench: Do Agent Skills Actually Help in Real-World Software Engineering?

Han, Zhang, Song, Fang, Chen, Sun, and Hu (submitted 16 March 2026). The first requirement-driven benchmark isolating the marginal utility of agent skills in real software engineering: 49 public SWE skills paired with authentic GitHub repos pinned to fixed commits and requirement documents with explicit acceptance criteria, yielding ~565 task instances across six SE subdomains, scored by a deterministic execution-based verification framework (paired with/without-skill comparison).

## Influenced pages

- [Training — Agent skill methodology](../../training/agent-skill-methodology.md) — cited as a second, independent skills benchmark alongside SkillsBench

## Key claims extracted

- 39 of 49 skills yield zero pass-rate improvement; average gain across all 49 is only +1.2%
- Token overhead ranges from modest savings to +451%, independent of pass-rate change
- 7 skills produce meaningful gains (up to +30%) — all supplying specialized, otherwise-unavailable domain knowledge
- 3 skills degrade performance (up to -10%) due to version-mismatched guidance conflicting with the project's actual code
```

## Open questions

- None.
