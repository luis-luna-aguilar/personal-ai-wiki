---
title: Introducing dynamic workflows in Claude Code
type: source
source_type: article
source_file: raw/articles/2026-06-03-claudecom-blog-introducing-dynamic-workflows-in-claude-code.md
url: https://claude.com/blog/introducing-dynamic-workflows-in-claude-code
published: 2026-05-28
ingested: 2026-06-03
domains: [coding, agents]
---

# Introducing dynamic workflows in Claude Code

Anthropic announces dynamic workflows in Claude Code (research preview): Claude dynamically writes orchestration scripts that run tens to hundreds of parallel subagents in a single session, plans and splits the task, verifies each result (with adversarial agents trying to refute findings) before folding it in, and iterates until answers converge. Targets long-running parallel engineering work (hours to days) — bug hunts, audits, large migrations, double-checked critical work — and checkpoints progress so interrupted runs resume.

## Influenced pages
- [Claude Code](../../tools/claude-code.md) — new `## Dynamic workflows` section, recent-change entry
- [State of Coding](../../state-of/coding.md) — extended Claude Code leader line, recent-change entry
- [Agentic orchestration patterns](../../workflows/agentic-orchestration-patterns.md) — added to "Where these patterns surfaced"

## Key claims extracted
- Dynamic workflows: Claude dynamically writes orchestration scripts running tens-to-hundreds of parallel subagents in a single session → plan → split → parallel fan-out → verify before merge → iterate to convergence.
- Adversarial verification: independent agents attempt the problem from different angles; other agents try to break each finding before it reaches the user.
- Built for parallel/long-running work spanning hours to days; checkpoints progress and resumes interrupted runs; coordination happens outside the conversation.
- Enabled via `ultracode` (effort menu; sets effort to xhigh; Claude auto-decides when to spawn a workflow). Auto mode recommended. Alternatively ask Claude to "create a workflow."
- Consumes substantially more tokens than a typical session; first run prompts for confirmation; org admins can disable via managed settings.
- Availability (research preview): Claude Code CLI, Desktop, VS Code extension; Claude API; Amazon Bedrock; Vertex AI; Microsoft Foundry. On by default for Max/Team/API; off by default (admin-enabled) for Enterprise.
- Use cases cited: codebase-wide bug hunts, profiler-guided optimization audits, security/hardening passes (auth, input validation, unsafe patterns), large migrations and language ports across thousands of files, high-stakes double-checked work.
- Flagship case: Bun ported Zig→Rust with dynamic workflows — ~750,000 lines of Rust, 99.8% test suite passing, 11 days first commit to merge; lifetime-mapping workflow, behavior-identical per-file port (hundreds of parallel agents + 2 reviewers/file), build/test fix loop, overnight data-copy cleanup opening one PR per fix. Not yet in production.
- Published 2026-05-28.
