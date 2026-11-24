---
title: Acceptance contracts and test oracles
type: training
domains: [coding]
as_of: 2026-10-22
sources: [lavaee-verification-pyramid-2026-10, rauchg-gdp-ts-2026-10, bcherny-formal-verification-agent-sdk-2026-09-22, openai-low-resource-programming-languages-2026-10-19, anthropic-formal-verification-2026-10-22]
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
- **Differential tests** run old vs new, or yours vs a reference, on the same input. For migrations this is the main oracle: OpenAI's COBOL-migration eval requires byte-for-byte parity of outputs between the COBOL original and the rewrite on hidden tests, and passes a migration only if every test passes. It catches changes a reviewer would miss: COBOL drops extra decimal digits unless told to round, so a rewrite that rounds runs cleanly and still gets the money wrong ([MultiLangBench](../benchmarks/multilangbench.md)).
- **Mutation tests** plant small faults; if tests still pass, they aren't testing what you think.
- **Approved snapshots** change only when a person approves the new snapshot.
- **Invariants and contracts** check pre/post-conditions on every run.
- **Proof-carrying types** make a check impossible to skip: the sensitive function demands a compile-time proof about its exact arguments that only one trusted module can mint, so a missing, stale, or mismatched authorization check is a type error, and a lint preset blocks forged proofs ([gdp-ts](../tools/gdp-ts.md) for TypeScript).
- **Model-checked specifications** have the agent write a formal model of the risky part of the code (TLA+ for concurrency and races, Lean for state and data flow), let the checker search for counterexamples, then reproduce each one in the real code before fixing it. Boris Cherny reports that a couple of prompts to Opus 5.5 turned the Claude Agent SDK into 16 bug- and race-fix PRs, without his knowing either language well. The caveat: models have been weak at choosing the high-level properties worth checking, so a person should review those (Hillel Wayne).
- **Proved fuzz tests** turn a fuzz test you already have into a statement ("this entry point never crashes for any input under 64 MB") and have the agent prove it over the compiled binary. A proof checker, not a reviewer, validates the proof, so you only need to trust the statement, the machine model and the checker. Anthropic and Theorem did this for 239 OSS-Fuzz entry points in 123 libraries, and the attempt itself surfaced bugs fuzzing would rarely reach, such as an underflow that only triggered on rare ~20 MB inputs. The caveat: the proof holds only for the modeled machine (here single-threaded static RISC-V builds with musl) and only for what the test checks. More on [AI formal verification](../trends/ai-formal-verification.md).
- **Seeded replays** re-run a recorded session deterministically.

The agent can write property tests; a person decides which matter. Treat coverage as a record of what ran, not of what was checked.

## Failure modes

- Prompt-only guards on test integrity — an instruction not to suppress failing tests is not a runtime check; enforce it with a hook or CI step

## Recent changes

- [2026-10-22] Added proved fuzz tests as an oracle: Anthropic and Theorem had Claude prove 239 OSS-Fuzz entry points crash-free on compiled RISC-V binaries.
- [2026-10-19] Added proof-carrying types (gdp-ts) as an oracle: authorization checks enforced by the TypeScript compiler and a lint preset rather than by review.
- [2026-10-19] Added OpenAI's COBOL-migration eval as a differential-test example: byte-for-byte output parity on hidden tests, all tests must pass.
- [2026-10-14] Added Lavaee's verification-pyramid guidance: acceptance contract first, oracles agents can't game, test-diff-first review, multi-judge mean-plus-veto scoring, and scenario-driven browser and performance checks.
- [2026-09-22] Added model-checked specifications (TLA+/Lean) as an oracle: Opus 5.5 modeled the Claude Agent SDK and its counterexamples became 16 bug- and race-fix PRs.
- [2026-10-20] Page created, split out of [Evals for agentic software development](evals-for-agentic-software-development.md).

## Related

- [Evals for agentic software development](evals-for-agentic-software-development.md) — the full eval stack these checks feed
- [AI PR and code review](../workflows/ai-pr-code-review.md) — fresh-session review
- [gdp-ts](../tools/gdp-ts.md) — proof-carrying types for TypeScript
- [MultiLangBench](../benchmarks/multilangbench.md) — OpenAI's multi-language build benchmark and COBOL-migration eval
- [AI formal verification](../trends/ai-formal-verification.md) — proofs over real code, beyond tests

## Sources

- [Agents Write the Code. Your System Has to Prove It. — Alex Lavaee](../sources/tweets/lavaee-verification-pyramid-2026-10.md)
- [rauchg/gdp-ts — Ghosts of Departed Proofs for TypeScript (GitHub)](../sources/repos/rauchg-gdp-ts-2026-10.md)
- [Boris Cherny — formally verifying the Claude Agent SDK with Lean and Opus 5.5](../sources/tweets/bcherny-formal-verification-agent-sdk-2026-09-22.md)
- [OpenAI — Advancing coding in low-resource programming languages](../sources/articles/openai-low-resource-programming-languages-2026-10-19.md)
- [Anthropic — LLMs are making formal software verification feasible at a much larger scale](../sources/articles/anthropic-formal-verification-2026-10-22.md)
