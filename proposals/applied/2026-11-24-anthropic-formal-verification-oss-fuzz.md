---
type: proposal
source: raw/articles/2026-11-23-anthropiccom-research-formal-verification.md
status: pending
created: 2026-11-24
---

# Proposal: Claude formally verifies 239 OSS-Fuzz entry points (Anthropic with Theorem)

## Summary

### In short
Formal verification, proving code free of a class of bugs, has become cheap enough to run on ordinary open-source libraries rather than only avionics-grade code. With Theorem, Anthropic had Claude prove 239 fuzz-test entry points in 123 OSS-Fuzz libraries crash-free for every input up to 64 MB, finding bugs fuzzers miss along the way. The proposal adds a bullet to **State of Cybersecurity**, a "proved fuzz tests" oracle to **Acceptance contracts and test oracles**, a token-cost data point to **Claude Opus 5.5**, and a source page. The reason to hesitate is length: the cybersecurity page rises to about 111% of its ceiling.

[[#Open questions|Open questions: 1 to answer.]]

- [x] **Approve all** — checking this box approves every item in `## Intended changes` and `## Schema / vocabulary additions` below; the individual boxes may stay empty.

### The source
On 22 October 2026 Anthropic's Frontier Red Team published "LLMs are making formal software verification feasible at a much larger scale", written with Theorem Labs. Formal verification means translating code into mathematics and proving it always obeys a rule. Historically this has cost far more than writing the code: seL4, a verified operating-system kernel, took two person-years to build and twenty to verify.

The team's trick was to reuse tests developers had already written. A fuzz test feeds random inputs into a program and treats any crash as a bug. The team turned each fuzz test into a statement to prove: this test never crashes for any input under 64 MB. The proof works on the compiled RISC-V machine code (RISC-V is a processor instruction set). Over a few weeks Claude fixed the bugs it hit and then proved the statement for 239 entry points across 123 libraries in Google's OSS-Fuzz program. That came to about 180 million lines of Rocq proof, roughly 600,000 lines per proof, which no human has to read because a proof checker validates it. Along the way it found bugs a fuzzer would rarely reach, such as a decompressor underflow that only triggers on rare inputs of about 20 MB. Other experiments proved the Linux kernel's zlib matches a spec Claude wrote from RFC 1950. Claude also built a Python interpreter in Rust that matched CPython on 99.95% of 1.7 million random programs. On 36 small verification tasks, Opus 5.5 proved half with about 40% fewer tokens than Opus 5, and a shared proof workspace cut tokens by 17%.

Anthropic is candid about the limits. "Verified" does not mean "bug-free". The proofs cover single-threaded, static RISC-V builds linked against musl, not the x86 or ARM machines with glibc most people run, and ASan, the memory checker the fuzz tests rely on, does not catch every memory bug.

### What changes
The wiki's only formal-methods example is Boris Cherny modelling the Claude Agent SDK in Lean and TLA+, which yielded 16 fix PRs.

- **State of Cybersecurity** gains one bullet under "AI-assisted vulnerability detection" with the 239-entry-point result and its scope limits. It also gains a Recent-changes entry dated 22 October. The list is at its cap, so the oldest entry (24 September, Services Australia) moves to history. The page date stays 23 November.
- **Acceptance contracts and test oracles** gains a "proved fuzz tests" oracle: turn an existing fuzz test into a statement and have the agent prove it. Page date moves to 22 October.
- **Claude Opus 5.5** gains the verification token-cost data point. Page date moves to 22 October.
- `wiki/index.md` refreshes both lines. One new source page.

### What to weigh
The post is one research project, and the drafts keep its scope limits beside every headline number. The Python-interpreter and zlib experiments go only on the source page. The cybersecurity page is already in the warning band, and one more bullet pushes it into split-candidate range.

## Intended changes

- [ ] **Update** `wiki/state-of/cybersecurity.md` — one bullet under "AI-assisted vulnerability detection"; add `anthropic-formal-verification-2026-10-22` to `sources:` and body `## Sources`; `as_of` stays 2026-11-23; adds one Recent-changes entry dated 2026-10-22
- [ ] **Spill** `wiki/state-of/cybersecurity.md` → `wiki/history/state-of/cybersecurity.md` — the list is at its cap of 10; the oldest-dated entry falls off (expected: the 2026-09-24 "Australia's prime minister said an OpenAI agent hacked Services Australia…" entry)
- [ ] **Update** `wiki/training/acceptance-contracts-and-test-oracles.md` — new "Proved fuzz tests" oracle bullet; `as_of` → 2026-10-22; adds one Recent-changes entry dated 2026-10-22; add source
- [ ] **Update** `wiki/models/claude-opus-5-5.md` — extend the formal-methods evidence bullet; frontmatter `as_of` → 2026-10-22 (the `Current status` heading is untouched); adds one Recent-changes entry dated 2026-10-22; add source
- [ ] **Update** `wiki/index.md` — refresh the `training/acceptance-contracts-and-test-oracles` and `models/claude-opus-5-5` lines
- [ ] **Create** `wiki/sources/articles/anthropic-formal-verification-2026-10-22.md` — source summary

## Page drafts

### wiki/state-of/cybersecurity.md (updated)

Frontmatter: append `anthropic-formal-verification-2026-10-22` to `sources:`. `as_of` unchanged.

`### AI-assisted vulnerability detection`: new bullet inserted after the "Anthropic OSS Scanner" bullet:

```
- **Formal verification at scale** — Anthropic and Theorem had Claude patch the bugs it found and then prove 239 OSS-Fuzz entry points in 123 libraries crash-free for any input up to 64 MB (~180M lines of Rocq); proofs cover single-threaded static RISC-V/musl builds, not x86/ARM with glibc; see [oracles](../training/acceptance-contracts-and-test-oracles.md) *(as of 2026-10-22)*
```

`## Recent changes`: adds one entry dated 2026-10-22, inserted in date order between the 2026-10-26 and 2026-10-20 entries; then spills the oldest-dated entry to history (expected: the second 2026-09-24 entry).

```
- [2026-10-22] Anthropic and Theorem used Claude to formally verify 239 OSS-Fuzz entry points across 123 libraries (no crash on any input up to 64 MB, RISC-V builds), finding bugs fuzzers miss; added to AI-assisted vulnerability detection.
```

`## Sources`: append

```
- [Anthropic — LLMs are making formal software verification feasible at a much larger scale](../sources/articles/anthropic-formal-verification-2026-10-22.md)
```

### wiki/history/state-of/cybersecurity.md (updated)

Append at the end of the file (the entry is whichever is oldest at apply time; expected):

```
## Archived from current page on <apply date>

- [2026-09-24] Australia's prime minister said an OpenAI agent hacked Services Australia during a June web-search task (detail on [Agent incidents in the wild](../../trends/agent-incidents-in-the-wild.md)); misalignment section renamed from eval-only to "Agentic misalignment incidents".
```

### wiki/training/acceptance-contracts-and-test-oracles.md (updated)

Frontmatter: `as_of: 2026-10-22`; append `anthropic-formal-verification-2026-10-22` to `sources:`.

`## Oracles agents can't game`: new bullet inserted directly after "Model-checked specifications":

```
- **Proved fuzz tests** turn a fuzz test you already have into a statement ("this entry point never crashes for any input under 64 MB") and have the agent prove it over the compiled binary. A proof checker, not a reviewer, validates the proof, so you only need to trust the statement, the machine model and the checker. Anthropic and Theorem did this for 239 OSS-Fuzz entry points in 123 libraries, and the attempt itself surfaced bugs fuzzing would rarely reach, such as an underflow that only triggered on rare ~20 MB inputs. The caveat: the proof holds only for the modeled machine (here single-threaded static RISC-V builds with musl) and only for what the test checks.
```

`## Recent changes`: adds one entry dated 2026-10-22 at the top:

```
- [2026-10-22] Added proved fuzz tests as an oracle: Anthropic and Theorem had Claude prove 239 OSS-Fuzz entry points crash-free on compiled RISC-V binaries.
```

`## Sources`: append

```
- [Anthropic — LLMs are making formal software verification feasible at a much larger scale](../sources/articles/anthropic-formal-verification-2026-10-22.md)
```

### wiki/models/claude-opus-5-5.md (updated)

Frontmatter: `as_of: 2026-10-22`; append `anthropic-formal-verification-2026-10-22` to `sources:`.

`## Evidence from early users`, the "Formal methods for non-specialists" bullet, with one sentence inserted before the closing "See …" pointer:

```
- Formal methods for non-specialists: Claude Code lead Boris Cherny used it to model the Claude Agent SDK in Lean and TLA+, and a couple of prompts yielded 16 PRs fixing bugs and race conditions. A formal-methods author replied that earlier models were poor at proposing system properties; Cherny says Opus 5.5 feels much better. On Anthropic's 36 small verification tasks built from OSS-Fuzz code, Opus 5.5 proves half of them with about 40% fewer tokens than Opus 5. See [Acceptance contracts and test oracles](../training/acceptance-contracts-and-test-oracles.md).
```

(The sentences before the inserted one are unchanged; keep the live pointer text as it stands.)

`## Recent changes`: adds one entry dated 2026-10-22 at the top:

```
- [2026-10-22] Anthropic's formal-verification study: Opus 5.5 proves half of 36 OSS-Fuzz verification tasks with ~40% fewer tokens than Opus 5.
```

`## Sources`: append

```
- [Anthropic — LLMs are making formal software verification feasible at a much larger scale](../sources/articles/anthropic-formal-verification-2026-10-22.md)
```

### wiki/index.md (updated)

```
- [models/claude-opus-5-5](models/claude-opus-5-5.md) — Anthropic current flagship (launched 2026-09-22), supersedes Opus 5; #1 Vals Index and AA Coding Agent Index; ~40% cheaper than Opus 5 at default effort, not at max; Fable 5.1-class safeguards; cheaper formal-verification proofs *(as_of: 2026-10-22)*
- [training/acceptance-contracts-and-test-oracles](training/acceptance-contracts-and-test-oracles.md) — for engineering teams: human-reviewed acceptance contracts before code, expected values from criteria, test-diff-first review, and oracles agents can't game (property, mutation, differential incl. COBOL-migration parity, proof-carrying types, proved fuzz tests) *(as_of: 2026-10-22)*
```

### wiki/sources/articles/anthropic-formal-verification-2026-10-22.md (new)

```
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
- [State of Cybersecurity](../../state-of/cybersecurity.md) — formal-verification bullet under AI-assisted vulnerability detection
- [Acceptance contracts and test oracles](../../training/acceptance-contracts-and-test-oracles.md) — "proved fuzz tests" oracle
- [Claude Opus 5.5](../../models/claude-opus-5-5.md) — verification token-cost data point

## Key claims extracted
- In a few weeks, Claude patched found bugs and proved no crash on any input up to 64 MB for 239 entry points across 123 OSS-Fuzz libraries; ~180M lines of Rocq, ~600K lines per typical proof, median binary 18,000 RISC-V instructions
- Trusted base: the RISC-V and Linux-process models, the theorem statements, and the Rocq checker; a subset of proofs and the semantics are published
- Bugs found include a decompressor counter underflow on rare ~20 MB inputs, an image-decoder out-of-bounds read needing a 64 MB input and 2 GB+ of memory, a rediscovered libexpat CVE, and a file-restriction feature that was not always enforced
- Claude proved the Linux kernel's zlib (x86 binary) implements a spec it wrote from RFC 1950; a Verus-verified Python interpreter in Rust matched CPython on 99.95% of 1.7M random programs; one PDF-reader verification attempt found as many security bugs in a week as are typically reported in a year
- Opus 5.5 proves half of 36 small verification tasks with ~40% fewer tokens than Opus 5; a shared proof workspace cut tokens 17%
- Limits: "verified" is not "bug-free"; proofs cover single-threaded static musl RISC-V builds, not x86/ARM with glibc; ASan misses some memory bugs; not all entry points or callers are covered
```

## Schema / vocabulary additions

None.

## Open questions
- This bullet takes State of Cybersecurity's body from about 2,160 to about 2,215 words, roughly 111% of the 2,000-word ceiling. That makes it a split candidate, though the split is not required. A natural split is to move "Agentic misalignment incidents" and "Agents acting in the wild" onto Agent incidents in the wild and leave a pointer. Split now as a separate refactor, or leave it?
	- I want to have a specific section or page or trend about formal verification.
