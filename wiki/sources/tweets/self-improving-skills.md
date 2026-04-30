---
title: Self-improving agent skills — auto-improvement loops
type: source
source_type: tweet
source_file: raw/tweets/2026-04-22-tricalt-2032179887277060476.md
url: https://x.com/tricalt/status/2032179887277060476
published: 2026-04-22
ingested: 2026-04-22
domains: [agents]
---

# Self-improving agent skills — auto-improvement loops

Two sources. (1) tricalt article: skills are static but environments drift; treat skills as living components with closed improvement feedback loops; diagnose routing vs instructions vs tool calls. (2) Ole Lehmann tweet: meta-skill that auto-improves any other skill in 5 steps (run → score → change one thing → re-run → keep if better). Based on Karpathy's autoresearch method.

## Influenced pages

- [Agent improvement loop](../../concepts/agent-improvement-loop.md) — self-improving skills section added

## Key claims extracted

- Skills fail quietly when codebases change, models update, or user patterns shift
- Failures are often invisible until output is noticeably worse
- Loop needs to diagnose routing vs instructions vs tool call as separate failure points
- Meta-skill: 5-step prompt optimization loop; fully automated; improves skills without human intervention
- Based on Karpathy autoresearch method
