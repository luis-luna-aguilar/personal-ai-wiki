---
title: 'Arena — HarnessTax: How much does the harness matter for coding agents?'
type: source
source_type: article
source_file: raw/articles/2026-11-24-arenaai-blog-coding-agents-harness-tax.md
url: https://arena.ai/blog/coding-agents-harness-tax
published: 2026-09-16
ingested: 2026-11-24
domains: [agents, coding]
---

# Arena — HarnessTax

Melissa Pan and co-authors (including Ion Stoica and Matei Zaharia), with Arena, ran 21 model–harness pairs: seven models in Claude Code, Codex CLI and Pi. Each pair did the same 30 sampled tasks from SWE-bench Lite and Terminal-Bench 2.0, three attempts each, at the harness's high effort setting and capped at 100 turns, with costs from one fixed price list. The "harness tax" is paying more for the same quality because of the default harness. The authors say the two open benchmarks may have been seen in training, and results may differ elsewhere.

## Influenced pages
- [Harness-model co-evolution](../../concepts/harness-model-co-evolution.md) — HarnessTax paragraph in the dissent section

## Key claims extracted
- Harness choice moved success within about ±2% on SWE-bench Lite and about ±5% on Terminal-Bench 2.0; the same model could cost up to 5x more
- Across shared models, Claude Code cost about 2.0x Pi and 1.6x Codex on SWE-bench Lite, and 1.5x Pi on Terminal-Bench 2.0 (geometric means)
- Fable 5: 97.8% in Claude Code, 96.7% in Codex and Pi; Claude Code about twice Pi's cost at similar turn counts (15.3 vs 15.4)
- Claude Code's mean initial context is over 10x Pi's
- Pi (read, write, edit, bash) reaches the Pareto frontier on both benchmarks
- An alternative harness gave the highest success in 9 of 12 Anthropic/OpenAI model–benchmark comparisons (e.g. GPT-5.6 Sol 83.3% in Pi vs 78.9% in Codex on Terminal-Bench, at about half the cost)
