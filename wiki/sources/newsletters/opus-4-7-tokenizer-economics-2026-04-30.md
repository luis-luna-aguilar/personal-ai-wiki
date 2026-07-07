---
title: Opus 4.7 tokenizer economics
type: source
source_type: newsletter
source_file: raw/newsletters/2026-04-30-cursor-sdk-is-here.md
published: 2026-04-30
ingested: 2026-05-05
domains: [models, coding]
---

# Opus 4.7 tokenizer economics

The Code summarizes analysis from OpenRouter and Simon Willison claiming that Claude Opus 4.7's new tokenizer maps some prompts — especially code-heavy or symbol-dense inputs — into more tokens than Opus 4.6 did for the same content. This raises real agent-loop costs despite unchanged per-token sticker pricing.

## Key claims extracted

- Opus 4.7's tokenizer is reported to produce more tokens per character than Opus 4.6 for certain input types, particularly code and structured text
- The practical effect: same-sized codebases cost more to process with Opus 4.7 than with 4.6, even at identical per-token rates
- OpenRouter data and Simon Willison's analysis are the primary sources cited
- Agent loop impact: longer-running agents that process many files see the cost difference multiply across many context windows

## Caveats

- Newsletter synthesis; Anthropic has not published a formal tokenizer comparison
- Exact multiplier claims (e.g., "X% more tokens") should not be applied without finding the original OpenRouter or Willison analysis
- Cost impact is workload-dependent; short, natural-language-heavy tasks may not show the same effect

## Influenced pages

- `wiki/history/models/claude-opus-4-7.md` — tokenizer cost caveat
- `wiki/training/evals-for-agentic-software-development.md` — tokenizer and cache as cost variables
