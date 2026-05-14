---
type: proposal
source: raw/tweets/2026-05-13-bidah-2053071057737679138.md
status: pending
created: 2026-05-13
---

# Proposal: Onboarding videos as an agent-skill use case

## Summary

ROFI describes a Claude skill that turns ordered app screenshots into animated onboarding walkthroughs with pointer movement, highlighted targets, pauses, regenerated UI, and polished output before a mobile-app paywall. The triage comment asks for a root `use-cases` area; because the current schema has no `use-case` type or directory, this proposal asks for that structural change explicitly before creating the page.

## Intended changes

- [x] **Update** `LLM-INSTRUCTIONS.md` — add `wiki/use-cases/` and a `use-case` page type to the operating schema
    > Add `use-cases/` to the directory layout and add `use-case` to the allowed `type:` values for pages.

- [x] **Create** `wiki/use-cases/onboarding-videos-from-screenshots.md` — first use-case page
    > See draft below

- [x] **Update** `wiki/index.md` — add a `## Use Cases` section with the new page
    > Add: `- [use-cases/onboarding-videos-from-screenshots](use-cases/onboarding-videos-from-screenshots.md) — using agent skills to turn app screenshots into animated onboarding or training videos *(as_of: 2026-05-13)*`

- [ ] **Update** `wiki/training/agent-skill-methodology.md` — add production-workflow example
    > Add to Evidence from practice: `A May 2026 Claude-skill example packages a narrow creative/business workflow: ordered screenshots in, animated onboarding walkthrough out, including pointer motion, tap highlights, pauses, and regenerated UI.`

- [x] **Create** `wiki/sources/tweets/onboarding-video-skill-2026-05-13.md`
    > See draft below

## Page drafts

### wiki/use-cases/onboarding-videos-from-screenshots.md (new)

```markdown
---
title: Onboarding videos from screenshots
type: use-case
domains: [creative, agents]
tags: [agentic]
as_of: 2026-05-13
sources: [onboarding-video-skill-2026-05-13]
---

# Onboarding videos from screenshots

Agent skills can package narrow creative production workflows, such as turning ordered app screenshots into short onboarding or training videos. The useful pattern is not just "generate a video"; it is converting static UI states into a didactic walkthrough with motion, emphasis, pauses, and a clear value moment.

## Current guidance

- Use screenshots or screen states as structured input.
- Ask the skill to teach the workflow, not merely replay the app.
- Highlight tap targets before actions and pause on screens that carry the value proposition.
- Use this for onboarding, training, feature education, and internal product walkthroughs.

## Why it matters

For mobile apps, pre-paywall onboarding often needs to prove that the product works before asking for payment. For teams, the same pattern applies to training material: show the actual workflow, emphasize decisions, and make the steps easier to follow than a raw recording.

## Failure modes

- Raw screen recordings that show motion but do not teach the user what matters.
- Overproduced videos that hide the real product interaction.
- Treating the skill as a generic video generator instead of a reusable workflow with specific inputs and quality criteria.

## Sources

- [ROFI onboarding-video Claude skill](../sources/tweets/onboarding-video-skill-2026-05-13.md)
```

### wiki/sources/tweets/onboarding-video-skill-2026-05-13.md (new)

```markdown
---
title: ROFI onboarding-video Claude skill
type: source
source_type: tweet
source_file: raw/tweets/2026-05-13-bidah-2053071057737679138.md
published: 2026-05-13
ingested: 2026-05-13
domains: [creative, agents]
---

# ROFI onboarding-video Claude skill

ROFI describes a Claude skill that turns an ordered sequence of app screenshots into animated onboarding walkthroughs with pointer movement, highlighted tap targets, pauses, regenerated interactive UI, and polished videos intended for mobile-app onboarding before a paywall.

## Influenced pages

- [Onboarding videos from screenshots](../../use-cases/onboarding-videos-from-screenshots.md)
- [Agent skill methodology](../../training/agent-skill-methodology.md)

## Key claims extracted

- Didactic onboarding videos can teach the product better than raw screen recordings.
- A skill can encapsulate the workflow from screenshots to motion walkthrough.
- This is a practical example of skills packaging narrow creative/business outcomes, not only coding tasks.
```

