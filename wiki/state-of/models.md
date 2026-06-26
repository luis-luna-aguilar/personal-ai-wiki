---
title: State of Models
type: state-of
domains: [models]
tags: []
as_of: 2026-06-17
sources: [muse-spark, kimi-k2-6-blog, ainews-2026-04-21, ainews-2026-04-22, every-opus-4-7-vibe-check, vectorlab-opus-4-7-flop, vectorlab-qwen-3-6-local-threshold, open-agentic-coding-models, restricted-frontier-deployment, open-weight-momentum-early-april, late-march-small-coding-models, gpt-5-4-march, qwen-3-5-medium-february, glasswing, nano-banana-2-tweet, google-cloud-next-2026, openai-gpt-5-5-launch, danshipper-gpt-5-5-vibe-check, deepseek-v4-preview, ainews-2026-04-25, qwen-3-6-27b-aa-2026-05-01, open-weight-economics-fragmenting-2026-04-30, open-weight-pricing-pressure-2026-04-29, anthropic-spacex-dreams-2026-05-07, arena-leaderboard-2026-05-13, end-of-finetuning-debate-2026-05-13, thinking-machines-interaction-2026-05-12, gpt-5-5-instant-default-2026-05-06, qwen-3-7-arena-2026-05, fable-ban-june-2026, ainews-glm-52-june-2026, kimi-k27-code-june-2026, openai-economics-june-2026, ainews-fable5-june-2026, ainews-open-models-june-2026, every-fable5-vibe-check]
---

# State of Models

Current state of foundation models — frontier and otherwise. Organized by subcategory. A subcategory can have multiple leaders.

## Subcategories

### Frontier multimodal models

General-purpose frontier models competing on broad multimodal capability rather than narrow specialization.

- [Claude Fable 5](../models/claude-fable-5.md) — Anthropic; SWE-Bench Pro 80.3%, FrontierCode Diamond 29.3%, HLE 53%, Terminal-Bench 2.1 88.0%, AA Intelligence Index #1 (64.9); $10/$50/M tokens; **currently suspended globally under US export controls** *(as of 2026-06-17)*
- [Claude Opus 4.7](../models/claude-opus-4-7.md) — Anthropic flagship; Arena (May 2026): "most consistently dominant model," leads nearly every category *(as of 2026-05-13)*
- [GPT-5.5](../models/gpt-5-5.md) — OpenAI; Arena (May 2026): strongest in math; leads on Terminal-Bench 2.0, GDPval, ARC-AGI-2, CyberGym, and BixBench *(as of 2026-05-13)*
- **Gemini 3.1 Pro** — Google; Arena (May 2026): close second overall; leads creative writing *(as of 2026-05-13)*
- **Grok 4.20** — xAI; Arena (May 2026): leads creative writing and hard prompts *(as of 2026-05-13)*
- [Muse Spark](../models/muse-spark.md) — Meta's new multimodal model; the captured launch source emphasizes scaling efficiency and claims Llama 4 Maverick-level capability with over an order of magnitude less training compute *(as of 2026-04-10)*

### Coding models

Open-weight and frontier models evaluated primarily for agentic coding tasks.

- [Kimi K2.7-Code](../models/kimi-k2-7-code.md) — Moonshot AI; open-source 1T/32B MoE; 256K context; +21.8% Kimi Code Bench v2; 30% fewer reasoning tokens than K2.6; vLLM/SGLang day-0 support *(as of 2026-06-13)*
- [MiniMax M2.7](../models/minimax-m2-7.md) — MiniMax; 220B MoE coding / agent model; late-March sources describe unusually strong cost-performance: 56.22% SWE-Pro, 55.6% VIBE-Pro, native multi-agent collaboration, and roughly `$0.30 / $1.20` per million input/output tokens *(as of 2026-03-22)*
- [Composer 2](../models/composer-2.md) — Cursor's in-house coding model; positioned for complex long-horizon coding tasks with reported 61.7 TerminalBench 2.0 and 73.7 SWE-bench Multilingual, plus unusually low input-token pricing inside Cursor; later disclosure says it starts from Moonshot's Kimi-k2.5 and adds continued pretraining plus RL *(as of 2026-03-23)*
- [Qwen 3.6 27B](../models/qwen-3-6-27b.md) — Alibaba; dense 27B (Apache 2.0); beats prior 397B MoE on all coding benchmarks (SWE-bench Verified 77.2, SWE-bench Pro 53.5); runnable under 20 GB RAM; day-0 vLLM/Unsloth/llama.cpp/Ollama; Artificial Analysis (via AINews) ranks it #1 under 150B with Intelligence Index 46 but notes unusually high output-token cost (~21× Gemma 4 31B on the suite) *(as of 2026-05-01)*
- [Qwen 3.6 35B-A3B](../models/qwen-3-6-35b-a3b.md) — Alibaba; MoE variant; practical local-agent baseline on 24GB-class hardware; benchmark lead now held by 27B dense sibling *(as of 2026-04-22)*
- [Qwen 3.7](../models/qwen-3-7.md) — Alibaba; Qwen3.7 Max Preview at #13 overall Arena text (#7 Math, #9 Expert, #10 Coding); Alibaba now #6 lab in text by Arena; Arena preview only at time of writing *(as of 2026-05-19)*
- [GLM-5.2](../models/glm-5-2.md) — Z.ai; MIT; 744B/40B MoE; 1M context; IndexShare (2.9× lower FLOPs at 1M); #1 open Agent Arena; #2 Code Arena frontend; FrontierSWE #3 (behind Fable 5 [banned] and Opus 4.8); Terminal-Bench 2.1: 81.0 *(as of 2026-06-17)*
- [DeepSeek V4](../models/deepseek-v4.md) — DeepSeek; released open-weight Pro/Flash MoE lineup with 1M context, MIT license, strong open-model agentic benchmark placement, and a major KV-cache / inference-systems story; still below the strongest closed frontier systems overall *(as of 2026-04-25)*
- **Meta Spark** — Meta; Arena (May 2026): leads coding category *(as of 2026-05-13)*

### Architecture experiments

Open-weight models notable primarily for architectural innovation rather than benchmark leadership.

- [DiffusionGemma](../models/diffusiongemma.md) — Google; 26B MoE; Apache 2.0; block denoising text generation (non-autoregressive); 1,200 tok/s on H200 in vLLM; first diffusion LLM at this scale; research artifact, not a production replacement *(as of 2026-06-11)*

### Image generation

Specialized models for text-to-image synthesis, image editing, and visual design artifacts.

- [GPT-Image-2](../models/gpt-image-2.md) — OpenAI; #1 across all image arena categories by a +242 Elo margin on text-to-image; thinking mode + web search integration; design-to-code bridge *(as of 2026-04-22)*
- [Nano Banana 2](../models/nano-banana-2.md) — Google; powered by Gemini world understanding + real-time web search imagery; can reflect real-world conditions (current events, weather) in generated images *(as of 2026-04-22)*
- **Veo 3.1** — Google; Arena (May 2026): leads video generation category *(as of 2026-05-13)*

### Specialized utility models

Narrow-purpose models built for a specific infrastructure or pipeline task, rather than general-purpose generation or reasoning.

- [OpenAI Privacy Filter](../models/openai-privacy-filter.md) — OpenAI; 1.5B-total / 50M-active MoE for on-device PII detection and masking; 128k context; Apache 2.0; designed for cheap on-device preprocessing before cloud API calls *(as of 2026-04-23)*

### Real-time voice / interaction models

AI systems that process live audio and/or video streams and respond with sub-second latency — ambient co-presence rather than turn-taking chat. See [State of Voice AI](voice.md) for the broader product surface.

- **TML-Interaction-Small** — Thinking Machines Lab (Mira Murati); 276B-parameter model; 200ms audio streams, 0.4s end-to-end response, mid-sentence interruption; processes live video and audio simultaneously; research preview *(as of 2026-05-12)*
- [GPT-Realtime-2](../tools/gpt-realtime-2.md) — OpenAI; native streaming voice model with 128K context, adjustable reasoning effort, tool use, and interruption recovery *(as of 2026-05-08)*
- **Gemini Magic Pointer** (Googlebook) — Google; OS-level cursor for the Googlebook laptop that activates Gemini when the user clicks anything on screen; integrates Gemini as a pointing intelligence layer *(as of 2026-05-13)*

### Security / cyber-offense capability

Frontier models deployed selectively for autonomous cybersecurity research rather than broadly.

- [Claude Mythos Preview](../models/claude-mythos-preview.md) — Anthropic; restricted preview model; autonomously identifies zero-days at scale; Project Glasswing partners: Cisco, AWS, Microsoft; **also suspended globally under US export controls (June 2026)** *(as of 2026-06-17)*

## AI economics snapshot (as of 2026-06-17)

Key economic signals that shape how frontier model access should be understood:

- **OpenAI FY2025 (leaked):** $38.5B net loss (7× worse than 2024's $5B); revenue $3.7B → $13B; ChatGPT market share dipped below 50% for first time; confidential S-1 filed for IPO; company considering drastic API price cuts ahead of anticipated Anthropic move (WSJ)
- **Subscriber compute costs (SemiAnalysis):** $200/mo Claude Max plan costs Anthropic up to $8,000/mo in compute; $200/mo ChatGPT Pro costs OpenAI up to $14,000/mo — both unlimited-usage tiers are structurally loss-leading at current usage rates
- **Enterprise deployment reality (Scale "6% Report"):** Only 6% of organizations have deployed AI at scale with measurable business value despite large spending; most are still in pilot stage
- **Oracle:** $19B quarterly revenue; largest cloud infrastructure beneficiary of frontier AI compute spending

## Recent changes

- [2026-06-11] DiffusionGemma released (Google, Apache 2.0): 26B MoE diffusion text model; block denoising; 4× faster than diffusion baselines; first diffusion LLM natively in vLLM; open research direction for non-autoregressive text generation
- [2026-06-17] OpenAI FY2025 leaked: $38.5B net loss, $13B revenue, below-50% ChatGPT market share; IPO S-1 filed; SemiAnalysis: $200/mo Claude Max costs Anthropic up to $8,000/mo compute; Scale 6% Report: only 6% of orgs at AI-at-scale stage
- [2026-06-17] Claude Fable 5 and Mythos 5 suspended globally under US government export controls; Fable 5 had topped DeepSWE, FrontierSWE, FrontierMath, and Epoch Capabilities Index (161) before suspension; Claude Opus 4.7 remains the accessible Anthropic frontier model
- [2026-06-17] GLM-5.2 released (MIT, 744B/40B MoE, 1M context): #1 open Agent Arena, #2 Code Arena frontend, Terminal-Bench 2.1: 81.0; supersedes GLM-5.1 (archived to history/)
- [2026-06-13] Kimi K2.7-Code released: +21.8% Kimi Code Bench v2, 30% fewer reasoning tokens vs K2.6, open-source; K2.6 archived to history/
- [2026-05-19] Qwen 3.7 Arena preview: Qwen3.7 Max Preview #13 overall text (#7 Math, #9 Expert, #10 Coding); Qwen3.7 Plus Preview #16 vision; Alibaba reaches top-15 overall in text for the first time
- [2026-05-18] Claude Mythos Preview: Calif team defeated Apple M5 Memory Integrity Enforcement in <5 days — first public kernel memory corruption on M5; small team + frontier AI matches org-scale security research throughput
- [2026-05-06] Secondary coverage says GPT-5.5 Instant became ChatGPT's new default model, replacing GPT-5.3 Instant; official verification still needed for exact rollout and hallucination claims.
- [2026-05-13] Added merged `Real-time voice / interaction models` subcategory; TML-Interaction-Small (Thinking Machines Lab, 276B, 200ms audio, 0.4s response), GPT-Realtime-2, and Google Magic Pointer are first entries
- [2026-05-13] "End of finetuning" debate: OpenAI deprecating finetuning APIs; consensus forming that long-context prompts suffice for ~80% of use cases; counterpoint from top tier (Cursor, Cognition $25B) is increased open-model RLFT, not decreased — weight specialization remains central to their custom-ASIC strategy
