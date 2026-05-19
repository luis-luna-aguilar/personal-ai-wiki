---
title: Cursor Composer 2.5 — launch post
type: source
source_type: article
source_file: raw/articles/2026-05-18-cursorcom-blog-composer-2-5.md
url: https://cursor.com/blog/composer-2-5
published: 2026-05-18
ingested: 2026-05-18
domains: [coding]
---

# Cursor Composer 2.5 — launch post

Cursor's engineering post announcing Composer 2.5, the upgraded version of their in-house long-horizon coding model. Built on Kimi K2.5, trained with targeted RL using textual hints inserted at specific trajectory failure points plus KL distillation between a hinted teacher and an unhinted student. 25× more synthetic tasks than Composer 2, including a new "feature deletion" task type. Sharded Muon + dual mesh HSDP optimizer. Fast variant pricing: $3.00/M input · $15.00/M output. Next model: SpaceX training partnership on Colossus 2 (targeting million H100-equivalents).

## Influenced pages

- [Cursor](../../tools/cursor.md) — Composer 2 → 2.5 upgrade, training method, pricing, next model

## Key claims extracted

- Kimi K2.5 base (same as Composer 2)
- Targeted RL with textual feedback: hints inserted at problem trajectory points; KL distillation between hinted teacher and unhinted student
- 25× more synthetic tasks than Composer 2
- New "feature deletion" synthetic task type
- Sharded Muon + dual mesh HSDP optimizer; step time 0.2s on 1T model
- Standard pricing: $0.50/M input, $2.50/M output; fast variant: $3.00/M, $15.00/M
- SpaceX training partnership; next model on Colossus 2 (million H100-equivalents)
