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

## Related

- [Agent skill methodology](../training/agent-skill-methodology.md) - how to package narrow workflows as maintainable skills.
- [Agent-generated HTML artifacts](../workflows/agent-generated-html-artifacts.md) - adjacent review-artifact pattern for interactive or visual agent outputs.

## Sources

- [ROFI onboarding-video Claude skill](../sources/tweets/onboarding-video-skill-2026-05-13.md)
