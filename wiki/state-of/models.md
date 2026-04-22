---
title: State of Models
type: state-of
domains: [models]
tags: []
as_of: 2026-04-21
sources: [muse-spark, kimi-k2-6-blog, ainews-2026-04-21, every-opus-4-7-vibe-check, vectorlab-opus-4-7-flop, vectorlab-qwen-3-6-local-threshold, open-agentic-coding-models, restricted-frontier-deployment, open-weight-momentum-early-april, late-march-small-coding-models]
---

# State of Models

Current state of foundation models — frontier and otherwise. Organized by subcategory. A subcategory can have multiple leaders.

## Subcategories

### Frontier multimodal models

General-purpose frontier models competing on broad multimodal capability rather than narrow specialization.

- [[models/claude-opus-4-7]] — Anthropic flagship; stronger on explicit coding, document, and visual artifact tasks, but early user reports describe more literal behavior and mixed long-context reliability *(as of 2026-04-21)*
- [[models/muse-spark]] — Meta's new multimodal model; the captured launch source emphasizes scaling efficiency and claims Llama 4 Maverick-level capability with over an order of magnitude less training compute *(as of 2026-04-10)*

### Coding models

Open-weight and frontier models evaluated primarily for agentic coding tasks.

- [[models/kimi-k2-6]] — Moonshot AI; open-weight 1T-param MoE; open-source SOTA claims: HLE w/ tools 54.0, SWE-Bench Pro 58.6, SWE-bench Multilingual 76.7, BrowseComp 83.2; 4K+ tool calls, 12+ hour continuous runs *(as of 2026-04-21)*
- [[models/minimax-m2-7]] — MiniMax; 220B MoE coding / agent model; late-March sources describe unusually strong cost-performance: 56.22% SWE-Pro, 55.6% VIBE-Pro, native multi-agent collaboration, and roughly `$0.30 / $1.20` per million input/output tokens *(as of 2026-03-22)*
- [[models/composer-2]] — Cursor's in-house coding model; positioned for complex long-horizon coding tasks with reported 61.7 TerminalBench 2.0 and 73.7 SWE-bench Multilingual, plus unusually low input-token pricing inside Cursor; later disclosure says it starts from Moonshot's Kimi-k2.5 and adds continued pretraining plus RL *(as of 2026-03-23)*
- [[models/qwen-3-6-35b-a3b]] — Alibaba; open-weight MoE coding model increasingly described as the first practical local-agent baseline for roughly 24GB-class local hardware, such as a higher-memory MacBook Pro or comparable GPU setup *(as of 2026-04-21)*
- [[models/glm-5-1]] — open-weight contender described in the captured sources as a top benchmark performer for coding and agent workflows *(as of 2026-04-08)*

## Recent changes

- [2026-03-23] Late-March small-model cluster sharpened the affordable coding tier: MiniMax M2.7 looks stronger on practical economics, while Composer 2 graduated from a Cursor-only mention to a real model with benchmark and lineage claims
- [2026-04-07] Early-April open-weight momentum broadened beyond coding-only releases: Gemma 4 became a notable open multimodal adoption signal; see [[trends/open-weight-momentum-broadens]]
- [2026-04-13] Added [[models/minimax-m2-7]] and [[models/glm-5-1]] under `Coding models`; earlier April sources show open coding-model momentum was broader than the later Qwen/Kimi cluster alone
- [2026-04-08] Mythos / Glasswing cluster suggests a new trend: frontier capability may increasingly be deployed selectively rather than broadly — see [[trends/restricted-frontier-deployment]]
- [2026-04-21] Added [[models/qwen-3-6-35b-a3b]] under `Coding models`; practical local-agent baseline on 24GB-class hardware
- [2026-04-21] Anthropic/AWS: 5 GW compute secured, $5B investment, up to $20B more — see [[trends/compute-infrastructure]]
- [2026-04-21] Added [[models/claude-opus-4-7]] — #1 Vision & Document Arena
