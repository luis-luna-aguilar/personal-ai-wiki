---
title: 'Cloudflare — Introducing Clef: open-source decision models and RL fine-tuning'
type: source
source_type: article
source_file: raw/articles/2026-10-02-cloudflare-clef-decision-models.md
url: https://blog.cloudflare.com/clef-decision-models/
published: 2026-10-02
ingested: 2026-10-20
domains: [models]
---

# Cloudflare — Introducing Clef: open-source decision models and RL fine-tuning

Cloudflare's launch post for Clef and Clef-flash: Apache 2.0 decision models hosted on Workers AI, API-compatible with Jev. It also announces an RL fine-tuning service, first run by Cloudflare's forward-deployed engineers and later offered as a self-serve product.

## Influenced pages
- [Decision models](../../concepts/decision-models.md) — architecture, Clef entry
- [Jev](../../models/jev.md) — 32K context, latency, benchmark rows
- [State of Models](../../state-of/models.md) — Clef line

## Key claims extracted
- Clef freezes Qwen3.8-27B (Clef-flash: Qwen3.5-9B); one prefill pass, then a schema head scores valid options in parallel; LoRA rank 256, label-smoothed cross-entropy plus Brier loss, and Cloudflare's own RLCD stage
- Image input and 64K context (Jev: text only, 32K)
- Cloudflare's 10-benchmark table: Clef or Clef-flash top 7 rows; Jev tops When2Call (80.97) and BRIGHT (47.52)
- Median latency: Clef 209 ms, Clef-flash 39 ms, Jev 524 ms
- Threat-intelligence domain classification took 2.2 s with Clef vs 4.7 s with gpt-oss-120b
