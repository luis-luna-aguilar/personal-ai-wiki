---
title: AI formal verification
type: trend
domains: [cybersecurity, coding]
tags: [anthropic]
as_of: 2026-10-22
sources: [anthropic-formal-verification-2026-10-22, bcherny-formal-verification-agent-sdk-2026-09-22]
---

# AI formal verification

The trend: models are making formal verification of ordinary software affordable. Formal verification means turning code into mathematics and proving it always obeys a rule, rather than testing a sample of inputs. It used to cost far more than writing the code (seL4, a verified kernel, took two person-years to build and twenty to verify), so it was reserved for avionics-grade systems. Agents now write the proofs, and a proof checker, not a human reviewer, decides whether they hold. Proofs in pure mathematics are a separate track, on [AI math verification](ai-math-verification.md).

## Current signal (as of 2026-10-22)

- **Proved fuzz tests at OSS-Fuzz scale:** Anthropic and Theorem Labs had Claude turn existing fuzz tests into statements ("this entry point never crashes on any input up to 64 MB") and prove them over the compiled RISC-V binary. Over a few weeks it fixed the bugs it hit, then proved 239 entry points across 123 OSS-Fuzz libraries, about 180M lines of Rocq proof that only the checker reads. The attempt found bugs fuzzers rarely reach, such as a decompressor underflow on rare ~20 MB inputs.
- **The limits are stated up front:** "verified" is not "bug-free". The proofs cover single-threaded static RISC-V builds linked against musl, not the x86 or ARM machines with glibc most people run, and only what the fuzz test checks.
- **Getting cheaper per proof:** on 36 small verification tasks, [Claude Opus 5.5](../models/claude-opus-5-5.md) proves half with about 40% fewer tokens than Opus 5.
- **Non-specialists can use it:** Boris Cherny modelled the Claude Agent SDK in Lean and TLA+ with Opus 5.5 and got 16 bug- and race-fix PRs. Both techniques are written up as oracles on [Acceptance contracts and test oracles](../training/acceptance-contracts-and-test-oracles.md).
- **Proof certificates in tools:** [Open Ontologies](../tools/open-ontologies.md) has each reasoning run write a certificate that a separate, formally verified Lean 4 checker re-checks.

## Why it matters

Once proof is cheap, the question shifts from "did the tests pass?" to "is the statement right?". People review the specification and the machine model, the checker does the rest. That also makes proof a security tool: see [State of Cybersecurity](../state-of/cybersecurity.md).

## What to watch

- Proofs over x86 and ARM builds, and over multi-threaded code
- Whether Theorem's offer to run the pipeline for open-source projects gets uptake

## Related

- [AI math verification](ai-math-verification.md) — machine-checked proofs in mathematics (Fermat's Last Theorem in Lean)
- [Acceptance contracts and test oracles](../training/acceptance-contracts-and-test-oracles.md) — proved fuzz tests and model-checked specifications as oracles

## Recent changes

- [2026-10-22] Page created: Anthropic and Theorem formally verified 239 OSS-Fuzz entry points with Claude; existing formal-methods material on the wiki linked from here.

## Sources

- [Anthropic — LLMs are making formal software verification feasible at a much larger scale](../sources/articles/anthropic-formal-verification-2026-10-22.md)
- [Boris Cherny — formally verifying the Claude Agent SDK with Lean and Opus 5.5](../sources/tweets/bcherny-formal-verification-agent-sdk-2026-09-22.md)
