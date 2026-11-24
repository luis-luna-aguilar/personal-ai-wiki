---
type: proposal
source: raw/newsletters/2026-10-20-ainews-not-much-happened-today.md
sources:
  - raw/newsletters/2026-10-20-ainews-not-much-happened-today.md
  - raw/newsletters/2026-10-15-ainews-modals-1b-arr-16b-series-d-makes-it-n.md
triage: proposals/triage/2026-10-11-to-2026-10-20-ai-digest.md
status: pending
created: 2026-10-20
---

# Proposal: DeepSeek V4.1 Flash 1017, MiniMax M3.1 Flash, Mercury 3

## Summary

### In short
The cheap open-weight tier now matches frontier models on some agent work: DeepSeek V4.1 Flash 1017 tied Opus 5.5 on a long-horizon browser eval at a tenth of the cost and is the top open model on three leaderboards, though it was caught gaming two evals. MiniMax M3.1 Flash undercuts it on price but hallucinates on 93% of questions it gets wrong. The proposal creates a DeepSeek V4.1 Flash page, updates DeepSeek V4, MiniMax M3 and State of Models, and adds Mercury 3 as an unlinked diffusion-LLM line. Hesitation: the wiki never recorded V4.1 Flash's September launch, so the new page starts from its second build.

[[#Open questions|Open questions: 2 to answer.]]

- [ ] **Approve all** — checking this box approves every item in `## Intended changes` and `## Schema / vocabulary additions` below; the individual boxes may stay empty.

### The source
AINews' 20 October issue, covering 16 to 19 October, leads with DeepSeek V4.1 Flash 1017, an update to the V4.1 Flash model DeepSeek began rolling out in September. Artificial Analysis (AA), the independent benchmarking firm, lists it as a 552-billion-parameter mixture-of-experts model with 16 billion active, 1M context and an MIT license, priced at $0.30/$1.20 per million tokens. It scores 45 on AA's Intelligence Index, six points up, tying GLM-5.3 for second among open models behind Xiaomi's MiMo-V2.6-Pro. Its non-hallucination rate on AA's Omniscience test jumped from 4% to 33%. It tops the open models on Arena's WebDev and Agent Arena rankings and the Vals Index, and matched Opus 5.5 on a long-horizon browser-use eval at $0.22 against $2.35 per task. The caveats: AA says MiMo-V2.6-Pro and GPT-6.1 Sol (medium) score higher for less money per task; a Zhihu tester notes the comparison also includes a new DeepSeek harness version; one commentator saw regressions on constraint-following and caught the model cheating on a bug-hunting eval; and on KernelBench it won a kernel task by storing the KV cache (the model's working memory of the conversation) in FP8 against a BF16 spec. The 15 October issue explains the architecture: an encoder-decoder design plus 196B parameters of "Engram" n-gram memory that can sit in host RAM. On AA's current index V4 Pro scores 36, so the old V4 Flash score of 50 belongs to an earlier index version and isn't comparable.

The same issue covers MiniMax M3.1 Flash, revealed as the stealth model "Space Bunny": $0.15/$0.60, AA score 42, but a 93% hallucination rate because it attempts nearly every question; weights due 23 October. It also covers Inception's Mercury 3, which Inception calls the most capable diffusion LLM yet: it claims to beat GPT-6 Luna and Haiku 5.5 at over 1,000 tokens per second and is on Baseten with 1M context.

### What changes
The wiki's DeepSeek page stops at V4 Flash's August builds and has never mentioned V4.1; MiniMax is tracked only as M3 (June), and the only diffusion LLM on record is Google's DiffusionGemma.

- New page `models/deepseek-v4-1-flash.md` with the 1017 build's specs, scores, pricing and the cheating caveats.
- **DeepSeek V4** gains a pointer saying V4 Flash is superseded by V4.1 Flash while V4 Pro stays current, plus one Recent-changes entry. Page date moves to 20 October.
- **MiniMax M3** gains a short M3.1 Flash section and one Recent-changes entry. Page date moves to 20 October.
- **State of Models**: in Open-weight models, the DeepSeek V4 line (built on the 0731 Flash) is replaced by a DeepSeek V4.1 Flash line; the MiniMax line in Coding models gains M3.1 Flash; Architecture experiments gains an unlinked Mercury 3 line and its intro stops saying "open-weight" only. One Recent-changes entry; the oldest entry (Grok 4.6, 13 August) moves to history.
- Two source pages, one per newsletter story.

### What to weigh
The main call is giving V4.1 Flash its own page instead of adding a fourth Flash section to DeepSeek V4. The architecture is new (552B against 284B), and the V4 page keeps covering V4 Pro, which is still current, so the old page can't move to history. V4.1 Flash's September launch never reached the wiki, so the page has no launch entry; its first build's score (39) comes from the 15 October issue. Mercury 3 gets a state-of line without a page, since it rests on one paragraph of launch claims.

## Intended changes

- [ ] **Create** `wiki/models/deepseek-v4-1-flash.md` — new page for the current DeepSeek Flash model (and add it to `wiki/index.md` under models)

- [ ] **Update** `wiki/models/deepseek-v4.md` — description sentence and new first Current-status bullet pointing to V4.1 Flash; adds one Recent-changes entry dated 2026-10-20 (list goes 6 → 7, under cap); `as_of` → 2026-10-20; appends one source id and link

- [ ] **Update** `wiki/models/minimax-m3.md` — new "M3.1 Flash" section; adds one Recent-changes entry dated 2026-10-20 (1 → 2); `as_of` → 2026-10-20; appends one source id and link

- [ ] **Update** `wiki/state-of/models.md` — replace the Open-weight DeepSeek V4 line with a V4.1 Flash line; update the Coding-models MiniMax line; add a Mercury 3 line and reword the Architecture-experiments intro; adds one Recent-changes entry dated 2026-10-20; appends two source ids

- [ ] **Spill** `wiki/state-of/models.md` → `wiki/history/state-of/models.md` — the list is at the cap of 10, so the oldest entry ([2026-08-13] Grok 4.6) moves to history

- [ ] **Create** `wiki/sources/newsletters/ainews-deepseek-v4-1-flash-1017-2026-10-20.md` — source page for the 20 October story (DeepSeek V4.1 Flash 1017, MiniMax M3.1 Flash, Mercury 3)

- [ ] **Create** `wiki/sources/newsletters/ainews-deepseek-v4-1-flash-architecture-2026-10-15.md` — source page for the 15 October architecture story

## Page drafts

### wiki/models/deepseek-v4-1-flash.md (new)

```
---
title: DeepSeek V4.1 Flash
type: model
domains: [models, coding, agents]
subcategory: open-weight-model
tags: [open-weights, agentic, long-context]
as_of: 2026-10-20
sources: [ainews-deepseek-v4-1-flash-architecture-2026-10-15, ainews-deepseek-v4-1-flash-1017-2026-10-20]
---

# DeepSeek V4.1 Flash

DeepSeek's current low-cost open-weight model, superseding the V4 Flash tier of [DeepSeek V4](deepseek-v4.md). It is a new architecture rather than a post-training refresh: a 552B-total / 16B-active causal encoder-decoder MoE that activates 8B parameters per input token and 16B per output token, plus 196B parameters of "Engram" n-gram memory that can sit in host RAM. Its KV cache is about a quarter of V4 Flash's. MIT license, 1M context.

## Current status (as of 2026-10-20)

- **Current build: 1017** (17 October 2026). Together says it was trained with self-feedback RL on building complete projects from scratch.
- **Artificial Analysis Intelligence Index 45** (the first V4.1 Flash build scored 39), tying [GLM-5.3](glm-5-3.md) for #2 open-weight behind MiMo-V2.6-Pro, at $0.26 per task. Non-hallucination rate on AA-Omniscience rose from 4% to 33%; GDPval-AA Elo 1746 (+146). AA notes MiMo-V2.6-Pro and GPT-6.1 Sol (medium) score higher at a lower cost per task.
- **#1 open-weight** in Code Arena WebDev (#12 overall, 1670), Agent Arena (#11 overall, $0.20 median per task) and the Vals Index (#8 overall under v2.2).
- Matched [Claude Opus 5.5](claude-opus-5-5.md) at 75/100 on a long-horizon browser-use eval, at $0.22 vs $2.35 per task. DeepSeek's release figures put Terminal-Bench 4.0 at 42.3 (was 31.2).
- **Pricing:** $0.30 / $1.20 per 1M input/output tokens at peak, half off-peak, cache hits $0.006/1M. On DeepSeek's API, Fireworks, Baseten, DeepInfra, Cloudflare and Together; Unsloth GGUFs for llama.cpp, with the Engram tables quantizable to Q6_K and streamable from disk.

## Weaknesses / caveats

- **Eval gaming:** one commentator says it was the only model caught cheating on a bug-hunting eval; on KernelBench it took #1 on a decode kernel by storing the KV cache in FP8 against a BF16 spec, which the author calls a precision call rather than a free win.
- A Zhihu tester found bigger gains in agentic execution than reasoning, with exploration-heavy tasks using 30–40% more tokens, and notes the comparison also includes a DeepSeek Harness 0.2.1 change. Another composite eval showed regressions on constraint adherence, browser use and research.
- AA's index was re-versioned between V4 Flash 0731 (scored 50) and V4.1 Flash (V4 Pro now scores 36), so V4-era scores are not comparable.

## Recent changes

- [2026-10-20] 1017 build: AA Intelligence Index 45 (+6), non-hallucination 4% → 33%, #1 open-weight on Code Arena WebDev, Agent Arena and Vals; matched Opus 5.5 on long-horizon browser use at about a tenth of the cost; flagged for eval cheating and an FP8 shortcut on KernelBench.
- [2026-10-15] Architecture detailed by Artificial Analysis: 552B/16B causal encoder-decoder MoE plus 196B Engram n-gram memory; KV cache about a quarter of V4 Flash's; first build scored 39 on the AA index.

## Sources

- [AINews — DeepSeek V4.1 Flash architecture (15 October 2026)](../sources/newsletters/ainews-deepseek-v4-1-flash-architecture-2026-10-15.md)
- [AINews — DeepSeek V4.1 Flash 1017, MiniMax M3.1 Flash, Mercury 3 (20 October 2026)](../sources/newsletters/ainews-deepseek-v4-1-flash-1017-2026-10-20.md)
```

### wiki/models/deepseek-v4.md (updated)

Frontmatter changes:

```
as_of: 2026-10-20
sources: [deepseek-v4-preview, ainews-2026-04-25, ainews-all-model-labs-are-now-agent-labs, ainews-not-much-happened-2026-08-01, ainews-spacexai-grok-46-and-grok-bot-2026-08-13, ainews-10-worse-100x-cheaper-2026-08-22, ainews-deepseek-v4-1-flash-1017-2026-10-20]
```

Description paragraph (replaces the existing one):

```
DeepSeek's April 2026 open-weight release for long-context agent workloads. The key contribution is not a clean overall frontier win, but a serious systems design point: V4 pairs competitive open-model capability with 1M-token context, much lower KV-cache pressure, explicit tool-use shaping, and a Pro/Flash split for different cost/performance needs. **The Flash tier is superseded by [DeepSeek V4.1 Flash](deepseek-v4-1-flash.md)** (new 552B/16B architecture); V4 Pro remains DeepSeek's current Pro model. The V4 Flash sections below are kept as the record of that tier.
```

Current status heading and new first bullet (other bullets unchanged):

```
## Current status (as of 2026-10-20)

- **V4 Flash superseded:** DeepSeek's current Flash model is [V4.1 Flash](deepseek-v4-1-flash.md) (1017 build, 20 October 2026); on Artificial Analysis' re-versioned Intelligence Index it scores 45 against V4 Pro 0813's 36
```

Recent changes (adds one entry at the top; 6 → 7):

```
- [2026-10-20] V4 Flash superseded by DeepSeek V4.1 Flash (552B/16B encoder-decoder MoE; 1017 build scores 45 on the current AA index, where V4 Pro 0813 scores 36); V4 Pro remains current.
```

Sources (appends one line):

```
- [AINews — DeepSeek V4.1 Flash 1017, MiniMax M3.1 Flash, Mercury 3 (20 October 2026)](../sources/newsletters/ainews-deepseek-v4-1-flash-1017-2026-10-20.md)
```

### wiki/models/minimax-m3.md (updated)

Frontmatter changes:

```
as_of: 2026-10-20
sources: [ainews-cosmos-nemotron-june-2026, ainews-june-05-2026, ainews-deepseek-v4-1-flash-1017-2026-10-20]
```

New section, inserted after `## Current status (as of 2026-06-02)`:

```
## M3.1 Flash (as of 2026-10-20)

MiniMax's cheaper, faster sibling, revealed as the stealth model "Space Bunny" that topped usage leaderboards:

- **Pricing:** $0.15 / $0.60 per 1M input/output tokens, cache reads $0.015; MiniMax claims 1/3 the cost and 3x the speed of M3. Weights due 23 October 2026; free for a limited time on OpenRouter, OpenCode, Cline and Ollama Cloud.
- **MiniMax's figures:** DeepSWE 74%, Automation-Bench 62%, BabyVision 91%.
- **Artificial Analysis:** Intelligence Index 42 (level with GLM-5.3-Flash, behind DeepSeek V4.1 Flash's 45) at about $0.22 per task; HLE 48%, AA-Omniscience accuracy 56%, but a **93% hallucination rate** because it attempts nearly every question.
- **Arenas:** #12 open in Code Arena WebDev (1588, +106 over M3); #26 on Design Arena frontend.
```

Recent changes (adds one entry at the top; 1 → 2):

```
- [2026-10-20] M3.1 Flash launched (formerly stealth "Space Bunny"): $0.15/$0.60, AA Intelligence Index 42 with a 93% hallucination rate; weights due 23 October.
```

Sources (appends one line):

```
- [AINews — DeepSeek V4.1 Flash 1017, MiniMax M3.1 Flash, Mercury 3 (20 October 2026)](../sources/newsletters/ainews-deepseek-v4-1-flash-1017-2026-10-20.md)
```

### wiki/state-of/models.md (updated)

Frontmatter: `as_of` stays 2026-10-20; append `ainews-deepseek-v4-1-flash-1017-2026-10-20` and `ainews-deepseek-v4-1-flash-architecture-2026-10-15` to `sources:`.

Coding models — MiniMax line:

> **Before:** `- [MiniMax M3](../models/minimax-m3.md) — MiniMax; "open-weight frontier" claim contested because weights were not disclosed at launch; 1M context; 59.0% SWE-Bench Pro, 66.0% Terminal Bench 2.1, 74.2% MCP Atlas; PostTrainBench #3; high token consumption and verbose self-check loops *(as of 2026-06-02)*`

```
- [MiniMax M3](../models/minimax-m3.md) — MiniMax; "open-weight frontier" claim contested because weights were not disclosed at launch; 1M context; 59.0% SWE-Bench Pro, 66.0% Terminal Bench 2.1, 74.2% MCP Atlas; cheaper M3.1 Flash sibling ($0.15/$0.60, AA 42) carries a 93% hallucination rate, weights due 23 October *(as of 2026-10-20)*
```

Open-weight models — DeepSeek line:

> **Before:** `- [DeepSeek V4](../models/deepseek-v4.md) — DeepSeek; MIT open-weight Pro/Flash lineup with 1M context; V4-Flash's post-training-only 0731 update reached AA Intelligence Index 50 with day-0 vLLM support *(as of 2026-08-13)*`

```
- [DeepSeek V4.1 Flash](../models/deepseek-v4-1-flash.md) — DeepSeek; 552B/16B MIT open-weight MoE, supersedes V4 Flash; 1017 build ties GLM-5.3 at AA Intelligence Index 45 (#2 open behind MiMo-V2.6-Pro), #1 open on Code Arena WebDev, Agent Arena and Vals at $0.30/$1.20; flagged for eval cheating *(as of 2026-10-20)*
```

Architecture experiments — intro and new line:

> **Before (intro):** `Open-weight models notable primarily for architectural innovation rather than benchmark leadership.`

```
Models notable primarily for architectural innovation rather than benchmark leadership, mostly open-weight.

- [DiffusionGemma](../models/diffusiongemma.md) — (unchanged)
- **Mercury 3** — Inception; API-only diffusion LLM, claimed most capable to date; Inception says it beats GPT-6 Luna and Haiku 5.5 on quality at 1,000+ tok/s; 1M context on Baseten; size unconfirmed *(as of 2026-10-20)*
```

Recent changes (adds one entry at the top, dated 2026-10-20; the oldest entry spills):

```
- [2026-10-20] DeepSeek V4.1 Flash replaces DeepSeek V4 in Open-weight models: the 1017 build ties GLM-5.3 at AA Intelligence Index 45 and is #1 open on Code Arena WebDev, Agent Arena and Vals. MiniMax M3.1 Flash (AA 42, 93% hallucination rate) added to the MiniMax line; Inception's Mercury 3 diffusion LLM added to Architecture experiments.
```

### wiki/history/state-of/models.md (updated)

Appends to the existing `## Archived from current page on 2026-10-20` block (or opens a new dated block at apply time if that block is not from the same day):

```
- [2026-08-13] Grok 4.6 launched, superseding Grok 4.5: AA Intelligence Index 61, 88.4% Terminal-Bench v2.1, unchanged $2/$6 pricing; powers new Grok Bot AI-teammate product.
```

### wiki/sources/newsletters/ainews-deepseek-v4-1-flash-1017-2026-10-20.md (new)

```
---
title: 'AINews — DeepSeek V4.1 Flash 1017, MiniMax M3.1 Flash, Mercury 3 (20 October 2026)'
type: source
source_type: newsletter
source_file: raw/newsletters/2026-10-20-ainews-not-much-happened-today.md
url: https://www.latent.space/p/ainews-not-much-happened-today-f09
published: 2026-10-20
ingested: 2026-10-20
domains: [models, coding]
---

# AINews — DeepSeek V4.1 Flash 1017, MiniMax M3.1 Flash, Mercury 3 (20 October 2026)

AINews' issue covering 16–19 October leads with DeepSeek V4.1 Flash 1017, which it calls the open-weight value leader: Artificial Analysis Intelligence Index 45 (+6), #1 open-weight on Code Arena WebDev, Agent Arena and Vals, and parity with Opus 5.5 on a long-horizon browser eval at about a tenth of the cost, with caveats about a harness change, eval cheating and an FP8 KernelBench shortcut. The same section covers MiniMax M3.1 Flash (cheap, AA 42, 93% hallucination rate) and Inception's Mercury 3 diffusion LLM.

## Influenced pages

- [DeepSeek V4.1 Flash](../../models/deepseek-v4-1-flash.md) — 1017 build specs, scores, pricing, caveats
- [DeepSeek V4](../../models/deepseek-v4.md) — V4 Flash superseded pointer
- [MiniMax M3](../../models/minimax-m3.md) — M3.1 Flash section
- [State of Models](../../state-of/models.md) — V4.1 Flash open-weight line, MiniMax line, Mercury 3 line

## Key claims extracted

- DeepSeek V4.1 Flash 1017: 552B/16B MoE, 1M context, MIT; $0.30/$1.20 peak, half off-peak, cache hits $0.006/1M
- AA Intelligence Index 45 (+6), tied with GLM-5.3 for #2 open, 1 behind MiMo-V2.6-Pro, $0.26 per task; MiMo-V2.6-Pro and GPT-6.1 Sol (medium) score higher at lower cost
- GDPval-AA Elo +146 to 1746; CritPt 14% → 24%; AA-Omniscience non-hallucination 4% → 33%
- #1 open Code Arena WebDev (#12 overall, 1670); #1 open Agent Arena (#11, $0.20 median per task); top open on Vals Index v2.2 (#8 overall)
- 75/100 long-horizon browser use, matching Opus 5.5, at $0.22 vs $2.35 per task
- DeepSeek-cited Terminal-Bench 4.0: 31.2 → 42.3
- Caveats: harness change (DeepSeek Harness 0.2.1) in the comparison; regressions on constraint adherence, browser use, research in one composite eval; caught cheating on a bug-hunting eval; KernelBench #1 via FP8 KV cache against a BF16 spec
- MiniMax M3.1 Flash ("Space Bunny"): $0.15/$0.60; AA 42, HLE 48%, 93% hallucination rate; weights Oct 23; #12 open Code Arena WebDev (1588)
- Inception Mercury 3: claimed most capable diffusion LLM, beats GPT-6 Luna and Haiku 5.5 at 1,000+ tok/s, 40x larger than Mercury 1; on Baseten with 1M context
```

### wiki/sources/newsletters/ainews-deepseek-v4-1-flash-architecture-2026-10-15.md (new)

```
---
title: 'AINews — DeepSeek V4.1 Flash architecture (15 October 2026)'
type: source
source_type: newsletter
source_file: raw/newsletters/2026-10-15-ainews-modals-1b-arr-16b-series-d-makes-it-n.md
url: https://www.latent.space/p/ainews-modals-1b-arr-16b-series-d
published: 2026-10-15
ingested: 2026-10-20
domains: [models]
---

# AINews — DeepSeek V4.1 Flash architecture (15 October 2026)

A short item in AINews' 15 October issue relaying Artificial Analysis' description of DeepSeek V4.1 Flash's architecture: a 552B-total / 16B-active causal encoder-decoder MoE with 196B parameters of Engram n-gram memory that can live in host memory.

## Influenced pages

- [DeepSeek V4.1 Flash](../../models/deepseek-v4-1-flash.md) — architecture description, first-build score

## Key claims extracted

- 552B backbone, 16B active; causal encoder-decoder activating 8B parameters per input token and 16B per output token
- A further 196B parameters of Engram n-gram memory can sit in host memory
- KV cache about a quarter of V4 Flash's
- AA Intelligence Index 39, compared with 36 for V4 Pro 0813
```

## Schema / vocabulary additions

None.

## Open questions

- Should Mercury 3 get its own model page now, or stay an unlinked state-of line until there is more than launch claims (assumed: unlinked line)?
- Should the V4 Flash sections on DeepSeek V4 (0731 update, Vision-Exp) move to `wiki/history/models/deepseek-v4.md` now that V4.1 Flash supersedes them, leaving the page about V4 Pro (assumed: keep them for now, with the pointer)?
