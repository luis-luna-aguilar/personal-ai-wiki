---
title: "AINews — Claude Fable/Mythos 5.1: new SOTA model"
type: source
source_type: newsletter
source_file: raw/newsletters/2026-09-02-ainews-claude-fablemythos-51-new-sota-model.md
url: https://www.latent.space/p/ainews-claude-fablemythos-51-new
published: 2026-09-02
ingested: 2026-09-09
domains: [models, agents]
---

# AINews — Claude Fable/Mythos 5.1: new SOTA model

AINews' AI Twitter recap deep-dive on Anthropic's Fable 5.1/Mythos 5.1 launch: benchmarks, pricing, the same-weights/different-safety-routing debate, Enterprise Frontier Safeguards false positives, and the "less Claudese" stylistic shift — plus same-day coverage of OpenAI's Astra preparedness/architecture debate, Qwen3.8-Max-0902's #1 WebDev result, and World Labs' Atlas world model.

## Influenced pages

- [Claude Fable 5.1 / Mythos 5.1](../../models/claude-fable-5-1.md) — primary launch coverage
- [State of Models](../../state-of/models.md) — leader-line update
- [Qwen 3.8](../../models/qwen-3-8.md) — Qwen3.8-Max-0902 #1 WebDev result
- [Open-weight momentum broadens](../../trends/open-weight-momentum-broadens.md) — Qwen3.8-Max-0902 data point
- [AGI timeline claims](../../trends/agi-timeline-claims.md) — Astra "Critical" cyber-capability preparedness milestone
- [Agent safety and alignment research](../../trends/agent-safety-and-alignment-research.md) — Astra recurrent-depth/CoT-monitorability debate

## Key claims extracted

- Fable 5.1 pricing: $10/$50/$12.5 per MTok input/output/cache-write (unchanged), cache-read cut 75% to $0.25/MTok
- Artificial Analysis Intelligence Index 66 (Opus 5: 63, Fable 5: 62, GPT-5.6 Sol: 61); HLE 65% with tools; Terminal-Bench v2.1 91.4%
- Output tokens ~1.7x Fable 5's, so per-task cost ~20% higher despite cache cut ($3.76/task at max effort)
- Community claim (@eliebakouch): Fable and Mythos 5.1 are the same weights, differing by safety-classifier threshold; ~4% of output tokens fall back to Opus 4.8 per Artificial Analysis
- OpenAI's Astra hit the "Critical" cyber-capability threshold under OpenAI's Preparedness Framework; reporting describes a recurrent-depth/"looped transformer" architecture, disputed by OpenAI chief scientist @merettm (~2x GPT-4 computation-graph depth, CoT monitoring still a research priority)
- Alibaba's Qwen3.8-Max-0902 (2.4T params, 1M context, $2/$6 per MTok) debuted #1 on Arena's Code Arena: WebDev (1691), ahead of Claude Opus 5 Max and Kimi K3 Max
