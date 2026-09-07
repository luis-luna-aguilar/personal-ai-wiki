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
