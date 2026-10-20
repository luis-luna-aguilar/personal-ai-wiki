---
title: Acceptance contracts and test oracles
type: training
domains: [coding]
as_of: 2026-10-19
sources: [lavaee-verification-pyramid-2026-10, rauchg-gdp-ts-2026-10]
---

# Acceptance contracts and test oracles

When a coding agent reports "done", that is a claim. It becomes evidence only when checks the agent didn't write and can't change show the acceptance criteria are met. This page covers the two things those checks rest on: the acceptance contract, written and reviewed before the agent starts, and oracles, the checks that decide pass or fail against something the agent can't game. The wider eval stack (deterministic gates, MVES, shadow mode, judges, browser proof) is on [Evals for agentic software development](evals-for-agentic-software-development.md).

## Current guidance

- Write the acceptance contract before the code: who acts, the starting state, the action, the checkable result on screen and in stored state, a numeric threshold where one applies, the oracle that checks it, and which dependencies must be real. A person reviews it before the agent starts.
- Take expected values from the criteria or a reference, never from running the new code. LLM-written tests tend to encode what the code does rather than what it should do, so a test whose expectation came from the implementation agrees with the bug.
- Read the test diff before the implementation diff. A weakened assertion, deleted case, or newly mocked dependency makes a green check meaningless.
- Block fixes that edit, skip, or delete a failing test with a hook or CI check, not a prompt rule, so "green" can't come from moving the goalposts.

## Oracles agents can't game

An oracle is whatever decides pass/fail against something trusted. Fixed example asserts are the easiest for an agent to satisfy without being right. Harder to game:

- **Property-based tests** check an invariant over thousands of generated inputs ("output is always sorted").
- **Metamorphic tests** compare related runs (same inputs at 30 and 120 FPS must give the same outcome).
- **Differential tests** run old vs new, or yours vs a reference, on the same input.
- **Mutation tests** plant small faults; if tests still pass, they aren't testing what you think.
- **Approved snapshots** change only when a person approves the new snapshot.
- **Invariants and contracts** check pre/post-conditions on every run.
- **Proof-carrying types** make a check impossible to skip: the sensitive function demands a compile-time proof about its exact arguments that only one trusted module can mint, so a missing, stale, or mismatched authorization check is a type error, and a lint preset blocks forged proofs ([gdp-ts](../tools/gdp-ts.md) for TypeScript).
- **Seeded replays** re-run a recorded session deterministically.

The agent can write property tests; a person decides which matter. Treat coverage as a record of what ran, not of what was checked.

## Failure modes

- Prompt-only guards on test integrity — an instruction not to suppress failing tests is not a runtime check; enforce it with a hook or CI step

## Recent changes

- [2026-10-19] Added proof-carrying types (gdp-ts) as an oracle: authorization checks enforced by the TypeScript compiler and a lint preset rather than by review.
- [2026-10-14] Added Lavaee's verification-pyramid guidance: acceptance contract first, oracles agents can't game, test-diff-first review, multi-judge mean-plus-veto scoring, and scenario-driven browser and performance checks.
- [2026-10-20] Page created, split out of [Evals for agentic software development](evals-for-agentic-software-development.md).

## Related

- [Evals for agentic software development](evals-for-agentic-software-development.md) — the full eval stack these checks feed
- [AI PR and code review](../workflows/ai-pr-code-review.md) — fresh-session review
- [gdp-ts](../tools/gdp-ts.md) — proof-carrying types for TypeScript

## Sources

- [Agents Write the Code. Your System Has to Prove It. — Alex Lavaee](../sources/tweets/lavaee-verification-pyramid-2026-10.md)
- [rauchg/gdp-ts — Ghosts of Departed Proofs for TypeScript (GitHub)](../sources/repos/rauchg-gdp-ts-2026-10.md)
