# State of Models — History

## Archived from current page on 2026-08-25

- [2026-06-17] GLM-5.2 released (MIT, 744B/40B MoE, 1M context): #1 open Agent Arena, #2 Code Arena frontend, Terminal-Bench 2.1: 81.0; supersedes GLM-5.1 (archived to history/)
- [2026-06-13] Kimi K2.7-Code released: +21.8% Kimi Code Bench v2, 30% fewer reasoning tokens vs K2.6, open-source; K2.6 archived to history/
- [2026-06-11] DiffusionGemma released (Google, Apache 2.0): 26B MoE diffusion text model; block denoising; 4× faster than diffusion baselines; first diffusion LLM natively in vLLM; open research direction for non-autoregressive text generation
- [2026-06-05] Anthropic RSI: 80%+ code by Claude, 8x engineer throughput, task success 26% -> 76%; Mythos 52x speedup vs Opus 4 on training script task; S-1 confidentially filed with SEC

- [2026-04-10] Gemini adds custom interactive visualizations in chat and notebooks (dedicated workspaces with grouped chats, file uploads, instructions); rolling out to paid accounts first
- [2026-04-21] Added [Kimi K2.6](../models/kimi-k2-6.md) under new `Coding models` subcategory
- [2026-04-10] Added `frontier-model` subcategory with [Muse Spark](../../models/muse-spark.md)
## Archived from current page on 2026-05-13

- [2026-04-23] Google Cloud Next '26: Gemini 3.1 Pro, Gemini 3.1 Flash Image, Gemma 4, Lyria 3, and Gemini Embedding 2 surfaced as Google's active platform model stack
- [2026-04-23] Added 'Specialized utility models' subcategory; [OpenAI Privacy Filter](../../models/openai-privacy-filter.md) is the first entry — on-device PII redaction, 1.5B MoE, Apache 2.0
- [2026-04-23] Added [Qwen 3.6 27B](../../models/qwen-3-6-27b.md) to Coding models; dense 27B beats prior 397B MoE on all coding benchmarks; day-0 open ecosystem support
- [2026-03-08] Added [GPT-5.4](../models/gpt-5-4.md) under `Frontier multimodal models`; strongest captured March signal for general-purpose reasoning, browsing, and agent work, with Claude still stronger on writing/taste
- [2026-03-23] Late-March small-model cluster sharpened the affordable coding tier: MiniMax M2.7 looks stronger on practical economics, while Composer 2 graduated from a Cursor-only mention to a real model with benchmark and lineage claims
- [2026-04-07] Early-April open-weight momentum broadened beyond coding-only releases: Gemma 4 became a notable open multimodal adoption signal; see [Open-weight momentum broadens](../../trends/open-weight-momentum-broadens.md)
- [2026-04-13] Added [MiniMax M2.7](../models/minimax-m2-7.md) and [GLM-5.1](../models/glm-5-1.md) under `Coding models`; earlier April sources show open coding-model momentum was broader than the later Qwen/Kimi cluster alone
- [2026-04-08] Mythos / Glasswing cluster suggests a new trend: frontier capability may increasingly be deployed selectively rather than broadly — see [Restricted frontier deployment](../../trends/restricted-frontier-deployment.md)
- [2026-04-21] Added [Qwen 3.6 35B-A3B](../../models/qwen-3-6-35b-a3b.md) under `Coding models`; practical local-agent baseline on 24GB-class hardware
- [2026-04-21] Anthropic/AWS: 5 GW compute secured, $5B investment, up to $20B more — see [Compute infrastructure as decisive competitive moat](../../trends/compute-infrastructure.md)
- [2026-04-21] Added [Claude Opus 4.7](../models/claude-opus-4-7.md) — #1 Vision & Document Arena
- [2026-04-22] Added `Image generation` subcategory; [GPT-Image-2](../../models/gpt-image-2.md) debuts as dominant arena leader by +242 Elo margin on text-to-image; also updates the image-as-spec pattern for coding agents
- [2026-04-22] Qwen 3.6 35B-A3B niche sharpened: strong for coding/tools, weaker for creative/translation; Qwen 3.6 Max Preview live but likely proprietary-only
- [2026-04-22] Kimi K2.6: community framing as practical Opus 4.7 replacement for ~85% of tasks
- [2026-04-22] Added `Security / cyber-offense capability` subcategory; [Claude Mythos Preview](../../models/claude-mythos-preview.md) confirms restricted-frontier pattern with autonomous zero-day discovery across major OSes/browsers
- [2026-04-22] Added [Nano Banana 2](../../models/nano-banana-2.md) to `Image generation` subcategory; Google enters the arena with Gemini+web-search-grounded image generation

## Archived from current page on 2026-05-19

- [2026-05-13] Arena leaderboard (May 2026): Claude Opus 4.7 "most consistently dominant" overall; Gemini 3.1 Pro close second/creative writing; Meta Spark leads coding; GPT-5.5 leads math; Grok 4.20 leads creative/hard prompts; GPT-Image-2 tops text-to-image; Veo 3.1 leads video
- [2026-05-07] Anthropic signs compute deal with SpaceX Colossus 1: 220K+ NVIDIA GPUs; doubled Claude Code limits on paid plans immediately; notable context: Musk vs. Altman court battle ongoing
- [2026-05-05] Open-weight economics fragmenting: no single model dominates across transparency, token efficiency, edge deployment, coding benchmarks, and inference cost; selection now driven by deployment constraint rather than a single ranking (editorial synthesis)
- [2026-05-05] Open-weight pricing pressure on closed-frontier for coding assistants and RAG; closed frontier retains clearer advantages in long-context and complex agentic tasks (editorial synthesis, The Code)
- [2026-05-01] Qwen 3.6 27B: Artificial Analysis (via AINews) confirms #1 ranking under 150B (Intelligence Index 46) but flags ~21× Gemma 4 31B output-token cost on the evaluation suite
- [2026-04-25] DeepSeek V4 moved from preview to release framing: Pro/Flash specs, MIT license, API pricing, independent open-model placement, Ascend compatibility, and token-usage caveats
- [2026-04-23] GPT-5.5 released; replaces GPT-5.4 as the current OpenAI frontier model in the wiki; OpenAI leads more public benchmark categories again, while Claude Opus 4.7 retains some important engineering/tool-use edges

## Archived from current page on 2026-07-08

- [2026-06-04] Ideogram 4.0: 9.3B DiT, #1 open image model (Arena #8 overall); fp8/nf4 checkpoints, ComfyUI; strong text rendering and branding capabilities
- [2026-06-03] Microsoft Build: MAI model family launched from scratch; MAI-Thinking-1 (35B/1T MoE, 97% AIME 2025, 53% SWE-Pro, blind human preference over Sonnet 4.6), MAI-Code-1-Flash (5B/137B, 51% SWE-Pro, in GitHub Copilot/VS Code)
- [2026-06-03] Claude Opus 4.8 released with Dynamic Workflows and Figma MCP bidirectional code-to-design/design-to-code workflows; Opus 4.7 archived
- [2026-06-02] MiniMax M3 launched: 59.0% SWE-Bench Pro, 66.0% Terminal Bench 2.1, 74.2% MCP Atlas; PostTrainBench #3; 1M context; "open-weight" claim contested because weights and parameter count were not disclosed at launch; supersedes M2.7
- [2026-06-02] Nemotron 3 Ultra released (NVIDIA): 550B/55B hybrid Mamba/attention MoE; OpenMDW 1.1; 47.7 Intelligence Index; high-throughput open-weight model signal
- [2026-06-02] NVIDIA Cosmos 3: Mixture-of-Transformers architecture (autoregressive reasoner + diffusion generator); Nano 16B / Super 64B; #1 open-weight Text2Image and Image2Video; full open release with Runway Cosmos Coalition
- [2026-05-19] Qwen 3.7 Arena preview: Qwen3.7 Max Preview #13 overall text (#7 Math, #9 Expert, #10 Coding); Qwen3.7 Plus Preview #16 vision; Alibaba reaches top-15 overall in text for the first time
- [2026-05-18] Claude Mythos Preview: Calif team defeated Apple M5 Memory Integrity Enforcement in <5 days — first public kernel memory corruption on M5; small team + frontier AI matches org-scale security research throughput
- [2026-05-13] Added merged `Real-time voice / interaction models` subcategory; TML-Interaction-Small (Thinking Machines Lab, 276B, 200ms audio, 0.4s response), GPT-Realtime-2, and Google Magic Pointer are first entries
- [2026-05-13] "End of finetuning" debate: OpenAI deprecating finetuning APIs; consensus forming that long-context prompts suffice for ~80% of use cases; counterpoint from top tier (Cursor, Cognition $25B) is increased open-model RLFT, not decreased — weight specialization remains central to their custom-ASIC strategy
- [2026-05-06] Secondary coverage says GPT-5.5 Instant became ChatGPT's new default model, replacing GPT-5.3 Instant; official verification still needed for exact rollout and hallucination claims.
