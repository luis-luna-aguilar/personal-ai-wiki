---
type: proposal
source: raw/newsletters/2026-04-25-ainews-deepseek-v4-pro-16t-a49b-and-flash-28.md
status: pending
created: 2026-04-25
---

# Proposal: AINews DeepSeek V4 release follow-through

## Summary

The AINews issue turns the prior DeepSeek V4 preview signal into a fuller release picture: V4 Pro and V4 Flash are now described as released open-weight models with clearer specs, pricing, 1M-token context, MIT licensing, and fast ecosystem support. The durable update is not "DeepSeek is the overall best model"; it is that DeepSeek is becoming a serious open-weight long-context and agent-inference systems player while still trailing the strongest closed frontier models in aggregate.

## Intended changes

- [x] **Update** `wiki/models/deepseek-v4.md` - change the page from preview framing to release framing; add pricing, MIT license, independent benchmark placement, token-cost caveat, and Ascend/Huawei compatibility.

- [x] **Update** `wiki/state-of/models.md` - refresh the DeepSeek V4 coding-model line and top recent-change entry.

- [x] **Update** `wiki/trends/open-weight-momentum-broadens.md` - sharpen the trend from "preview strengthens the trend" to "released Pro/Flash lineup strengthens the trend."

- [x] **Create** `wiki/sources/newsletters/ainews-2026-04-25.md` - source summary for the AINews issue.

## Page drafts

### `wiki/models/deepseek-v4.md` diff

```md
---
title: DeepSeek V4
type: model
domains: [models, coding, agents]
subcategory: coding-model
tags: [open-weights, agentic]
as_of: 2026-04-25
sources: [deepseek-v4-preview, ainews-2026-04-25]
---

# DeepSeek V4

DeepSeek's April 2026 open-weight release for long-context agent workloads. The key contribution is not a clean overall frontier win, but a serious systems design point: V4 pairs competitive open-model capability with 1M-token context, much lower KV-cache pressure, explicit tool-use shaping, and a Pro/Flash split for different cost/performance needs.

## Current status (as of 2026-04-25)

- Released as **V4 Pro** (1.6T total / 49B active) and **V4 Flash** (284B total / 13B active), with base and instruct variants, 1M-token context, and MIT licensing
- V4 Pro is now positioned near the top of open weights, but still below GPT-5.x / Claude Opus 4.7 / Gemini 3.1 Pro in aggregate closed-frontier comparisons
- Independent benchmark synthesis in AINews places V4 Pro as a leading open model for agentic real-world work, while also noting very high token usage in some evaluations
- First-party API pricing reported in the AINews issue: V4 Pro at `$1.74 / $3.48` per 1M input/output tokens, V4 Flash at `$0.14 / $0.28`
- Huawei Ascend compatibility and rapid vLLM / third-party support make the release part of a broader inference-substrate story, not just a checkpoint drop

## Strengths

- Serious open-weight long-context release with unusually concrete attention to KV-cache and long-trace economics
- Flash tier may matter more for practical adoption than Pro in workloads where 1M context and low per-token price dominate
- Competitive with top open-weight coding/agent models while exposing a richer technical report than many frontier releases

## Weaknesses / caveats

- Still behind the strongest closed frontier systems overall according to the captured independent benchmark framing
- Cheap per-token pricing does not guarantee cheap tasks; AINews highlights evaluations where V4 emitted very large token volumes
- Architecture complexity may limit how much the wider open ecosystem can reproduce the training-side gains, even if inference support spreads quickly

## Recent changes

- [2026-04-25] AINews follow-up reframed DeepSeek V4 from preview to release: Pro/Flash specs, MIT license, API pricing, independent open-model placement, Huawei Ascend compatibility, and token-volume caveats
- [2026-04-24] Preview released: DeepSeek moves its open-model story toward 1M-context agent workloads, hybrid attention for cheaper long traces, and stronger tool-use positioning

## Sources

- [[sources/articles/deepseek-v4-preview]]
- [[sources/newsletters/ainews-2026-04-25]]
```

### `wiki/state-of/models.md` diff

```md
---
title: State of Models
type: state-of
domains: [models]
tags: []
as_of: 2026-04-25
sources: [muse-spark, kimi-k2-6-blog, ainews-2026-04-21, ainews-2026-04-22, every-opus-4-7-vibe-check, vectorlab-opus-4-7-flop, vectorlab-qwen-3-6-local-threshold, open-agentic-coding-models, restricted-frontier-deployment, open-weight-momentum-early-april, late-march-small-coding-models, gpt-5-4-march, qwen-3-5-medium-february, glasswing, nano-banana-2-tweet, google-cloud-next-2026, openai-gpt-5-5-launch, danshipper-gpt-5-5-vibe-check, deepseek-v4-preview, ainews-2026-04-25]
---

### Coding models

- [[models/deepseek-v4]] - DeepSeek; released open-weight Pro/Flash MoE lineup with 1M context, MIT license, strong open-model agentic benchmark placement, and a major KV-cache / inference-systems story; still below the strongest closed frontier systems overall *(as of 2026-04-25)*

## Recent changes

- [2026-04-25] DeepSeek V4 moved from preview to release framing: Pro/Flash specs, MIT license, API pricing, independent open-model placement, Ascend compatibility, and token-usage caveats
```

### `wiki/trends/open-weight-momentum-broadens.md` diff

```md
---
title: Open-weight momentum broadens
type: trend
domains: [models, computer-use]
tags: [open-weights, google]
as_of: 2026-04-25
sources: [open-weight-momentum-early-april, deepseek-v4-preview, ainews-2026-04-25]
---

## Current signal

- **DeepSeek V4** is the clearest late-April signal that open-weight competition is not only broadening, but maturing into serious long-context agent infrastructure. The released Pro/Flash lineup combines 1M-token context, MIT licensing, first-party API pricing, rapid serving support, and a concrete KV-cache/inference story; the caveat is that the best closed frontier systems still lead in aggregate capability.

## Recent changes

- [2026-04-25] DeepSeek V4 release follow-through adds Pro/Flash specs, MIT license, pricing, Huawei Ascend compatibility, and independent benchmark placement to the earlier preview signal
- [2026-04-24] DeepSeek V4 Preview strengthens the trend: open-weight competition now includes explicit architectural work for long-running agent traces, not just cheaper coding models
```

### `wiki/sources/newsletters/ainews-2026-04-25.md` draft

```md
---
title: AINews - DeepSeek V4 Pro and Flash
type: source
source_type: newsletter
source_file: raw/newsletters/2026-04-25-ainews-deepseek-v4-pro-16t-a49b-and-flash-28.md
url: https://www.latent.space/p/ainews-deepseek-v4-pro-16t-a49b-and
published: 2026-04-25
ingested: 2026-04-25
domains: [models, agents]
---

# AINews - DeepSeek V4 Pro and Flash

AINews synthesis of the DeepSeek V4 release and surrounding reaction. The issue treats V4 as a serious open-weight long-context and agent-inference release: V4 Pro and V4 Flash ship with 1M-token context, MIT licensing, first-party pricing, rapid ecosystem support, and Huawei Ascend compatibility, while independent benchmark framing still places V4 below the strongest closed frontier systems overall.

## Influenced pages

- [[models/deepseek-v4]] - release framing, specs, pricing, benchmark placement, and caveats
- [[state-of/models]] - updated DeepSeek V4 coding-model line
- [[trends/open-weight-momentum-broadens]] - stronger open-weight long-context / inference-stack signal

## Key claims extracted

- V4 Pro is 1.6T total / 49B active; V4 Flash is 284B total / 13B active
- Both support 1M-token context and are described as MIT-licensed
- V4 Pro is near the top of open weights, but not a clean overall closed-frontier leader
- V4's most durable contribution may be long-context KV-cache and inference efficiency rather than benchmark rank alone
- Token volume remains a practical cost caveat despite attractive per-token pricing
```

## Schema / vocabulary additions

None.

## Open questions

- Should the wiki keep DeepSeek V4 as one family page, or split Pro and Flash into separate pages if later sources show materially different adoption patterns?
	- Lets keep it as one family page.
