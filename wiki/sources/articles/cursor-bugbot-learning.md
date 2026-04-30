---
title: Bugbot now self-improves with learned rules
type: source
source_type: article
source_file: raw/articles/2026-04-10-cursorcom-blog-bugbot-learning.md
url: https://cursor.com/blog/bugbot-learning
ingested: 2026-04-10
domains: [coding, agents]
---

# Bugbot now self-improves with learned rules

Cursor describes Bugbot's shift from purely offline improvement to a live learning loop based on production PR feedback. The core mechanism is simple: Bugbot turns reactions, replies, and human-reviewer comments from merged PRs into candidate rules, promotes rules that earn positive signal, and disables rules that consistently perform poorly.

## Influenced pages

- [Cursor](../../tools/cursor.md) — adds a substantive Bugbot product update and refreshes current status
- [Agent improvement loop](../../concepts/agent-improvement-loop.md) — adds a concrete example of a production system turning live feedback into structured agent improvements
- [Coding](../../history/state-of/coding.md) — refreshes Cursor's line with the Bugbot signal

## Key claims extracted

- Cursor says Bugbot's resolution rate improved from 52% at launch to 78.13%
- The comparison table in the source covers 50,310 public PRs for Bugbot
- Cursor compares Bugbot against Greptile, CodeRabbit, GitHub Copilot, Codex, and Gemini Code Assist in the same post
- Cursor says Bugbot previously improved only through offline experiments
- The new learning loop uses reactions to Bugbot comments, replies to Bugbot comments, and human reviewer comments
- Candidate rules are promoted or disabled based on future signal from incoming PRs
- Cursor says 110,000+ repos have enabled learning and generated 44,000+ learned rules

## Caveats

- The ranking and resolution-rate comparison are vendor-reported
- The source covers only public repositories and uses an LLM judge to determine whether comments were addressed
- The post is product-focused and does not publish full methodology details beyond the brief description captured here
