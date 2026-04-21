---
type: proposal
sources:
  - raw/newsletters/2026-04-20-we-need-to-talk-about-ai-autopilot.md
  - raw/newsletters/2026-04-16-youre-the-manager-now.md
status: pending
created: 2026-04-21
---

# Proposal: Anti-autopilot review friction

## Summary

This batch adds a practical training pattern the wiki does not currently name clearly: once AI outputs become fluent and mostly right, humans stop truly reviewing them. The proposed antidote is deliberate friction: make a judgment before seeing the answer, insert a review gap, and force explicit reasons for accepting the output. This belongs in `training/`, not just as a scattered note inside broader enablement pages.

## Intended changes

- [x] **Create** `wiki/training/anti-autopilot-review-friction.md` — new training page
  > See draft below.

- [x] **Update** `wiki/training/company-wide-ai-enablement.md` — add anti-autopilot as a company-scale failure mode and operating control
  > Add a `Failure modes` bullet:
  > `- Letting fluent AI output pass as "reviewed" without forcing humans to form an independent judgment first`

- [x] **Update** `wiki/index.md` — add the new training page and refresh counts

- [x] **Create** `wiki/sources/newsletters/every-ai-autopilot.md` — source summary

## Page drafts

### wiki/training/anti-autopilot-review-friction.md (new)

```md
---
title: Anti-autopilot review friction
type: training
as_of: 2026-04-21
sources: [every-ai-autopilot, every-youre-the-manager-now]
---

# Anti-autopilot review friction

As AI output gets more fluent and more often correct, people stop truly checking it. The result is not only hallucinations slipping through, but humans losing track of whether they ever formed their own judgment in the first place. Anti-autopilot review friction is the practice of deliberately inserting small costs back into the workflow so judgment stays human.

## Current guidance

- Write your own rough position before asking the model for its answer
- Separate generation and review in time or surface so the review brain is different from the generation brain
- Force yourself to explain why an accepted output is right for this reader, client, or task
- Use confidence checks as a trigger for more review, not as a substitute for review

## Proven patterns

- **Think before you look.** Create bullets, constraints, or your own thesis first
- **Build in a gap.** Review later, or in a different interface, after attention has reset
- **Require acceptance reasons.** Don't accept "sounds good"; require a defensible why
- **Use forcing functions.** Make the human judge before the AI answer becomes the default anchor

## Failure modes

- Mistaking "I saw it" for "I reviewed it"
- Letting fluency stand in for correctness
- Reviewing too many AI outputs in a row without reset
- Using AI to replace the judgment layer rather than the execution layer

## Sources

- [[sources/newsletters/every-ai-autopilot]]
- [[sources/newsletters/every-youre-the-manager-now]]
```

### wiki/sources/newsletters/every-ai-autopilot.md (new)

```md
---
title: Every — We Need to Talk About AI Autopilot
type: source
source_type: newsletter
source_file: raw/newsletters/2026-04-20-we-need-to-talk-about-ai-autopilot.md
ingested: 2026-04-21
domains: [training]
---

# Every — We Need to Talk About AI Autopilot

Essay on why increasingly fluent AI output makes users less likely to truly review it. The piece connects older automation-bias and fluency-bias research to current AI workflows, then proposes concrete forcing functions: think before looking, create review gaps, and require explicit reasons for accepting output.

## Key claims extracted

- Reliability increases overreliance; people scrutinize tools less once they are often right
- Fluent presentation makes output feel truer than it is
- The strongest interventions are cognitive forcing functions that make humans judge first
- Effective review patterns feel slower and are often disliked, but work better
```
