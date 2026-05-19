---
title: State of Models
type: state-of
domains: [models]
tags: []
as_of: 2026-05-19
sources: [muse-spark, kimi-k2-6-blog, ainews-2026-04-21, ainews-2026-04-22, every-opus-4-7-vibe-check, vectorlab-opus-4-7-flop, vectorlab-qwen-3-6-local-threshold, open-agentic-coding-models, restricted-frontier-deployment, open-weight-momentum-early-april, late-march-small-coding-models, gpt-5-4-march, qwen-3-5-medium-february, glasswing, nano-banana-2-tweet, google-cloud-next-2026, openai-gpt-5-5-launch, danshipper-gpt-5-5-vibe-check, deepseek-v4-preview, ainews-2026-04-25, qwen-3-6-27b-aa-2026-05-01, open-weight-economics-fragmenting-2026-04-30, open-weight-pricing-pressure-2026-04-29, anthropic-spacex-dreams-2026-05-07, arena-leaderboard-2026-05-13, end-of-finetuning-debate-2026-05-13, thinking-machines-interaction-2026-05-12, gpt-5-5-instant-default-2026-05-06, qwen-3-7-arena-2026-05]
---

# State of Models

Current state of foundation models — frontier and otherwise. Organized by subcategory. A subcategory can have multiple leaders.

## Subcategories

### Frontier multimodal models

General-purpose frontier models competing on broad multimodal capability rather than narrow specialization.

- [Claude Opus 4.7](../models/claude-opus-4-7.md) — Anthropic flagship; Arena (May 2026): "most consistently dominant model," leads nearly every category *(as of 2026-05-13)*
- [GPT-5.5](../models/gpt-5-5.md) — OpenAI; Arena (May 2026): strongest in math; leads on Terminal-Bench 2.0, GDPval, ARC-AGI-2, CyberGym, and BixBench *(as of 2026-05-13)*
- **Gemini 3.1 Pro** — Google; Arena (May 2026): close second overall; leads creative writing *(as of 2026-05-13)*
- **Grok 4.20** — xAI; Arena (May 2026): leads creative writing and hard prompts *(as of 2026-05-13)*
- [Muse Spark](../models/muse-spark.md) — Meta's new multimodal model; the captured launch source emphasizes scaling efficiency and claims Llama 4 Maverick-level capability with over an order of magnitude less training compute *(as of 2026-04-10)*

### Coding models

Open-weight and frontier models evaluated primarily for agentic coding tasks.

- [Kimi K2.6](../models/kimi-k2-6.md) — Moonshot AI; open-weight 1T-param MoE; SOTA coding/agent benchmark claims; 4K+ tool calls, 12+ hour runs; community now treating it as an Opus 4.7 replacement for ~85% of practical tasks *(as of 2026-04-22)*
- [MiniMax M2.7](../models/minimax-m2-7.md) — MiniMax; 220B MoE coding / agent model; late-March sources describe unusually strong cost-performance: 56.22% SWE-Pro, 55.6% VIBE-Pro, native multi-agent collaboration, and roughly `$0.30 / $1.20` per million input/output tokens *(as of 2026-03-22)*
- [Composer 2](../models/composer-2.md) — Cursor's in-house coding model; positioned for complex long-horizon coding tasks with reported 61.7 TerminalBench 2.0 and 73.7 SWE-bench Multilingual, plus unusually low input-token pricing inside Cursor; later disclosure says it starts from Moonshot's Kimi-k2.5 and adds continued pretraining plus RL *(as of 2026-03-23)*
- [Qwen 3.6 27B](../models/qwen-3-6-27b.md) — Alibaba; dense 27B (Apache 2.0); beats prior 397B MoE on all coding benchmarks (SWE-bench Verified 77.2, SWE-bench Pro 53.5); runnable under 20 GB RAM; day-0 vLLM/Unsloth/llama.cpp/Ollama; Artificial Analysis (via AINews) ranks it #1 under 150B with Intelligence Index 46 but notes unusually high output-token cost (~21× Gemma 4 31B on the suite) *(as of 2026-05-01)*
- [Qwen 3.6 35B-A3B](../models/qwen-3-6-35b-a3b.md) — Alibaba; MoE variant; practical local-agent baseline on 24GB-class hardware; benchmark lead now held by 27B dense sibling *(as of 2026-04-22)*
- [Qwen 3.7](../models/qwen-3-7.md) — Alibaba; Qwen3.7 Max Preview at #13 overall Arena text (#7 Math, #9 Expert, #10 Coding); Alibaba now #6 lab in text by Arena; Arena preview only at time of writing *(as of 2026-05-19)*
- [GLM-5.1](../models/glm-5-1.md) — open-weight contender described in the captured sources as a top benchmark performer for coding and agent workflows *(as of 2026-04-08)*
- [DeepSeek V4](../models/deepseek-v4.md) — DeepSeek; released open-weight Pro/Flash MoE lineup with 1M context, MIT license, strong open-model agentic benchmark placement, and a major KV-cache / inference-systems story; still below the strongest closed frontier systems overall *(as of 2026-04-25)*
- **Meta Spark** — Meta; Arena (May 2026): leads coding category *(as of 2026-05-13)*

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

- [Claude Mythos Preview](../models/claude-mythos-preview.md) — Anthropic; restricted preview model; autonomously identifies zero-days at scale; Calif team used it to defeat Apple M5 Memory Integrity Enforcement in <5 days (May 2026); Project Glasswing partners: Cisco, AWS, Microsoft; not publicly available *(as of 2026-05-18)*

## Recent changes

- [2026-05-19] Qwen 3.7 Arena preview: Qwen3.7 Max Preview #13 overall text (#7 Math, #9 Expert, #10 Coding); Qwen3.7 Plus Preview #16 vision; Alibaba reaches top-15 overall in text for the first time
- [2026-05-18] Claude Mythos Preview: Calif team defeated Apple M5 Memory Integrity Enforcement in <5 days — first public kernel memory corruption on M5; small team + frontier AI matches org-scale security research throughput
- [2026-05-06] Secondary coverage says GPT-5.5 Instant became ChatGPT's new default model, replacing GPT-5.3 Instant; official verification still needed for exact rollout and hallucination claims.
- [2026-05-13] Added merged `Real-time voice / interaction models` subcategory; TML-Interaction-Small (Thinking Machines Lab, 276B, 200ms audio, 0.4s response), GPT-Realtime-2, and Google Magic Pointer are first entries
- [2026-05-13] "End of finetuning" debate: OpenAI deprecating finetuning APIs; consensus forming that long-context prompts suffice for ~80% of use cases; counterpoint from top tier (Cursor, Cognition $25B) is increased open-model RLFT, not decreased — weight specialization remains central to their custom-ASIC strategy
