---
title: AI code review and benchmark integrity
type: source
source_type: newsletter
source_file: raw/newsletters/2026-06-26-alibaba-allegedly-cloned-claude.md
url: https://jangiacomelli.com/blog/3-tips-for-ai-code-review-that-doesnt-suck/
published: 2026-06-26
ingested: 2026-07-07
domains: [coding, agents]
---

# AI code review and benchmark integrity

The Code summarizes practical AI code-review advice: useful review depends less on a smarter generic reviewer and more on small PRs, project-specific standards, and deliberate CI trigger points. AINews adds a related benchmark-integrity concern: public coding benchmarks can be hacked by models retrieving known solutions from the internet or git history, making harness design part of the eval.

## Influenced pages

- [Evals for agentic software development](../../training/evals-for-agentic-software-development.md) — adds review and benchmark-integrity guidance.
- [Agent evals](../../concepts/agent-evals.md) — adds public benchmark leakage caveat.
- [Agentic orchestration patterns](../../workflows/agentic-orchestration-patterns.md) — adds review-noise failure mode.

## Key claims extracted

- AI review quality improves when PRs are small and standards are explicit.
- Team-agreed review criteria should live in Markdown, not only in reviewer taste.
- AI review should often run as an explicit CI job rather than on every push.
- Public coding benchmarks are vulnerable when models can retrieve solutions from internet or git history.
- No-internet and leakage-controlled harnesses are becoming important for coding-agent evals.
