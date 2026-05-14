---
type: proposal
sources:
  - raw/tweets/2026-05-13-trq212-2052809885763747935.md
  - raw/tweets/2026-05-13-antirez-2053113951123054963.md
  - raw/tweets/2026-05-13-deryatr_-2052973235705368957.md
status: pending
created: 2026-05-13
---

# Proposal: Agent-generated HTML artifacts

## Summary

Thariq argues that single-file HTML artifacts are becoming a better review surface for complex agent work than long Markdown plans because they can combine prose, tables, SVG diagrams, annotated diffs, controls, live previews, and export buttons. The antirez counterpoint is important: Markdown remains more semantically dense and token-efficient, so the useful distinction is not "replace Markdown," but "use HTML when review, visualization, comparison, or interactivity matters."

## Intended changes

- [x] **Create** `wiki/workflows/agent-generated-html-artifacts.md` — reusable workflow for when agents should produce HTML artifacts instead of Markdown
    > See draft below

- [x] **Update** `wiki/workflows/agentic-orchestration-patterns.md` — add artifact-based review to current patterns
    > Add a bullet: `**Review artifacts over raw transcripts.** For complex agent work, ask for purpose-built review artifacts (HTML explainers, annotated diffs, comparison grids, one-off editors) when a human needs to inspect options, tune values, or export structured decisions back into the workflow.`

- [x] **Update** `wiki/training/agent-skill-methodology.md` — add caution that this should not become an always-on `/html` skill
    > Add to Failure modes: `**Artifact maximalism:** HTML is useful for review and interaction, but making every agent output HTML can waste tokens and make version control noisy. Keep Markdown for durable, versioned knowledge and use HTML when the artifact changes the review behavior.`

- [x] **Create** `wiki/sources/tweets/agent-html-artifacts-2026-05-13.md` — source summary
    > See draft below

## Page drafts

### wiki/workflows/agent-generated-html-artifacts.md (new)

```markdown
---
title: Agent-generated HTML artifacts
type: workflow
domains: [agents, coding]
subcategory: agentic-orchestration-patterns
tags: [agentic]
as_of: 2026-05-13
sources: [agent-html-artifacts-2026-05-13]
---

# Agent-generated HTML artifacts

Single-file HTML artifacts are useful when an agent needs to make work reviewable, visual, or interactive rather than merely recorded. They are strongest for comparison grids, annotated diffs, implementation explainers, design explorations, one-off editors, dashboards, and artifacts that export decisions back as Markdown, JSON, prompts, or diffs.

## Current guidance

- Use HTML when the human needs to compare options, inspect visual structure, tune values, or review code/data with annotations.
- Keep Markdown for durable notes, source summaries, versioned instructions, and compact knowledge that should diff cleanly.
- End interactive artifacts with an export path: copy as Markdown, JSON, prompt text, config diff, or issue list.
- Treat generated HTML as a review surface, not automatically as production UI.

## Patterns

- Design or onboarding alternatives laid out side by side with labeled tradeoffs.
- PR explainers with rendered diffs, severity-coded findings, and diagrams.
- Implementation plans with mockups, data-flow diagrams, and key code snippets.
- Throwaway editors for prioritizing tickets, editing feature flags, tuning prompts, or annotating datasets.

## Failure modes

- Replacing every Markdown artifact with HTML and losing token density, clean diffs, and long-term maintainability.
- Producing decorative UI instead of a clearer decision surface.
- Forgetting the export path, forcing the human to manually translate visual choices back into the agent workflow.

## Sources

- [Thariq on HTML artifacts for Claude Code](../sources/tweets/agent-html-artifacts-2026-05-13.md)
```

### wiki/sources/tweets/agent-html-artifacts-2026-05-13.md (new)

```markdown
---
title: Agent-generated HTML artifacts — Thariq and antirez
type: source
source_type: tweet
source_file: raw/tweets/2026-05-13-trq212-2052809885763747935.md
published: 2026-05-13
ingested: 2026-05-13
domains: [agents, coding]
---

# Agent-generated HTML artifacts — Thariq and antirez

Thariq describes using Claude Code to generate single-file HTML artifacts for richer agent-human review: comparison grids, implementation plans, PR explainers, design prototypes, reports, and one-off editors with export buttons. Antirez provides the counterpoint that Markdown is more semantically dense and token-efficient, so HTML should not replace Markdown wholesale.

## Influenced pages

- [Agent-generated HTML artifacts](../../workflows/agent-generated-html-artifacts.md) — new workflow
- [Agentic orchestration patterns](../../workflows/agentic-orchestration-patterns.md) — review-artifact pattern
- [Agent skill methodology](../../training/agent-skill-methodology.md) — artifact maximalism caveat

## Key claims extracted

- HTML can combine text, tables, SVG diagrams, annotated diffs, controls, live previews, and export buttons in a single artifact.
- HTML artifacts can keep humans more engaged with complex agent work than 100+ line Markdown files.
- Markdown remains better for compact, versioned, durable knowledge because it is semantically denser and easier to diff.
```

