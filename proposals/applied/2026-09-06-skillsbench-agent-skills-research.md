---
type: proposal
source: raw/newsletters/2026-07-15-gpt-56-is-raising-concerns.md
status: pending
created: 2026-09-06
---

# Proposal: SkillsBench — empirical evidence on when agent skills help or hurt

## Summary

### The source

Until now the wiki's skill-authoring guidance (`training/agent-skill-methodology.md`) has been entirely practitioner-sourced: methodology from Perplexity, patterns from Impeccable and Vercel, no controlled measurement of whether any of it actually works. The Code's July 15 issue covers three papers that quantify it for the first time, led by SkillsBench (a public, open-source benchmark harness). Three findings, tested on identical tasks with and without skills: self-written skills — the shortcut every team tries first, asking the model to write its own skill — scored *worse on average than using no skills at all*, meaning the operating knowledge has to come from a human, not the model itself. Short, focused skills (two or three modules) beat exhaustive documentation, which sank below the no-skill baseline. And loading every available skill made things worse too — a second paper found a handful of relevant skills beat the full library, at lower token cost. The most striking detail: none of this is visible by inspecting output quality. Responses with skills enabled looked more professional even when they failed more often — 16 of 84 SkillsBench tasks performed worse with skills turned on, and the only way to catch it was a direct head-to-head comparison against the no-skill baseline.

### What changes

- **Agent skill methodology** gains a new evidence section citing SkillsBench and the companion paper: the self-written-skills-underperform-baseline finding, the short-beats-exhaustive finding (which the page's existing "cut every line" guidance already argued for on intuition, now with a benchmark behind it), the full-library-vs-few-relevant-skills finding, and the "polish hides the damage" caveat that a skill's output can look better while performing worse — argued as a reason the page's existing regression-testing guidance ("regression-test skills after model changes") should extend to *every* skill change, not only model upgrades. Page date moves to 15 July.
- New source page for the SkillsBench coverage.

### What to weigh

Everything here is one newsletter's summary of three papers; only the lead paper (SkillsBench) is named with a fetchable link — the "second paper" on library-size is referenced without a title or authors, so that specific claim is attributed to "a companion paper, name unconfirmed" rather than cited by name. The self-written-skills finding is the most consequential claim on the page (it argues against a shortcut teams are likely already taking) and deserves a closer read of the primary paper before being stated as flatly as the newsletter states it.

## Intended changes

- [x] **Approve all** — checking this box approves every item in `## Intended changes` and `## Schema / vocabulary additions` below; the individual boxes may stay empty.

- [ ] **Update** `wiki/training/agent-skill-methodology.md` — add a new evidence section citing SkillsBench's three findings; bump `as_of`; add new source
    > See draft below

- [ ] **Create** `wiki/sources/newsletters/the-code-skillsbench-agent-skills-2026-07-15.md` — source summary (scoped to the SkillsBench item only; this issue's main story — a GPT-5.6 Sol safety incident — is a separate, unrelated signal not actioned here)

## Page drafts

### wiki/training/agent-skill-methodology.md (updated)

Frontmatter — bump `as_of` and add source:

```yaml
as_of: 2026-07-15
sources: [perplexity-agent-skill-methodology-2026-05-12, agent-html-artifacts-2026-05-13, agent-skills-context-evals-2026-05-13, skill-engineering-impeccable-2026-07-02, vercel-agents-new-software-2026-07-03, autoresearch-agent-recipes-2026-07, powerpoint-agent-skill-failure-mode-2026-06, the-code-skillsbench-agent-skills-2026-07-15]
```

Add a new section after `## Evidence from practice` and before `## Recent changes`:

```md
## What the benchmarks say

The methodology above was practitioner-sourced until SkillsBench and a companion paper (July 2026) became the first controlled measurements of whether skills actually help:

- **Self-written skills underperform no skills at all.** SkillsBench tested the shortcut every team tries first — asking the model to write its own skill — against a no-skill baseline. Self-written skills scored *worse on average* than no skills. The operating knowledge has to come from a human; the model cannot bootstrap its own judgment into a skill.
- **Short beats exhaustive, with a number behind it now.** Two or three focused modules outperformed detailed, exhaustive documentation, which scored below the no-skill baseline — the same direction as this page's existing "cut every line the agent would get right without it" guidance, now with a benchmark result rather than only intuition.
- **Loading every skill you have makes things worse too.** A second paper (name not given in the source newsletter) found that a few relevant skills beat loading the full skill library, at lower token cost as well — reinforcing progressive disclosure as a correctness concern, not just an efficiency one.
- **Polish hides the damage.** Responses with skills enabled looked more professional even when they failed more often: 16 of 84 SkillsBench tasks performed worse with skills turned on, invisible without a direct head-to-head comparison against the no-skill baseline. This argues for extending this page's "regression-test skills after model changes" guidance to any skill change, not only model upgrades — a skill edit can silently make things worse behind more polished-looking output.

The SkillsBench harness is open-source, so a team can run these same comparisons on its own skills rather than trusting the published numbers alone.
```

`## Recent changes` (new entry at top):

```md
- [2026-07-15] Added SkillsBench findings: self-written skills score worse than no skills; short skills beat exhaustive documentation; loading every available skill underperforms a few relevant ones; skill regressions are invisible without a head-to-head comparison ("polish hides the damage").
```

### wiki/sources/newsletters/the-code-skillsbench-agent-skills-2026-07-15.md (new)

```md
---
title: "The Code — SkillsBench and the empirics of agent skills"
type: source
source_type: newsletter
source_file: raw/newsletters/2026-07-15-gpt-56-is-raising-concerns.md
url: https://codenewsletter.ai/p/gpt-5-6-sol-deletes-user-files-unprompted-prismml-ships-bonsai-27b
published: 2026-07-15
ingested: 2026-09-06
domains: [training, agents]
---

# The Code — SkillsBench and the empirics of agent skills

The Code's "Insight" section for July 15 covers three papers (led by SkillsBench) that quantify, for the first time, whether agent skills — folders of instructions that teach a coding agent how a team works — actually improve outcomes. This source page covers only that item; the issue's main story (a GPT-5.6 Sol safety incident involving unauthorized file/database deletion) is a separate, unrelated signal handled elsewhere.

## Influenced pages

- [Agent skill methodology](../../training/agent-skill-methodology.md) — added a new evidence section citing all four findings

## Key claims extracted

- SkillsBench (lead paper, https://arxiv.org/abs/2602.12670) tested self-written skills (model writes its own skill) against a no-skill baseline: self-written skills scored worse on average than no skills at all
- Short skills (2-3 focused modules) beat exhaustive documentation, which sank below the no-skill baseline
- A second paper (https://arxiv.org/abs/2606.32025, per the newsletter's link — title/authors not given in the fetched text) found a few relevant skills beat loading the full skill library, at lower token cost
- 16 of 84 SkillsBench tasks performed worse with skills enabled; the newsletter notes this is invisible from output polish alone and requires a direct head-to-head comparison to catch
- The SkillsBench harness is open-source (github.com/benchflow-ai/skillsbench per the newsletter), so teams can run the same comparison on their own skills
- Anthropic's own skill-authoring guide (platform.claude.com) is cited as a starting point for the authoring-and-evaluation process
