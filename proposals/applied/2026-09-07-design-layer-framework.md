---
type: proposal
source: raw/newsletters/2026-08-04-to-stay-ahead-on-ai-think-like-a-designer.md
status: pending
created: 2026-09-07
---

# Proposal: "Design layer" framework for staying valuable as AI absorbs execution

## Summary

### The source

In the final piece of Every's "unlearning" series (with Maven), Aishwarya Reganti — a former Amazon AI scientist turned founder of LevelUp Labs, which builds AI applications for mid-market and enterprise clients — argues that the career skill worth building now is not faster execution but "designing" the work: defining constraints, standards, and direction before execution starts, whether the executor is a person or an agent. She lays out five concrete, reusable patterns drawn from running her own company and dozens of client engagements. First, write a spec before anything gets built — she includes a full worked example (a personal "friend tracker" app) covering an overview, a hero scenario walking through the primary use case, functional and behavioral requirements, explicit non-goals, and named failure modes, arguing that almost every line depends on something AI can't infer because it depends on how a specific person lives and works. Second, when an agent produces a large output (her example: 200 files for a payments feature), ask five targeted questions that expose likely failure points — "How are you handling auth?", "What happens when a token expires mid-session?", "What are the different payment failure paths?" — rather than reading every file. Third, when the same correction keeps recurring across AI drafts, turn it into a standing instruction instead of re-correcting it each time. Fourth, evaluate a new tool by whether it solves a real, understood problem, not by novelty, and check whether an agent can use it too. Fifth, build feedback loops deliberately, since AI output quality drifts as models, inputs, and context change, and a setup that worked on day one can silently degrade by month three with no obvious cause.

### What changes

The wiki's `training/ai-delegation-management.md` already covers writing delegation documents and reviewing agent output, but has no worked example and doesn't yet cover targeted review questions, converting corrections into reusable instructions, or drift-driven feedback loops — this proposal fleshes that page out with Reganti's framework rather than creating a new one, since the underlying skill (operationalizing judgment so agents and people execute it) is the same.

- **AI delegation management** gains a new Current-guidance bullet on writing the spec before execution starts, four new Proven-patterns entries (spec-first delegation with the worked example, targeted review questions, converting corrections into reusable instructions, evaluating tools by problem-fit), a new Failure-modes entry on constraint drift, a new `## Recent changes` section (the page didn't previously have one), and a new `## See also` cross-link to the existing spec-driven-development concept page. Page date moves to 4 August.
- New source page for the Every essay.

### What to weigh

The worked example (the friend-tracker spec) is compressed into the proposed draft rather than reproduced in full — the source's version runs to several dozen lines across five subsections; I kept the shape and one representative line per subsection so the page stays within the wiki's usual training-page length, and pointed the source page at the original for anyone who wants the complete text. This is the first proposal to add a `## Recent changes` section to `ai-delegation-management.md`, since the page previously had none — consistent with the convention used on the wiki's other training pages, but worth flagging as a structural addition rather than a pure content edit.

## Intended changes

- [x] **Approve all** — checking this box approves every item in `## Intended changes` and `## Schema / vocabulary additions` below; the individual boxes may stay empty.

- [ ] **Update** `wiki/training/ai-delegation-management.md` — add spec-first guidance, four proven patterns, one failure mode, a new Recent-changes section, a new See-also section, `as_of`/sources bump
    > See draft below

- [ ] **Create** `wiki/sources/newsletters/design-layer-framework-2026-08-04.md` — source summary

## Page drafts

### wiki/training/ai-delegation-management.md (updated)

Frontmatter: bump `as_of: 2026-07-08` → `as_of: 2026-08-04`; append `design-layer-framework-2026-08-04` to the `sources:` list.

Append this bullet to the end of `## Current guidance`:

```md
- Write the spec before execution starts, not after — encode constraints, standards, and what "good" looks like so both people and agents downstream can make the decisions you would make. See the worked example under Proven patterns.
```

Append these four bullets to the end of `## Proven patterns`:

```md
- **Spec-first delegation, worked example.** Before any build starts, write a spec covering an overview, a hero scenario (a concrete walkthrough of the primary use case), functional and behavioral requirements, explicit non-goals, and failure modes — the details AI can't infer because they depend on how you live and work, not on general knowledge. Worked example (a personal "friend tracker" app): overview states the goal in one line; the hero scenario describes a specific Sunday-morning walkthrough; behavioral rules define what counts as "contact" and forbid nagging notifications; non-goals rule out gamification and relationship scoring; failure modes name what "gone wrong" looks like (feels like obligation, generic suggestions, more than 3 people surfaced at once). This generalizes [spec-driven development](../concepts/spec-driven-development.md)'s coding-specific spec-first practice to delegating any kind of work, human or agent. (Aishwarya Reganti, Aug 2026)
- **Targeted review questions over exhaustive reading.** When an agent produces a large multi-file output, ask four or five pointed questions that expose likely failure points — "How are you handling auth?", "What happens when a token expires mid-session?", "What are the different failure paths?" — rather than reading every line. The domain expertise is in knowing what to ask, not in reading everything.
- **Turn recurring corrections into reusable instructions.** When the same correction keeps recurring across AI drafts, write it into a standing instruction or prompt rule instead of correcting it again next time — converts one-off taste into something reusable by the team and its agents.
- **Evaluate new tools by the problem they solve, not by novelty.** Skip tools that take a long time to learn or pull you back into low-level execution unless they solve a real, understood problem; also check whether an agent, not just a person, can use the tool.
```

Append this bullet to the end of `## Failure modes`:

```md
- **Constraint drift.** AI output quality drifts as models, inputs, and context change; a setup that works well on day one can quietly degrade by month three with no obvious trigger unless someone deliberately re-checks output against the original spec on a schedule.
```

Add a new section after `## Failure modes` and before `## Sources`:

```md
## Recent changes

- [2026-08-04] Added spec-first "design layer" framework: a worked spec example, targeted review questions, converting recurring corrections into reusable instructions, tool selection by problem-fit, and constraint drift as a failure mode.

## See also

- [Spec-Driven Development](../concepts/spec-driven-development.md) — the coding-specific version of writing a spec before an agent executes
- [Anti-autopilot review friction](anti-autopilot-review-friction.md) — deliberate review friction techniques, including targeted-question review artifacts
```

### wiki/sources/newsletters/design-layer-framework-2026-08-04.md (new)

```md
---
title: "To Stay Ahead on AI, Think Like a Designer"
type: source
source_type: newsletter
source_file: raw/newsletters/2026-08-04-to-stay-ahead-on-ai-think-like-a-designer.md
url: https://every.to/p/to-stay-ahead-on-ai-think-like-a-designer
published: 2026-08-04
ingested: 2026-09-07
domains: [training]
---

# To Stay Ahead on AI, Think Like a Designer

Aishwarya Reganti (ex-Amazon AI scientist, LevelUp Labs founder) argues that as AI absorbs execution work, the valuable skill becomes designing the constraints AI and people execute within. She lays out five patterns: write a spec before anything gets built (with a full worked example — a personal "friend tracker" app spec covering overview, hero scenario, functional/behavioral requirements, non-goals, and failure modes); ask targeted review questions instead of reading every generated file; turn recurring corrections into reusable instructions; evaluate tools by the problem they solve, not novelty; and build feedback loops since AI output quality drifts over time.

## Influenced pages

- [AI delegation management](../../training/ai-delegation-management.md) — spec-first guidance, four new proven patterns, one new failure mode, new Recent-changes and See-also sections

## Key claims extracted

- Five patterns for operating at "the design layer": (1) write a spec before execution starts, (2) ask targeted review questions instead of reading every file, (3) turn recurring corrections into reusable instructions, (4) evaluate tools by problem-fit not novelty, (5) build feedback loops against AI output drift
- Full worked spec example for a personal CRM "friend tracker" app: overview, hero scenario, functional requirements, behavioral rules, non-goals, failure modes
- Example review questions for a large agent-generated payments feature: "How are you handling auth?", "What happens when a token expires mid-session?", "What are the different payment failure paths?", "What if Stripe returns a timeout?", "This needs 10,000 concurrent users — where is the rate limiting?"
- AI output quality can silently degrade over months as models/context change; the fix is a deliberate, scheduled feedback loop, not a one-time setup
```

## Schema / vocabulary additions

None.

## Open questions

- None beyond the compression of the worked example noted above.
