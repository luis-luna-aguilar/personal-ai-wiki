---
title: AI delegation management
type: training
domains: [agents, training]
tags: [agentic]
as_of: 2026-08-04
sources: [management-as-ai-superpower-2026-07, andy-matuschak-agent-loop-tempo-2026-07, design-layer-framework-2026-08-04]
---

# AI delegation management

Working with agents is increasingly a management skill: define the job, explain what good looks like, bound the agent's authority, and review outcomes without losing the mental model needed to steer the next round.

## Current guidance

- Delegate when the human baseline time is high enough to justify prompt, wait, and review overhead.
- Estimate probability of success before delegating. If the agent has a low chance of meeting the bar and review is expensive, doing the task yourself may still be faster.
- Write delegation documents like managers already do: purpose, constraints, authority limits, deliverables, interim checkpoints, and definition of done.
- Match loop tempo to the work. Fast 1-2 minute loops keep the human in control; slow delegated loops work when the human can ignore details until checkpoints. Mid-speed 10-30 minute loops can create context switching and comprehension loss.
- Write the spec before execution starts, not after — encode constraints, standards, and what "good" looks like so both people and agents downstream can make the decisions you would make. See the worked example under Proven patterns.

## Proven patterns

- Use domain expertise to explain the output standard and catch subtle failures.
- Convert repeated delegation into templates, checklists, or skills once the first few runs are stable.
- Ask for interim evidence when the cost of a wrong direction is high.
- **Spec-first delegation, worked example.** Before any build starts, write a spec covering an overview, a hero scenario (a concrete walkthrough of the primary use case), functional and behavioral requirements, explicit non-goals, and failure modes — the details AI can't infer because they depend on how you live and work, not on general knowledge. Worked example (a personal "friend tracker" app): overview states the goal in one line; the hero scenario describes a specific Sunday-morning walkthrough; behavioral rules define what counts as "contact" and forbid nagging notifications; non-goals rule out gamification and relationship scoring; failure modes name what "gone wrong" looks like (feels like obligation, generic suggestions, more than 3 people surfaced at once). This generalizes [spec-driven development](../concepts/spec-driven-development.md)'s coding-specific spec-first practice to delegating any kind of work, human or agent. (Aishwarya Reganti, Aug 2026)
- **Targeted review questions over exhaustive reading.** When an agent produces a large multi-file output, ask four or five pointed questions that expose likely failure points — "How are you handling auth?", "What happens when a token expires mid-session?", "What are the different failure paths?" — rather than reading every line. The domain expertise is in knowing what to ask, not in reading everything.
- **Turn recurring corrections into reusable instructions.** When the same correction keeps recurring across AI drafts, write it into a standing instruction or prompt rule instead of correcting it again next time — converts one-off taste into something reusable by the team and its agents.
- **Evaluate new tools by the problem they solve, not by novelty.** Skip tools that take a long time to learn or pull you back into low-level execution unless they solve a real, understood problem; also check whether an agent, not just a person, can use the tool.

## Failure modes

- Delegating vague work where the desired output is specific but unstated.
- Creating partial-control loops where the human is responsible for planning and review but cannot keep enough context in working memory.
- Treating speed as success when review and correction consume the saved time.
- **Constraint drift.** AI output quality drifts as models, inputs, and context change; a setup that works well on day one can quietly degrade by month three with no obvious trigger unless someone deliberately re-checks output against the original spec on a schedule.

## Recent changes

- [2026-08-04] Added spec-first "design layer" framework: a worked spec example, targeted review questions, converting recurring corrections into reusable instructions, tool selection by problem-fit, and constraint drift as a failure mode.

## See also

- [Spec-Driven Development](../concepts/spec-driven-development.md) — the coding-specific version of writing a spec before an agent executes
- [Anti-autopilot review friction](anti-autopilot-review-friction.md) — deliberate review friction techniques, including targeted-question review artifacts

## Sources

- [Management as AI superpower](../sources/articles/management-as-ai-superpower-2026-07.md)
- [Andy Matuschak on agent loop tempo](../sources/tweets/andy-matuschak-agent-loop-tempo-2026-07.md)
- [To Stay Ahead on AI, Think Like a Designer](../sources/newsletters/design-layer-framework-2026-08-04.md)
