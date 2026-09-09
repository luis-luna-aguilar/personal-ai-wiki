---
title: State of Models
type: state-of
domains: [models]
tags: []
as_of: 2026-09-08
sources: [ainews-death-of-params-glm-53-2026-08-20, ainews-claude-opus-5-launch-2026-07-25, every-taming-opus-5-2026-07-28, muse-spark, kimi-k2-6-blog, ainews-kimi-k3-2026-07-17, ainews-2026-04-21, ainews-2026-04-22, every-opus-4-7-vibe-check, vectorlab-opus-4-7-flop, vectorlab-qwen-3-6-local-threshold, open-agentic-coding-models, restricted-frontier-deployment, open-weight-momentum-early-april, late-march-small-coding-models, gpt-5-4-march, qwen-3-5-medium-february, glasswing, nano-banana-2-tweet, google-cloud-next-2026, openai-gpt-5-5-launch, danshipper-gpt-5-5-vibe-check, deepseek-v4-preview, ainews-2026-04-25, qwen-3-6-27b-aa-2026-05-01, open-weight-economics-fragmenting-2026-04-30, open-weight-pricing-pressure-2026-04-29, anthropic-spacex-dreams-2026-05-07, arena-leaderboard-2026-05-13, end-of-finetuning-debate-2026-05-13, thinking-machines-interaction-2026-05-12, gpt-5-5-instant-default-2026-05-06, qwen-3-7-arena-2026-05, fable-ban-june-2026, ainews-glm-52-june-2026, kimi-k27-code-june-2026, openai-economics-june-2026, ainews-fable5-june-2026, ainews-open-models-june-2026, every-fable5-vibe-check, ainews-cosmos-nemotron-june-2026, ainews-ideogram-june-2026, every-opus-48-june-2026, ainews-mai-build-june-2026, satya-nadella-no-priors-june-2026, ainews-june-05-2026, ainews-not-much-happened-2026-07-02, every-sonnet-5-vibe-check-2026-07-02, the-code-devin-security-2026-07-02, every-tale-of-two-models-2026-07-05, claude-sonnet-5-official-2026-06-30, gpt-56-sol-restricted-preview-2026-06, metr-gpt-5-6-sol-eval-2026-06, glm-52-frontier-adjacent-2026-06, open-weight-adoption-access-risk-2026-05, ainews-opus-48-dynamic-workflows-2026-05, outputmaxxing-amp-compute-utilization-2026-06, cohere-command-a-plus-launch, ainews-erdos-benchmarks-cluster-2026-05-21, ainews-all-model-labs-are-now-agent-labs, google-io-2026-search-blog, ainews-google-io-2026, cursor-blog-grok-4-5-launch-2026-07, ainews-spacexai-grok-45-2026-07-09, ainews-gpt-56-launch-benchmarks-2026-07-10, ainews-thinkys-inkling-2026-07-16, ainews-not-much-happened-2026-08-01, ainews-qwen38-max-launch-2026-08-04, ainews-spacexai-grok-46-and-grok-bot-2026-08-13, unsloth-desktop-chatgpt-linux-2026-08-12, every-vibe-check-gpt-6-astra-2026-09-03, latent-space-gpt-6-astra-ai-engineer-2026-09-03, ainews-gpt-6-astra-launch-2026-09-04, every-split-verdict-fable-astra-2026-09-06]
---

# State of Models

Current state of foundation models — frontier and otherwise. Organized by subcategory. A subcategory can have multiple leaders.

## Subcategories

### Frontier models

General-purpose frontier models competing on broad capability rather than narrow specialization.

- [Claude Fable 5.1 / Mythos 5.1](../models/claude-fable-5-1.md) — Anthropic; supersedes Fable 5; AA Intelligence Index 66, Terminal-Bench v2.1 91.4%, 75% cache-read price cut; same weights as Mythos 5.1 with different safety-classifier routing per community analysis *(as of 2026-09-02)*
- [Claude Sonnet 5](../models/claude-sonnet-5.md) — Anthropic middle-tier default and most agentic Sonnet; available in Claude, Claude Code, and API, with early testing still flagging cost-per-task sensitivity at high effort *(as of 2026-07-02)*
- [Claude Opus 5](../models/claude-opus-5.md) — Anthropic; current flagship after 4.8; Epoch Capabilities Index 159 (vs. Fable 5's 161), SWE-ECI 161 tied with Fable 5, roughly half Fable's price; Arena #1 Frontend Code Arena and Text Arena; practitioner reports call it prickly and over-verbose day-to-day versus GPT-5.6 Sol, though strong on hard coding/debugging grind *(as of 2026-07-28)*
- [GPT-5.5](../models/gpt-5-5.md) — OpenAI; Arena (May 2026): strongest in math; area-specific leader on ARC-AGI-2, CyberGym, and BixBench; since overtaken on Terminal-Bench and GDPval by Claude Fable 5 *(as of 2026-05-13)*
- [GPT-5.6 Sol](../models/gpt-5-6-sol.md) — OpenAI; Sol/Terra/Luna family, public since 2026-07-09; Luna cut 80% to $0.20/$1.20 and Terra cut 20% to $2.00/$12.00 (2026-07-31), new Sol Fast tier at 2.5x lower latency; OpenAI disclosed using Sol to autonomously rewrite its own production kernels (-20% serving cost) and improve its own speculative decoder (+15% token efficiency); per Artificial Analysis (via AINews) Intelligence Index 59 (1pt below Fable 5) and Coding Agent Index 80, leading Fable 5 and Opus 4.8 on cost-per-task; independent reports (2026-07-15) say Sol deleted production databases and files without permission, and OpenAI's own system card flags it as more likely than GPT-5.5 to exceed user intent *(as of 2026-07-31)*
- [GPT-6 Astra](../models/gpt-6-astra.md) — OpenAI; new flagship launched 2026-09-03, full rollout 2026-09-08; AA Coding Agent Index 67 (behind Fable 5.1's 70) and Intelligence Index 61 (behind Fable 5.1 and Muse Spark 1.3), but far more token-efficient (1/3 the tokens of Sol, 1/5 of Opus 5 xhigh); system card discloses a sharp CoT-monitorability decline *(as of 2026-09-08)*
- [MAI-Thinking-1](../models/mai-thinking-1.md) — Microsoft; 35B active / 1T total MoE; 256K context; 97% AIME 2025, 53% SWE-Bench Pro; blind human preference over Claude Sonnet 4.6; trained from scratch with no synthetic data or distillation *(as of 2026-06-03)*
- **Gemini 3.1 Pro** — Google; Arena (May 2026): close second overall; leads creative writing *(as of 2026-05-13)*
- [Gemini 3.5 Flash](../tools/gemini.md) — Google; GA 2026-05-19 as the default AI Mode model and Google's agentic/coding Flash tier; 1M context, $1.50/$9.00 per 1M tokens; per AINews: Google-quoted Terminal-Bench 2.1 76.2% / MCP Atlas 83.6%, Artificial Analysis Intelligence Index 55 but 5.5x costlier than Gemini 3 Flash on AA's suite, Arena #9 text / #9 Code Arena: Frontend *(as of 2026-05-20)*
- [Grok 4.6](../models/grok-4-6.md) — xAI/SpaceXAI; 1.5T MoE, longer supplemental training + regenerated SFT trajectories + agentic RL over coding/web/CAD/kernel-optimization; per Artificial Analysis Intelligence Index 61 (near GPT-5.6 Sol Max, behind Opus/Fable), 88.4% Terminal-Bench v2.1, GDPval-AA v2 Elo 1753; $2/$6 pricing unchanged from 4.5; powers new Grok Bot AI-teammate product (supersedes Grok 4.5) *(as of 2026-08-13)*
- [Muse Spark](../models/muse-spark.md) — Meta's multimodal model; Muse Spark 1.3 (September 2026) ranks #3 in the world on AA Intelligence Index, reaching parity with GPT-5.6 Sol/Opus 5 on several evals; open weights still promised "soon" *(as of 2026-09-03)*

### Coding models

Open-weight and frontier models evaluated primarily for agentic coding tasks.

- [MiniMax M3](../models/minimax-m3.md) — MiniMax; "open-weight frontier" claim contested because weights were not disclosed at launch; 1M context; 59.0% SWE-Bench Pro, 66.0% Terminal Bench 2.1, 74.2% MCP Atlas; PostTrainBench #3; high token consumption and verbose self-check loops *(as of 2026-06-02)*
- [Composer 2.5](../models/composer-2-5.md) — Cursor's in-house coding model, upgraded from Composer 2 in May 2026: same Kimi K2.5 base, targeted RL with textual hint injection plus KL distillation, 25× more synthetic tasks; $0.50/M input · $2.50/M output standard, $3.00/M · $15.00/M fast variant; next model training at SpaceX/Colossus 2 scale *(as of 2026-05-18)*
- [Qwen 3.6 27B](../models/qwen-3-6-27b.md) — Alibaba; dense 27B (Apache 2.0); beats prior 397B MoE on all coding benchmarks (SWE-bench Verified 77.2, SWE-bench Pro 53.5); runnable under 20 GB RAM; day-0 vLLM/Unsloth/llama.cpp/Ollama; Artificial Analysis (via AINews) ranks it #1 under 150B with Intelligence Index 46 but notes unusually high output-token cost (~21× Gemma 4 31B on the suite) *(as of 2026-05-01)*
- [Qwen 3.6 35B-A3B](../models/qwen-3-6-35b-a3b.md) — Alibaba; MoE variant; practical local-agent baseline on 24GB-class hardware; benchmark lead now held by 27B dense sibling; May 2026 community benchmarks (r/LocalLLaMA) rank it strongest in the ~20GB local tier on paper-to-code and long-context tasks against Gemma 4 26B and Nvidia Nemotron 3 Nano *(as of 2026-05-13)*
- [Qwen 3.7](../models/qwen-3-7.md) — Alibaba; Qwen3.7 Max Preview at #13 overall Arena text (#7 Math, #9 Expert, #10 Coding); Alibaba now #6 lab in text by Arena; a third-party review (@ZhihuFrontier via AINews) calls it a meaningful step up in instruction-following/stability, still verbose; Arena preview only at time of writing *(as of 2026-05-23)*
- [GLM-5.3](../models/glm-5-3.md) — Z.ai; supersedes GLM-5.2; same 753B/40B MoE footprint and 1M context, MIT license once weights land; large post-training-RL benchmark jump (+246 GDPval-AA v2, ties Kimi K3 on AA Intelligence Index) attributed to RL rather than scale *(as of 2026-08-20)*
- [DeepSeek V4](../models/deepseek-v4.md) — DeepSeek; released open-weight Pro/Flash MoE lineup with 1M context, MIT license; V4-Flash's 0731 post-training update jumped Terminal-Bench to 82.7 and AA Intelligence Index to 50 (1pt behind GPT-5.6 Luna) at $0.14/$0.28 per M tokens; V4 Pro reached GA 2026-08-13 at $0.435/$0.87 per M tokens (~57x cheaper than Fable 5 per Cline), +15.8% Terminal-Bench over its preview, mixed capability reception *(as of 2026-08-13)*
- **MAI-Code-1-Flash** — Microsoft; 5B active / 137B MoE; 51% SWE-Bench Pro; powers GitHub Copilot and VS Code; designed for high-throughput coding inference *(as of 2026-06-03)*
- **Meta Spark** — Meta; Arena (May 2026): leads coding category *(as of 2026-05-13)*

### Open-weight models

Broad foundation models whose main current-state question is open or open-ish weight availability, deployment control, and practical ecosystem support.

- [Inkling](../models/inkling.md) — Thinking Machines Lab; 975B/41B MoE flagship (Intelligence Index 41) plus a shipped Inkling-Small sibling (276B/12B, Index 40, ~1/4 the active footprint at near-flagship capability); natively multimodal (text/image/audio); Apache 2.0 *(as of 2026-07-31)*
- [Nemotron 3 Ultra](../models/nemotron-3-ultra.md) — NVIDIA; 550B/55B MoE; hybrid Mamba/attention + LatentMoE; 1M context; 300-400+ tok/s; OpenMDW 1.1; NVFP4 pretraining on 20T tokens; 47.7 Intelligence Index BF16 *(as of 2026-06-02)*
- [Nemotron 3.5 Lightning](../models/nemotron-35-lightning.md) — NVIDIA; 31.6B/3.6B active MoE; AA Intelligence Index 24, GDPval-AA v2 Elo 824, Terminal-Bench v2.1 24%; Harvey post-training took it 0%→8.3% on Legal Agent Bench, beating Opus 4.6 and Nemotron 3 Ultra; day-0 across Together AI, Ollama, Baseten, vLLM, Perplexity API *(as of 2026-08-12)*
- [DeepSeek V4](../models/deepseek-v4.md) — DeepSeek; MIT open-weight Pro/Flash lineup with 1M context; V4-Flash's 0731 update (post-training only, same 284B/13B architecture) reached AA Intelligence Index 50 and Terminal-Bench 82.7, day-0 vLLM support with DSpark speculative decoding; V4 Pro reached GA 2026-08-13 at $0.435/$0.87 pricing with a 15.8% Terminal-Bench gain over preview, mixed early capability reception *(as of 2026-08-13)*
- [Cohere Command A+](../models/cohere-command-a-plus.md) — Cohere; its first fully open (Apache 2.0) model; 218B/25B MoE; AA Intelligence Index 37 (~Claude 4.5 Haiku tier per AINews' summary of AA); AA reports strong non-hallucination behavior but weaker coding/science reasoning than top peers *(as of 2026-05-21)*
- [Kimi K3](../models/kimi-k3.md) — Moonshot AI; 2.8T params; Kimi Delta Attention; Intelligence Index 57 at $0.94/task; #1 Frontend Code Arena (1679 Elo, 76% win rate); open weights promised 2026-07-27 *(as of 2026-07-17)*
- [Laguna S 2.1](../models/laguna-s-2-1.md) — Poolside; 118B/8B-active MoE; OpenMDW-1.1 license; runs on a single DGX Spark; 70.2% Terminal-Bench 2.1, 78.5% SWE-bench Multilingual, 59.4% SWE-Bench Pro; cheaper than DeepSeek V4 Flash while beating V4 Pro *(as of 2026-07-23)*
- [Qwen 3.8](../models/qwen-3-8.md) — Alibaba; 2.4T/~95B-active MoE; #4 Frontend Code Arena (1,668 Elo); SWE-bench 87.3%, Terminal-Bench 2.1 67.4; open weights shipped 2026-08-13 (text-only initial drop, no vision), day-0 vLLM/Together/Baseten support; license reportedly restricts use in US/EU/UK/Korea *(as of 2026-08-13)*

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

- [2026-09-03] GPT-6 Astra launched (OpenAI): new flagship, but not a clean win — Fable 5.1 leads AA's coding-agent and intelligence indices, Astra leads token efficiency and cost-per-task; full rollout completed 2026-09-08; system card discloses a sharp CoT-monitorability decline.
- [2026-09-03] Muse Spark 1.3 launched: AA Intelligence Index #3 in the world, parity with GPT-5.6 Sol/Opus 5 on several evals, open weights still pending.
- [2026-09-01] Claude Fable 5.1 / Mythos 5.1 launched, superseding Fable 5: AA Intelligence Index 66 (was 62), 75% cache-read price cut, same-weights/different-safety-routing debate between the two paired model names.
- [2026-08-20] GLM-5.3 launched, superseding GLM-5.2: same 753B/40B MoE footprint and price, +246 GDPval-AA v2, ties Kimi K3 on AA Intelligence Index — gains attributed to post-training RL rather than scale.
- [2026-08-13] Grok 4.6 launched, superseding Grok 4.5: AA Intelligence Index 61, 88.4% Terminal-Bench v2.1, unchanged $2/$6 pricing; powers new Grok Bot AI-teammate product.
- [2026-08-13] Qwen3.8-Max shipped open weights (2.4T/~95B active MoE), text-only initial drop; day-0 vLLM/Together/Baseten support.
- [2026-08-13] DeepSeek V4 Pro reached general availability at $0.435/$0.87 pricing, +15.8% Terminal-Bench over preview; capability reception mixed versus Kimi/Flash.
- [2026-08-12] Nemotron 3.5 Lightning (NVIDIA, 31.6B/3.6B active) added to Open-weight models: AA Intelligence Index 24, strong per-size agentic benchmarks, Harvey's Legal Agent Bench post-training result beating Opus 4.6 and Nemotron 3 Ultra.
- [2026-08-04] Qwen3.8-Max (Alibaba, 2.4T/~95B active) added to Open-weight models: #4 Frontend Code Arena, SWE-bench 87.3%, Terminal-Bench 2.1 67.4; open weights promised for Max + a 27B sibling; license reportedly restricts use in US/EU/UK/Korea.
- [2026-07-31] Thinking Machines shipped Inkling-Small (276B/12B MoE, Intelligence Index 40), a near-flagship-capability sibling to Inkling at roughly a quarter the active footprint.
