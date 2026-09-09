---
type: proposal
source: raw/newsletters/2026-08-28-33-questions-executives-ask-about-aianswered.md
status: pending
created: 2026-09-08
---

# Proposal: Every's "33 Questions Executives Ask About AI—Answered"

## Summary

### The source

Every's consulting team — Natalia Quintero, who has advised 400+ companies including the New York Times and hedge fund Walleye Capital, and Mike Taylor, Every's head of evals — published detailed answers to 33 recurring executive questions from a live June 2026 webinar with 400 attendees, covering strategy, winning over skeptics, tool selection, governance, and organizational restructuring. Several answers are concrete enough to act on directly: an 8-level AI-fluency ladder, where most people sit at levels 1-2 (chat, co-working) and agentic work starts at level 3, with orchestration (a "manager AI" managing other AIs) at level 8; a "pick one platform" default answer to tool-switching questions, since skills don't port cleanly between ecosystems (Codex vs. Claude Code) and switching costs (retraining, contract renegotiation) are real; a token-economics rule that favors frontier models by default for novel or one-off work, only routing settled, recurring tasks to smaller models via frameworks like DSPy or prompt optimization; a governance split where a central AI team owns standards, security, and shared infrastructure while business teams own their own workflows; and a rejection of any single AI-adoption metric in favor of workflow-level measurement (cycle time, error/rework rate, NPS) against a pre-AI baseline.

### What changes

`training/company-wide-ai-enablement.md` already covers broad AI-adoption patterns, governance, and staged autonomy in depth. This proposal adds five new bullets to its "Proven patterns" section (platform-lock-in economics, token-economics-by-task-novelty, governance ownership split, workflow-level measurement, and the AI-fluency ladder as a named framework), bumps `as_of` to 2026-08-28, and adds one Recent-changes entry — which lands exactly at the page's 10-entry cap with no spill required yet.

### What to weigh

Nothing beyond the sourcing itself: this is a single, substantial primary source (Every's own published Q&A, not a secondary recap), and its guidance is consistent with rather than contradicting the page's existing content — it adds specificity (an explicit fluency ladder, a concrete token-economics rule) rather than introducing new claims that conflict with what's already there.

## Intended changes

- [x] **Approve all** — checking this box approves every item below; the individual boxes may stay empty.

- [ ] **Update** `wiki/training/company-wide-ai-enablement.md` — add 5 new Proven-patterns bullets, bump `as_of`, add Recent-changes entry
    > See draft below

- [ ] **Create** `wiki/sources/newsletters/every-33-questions-executives-2026-08-28.md` — source summary

## Page drafts

### wiki/training/company-wide-ai-enablement.md (updated)

```md
---
as_of: 2026-08-28
sources: [..., every-33-questions-executives-2026-08-28]
---

## Proven patterns

(... existing bullets unchanged ...)

- **An explicit AI-fluency ladder.** Every's consulting practice uses an 8-level fluency framework: most people sit at levels 1-2 (chatbot use, co-working with AI in Docs/Excel); level 3, agentic, is where knowledge workers are actively moving (Codex, Claude Cowork, Claude Code, adopting skills and running multiple tasks at once); above that is largely experimental, up to level 8 where a manager AI orchestrates other AIs. Use this to calibrate expectations rather than pushing every team toward the highest level.
- **Pick one platform as the default.** Switching tool ecosystems is expensive — contracts need renegotiating, staff need retraining, and skills written for one coding agent (Codex) often don't transfer cleanly to another (Claude Code). Default recommendation: stay on one platform from Anthropic or OpenAI, or a third party with access to both (Cursor, Copilot), rather than chasing the frontier model of the week; being a month or two behind rarely costs real capability since genuinely good techniques get copied across labs within 8-12 weeks.
- **Route by task novelty, not just task size.** For a brand-new, high-stakes, or one-off task, use the best available model — it's often cheaper overall because it avoids costly mistakes and self-correction cycles. Only once a task becomes recurring and well-understood should it move to a smaller model via a framework like DSPy or prompt optimization.
- **Split governance ownership explicitly.** A central AI team should own standards, security and vendor decisions, shared infrastructure, and the first few working examples; individual business teams should own their own workflows. Centralizing everything creates a bottleneck; leaving every team to build alone creates sprawl.
- **Measure at the workflow level, never by a single metric.** Track cycle time, output quality, error/rework rate, user satisfaction (e.g. NPS), and traditional cost-benefit business impact — and track reuse of shared skills as a leading indicator. Establish a pre-AI baseline (time, quality standard, cost, common mistakes) before claiming a workflow improved.

## Recent changes

- [2026-08-28] Added Every's 33-Questions guidance: an explicit 8-level AI-fluency ladder, "pick one platform" as the tool-switching default, route-by-task-novelty token economics, an explicit governance ownership split, and workflow-level (not single-metric) measurement.
- (... existing entries follow ...)
```

### wiki/sources/newsletters/every-33-questions-executives-2026-08-28.md (new)

```md
---
title: "33 Questions Executives Ask About AI—Answered"
type: source
source_type: newsletter
source_file: raw/newsletters/2026-08-28-33-questions-executives-ask-about-aianswered.md
url: https://every.to/p/every-answers-your-ai-questions
published: 2026-08-28
ingested: 2026-09-08
domains: [training]
---

# 33 Questions Executives Ask About AI—Answered

Every's consulting team (Natalia Quintero, Mike Taylor) publishes detailed answers to 33 recurring executive questions from a June 2026 live webinar with 400 attendees, covering AI strategy, tool selection, governance, org restructuring, and measurement.

## Influenced pages

- [Company-wide AI enablement](../../training/company-wide-ai-enablement.md) — 5 new Proven-patterns bullets

## Key claims extracted

- 8-level AI-fluency ladder: levels 1-2 (chat/co-work) most common, level 3 (agentic) the current frontier, level 8 (orchestration) experimental
- "Pick one platform" as the default tool-switching answer; genuinely good techniques get copied across labs within 8-12 weeks
- Route by task novelty: frontier models for novel/high-stakes work, smaller models (DSPy, prompt optimization) for recurring settled work
- Governance split: central team owns standards/security/infra, business teams own workflows
- No single AI-adoption metric — measure at the workflow level (cycle time, rework rate, NPS) against a pre-AI baseline
```
