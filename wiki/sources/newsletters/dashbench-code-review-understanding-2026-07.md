---
title: DashBench and understanding-preserving AI code review
type: source
source_type: newsletter
source_file: raw/newsletters/2026-07-08-claude-cowork-now-runs-on-mobile.md
url: https://codenewsletter.ai/p/anthropic-extends-fable-5-access-doordash-drops-dashbench
published: 2026-07-08
ingested: 2026-07-08
domains: [coding, agents, training]
---

# DashBench and understanding-preserving AI code review

The Code reports that DoorDash released DashBench, a benchmark that replays historical PRs to evaluate AI code reviewers against real issues. The same issue summarizes Geoffrey Litt's argument that engineers should still understand agent-written code because understanding is what lets them participate in the next loop.

## Influenced pages

- [AI PR and code review](../../workflows/ai-pr-code-review.md) - creates a dedicated workflow for pull-request analysis, review execution, historical PR replay, review artifacts, and understanding-preserving review.
- [Evals for agentic software development](../../training/evals-for-agentic-software-development.md) - keeps broader eval-stack framing and links to the dedicated PR-review workflow.
- [AI enablement - software development](../../training/ai-enablement-software-development.md) - adds PR review as a first-class enablement workflow.
- [Agent evals](../../concepts/agent-evals.md) - adds historical PR replay as an eval-infrastructure pattern.
- [Agentic orchestration patterns](../../workflows/agentic-orchestration-patterns.md) - links review artifacts and repo-local review standards to the dedicated workflow.

## Key claims extracted

- DashBench replays DoorDash historical PRs to test whether AI reviewers catch real issues.
- The Code reports a Kimi K2.6 + Claude Fable 5 combo beat DoorDash's production setup on weighted recall.
- Geoffrey Litt argues verification is not the only reason to read agent-written code; comprehension drives the next move.
- His `explain-diff` skill turns changes into teaching docs and quizzes.
- The practical workflow combines automated review execution with human understanding preservation.
