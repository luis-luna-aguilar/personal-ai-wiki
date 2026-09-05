---
title: Introducing Command A+ | Cohere
type: source
source_type: article
source_file: raw/articles/2026-08-25-coherecom-blog-command-a-plus.md
url: https://cohere.com/blog/command-a-plus
published: 2026-05-21
ingested: 2026-08-25
domains: [models]
---

# Introducing Command A+ | Cohere

Cohere's own announcement of Command A+, its first fully open (Apache 2.0) model, unifying the Command A family (base, Reasoning, Vision, Translate) into one 218B/25B-active MoE model for enterprise agentic workflows, born from a year of deploying North (Cohere's agentic enterprise workspace). The raw capture (fetched 2026-08-25) carries no explicit publication date; `published` is taken from AINews' same-day coverage of the launch on 2026-05-21.

## Influenced pages

- [Cohere Command A+](../../models/cohere-command-a-plus.md) — new page
- [State of Models](../../state-of/models.md) — new Open-weight models entry
- [Open-weight momentum broadens](../../trends/open-weight-momentum-broadens.md) — new bullet on fully-open releases broadening beyond the usual labs

## Key claims extracted

- 218B total / 25B active MoE; Apache 2.0 license; 128K input context, 64K max generation; text/image/tool-use input; 48 languages
- Runs on 1x NVIDIA Blackwell GPU or 2x H100s at W4A4; BF16/FP8/W4A4 quantizations on Hugging Face; vLLM/Transformers support
- AA Intelligence Index score of 37, "outperforming other leading open models" per Cohere's framing of that specific benchmark
- Gains over Command A Reasoning: 𝜏²-Bench Telecom 37%→85%, Terminal-Bench Hard 3%→25%, MMMU 75.1%, MathVista 80.6%, CharXiv 52.7%
- Up to 63% higher output tokens/sec and 17% lower time-to-first-token vs Command A Reasoning at same quantization/concurrency; W4A4 adds another 47% speed / 13% latency improvement
- New tokenizer: ~20% fewer tokens for Arabic, ~16% Korean, ~18% Japanese vs predecessor
