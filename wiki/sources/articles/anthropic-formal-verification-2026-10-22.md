---
title: Anthropic — LLMs are making formal software verification feasible at a much larger scale
type: source
source_type: article
source_file: raw/articles/2026-11-23-anthropiccom-research-formal-verification.md
url: https://www.anthropic.com/research/formal-verification
published: 2026-10-22
ingested: 2026-11-24
domains: [cybersecurity, coding]
---

# Anthropic — LLMs are making formal software verification feasible at a much larger scale

Anthropic's Frontier Red Team, with Theorem Labs, shows Claude producing formal proofs at scale. It converted OSS-Fuzz fuzz tests into specifications over compiled RISC-V binaries and proved them, patching the bugs it found along the way. Anthropic calls it the first large-scale effort to apply AI-driven formal verification to production software at the assembly level, and expects verification to become as practical as fuzzing. Theorem offers to run the pipeline for other open-source projects and publishes a Claude skill to get started.

## Influenced pages
- [AI formal verification](../../trends/ai-formal-verification.md) — new trend page built around this result
- [State of Cybersecurity](../../state-of/cybersecurity.md) — one-line formal-verification pointer under AI-assisted vulnerability detection
- [Acceptance contracts and test oracles](../../training/acceptance-contracts-and-test-oracles.md) — "proved fuzz tests" oracle
- [Claude Opus 5.5](../../models/claude-opus-5-5.md) — verification token-cost data point

## Key claims extracted
- In a few weeks, Claude patched found bugs and proved no crash on any input up to 64 MB for 239 entry points across 123 OSS-Fuzz libraries; ~180M lines of Rocq, ~600K lines per typical proof, median binary 18,000 RISC-V instructions
- Trusted base: the RISC-V and Linux-process models, the theorem statements, and the Rocq checker; a subset of proofs and the semantics are published
- Bugs found include a decompressor counter underflow on rare ~20 MB inputs, an image-decoder out-of-bounds read needing a 64 MB input and 2 GB+ of memory, a rediscovered libexpat CVE, and a file-restriction feature that was not always enforced
- Claude proved the Linux kernel's zlib (x86 binary) implements a spec it wrote from RFC 1950; a Verus-verified Python interpreter in Rust matched CPython on 99.95% of 1.7M random programs; one PDF-reader verification attempt found as many security bugs in a week as are typically reported in a year
- Opus 5.5 proves half of 36 small verification tasks with ~40% fewer tokens than Opus 5; a shared proof workspace cut tokens 17%
- Limits: "verified" is not "bug-free"; proofs cover single-threaded static musl RISC-V builds, not x86/ARM with glibc; ASan misses some memory bugs; not all entry points or callers are covered
