---
type: proposal
sources:
  - raw/newsletters/2026-05-21-ainews-openai-gpt-next-disproves-80-year-old-erd.md
  - raw/newsletters/2026-05-23-ainews-all-model-labs-are-now-agent-labs.md
status: pending
created: 2026-08-25
---

# Proposal: Cohere Command A+ (fully open Apache 2.0) and Chinese frontier models close the price/capability gap

## Summary

Cohere released Command A+, its first fully open (Apache 2.0) model — a 218B/25B MoE scoring 37 on the Artificial Analysis Intelligence Index. Separately, DeepSeek made its 75% V4-Pro price discount permanent (now ~19x cheaper than Claude Opus 4.7 to run AA's Intelligence Index per-token), Qwen3.7-Max drew a positive third-party review for instruction-following/stability, and a single tweet-sourced ALE-Bench claim had several Chinese open models beating Western releases. Bundled into one "models landscape" proposal since both signals update the same open-weight/pricing narrative on `state-of/models.md` and `trends/open-weight-momentum-broadens.md`.

## Verification notes

- **Cohere Command A+:** Fetched Cohere's own announcement (`https://cohere.com/blog/command-a-plus`) directly — confirms 218B total/25B active MoE, Apache 2.0, 128K input/64K max generation context, 48 languages, AA Intelligence Index score of 37, and Cohere's own benchmark deltas over Command A Reasoning. The triage's "strong non-hallucination behavior but weaker coding/scientific reasoning" framing and the specific architecture claims (parallel transformer blocks, large shared-expert usage, LayerNorm over RMSNorm, 32 layers) are **not** in Cohere's own post — confirmed instead via the AINews newsletter, attributed there to Artificial Analysis and named ML community accounts (@eliebakouch, @rasbt) respectively. Both are included below with that attribution rather than presented as Cohere's own claims. No existing wiki page covers Cohere (confirmed via grep — the only wiki hits for "cohere" were coincidental uses of the English word "coherent").
- **DeepSeek V4-Pro pricing:** The AINews newsletter (2026-05-23) attributes exact figures to Artificial Analysis: $0.435/M input, $0.87/M output, $0.0036/M cached input, ~$0.18/M blended; ~3x/~12x/~19x cheaper than Gemini 3.1 Pro Preview/GPT-5.5/Claude Opus 4.7 respectively to run AA's Intelligence Index. I also fetched DeepSeek's **live** pricing page today (`https://api-docs.deepseek.com/quick_start/pricing`) to sanity-check this — it now shows a peak/off-peak, cache-hit/cache-miss pricing structure for `deepseek-v4-pro` ($0.66-$1.32/M input off-peak/peak on cache-miss, $1.98-$3.96/M output) that does not match the newsletter's flat figures. This means DeepSeek's pricing has been revised at least once more since the May 2026 "permanent" discount — I'm recording the newsletter's claim as a dated historical fact (attributed to that source/date) rather than presenting it as today's live price, and flagging the discrepancy in Open Questions.
- **Qwen3.7-Max review:** Sourced to a third-party review (@ZhihuFrontier, via AINews) — this is the same "Qwen3.7 Max Preview" already tracked on `models/qwen-3-7.md` (as_of 2026-05-19, from its own Arena-preview signal), so this update adds qualitative review commentary to the existing page rather than creating a new one. This is distinct from the "Qwen3.7 Reddit chatter" that the triage separately excluded as already-covered/thin.
- **ALE-Bench claim:** Sourced to a single tweet (@scaling01, via AINews) with the word "claimed" in the triage itself. Kept as a heavily caveated one-line mention in `trends/open-weight-momentum-broadens.md` only — not promoted to a benchmark page or a hard claim on any model page, per the "verify important claims" guidance for thin/single-tweet sourcing.
- **Cap check:** `wiki/state-of/models.md` and `wiki/trends/open-weight-momentum-broadens.md` both already have exactly 10 Recent-changes entries (at cap). Each gets exactly one combined new entry below, spilling its oldest entry to the corresponding `wiki/history/` file (both history files already exist; appending a new dated section, not reformatting existing content). `wiki/models/deepseek-v4.md` (2 entries) and `wiki/models/qwen-3-7.md` (1 entry) have headroom — no spill needed there.

## Intended changes

- [ ] **Create** `wiki/models/cohere-command-a-plus.md` — Cohere's first fully open model
- [ ] **Update** `wiki/models/deepseek-v4.md` — add permanent V4-Pro pricing discount, AA cost comparison, and a caveat that live pricing has since changed again
- [ ] **Update** `wiki/models/qwen-3-7.md` — add third-party review commentary on Qwen3.7-Max
- [ ] **Update** `wiki/state-of/models.md` — add Command A+ to "Open-weight models"; refresh DeepSeek V4 and Qwen 3.7 leader lines; one combined Recent-changes entry
- [ ] **Spill** `wiki/state-of/models.md` → `wiki/history/state-of/models.md` — oldest Recent-changes entry falls off
- [ ] **Update** `wiki/trends/open-weight-momentum-broadens.md` — add a bullet on Cohere's open Apache 2.0 entry and the China price/capability gap; one combined Recent-changes entry
- [ ] **Spill** `wiki/trends/open-weight-momentum-broadens.md` → `wiki/history/trends/open-weight-momentum-broadens.md` — oldest Recent-changes entry falls off
- [ ] **Create** `wiki/sources/articles/cohere-command-a-plus-launch.md` — source summary
- [ ] **Create** `wiki/sources/newsletters/ainews-erdos-cohere-2026-05-21.md` — source summary
- [ ] **Create** `wiki/sources/newsletters/ainews-all-model-labs-agent-labs-2026-05-23.md` — source summary

## Schema / vocabulary additions

- [ ] Add new tag `cohere` to `wiki/_schema/tags.md` — vendor/org: Cohere (needed for the new Command A+ model page)

## Page drafts

### wiki/models/cohere-command-a-plus.md (new)

```md
---
title: Cohere Command A+
type: model
domains: [models, agents]
subcategory: open-weight-model
tags: [cohere, open-weights]
as_of: 2026-05-21
sources: [cohere-command-a-plus-launch, ainews-erdos-cohere-2026-05-21]
---

# Cohere Command A+

Cohere's first fully open model release: Command A+ ships under an Apache 2.0 license, unifying and surpassing the prior Command A family (base, Reasoning, Vision, Translate) into one MoE model built for enterprise agentic workloads, born out of a year deploying Cohere's North workspace product.

## Current status (as of 2026-05-21)

- 218B total / 25B active MoE, 128K input context (64K max generation), text + image + tool-use input, 48 languages (up from 23 on prior Command A models)
- Runs on as little as 1x NVIDIA Blackwell GPU or 2x H100s at W4A4 quantization; ships in BF16/FP8/W4A4 on Hugging Face; day-0 vLLM support
- Artificial Analysis Intelligence Index: 37 — roughly Claude 4.5 Haiku territory; AA also reports especially strong non-hallucination behavior and decent speed, but weaker scientific reasoning and coding than top closed/open peers
- Cohere's own benchmarks show large gains over Command A Reasoning: 𝜏²-Bench Telecom 37% → 85%, Terminal-Bench Hard (agentic coding) 3% → 25%, MMMU 75.1%, MathVista 80.6%
- Community architecture analysis (unconfirmed by Cohere's own post): parallel transformer blocks, large shared-expert usage, LayerNorm over RMSNorm, and a comparatively shallow 32 layers

## Strengths

- Most permissively licensed frontier-adjacent release to date from a major closed-model lab — Apache 2.0, no usage restrictions
- Efficiency-first design: quantization support, a faster tokenizer (~20% fewer tokens for Arabic, ~16-18% for Korean/Japanese), and 47-63% throughput gains over Command A Reasoning depending on quantization
- Strong non-hallucination behavior per Artificial Analysis

## Weaknesses / caveats

- Intelligence Index of 37 trails the strongest open-weight coding/agent models tracked elsewhere in the wiki (GLM-5.2, Kimi K2.7-Code, DeepSeek V4)
- Weaker coding and scientific reasoning than top peers per AA
- Architecture details (parallel transformer blocks, LayerNorm, 32-layer depth) come from community analysis, not Cohere's own announcement

## Recent changes

- [2026-05-21] Command A+ released: 218B/25B MoE, Apache 2.0, 48 languages, AA Intelligence Index 37

## Sources

- [Introducing Command A+](../sources/articles/cohere-command-a-plus-launch.md)
- [AINews — Cohere Command A+ open release and architecture discussion](../sources/newsletters/ainews-erdos-cohere-2026-05-21.md)
```

### wiki/models/deepseek-v4.md (updated)

Frontmatter — bump `as_of` and add source:

```yaml
as_of: 2026-05-23
sources: [deepseek-v4-preview, ainews-2026-04-25, ainews-all-model-labs-agent-labs-2026-05-23]
```

Add to `## Current status`, after the existing pricing bullet:

```md
- **Permanent price cut (as of 2026-05-23):** DeepSeek made its previously-temporary 75% V4-Pro discount permanent. Artificial Analysis quantifies first-party pricing at $0.435/M input, $0.87/M output, $0.0036/M cached input — a blended ~$0.18/M — and estimates running AA's Intelligence Index on V4-Pro now costs ~3x less than Gemini 3.1 Pro Preview, ~12x less than GPT-5.5, and ~19x less than Claude Opus 4.7. **Caveat:** a direct check of DeepSeek's live pricing page on 2026-08-25 shows a different structure (peak/off-peak, cache-hit/cache-miss tiers) with higher current figures for V4-Pro — DeepSeek appears to have revised pricing again since May 2026; treat the figures above as a historical snapshot, not current pricing.
```

Add to `## Recent changes` (top, newest-first; no spill needed — page has 2 entries, goes to 3):

```md
## Recent changes

- [2026-05-23] DeepSeek made the 75% V4-Pro discount permanent; Artificial Analysis pricing/cost-per-Intelligence-Index comparison added. Live pricing re-checked 2026-08-25 shows a different (peak/off-peak) structure — pricing has moved again since.
- [2026-04-25] AINews follow-up reframed DeepSeek V4 from preview to release: Pro/Flash specs, MIT license, API pricing, independent open-model placement, Huawei Ascend compatibility, and token-volume caveats
- [2026-04-24] Preview released: DeepSeek moves its open-model story toward 1M-context agent workloads, hybrid attention for cheaper long traces, and stronger tool-use positioning
```

Add to `## Sources`:

```md
- [AINews — All model labs are now agent labs (DeepSeek V4-Pro permanent discount)](../sources/newsletters/ainews-all-model-labs-agent-labs-2026-05-23.md)
```

### wiki/models/qwen-3-7.md (updated)

Frontmatter — bump `as_of` and add source:

```yaml
as_of: 2026-05-23
sources: [qwen-3-7-arena-2026-05, ainews-all-model-labs-agent-labs-2026-05-23]
```

Add to `## Current status`:

```md
- **Third-party review (2026-05-23):** A long-form review (@ZhihuFrontier, via AINews) described Qwen3.7-Max as a meaningful step up over prior Qwen releases, especially in instruction following, context reliability, and stability — while still noting verbosity and high token usage.
```

Add to `## Recent changes`:

```md
## Recent changes

- [2026-05-23] Third-party review reinforces Qwen3.7-Max as a meaningful step up in instruction following and stability, with verbosity/token-usage still a weakness.
- [2026-05-19] Qwen3.7 Max Preview hits #13 overall Arena text; Qwen3.7 Plus Preview at #16 vision
```

Add to `## Sources`:

```md
- [AINews — All model labs are now agent labs (Qwen3.7-Max review)](../sources/newsletters/ainews-all-model-labs-agent-labs-2026-05-23.md)
```

### wiki/state-of/models.md (updated)

Frontmatter — add new source IDs:

```yaml
sources: [muse-spark, kimi-k2-6-blog, ainews-2026-04-21, ainews-2026-04-22, every-opus-4-7-vibe-check, vectorlab-opus-4-7-flop, vectorlab-qwen-3-6-local-threshold, open-agentic-coding-models, restricted-frontier-deployment, open-weight-momentum-early-april, late-march-small-coding-models, gpt-5-4-march, qwen-3-5-medium-february, glasswing, nano-banana-2-tweet, google-cloud-next-2026, openai-gpt-5-5-launch, danshipper-gpt-5-5-vibe-check, deepseek-v4-preview, ainews-2026-04-25, qwen-3-6-27b-aa-2026-05-01, open-weight-economics-fragmenting-2026-04-30, open-weight-pricing-pressure-2026-04-29, anthropic-spacex-dreams-2026-05-07, arena-leaderboard-2026-05-13, end-of-finetuning-debate-2026-05-13, thinking-machines-interaction-2026-05-12, gpt-5-5-instant-default-2026-05-06, qwen-3-7-arena-2026-05, fable-ban-june-2026, ainews-glm-52-june-2026, kimi-k27-code-june-2026, openai-economics-june-2026, ainews-fable5-june-2026, ainews-open-models-june-2026, every-fable5-vibe-check, ainews-cosmos-nemotron-june-2026, ainews-ideogram-june-2026, every-opus-48-june-2026, ainews-mai-build-june-2026, satya-nadella-no-priors-june-2026, ainews-june-05-2026, ainews-not-much-happened-2026-07-02, every-sonnet-5-vibe-check-2026-07-02, the-code-devin-security-2026-07-02, every-tale-of-two-models-2026-07-05, claude-sonnet-5-official-2026-06-30, gpt-56-sol-restricted-preview-2026-06, metr-gpt-5-6-sol-eval-2026-06, glm-52-frontier-adjacent-2026-06, open-weight-adoption-access-risk-2026-05, ainews-opus-48-dynamic-workflows-2026-05, outputmaxxing-amp-compute-utilization-2026-06, cohere-command-a-plus-launch, ainews-erdos-cohere-2026-05-21, ainews-all-model-labs-agent-labs-2026-05-23]
```

In `### Open-weight models`, add Command A+ (after the existing two entries):

```md
### Open-weight models

Broad foundation models whose main current-state question is open or open-ish weight availability, deployment control, and practical ecosystem support.

- [Nemotron 3 Ultra](../models/nemotron-3-ultra.md) — NVIDIA; 550B/55B MoE; hybrid Mamba/attention + LatentMoE; 1M context; 300-400+ tok/s; OpenMDW 1.1; NVFP4 pretraining on 20T tokens; 47.7 Intelligence Index BF16 *(as of 2026-06-02)*
- [DeepSeek V4](../models/deepseek-v4.md) — DeepSeek; MIT open-weight Pro/Flash lineup with 1M context and serious long-context agent infrastructure signal; V4-Pro's 75% price discount is now permanent, ~19x cheaper than Claude Opus 4.7 to run AA's Intelligence Index *(as of 2026-05-23)*
- [Cohere Command A+](../models/cohere-command-a-plus.md) — Cohere; its first fully open (Apache 2.0) model; 218B/25B MoE; AA Intelligence Index 37 (~Claude 4.5 Haiku tier); strong non-hallucination behavior but weaker coding/science reasoning than top peers *(as of 2026-05-21)*
```

In `### Coding models`, update the Qwen 3.7 line:

```md
- [Qwen 3.7](../models/qwen-3-7.md) — Alibaba; Qwen3.7 Max Preview at #13 overall Arena text (#7 Math, #9 Expert, #10 Coding); Alibaba now #6 lab in text by Arena; third-party review calls it a meaningful step up in instruction-following/stability, still verbose *(as of 2026-05-23)*
```

`## Recent changes` — add one combined entry at the top, and spill the oldest (last) entry to history:

```md
## Recent changes

- [2026-05-23] China closes the price/capability gap: DeepSeek made its V4-Pro 75% discount permanent (~19x cheaper than Opus 4.7 per AA Intelligence Index run); Qwen3.7-Max drew a positive third-party review on instruction-following/stability; a single-tweet ALE-Bench claim had Kimi-K2.6/DeepSeek-V4/GLM-5.1 beating several Western releases (unverified, see trend page). Cohere also shipped Command A+, its first fully open (Apache 2.0) model, added to Open-weight models.
- [2026-06-18] Outputmaxxing coverage adds compute-utilization nuance: frontier lab advantage depends on scheduling, MFU, power, and systems coordination, not only announced GPU capacity.
- [2026-05-29] Opus 4.8 launch coverage adds benchmark/pricing detail and positions Dynamic Workflows as the companion Claude Code systems feature.
- [2026-05-30] Open-weight adoption broadened operationally: AINews reports one in three AI teams ran open weights in April 2026, while access-risk coverage reframes local/open models as resilience infrastructure, not only cheaper alternatives.
- [2026-07-02] Fable 5 returned online with safety fallback routing; Sonnet 5 arrived as Anthropic's middle-tier Claude 5 model but early testing questioned its cost/performance positioning.
- [2026-06-23] GLM-5.2 follow-on coverage adds frontier-adjacent open-weight signal: strong AA-Briefcase cost/performance, broad hosted-provider adoption, and coding-agent harness uptake.
- [2026-06-30] Official Sonnet 5 launch details added: Claude Code/API availability, `claude-sonnet-5`, launch pricing, effort levels, and safety notes.
- [2026-06-29] Added caveated GPT-5.6/Sol restricted-preview note from newsletter coverage; official source capture still blocked.
- [2026-06-26] METR published its GPT-5.6 Sol predeployment evaluation, emphasizing high detected cheating and uncertainty rather than a clean capability estimate.
- [2026-06-17] OpenAI FY2025 leaked: $38.5B net loss, $13B revenue, below-50% ChatGPT market share; IPO S-1 filed; SemiAnalysis: $200/mo Claude Max costs Anthropic up to $8,000/mo compute; Scale 6% Report: only 6% of orgs at AI-at-scale stage
```

(the bottom entry — `[2026-06-17] Claude Fable 5 and Mythos 5 suspended globally under US government export controls...` — is spilled to history below)

### wiki/history/state-of/models.md (updated)

**Note:** this history file already has a `## Archived from current page on 2026-08-25` section at the top (from an earlier batch applied this morning). Append the new spilled line to the *end of that existing section* (immediately before the following `## Archived from current page on 2026-05-13` header) rather than creating a second same-dated header:

```md
## Archived from current page on 2026-08-25

- [2026-06-17] GLM-5.2 released (MIT, 744B/40B MoE, 1M context): #1 open Agent Arena, #2 Code Arena frontend, Terminal-Bench 2.1: 81.0; supersedes GLM-5.1 (archived to history/)
- [2026-06-13] Kimi K2.7-Code released: +21.8% Kimi Code Bench v2, 30% fewer reasoning tokens vs K2.6, open-source; K2.6 archived to history/
- [2026-06-11] DiffusionGemma released (Google, Apache 2.0): 26B MoE diffusion text model; block denoising; 4× faster than diffusion baselines; first diffusion LLM natively in vLLM; open research direction for non-autoregressive text generation
- [2026-06-05] Anthropic RSI: 80%+ code by Claude, 8x engineer throughput, task success 26% -> 76%; Mythos 52x speedup vs Opus 4 on training script task; S-1 confidentially filed with SEC

- [2026-04-10] Gemini adds custom interactive visualizations in chat and notebooks (dedicated workspaces with grouped chats, file uploads, instructions); rolling out to paid accounts first
- [2026-04-21] Added [Kimi K2.6](../models/kimi-k2-6.md) under new `Coding models` subcategory
- [2026-04-10] Added `frontier-model` subcategory with [Muse Spark](../../models/muse-spark.md)
- [2026-06-17] Claude Fable 5 and Mythos 5 suspended globally under US government export controls; Fable 5 had topped DeepSWE, FrontierSWE, FrontierMath, and Epoch Capabilities Index (161) before suspension; Claude Opus 4.8 remains the accessible Anthropic frontier model
## Archived from current page on 2026-05-13
```
(only the last bullet — the Fable 5/Mythos suspension line — is new; everything above it is the file's existing, unchanged content, reproduced here so the insertion point is unambiguous)

### wiki/trends/open-weight-momentum-broadens.md (updated)

Frontmatter — bump `as_of` and add sources:

```yaml
as_of: 2026-05-23
sources: [open-weight-momentum-early-april, deepseek-v4-preview, ainews-2026-04-25, china-open-agent-models-2026-04-28, local-offline-agents-2026-04-29, nvidia-nemotron-3-nano-omni-2026-04-29, open-weight-economics-fragmenting-2026-04-30, open-weight-pricing-pressure-2026-04-29, fable-ban-june-2026, ainews-glm-52-june-2026, ainews-open-models-june-2026, ainews-cosmos-nemotron-june-2026, local-ai-infrastructure-2026-06, open-weight-adoption-access-risk-2026-05, cohere-command-a-plus-launch, ainews-erdos-cohere-2026-05-21, ainews-all-model-labs-agent-labs-2026-05-23]
```

Add a new bullet under `## Current signal` (after the DeepSeek V4 bullet):

```md
- **Cohere Command A+ (May 2026)** is the clearest signal that fully open, permissively-licensed releases are no longer limited to Meta/Alibaba/DeepSeek/Z.ai — Cohere's first Apache 2.0 model (218B/25B MoE, AA Intelligence Index 37) extends open-weight competition to a lab that had previously kept its strongest models closed.
- **China's price/capability gap keeps narrowing (May 2026):** DeepSeek made its 75% V4-Pro discount permanent (AA: ~19x cheaper than Claude Opus 4.7 per Intelligence Index run); Qwen3.7-Max drew a positive third-party review on instruction-following/stability. A single-tweet ALE-Bench claim (unverified, one source) had Kimi-K2.6, DeepSeek-V4, and GLM-5.1 outperforming several Western releases in that setting — flagged here as a claim to watch, not a confirmed result.
```

`## Recent changes` — add one combined entry at the top, and spill the oldest (last) entry to history:

```md
## Recent changes

- [2026-05-23] China price/capability gap narrows further: DeepSeek's V4-Pro 75% discount made permanent (~19x cheaper than Opus 4.7 per AA Intelligence Index run); Qwen3.7-Max reviewed favorably on instruction-following/stability; unverified single-tweet ALE-Bench claim has several Chinese open models beating Western releases. Cohere Command A+ also extends fully-open (Apache 2.0) releases to a previously-closed lab.
- [2026-05-30] AINews reports open-weight usage at one in three AI teams in April 2026, up from one in five nine months earlier; access-risk framing strengthened by Claude Fable/Mythos suspension coverage.
- [2026-06-30] Local AI framing added: open-weight deployment is becoming a stack of models, search, documents, agents, harnesses, and hybrid routing rather than just running a checkpoint locally.
- [2026-06-02] Nemotron 3 Ultra (NVIDIA): 550B/55B hybrid Mamba/attention MoE; OpenMDW 1.1; 47.7 Intelligence Index; first significant NVIDIA open-weight model competing in the agentic frontier-model conversation
- [2026-06-11] Sarah Guo Agent Labs vs Model Labs framing: moat is "untrainable" integration work, not model capability; open-weight lag ~4 months; "intent is scarcer than compute"
- [2026-06-17] Fable 5 export-control ban accelerated model sovereignty framing: @hwchase17 argues model neutrality matters more than cloud neutrality; GLM-5.2 (MIT) adopted as the concrete alternative for teams losing closed frontier access
- [2026-05-05] Open-weight economics are fragmenting by deployment constraint: no single model dominates across transparency, token efficiency, edge deployment, coding benchmarks, and inference cost; Granite, Ant OSS Ling, and Hunyuan illustrate the divergence (secondary coverage; verify specifics)
- [2026-05-05] Open-weight competition is pressuring closed-frontier pricing for coding assistants and RAG workloads, while long-context and complex agentic tasks remain clearest closed-frontier advantages (editorial synthesis, The Code)
- [2026-05-05] NVIDIA Nemotron 3 Nano Omni described as an open multimodal model for agent perception across text/image/video/audio/documents; caveated — specs and benchmarks pending NVIDIA primary documentation
- [2026-05-05] Local/offline agent deployment is becoming practically accessible: browser-local agents, MLX on Apple Silicon, hardware-aware Hugging Face model selection, and Gemma tutorials all signal that capable offline agents are no longer only theoretical
```

(the bottom entry — `[2026-05-05] China-origin open-weight releases (Xiaomi MiMo-V2.5, Kimi K2.6, others) continue pressure...` — is spilled to history below)

Add to `## Sources`:

```md
- [Introducing Command A+](../sources/articles/cohere-command-a-plus-launch.md)
- [AINews — Cohere Command A+ open release and architecture discussion](../sources/newsletters/ainews-erdos-cohere-2026-05-21.md)
- [AINews — All model labs are now agent labs](../sources/newsletters/ainews-all-model-labs-agent-labs-2026-05-23.md)
```

### wiki/history/trends/open-weight-momentum-broadens.md (updated)

Append a new archived section at the top:

```md
# Open-Weight Momentum Broadens — History

## Archived from current page on 2026-08-25

- [2026-05-05] China-origin open-weight releases (Xiaomi MiMo-V2.5, Kimi K2.6, others) continue pressure across long context, agent tasks, open-ish licensing, and inference cost; do not apply model-specific benchmark numbers without primary source verification

## Archived from current page on 2026-05-19
```
(existing archived sections below are unchanged)

### wiki/sources/articles/cohere-command-a-plus-launch.md (new)

```md
---
title: Introducing Command A+ | Cohere
type: source
source_type: article
source_file: raw/articles/2026-08-25-coherecom-blog-command-a-plus.md
url: https://cohere.com/blog/command-a-plus
published: 2026-05-21
ingested: 2026-08-25
domains: [models]
---

# Introducing Command A+ | Cohere

Cohere's own announcement of Command A+, its first fully open (Apache 2.0) model, unifying the Command A family (base, Reasoning, Vision, Translate) into one 218B/25B-active MoE model for enterprise agentic workflows, born from a year of deploying North (Cohere's agentic enterprise workspace).

## Influenced pages

- [Cohere Command A+](../../models/cohere-command-a-plus.md) — new page
- [State of Models](../../state-of/models.md) — new Open-weight models entry
- [Open-weight momentum broadens](../../trends/open-weight-momentum-broadens.md) — new bullet on fully-open releases broadening beyond the usual labs

## Key claims extracted

- 218B total / 25B active MoE; Apache 2.0 license; 128K input context, 64K max generation; text/image/tool-use input; 48 languages
- Runs on 1x NVIDIA Blackwell GPU or 2x H100s at W4A4; BF16/FP8/W4A4 quantizations on Hugging Face; vLLM/Transformers support
- AA Intelligence Index score of 37, "outperforming other leading open models" per Cohere's framing of that specific benchmark
- Gains over Command A Reasoning: 𝜏²-Bench Telecom 37%→85%, Terminal-Bench Hard 3%→25%, MMMU 75.1%, MathVista 80.6%, CharXiv 52.7%
- Up to 63% higher output tokens/sec and 17% lower time-to-first-token vs Command A Reasoning at same quantization/concurrency; W4A4 adds another 47% speed / 13% latency improvement
- New tokenizer: ~20% fewer tokens for Arabic, ~16% Korean, ~18% Japanese vs predecessor
```

### wiki/sources/newsletters/ainews-erdos-cohere-2026-05-21.md (new)

```md
---
title: "AINews — OpenAI's Erdős disproof and Cohere Command A+"
type: source
source_type: newsletter
source_file: raw/newsletters/2026-05-21-ainews-openai-gpt-next-disproves-80-year-old-erd.md
url: https://www.latent.space/p/ainews-openai-gpt-next-disproves
published: 2026-05-21
ingested: 2026-08-25
domains: [models, agents]
---

# AINews — OpenAI's Erdős disproof and Cohere Command A+

AINews recap covering (separately) an OpenAI reasoning model's disproof of a long-standing Erdős unit-distance conjecture, and Cohere's Command A+ open release, plus new agent/memory/science benchmarks (InferenceBench, Terminal-Bench Science, MINTEval) and Google I/O follow-through coverage. Only the Command A+ section is used for this proposal; the OpenAI math item and benchmark cluster are separate, unrelated triage signals not part of this ingest.

## Influenced pages

- [Cohere Command A+](../../models/cohere-command-a-plus.md) — new page
- [State of Models](../../state-of/models.md) — new Open-weight models entry

## Key claims extracted

- Command A+ released as Apache 2.0 open weights; Cohere's first fully open Apache 2.0 model per Cohere co-founder @aidangomez
- ~218B MoE / 25B active, multimodal, 48 languages; runs on as little as 2x H100s at W4A4; vLLM day-0 support
- Artificial Analysis: Intelligence Index 37, "around Claude 4.5 Haiku territory," with especially strong non-hallucination behavior and decent speed but weaker scientific reasoning and coding than top peer models
- Community architecture discussion (not confirmed by Cohere): parallel transformer block, large shared-expert usage, LayerNorm over RMSNorm, 32-layer depth, atypical head/expert configuration
```

### wiki/sources/newsletters/ainews-all-model-labs-agent-labs-2026-05-23.md (new)

```md
---
title: "AINews — All model labs are now agent labs"
type: source
source_type: newsletter
source_file: raw/newsletters/2026-05-23-ainews-all-model-labs-are-now-agent-labs.md
url: https://www.latent.space/p/ainews-all-model-labs-are-now-agent
published: 2026-05-23
ingested: 2026-08-25
domains: [models, agents]
---

# AINews — All model labs are now agent labs

AINews recap centered on Greg Brockman's "the model alone is no longer the product," DeepSeek's permanent V4-Pro price cut, Qwen3.7-Max review commentary, an unverified ALE-Bench claim about Chinese open models, MCP's 2026-07-28 stateless release candidate, and sandboxes-as-primitives coverage (Gemini Managed Agents, CoreWeave Sandboxes, Cloudsail). Only the DeepSeek pricing and Qwen3.7-Max/ALE-Bench items are used for this proposal; the harness/MCP/sandbox material is a separate, already-otherwise-tracked signal cluster (see `concepts/agent-labs-vs-model-labs.md`, `concepts/mcp.md`) not part of this ingest.

## Influenced pages

- [DeepSeek V4](../../models/deepseek-v4.md) — permanent pricing update
- [Qwen 3.7](../../models/qwen-3-7.md) — third-party review addition
- [State of Models](../../state-of/models.md) — leader-line refresh
- [Open-weight momentum broadens](../../trends/open-weight-momentum-broadens.md) — China price/capability bullet

## Key claims extracted

- @deepseek_ai made the 75% DeepSeek-V4-Pro discount permanent; @ArtificialAnlys quantified first-party pricing at $0.435/M input, $0.87/M output, $0.0036/M cached input, ~$0.18/M blended; AA estimates running its Intelligence Index on V4-Pro costs ~3x less than Gemini 3.1 Pro Preview, ~12x less than GPT-5.5, ~19x less than Claude Opus 4.7
- A third-party review (@ZhihuFrontier) portrayed Qwen3.7-Max as a meaningful step up, especially in instruction following, context reliability, and stability, while still suffering from verbosity and high token usage
- @scaling01 claimed recent ALE-Bench runs show Chinese models (Kimi-K2.6, DeepSeek-V4, GLM-5.1) outperforming several Western releases in that setting — single-tweet sourcing, not independently verified
- Separately: Greg Brockman's "the model alone is no longer the product," AI21 shuttering its model team to pivot to agents, DeepSeek building its first "harness team," MCP's 2026-07-28 release candidate going stateless, and new managed-sandbox primitives (Gemini Managed Agents, CoreWeave Sandboxes, Cloudsail) — not used in this proposal, already tracked or better suited to other pages
```

## Open questions

- **DeepSeek pricing discrepancy:** the newsletter's "permanent" May 2026 discount figures ($0.435/$0.87 flat) don't match DeepSeek's live pricing page as checked today (peak/off-peak, cache-hit/miss tiers, higher headline numbers). I've recorded the May figures as a historical claim with a caveat rather than silently updating to today's live numbers (which would require its own dated ingest with a fresh source date). Should a follow-up proposal capture DeepSeek's current live pricing structure explicitly?
- **History file section dating:** `wiki/history/state-of/models.md` was already touched by an earlier batch applied this morning (2026-08-25) and already has a `## Archived from current page on 2026-08-25` section — the draft above appends into that existing section rather than duplicating the heading. `wiki/history/trends/open-weight-momentum-broadens.md` was **not** touched this morning (confirmed via `git status`), so a fresh `## Archived from current page on 2026-08-25` header there is correct as drafted. Please re-check both files' live state immediately before applying, since more proposals may land between now and then.
- **ALE-Bench:** left deliberately out of any model page and out of a new benchmark page given single-tweet sourcing — flag if you'd like it verified against a primary leaderboard before it's used anywhere more prominent.
