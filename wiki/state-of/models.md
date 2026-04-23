---
title: State of Models
type: state-of
domains: [models]
tags: []
as_of: 2026-04-23
sources: [muse-spark, kimi-k2-6-blog, ainews-2026-04-21, ainews-2026-04-22, every-opus-4-7-vibe-check, vectorlab-opus-4-7-flop, vectorlab-qwen-3-6-local-threshold, open-agentic-coding-models, restricted-frontier-deployment, open-weight-momentum-early-april, late-march-small-coding-models, gpt-5-4-march, qwen-3-5-medium-february, glasswing, nano-banana-2-tweet]
---

# State of Models

Current state of foundation models — frontier and otherwise. Organized by subcategory. A subcategory can have multiple leaders.

## Subcategories

### Frontier multimodal models

General-purpose frontier models competing on broad multimodal capability rather than narrow specialization.

- [[models/gpt-5-4]] — OpenAI's March frontier update looked like the strongest general-purpose reasoning / browsing / agent model in the captured source cycle, though the same coverage still gives Claude the edge on writing, personality, and design-heavy work *(as of 2026-03-08)*
- [[models/claude-opus-4-7]] — Anthropic flagship; stronger on explicit coding, document, and visual artifact tasks, but early user reports describe more literal behavior and mixed long-context reliability *(as of 2026-04-21)*
- [[models/muse-spark]] — Meta's new multimodal model; the captured launch source emphasizes scaling efficiency and claims Llama 4 Maverick-level capability with over an order of magnitude less training compute *(as of 2026-04-10)*

### Coding models

Open-weight and frontier models evaluated primarily for agentic coding tasks.

- [[models/kimi-k2-6]] — Moonshot AI; open-weight 1T-param MoE; SOTA coding/agent benchmark claims; 4K+ tool calls, 12+ hour runs; community now treating it as an Opus 4.7 replacement for ~85% of practical tasks *(as of 2026-04-22)*
- [[models/minimax-m2-7]] — MiniMax; 220B MoE coding / agent model; late-March sources describe unusually strong cost-performance: 56.22% SWE-Pro, 55.6% VIBE-Pro, native multi-agent collaboration, and roughly `$0.30 / $1.20` per million input/output tokens *(as of 2026-03-22)*
- [[models/composer-2]] — Cursor's in-house coding model; positioned for complex long-horizon coding tasks with reported 61.7 TerminalBench 2.0 and 73.7 SWE-bench Multilingual, plus unusually low input-token pricing inside Cursor; later disclosure says it starts from Moonshot's Kimi-k2.5 and adds continued pretraining plus RL *(as of 2026-03-23)*
- [[models/qwen-3-6-27b]] — Alibaba; dense 27B (Apache 2.0); beats prior 397B MoE on all coding benchmarks (SWE-bench Verified 77.2, SWE-bench Pro 53.5); runnable under 20 GB RAM; day-0 vLLM/Unsloth/llama.cpp/Ollama *(as of 2026-04-23)*
- [[models/qwen-3-6-35b-a3b]] — Alibaba; MoE variant; practical local-agent baseline on 24GB-class hardware; benchmark lead now held by 27B dense sibling *(as of 2026-04-22)*
- [[models/glm-5-1]] — open-weight contender described in the captured sources as a top benchmark performer for coding and agent workflows *(as of 2026-04-08)*

### Image generation

Specialized models for text-to-image synthesis, image editing, and visual design artifacts.

- [[models/gpt-image-2]] — OpenAI; #1 across all image arena categories by a +242 Elo margin on text-to-image; thinking mode + web search integration; design-to-code bridge *(as of 2026-04-22)*
- [[models/nano-banana-2]] — Google; powered by Gemini world understanding + real-time web search imagery; can reflect real-world conditions (current events, weather) in generated images *(as of 2026-04-22)*

### Specialized utility models

Narrow-purpose models built for a specific infrastructure or pipeline task, rather than general-purpose generation or reasoning.

- [[models/openai-privacy-filter]] — OpenAI; 1.5B-total / 50M-active MoE for on-device PII detection and masking; 128k context; Apache 2.0; designed for cheap on-device preprocessing before cloud API calls *(as of 2026-04-23)*

### Security / cyber-offense capability

Frontier models deployed selectively for autonomous cybersecurity research rather than broadly.

- [[models/claude-mythos-preview]] — Anthropic; restricted preview model; autonomously identifies zero-days at scale in major OSes and browsers; used in Project Glasswing with partners Cisco, AWS, Microsoft; not publicly available *(as of 2026-04-22)*

## Recent changes

- [2026-04-23] Added 'Specialized utility models' subcategory; [[models/openai-privacy-filter]] is the first entry — on-device PII redaction, 1.5B MoE, Apache 2.0
- [2026-04-23] Added [[models/qwen-3-6-27b]] to Coding models; dense 27B beats prior 397B MoE on all coding benchmarks; day-0 open ecosystem support
- [2026-03-08] Added [[models/gpt-5-4]] under `Frontier multimodal models`; strongest captured March signal for general-purpose reasoning, browsing, and agent work, with Claude still stronger on writing/taste
- [2026-03-23] Late-March small-model cluster sharpened the affordable coding tier: MiniMax M2.7 looks stronger on practical economics, while Composer 2 graduated from a Cursor-only mention to a real model with benchmark and lineage claims
- [2026-04-07] Early-April open-weight momentum broadened beyond coding-only releases: Gemma 4 became a notable open multimodal adoption signal; see [[trends/open-weight-momentum-broadens]]
- [2026-04-13] Added [[models/minimax-m2-7]] and [[models/glm-5-1]] under `Coding models`; earlier April sources show open coding-model momentum was broader than the later Qwen/Kimi cluster alone
- [2026-04-08] Mythos / Glasswing cluster suggests a new trend: frontier capability may increasingly be deployed selectively rather than broadly — see [[trends/restricted-frontier-deployment]]
- [2026-04-21] Added [[models/qwen-3-6-35b-a3b]] under `Coding models`; practical local-agent baseline on 24GB-class hardware
- [2026-04-21] Anthropic/AWS: 5 GW compute secured, $5B investment, up to $20B more — see [[trends/compute-infrastructure]]
- [2026-04-21] Added [[models/claude-opus-4-7]] — #1 Vision & Document Arena
- [2026-04-22] Added `Image generation` subcategory; [[models/gpt-image-2]] debuts as dominant arena leader by +242 Elo margin on text-to-image; also updates the image-as-spec pattern for coding agents
- [2026-04-22] Qwen 3.6 35B-A3B niche sharpened: strong for coding/tools, weaker for creative/translation; Qwen 3.6 Max Preview live but likely proprietary-only
- [2026-04-22] Kimi K2.6: community framing as practical Opus 4.7 replacement for ~85% of tasks
- [2026-04-22] Added `Security / cyber-offense capability` subcategory; [[models/claude-mythos-preview]] confirms restricted-frontier pattern with autonomous zero-day discovery across major OSes/browsers
- [2026-04-22] Added [[models/nano-banana-2]] to `Image generation` subcategory; Google enters the arena with Gemini+web-search-grounded image generation
