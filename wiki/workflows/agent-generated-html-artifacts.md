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

## Related

- [Anti-autopilot review friction](../training/anti-autopilot-review-friction.md) - why review artifacts matter for judgment-heavy AI output.
- [AI enablement for software development](../training/ai-enablement-software-development.md) - engineering use cases such as annotated PR explainers and implementation-plan artifacts.

## Sources

- [Thariq on HTML artifacts for Claude Code](../sources/tweets/agent-html-artifacts-2026-05-13.md)
