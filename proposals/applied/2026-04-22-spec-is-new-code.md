---
type: proposal
source: raw/tweets/2026-04-22-juliandeangeiis-2033303156340240481.md
status: pending
created: 2026-04-22
---

# Proposal: "The Spec Is the New Code" — SDD convergence across tools

## Summary

A synthesis article by Julian De Angelis arguing the entire ecosystem is independently converging on Spec-Driven Development. New evidence since the last SDD page update: GitHub Spec-Kit at 77k stars, OpenAI Symphony (monitors issue tracker, requires SPEC.md), and "The Ralph Loop" (PRD in infinite agent loop with git-persisted state). The article also makes the claim that agent failures are primarily communication failures, not model failures.

## Intended changes

- [x] **Update** `wiki/concepts/spec-driven-development.md` — add ecosystem convergence signal, three new patterns, and updated status
    > **Replace `## Current status (as of 2025-10-15)` section with:**
    > ```markdown
    > ## Current status (as of 2026-04-22)
    >
    > - The ecosystem is independently converging on spec-first approaches from multiple directions — not just dedicated SDD tools
    > - GitHub Spec-Kit: 77,000 stars as of April 2026; agent-agnostic; works across Claude Code, Cursor, and others
    > - OpenAI Symphony: monitors issue trackers, spins up autonomous agents per issue; requires a `SPEC.md` as the contract between human and agent
    > - "The Ralph Loop": PRD placed in an infinite agent loop; progress persists in files and git (not in context window), so the agent can resume across sessions
    > - Plan mode in Claude Code and Cursor is now framed as a lightweight built-in SDD step — the ecosystem is absorbing the concept at the platform level
    > - The core argument gaining traction: agent failures are mostly *communication failures*, not model failures. The problem is ambiguity in instructions, not model capability.
    > ```
    >
    > **Add new section `## New patterns (2026)` after `## Spec vs memory bank`:**
    > ```markdown
    > ## New patterns (2026)
    >
    > ### The Ralph Loop
    > A PRD lives in an infinite agent loop. The agent executes steps, writes progress to files and git commits after each step, and can be interrupted and resumed without losing state. The loop continues until the PRD is complete. Key insight: progress in files/git, not in the context window.
    >
    > ### OpenAI Symphony
    > Monitors your issue tracker, identifies new issues, spins up autonomous coding agents per issue. Requires a `SPEC.md` as the formal contract between human intent and agent execution. No `SPEC.md` → no agent run.
    >
    > ### Plan mode as lightweight SDD
    > Built-in plan modes in Claude Code (shift-tab) and Cursor act as a minimal spec-and-plan step before execution. The ecosystem is absorbing SDD at the platform level for users who never use a dedicated SDD tool.
    > ```
    >
    > **Update `as_of: 2026-04-22` in frontmatter.**
    > **Add to sources list: `spec-is-new-code`.**
    > **Add to `## Recent changes`:**
    > ```
    > - [2026-04-22] Added ecosystem convergence signal: Spec-Kit 77k stars, OpenAI Symphony, The Ralph Loop, and plan mode as built-in SDD step
    > ```

- [x] **Create** `wiki/sources/tweets/spec-is-new-code.md` — source summary
    > See draft below

## Page drafts

### wiki/sources/tweets/spec-is-new-code.md (new)

```md
---
title: "The Spec Is the New Code" — Julian De Angelis
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
```
