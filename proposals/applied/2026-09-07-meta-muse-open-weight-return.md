---
type: proposal
source: raw/newsletters/2026-08-06-a-codex-of-ones-own.md
sources:
  - raw/newsletters/2026-08-06-a-codex-of-ones-own.md
  - raw/newsletters/2026-08-07-ainews-amd-buys-taalas.md
  - raw/newsletters/2026-08-11-ainews-muse-glimmer-and-spark-open-weights-retu.md
status: pending
created: 2026-09-07
---

# Proposal: Meta's open-weight return — Muse Code, Muse Spark 1.2, Muse Glimmer

## Summary

### The source

Across three separate AINews/Every dispatches between 2026-08-06 and 2026-08-11, Meta's Superintelligence Labs effort visibly re-escalated after a quieter stretch that had included Muse Spark 1.1's pivot to a closed, metered API. On 2026-08-06, Every reported Meta launching Muse Code in beta — its first terminal coding agent, which Mark Zuckerberg pitched as handling "complete software engineering tasks" across large repos, aimed squarely at Claude Code and Codex; the same week Google DeepMind was independently reshuffling its own leadership (covered in a separate proposal), and Every framed both moves as labs racing to close a coding-agent gap. On 2026-08-07, AINews reported Muse Spark 1.2 breaking into frontier-tier third-party benchmarks: a top-5 Vals Index placement at a fraction of rival cost, the first model to clear 60% on Finance Agent v2, and a Meta-claimed sweep of gold-medal-level results across five STEM Olympiads achieved with no external tools — gains Meta itself credited partly to multi-agent orchestration rather than raw model capability. Finally, on 2026-08-11, AINews covered Meta's full open-weight re-entry: Muse Glimmer, a 30B dense multimodal model released under Apache 2.0 and purpose-built for always-on local agents, arrived alongside a sequel to Zuckerberg's "Personal Superintelligence" essay and Alexandr Wang's confirmation that Muse Spark 1.2's own weights are coming soon too — a reversal of Spark 1.1's closed-API-only launch. Third-party benchmarks place Glimmer just behind two existing open-weight peers on raw capability, with its real pitch being local deployability rather than frontier intelligence.

### What changes

The wiki currently treats Muse Spark as a single evolving page, with no coding-agent-product page for Meta and no coverage of a genuinely open-weight Meta model.

- **Muse Spark** gains a new section documenting the 1.2 benchmark breakout (Vals Index, Finance Agent v2, STEM Olympiad results) and a pointer to its new sibling; page date moves to 11 August.
- New page `models/muse-glimmer.md`, since Glimmer is architecturally distinct from Spark (dense vs. Spark's design, Apache 2.0 vs. closed/paid, logit-distilled and trained from scratch on agentic traces rather than a version bump).
- New page `tools/muse-code.md`, since Meta's terminal coding agent is a distinct product surface, in the same category as Claude Code and Codex.
- **Open-weight momentum broadens** gains a new Current-signal bullet and a Recent-changes entry for Meta's return to open weights; the list is already at its 10-entry cap, so the oldest entry (Kimi K3's July 17 announcement) spills to history. Page date moves to 11 August.
- Three new source pages, one per raw newsletter.

### What to weigh

The main judgment call is the Muse Glimmer/Muse Spark page split — Glimmer could instead have been folded into `muse-spark.md` as another dated section, the way Spark 1.1 was. This proposal treats it as a separate model page because it's a different lineage (a distilled sibling, not a version bump) with a different license and purpose, consistent with how the wiki already separates related-but-distinct model lines elsewhere. All benchmark figures (Vals Index, Artificial Analysis Intelligence/Openness Index) are third-party, relayed through AINews summaries rather than primary Meta or benchmark-provider documentation — treat them as directionally useful, not verified. Muse Code's launch source is Every's brief Signal item, not a first-party Meta writeup, so the tool page is necessarily thin; no `state-of/coding.md` leader-line change is proposed since nothing in the source establishes Muse Code as currently leading any subcategory.

## Intended changes

- [x] **Approve all** — checking this box approves every item in `## Intended changes` and `## Schema / vocabulary additions` below; the individual boxes may stay empty.

- [ ] **Update** `wiki/models/muse-spark.md` — add Muse Spark 1.2 benchmark section, sibling pointer to Glimmer, Recent-changes entries, bump as_of
    > See draft below

- [ ] **Create** `wiki/models/muse-glimmer.md` — new open-weight model page

- [ ] **Create** `wiki/tools/muse-code.md` — new terminal-coding-agent tool page

- [ ] **Update** `wiki/trends/open-weight-momentum-broadens.md` — new Current-signal bullet, new Recent-changes entry, bump as_of
    > See draft below

- [ ] **Spill** `wiki/trends/open-weight-momentum-broadens.md` → `wiki/history/trends/open-weight-momentum-broadens.md` — oldest Recent-changes entry ([2026-07-17] Kimi K3 announced) falls off the cap

- [ ] **Create** `wiki/sources/newsletters/muse-code-launch-2026-08-06.md` — source summary

- [ ] **Create** `wiki/sources/newsletters/muse-spark-12-benchmarks-2026-08-07.md` — source summary

- [ ] **Create** `wiki/sources/newsletters/muse-glimmer-launch-2026-08-11.md` — source summary

## Page drafts

### wiki/models/muse-spark.md (updated)

```md
---
title: Muse Spark
type: model
domains: [models, creative]
subcategory: frontier-model
tags: [closed-source, agentic, meta]
as_of: 2026-08-11
sources: [muse-spark, open-creative-workflows-2026-06, meta-muse-image-video-2026-07, superhuman-chatgpt-work-muse-spark-2026-07, the-code-databricks-coding-benchmark-2026-07-10, ainews-gpt-56-rollout-not-much-happened-2026-07-11, muse-spark-12-benchmarks-2026-08-07, muse-glimmer-launch-2026-08-11]
---

[... unchanged intro and earlier sections through "## Muse Spark 1.1 — Meta's first paid model" ...]

## Muse Spark 1.2 breaks into frontier benchmarks (as of 2026-08-07)

Muse Spark 1.2 moved from off-the-board to frontier-tier quickly. On the Vals Index, it entered the top 5 at $0.69/test — reportedly 3x cheaper than Kimi and 10x+ cheaper than Fable, Opus, and GPT-5.6 Sol — and became the first model to score above 60% on Finance Agent v2, at $0.77/test versus the prior #1 (Claude Opus 5) at $5.12/test and roughly half the latency. Artificial Analysis's v4.1.1 grading-update patch also gave Muse Spark 1.2 one of the largest score increases of any model that round.

Meta separately claimed gold-medal-level performance across five STEM Olympiads (APhO, IPhO — perfect theory scores — IMO, IChO, RMM), three submitted under live competition conditions and officially graded, using no external tools (no search, code execution, or calculator) and attributing part of the gain to multi-agent orchestration with parallel reasoning. The tool-free framing immediately fed into the ongoing "LLMs vs. harnesses vs. neurosymbolic" debate (François Chollet and others), since Meta's own explanation credits orchestration as much as raw model capability.

A smaller, architecturally distinct sibling, **Muse Glimmer** (30B dense, multimodal, Apache 2.0, designed for always-on local agents) shipped 2026-08-11 — see [Muse Glimmer](muse-glimmer.md). Alexandr Wang confirmed Muse Spark 1.2's own weights are coming "soon," a reversal from Spark 1.1's closed, metered-API-only launch.

## Recent changes

- [2026-08-11] Muse Glimmer ships as a smaller, open-weight (Apache 2.0) sibling model; Muse Spark 1.2's own weights promised "soon" — a reversal from Spark 1.1's closed API-only launch.
- [2026-08-07] Muse Spark 1.2 breaks into frontier-tier benchmarks: Vals Index top 5 at $0.69/test, first model above 60% on Finance Agent v2, five STEM Olympiad gold-medal-level results under no-tool conditions.
- [2026-07-09] Muse Spark 1.1 launches on the new Meta Model API — Meta's first paid, metered model; AA Intelligence Index 51 (+8 vs 1.0); Arena #9 Code Arena: Frontend.
- [2026-07-08] Muse Image launches in Meta AI, Instagram Stories, and WhatsApp; Muse Video previewed; AINews describes an agentic planning/tool-use/self-refinement generation loop.
- [2026-06-24] Superhuman reports Meta Glasses launched with Muse Spark built in; secondary coverage only.
- [2026-04-10] Page created from Meta's Muse Spark introduction post

## Sources

[... unchanged existing source lines ...]
- [AINews — Muse Spark 1.2 benchmark breakout](../sources/newsletters/muse-spark-12-benchmarks-2026-08-07.md)
- [AINews — Muse Glimmer launch](../sources/newsletters/muse-glimmer-launch-2026-08-11.md)
```

### wiki/models/muse-glimmer.md (new)

```md
---
title: Muse Glimmer
type: model
domains: [models, agents]
subcategory: open-weight-model
tags: [meta, open-weights, agentic]
as_of: 2026-08-11
sources: [muse-glimmer-launch-2026-08-11]
---

# Muse Glimmer

Muse Glimmer is Meta Superintelligence Labs' first genuinely open-weight frontier-adjacent model: a 30B dense, multimodal, agent-focused model released under Apache 2.0 on 2026-08-11, alongside a promise to open Muse Spark 1.2's own weights "soon." Unlike a conventional base-then-post-train release, Glimmer was logit-distilled from Muse Spark and trained from the outset on agentic traces.

## Current status (as of 2026-08-11)

- 30B dense parameters, interleaved text+image input via a dedicated perception encoder, 100+ languages, controllable reasoning effort
- Designed for always-on local agents: ~4-bit quantization brings the model under 20GB, paired with a lightweight DFlash speculative-decoding drafter for faster on-device generation; ~60GB at BF16
- 128K context; memory-efficient hybrid attention (community notes: Gemma-4-style hybrid attention plus scale-free QK norm, larger vision depth, longer sliding-window attention)
- Benchmarked on agent-specific suites: DeepSearch QA, MCP-Atlas, τ³-Bench, SWE-Bench
- Planned day-0/near-day-0 support: Ollama, LM Studio, Unsloth, torchtitan, llama.cpp, MLX, ExecuTorch, vLLM, SGLang; weights on Hugging Face

## Benchmarks

- Artificial Analysis Intelligence Index: 35 — just behind Qwen3.6-27B (38) and near Kimi K2.5 (36)
- Artificial Analysis Openness Index: 44 — a strong score reflecting the Apache 2.0 license and local-deployment focus
- Does well on Tau3-Banking tool-use follow-up; comparatively weak on hallucination/knowledge calibration and general agentic knowledge work versus similarly-sized peers

## Why it matters

Glimmer marks Meta's return to shipping genuinely open weights after Muse Spark 1.1 pivoted to a closed, metered API — arriving alongside Zuckerberg's sequel "Personal Superintelligence" essay reaffirming Meta's stated strategy of keeping frontier capability in individual hands rather than institutions. It's a small-footprint, locally-deployable agent model rather than a flagship capability play.

## Caveats

- Benchmark placement (AA Intelligence Index 35) trails several existing open-weight peers on raw capability; Glimmer's pitch is local-agent deployability, not frontier intelligence
- Hallucination/knowledge-calibration weakness is a real caveat for any workflow requiring factual reliability
- All benchmark figures here are third-party (Artificial Analysis) via an AINews summary, not independently verified by this wiki

## Sources

- [AINews — Muse Glimmer launch](../sources/newsletters/muse-glimmer-launch-2026-08-11.md)
```

### wiki/tools/muse-code.md (new)

```md
---
title: Muse Code
type: tool
domains: [coding, agents]
subcategory: terminal-coding-agent
tags: [meta, cli, agentic, beta]
as_of: 2026-08-06
sources: [muse-code-launch-2026-08-06]
---

# Muse Code

Muse Code is Meta's first terminal coding agent, launched in beta on 2026-08-06 — Meta's answer to Claude Code and Codex. Mark Zuckerberg described it as able to tackle "complete software engineering tasks" (planning, writing, and validating code) across large repositories.

## Current status (as of 2026-08-06)

- Launched in beta 2026-08-06, positioned directly against Claude Code and OpenAI Codex
- Framed by Meta as capable of end-to-end tasks: planning, writing, and validating code across large repos
- Arrives the same week as Google DeepMind's leadership reshuffle, widely read (per Every) as both Meta and DeepMind moving to close a coding-agent gap against OpenAI and Anthropic
- No independent benchmark results are available yet in the captured source

## Why it matters

This is Meta's clearest entry into the terminal-coding-agent category, following Muse Spark's earlier pivot toward agentic/coding capability. It brings the count of frontier labs actively competing for coding-agent mindshare to five (OpenAI, Anthropic, Google DeepMind, Meta, and xAI/SpaceXAI), per Every's own count.

## Caveats

- Beta product with no independent benchmarking captured yet — this page will need a follow-up update once real usage data or benchmarks appear
- The launch source is secondary commentary (Every), not a first-party Meta announcement or technical writeup

## Sources

- [Every — Meta launches Muse Code beta](../sources/newsletters/muse-code-launch-2026-08-06.md)
```

### wiki/trends/open-weight-momentum-broadens.md (updated)

```md
---
title: Open-weight momentum broadens
type: trend
domains: [models, computer-use]
tags: [open-weights, google]
as_of: 2026-08-11
sources: [..., ainews-qwen38-max-launch-2026-08-04, muse-glimmer-launch-2026-08-11]
---

[... unchanged intro ...]

## Current signal

[... unchanged existing bullets, ending with the Qwen 3.8 Max bullet ...]
- **Meta returns to open weights (August 2026):** After Muse Spark 1.1 pivoted to a closed, metered API in July, Meta shipped Muse Glimmer on 2026-08-11 — a 30B dense multimodal agent model under Apache 2.0, logit-distilled from Muse Spark and trained from the outset on agentic traces, designed for always-on local agents (~20GB at 4-bit, 128K context). Alexandr Wang confirmed Muse Spark 1.2's own weights are coming "soon." Third-party benchmarks (Artificial Analysis) place Glimmer at Intelligence Index 35 — behind Qwen3.6-27B (38) and near Kimi K2.5 (36) — with a strong 44 Openness Index but weaker hallucination/knowledge-calibration scores; the pitch is local-agent deployability, not frontier capability.
- **Kimi K3 (Moonshot, July 2026):** [... unchanged ...]
[... remaining unchanged bullets ...]

[... unchanged "Why it matters" and "Model sovereignty" sections ...]

## Recent changes

- [2026-08-11] Meta returns to open weights: ships Muse Glimmer (30B dense multimodal, Apache 2.0, AA Intelligence Index 35, Openness Index 44) for always-on local agents; Muse Spark 1.2's own weights promised "soon" per Alexandr Wang.
- [2026-08-04] Qwen 3.8 Max ships in full (2.4T/~95B active): strong third-party benchmarks, open weights promised for Max + a 27B sibling — but license reportedly restricts use/download in US/EU/UK/Korea, echoing a similar MiniMax H3 complaint.
- [2026-07-31] Thinking Machines shipped Inkling-Small (276B/12B MoE, Intelligence Index 40, ~1/4 the flagship's active footprint at near-flagship capability), extending its US-origin open-weight flagship into a smaller sibling.
- [2026-07-29] Kimi K3 deployment economics documented: ~8×MI355X minimum to load, 64+ GPUs for production serving, six-figure entry cost; Composio's cross-harness comparison shows the same model performs similarly but at very different cost/speed depending on the agent harness used (Kimi Code, Hermes, Claude Code).
- [2026-07-29] Corrects the prior entry: OpenAI in fact declined to join the Open Secure AI Alliance, per a more detailed 2026-07-29 AINews recap — the decision reportedly triggered internal employee backlash. The earlier "OpenAI signs" report (2026-07-28) appears to have been premature or imprecise.
- [2026-07-28] NVIDIA launches the "Open Secure AI Alliance" (Adobe, Cisco, Cloudflare, Hugging Face, IBM, Microsoft, Red Hat, Salesforce, SAP, ServiceNow, Snowflake, SpaceX); Anthropic does not join — publishing its own position (chip controls, anti-distillation, safety testing, not a ban) instead; NYT reports both labs lobbying Washington against open models even as Altman publicly backs them
- [2026-07-28] Kimi K3's weights ship in full (104B active/896 experts, FlashKDA/MoonEP/AgentENV infra open-sourced); separately, Kratsios accuses Moonshot of covertly distilling Fable to build it, Treasury signals possible Entity List sanctions, critics call the timeline technically implausible
- [2026-07-22] Poolside released Laguna S 2.1 (118B/8B-active MoE, OpenMDW-1.1 license): a new non-Chinese open-weight coding entrant, strong on agentic-coding benchmarks, more prone to fabrication under pressure than Qwen3.5-122B per one independent eval.
- [2026-07-21] Sovereignty pressure reverses direction: US reported weighing restrictions on Chinese open-weight models (procurement, Entity List, hosting liability); Hugging Face's Clément Delangue and others push back citing HF's own self-hosted GLM-5.2 use during a cyber incident as evidence open models are security infrastructure
- [2026-07-20] Qwen3.8-Max-Preview enters live preview, 2.4T parameters (third-party estimate), native video understanding; Alibaba signals the eventual official release will be open-weighted

[... unchanged "What to watch" and "Sources" (append the Glimmer source line) ...]
```

### wiki/history/trends/open-weight-momentum-broadens.md (updated)

```md
## Archived from current page on 2026-09-07

- [2026-07-17] Kimi K3 (Moonshot, 2.8T) announced: Intelligence Index 57, #1 Frontend Code Arena — the clearest open-weight capability jump in this trend so far.
- [2026-07-16] Thinking Machines Lab released Inkling (975B/41B MoE, Apache 2.0, Intelligence Index 41) — its first flagship model, and a rare US-origin open-weight flagship choice.
[... unchanged remaining entries under this header, and all earlier headers, unchanged ...]
```

### wiki/sources/newsletters/muse-code-launch-2026-08-06.md (new)

```md
---
title: Every — Meta launches Muse Code beta
type: source
source_type: newsletter
source_file: raw/newsletters/2026-08-06-a-codex-of-ones-own.md
url: https://every.to/context-window/a-codex-of-ones-own
published: 2026-08-06
ingested: 2026-09-07
domains: [coding]
---

# Every — Meta launches Muse Code beta

Every's "A Codex of One's Own" Signal item: Meta launched Muse Code, its first terminal coding agent, in beta on 2026-08-06 — pitched by Mark Zuckerberg as able to handle "complete software engineering tasks" across large repos, directly against Claude Code and Codex. The same issue covers the Demis Hassabis/Koray Kavukcuoglu GDM leadership reshuffle (covered in a separate proposal) and Every's own Codex-workspace-setup piece (covered in a separate proposal).

## Influenced pages

- [tools/muse-code](../../tools/muse-code.md) — new page: beta launch, positioning against Claude Code/Codex

## Key claims extracted

- Muse Code launched in beta 2026-08-06, Meta's first terminal coding agent
- Zuckerberg: agent can tackle "complete software engineering tasks" (planning, writing, validating code) across large repos
- Positioned directly against Claude Code and OpenAI Codex
```

### wiki/sources/newsletters/muse-spark-12-benchmarks-2026-08-07.md (new)

```md
---
title: AINews — Muse Spark 1.2 benchmark breakout
type: source
source_type: newsletter
source_file: raw/newsletters/2026-08-07-ainews-amd-buys-taalas.md
url: https://www.latent.space/p/ainews-amd-buys-taalas
published: 2026-08-07
ingested: 2026-09-07
domains: [models]
---

# AINews — Muse Spark 1.2 benchmark breakout

AINews Twitter recap covering Muse Spark 1.2's rapid climb into frontier-tier benchmarks: Vals Index top-5 placement at $0.69/test (3x cheaper than Kimi, 10x+ cheaper than Fable/Opus/GPT-5.6 Sol), first model above 60% on Finance Agent v2 at $0.77/test vs. Claude Opus 5's prior #1 at $5.12/test, a large Artificial Analysis v4.1.1 grading-update score increase, and Meta's claim of gold-medal-level performance across five STEM Olympiads under no-tool, multi-agent-orchestrated conditions. The same issue covers AMD's acquisition of Taalas and OpenAI's ChatGPT model unification (both covered in separate proposals).

## Influenced pages

- [models/muse-spark](../../models/muse-spark.md) — new "Muse Spark 1.2" section: Vals Index/Finance Agent v2 benchmarks, STEM Olympiad results

## Key claims extracted

- Muse Spark 1.2: Vals Index top 5 at $0.69/test; 3x cheaper than Kimi, 10x+ cheaper than Fable/Opus/GPT-5.6 Sol
- First model above 60% on Finance Agent v2, at $0.77/test and roughly 2x the speed of the prior #1 (Claude Opus 5 at $5.12/test)
- Artificial Analysis v4.1.1 grading-update patch gave Muse Spark 1.2 one of the largest score increases of any model
- Meta claims gold-medal-level performance in five STEM Olympiads (APhO, IPhO, IMO, IChO, RMM), three under live competition conditions, officially graded, no external tools used
- Meta attributes some gains to multi-agent orchestration with parallel reasoning
```

### wiki/sources/newsletters/muse-glimmer-launch-2026-08-11.md (new)

```md
---
title: AINews — Muse Glimmer and Spark's open-weights return
type: source
source_type: newsletter
source_file: raw/newsletters/2026-08-11-ainews-muse-glimmer-and-spark-open-weights-retu.md
url: https://www.latent.space/p/ainews-muse-glimmer-and-spark-open
published: 2026-08-11
ingested: 2026-09-07
domains: [models]
---

# AINews — Muse Glimmer and Spark's open-weights return

AINews recap of Meta's 2026-08-11 open-weight re-entry: Muse Glimmer, a 30B dense multimodal agent model under Apache 2.0 designed for always-on local agents, ships alongside Zuckerberg's sequel "Personal Superintelligence" essay and Alexandr Wang's confirmation that Muse Spark 1.2's own weights are coming "soon." Covers Glimmer's architecture (logit-distilled from Muse Spark, trained from the outset on agentic traces, DFlash speculative decoding, ~20GB at 4-bit, 128K context) and third-party Artificial Analysis benchmark placement (Intelligence Index 35, Openness Index 44). The same issue covers Anthropic's Riemann Hypothesis result and Claude Sonnet 5's permanent pricing (both covered in separate proposals).

## Influenced pages

- [models/muse-glimmer](../../models/muse-glimmer.md) — new page: full launch details and benchmarks
- [models/muse-spark](../../models/muse-spark.md) — sibling-release pointer, Spark 1.2 open-weights promise
- [trends/open-weight-momentum-broadens](../../trends/open-weight-momentum-broadens.md) — new Current-signal bullet and Recent-changes entry

## Key claims extracted

- Muse Glimmer: 30B dense, multimodal, Apache 2.0, released 2026-08-11
- Logit-distilled from Muse Spark; trained from the outset on agentic traces (not a conventional base-then-post-train release)
- ~20GB at 4-bit quantization (~60GB BF16), DFlash speculative-decoding drafter, 128K context
- Artificial Analysis Intelligence Index 35 (behind Qwen3.6-27B's 38, near Kimi K2.5's 36); Openness Index 44
- Weaker on hallucination/knowledge calibration and general agentic knowledge work vs. similarly-sized peers
- Muse Spark 1.2's own weights promised "soon" per Alexandr Wang
```
