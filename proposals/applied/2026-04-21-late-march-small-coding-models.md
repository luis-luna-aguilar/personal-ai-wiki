---
type: proposal
sources:
  - raw/newsletters/2026-03-19-minimax-m27-rivals-top-models.md
  - raw/newsletters/2026-03-20-cursor-drops-composer-2.md
  - raw/newsletters/2026-03-22-how-good-is-gpt-54-mini-and-nano.md
  - raw/newsletters/2026-03-23-supermemory-cracks-agent-memory.md
status: pending
created: 2026-04-21
---

# Proposal: Late-March small coding models

## Summary

The late-March model cluster adds a more opinionated picture of the "cheap but capable" coding-model tier. MiniMax M2.7 looks stronger than the current wiki gives it credit for on both agentic benchmarks and cost/performance, while Composer 2 moves from stub status to a real model page with benchmark claims, pricing claims, and the now-disclosed Kimi-k2.5 base-model lineage. The same batch also adds a useful negative signal: GPT-5.4 Mini and Nano were launched as small coding/agent models, but one source argues they underwhelm once token budgets and actual economics are considered.

## Intended changes

- [x] **Update** `wiki/state-of/models.md` — strengthen MiniMax's placement and add Composer 2 to `Coding models`
  > See snippet below.

- [x] **Update** `wiki/models/minimax-m2-7.md` — replace the thin early-April summary with the stronger late-March benchmark / economics picture
  > See snippet below.

- [x] **Update** `wiki/models/composer-2.md` — turn the stub into a proper model page with benchmarks, pricing claims, and disclosed Kimi-k2.5 lineage
  > See snippet below.

- [x] **Update** `wiki/tools/cursor.md` — make the Composer 2 relationship more concrete
  > See snippet below.

- [x] **Create** `wiki/sources/newsletters/late-march-small-coding-models.md` — grouped source summary page
  > See full draft below.

## Page drafts

### wiki/state-of/models.md (updated snippet)

```markdown
### Coding models

- [[models/kimi-k2-6]] — Moonshot AI; open-weight 1T-param MoE; open-source SOTA claims: HLE w/ tools 54.0, SWE-Bench Pro 58.6, SWE-bench Multilingual 76.7, BrowseComp 83.2; 4K+ tool calls, 12+ hour continuous runs *(as of 2026-04-21)*
- [[models/minimax-m2-7]] — MiniMax; 220B MoE coding / agent model; late-March sources describe unusually strong cost-performance: 56.22% SWE-Pro, 55.6% VIBE-Pro, native multi-agent collaboration, and roughly `$0.30 / $1.20` per million input/output tokens *(as of 2026-03-22)*
- [[models/composer-2]] — Cursor's in-house coding model; positioned for complex long-horizon coding tasks with reported 61.7 TerminalBench 2.0 and 73.7 SWE-bench Multilingual, plus unusually low input-token pricing inside Cursor; later disclosure says it starts from Moonshot's Kimi-k2.5 and adds continued pretraining plus RL *(as of 2026-03-23)*
- [[models/qwen-3-6-35b-a3b]] — Alibaba; open-weight MoE coding model increasingly described as the first practical local-agent baseline for roughly 24GB-class local hardware, such as a higher-memory MacBook Pro or comparable GPU setup *(as of 2026-04-21)*
- [[models/glm-5-1]] — open-weight contender described in the captured sources as a top benchmark performer for coding and agent workflows *(as of 2026-04-08)*

## Recent changes

- [2026-03-23] Late-March small-model cluster sharpened the affordable coding tier: MiniMax M2.7 looks stronger on practical economics, while Composer 2 graduated from a Cursor-only mention to a real model with benchmark and lineage claims
```

### wiki/models/minimax-m2-7.md (updated snippet)

```markdown
# MiniMax M2.7

MiniMax M2.7 is an open-weight coding and agent model that looks more consequential than the current page suggests. The strongest late-March signal is not only benchmark competitiveness, but economics: it is repeatedly framed as one of the most attractive "cheap but capable" models for agentic coding work.

## Current status (as of 2026-03-22)

- 220B-parameter MoE model positioned for coding and general agentic tasks
- MiniMax says an earlier checkpoint helped with 30-50% of the RL team's own workflows, framing the model as partially self-improving during development
- Reported benchmark claims include 56.22% on SWE-Pro and 55.6% on VIBE-Pro
- Source coverage also claims native multi-agent collaboration and 97% skill adherence across 40+ tools
- Pricing cited in the late-March sources is roughly `$0.30 / $1.20` per million input/output tokens, materially below several direct competitors

## Strengths

- Strong cost/performance signal for agentic coding workloads
- Benchmarks and product framing both emphasize tool-heavy work, not only static code completion
- Looks usable in real agent stacks, not only impressive on paper

## Weaknesses / caveats

- Most claims in the current source set are relayed through newsletters rather than a direct technical report
- The strongest criticism is indirect: if the pricing and token-efficiency comparison is correct, OpenAI's small-model tier looks weak against it, but that is still one practitioner's interpretation rather than settled consensus
```

### wiki/models/composer-2.md (updated snippet)

```markdown
# Composer 2

Composer 2 is Cursor's in-house coding model for complex long-horizon engineering work. It is no longer just a stub-level mention from the Cursor 3 launch: late-March sources add benchmark claims, pricing claims, and the now-disclosed fact that Cursor started from Moonshot's Kimi-k2.5 before doing continued pretraining and reinforcement learning.

## Current status (as of 2026-03-23)

- Cursor positions Composer 2 as its own model for complex, long-term coding tasks
- Reported benchmark claims: 61.7 on TerminalBench 2.0 and 73.7 on SWE-bench Multilingual
- Source coverage says it trails GPT-5.4 slightly, but beats Anthropic's Opus 4.6 on those cited coding benchmarks
- Launch pricing claim in the source set: about `$0.50` per million input tokens, roughly one-tenth of some frontier competitors
- Later source coverage says Cursor did not train it from scratch: the model reportedly starts from Moonshot's open Kimi-k2.5, then adds continued pretraining plus Cursor-specific finetuning / RL
- Available only inside Cursor products; no standalone API

## Strengths

- Clearer benchmark story than the original stub implied
- Integrated tightly into Cursor's agent workspace, so the model and product can co-evolve
- Low-cost positioning matters if the benchmark claims hold up in real usage

## Weaknesses / caveats

- Benchmarks and pricing come through secondary reporting in the captured source set
- The Kimi-k2.5 disclosure created credibility friction around the launch story
- Closed distribution makes independent evaluation harder than for open-weight peers
```

### wiki/tools/cursor.md (updated snippet)

```markdown
## Current status (as of 2026-04-14)

- Backed by [[models/composer-2|Composer 2]], Cursor's own coding model for complex long-horizon tasks; late-March coverage adds reported 61.7 TerminalBench 2.0, 73.7 SWE-bench Multilingual, low input-token pricing, and the now-disclosed Kimi-k2.5 base-model lineage
```

### wiki/sources/newsletters/late-march-small-coding-models.md (new)

```markdown
---
title: Late-March small coding models
type: source
source_type: newsletter
source_file: raw/newsletters/2026-03-19-minimax-m27-rivals-top-models.md
ingested: 2026-04-21
domains: [models, coding]
---

# Late-March small coding models

This source cluster covers the affordable-but-serious coding-model tier. The strongest signal is comparative: MiniMax M2.7 looks unusually strong on cost/performance, Composer 2 becomes legible as a real model rather than a product footnote, and GPT-5.4 Mini / Nano pick up a skeptical counter-reading on token economics.

## Influenced pages

- [[state-of/models]] — strengthens the affordable coding-model tier and adds Composer 2
- [[models/minimax-m2-7]] — adds benchmark and economics detail
- [[models/composer-2]] — turns the page from stub into a real current-state summary
- [[tools/cursor]] — makes the Composer 2 relationship more concrete

## Key claims extracted

- MiniMax M2.7 is presented as a 220B MoE coding / agent model with 56.22% SWE-Pro, 55.6% VIBE-Pro, and unusually low token pricing
- One late-March source argues GPT-5.4 Mini reaches the same practical neighborhood only by using much more reasoning budget and therefore much worse effective economics
- Composer 2 is reported at 61.7 on TerminalBench 2.0 and 73.7 on SWE-bench Multilingual
- Cursor later confirmed Composer 2 builds from Moonshot's Kimi-k2.5 plus continued training, which materially changes how the launch should be interpreted
- The practical contest is no longer only "best benchmark"; it is increasingly "best usable model per dollar and per reasoning token"
```
