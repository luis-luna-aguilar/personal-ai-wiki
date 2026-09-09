---
type: proposal
source: raw/newsletters/2026-09-08-to-reador-not-to-read-the-code.md
status: pending
created: 2026-09-09
---

# Proposal: "Read the code to learn" and the irony of automation

## Summary

### The source

Every's Kieran Klaassen (Cora GM) writes about a shift in how he uses AI a year into heavy delegation: he's shipping more than ever, but noticed his own understanding thinning out underneath the output. His rule for what should run unattended versus what needs him present isn't about task size — a four-pixel spacing bug can run fully "in the dark" because his understanding wouldn't change the decision, but plenty of work that looks mechanical has a real decision hiding inside it, and those are the places he deliberately keeps the lights on. Concretely, he's gone back to reading code — not to verify it (planning, testing, and review agents already do that better than he does), but to learn. His main tool is a custom `/ce-explain` command that traces mechanics — not diffs — through his own codebase: pointed at a feature, it walks the real data flow end to end; pointed at a production incident (Cora had permanently deleted emails a customer had already sent, seconds after they hit Send), it reconstructed exactly what happened and let him reject two plausible-sounding but wrong fixes in favor of the one that actually addressed the failure. He also borrowed a practice from Thariq Shihipar: after a long session, ask the model for a written explanation and a quiz on what changed, and don't merge until you score well — the tests decide whether the code can merge, the quiz decides what you still need to learn. He grounds this in a 2026 paper by Margaret Mitchell, Avijit Ghosh, and Samir Passi (arXiv:2608.23642), which reviews evidence that extended AI-agent use measurably erodes the vigilance, critical thinking, and domain skill that human oversight depends on — an agent-era instance of the "irony of automation," a term coined in 1983 by a safety researcher studying human operators of automated factories and power plants: the more capable the automation, the faster the human's own skill erodes, and agents just make that move faster.

### What changes

The wiki's **Anti-autopilot review friction** training page already covers closely related ground — cognitive debt (Osmani), the Anthropic comprehension study, and several forcing-function patterns for keeping human judgment active — but doesn't yet have a citable academic source for the general erosion claim, or this specific pair of practices (mechanics-tracing, quiz-before-merge).

- **Anti-autopilot review friction** gains two new entries in `## Proven patterns` (mechanics-tracing via a custom explain command; quiz-before-merge) and a new citation for the Mitchell/Ghosh/Passi paper plus the "irony of automation" framing, folded into the existing `## Cognitive debt` section alongside the page's other empirical studies. Page date moves to 8 September.
- One new source page for the Every essay.

### What to weigh

The paper citation (arXiv:2608.23642) is referenced by Every rather than read directly here — the draft below quotes the author's own characterization of the paper's finding rather than the paper's own abstract or results section, consistent with how this proposal is scoped to what the newsletter itself reports.

## Intended changes

- [x] **Approve all**

- [ ] **Update** `wiki/training/anti-autopilot-review-friction.md` — two new proven patterns, one new cited study in the Cognitive debt section
    > See draft below

- [ ] **Create** `wiki/sources/newsletters/every-read-the-code-2026-09-08.md` — source summary

## Page drafts

### wiki/training/anti-autopilot-review-friction.md (updated)

Frontmatter `as_of` moves from `2026-06-29` to `2026-09-08`; append `every-read-the-code-2026-09-08` to `sources:`.

Two new bullets appended to `## Proven patterns`, after the existing "Spec-drift logging" bullet:

```md
- **Trace mechanics, not diffs.** When reviewing a change or investigating a failure, ask the agent to walk the real data/control flow end to end — where the process begins, what happens next, where information goes, which other systems touch it — rather than reading the diff itself. A map of the whole journey catches wrong-but-plausible fixes that a diff alone won't: one practitioner used this to reject two reasonable-sounding incident fixes in favor of the one that matched what had actually happened. *Source: Every, Kieran Klaassen (2026-09-08)*
- **Quiz before merge.** After a long agent session, ask the model for a written explanation of the change plus a quiz on it, and don't merge until you score well. Tests decide whether the code can merge; the quiz decides what you still need to learn — keeping a running list of missed questions as your own syllabus. *Source: Thariq Shihipar, via Every (2026-09-08)*
```

New paragraph appended to the end of `## Cognitive debt` (after the existing three empirical studies and before `## Failure modes`):

```md
**A fourth data point, and an older name for the pattern:** a 2026 review by Margaret Mitchell, Avijit Ghosh, and Samir Passi (arXiv:2608.23642) documents that extended AI-agent use measurably erodes the vigilance, critical thinking, and domain skill human oversight depends on. The underlying dynamic isn't new — it's the "irony of automation," a term coined in 1983 by a safety researcher studying human operators of automated factories and power plants: the more capable the automation gets, the faster the human's own skill erodes. Agents just make it move faster. *Source: Every, Kieran Klaassen, "To Read—Or Not to Read the Code?" (2026-09-08)*
```

New entry at the top of `## Recent changes`:

```md
- [2026-09-08] Added two proven patterns (trace mechanics not diffs; quiz before merge) and a fourth cited study on AI-agent-use skill erosion (Mitchell/Ghosh/Passi, arXiv:2608.23642), framed via the 1983 "irony of automation."
```

### wiki/sources/newsletters/every-read-the-code-2026-09-08.md (new)

```md
---
title: "To Read—Or Not to Read the Code?"
type: source
source_type: newsletter
source_file: raw/newsletters/2026-09-08-to-reador-not-to-read-the-code.md
url: https://every.to/source-code/to-read-or-not-to-read-the-code
published: 2026-09-08
ingested: 2026-09-09
domains: [training, coding]
---

# To Read—Or Not to Read the Code?

Every's Kieran Klaassen on deliberately re-engaging with code after a year of heavy AI delegation: a custom `/ce-explain` command for tracing mechanics rather than diffs, a quiz-before-merge practice borrowed from Thariq Shihipar, and a 2026 paper (Mitchell/Ghosh/Passi, arXiv:2608.23642) documenting measurable skill erosion from extended AI-agent use — the agent-era instance of the 1983 "irony of automation."

## Influenced pages

- [Anti-autopilot review friction](../../training/anti-autopilot-review-friction.md) — two new proven patterns, new cited study

## Key claims extracted

- `/ce-explain`: traces data/control flow through the codebase rather than reading diffs
- Quiz-before-merge: model quizzes the developer on a session before it's allowed to merge
- Mitchell/Ghosh/Passi (arXiv:2608.23642): extended AI-agent use measurably erodes vigilance, critical thinking, domain skill
- "Irony of automation" coined 1983, studying human operators of automated factories/power plants
```

## Schema / vocabulary additions

None.

## Open questions

None beyond the sourcing noted above.
