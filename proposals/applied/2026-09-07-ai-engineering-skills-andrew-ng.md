---
type: proposal
source: raw/newsletters/2026-08-25-ainews-andrew-ng-gets-into-ai-engineering.md
status: pending
created: 2026-09-07
---

# Proposal: Andrew Ng relaunches DeepLearning.AI around four "AI Engineering" skills

## Summary

### The source

Andrew Ng — Google Brain and Coursera cofounder — relaunched DeepLearning.AI's curriculum focus around "AI Engineering," a term the newsletter's authors (Latent Space's swyx and team, who originally popularized the "AI Engineer" framing in 2023) have been tracking as an emerging job category for years. Ng's team built the framing from an analysis of over 10,000 job postings, dozens of structured interviews with AI experts, hiring managers, and recruiters, plus survey data. The result is four named skills: building and deploying AI applications (the building blocks — LLMs, context engineering, RAG, agentic workflows — plus disciplined evals and error-analysis loops to steer and govern system behavior); software engineering fundamentals (the tradeoff judgment that separates an experienced developer directing an agent well from someone "vibe coding" a solution without knowing what context their agent needed); using coding agents effectively (a working mental model of agent limits — when to write a spec, how much to intervene, how to orchestrate multiple agents, how to avoid costly mistakes — treated as a moving target that requires continually testing new tools as best practices shift); and shaping the build (product sense and business context, including judgment calls like when to ship a fast MVP versus slow down and build carefully). The newsletter frames the first two skills as closest to the traditional MLE and SWE tracks respectively, the third as the piece of "AI Engineer" that wasn't obviously coming when the term was coined in 2023, and the fourth — product judgment — as the dimension the original framing missed entirely.

### What changes

No existing wiki page names or organizes this specific four-skill taxonomy — the wiki's `training/` pages so far cover specific practices (delegation, cost routing, agent-skill authoring, evals) rather than a general "what skills matter for AI engineering" framing, so this proposes a new page rather than folding it into an existing one.

- New page `training/ai-engineering-skills.md`, covering the four skills and Ng's evidence base, with no `domains` (cross-functional, consistent with other training pages that omit it).
- Reuses the AINews source page already drafted by a companion proposal (the harness-compounding proposal) rather than creating a duplicate — this proposal's own Influenced-pages line gets appended to it.
- Updates `wiki/index.md` to list the new page and bump the training/total page counts.

### What to weigh

The main judgment call is the new-page decision itself: this taxonomy could instead have been folded as a section into an existing page, but none of the current training pages are actually about a general skills taxonomy, so a new page seemed like the better fit than forcing it into an unrelated one. The taxonomy itself is Ng's own framing, evidence-gathered but not independently validated by a second source.

## Intended changes

- [x] **Approve all**

- [x] **Create** `wiki/training/ai-engineering-skills.md` — new training page
    > See draft below

- [x] **Update** `wiki/index.md` — add new training page entry, bump page counts
    > See draft below

## Page drafts

### wiki/training/ai-engineering-skills.md (new)

```md
---
title: AI Engineering skills
type: training
as_of: 2026-08-25
sources: [ainews-andrew-ng-ai-engineering-2026-08-25]
---

# AI Engineering skills

A practical skills taxonomy for anyone working with AI day to day, not just people with "AI Engineer" in their title. Andrew Ng (Google Brain/Coursera cofounder) relaunched DeepLearning.AI's curriculum around it in August 2026, based on an analysis of 10,000+ job postings plus structured interviews with hiring managers and recruiters.

## Current guidance

Four core skills, in Ng's framing:

- **Building and deploying AI applications** — understanding the building blocks (LLMs, context engineering, RAG, agentic workflows, classic ML/deep learning) and, critically, running disciplined evals and error-analysis loops to measure, steer, and govern AI system behavior. Closest to traditional MLE/MLOps work, extended through prompt/harness engineering and fine-tuning.
- **Software engineering fundamentals** — architecture, data-store design, and testing judgment that determines whether someone can spot the tradeoffs their coding agent is silently making. Ng frames this as the difference between an experienced developer directing an agent well and an inexperienced one "vibe coding" a solution without knowing what context the agent needed.
- **Using coding agents effectively** — a working mental model of agent limits: knowing how much to intervene versus leave the agent alone, when a written spec is worth the overhead and when it isn't, how to orchestrate multiple agents working together, and how to avoid costly mistakes (for example, an agent misconfiguring a production database). Because agentic coding practice moves fast, this skill includes a standing habit of testing new tools and revising workflow as best practices shift, not a fixed technique set.
- **Shaping the build** — product sense: understanding business context and customer goals well enough to help decide what to build, including judgment calls like when to ship a fast MVP for user testing versus slow down and build more carefully.

## Why it matters

Ng frames the first two skills as adjacent to the traditional MLE and SWE tracks respectively, the third as newly critical since coding agents went mainstream, and the fourth — product/business judgment — as the dimension the original "AI Engineer" framing (2023) didn't fully anticipate.

## Open questions

- How much of this taxonomy holds for non-technical roles (marketing, ops) using AI day to day, versus being specific to people building AI-powered software?
- Does "software engineering fundamentals" matter less over time as agents absorb more tradeoff-navigation work themselves, or more as the floor for unskilled use rises?

## Recent changes

- [2026-08-25] Page created from Andrew Ng's DeepLearning.AI relaunch around four AI Engineering skills, based on a 10,000+ job-posting analysis plus hiring-manager interviews.

## Sources

- [AINews — Andrew Ng gets into AI Engineering](../sources/newsletters/ainews-andrew-ng-ai-engineering-2026-08-25.md)
```

### wiki/index.md (updated)

> **Before** (`## Training` section — insert alphabetically; showing the two neighboring lines):
> ```
> - [training/agent-skill-methodology](training/agent-skill-methodology.md) — evals-first method for writing maintainable agent skills with natural triggers, principles, production lessons, pruning, and portable domain judgment *(as_of: 2026-07-15)*
> - [training/evals-for-agentic-software-development](training/evals-for-agentic-software-development.md) — eval stack for coding agents: deterministic gates, sandboxed execution, historical PR replay, benchmark integrity, QA artifact capture, browser self-verification, MVES, and trace mining *(as_of: 2026-07-08)*
> ```
> **After:**
> ```
> - [training/agent-skill-methodology](training/agent-skill-methodology.md) — evals-first method for writing maintainable agent skills with natural triggers, principles, production lessons, pruning, and portable domain judgment *(as_of: 2026-07-15)*
> - [training/ai-engineering-skills](training/ai-engineering-skills.md) — four-skill taxonomy (building/deploying AI apps, SWE fundamentals, using coding agents, shaping the build) from Andrew Ng's DeepLearning.AI relaunch, evidence-gathered from 10,000+ job postings *(as_of: 2026-08-25)*
> - [training/evals-for-agentic-software-development](training/evals-for-agentic-software-development.md) — eval stack for coding agents: deterministic gates, sandboxed execution, historical PR replay, benchmark integrity, QA artifact capture, browser self-verification, MVES, and trace mining *(as_of: 2026-07-08)*
> ```
>
> **Before** (`## Page count`):
> ```
> - training: 13
> ...
> **Total content pages: 188.**
> ```
> **After:**
> ```
> - training: 14
> ...
> **Total content pages: 189.**
> ```
> (Note: if the Simile proposal is applied first or after this one, the running total in `## Page count` should reflect both new pages together — 190 once both are live; apply each increment against whatever the live count is at that moment rather than this draft's snapshot.)

## Open questions

- Should this page instead live as a section on an existing page rather than standalone? I didn't find a clean fit, but flagging since the wiki is well past its bootstrap fan-out threshold.
