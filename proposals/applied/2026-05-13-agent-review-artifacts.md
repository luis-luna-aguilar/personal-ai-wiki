---
type: proposal
sources:
  - raw/tweets/2026-05-13-trq212-2052809885763747935.md
  - raw/tweets/2026-05-13-deryatr_-2052973235705368957.md
status: pending
created: 2026-05-13
---

# Proposal: Purpose-built review artifacts for agent work

## Summary

The HTML-artifact thread includes a broader operating pattern: agents should often produce task-specific review artifacts, not just better prompts or longer plans. The examples are concrete: UI comparison grids, implementation plans with mockups and data flow, annotated PR explainers, interactive animation tuning surfaces, Linear prioritization boards, feature-flag editors, and prompt editors with live previews.

## Intended changes

- [x] **Update** `wiki/training/anti-autopilot-review-friction.md` — add review artifacts as a practical way to slow down fluent but shallow acceptance
    > Add under `## Current guidance`: `Ask agents to turn high-risk or judgment-heavy outputs into review artifacts before accepting them: comparison grids for options, annotated diffs for code, dashboards for data, and one-off editors for structured decisions. The point is to make review easier, not to make output look more polished.`

- [x] **Update** `wiki/training/ai-enablement-software-development.md` — add PR explainers and implementation-plan artifacts as engineering enablement examples
    > Add to practical guidance: `For complex PRs, ask the agent to generate an annotated HTML explainer with the actual diff, architecture diagram, risk areas, and reviewer questions. This can improve review quality when the default GitHub diff is too low-context.`

- [x] **Create** `wiki/sources/tweets/agent-review-artifacts-2026-05-13.md`
    > See draft below

## Page drafts

### wiki/sources/tweets/agent-review-artifacts-2026-05-13.md (new)

```markdown
---
title: Purpose-built review artifacts for agent work
type: source
source_type: tweet
source_file: raw/tweets/2026-05-13-trq212-2052809885763747935.md
published: 2026-05-13
ingested: 2026-05-13
domains: [agents, coding]
---

# Purpose-built review artifacts for agent work

Thariq's HTML-artifact thread gives concrete examples of agent outputs designed around review: UI-option grids, implementation plans with mockups and data flow, PR explainers with annotated diffs, animation tuners with sliders, one-off ticket prioritization boards, feature-flag editors, and prompt editors with live previews.

## Influenced pages

- [Anti-autopilot review friction](../../training/anti-autopilot-review-friction.md)
- [AI enablement for software development](../../training/ai-enablement-software-development.md)

## Key claims extracted

- The human role in agent-heavy work often shifts toward taste, review, prioritization, and boundary setting.
- A purpose-built review artifact can make the human more likely to inspect the work carefully than a long Markdown plan or raw transcript.
- The artifact should export the human's decisions back into the workflow as Markdown, JSON, prompt text, or a diff.
```

