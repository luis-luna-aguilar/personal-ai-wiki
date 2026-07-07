---
type: proposal
sources:
  - raw/newsletters/2026-06-05-ainews-not-much-happened-today.md
  - raw/newsletters/2026-06-02-ainews-nvidia-cosmos-3-nemotron-3-ultra-and-rt.md
status: pending
created: 2026-06-24
---

# Proposal: Anthropic RSI productivity claims + S-1 filed

## Summary

Anthropic's RSI (Responsible Scaling Intelligence) disclosure: Claude now writes 80%+ of Anthropic's merged code, engineers ship 8× more code per quarter, internal task success improved from 26%→76% in 6 months, and Mythos Preview achieved a 52× speedup on training script optimization (vs 3× for Claude Opus 4). Separately, Anthropic filed a confidential S-1 with the SEC. Arena Agent Arena debut: GPT-5.5 #1, Claude Opus 4.7 #2, GLM-5.1 #3, Gemini 3.1 Pro #4.

## Intended changes

- [x] **Update** `wiki/state-of/models.md` — add RSI productivity data to AI economics snapshot; add Arena Agent Arena results to relevant entries; add Recent changes entry
    > **Add to `## AI economics snapshot` section (new bullet):**
    > `- **Anthropic RSI (June 2026):** Claude writes 80%+ of Anthropic's merged code; engineers ship 8× more code/quarter; internal task success 26%→76% in 6 months; Mythos Preview: 52× speedup on training script optimization vs Claude Opus 4 baseline (~3×); Mythos gave better "next step" suggestions than humans 64% of time`
    >
    > **Add to Recent changes:**
    > `- [2026-06-05] Anthropic RSI: 80%+ code by Claude, 8× engineer throughput, task success 26%→76%; Mythos 52× speedup vs Opus 4 on training script task; S-1 confidentially filed with SEC`
    >
    > **Add to Arena Agent Arena note in frontier multimodal section (or update Claude Opus 4.7 line):**
    > Currently: `- [Claude Opus 4.7](../models/claude-opus-4-7.md) — Anthropic flagship; Arena (May 2026): "most consistently dominant model," leads nearly every category *(as of 2026-05-13)*`
    > Add note: `*(as of 2026-05-13); Arena Agent Arena debut (June 2026): #2 behind GPT-5.5*`

- [x] **Update** `wiki/training/ai-enablement-software-development.md` — add Anthropic internal RSI data as evidence
    > **Add to `## Evidence from practice` section (or create if not present):**
    >
    > - **Anthropic internal RSI data (June 2026):** The strongest first-party self-reported numbers from a frontier lab. Claude writes 80%+ of Anthropic's merged code commits. Engineers report shipping 8× more code per quarter than pre-Claude. Internal automated task success rate improved from 26% → 76% over 6 months of harness iteration. Mythos Preview (the restricted Anthropic model) achieved a 52× speedup on a training script optimization task vs. 3× for Claude Opus 4 on the same task. Mythos gave better "next step" suggestions than humans 64% of the time. Caveat: self-reported, no independent verification.
    >
    > **Update frontmatter sources:** add `ainews-june-05-2026`

- [ ] **Create** `wiki/sources/newsletters/ainews-june-05-2026.md` — source summary for June 5 AINews newsletter
    > See draft below

## Page drafts

### wiki/sources/newsletters/ainews-june-05-2026.md (new)

````md
---
title: AINews — Anthropic RSI, Arena Agent Arena debut, Nemotron follow-up (June 5)
type: source
source_type: newsletter
source_file: raw/newsletters/2026-06-05-ainews-not-much-happened-today.md
published: 2026-06-05
ingested: 2026-06-24
domains: [models, agents, coding]
---

# AINews — Anthropic RSI, Arena Agent Arena debut, Nemotron follow-up (June 5)

AINews covering Anthropic's RSI disclosure; Arena Agent Arena debut leaderboard; Nemotron 3 Ultra architecture clarification (NVFP4, 20T tokens); Ideogram 4.0 open weights; Sakana AI RSI Lab launch.

## Influenced pages

- [State of Models](../../state-of/models.md) — RSI data, Arena Agent Arena results
- [AI enablement — software development](../../training/ai-enablement-software-development.md) — RSI evidence from practice

## Key claims extracted

- Anthropic RSI: 80%+ merged code by Claude; 8× engineer code/quarter; task success 26%→76% in 6 months
- Mythos Preview: 52× speedup on training script optimization vs Claude Opus 4 (~3×); better "next step" suggestions than humans 64% of time
- Arena Agent Arena debut: GPT-5.5 #1, Claude Opus 4.7 #2, GLM-5.1 #3, Gemini 3.1 Pro #4, Kimi-K2.6 #5; 300K+ tasks, 2M+ tool calls, 40M lines of code evaluated
- Nemotron 3 Ultra: NVFP4 pretraining on 20T tokens; 47.7 Intelligence Index BF16
- Ideogram 4.0: 9.3B DiT, fp8/nf4 checkpoints, ComfyUI support, Qwen3-VL text encoding
- Sakana AI RSI Lab launched in Tokyo
- Cloudflare AI Gateway: spend limits by model/user, fallbacks
- Anthropic doubled Claude Cowork usage limits
````

## Feedback
- Lets skip the agent arena stuff. Not relevant anymore.