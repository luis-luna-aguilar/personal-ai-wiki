---
title: Qwen 3.6 35B A3B community benchmarks — May 2026 local-tier comparison
type: source
source_type: newsletter
source_file: raw/newsletters/2026-05-13-ainews-the-end-of-finetuning.md
published: 2026-05-13
ingested: 2026-05-13
domains: [models, coding]
---

# Qwen 3.6 35B A3B community benchmarks — May 2026 local-tier comparison

AINews newsletter (May 13) includes a summary of r/LocalLLaMA community benchmarks for the ~20GB local model tier. Primary source: https://www.reddit.com/r/LocalLLaMA/ (week of May 13, 2026).

## Influenced pages

- [Qwen 3.6 35B-A3B](../../models/qwen-3-6-35b-a3b.md) — community benchmark data added

## Key claims extracted

- Task: paper-to-code comprehension and long-context evaluation
- Models compared: Qwen 3.6 35B A3B, Qwen 3.6 27B, Gemma 4 26B A4B, Nvidia Nemotron 3 Nano
- Winner: Qwen 3.6 35B A3B judged strongest overall across the tested tasks
- Baseline improvement: all four models substantially outperform Devstral Small 2
- Practical size: Qwen 3.6 35B A3B ~20GB at q4; Gemma 4 26B ~15GB (faster for chat)
- Multi-model setup: users running Qwen 35B and Gemma 26B simultaneously on one machine
- Caveat: Qwen 35B thinking mode can be verbose and slow; performance sensitive to temperature and quantization settings
- Source: community evaluations from r/LocalLLaMA, not a formal benchmark study
