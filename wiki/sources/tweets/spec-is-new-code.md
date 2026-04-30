---
title: '"The Spec Is the New Code" — Julian De Angelis'
type: source
source_type: tweet
source_file: raw/tweets/2026-04-22-juliandeangeiis-2033303156340240481.md
url: https://x.com/juliandeangeIis/status/2033303156340240481
published: 2026-04-22
ingested: 2026-04-22
domains: [coding, agents]
---

# "The Spec Is the New Code"

Long-form article by Julian De Angelis. Argues that agent failures are primarily communication (ambiguity) failures, not model failures, and that the ecosystem is independently converging on spec-driven development. Evidence: GitHub Spec-Kit (77k stars), OpenAI Symphony (issue-tracker-monitoring agent, requires SPEC.md), The Ralph Loop (PRD in infinite agent loop with git-persisted state), and plan modes in Claude Code/Cursor as platform-level SDD.

## Influenced pages

- [[concepts/spec-driven-development]] — updated current status; added Ralph Loop, Symphony, and plan-mode-as-SDD patterns

## Key claims extracted

- Agent failures are mostly ambiguity/communication failures, not model failures
- GitHub Spec-Kit: 77,000 stars; agent-agnostic (Claude Code, Cursor, others)
- OpenAI Symphony: monitors issue tracker; requires SPEC.md as contract; spawns autonomous agents per issue
- The Ralph Loop: PRD in infinite agent loop; progress in files + git, not context window
- Plan mode in Claude Code and Cursor = lightweight built-in SDD step
- Convergence is independent — tools built it separately without coordination
