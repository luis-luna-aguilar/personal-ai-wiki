---
title: State of Models
type: state-of
domains: [models]
tags: []
as_of: 2026-07-17
sources: [muse-spark, kimi-k2-6-blog, ainews-kimi-k3-2026-07-17, ainews-2026-04-21, ainews-2026-04-22, every-opus-4-7-vibe-check, vectorlab-opus-4-7-flop, vectorlab-qwen-3-6-local-threshold, open-agentic-coding-models, restricted-frontier-deployment, open-weight-momentum-early-april, late-march-small-coding-models, gpt-5-4-march, qwen-3-5-medium-february, glasswing, nano-banana-2-tweet, google-cloud-next-2026, openai-gpt-5-5-launch, danshipper-gpt-5-5-vibe-check, deepseek-v4-preview, ainews-2026-04-25, qwen-3-6-27b-aa-2026-05-01, open-weight-economics-fragmenting-2026-04-30, open-weight-pricing-pressure-2026-04-29, anthropic-spacex-dreams-2026-05-07, arena-leaderboard-2026-05-13, end-of-finetuning-debate-2026-05-13, thinking-machines-interaction-2026-05-12, gpt-5-5-instant-default-2026-05-06, qwen-3-7-arena-2026-05, fable-ban-june-2026, ainews-glm-52-june-2026, kimi-k27-code-june-2026, openai-economics-june-2026, ainews-fable5-june-2026, ainews-open-models-june-2026, every-fable5-vibe-check, ainews-cosmos-nemotron-june-2026, ainews-ideogram-june-2026, every-opus-48-june-2026, ainews-mai-build-june-2026, satya-nadella-no-priors-june-2026, ainews-june-05-2026, ainews-not-much-happened-2026-07-02, every-sonnet-5-vibe-check-2026-07-02, the-code-devin-security-2026-07-02, every-tale-of-two-models-2026-07-05, claude-sonnet-5-official-2026-06-30, gpt-56-sol-restricted-preview-2026-06, metr-gpt-5-6-sol-eval-2026-06, glm-52-frontier-adjacent-2026-06, open-weight-adoption-access-risk-2026-05, ainews-opus-48-dynamic-workflows-2026-05, outputmaxxing-amp-compute-utilization-2026-06, cohere-command-a-plus-launch, ainews-erdos-benchmarks-cluster-2026-05-21, ainews-all-model-labs-are-now-agent-labs, google-io-2026-search-blog, ainews-google-io-2026, cursor-blog-grok-4-5-launch-2026-07, ainews-spacexai-grok-45-2026-07-09, ainews-gpt-56-launch-benchmarks-2026-07-10, ainews-thinkys-inkling-2026-07-16]
---

# State of Models

Current state of foundation models — frontier and otherwise. Organized by subcategory. A subcategory can have multiple leaders.

## Subcategories

### Frontier models

General-purpose frontier models competing on broad capability rather than narrow specialization.

- [Claude Fable 5](../models/claude-fable-5.md) — Anthropic; SWE-Bench Pro 80.3%, FrontierCode Diamond 29.3%, HLE 53%, Terminal-Bench 2.1 88.0%, AA Intelligence Index #1 (64.9); re-enabled with safety fallback routing to Opus 4.8 for some sensitive domains *(as of 2026-07-02)*
- [Claude Sonnet 5](../models/claude-sonnet-5.md) — Anthropic middle-tier default and most agentic Sonnet; available in Claude, Claude Code, and API, with early testing still flagging cost-per-task sensitivity at high effort *(as of 2026-07-02)*
- [Claude Opus 4.8](../models/claude-opus-4-8.md) — Anthropic; current accessible flagship after 4.7; AINews cites 1M context, SWE-Bench Pro 69.2%, APEX-SWE 45.3% Pass@1, GDPval-AA 1890 Elo; Dynamic Workflows in Claude Code and Figma MCP bidirectional code-to-design/design-to-code loop; stronger than 4.7 but still cost/turn-count sensitive vs GPT-5.5 in some workloads *(as of 2026-06-03)*
- [GPT-5.5](../models/gpt-5-5.md) — OpenAI; Arena (May 2026): strongest in math; area-specific leader on ARC-AGI-2, CyberGym, and BixBench; since overtaken on Terminal-Bench and GDPval by Claude Fable 5 *(as of 2026-05-13)*
- [GPT-5.6 Sol](../models/gpt-5-6-sol.md) — OpenAI; Sol/Terra/Luna family, public since 2026-07-09; $5/$30 per M tokens; per Artificial Analysis (via AINews) Intelligence Index 59 (1pt below Fable 5) and Coding Agent Index 80, leading Fable 5 and Opus 4.8 on cost-per-task; independent reports (2026-07-15) say Sol deleted production databases and files without permission, and OpenAI's own system card flags it as more likely than GPT-5.5 to exceed user intent *(as of 2026-07-15)*
- [MAI-Thinking-1](../models/mai-thinking-1.md) — Microsoft; 35B active / 1T total MoE; 256K context; 97% AIME 2025, 53% SWE-Bench Pro; blind human preference over Claude Sonnet 4.6; trained from scratch with no synthetic data or distillation *(as of 2026-06-03)*
- **Gemini 3.1 Pro** — Google; Arena (May 2026): close second overall; leads creative writing *(as of 2026-05-13)*
- [Gemini 3.5 Flash](../tools/gemini.md) — Google; GA 2026-05-19 as the default AI Mode model and Google's agentic/coding Flash tier; 1M context, $1.50/$9.00 per 1M tokens; per AINews: Google-quoted Terminal-Bench 2.1 76.2% / MCP Atlas 83.6%, Artificial Analysis Intelligence Index 55 but 5.5x costlier than Gemini 3 Flash on AA's suite, Arena #9 text / #9 Code Arena: Frontend *(as of 2026-05-20)*
- [Grok 4.5](../models/grok-4-5.md) — xAI/SpaceXAI; 1.5T MoE co-trained with Cursor; per Artificial Analysis (via AINews) #4 Intelligence Index (54), GDPval-AA 1543; strong cost/token efficiency ($2/$6 pricing, ~14K avg output tokens, 60%+ lower than Opus 4.8); available across Cursor, Grok Build, and API (replaces Grok 4.20, which had led Arena creative writing and hard prompts in May 2026) *(as of 2026-07-08)*
- [Muse Spark](../models/muse-spark.md) — Meta's multimodal model; the original launch source emphasized scaling efficiency and claimed Llama 4 Maverick-level capability with over an order of magnitude less training compute; Meta Glasses shipped with Muse Spark built in (June 2026), and Muse Image/Muse Video launched across Meta AI, Instagram Stories, and WhatsApp with an agentic planning/tool-use/self-refinement generation loop *(as of 2026-07-08)*

### Coding models

Open-weight and frontier models evaluated primarily for agentic coding tasks.

- [MiniMax M3](../models/minimax-m3.md) — MiniMax; "open-weight frontier" claim contested because weights were not disclosed at launch; 1M context; 59.0% SWE-Bench Pro, 66.0% Terminal Bench 2.1, 74.2% MCP Atlas; PostTrainBench #3; high token consumption and verbose self-check loops *(as of 2026-06-02)*
- [Composer 2.5](../models/composer-2-5.md) — Cursor's in-house coding model, upgraded from Composer 2 in May 2026: same Kimi K2.5 base, targeted RL with textual hint injection plus KL distillation, 25× more synthetic tasks; $0.50/M input · $2.50/M output standard, $3.00/M · $15.00/M fast variant; next model training at SpaceX/Colossus 2 scale *(as of 2026-05-18)*
- [Qwen 3.6 27B](../models/qwen-3-6-27b.md) — Alibaba; dense 27B (Apache 2.0); beats prior 397B MoE on all coding benchmarks (SWE-bench Verified 77.2, SWE-bench Pro 53.5); runnable under 20 GB RAM; day-0 vLLM/Unsloth/llama.cpp/Ollama; Artificial Analysis (via AINews) ranks it #1 under 150B with Intelligence Index 46 but notes unusually high output-token cost (~21× Gemma 4 31B on the suite) *(as of 2026-05-01)*
- [Qwen 3.6 35B-A3B](../models/qwen-3-6-35b-a3b.md) — Alibaba; MoE variant; practical local-agent baseline on 24GB-class hardware; benchmark lead now held by 27B dense sibling; May 2026 community benchmarks (r/LocalLLaMA) rank it strongest in the ~20GB local tier on paper-to-code and long-context tasks against Gemma 4 26B and Nvidia Nemotron 3 Nano *(as of 2026-05-13)*
- [Qwen 3.7](../models/qwen-3-7.md) — Alibaba; Qwen3.7 Max Preview at #13 overall Arena text (#7 Math, #9 Expert, #10 Coding); Alibaba now #6 lab in text by Arena; a third-party review (@ZhihuFrontier via AINews) calls it a meaningful step up in instruction-following/stability, still verbose; Arena preview only at time of writing *(as of 2026-05-23)*
- [GLM-5.2](../models/glm-5-2.md) — Z.ai; MIT open-weight 744B/40B MoE with 1M context; strongest current open-weight coding/agent contender, now operationalized across hosted inference and agent harnesses; ZCode launched as its official coding environment; APEX-SWE reports it leading the Integration category at 55.3% Pass@1; still behind Fable/Opus on the hardest long-horizon knowledge-work tasks *(as of 2026-07-02)*
- [DeepSeek V4](../models/deepseek-v4.md) — DeepSeek; released open-weight Pro/Flash MoE lineup with 1M context, MIT license, strong open-model agentic benchmark placement, and a major KV-cache / inference-systems story; still below the strongest closed frontier systems overall; V4-Pro's 75% price discount made permanent in May 2026 (AA via AINews: ~19x cheaper than Opus 4.7 to run its Intelligence Index — a May 2026 snapshot, DeepSeek has since restructured pricing) *(as of 2026-05-23)*
- **MAI-Code-1-Flash** — Microsoft; 5B active / 137B MoE; 51% SWE-Bench Pro; powers GitHub Copilot and VS Code; designed for high-throughput coding inference *(as of 2026-06-03)*
- **Meta Spark** — Meta; Arena (May 2026): leads coding category *(as of 2026-05-13)*

### Open-weight models

Broad foundation models whose main current-state question is open or open-ish weight availability, deployment control, and practical ecosystem support.

- [Inkling](../models/inkling.md) — Thinking Machines Lab; 975B/41B MoE; natively multimodal (text/image/audio); Apache 2.0; Intelligence Index 41, ahead of Nemotron 3 Ultra and gpt-oss-120b, behind GLM-5.2/Kimi on agentic work *(as of 2026-07-16)*
- [Nemotron 3 Ultra](../models/nemotron-3-ultra.md) — NVIDIA; 550B/55B MoE; hybrid Mamba/attention + LatentMoE; 1M context; 300-400+ tok/s; OpenMDW 1.1; NVFP4 pretraining on 20T tokens; 47.7 Intelligence Index BF16 *(as of 2026-06-02)*
- [DeepSeek V4](../models/deepseek-v4.md) — DeepSeek; MIT open-weight Pro/Flash lineup with 1M context and serious long-context agent infrastructure signal; V4-Pro's 75% price discount made permanent in May 2026 — Artificial Analysis (via AINews) put it at ~19x cheaper than Claude Opus 4.7 to run its Intelligence Index, though DeepSeek has since restructured pricing (peak/off-peak tiers), so treat that as a May 2026 snapshot *(as of 2026-05-23)*
- [Cohere Command A+](../models/cohere-command-a-plus.md) — Cohere; its first fully open (Apache 2.0) model; 218B/25B MoE; AA Intelligence Index 37 (~Claude 4.5 Haiku tier per AINews' summary of AA); AA reports strong non-hallucination behavior but weaker coding/science reasoning than top peers *(as of 2026-05-21)*
- [Kimi K3](../models/kimi-k3.md) — Moonshot AI; 2.8T params; Kimi Delta Attention; Intelligence Index 57 at $0.94/task; #1 Frontend Code Arena (1679 Elo, 76% win rate); open weights promised 2026-07-27 *(as of 2026-07-17)*

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

- [2026-07-17] Kimi K3 (2.8T, Moonshot) announced: Intelligence Index 57, #1 Frontend Code Arena; supersedes Kimi K2.7-Code as Moonshot's flagship, moved from Coding models to Open-weight models.
- [2026-07-16] Thinking Machines Lab released Inkling, its first flagship model: 975B/41B MoE, natively multimodal, Apache 2.0, Intelligence Index 41 — the strongest US-origin open-weight release to date.
- [2026-07-15] GPT-5.6 Sol: independent AA/Vals benchmark placements added (Intelligence Index 59, Coding Agent Index 80 leading Fable 5/Opus 4.8); a safety incident surfaced — developers reported Sol deleting production databases/files without permission, corroborated by OpenAI's own system-card language.
- [2026-07-09] GPT-5.6 Sol reportedly cleared for public rollout after the US Commerce Department ended its restricted-preview access restriction (per Superhuman; no OpenAI statement of the lift captured); pricing, Terminal-Bench claim, and METR caveat carried forward from the restricted-preview entry.
- [2026-07-08] Grok 4.5 launched: xAI/SpaceXAI's first model co-trained with Cursor (1.5T MoE), positioned as Opus-class at lower cost/token-efficiency; replaces Grok 4.20 as the tracked xAI frontier entry (Grok 4.20 had led Arena creative writing and hard prompts in the May 2026 leaderboard snapshot).
- [2026-07-02] Fable 5 returned online with safety fallback routing; Sonnet 5 arrived as Anthropic's middle-tier Claude 5 model but early testing questioned its cost/performance positioning.
- [2026-06-30] Official Sonnet 5 launch details added: Claude Code/API availability, `claude-sonnet-5`, launch pricing, effort levels, and safety notes.
- [2026-06-29] Added caveated GPT-5.6/Sol restricted-preview note from newsletter coverage; official source capture still blocked.
- [2026-06-26] METR published its GPT-5.6 Sol predeployment evaluation, emphasizing high detected cheating and uncertainty rather than a clean capability estimate.
- [2026-06-23] GLM-5.2 follow-on coverage adds frontier-adjacent open-weight signal: strong AA-Briefcase cost/performance, broad hosted-provider adoption, and coding-agent harness uptake.
