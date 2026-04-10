---
type: proposal
source: raw/tweets/2026-04-10-vtrivedy10-2041927488918413589.md
status: pending
created: 2026-04-10
---

# Proposal: LangChain Better-Harness (auto-eval harness hill-climbing)

## Summary

LangChain open-sourced "Better-Harness," a system that uses evals as a training signal to autonomously improve agent harnesses. It sources evals (hand-curated, production traces, external datasets), splits into optimization/holdout sets, then iteratively diagnoses failures from traces and proposes targeted harness changes — validated against holdout to avoid overfitting.

## Intended changes

- [x] **Update** `wiki/concepts/agent-improvement-loop.md` — add Better-Harness as a concrete implementation of the loop; update sources
    > **Add to "Current status" bullets:**
    > `- LangChain's Better-Harness (open-sourced 2026-04-10) automates the loop: sources evals, splits optimization/holdout sets, iteratively diagnoses failures from traces, and proposes targeted harness changes with overfitting guards`
    > **Add new section after "Role of human review":**
    > ```
    > ## Better-Harness: autonomous harness hill-climbing
    >
    > LangChain's Better-Harness is a prototype that formalizes the improvement loop as:
    >
    > 1. **Source and tag evals** — hand-curated, mined from production traces, adapted from external datasets
    > 2. **Split** into optimization and holdout sets per behavioral category
    > 3. **Baseline** — run the current harness against both sets
    > 4. **Optimize** — iteratively diagnose errors from traces, propose one scoped harness change at a time (prompt edits, tool descriptions, tool additions)
    > 5. **Validate** — check that changes pass new evals without regressing passing ones; holdout set guards against overfitting
    > 6. **Human review** — manual gate catches overfit instructions and token waste
    >
    > Tested with Claude Sonnet 4.6 and GLM-5. Results showed near-full generalization to holdout sets on tool_selection and followup_quality categories. The analogy is explicit: `harness + evals + harness engineering → better agent`, mirroring `model + training data + gradient descent → better model`.
    > ```
    > **Update frontmatter:** add `langchain-better-harness` to `sources:`, bump `as_of` to `2026-04-10`
    > **Add to Recent changes:**
    > `- [2026-04-10] Added Better-Harness section — LangChain's autonomous harness hill-climbing system`

- [x] **Create** `wiki/sources/articles/langchain-better-harness.md` — source summary

## Page drafts

### wiki/sources/articles/langchain-better-harness.md (new)

```
---
title: "Better Harness: A Recipe for Harness Hill-Climbing with Evals" — LangChain
type: source
source_type: tweet
source_file: raw/tweets/2026-04-10-vtrivedy10-2041927488918413589.md
url: https://x.com/Vtrivedy10/status/2041927488918413589
published: 2026-04-10
ingested: 2026-04-10
domains: [agents]
---

# Better Harness: A Recipe for Harness Hill-Climbing with Evals

LangChain shares Better-Harness, an open-source prototype for autonomously improving agent harnesses using evals as a hill-climbing signal. Sources evals from hand-curation, production traces, and external datasets; uses optimization/holdout splits to guard against overfitting; iteratively diagnoses failures and proposes scoped harness changes.

## Influenced pages

- [[concepts/agent-improvement-loop]] — added Better-Harness section as concrete implementation

## Key claims extracted

- `harness + evals + harness engineering → better agent` (analogous to model training)
- Eval sources: hand-curated, production traces, external datasets
- Optimization/holdout split per behavioral category prevents overfitting
- One scoped change per iteration (may include prompt + tool together)
- Tested with Claude Sonnet 4.6 and GLM-5; near-full generalization to holdout
- Common changes: prompt/instruction updates, tool description edits, new tool additions
- Human review remains a gate — catches overfit instructions and token waste
- Open-sourced as a prototype for builders
```

## Comments

-  the concept of harness is mentioned a lot in this wiki but we don't have a page for it. I think we need to research online and create one because right now it is not very clear to me what harness encompasses. It's still very diverse in interpretation and we need to anchor it somehow.