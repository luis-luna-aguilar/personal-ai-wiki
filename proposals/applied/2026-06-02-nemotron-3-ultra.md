---
type: proposal
source: raw/newsletters/2026-06-02-ainews-nvidia-cosmos-3-nemotron-3-ultra-and-rt.md
status: pending
created: 2026-06-24
---

# Proposal: NVIDIA Nemotron 3 Ultra

## Summary

NVIDIA launched Nemotron 3 Ultra at Computex 2026 — a 550B/55B MoE model with a hybrid Mamba/attention + LatentMoE architecture, 1M context, and 300–400+ tok/s serving speed. It claims the top US open-weight Intelligence Index score (47.7) and placed #3 on Arena Agent Arena.

## Intended changes

- [x] **Create** `wiki/models/nemotron-3-ultra.md` — new model page
    > See draft below

- [ ] **Update** `wiki/state-of/models.md` — add Nemotron 3 Ultra to the Coding models section; add Recent changes entry
    > **Add to coding models section:**
    > `- [Nemotron 3 Ultra](../models/nemotron-3-ultra.md) — NVIDIA; 550B/55B MoE; hybrid Mamba/attention + LatentMoE; 1M context; 300–400+ tok/s; OpenMDW 1.1; 47.7 Intelligence Index BF16; #3 Arena Agent Arena *(as of 2026-06-02)*`
    >
    > **Add to Recent changes:**
    > `- [2026-06-02] Nemotron 3 Ultra released (NVIDIA): 550B/55B MoE, hybrid Mamba/attention + LatentMoE + MTP; 1M context; 300-400+ tok/s; 47.7 Intelligence Index — top US open-weight; #3 Arena Agent Arena; OpenMDW 1.1 license`

- [x] **Update** `wiki/trends/open-weight-momentum-broadens.md` — add Nemotron 3 Ultra as latest open-weight signal; add Recent changes entry
    > **Add to Current signal section (after GLM-5.2 mention or as new bullet):**
    > `- **Nemotron 3 Ultra** is the clearest US-origin open-weight signal in the June 2026 period: hybrid Mamba/attention + LatentMoE architecture, OpenMDW 1.1, 300–400+ tok/s serving, and #3 Arena Agent Arena placement confirm NVIDIA as a new first-party open-weight competitor alongside Meta and Alibaba.`
    >
    > **Add to Recent changes:**
    > `- [2026-06-02] Nemotron 3 Ultra (NVIDIA): 550B/55B hybrid Mamba/attention MoE; OpenMDW 1.1; #3 Arena Agent Arena; 47.7 Intelligence Index — first significant NVIDIA open-weight model competing on agent benchmarks`

- [x] **Create** `wiki/sources/newsletters/ainews-cosmos-nemotron-june-2026.md` — source summary for the June 2 AINews newsletter (also covers Cosmos 3 and MiniMax M3)
    > See draft below

## Page drafts

### wiki/models/nemotron-3-ultra.md (new)

````md
---
title: Nemotron 3 Ultra
type: model
domains: [models, coding]
subcategory: coding-model
tags: [nvidia, open-weights, agentic]
as_of: 2026-06-02
sources: [ainews-cosmos-nemotron-june-2026]
---

# Nemotron 3 Ultra

NVIDIA's first-party frontier open-weight model, released at Computex 2026. A 550B total / 55B active MoE with a novel hybrid Mamba/attention + LatentMoE + native Multi-Token Prediction architecture, positioned for long-context agentic inference at high serving throughput.

## Current status (as of 2026-06-02)

- 550B total / ~55B active parameters (~10% active weight ratio — less sparse than Kimi K2 / DeepSeek V4 at ~3%)
- Hybrid Mamba/attention + LatentMoE + native MTP (Multi-Token Prediction)
- 1M context window
- 300–400+ tokens/second serving speed
- NVFP4 pretraining on 20T tokens
- 47.7 Intelligence Index (BF16) — claimed top US open-weight model at launch
- **OpenMDW 1.1** license (permissive open-model license)
- #3 Arena Agent Arena (June 2026; behind GPT-5.5 #1 and Claude Opus 4.7 #2)
- Day-0: OpenRouter, vLLM support

## Strengths

- Unusually high serving throughput for a model at this scale — 300-400+ tok/s makes long-context agent loops practically affordable
- First NVIDIA-origin open-weight model competing directly on agent benchmarks
- ~10% active weight ratio is higher than DeepSeek/Kimi MoEs, which may improve practical routing quality at the cost of slightly higher compute-per-token

## Weaknesses / caveats

- 10% active weight is less sparse than leading MoEs, meaning higher cost per token in inference than K2/DeepSeek at comparable total-param scale
- OpenMDW 1.1 license — less permissive than MIT; check enterprise use terms before deployment
- Claims are from NVIDIA's own launch materials; independent third-party benchmarks pending

## Recent changes

- [2026-06-02] Launched at Computex 2026; initial benchmarks and placement

## Sources

- [AINews — NVIDIA Cosmos 3, Nemotron 3 Ultra (June 2)](../../sources/newsletters/ainews-cosmos-nemotron-june-2026.md)
````

### wiki/sources/newsletters/ainews-cosmos-nemotron-june-2026.md (new)

````md
---
title: AINews — NVIDIA Cosmos 3, Nemotron 3 Ultra, and MiniMax M3 (June 2)
type: source
source_type: newsletter
source_file: raw/newsletters/2026-06-02-ainews-nvidia-cosmos-3-nemotron-3-ultra-and-rt.md
published: 2026-06-02
ingested: 2026-06-24
domains: [models, creative]
---

# AINews — NVIDIA Cosmos 3, Nemotron 3 Ultra, and MiniMax M3 (June 2)

AINews newsletter covering three major open-weight releases at Computex 2026: NVIDIA Cosmos 3 (Mixture-of-Transformers world model), NVIDIA Nemotron 3 Ultra (550B/55B MoE frontier LLM), and MiniMax M3 (claimed open-weight frontier with contested weight disclosure). Also noted: Anthropic S-1 filed confidentially with SEC; Claude Code rate-limit incident (Opus 4.8 spawned too many parallel subagents).

## Influenced pages

- [Nemotron 3 Ultra](../../models/nemotron-3-ultra.md) — new page
- [NVIDIA Cosmos 3](../../models/cosmos-3.md) — new page (see cosmos-3-ideogram-4 proposal)
- [MiniMax M3](../../models/minimax-m3.md) — new page (see minimax-m3 proposal)
- [State of Models](../../state-of/models.md) — coding models section updated
- [Open-weight momentum broadens](../../trends/open-weight-momentum-broadens.md) — new entry

## Key claims extracted

- Nemotron 3 Ultra: 550B/55B MoE, hybrid Mamba/attention + LatentMoE + MTP; 1M context; 300-400+ tok/s; 47.7 Intelligence Index; #3 Arena Agent Arena; OpenMDW 1.1
- Cosmos 3: Mixture-of-Transformers (autoregressive + diffusion); Nano 16B (8B+8B), Super 64B; #1 open-weight Text-to-Image and Image-to-Video; Cosmos Coalition with Runway; full weights/code/data released
- MiniMax M3: "open-weight frontier" claim; 1M context; 59.0% SWE-Bench Pro, 66.0% Terminal Bench 2.1, 74.2% MCP Atlas; PostTrainBench #3; BUT weights and parameter count NOT disclosed at launch
- Anthropic S-1: confidentially filed with SEC
- Claude Code incident: Opus 4.8 spawned excess parallel subagents, triggering rate limits
````

## Open questions

- Nemotron 3 Ultra uses OpenMDW 1.1 — is this subcategory `coding-model` appropriate, or should there be a separate `open-weight-frontier` subcategory?
	- I dont think this is a coding model. Mixture of Experts usually are not coding models. We should just put it in open-weight, theres no need to split it into frontier models, thats a temporal characteristic.
- Should this model be placed under "Architecture experiments" instead of "Coding models" given the novel Mamba/attention hybrid?
	- Lets just put it into open-weight models.
