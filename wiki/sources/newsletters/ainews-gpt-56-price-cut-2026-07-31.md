---
title: AINews — GPT-5.6 price cuts, Inkling-Small, Gemini Robotics 2
type: source
source_type: newsletter
source_file: raw/newsletters/2026-07-31-ainews-gpt-56-price-cut-by-20-80-cost-of-gpt.md
url: https://www.latent.space/p/ainews-gpt-56-price-cut-by-20-80
published: 2026-07-31
ingested: 2026-09-07
domains: [models, agents]
---

# AINews — GPT-5.6 price cuts, Inkling-Small, Gemini Robotics 2

AINews recap covering three separate stories from the same issue: OpenAI's GPT-5.6 price cuts (Luna -80%, Terra -20%, new Sol Fast tier) tied to the ongoing "cost of constant intelligence" curve, plus OpenAI's disclosure that Sol was used to autonomously optimize its own serving kernels and speculative decoder; Thinking Machines' Inkling-Small open-weight release (276B/12B active, AA Intelligence Index 40); and Google DeepMind's Gemini Robotics 2 launch (whole-body humanoid control, multi-robot coordination, Gemini Robotics ER 2 embodied reasoning).

## Influenced pages

- [trends/physical-ai-deployment](../../trends/physical-ai-deployment.md) — added Gemini Robotics 2 as the clearest embodied-generality jump tracked so far
- [models/gpt-5-6-sol](../../models/gpt-5-6-sol.md) — new pricing, self-optimizing-infrastructure note
- [state-of/models](../../state-of/models.md) — updated GPT-5.6 Sol and Inkling leader lines, Recent-changes entries
- [models/inkling](../../models/inkling.md) — Inkling-Small shipped status, benchmarks, deployment support
- [trends/open-weight-momentum-broadens](../../trends/open-weight-momentum-broadens.md) — Inkling-Small Recent-changes entry

## Key claims extracted

- Gemini Robotics 2: "one brain for any robot" — whole-body humanoid control, dexterity, multi-robot coordination
- Gemini Robotics ER 2: embodied-reasoning model that observes, plans, coordinates with a VLA model, tracks progress, and recovers from failed steps during multi-minute tasks
- Same checkpoint reportedly controls multiple hardware types
- On-Device 2 can adapt to a new two-arm robot from fewer than 200 examples
- Demos: knot-tying, screwing in a bulb, collaborative garage cleanup
- OpenAI cut GPT-5.6 Luna pricing 80% (to $0.20/$1.20 per 1M tokens) and Terra 20% (to $2.00/$12.00); added Sol Fast at 2.5x lower latency for 2x price
- GPT-5.6 Sol was used post-deployment to autonomously rewrite production Triton/Gluon kernels, cutting serving cost 20%
- A separate Sol-driven effort improved its own speculative-decoding draft model's training, raising token-generation efficiency 15%+
- OpenAI's agentic harness now uses deferred tool discovery, a 10,000-token default tool-output cap, and append-only history for cache-hit rates
- AINews: GPT-5.4-equivalent intelligence now costs ~1/13th what it did four months ago (~2000x annualized), continuing a longer-running cost-collapse trend
- Inkling-Small: 276B total / 12B active MoE, open-weight, natively multimodal (audio+image+text), Python-based image inspection mid-reasoning
- Artificial Analysis Intelligence Index: Inkling-Small 40 vs flagship Inkling 41
- Inkling-Small strengths: Humanity's Last Exam, GPQA Diamond, CritPt, SciCode; weaker on some agentic tasks and factual knowledge
- Day-0 support: vLLM, Modal (single-B300), SGLang, Unsloth (local/GGUF)
