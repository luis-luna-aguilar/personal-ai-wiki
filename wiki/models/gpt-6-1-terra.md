---
title: GPT-6.1 Terra
type: model
domains: [models]
subcategory: small-model
tags: [openai, closed-source]
as_of: 2026-10-29
sources: [bleepingcomputer-gpt-6-1-terra-2026-10-26, every-gpt-6-1-terra-skip-2026-10-29, openai-introducing-gpt-6-2-astra-sol, openai-background-mode-docs-2026-11]
---

# GPT-6.1 Terra

OpenAI's fast, low-cost tier, launched 2026-10-26 and pitched for computer use, visual reasoning and everyday writing: forms, technical drawings, video edits and proposal drafts. It sits between [GPT-6.2 Sol](gpt-6-2-sol.md) and [GPT-6 Luna](gpt-6-luna.md). The GPT-6.2 release refreshed only Astra and Sol, so Terra remains current.

## Current status (as of 2026-10-29)

- **Price:** $1/$5 per 1M input/output tokens, half GPT-5.6 Terra's price. Discounted background windows apply ([OpenAI discounted async processing](../workflows/async-discounted-processing.md)).
- **Availability:** Plus, Pro, Enterprise and Edu in ChatGPT Work and Codex; API as `gpt-6.1-terra`.
- **OpenAI's launch numbers:** [Terminal-Bench](../benchmarks/terminal-bench.md) 4.0 50.3% at max effort (GPT-5.6 Terra 21.5%); [Agents' Last Exam](../benchmarks/agents-last-exam.md) +15 points over GPT-5.6 Terra at medium effort for about a third of the cost; internal factual-error rate 16.7% at low effort (GPT-5.6 Terra 53.6%) and 4.3% at max. OpenAI says it is more than three times faster than its larger models and still recommends those for the hardest coding.
- **Every's read (2026-10-29): skip.** Too little writing gain to justify a Vibe Check; first drafts full of AI tells, but it revised well from notes, so a capable iterative writer that needs steering.

## Weaknesses / caveats

- OpenAI's comparisons at launch were against [GPT-6 Astra](../history/models/gpt-6-astra.md) and [GPT-6.1 Sol](../history/models/gpt-6-1-sol.md), both since replaced; no comparison with the 6.2 models is captured.
- Computer use is the pitch, but the only outside report is unclear: Every's newsletter says it is fast at simple tasks (installing Chrome) and fails complex ones (setting up that article in Every's CMS), then says no one at Every had tested its computer use yet.

## Recent changes

- [2026-10-29] Every skips a Vibe Check: small writing gain, needs human steering.
- [2026-10-26] Launched at $1/$5 for computer use, visual reasoning and writing; 50.3% Terminal-Bench 4.0 per OpenAI.

## Sources

- [BleepingComputer — OpenAI launches GPT-6.1 Terra](../sources/articles/bleepingcomputer-gpt-6-1-terra-2026-10-26.md)
- [Every — Skip: GPT-6.1 Terra (Context Window, 2026-10-29)](../sources/newsletters/every-gpt-6-1-terra-skip-2026-10-29.md)
- [OpenAI — Introducing GPT-6.2 Astra and Sol](../sources/articles/openai-introducing-gpt-6-2-astra-sol.md)
- [OpenAI API docs — Background mode](../sources/articles/openai-background-mode-docs-2026-11.md)
