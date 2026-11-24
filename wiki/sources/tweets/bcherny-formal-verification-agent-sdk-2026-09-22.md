---
title: Boris Cherny — formally verifying the Claude Agent SDK with Lean and Opus 5.5
type: source
source_type: tweet
source_file: raw/tweets/2026-10-26-bcherny-2102543349102338309.md
url: https://x.com/bcherny/status/2102543349102338309
published: 2026-09-22
ingested: 2026-10-26
domains: [coding, models]
---

# Boris Cherny — formally verifying the Claude Agent SDK with Lean and Opus 5.5

X thread from Claude Code lead Boris Cherny on launch day of Opus 5.5. He used the model to formally verify the Claude Agent SDK in Lean, sometimes combined with TLA+, and a couple of short prompts produced 16 PRs fixing bugs and race conditions, despite his not knowing either language well. A follow-up sketches the loop (model a race-prone part, find counterexamples, reproduce), and a reply from formal-methods author Hillel Wayne questions whether models can choose good system properties. The attached video was not reviewed.

## Influenced pages

- [Acceptance contracts and test oracles](../../training/acceptance-contracts-and-test-oracles.md) — model-checked specifications as an oracle
- [Claude Opus 5.5](../../models/claude-opus-5-5.md) — early-user formal-verification result
- [AI formal verification](../../trends/ai-formal-verification.md) — non-specialist formal-methods example

## Key claims extracted

- Opus 5.5 + Lean formally verified the Claude Agent SDK; a couple of short prompts → 16 PRs fixing bugs and race conditions
- TLA+ also works well; combining Lean and TLA+ helps find data-flow, concurrency and state-management issues; TLA+ preferred for race conditions
- Loop (2026-09-23 follow-up, truncated): build a model of a tricky state machine or race-prone code, find counterexamples (suspected bugs), reproduce them
- Cherny does not know either language well; says Claude is excellent at both
- Hillel Wayne: models have been very bad at proposing even beginner-level high-level system properties (last tried Fable 5.1); Cherny: Opus 5.5 "feels much better"
- Side note: Cherny runs at least 10 Claude Tag/Projects sessions at a time
