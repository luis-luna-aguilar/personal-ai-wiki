---
type: proposal
source:
  - raw/newsletters/2026-05-29-compound-engineering-gets-an-upgrade.md
  - raw/newsletters/2026-05-27-after-after-automation.md
  - raw/newsletters/2026-05-24-cheap-competence-new-frontier.md
  - raw/newsletters/2026-05-31-how-we-work-now.md
status: pending
created: 2026-07-08
---

# Proposal: Compound engineering and cheap competence

## Summary

Every's May coverage updates the operating model for AI-native work: compound engineering expands from a four-step coding loop to an eight-step human/AI loop, while "cheap competence" and "after automation" argue that automation shifts human work toward framing, taste, coordination, and judgment. This proposal updates training/workflow pages rather than creating a new tool page.

## Intended changes

- [x] **Update** `wiki/training/ai-native-product-building.md` - add ideate/brainstorm/plan/work/review/polish/compound/repeat and cheap-competence framing.
- [x] **Update** `wiki/training/company-wide-ai-enablement.md` - add cheap competence and "humans above the loop" implications.
- [x] **Update** `wiki/workflows/agentic-orchestration-patterns.md` - add the eight-step compound-engineering loop as a practical agentic workflow.
- [x] **Create** `wiki/sources/newsletters/every-compound-engineering-upgrade-2026-05.md` - source summary.
- [x] **Create** `wiki/sources/newsletters/every-cheap-competence-after-automation-2026-05.md` - source summary.

## Page drafts

### wiki/training/ai-native-product-building.md (updated sections)

```md
---
title: AI-native product building
type: training
domains: [coding]
as_of: 2026-05-29
sources: [..., every-compound-engineering-upgrade-2026-05, every-cheap-competence-after-automation-2026-05]
---

## Current guidance

- As the agentic middle gets cheaper and more reliable, human leverage moves to the beginning and end of the loop: decide what is worth building, define the frame, then polish the final experience after the agent has produced technically working output.
- Use the expanded compound-engineering loop for serious product work: **ideate -> brainstorm -> plan -> work -> review -> polish -> compound -> repeat**.
- Treat cheap competence as a frontier shift, not a replacement for judgment: models automate fixed frames, while humans keep creating and revising the frames.

## Proven patterns

- **AI sandwich for product work.** Humans supply the bread: intent, context, taste, and final judgment. AI handles much of the middle: drafting, coding, gathering, summarizing, and first-pass execution.
- **Polish as a first-class step.** Technically passing work can still feel wrong. Reserve human attention for copy, interaction quality, edge cases, and coherence after the agent has passed deterministic checks.

## Recent changes

- [2026-05-29] Expanded compound engineering loop added: ideate, brainstorm, plan, work, review, polish, compound, repeat.
- [2026-05-27] Cheap competence / after-automation framing added: AI shifts human work toward framing, taste, and judgment rather than eliminating work.

## Sources

- [Every - Compound Engineering Gets an Upgrade](../sources/newsletters/every-compound-engineering-upgrade-2026-05.md)
- [Every - Cheap competence and after automation](../sources/newsletters/every-cheap-competence-after-automation-2026-05.md)
```

### wiki/training/company-wide-ai-enablement.md (updated sections)

```md
---
as_of: 2026-05-27
sources: [..., every-cheap-competence-after-automation-2026-05]
---

## Proven patterns

- **Design for new frames, not only task automation.** Cheap competence means more work can be done inside a given frame, but the higher-value organizational skill is creating better frames: what to investigate, what to ship, what tradeoff matters, and what "good" means.
- **Keep humans at the judgment boundary.** As AI fills in the middle of workflows, employees need stronger habits for framing, taste, coordination, and review rather than only faster execution tactics.

## Failure modes

- **Automation without reframing.** Teams speed up existing tasks but never redesign the workflow or ask what new work becomes possible once competent execution is cheap.

## Recent changes

- [2026-05-27] Added cheap-competence / after-automation framing: AI expands the frontier of human work by shifting scarcity toward framing and judgment.
```

### wiki/workflows/agentic-orchestration-patterns.md (updated sections)

```md
---
as_of: 2026-05-29
sources: [..., every-compound-engineering-upgrade-2026-05]
---

## Current patterns

- **Compound engineering loop.** For product-building agents, the practical loop is now ideate -> brainstorm -> plan -> work -> review -> polish -> compound -> repeat. The agentic middle can be delegated when context and verification are strong; humans spend more time choosing the frame and polishing the outcome.

## Recent changes

- [2026-05-29] Every updated compound engineering from a four-step loop to an eight-step loop that explicitly includes ideation and polish around the agentic work phase.
```

### wiki/sources/newsletters/every-compound-engineering-upgrade-2026-05.md (new)

```md
---
title: Every - Compound Engineering Gets an Upgrade
type: source
source_type: newsletter
source_file: raw/newsletters/2026-05-29-compound-engineering-gets-an-upgrade.md
url: https://every.to/guides/compound-engineering
published: 2026-05-29
ingested: 2026-07-08
domains: [coding, agents, training]
---

# Every - Compound Engineering Gets an Upgrade

Kieran Klaassen updates compound engineering from a four-step engineering loop into an eight-step product loop: ideate, brainstorm, plan, work, review, polish, compound, repeat. The central point is that as the agentic work phase becomes more reliable, human leverage shifts toward deciding what is worth building and polishing the final product experience.

## Influenced pages

- [AI-native product building](../../training/ai-native-product-building.md) - updated loop and polish guidance
- [Agentic orchestration patterns](../../workflows/agentic-orchestration-patterns.md) - compound engineering loop pattern

## Key claims extracted

- The original compound engineering loop was brainstorm -> work -> review -> compound -> repeat.
- The expanded loop is ideate -> brainstorm -> plan -> work -> review -> polish -> compound -> repeat.
- The work phase is becoming less scarce; human judgment is concentrated at the beginning and end.
```

### wiki/sources/newsletters/every-cheap-competence-after-automation-2026-05.md (new)

```md
---
title: Every - Cheap competence and after automation
type: source
source_type: newsletter
source_file:
  - raw/newsletters/2026-05-27-after-after-automation.md
  - raw/newsletters/2026-05-24-cheap-competence-new-frontier.md
  - raw/newsletters/2026-05-31-how-we-work-now.md
published: 2026-05-27
ingested: 2026-07-08
domains: [training]
---

# Every - Cheap competence and after automation

Every's late-May coverage argues that cheap AI competence does not end human work; it changes where human work sits. Once competent execution gets cheap, the scarce work becomes framing, taste, judgment, coordination, and deciding what new work should exist.

## Influenced pages

- [AI-native product building](../../training/ai-native-product-building.md) - cheap-competence bottleneck shift
- [Company-wide AI enablement](../../training/company-wide-ai-enablement.md) - organizational framing and adoption guidance

## Key claims extracted

- AI automates work inside fixed frames, but humans still create and revise frames.
- The middle of many workflows becomes cheaper; the beginning and end become more important.
- AI adoption should redesign work, not only accelerate existing tasks.
```

## Open questions

- Should "cheap competence" become its own trend page later, or stay embedded in training pages for now?
