---
type: proposal
source: raw/articles/2026-10-19-felixriesebergcom-how-to-be-more-ambitious-a-tutorial-for-hu.md
status: pending
created: 2026-10-19
---

# Proposal: Felix Rieseberg — How to be more ambitious with models

## Summary

### In short
Most people under-use models because they ask for the same task done faster, when the bigger gains come from asking for the outcome behind the task, an expert-grade method, or several fields at once. Felix Rieseberg, who works on Claude, makes this concrete with a quarterly-review example and a reusable "deeper, not bigger" prompt, plus one hard rule: never let the model judge its own work. The proposal adds an ambition section to **AI delegation management** and an outcome-level delegation pattern to **AI work delegation modes**. Hesitation: the post carries no exact date.

[[#Open questions|Open questions: 1 to answer.]]

### The source
Felix Rieseberg, who says he works on Claude and builds products people use with it, wrote a mid-October 2026 essay arguing that "be more ambitious" is advice everyone repeats and few know how to follow. He splits ambition into four kinds. Speed, the same work in less time, he skips as already well understood. Altitude means asking "what do you want to happen next?" and handing the model the goal behind the task: he stopped asking Claude to fix individual crashes and asked it to keep the apps crash-free, which first required giving it crash reports, a map from app versions to git commits, and Windows, macOS and Linux machines to reproduce and verify fixes on. His tell for when altitude fits is that the work would otherwise lead to meetings; it fits creative work less well, and "go make money" still fails.

Depth means working the way a field-leading expert would. Models told to act like professionals change vocabulary without changing methods, so insist on the real instruments (statistical models, not markdown tables), set targets that look unreasonable, and have the model re-test the business's own assumptions against raw data. Above all, use an outside judge, ideally a tool the model can run, because self-judging does not work yet.

Range means pulling in fields the task would not normally touch: restate the deliverable as verbs, then "assemble the crew" of disciplines. Asking the model to write like a short seller is role play; asking it to do what a short seller does is the point. All of this assumes the model has a computer and data access.

### What changes
The wiki already covers delegation fundamentals (scope, authority, definition of done) and the split between autonomous delegation and human-steered collaboration, but has nothing on raising the ambition of what gets delegated.

- **AI delegation management** gains a new section on altitude, depth and range, the reusable "deeper, not bigger" prompt, and a failure mode for role play and self-judging. It gets one Recent-changes entry and the new source; page date moves to 19 October.
- **AI work delegation modes** gains a pattern on delegating the outcome rather than the task, including the plumbing that makes it work, and opens a Recent-changes section with one entry. Page date moves to 19 October.
- One new source page for the essay.

### What to weigh
The post has no publication date in the fetched copy; it links a 10 October post and speaks of "October 2026", so it is dated to the 19 October ingest date as a fallback. Range and depth are placed on the management page as a new section rather than inside Proven patterns, because that section is already near the flat-section limit.

## Intended changes

- [x] **Approve all** — checking this box approves every item in `## Intended changes` and `## Schema / vocabulary additions` below; the individual boxes may stay empty.

- [ ] **Update** `wiki/training/ai-delegation-management.md` — add a `## Raising the ambition of a delegation` section between Proven patterns and Failure modes; add one Failure-modes bullet; adds one Recent-changes entry dated 2026-10-19 (live list has 4, no spill); appends one id to frontmatter `sources:` and one link to `## Sources`; `as_of` to 2026-10-19
- [ ] **Update** `wiki/training/ai-work-delegation-modes.md` — add one Proven-patterns bullet (delegate the outcome, not the task); add a new `## Recent changes` section (none exists today) with one entry dated 2026-10-19, placed before `## Related`; appends one id to frontmatter `sources:` and one link to `## Sources`; `as_of` to 2026-10-19
- [ ] **Create** `wiki/sources/articles/rieseberg-how-to-be-more-ambitious.md` — source summary

## Page drafts

### wiki/training/ai-delegation-management.md (updated)

Frontmatter (changed fields only):

```
as_of: 2026-10-19
sources: [management-as-ai-superpower-2026-07, andy-matuschak-agent-loop-tempo-2026-07, design-layer-framework-2026-08-04, vibe-coded-security-risk-2026-08-10, securing-ai-employee-guide-2026-08-14, next-era-of-great-work-2026-08-16, engineering-team-cost-of-codex-2026-08-19, rieseberg-how-to-be-more-ambitious]
```

New section, inserted after `## Proven patterns` and before `## Failure modes`:

```
## Raising the ambition of a delegation

Delegating the same task faster is the default use of a model. Felix Rieseberg (Oct 2026) names three other directions, each with a different question to ask before handing work off:

- **Altitude: delegate the outcome behind the task.** Ask "what do you want to happen next?" and hand that over instead: not "fix this crash" but "keep the app crash-free". Fits work aimed at an outcome (a good sign is that it would otherwise generate meetings); fits creative work less well. See [AI work delegation modes](ai-work-delegation-modes.md) for the plumbing it needs.
- **Depth: demand the expert's method, not the expert's vocabulary.** Insist on the instruments specialists use (a database and a statistical model, not a markdown table); set targets that look unreasonable (200 ms, not 5 s) and say they are reachable; have the model re-test the team's own beliefs against raw data ("we believe churn is an onboarding problem; try to reproduce that"); then ask for something new, such as an early signal that predicts on held-out data.
- **Range: bring in fields the task would not normally touch.** Restate the deliverable as verbs (a quarterly review is "getting busy people to believe a story about cause and effect and decide under uncertainty in 30 minutes"), then ask which disciplines a dream team would include, adversarial ones too (a short seller, a forensic accountant).
- **Use an outside judge.** Depth only pays off if something other than the model confirms the result, ideally a check the model can run itself.

A reusable prompt for depth:

> I want a deeper version of this task, not a bigger one. Before rewriting it: (1) say what a top professional in this field would do here that I'm not asking for; (2) name the rawest material they would start from instead of what has already been digested for me; (3) name the specific methods and tools they would use; (4) say what, other than you or me, would show the result is right. Then rewrite my prompt to ask for exactly that.

All three directions assume the agent has a computer, can install software, and can reach the relevant data.
```

New bullet, appended to `## Failure modes`:

```
- **Role play instead of method, and self-grading.** Asking a model to "write like a short seller" changes the transcript, not the outcome; ask it to do what a short seller does to research a position. Likewise, a model asked to judge its own work is not evidence the work is right; insist on an outside check.
```

`## Recent changes` — adds one entry at the top (live list has 4 entries; no spill):

```
- [2026-10-19] Added "Raising the ambition of a delegation": Felix Rieseberg's altitude, depth, and range directions, a reusable "deeper, not bigger" prompt, and a failure mode for role play and self-grading.
```

`## Sources` — appends one link:

```
- [How to be more ambitious: a tutorial for humans with models — Felix Rieseberg](../sources/articles/rieseberg-how-to-be-more-ambitious.md)
```

### wiki/training/ai-work-delegation-modes.md (updated)

Frontmatter (changed fields only):

```
as_of: 2026-10-19
sources: [ai-work-splitting-2026-05-10, task-routing-cost-discipline-2026-05-13, every-after-automation-2026-05, every-chatgpt-openclaw-guides-2026-08-27, rieseberg-how-to-be-more-ambitious]
```

New bullet, appended to `## Proven patterns`:

```
- **Delegate the outcome, not the task, and build the plumbing first.** The most durable delegation-mode workflows come from handing over the goal behind a stream of tasks, so the human stops feeding the agent one task at a time. Felix Rieseberg moved from asking Claude to fix individual crashes to asking it to keep his apps crash-free; that only worked after he gave it crash reports, a mapping from app versions to git commits, and Windows, macOS, and Linux machines on which to reproduce and verify fixes itself. Outcome-level delegation usually means changing the workflow so the agent can observe and check results on its own. (Oct 2026)
```

New section, inserted after `## Open questions` and before `## Related`:

```
## Recent changes

- [2026-10-19] Added the outcome-level delegation pattern (delegate the goal, then give the agent the data and machines to verify it), from Felix Rieseberg's crash-free example.
```

`## Sources` — appends one link:

```
- [How to be more ambitious: a tutorial for humans with models — Felix Rieseberg](../sources/articles/rieseberg-how-to-be-more-ambitious.md)
```

### wiki/sources/articles/rieseberg-how-to-be-more-ambitious.md (new)

```
---
title: 'How to be more ambitious: a tutorial for humans with models — Felix Rieseberg'
type: source
source_type: article
source_file: raw/articles/2026-10-19-felixriesebergcom-how-to-be-more-ambitious-a-tutorial-for-hu.md
url: https://felixrieseberg.com/how-to-be-more-ambitious-a-tutorial-for-humans-with-models/
ingested: 2026-10-19
domains: [agents, training]
---

# How to be more ambitious: a tutorial for humans with models

Felix Rieseberg, who says he works on Claude, turns the slogan "we're not ambitious enough with AI" into a method. He names four kinds of ambition: speed (same work, less time; skipped as well understood), altitude (delegate the outcome behind the task), depth (work the way a field-leading expert would, with an outside judge), and range (draw on fields the task would not normally touch). A running example is a quarterly business review deck at an imagined company, escalated from "fill the template" to "design a better way for leadership to catch problems early and run it beside the current process for a quarter". He closes with self-efficacy research (Locke and Latham's goal-setting review, Dantzig, Bannister) as the reason humans need techniques to aim higher. Undated in the fetched copy; internal references place it in mid-October 2026.

## Influenced pages

- [AI delegation management](../../training/ai-delegation-management.md) — new "Raising the ambition of a delegation" section; role-play and self-grading failure mode
- [AI work delegation modes](../../training/ai-work-delegation-modes.md) — outcome-level delegation pattern (crash-free example)

## Key claims extracted

- Four types of ambition: speed, altitude, depth, range
- Altitude: ask "what do you want to happen next?"; author moved from "fix this crash" to "keep our apps crash-free", which required crash reports, version-to-commit mapping, and Windows/macOS/Linux machines for independent reproduction and verification
- Altitude fits outcome-driven work (tell: it would generate meetings) and fits creative work less well; "Claude, go make money" does not work for most businesses in 2026
- Depth: models told to act like professionals switch vocabulary without switching methods; insist on experts' instruments, set unreasonable goals, adversarially check assumptions against raw data, produce new knowledge
- Do not ask the model to judge itself; as of October 2026, insist on outside validation, ideally a tool the model can run
- Four-part "deeper, not bigger" prompt: what a top professional would do, the rawest starting material, the specific methods and tools, and what outside check would show the result is right
- Range: restate nouns as verbs; "assemble the crew" of fields including adversarial ones; avoid role play (ask the model to do what a short seller does, not write like one)
- All techniques assume the model has a computer, can install software, and has data access (e.g. MCP connectors)
```

## Schema / vocabulary additions

None.

## Open questions

- Range (pulling in other disciplines) sits close to the existing specialist-agent-roster pattern on **AI delegation management**; keep them as separate bullets (assumed), or merge range into that pattern?
	- Separate
