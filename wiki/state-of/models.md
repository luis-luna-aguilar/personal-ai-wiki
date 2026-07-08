---
title: State of Models
type: state-of
domains: [models]
tags: []
as_of: 2026-07-02
sources: [muse-spark, kimi-k2-6-blog, ainews-2026-04-21, ainews-2026-04-22, every-opus-4-7-vibe-check, vectorlab-opus-4-7-flop, vectorlab-qwen-3-6-local-threshold, open-agentic-coding-models, restricted-frontier-deployment, open-weight-momentum-early-april, late-march-small-coding-models, gpt-5-4-march, qwen-3-5-medium-february, glasswing, nano-banana-2-tweet, google-cloud-next-2026, openai-gpt-5-5-launch, danshipper-gpt-5-5-vibe-check, deepseek-v4-preview, ainews-2026-04-25, qwen-3-6-27b-aa-2026-05-01, open-weight-economics-fragmenting-2026-04-30, open-weight-pricing-pressure-2026-04-29, anthropic-spacex-dreams-2026-05-07, arena-leaderboard-2026-05-13, end-of-finetuning-debate-2026-05-13, thinking-machines-interaction-2026-05-12, gpt-5-5-instant-default-2026-05-06, qwen-3-7-arena-2026-05, fable-ban-june-2026, ainews-glm-52-june-2026, kimi-k27-code-june-2026, openai-economics-june-2026, ainews-fable5-june-2026, ainews-open-models-june-2026, every-fable5-vibe-check, ainews-cosmos-nemotron-june-2026, ainews-ideogram-june-2026, every-opus-48-june-2026, ainews-mai-build-june-2026, satya-nadella-no-priors-june-2026, ainews-june-05-2026, ainews-not-much-happened-2026-07-02, every-sonnet-5-vibe-check-2026-07-02, the-code-devin-security-2026-07-02, every-tale-of-two-models-2026-07-05, claude-sonnet-5-official-2026-06-30, gpt-56-sol-restricted-preview-2026-06, metr-gpt-5-6-sol-eval-2026-06, glm-52-frontier-adjacent-2026-06]
---

# State of Models

Current state of foundation models — frontier and otherwise. Organized by subcategory. A subcategory can have multiple leaders.

## Subcategories

### Frontier models

General-purpose frontier models competing on broad capability rather than narrow specialization.

- [Claude Fable 5](../models/claude-fable-5.md) — Anthropic; SWE-Bench Pro 80.3%, FrontierCode Diamond 29.3%, HLE 53%, Terminal-Bench 2.1 88.0%, AA Intelligence Index #1 (64.9); re-enabled with safety fallback routing to Opus 4.8 for some sensitive domains *(as of 2026-07-02)*
- [Claude Sonnet 5](../models/claude-sonnet-5.md) — Anthropic middle-tier default and most agentic Sonnet; available in Claude, Claude Code, and API, with early testing still flagging cost-per-task sensitivity at high effort *(as of 2026-07-02)*
- [Claude Opus 4.8](../models/claude-opus-4-8.md) — Anthropic; current accessible flagship after 4.7; Dynamic Workflows; Figma MCP bidirectional code-to-design and design-to-code loop *(as of 2026-06-03)*
- [GPT-5.5](../models/gpt-5-5.md) — OpenAI; Arena (May 2026): strongest in math; leads on Terminal-Bench 2.0, GDPval, ARC-AGI-2, CyberGym, and BixBench *(as of 2026-05-13)*
- [GPT-5.6 Sol](../models/gpt-5-6-sol.md) — OpenAI restricted-preview flagship reported by AINews; METR predeployment eval found unusually high detected cheating in its ReAct harness and highly uncertain time-horizon estimates *(as of 2026-06-26)*
- [MAI-Thinking-1](../models/mai-thinking-1.md) — Microsoft; 35B active / 1T total MoE; 256K context; 97% AIME 2025, 53% SWE-Bench Pro; blind human preference over Claude Sonnet 4.6; trained from scratch with no synthetic data or distillation *(as of 2026-06-03)*
- **Gemini 3.1 Pro** — Google; Arena (May 2026): close second overall; leads creative writing *(as of 2026-05-13)*
- **Grok 4.20** — xAI; Arena (May 2026): leads creative writing and hard prompts *(as of 2026-05-13)*
- [Muse Spark](../models/muse-spark.md) — Meta's new multimodal model; the captured launch source emphasizes scaling efficiency and claims Llama 4 Maverick-level capability with over an order of magnitude less training compute *(as of 2026-04-10)*

### Coding models

Open-weight and frontier models evaluated primarily for agentic coding tasks.

- [Kimi K2.7-Code](../models/kimi-k2-7-code.md) — Moonshot AI; open-source 1T/32B MoE; 256K context; +21.8% Kimi Code Bench v2; 30% fewer reasoning tokens than K2.6; vLLM/SGLang day-0 support *(as of 2026-06-13)*
- [MiniMax M3](../models/minimax-m3.md) — MiniMax; "open-weight frontier" claim contested because weights were not disclosed at launch; 1M context; 59.0% SWE-Bench Pro, 66.0% Terminal Bench 2.1, 74.2% MCP Atlas; PostTrainBench #3; high token consumption and verbose self-check loops *(as of 2026-06-02)*
- [Composer 2](../models/composer-2.md) — Cursor's in-house coding model; positioned for complex long-horizon coding tasks with reported 61.7 TerminalBench 2.0 and 73.7 SWE-bench Multilingual, plus unusually low input-token pricing inside Cursor; later disclosure says it starts from Moonshot's Kimi-k2.5 and adds continued pretraining plus RL *(as of 2026-03-23)*
- [Qwen 3.6 27B](../models/qwen-3-6-27b.md) — Alibaba; dense 27B (Apache 2.0); beats prior 397B MoE on all coding benchmarks (SWE-bench Verified 77.2, SWE-bench Pro 53.5); runnable under 20 GB RAM; day-0 vLLM/Unsloth/llama.cpp/Ollama; Artificial Analysis (via AINews) ranks it #1 under 150B with Intelligence Index 46 but notes unusually high output-token cost (~21× Gemma 4 31B on the suite) *(as of 2026-05-01)*
- [Qwen 3.6 35B-A3B](../models/qwen-3-6-35b-a3b.md) — Alibaba; MoE variant; practical local-agent baseline on 24GB-class hardware; benchmark lead now held by 27B dense sibling *(as of 2026-04-22)*
- [Qwen 3.7](../models/qwen-3-7.md) — Alibaba; Qwen3.7 Max Preview at #13 overall Arena text (#7 Math, #9 Expert, #10 Coding); Alibaba now #6 lab in text by Arena; Arena preview only at time of writing *(as of 2026-05-19)*
- [GLM-5.2](../models/glm-5-2.md) — Z.ai; MIT open-weight 744B/40B MoE with 1M context; strongest current open-weight coding/agent contender, now operationalized across hosted inference and agent harnesses, but still behind Fable/Opus on the hardest long-horizon knowledge-work tasks *(as of 2026-06-23)*
- [DeepSeek V4](../models/deepseek-v4.md) — DeepSeek; released open-weight Pro/Flash MoE lineup with 1M context, MIT license, strong open-model agentic benchmark placement, and a major KV-cache / inference-systems story; still below the strongest closed frontier systems overall *(as of 2026-04-25)*
- **MAI-Code-1-Flash** — Microsoft; 5B active / 137B MoE; 51% SWE-Bench Pro; powers GitHub Copilot and VS Code; designed for high-throughput coding inference *(as of 2026-06-03)*
- **Meta Spark** — Meta; Arena (May 2026): leads coding category *(as of 2026-05-13)*

### Open-weight models

Broad foundation models whose main current-state question is open or open-ish weight availability, deployment control, and practical ecosystem support.

- [Nemotron 3 Ultra](../models/nemotron-3-ultra.md) — NVIDIA; 550B/55B MoE; hybrid Mamba/attention + LatentMoE; 1M context; 300-400+ tok/s; OpenMDW 1.1; NVFP4 pretraining on 20T tokens; 47.7 Intelligence Index BF16 *(as of 2026-06-02)*
- [DeepSeek V4](../models/deepseek-v4.md) — DeepSeek; MIT open-weight Pro/Flash lineup with 1M context and serious long-context agent infrastructure signal *(as of 2026-04-25)*

### Architecture experiments

Open-weight models notable primarily for architectural innovation rather than benchmark leadership.

- [DiffusionGemma](../models/diffusiongemma.md) — Google; 26B MoE; Apache 2.0; block denoising text generation (non-autoregressive); 1,200 tok/s on H200 in vLLM; first diffusion LLM at this scale; research artifact, not a production replacement *(as of 2026-06-11)*

### Image generation

Specialized models for text-to-image synthesis, image editing, and visual design artifacts.

- [GPT-Image-2](../models/gpt-image-2.md) — OpenAI; #1 across all image arena categories by a +242 Elo margin on text-to-image; thinking mode + web search integration; design-to-code bridge *(as of 2026-04-22)*
- [Nano Banana 2](../models/nano-banana-2.md) — Google; powered by Gemini world understanding + real-time web search imagery; can reflect real-world conditions (current events, weather) in generated images *(as of 2026-04-22)*
- **[Ideogram 4.0](../models/ideogram-4.md) — Ideogram; 9.3B DiT; #8 overall Image Arena, #1 open image model; strong text rendering and branding; fp8/nf4 checkpoints, ComfyUI; no commercial license *(as of 2026-06-04)*
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
- **Anthropic RSI (June 2026):** Claude writes 80%+ of Anthropic's merged code; engineers ship 8x more code/quarter; internal task success 26% -> 76% in 6 months; Mythos Preview: 52x speedup on training script optimization vs Claude Opus 4 baseline (~3x); Mythos gave better "next step" suggestions than humans 64% of time

## Recent changes

- [2026-07-02] Fable 5 returned online with safety fallback routing; Sonnet 5 arrived as Anthropic's middle-tier Claude 5 model but early testing questioned its cost/performance positioning.
- [2026-06-23] GLM-5.2 follow-on coverage adds frontier-adjacent open-weight signal: strong AA-Briefcase cost/performance, broad hosted-provider adoption, and coding-agent harness uptake.
- [2026-06-30] Official Sonnet 5 launch details added: Claude Code/API availability, `claude-sonnet-5`, launch pricing, effort levels, and safety notes.
- [2026-06-29] Added caveated GPT-5.6/Sol restricted-preview note from newsletter coverage; official source capture still blocked.
- [2026-06-26] METR published its GPT-5.6 Sol predeployment evaluation, emphasizing high detected cheating and uncertainty rather than a clean capability estimate.
- [2026-06-17] OpenAI FY2025 leaked: $38.5B net loss, $13B revenue, below-50% ChatGPT market share; IPO S-1 filed; SemiAnalysis: $200/mo Claude Max costs Anthropic up to $8,000/mo compute; Scale 6% Report: only 6% of orgs at AI-at-scale stage
- [2026-06-17] Claude Fable 5 and Mythos 5 suspended globally under US government export controls; Fable 5 had topped DeepSWE, FrontierSWE, FrontierMath, and Epoch Capabilities Index (161) before suspension; Claude Opus 4.8 remains the accessible Anthropic frontier model
- [2026-06-17] GLM-5.2 released (MIT, 744B/40B MoE, 1M context): #1 open Agent Arena, #2 Code Arena frontend, Terminal-Bench 2.1: 81.0; supersedes GLM-5.1 (archived to history/)
- [2026-06-13] Kimi K2.7-Code released: +21.8% Kimi Code Bench v2, 30% fewer reasoning tokens vs K2.6, open-source; K2.6 archived to history/
- [2026-06-11] DiffusionGemma released (Google, Apache 2.0): 26B MoE diffusion text model; block denoising; 4× faster than diffusion baselines; first diffusion LLM natively in vLLM; open research direction for non-autoregressive text generation
- [2026-06-05] Anthropic RSI: 80%+ code by Claude, 8x engineer throughput, task success 26% -> 76%; Mythos 52x speedup vs Opus 4 on training script task; S-1 confidentially filed with SEC
