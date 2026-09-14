---
type: proposal
source: raw/articles/2026-09-09-anthropiccom-research-formalizing-fermats-last-theorem.md
status: pending
created: 2026-09-09
---

# Proposal: Anthropic formalizes Fermat's Last Theorem

## Summary

### The source

Anthropic announced the first complete, computer-checked proof of Fermat's Last Theorem (FLT) — the 1637 conjecture that no positive integers a, b, c satisfy aⁿ + bⁿ = cⁿ for any n > 2, first proven by Andrew Wiles in 1995 after a famous false start. This is not a new mathematical result: it's a *formalization*, converting Wiles's existing proof into Lean, a language a computer can verify step by step, a task the mathematical community (led by Imperial College London's Kevin Buzzard since 2024) had expected to take years. Anthropic researcher Tianyi Peng's team set a general-purpose internal research model — described in the post as "roughly comparable to Claude Fable 5.1," not confirmed to be Fable 5.1 itself — to work on it largely autonomously, using a Claude Code-based multi-agent harness. Over 11 days and roughly six billion output tokens, it produced 13 million lines of Lean code and proved 29,500 intermediate theorems on the way to the final result — more than five times the size of Mathlib, the mathematics community's own proof library that the work builds on. The proof uses only Lean's three standard axioms, and an independent comparator tool confirmed its final statement matches Mathlib's own statement of FLT. Buzzard, who reviewed the proof, called it "extraordinary" and said it shows "autoformalization artefacts are now robust enough to be built upon." Progress wasn't linear: early attempts where agents lost track of project state and stopped collaborating effectively contributed about 7% of the final proof's non-boilerplate lines before failing outright; the project turned a corner once it switched to Prove2Me, an open collaborative formalization platform (built by Peng and collaborators, described in a companion arXiv paper) that maintains a shared map of theorem statements so agents can pick next targets without duplicating or losing track of each other's work. The post itself carries no visible publish-date byline; the proof's own completion timestamp, quoted from the model's reasoning log, reads 02:00:57Z on August 18, 2026.

### What changes

The wiki's AI-in-mathematics trend page already tracks Terence Tao's "proof indigestion" observation — that AI is now generating more machine-verified proofs than mathematicians can humanly digest — and two novel-math results (the Erdős disproof, the Riemann Hypothesis bound). This proposal adds a third, differently-shaped data point.

- **AI in mathematics** gains a new Current-status entry, framed explicitly as the *verification-side* answer to Tao's already-tracked concern (a landmark proof made machine-checkable, rather than another new proof needing digestion) rather than as a fourth "new math" result. Page date moves to 9 September, since the underlying post's own publish date could not be confirmed and is dated by the wiki's ingest-date fallback rule.
- One new source page is created for the Anthropic post.

### What to weigh

The post's own publish date isn't shown on the live page — only the proof's August 18 completion timestamp is confirmable, quoted from within the article — so this entry is dated by the wiki's ingest-date fallback (2026-09-09) rather than a true source date; that moves the page's `as_of` forward on an ingest date rather than a confirmed publication date, which is flagged here rather than silently applied. Separately, like the Erdős and Riemann results already tracked on this page, this is a lab's own account of its own result — the only outside voice quoted is Kevin Buzzard, who was already directly involved in reviewing the proof, not an independent third party encountering it cold. The draft below keeps the "roughly comparable to Claude Fable 5.1" hedge exactly as the source states it, rather than asserting the model was Fable 5.1.

## Intended changes

- [x] **Approve all** — checking this box approves every item in `## Intended changes` below; the individual boxes may stay empty.

- [ ] **Update** `wiki/trends/ai-in-mathematics.md` — add 1 Current-status bullet, 1 Recent-changes entry, bump `as_of` to 2026-09-09, add source id
    > See draft below

- [ ] **Create** `wiki/sources/articles/anthropic-flt-formalization-2026-09-09.md` — source summary; no existing page covers this URL

## Page drafts

### wiki/trends/ai-in-mathematics.md (updated)

Frontmatter: bump `as_of: 2026-09-08` → `as_of: 2026-09-09`; append `anthropic-flt-formalization-2026-09-09` to `sources:`.

Add to `## Current status`, as a new bullet placed directly after the existing "Terence Tao names a verification bottleneck: 'proof indigestion'" bullet and before "Dedicated math tooling is building in parallel":

```
- **Anthropic produces the first complete computer-checked proof of Fermat's Last Theorem (2026-08-18):** Unlike the Erdős and Riemann results above, this is not new mathematics — Andrew Wiles proved FLT in 1995 — but a *formalization*: converting Wiles's proof into Lean, a language a computer can verify step-by-step, directly answering Tao's "proof indigestion" concern above by making a landmark proof machine-checkable rather than producing another one that needs digesting. Anthropic researcher Tianyi Peng's team set a general-purpose internal research model — described as "roughly comparable to Claude Fable 5.1," not Fable 5.1 itself — loose on the problem; working largely autonomously with a multi-agent Claude Code-based harness over 11 days (about six billion output tokens), it produced 13 million lines of Lean code and proved 29,500 intermediate theorems, more than 5x the size of Mathlib, the community's own proof library. Kevin Buzzard, who has led a multi-year community effort toward the same goal since 2024, called it "extraordinary" and confirmed the proof uses only Lean's three standard axioms and matches Mathlib's own statement of FLT via an independent comparator tool. The project succeeded once switched to Prove2Me, an open collaborative formalization platform (Peng et al., arXiv:2608.28433) that maintains a DAG of theorem statements agents use to pick next targets and avoid memory-degradation-driven duplicate work — roughly 7% of the final proof's non-boilerplate lines came from earlier failed attempts before this shift. Buzzard: autoformalization "artefacts are now robust enough to be built upon," a step toward catching errors across the existing mathematical corpus and easing the referee burden on AI-generated results going forward.
```

Add to `## Recent changes`, as the newest entry:

```
- [2026-09-09] Anthropic reports the first complete computer-checked (Lean) proof of Fermat's Last Theorem — a formalization of Wiles's existing 1995 proof, not new mathematics — completed 2026-08-18 by a Fable-5.1-class internal model working largely autonomously over 11 days via the Prove2Me collaborative-formalization platform; framed as the verification-side answer to Tao's "proof indigestion" concern tracked above.
```

The list has 6 entries currently (cap is 10) — no spill needed.

### wiki/sources/articles/anthropic-flt-formalization-2026-09-09.md (new)

```md
---
title: Formalizing Fermat's Last Theorem
type: source
source_type: article
source_file: raw/articles/2026-09-09-anthropiccom-research-formalizing-fermats-last-theorem.md
url: https://www.anthropic.com/research/formalizing-fermats-last-theorem
ingested: 2026-09-09
domains: [science]
---

# Formalizing Fermat's Last Theorem

Anthropic's account of the first complete, computer-checked (Lean) proof of Fermat's Last Theorem — a formalization of Andrew Wiles's 1995 proof, produced largely autonomously by an internal research model over 11 days via the Prove2Me collaborative-formalization platform. No publish-date byline is shown on the live page; the proof itself completed 2026-08-18 per an in-page quoted timestamp from the model's own reasoning log, and the post was very likely published shortly after, but no explicit date was found.

## Influenced pages

- [AI in mathematics](../../trends/ai-in-mathematics.md) — new Current-status entry, framed as the verification-side answer to Tao's "proof indigestion" concern

## Key claims extracted

- First complete, computer-checked proof of Fermat's Last Theorem, in Lean
- Completed 2026-08-18 (per an in-page quoted timestamp), 11 days of largely-autonomous work
- Model: "a general-purpose internal research model roughly comparable to Claude Fable 5.1" (not confirmed to be Fable 5.1 itself)
- ~6 billion output tokens; 13 million lines of Lean code; 29,500 intermediate theorems proved
- Proof is >5x the size of Mathlib, the community's own proof library
- Uses only Lean's 3 standard axioms; matches Mathlib's own FLT statement per an independent comparator tool
- Kevin Buzzard (led a community FLT-formalization effort since 2024) reviewed and endorsed the proof as "extraordinary"
- ~7% of the final proof's non-boilerplate lines came from earlier failed attempts, before the project switched to the Prove2Me platform
- Prove2Me: open collaborative formalization platform (Peng et al., arXiv:2608.28433) maintaining a DAG of theorem statements to coordinate agents and avoid duplicate work
```
