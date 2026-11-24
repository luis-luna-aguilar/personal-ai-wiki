---
title: Vals AI — Vals Router Index
type: source
source_type: article
source_file: raw/articles/2026-11-24-valsai-benchmarks-vals_router_index.md
url: https://www.vals.ai/benchmarks/vals_router_index
published: 2026-11-03
ingested: 2026-11-24
domains: [agents, models]
---

# Vals AI — Vals Router Index

Vals AI's leaderboard comparing six commercial model routers, each at its default settings, with every single model on the Vals Index's eight agentic finance, coding, law and tax benchmarks (about 1,250 tasks). None of the routers sits on the cost-accuracy frontier. Date is the page's last-update stamp (3 November, when Nexus Auto with Sol was added); AINews first reported a five-router version on 2026-10-21.

## Influenced pages
- [Cost-aware routing: evidence from practice](../../training/cost-aware-routing-evidence.md) — new Router Index bullet

## Key claims extracted
- Routers: OpenRouter Auto Router, Fireworks Nexus Auto (Sol pool and Opus pool), Ramp Router, Jev Router (TypeSafe, via OpenRouter), Sakana Fugu Max
- Each router beaten on both score and cost by at least one single model
- Best router: Nexus Auto with Sol 60.0% at $1.25/task; DeepSeek V4.1 Flash 1017 alone 61.3% at $0.66
- Oracle routing within each router's budget: +8 (Ramp) to +27 (Jev Router) points
- Routers appear to run models at lower reasoning effort by default; coding suffers most
- Ramp Router gave the final submit step to GPT-6 Luna in 131/198 Terminal-Bench attempts (25% pass) vs GPT-6.1 Sol (46% pass)
- Fugu Max weakest: about 110 median steps on Terminal-Bench, 45 of 66 tasks failed in all three runs
