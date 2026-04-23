---
type: proposal
source: raw/tweets/2026-04-22-omarsar0-2006063755449504154.md
status: pending
created: 2026-04-22
---

# Proposal: "Professional Developers Don't Vibe, They Control" — field research

## Summary

Field research (N=13 observations + N=99 surveys, developers with 3–41 years of experience) finds that experienced developers never delegate design control to agents — they control. 100% controlled their own software design. Agents modify generated code ~50% of the time. Works/fails task-type ratios are concrete and useful. This is the strongest empirical counterpoint to "vibe coding" in the current batch.

## Intended changes

- [x] **Update** `wiki/training/anti-autopilot-review-friction.md` — add research as empirical evidence for the "professionals control" pattern
    > **Add to `## Proven patterns` after the existing last entry:**
    > ```markdown
    > - **Professionals control, not vibe.** Field research (N=13 observations, N=99 surveys; 3–41 years of experience) finds 100% of observed developers controlled software design and implementation regardless of task familiarity. They control via: detailed prompts with explicit context (12× observed), 70+ step external plans executed 5-6 steps at a time, and user rules that enforce project conventions. Enjoyment average: 5.11/6 — but from collaboration, not delegation. "I do everything with assistance, but never let the agent be completely autonomous."
    > ```
    >
    > **Add new section `## What works and what fails (empirical ratios)`** after `## Proven patterns`:
    > ```markdown
    > ## What works and what fails (empirical ratios)
    >
    > From the same field research (suitable:unsuitable ratios from N=99 surveys):
    >
    > **Works well:**
    > - Small, well-scoped tasks — 33:1
    > - Tedious, repetitive work — 26:0
    > - Scaffolding and boilerplate — 25:0
    > - Following well-defined plans — 28:2
    > - Writing tests — 19:2
    > - Writing documentation — 20:0
    >
    > **Fails consistently:**
    > - Complex tasks requiring domain knowledge — 3:16
    > - Business logic — 2:15
    > - One-shotting code without modification — 5:23
    > - Integrating with existing or legacy code — 3:17
    > - Replacing human decision-making — 0:12
    > ```

- [x] **Create** `wiki/sources/tweets/prof-devs-control.md` — source summary
    > See draft below

## Page drafts

### wiki/sources/tweets/prof-devs-control.md (new)

```md
---
title: "Professional Software Developers Don't Vibe, They Control" — research summary
type: source
source_type: tweet
source_file: raw/tweets/2026-04-22-omarsar0-2006063755449504154.md
url: https://x.com/omarsar0/status/2006063755449504154
published: 2026-04-22
ingested: 2026-04-22
domains: [coding, agents]
---

# "Professional Software Developers Don't Vibe, They Control"

Research paper summary by Elvis (omarsar0). Field observations (N=13) and surveys (N=99) of developers with 3–41 years of experience. Core finding: 100% of observed developers controlled software design and implementation. Agents modify generated code ~50% of the time on average. Detailed task-type suitability ratios provided.

## Influenced pages

- [[training/anti-autopilot-review-friction]] — empirical "professionals control" pattern added; task-type ratios section added

## Key claims extracted

- N=13 field observations + N=99 surveys; 3–41 years experience
- 100% of observed developers controlled own software design, regardless of task familiarity
- Agents' generated code modified ~50% of the time
- 50/99 survey respondents mentioned driving architectural requirements themselves
- Control mechanisms: detailed prompting (12×/43×), external 70+ step plans (5-6 at a time), user rules
- Works: small tasks (33:1), repetitive (26:0), scaffolding (25:0), TDD (19:2), docs (20:0)
- Fails: domain knowledge (3:16), business logic (2:15), legacy integration (3:17), decision replacement (0:12)
- Enjoyment: 5.11/6 — from collaboration, not delegation
```
