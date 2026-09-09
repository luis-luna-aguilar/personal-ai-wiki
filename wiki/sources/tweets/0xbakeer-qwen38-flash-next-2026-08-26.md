---
title: "0xBakeer on X: \"the 51B nobody talks about\" — Qwen3.8-Flash-Next architecture explainer"
type: source
source_type: tweet
source_file: raw/tweets/2026-09-07-0xbakeer-2092644019830431817.md
url: https://x.com/0xbakeer/status/2092644019830431817?s=12
published: 2026-08-26
ingested: 2026-09-08
domains: [models]
---

# 0xBakeer — Qwen3.8-Flash-Next's 51B n-gram embedding table

Independent practitioner thread explaining Qwen3.8-Flash-Next's second embedding table (n-gram lookup, 51B of 180B total params) and a practical DGX Spark serving recipe that went from 22 to 97 tok/s over several days.

## Influenced pages

- [Open-weight momentum broadens](../../trends/open-weight-momentum-broadens.md) — Qwen3.8-Flash-Next architecture bullet

## Key claims extracted

- Qwen3.8-Flash-Next: 180B total params, 6B active, plus a 51B n-gram embedding lookup table
- The lookup table is never multiplied against anything — pure memorization, not computation — so it can be memory-mapped off NVMe/SSD instead of held in RAM
- This is what lets the 180B model fit on a 128GB unified-memory machine at Q4
- Serving recipe on a single DGX Spark improved from 22 tok/s to 97 tok/s (llama.cpp, then vLLM + NVFP4 + the model's own MTP draft head)
