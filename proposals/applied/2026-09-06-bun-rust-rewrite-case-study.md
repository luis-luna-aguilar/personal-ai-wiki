---
type: proposal
source: raw/newsletters/2026-07-16-openais-new-model-for-cyber-attacks.md
status: pending
created: 2026-09-06
---

# Proposal: Bun's 11-day Zig-to-Rust rewrite — an adversarial-review case study

## Summary

### The source

A multi-story AI newsletter dated 16 July carried a segment on Jarred Sumner, the creator of Bun and now an Anthropic engineer, who went viral back in May for porting Bun's entire runtime from Zig to Rust in just 11 days using a pre-release build of Claude Fable 5. This week he published the full account on Bun's own blog, and that post is rich enough to pull directly rather than rely on the newsletter's summary. The "why": Bun mixes Zig's manual memory management with JavaScriptCore's garbage collector, and that mismatch was the source of a long tail of use-after-free and memory-leak bugs. The "how" is the interesting part. One Claude session implemented each change; two more, in fresh context windows with no access to the implementer's reasoning, reviewed the diff alone and were told only to find reasons it might be wrong — with a standing rule that a workaround needing a paragraph-long comment to justify it is presumptively broken code. Two shared reference documents (a porting guide and a struct-lifetime table) kept every agent consistent across the effort. Sumner piloted the whole process on 3 of the codebase's 1,448 Zig files before scaling up, using Bun's own TypeScript test suite — bound to the public interface, so it survived the language swap — to grade the port from the outside. At peak, agents wrote about 1,300 lines of code per minute. Total cost: roughly $165,000 in tokens (5.9B uncached input, 690M output, 72B cached input reads), against Sumner's own estimate that three engineers would need about a year to do it by hand, freezing bugfixes and features the whole time.

### What changes

`training/ai-enablement-software-development.md` already name-drops this rewrite in one clause of its "Stack fungibility" bullet ("Bun merged 1M lines Zig→Rust in days"), sourced only from a secondhand mention with no real numbers behind it.

- **Training — AI enablement (software development)** corrects that clause with the real figures (535,496 lines of Zig, 11 days, ~$165,000 in tokens) and adds a new Evidence-from-practice entry describing the one-implementer/two-adversarial-reviewer methodology, the pilot-then-scale approach, and the throughput/cost numbers. Recent changes gains one new entry dated 16 July; the page's date moves to 16 July.
- Two new source pages: one for the newsletter (its Bun segment only — the same email covers unrelated stories other proposals draw from) and one for Sumner's own "Rewriting Bun in Rust" post.

### What to weigh

Sumner works at Anthropic (which acquired Bun in December 2025) and used a pre-release Claude model for the work — a first-party account, not an independent one, though his post discloses this itself. The blog post doesn't carry an explicit publish date, so both new source pages use the newsletter's 16 July date as the best available anchor.

## Intended changes

- [x] **Approve all** — checking this box approves every item in `## Intended changes` and `## Schema / vocabulary additions` below; the individual boxes may stay empty.

- [ ] **Update** `wiki/training/ai-enablement-software-development.md` — correct the Bun clause in the Stack-fungibility bullet, add an Evidence-from-practice entry, one new Recent-changes entry, `as_of` moves to 2026-07-16, merge two new source ids
    > See draft below

- [ ] **Create** `wiki/sources/newsletters/openais-new-model-for-cyber-attacks-2026-07-16.md` — source summary (Bun segment only)

- [ ] **Create** `wiki/sources/articles/bun-rust-rewrite-2026-07-16.md` — source summary for Sumner's own blog post

## Page drafts

### wiki/training/ai-enablement-software-development.md (updated)

```md
---
title: AI enablement — software development
type: training
as_of: 2026-07-16
sources: [ramp-ai-adoption-playbook, shopify-latent-space-april-2026, lennysan-simonw-interview, agentic-cognitive-overhead, garrytan-gstack-repo, the-code-2026-04-23, qa-tooling-for-software-agents-deep-research, agent-review-artifacts-2026-05-13, agentic-coding-trap-may-2026, ai-stack-fungibility-hashimoto-2026-05, shopify-claude-code-bessemer-2026-05, stanford-labor-june-2026, github-kyle-daigle-june-2026, ainews-june-05-2026, software-factories-fde-2026-07, dashbench-code-review-understanding-2026-07, cognitioncom-blog-ai-productivity, openais-new-model-for-cyber-attacks-2026-07-16, bun-rust-rewrite-2026-07-16]
---

## Proven patterns

(unchanged except the "Stack fungibility" bullet, whose Bun clause becomes:)

- **Stack fungibility.** AI agents make language and framework choice reversible at scale not previously possible. Bun's creator rewrote its 535,496-line Zig codebase to Rust in 11 days using a pre-release Claude Fable 5, at a cost of about $165,000 in tokens — against his own estimate that three engineers would need roughly a year by hand; Cloudflare reproduced Next.js API in a week; Ladybird JS engine C++→Rust in 14 days; one team rewrote mobile apps in React Native with a planned revert path. Hashimoto: "Tech stack is no longer a decade-long commitment — now a quarterly project." Language/framework lock-in arguments weaken substantially; migration risk can be hedged cheaply.

## Evidence from practice

(add as a new bullet, placed after the Cognition/Devin entry:)

- Bun's Zig→Rust rewrite (Jarred Sumner, July 2026): a documented large-scale case study in adversarial-review-driven agentic refactoring. One Claude session implemented each change; two more, in fresh context windows with no visibility into the implementer's reasoning, reviewed the diff alone with the sole job of finding reasons it might fail — under a standing rule that a workaround needing a paragraph-long justifying comment is presumptively wrong. A shared porting guide and struct-lifetime table kept agents consistent across the 1,448-file codebase, which Sumner piloted on just 3 files before scaling up; Bun's own TypeScript test suite, unaffected by the underlying language, graded the port from the outside. Peak throughput ~1,300 lines/minute; total cost ~$165,000 in tokens.

## Recent changes

(insert as the new first entry, newest-first; page is at 9/10 entries so nothing spills yet:)

- [2026-07-16] Corrected the Bun Zig→Rust rewrite figures in the Stack-fungibility bullet (535,496 lines, 11 days, ~$165K in tokens) and added a full case study of its one-implementer/two-adversarial-reviewer methodology.
- [2026-07-14] Added Cognition's production session-productivity estimator (`r_log = 0.74`) as evidence that hours/dollar-denominated AI engineering ROI measurement is moving from research into deployed practice.
(...remaining existing entries unchanged...)

## Sources

(append two new lines:)

- [OpenAI's new model for cyber attacks (newsletter digest)](../sources/newsletters/openais-new-model-for-cyber-attacks-2026-07-16.md)
- [Rewriting Bun in Rust](../sources/articles/bun-rust-rewrite-2026-07-16.md)
```

### wiki/sources/newsletters/openais-new-model-for-cyber-attacks-2026-07-16.md (new)

```md
---
title: OpenAI's new model for cyber attacks (newsletter digest)
type: source
source_type: newsletter
source_file: raw/newsletters/2026-07-16-openais-new-model-for-cyber-attacks.md
published: 2026-07-16
ingested: 2026-09-06
domains: [coding]
---

# OpenAI's new model for cyber attacks (newsletter digest)

A multi-story AI newsletter dated 2026-07-16. This source page currently records only its Bun Zig-to-Rust rewrite segment; other segments (GPT-Red, the Grok Build open-sourcing) are recorded on separate proposals against this same raw file.

## Influenced pages

- [Training — AI enablement (software development)](../../training/ai-enablement-software-development.md) — corrected Bun rewrite figures, new adversarial-review case-study entry

## Key claims extracted

- Bun creator Jarred Sumner (Anthropic MTS) ported Bun from Zig to Rust in 11 days using a pre-release Claude Fable 5
- Full methodology write-up published on Sumner's own blog, linked from this newsletter
```

### wiki/sources/articles/bun-rust-rewrite-2026-07-16.md (new)

```md
---
title: Rewriting Bun in Rust
type: source
source_type: article
source_file: raw/articles/2026-09-06-buncom-blog-bun-in-rust.md
url: https://bun.com/blog/bun-in-rust
published: 2026-07-16
ingested: 2026-09-06
domains: [coding]
---

# Rewriting Bun in Rust

Jarred Sumner's own account of rewriting Bun's 535,496-line Zig codebase to Rust in 11 days using a pre-release Claude Fable 5, published on Bun's blog. Discloses that Bun was acquired by Anthropic in December 2025 and that Sumner works there.

## Influenced pages

- [Training — AI enablement (software development)](../../training/ai-enablement-software-development.md) — full case study: adversarial-review methodology, pilot-then-scale approach, cost/throughput figures

## Key claims extracted

- 535,496 lines of Zig (excluding comments) rewritten to Rust in 11 days
- Methodology: 1 implementer + 2 adversarial-reviewer Claude sessions (fresh context, diff-only, no access to the implementer's reasoning) per change; standing rule that a workaround needing a paragraph-long justifying comment is presumed wrong
- Piloted on 3 of 1,448 `.zig` files before scaling to the full codebase; a shared `PORTING.md` and `LIFETIMES.tsv` kept agent sessions consistent
- Peak throughput ~1,300 lines of code/minute; total cost ~$165,000 in tokens (5.9B uncached input tokens, 690M output tokens, 72B cached input token reads)
- Sumner's estimate: a manual rewrite would take 3 engineers about a year, freezing bugfixes, security fixes, and feature work for that period
```

## Open questions

- Please add a section somewhere about how the two adversarial-review process works.
