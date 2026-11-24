---
type: proposal
source: raw/newsletters/2026-10-21-ainews-deepseek-deepinfer-open-source-sota-infe.md
sources:
  - raw/newsletters/2026-10-21-ainews-deepseek-deepinfer-open-source-sota-infe.md
  - raw/newsletters/2026-10-22-ainews-openais-patch-the-planet-program-is-1-of.md
status: pending
created: 2026-11-24
---

# Proposal: DeepSeek DeepInfer and open inference serving (TorchTPU, EAGLE-4, 12-hour prompt caching)

## Summary

### In short
Serving cached tokens to agents looks like a high-margin business, and the stack that does it is now largely open: DeepSeek open-sourced DeepInfer, the engine behind V4.1 Flash, and reported $38 of revenue per accelerator-hour with 96% of input tokens served from cache. Outside estimates put accelerator-only margins at roughly 74–87%, and vLLM matched DeepInfer's decode speed within 6%. The proposal adds a serving-stack section to the DeepSeek V4.1 Flash page, an open-inference bullet (with Google's TorchTPU and EAGLE-4) to the compute-infrastructure trend, and a caching update to Agent execution runtimes. The reason to hesitate: DeepSeek's own report and repository were not read.

[[#Open questions|Open questions: 1 to answer.]]

- [x] **Approve all** — checking this box approves every item in `## Intended changes` and `## Schema / vocabulary additions` below; the individual boxes may stay empty.

### The source
On 20 October 2026, the first day of PyTorch Conference, DeepSeek released DeepInfer under Apache 2.0: the inference engine that serves its V4.1 Flash model, derived from vLLM and running on NVIDIA's newest (SM100) chips and Huawei's Ascend 950. With it came `deepseek-recipe`, a Rust library that speaks the Chat Completions, Responses and Messages API formats, and an engineering report. AINews led its 21 October issue with the release, and its 22 October issue added follow-ups. Both are the sources here.

The design centres on caching. The reusable part of each conversation (the KV cache, the model's working memory of a prompt) is stored in blocks on a roughly 100-petabyte SSD cluster, kept three days for agent traffic and seven for chat, so any prefill server can pick up any cached prefix. A trick called SWA Bounded Replay rebuilds short-lived attention state from only the last 128 tokens, which DeepSeek says nearly halves prefill compute. Adaptive speculative decoding (a small draft model guesses tokens for the big one to verify) adds 6% throughput. The report claims 155 trillion tokens a day from one cluster, 96% input-cache hits, 400 ms to first token, 230 tokens a second (300 for coding), and $38 revenue per accelerator-hour at off-peak prices. Commentators turned that into margins of about 74–87% at $5–10 an hour hardware cost, before storage, networking, staff and idle capacity. Two caveats come with it: KV-cache management, prefill/decode separation and load balancing are not fully released, and vLLM's within-6% result covers decode only, not the whole service.

Three related items arrived the same week. OpenAI announced 12-hour prompt-cache retention in its API, against a 30-minute default, aimed at long agent sessions. Google open-sourced TorchTPU for native PyTorch on its TPUs, and SGLang's plugin for it reportedly runs production inference at Meta. EAGLE-4, a source-available speculative decoder, claims 3.59x over plain decoding on Qwen3.8-27B, with gains shrinking under load.

### What changes
The V4.1 Flash page covers the model's architecture and rankings but not how DeepSeek serves it; the compute-infrastructure page names DSpark and vLLM as an inference-efficiency counterforce without numbers; Agent execution runtimes lists OpenAI's 12-hour cache tier as a DevDay preview.

- **DeepSeek V4.1 Flash** gains a "Serving stack (DeepInfer)" section and one Recent-changes entry.
- **Compute infrastructure as decisive competitive moat** gains one Current-status bullet on open inference stacks and serving economics, and one Recent-changes entry; the list is at its cap, so the oldest entry moves to history. Its page date stays 20 November, since the Anthropic S-1 material is newer. The page goes from 110% to about 119% of its 1,200-word ceiling.
- **Agent execution runtimes** updates its 12-hour cache sentence and gains one Recent-changes entry.
- The index refreshes two lines; two new source pages, one per AINews story.

### What to weigh
DeepSeek's GitHub repository and English technical report were not fetched; every DeepInfer figure comes through AINews's summary of them, so this is a partial source. The margin range is commentators' arithmetic, and the drafts label it as such rather than as a DeepSeek disclosure.

## Intended changes

- [ ] **Update** `wiki/models/deepseek-v4-1-flash.md` — insert a `## Serving stack (DeepInfer)` section before `## Weaknesses / caveats`; add one Recent-changes entry dated 2026-10-20 (list at 2, no spill); append source id `ainews-deepseek-deepinfer-2026-10-21` and one Sources line; `as_of` unchanged (2026-10-20)
    > See draft below

- [ ] **Update** `wiki/trends/compute-infrastructure.md` — add one bullet to `## Current status`, after the "Open-model ecosystems are using serving and decode speed" bullet; Current-status heading and `as_of` stay 2026-11-20 (newer than this source); add one Recent-changes entry dated 2026-10-22, between the 2026-11-20 and 2026-08-19 entries (list at the 10-entry cap, so the oldest entry spills); append two source ids and two Sources lines; page goes from 110% to about 119% of its ceiling
    > See draft below

- [ ] **Spill** `wiki/trends/compute-infrastructure.md` → `wiki/history/trends/compute-infrastructure.md` — the oldest Recent-changes entry moves to history: two entries are dated 2026-05-05, and the lower one (Parallel Web Systems' $2B raise) spills (the Superhuman entry already spilled today)
    > See draft below

- [ ] **Update** `wiki/concepts/agent-execution-runtimes.md` — revise one sentence in the "Model-lab agent APIs" bullet; add one Recent-changes entry dated 2026-10-20 (list at 7, no spill); append source id and Sources line; `as_of` unchanged (2026-11-23)
    > See draft below

- [ ] **Update** `wiki/index.md` — refresh the deepseek-v4-1-flash and compute-infrastructure lines
    > See draft below

- [ ] **Create** `wiki/sources/newsletters/ainews-deepseek-deepinfer-2026-10-21.md` — source summary (AINews DeepInfer lead story)

- [ ] **Create** `wiki/sources/newsletters/ainews-inference-systems-2026-10-22.md` — source summary (AINews Inference Systems story: TorchTPU, EAGLE-4, cache accounting)

## Page drafts

### wiki/models/deepseek-v4-1-flash.md (updated)

Frontmatter (changed field):

```md
sources: [ainews-deepseek-v4-1-flash-architecture-2026-10-15, ainews-deepseek-v4-1-flash-1017-2026-10-20, ainews-deepseek-deepinfer-2026-10-21]
```

New section, inserted before `## Weaknesses / caveats`:

```md
## Serving stack (DeepInfer)

On 2026-10-20 DeepSeek open-sourced DeepInfer (Apache 2.0), the vLLM-derived engine that serves V4.1 Flash on NVIDIA SM100 and Huawei Ascend 950, plus `deepseek-recipe`, a Rust library for Chat Completions, Responses and Messages API formats. KV-cache management, prefill/decode disaggregation and load balancing are not fully released.

- **Cache design:** block KV cache on a ~100 PiB 3FS SSD cluster (kept 3 days for agent traffic, 7 for chat), so any prefill worker can serve any cached prefix; SWA Bounded Replay rebuilds short-lived sliding-window state from the last 128 tokens and nearly halves prefill compute; DSpark adaptive speculative decoding adds 6% over a fixed five-token draft.
- **Reported production figures:** 155T tokens a day from one cluster, 96% input-cache hits, 400 ms average time to first token, 230 tok/s (300 for coding), $38 revenue (not profit) per accelerator-hour at off-peak prices.
- **Reproduction:** vLLM reported decode throughput within 6% of DeepInfer on GB200 under a matched configuration; that covers decode, not the whole cached service.
```

Recent changes (adds one entry at the top):

```md
- [2026-10-20] DeepSeek open-sourced DeepInfer, the V4.1 Flash serving engine: 3-day agent KV cache on SSD, 96% input-cache hits, $38 revenue per accelerator-hour off-peak; vLLM matched its decode throughput within 6%.
```

Sources (appends one line):

```md
- [AINews — DeepSeek DeepInfer open-sources its production inference stack (21 October 2026)](../sources/newsletters/ainews-deepseek-deepinfer-2026-10-21.md)
```

### wiki/trends/compute-infrastructure.md (updated)

Frontmatter (changed fields): `as_of` unchanged (2026-11-20); append `ainews-deepseek-deepinfer-2026-10-21, ainews-inference-systems-2026-10-22` to `sources:`.

Heading unchanged: `## Current status (as of 2026-11-20)`.

New bullet, inserted after the "Open-model ecosystems are using serving and decode speed as adoption levers" bullet:

```md
- Production-grade inference serving is going open source, and its economics are now partly visible. DeepSeek's DeepInfer (October 2026), the engine behind [V4.1 Flash](../models/deepseek-v4-1-flash.md), reports $38 revenue per accelerator-hour off-peak with 96% of input tokens served from a 3-day SSD cache; commentators' accelerator-only margin estimates run about 74–87% at $5–10/hr hardware cost, before storage, networking and staff, and depend on that cache-heavy token mix. vLLM matched its decode throughput within 6%. In the same week Google open-sourced TorchTPU (native PyTorch on TPU; SGLang's plugin reportedly serves production inference at Meta), and EAGLE-4 claimed 3.59x over plain decoding on Qwen3.8-27B with gains shrinking at higher concurrency.
```

Recent changes (adds one entry in date order; the oldest entry spills):

```md
- [2026-10-22] Added open inference serving: DeepSeek's DeepInfer ($38 revenue per accelerator-hour, 96% cache hits, commentators' 74–87% accelerator-only margins), vLLM's within-6% decode match, Google's TorchTPU and EAGLE-4 speculative decoding.
```

(Inserted below the 2026-11-20 entry and above the 2026-08-19 entry. The lower 2026-05-05 entry, Parallel Web Systems, is removed from the live list.)

Sources (appends two lines):

```md
- [AINews — DeepSeek DeepInfer open-sources its production inference stack (21 October 2026)](../sources/newsletters/ainews-deepseek-deepinfer-2026-10-21.md)
- [AINews — Inference systems: DeepInfer economics, TorchTPU, EAGLE-4 (22 October 2026)](../sources/newsletters/ainews-inference-systems-2026-10-22.md)
```

### wiki/history/trends/compute-infrastructure.md (updated)

Appended to the existing `## Archived from current page on 2026-11-24` block at the end of the file (or a new block with the apply date if that differs):

```md
- [2026-05-05] Parallel Web Systems raised at a $2B valuation (secondary coverage) for internet/research APIs optimized for AI agents — market signal that agent-oriented web access infrastructure is becoming a standalone investable category
```

### wiki/concepts/agent-execution-runtimes.md (updated)

Frontmatter: append `ainews-deepseek-deepinfer-2026-10-21` to `sources:` (`as_of` stays 2026-11-23).

In the "Model-lab agent APIs" bullet, replace this clause:

```md
guaranteed 30-minute cache hits with a paid 12-hour tier in preview for single long-lived agent threads,
```

with:

```md
guaranteed 30-minute cache hits with a 12-hour retention tier for long-lived agent threads (previewed at DevDay, announced for the API around 2026-10-20, with mixed retention durations allowed within one request; DeepSeek's DeepInfer keeps agent prefixes for three days),
```

Recent changes (adds one entry, inserted by date between the 2026-10-07 and 2026-09-30 entries):

```md
- [2026-10-20] OpenAI's 12-hour prompt-cache retention announced for the API (30-minute default), aimed at long agent sessions; DeepSeek's open DeepInfer keeps agent KV prefixes for three days.
```

Sources (appends one line):

```md
- [AINews — DeepSeek DeepInfer open-sources its production inference stack (21 October 2026)](../sources/newsletters/ainews-deepseek-deepinfer-2026-10-21.md)
```

### wiki/index.md (updated)

```md
- [models/deepseek-v4-1-flash](models/deepseek-v4-1-flash.md) — DeepSeek's current low-cost open-weight model: 552B/16B encoder-decoder MoE plus Engram memory, MIT, 1M context; 1017 build AA Intelligence Index 45, #1 open on Code Arena WebDev, Agent Arena and Vals; eval-cheating caveats; open-sourced DeepInfer serving stack (3-day SSD KV cache, $38/accelerator-hour) *(as_of: 2026-10-20)*
```

```md
- [trends/compute-infrastructure](trends/compute-infrastructure.md) — frontier compute scale plus inference-system efficiency as competitive moats; lab economics including Anthropic's S-1 and IPO; open inference serving (DeepInfer economics, TorchTPU, EAGLE-4) *(as_of: 2026-11-20)*
```

### wiki/sources/newsletters/ainews-deepseek-deepinfer-2026-10-21.md (new)

```md
---
title: AINews — DeepSeek DeepInfer open-sources its production inference stack (21 October 2026)
type: source
source_type: newsletter
source_file: raw/newsletters/2026-10-21-ainews-deepseek-deepinfer-open-source-sota-infe.md
url: https://www.latent.space/p/ainews-deepseek-deepinfer-open-source
published: 2026-10-21
ingested: 2026-11-24
domains: [models, agents]
---

# AINews — DeepSeek DeepInfer open-sources its production inference stack (21 October 2026)

AINews's lead story on DeepSeek releasing DeepInfer, the inference engine behind V4.1 Flash, with an engineering report on its production serving: architecture, cache hierarchy, speculative decoding, reported production figures, vLLM's comparison and the debate over what the revenue figure implies for margins. Also notes OpenAI's 12-hour API prompt caching.

## Influenced pages

- [DeepSeek V4.1 Flash](../../models/deepseek-v4-1-flash.md) — new Serving stack section
- [Compute infrastructure as decisive competitive moat](../../trends/compute-infrastructure.md) — open inference serving and its economics
- [Agent execution runtimes](../../concepts/agent-execution-runtimes.md) — 12-hour prompt-cache retention

## Key claims extracted

- DeepInfer (Apache 2.0, vLLM-derived) released 2026-10-20 with `deepseek-recipe` for Chat Completions, Responses and Messages API processing; supports NVIDIA and Huawei Ascend
- KV-cache management and load balancing are not fully released because they are coupled to internal infrastructure
- Block KV cache on a ~100 PiB 3FS SSD cluster, retained 3 days for agent traffic and 7 for chat; any prefill worker can serve any cached prefix
- SWA Bounded Replay rebuilds short-lived state from the last 128 tokens, nearly halving prefill compute
- DSpark adaptive speculative decoding: +6% throughput over always verifying five draft tokens
- Reported: 155T tokens/day from one cluster, 96% input-cache hits, 400 ms average TTFT, 230 tok/s (300 for coding), $38 revenue per accelerator-hour off-peak
- vLLM: decode throughput within 6% of DeepInfer on GB200 under a matched configuration (decode only, not the whole service)
- Commentators' accelerator-only margins: about 73.7–86.8% at $5–10/hr; estimates omit SSD fleet, CPUs, networking, idle capacity and staff, and depend on the cache-heavy token mix
- OpenAI announced 12-hour API prompt-cache retention against a 30-minute default, with mixed retention durations within a request
```

### wiki/sources/newsletters/ainews-inference-systems-2026-10-22.md (new)

```md
---
title: AINews — Inference systems: DeepInfer economics, TorchTPU, EAGLE-4 (22 October 2026)
type: source
source_type: newsletter
source_file: raw/newsletters/2026-10-22-ainews-openais-patch-the-planet-program-is-1-of.md
url: https://www.latent.space/p/ainews-openais-patch-the-planet-program
published: 2026-10-22
ingested: 2026-11-24
domains: [models]
---

# AINews — Inference systems: DeepInfer economics, TorchTPU, EAGLE-4 (22 October 2026)

The inference-systems story from AINews's 2026-10-22 issue (the "Inference Systems" section plus the r/LocalLlama recap): follow-up accounting on DeepInfer's throughput figures, Google's open-source TorchTPU, and the EAGLE-4 speculative decoder.

## Influenced pages

- [Compute infrastructure as decisive competitive moat](../../trends/compute-infrastructure.md) — TorchTPU and EAGLE-4 in the open inference serving bullet

## Key claims extracted

- DeepInfer's 1.5M input tokens/s per prefill accelerator includes cache hits; excluding them it is about 60K at a 96% hit rate; decode about 14K output tokens/s per accelerator
- Google open-sourced TorchTPU for training and serving through PyTorch tooling; SGLang's TorchTPU plugin reportedly powers production inference at Meta; vLLM-TorchTPU adds prefix caching, speculative decoding and disaggregated serving
- EAGLE-4: source-available speculative decoding with hardware/workload-calibrated draft trees; claimed 3.59x over vanilla decoding on Qwen3.8-27B (vs 2.57x DSpark, 2.80x DFlash 2); gains shrink at higher concurrency; draft model about 3 GB larger than DFlash2
```

## Schema / vocabulary additions

None.

## Open questions

- **Compute infrastructure** lands at about 119% of its 1,200-word trend ceiling (1,320 live body words plus about 105). That is above the 110% warning band but under the 150% line where a split is required. Split it now? The natural cut is `## Lab and subscription economics` (about 390 words, including the Anthropic S-1 subsection) into its own trend page on frontier-lab economics, leaving a one-paragraph pointer; that would bring the page back to about 86%. Assumed not in this proposal.
	- No, keep like this
