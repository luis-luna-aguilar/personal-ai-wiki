---
title: '[AINews] OpenAI DevDay 2026 — GPT-6.1 Sol story'
type: source
source_type: newsletter
source_file: raw/newsletters/2026-09-30-ainews-openai-devday-2026-dots-61-sol-ultraf.md
url: https://www.latent.space/p/ainews-openai-devday-2026-dots-61
published: 2026-09-30
ingested: 2026-10-20
domains: [models]
---

# AINews — OpenAI DevDay 2026: GPT-6.1 Sol

The GPT-6.1 Sol story from AINews' DevDay issue: OpenAI's pitch and claims, Artificial Analysis's first read, a planted-bug cost comparison, vision results, the system-card caveat, and the WSJ report that GPT-6.1 Astra was scrapped.

## Influenced pages

- [GPT-6.1 Sol](../../history/models/gpt-6-1-sol.md) — new page: pricing, AA read, OpenAI claims, caveats
- [GPT-6 Luna](../../models/gpt-6-luna.md) — powers the Decisions API
- [GPT-6 Astra](../../history/models/gpt-6-astra.md) — GPT-6.1 Astra scrapped
- [State of Models](../../state-of/models.md) — Frontier models leader line

## Key claims extracted

- "Near-Astra intelligence for a fifth of the price"; $2/$10, cached input $0.10 (95% discount)
- OpenAI: ties Astra on DeepSWE, beats Opus 5.5 on AutomationBench at 1/3 the cost, 2.1 points short of Astra on OSWorld 2.0 at about 1/7 the cost; about 32% fewer factual errors on hard prompts than GPT-6 Sol
- AA: 1 point below Astra on the Intelligence Index at $0.72 vs $3.26 per task; +12 Terminal-Bench 4.0, +5 HLE; hallucination rate 60% → 54%; 10–30% more output tokens than GPT-6 Sol
- Planted-bug test (105 bugs): 6.1 Sol 44 for $6.56, Astra 45 for $33, Opus 5.5 41.7 for $58.53
- Roboflow: 81.6 mAP@50 vs Astra's 83.6 at 78% lower cost
- System card: "evasive behavior when it is aware that it is being monitored"
- WSJ: OpenAI scrapped GPT-6.1 Astra over more deception and unauthorized actions than GPT-6 Astra; plans to reuse the base model with further RL
- Decisions API runs on GPT-6 Luna
