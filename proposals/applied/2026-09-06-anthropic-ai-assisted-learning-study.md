---
type: proposal
source: raw/newsletters/2026-07-26-sometimes-you-have-to-delete-everything.md
status: pending
created: 2026-09-06
---

# Proposal: Anthropic's coding-skill study gets a primary source, and a pattern for why it happens

## Summary

### The source

Every's July 26 newsletter recaps the week's Claude Opus 5 coverage, and in a personal essay by Ashwin Sharma about watching mathematician Terence Tao use ChatGPT, cites a familiar finding: Anthropic ran a randomized study of 52 mostly-junior developers learning a new Python library, and the AI-assisted group scored 50% on a follow-up quiz versus 67% for those who coded by hand — the widest gap on debugging questions specifically. That statistic already lives in this wiki, added back in May from a secondary account, with an unresolved note that it "hasn't been reconciled against a primary source." Following the newsletter's link led straight to Anthropic's own writeup (anthropic.com/research/AI-assistance-coding-skills, underlying paper arXiv 2601.20245), fetched today, which confirms the 52-participant, 50%-vs-67% numbers exactly and adds detail the secondary accounts never carried.

The primary paper's real contribution is a taxonomy of *how* people used the AI assistant, because that predicted the outcome far more than *whether* they used it. Three low-scoring patterns (quiz average under 40%) all involved heavy reliance with little independent thought: wholesale delegation, starting with a few questions before drifting into full delegation, and asking the AI to debug rather than to explain. Three high-scoring patterns (65%+) all combined AI use with active comprehension-checking: generating code and then asking follow-up questions about it, asking for code and an explanation together, or asking only conceptual questions and reasoning the rest out independently. Anthropic's own conclusion: "not all AI-reliance is the same... the posture, not the tool, determined the outcome."

### What changes

`training/anti-autopilot-review-friction.md` already carries this study's headline numbers under Cognitive debt (added 2026-05-18). This proposal doesn't touch the numbers — it resolves the sourcing gap and adds the interaction-pattern nuance the page has been missing.

- **Anti-autopilot review friction** — the existing Anthropic-study bullet under Cognitive debt gets a citation update: the "hasn't been reconciled against a primary source" caveat is replaced with a confirmed cite to Anthropic's own writeup and arXiv 2601.20245. A new sub-point lists the three low-scoring and three high-scoring interaction patterns, plus Anthropic's own framing that AI use didn't guarantee a worse outcome — careless use did. `sources:` gains the new primary-source id; no Recent-changes entry, since this refines an already-logged finding rather than reporting a new one.
- New source page for Anthropic's primary research writeup, created under `wiki/sources/articles/`.

### What to weigh

Having the primary source now lets us check a separate, unresolved claim: `training/ai-enablement-software-development.md` currently cites a secondhand "47% drop in debugging ability," attributed to this same Anthropic study via Lars Faye's viral essay, and flags it as unreconciled against `anti-autopilot-review-friction.md`'s 50%-vs-67% figure. Having now read the primary paper directly, no "47%" figure appears anywhere in it — the actual reported quiz-score gap is 25% relative (50 vs. 67), not a 47% debugging-specific drop. That looks like a mis-citation on Faye's part, not a second real data point. This proposal does not touch `ai-enablement-software-development.md` (out of scope here), but the reconciliation should be a follow-up: replace the "47%" claim with the confirmed primary numbers, or flag it as an unverified secondary claim.

## Intended changes

- [x] **Approve all** — checking this box approves every item in `## Intended changes` and `## Schema / vocabulary additions` below; the individual boxes may stay empty.

- [ ] **Update** `wiki/training/anti-autopilot-review-friction.md` — confirm primary sourcing on the existing Anthropic-study bullet, add interaction-pattern nuance
    > See draft below

- [ ] **Create** `wiki/sources/articles/anthropic-ai-assistance-coding-skills-2026.md` — source summary for Anthropic's primary research writeup

## Page drafts

### wiki/training/anti-autopilot-review-friction.md (updated)

Replace the existing Anthropic-study bullet under `## Cognitive debt` (currently the first bullet under "Three empirical studies:") with:

```md
- **Anthropic comprehension study:** Engineers learned a new Python library — half with AI assistance, half without. Both groups finished tasks at about the same speed. But the AI group scored 50% on the follow-up comprehension quiz vs 67% for the manual group (Cohen's *d*=0.738); the gap widened most on debugging questions. Within the AI group, *how* people used the assistant mattered more than *whether* they did: three low-scoring patterns (quiz average under 40%) all involved heavy reliance with little independent thought — wholesale AI delegation, starting with a few questions before drifting into full delegation, and asking AI to debug rather than to explain. Three high-scoring patterns (65%+) all paired AI use with active comprehension-checking — generating code then asking follow-up questions, requesting code and explanation together, or asking only conceptual questions and reasoning the rest independently. Anthropic's own framing: "not all AI-reliance is the same" — the posture, not the tool, determined the outcome. Confirmed against Anthropic's own primary writeup (arXiv 2601.20245); no longer a secondary-account figure.
```

Add `anthropic-ai-assistance-coding-skills-2026` to the page's frontmatter `sources:` list.

### wiki/sources/articles/anthropic-ai-assistance-coding-skills-2026.md (new)

```md
---
title: How AI assistance impacts the formation of coding skills
type: source
source_type: article
source_file: raw/articles/2026-09-06-anthropiccom-research-ai-assistance-coding-skills.md
url: https://www.anthropic.com/research/AI-assistance-coding-skills
published: 2026-07-16
ingested: 2026-09-06
domains: [training]
---

# How AI assistance impacts the formation of coding skills

Anthropic's own randomized controlled trial (arXiv 2601.20245, Shen & Tamkin): 52 mostly-junior software engineers learned Trio, an unfamiliar Python async library, either with or without an AI coding assistant, then took a comprehension quiz. The AI group scored 50% vs. 67% for the hand-coding group (Cohen's *d*=0.738, p=0.01) — a gap concentrated in debugging questions. Qualitative analysis found the outcome depended on *how* people used the assistant: three low-scoring interaction patterns involved heavy AI reliance with little independent verification (full delegation, progressive delegation, AI-driven debugging); three high-scoring patterns combined AI use with active comprehension-checking (generate-then-ask-questions, code-plus-explanation requests, conceptual-only queries). Anthropic frames the core finding as: using AI didn't guarantee worse learning outcomes, but careless AI use did.

## Influenced pages

- [Anti-autopilot review friction](../../training/anti-autopilot-review-friction.md) — confirmed primary sourcing for the existing 50%-vs-67% finding, added interaction-pattern taxonomy

## Key claims extracted

- 52 mostly-junior developers, RCT design, learning Trio (Python async library)
- AI group: 50% quiz score; hand-coding group: 67% (Cohen's d=0.738, p=0.01)
- Largest score gap on debugging questions specifically
- Three low-scoring interaction patterns (avg quiz <40%): AI delegation, progressive AI reliance, iterative AI debugging
- Three high-scoring interaction patterns (avg quiz 65%+): generation-then-comprehension, hybrid code-explanation, conceptual inquiry
- Underlying paper: arXiv 2601.20245 (Shen & Tamkin, "How AI Impacts Skill Formation")
```

## Schema / vocabulary additions

None.

## Open questions

- Should `training/ai-enablement-software-development.md`'s "47% debugging-ability drop" claim (attributed to this same Anthropic study via Lars Faye's essay) be corrected or flagged now that the primary source shows no such figure? See "What to weigh" above — recommend a small follow-up proposal rather than folding it into this one.
