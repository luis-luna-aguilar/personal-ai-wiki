---
type: proposal
source: raw/newsletters/2026-08-12-ainews-how-to-steal-a-reasoning-trace.md
status: pending
created: 2026-09-07
---

# Proposal: NVIDIA Nemotron 3.5 Lightning launch

## Summary

### The source

AINews's 2026-08-12 issue ("How to steal a Reasoning Trace") carries the Nemotron 3.5 Lightning launch as its second major story. NVIDIA released Lightning on 2026-08-11, a 31.6B-total/3.6B-active MoE under the OpenMDW-1.1 license, shipped with both NVFP4 and BF16 weights and positioned explicitly for always-on agent workloads rather than general chat. Artificial Analysis's independent numbers put it at Intelligence Index 24 — roughly gpt-oss-120b tier despite its much smaller size — with ~670 tok/s median serving in pre-release endpoint testing. Its agentic scores stand out for the size class: GDPval-AA v2 Elo 824 and Terminal-Bench v2.1 24%, both large jumps over the prior Nemotron 3 Nano. It shipped day-0 across Together AI, Ollama, Baseten, vLLM, and the Perplexity API. Harvey's own post-training case study is the sharpest data point: fine-tuning Lightning on their Legal Agent Bench took it from 0% to 8.3% on held-out tasks — beating both Claude Opus 4.6 and NVIDIA's own larger Nemotron 3 Ultra in that setup — while cutting average output from 90k to 37k tokens. Commentary framed the release as reinforcing a "cheap execution model paired with a stronger planner" pattern, with NVIDIA describing Lightning as a "local agent workforce" complementing bigger planning models via routing.

### What changes

The wiki already tracks NVIDIA's open-weight line via **Nemotron 3 Ultra** (550B/55B, NVIDIA's frontier-scale open-weight flagship), but has no page for its smaller, faster sibling.

- New page `wiki/models/nemotron-35-lightning.md` covering the launch, its per-size agentic benchmarks, and the Harvey post-training result.
- **State of Models** gains a new leader line for Nemotron 3.5 Lightning under Open-weight models, alongside Nemotron 3 Ultra; Recent changes gains a new entry dated 12 August, and since the section is at its 10-entry cap, the oldest live entry spills to history.
- New source page for this AINews issue, scoped to the Lightning launch content only.

### What to weigh

The same AINews issue also covers reasoning-trace theft, Claude's text/image watermarking, and desktop AI tooling — those are being proposed separately, so this proposal carries only the model-launch content. The benchmark numbers are third-party (Artificial Analysis, Harvey) rather than NVIDIA's own launch materials, but that matches the sourcing pattern already used for the Nemotron 3 Ultra entry it sits beside.

## Intended changes

- [x] **Approve all** — checking this box approves every item below.

- [ ] **Create** `wiki/models/nemotron-35-lightning.md` — new model page
    > See draft below

- [ ] **Update** `wiki/state-of/models.md` — add a leader line under Open-weight models; add a Recent-changes entry
    > See draft below

- [ ] **Spill** `wiki/state-of/models.md` → `wiki/history/state-of/models.md` — oldest Recent-changes entry falls off the 10-entry cap (currently `[2026-07-09] GPT-5.6 Sol reportedly cleared for public rollout...`; re-check what's actually oldest at apply time)

- [ ] **Create** `wiki/sources/newsletters/nvidia-nemotron-35-lightning-2026-08-12.md` — source summary

## Page drafts

### wiki/models/nemotron-35-lightning.md (new)

```md
---
title: Nemotron 3.5 Lightning
type: model
domains: [models]
subcategory: open-weight-model
tags: [open-weights, agentic]
as_of: 2026-08-12
sources: [nvidia-nemotron-35-lightning-2026-08-12]
---

# Nemotron 3.5 Lightning

NVIDIA's small, fast open-weight model for always-on agent workloads — a compact sibling to the larger [Nemotron 3 Ultra](nemotron-3-ultra.md), tuned for high-volume tool use rather than general chat.

## Current status (as of 2026-08-12)

- 31.6B total / 3.6B active MoE; OpenMDW-1.1 license; NVFP4 and BF16 weight releases
- Artificial Analysis Intelligence Index 24 — roughly gpt-oss-120b tier at a fraction of the size; ~670 tok/s median serving in pre-release testing
- Strong agentic results for its size: GDPval-AA v2 Elo 824, Terminal-Bench v2.1 24% — both large jumps over the prior Nemotron 3 Nano
- Harvey post-trained it on Legal Agent Bench: 0% to 8.3% on held-out tasks, beating Claude Opus 4.6 and Nemotron 3 Ultra in that setup while cutting average output from 90k to 37k tokens
- Day-0 availability across Together AI, Ollama, Baseten, vLLM, and Perplexity API

## Why it matters

Reinforces the pattern of pairing a cheap, fast execution model with a stronger planner via routing rather than chasing general-chat capability — NVIDIA is explicitly positioning Lightning as a "local agent workforce" complementing larger planning models.

## Recent changes

- [2026-08-12] Launched: initial benchmarks, day-0 provider support, and Harvey's Legal Agent Bench post-training result

## Sources

- [AINews — Nemotron 3.5 Lightning launch (2026-08-12)](../sources/newsletters/nvidia-nemotron-35-lightning-2026-08-12.md)
```

### wiki/state-of/models.md (updated)

Add to `### Open-weight models`, directly after the existing Nemotron 3 Ultra line:

```md
- [Nemotron 3.5 Lightning](../models/nemotron-35-lightning.md) — NVIDIA; 31.6B/3.6B active MoE; AA Intelligence Index 24, GDPval-AA v2 Elo 824, Terminal-Bench v2.1 24%; Harvey post-training took it 0%→8.3% on Legal Agent Bench, beating Opus 4.6 and Nemotron 3 Ultra; day-0 across Together AI, Ollama, Baseten, vLLM, Perplexity API *(as of 2026-08-12)*
```

Add to `## Recent changes` (top, newest-first):

```md
- [2026-08-12] Nemotron 3.5 Lightning (NVIDIA, 31.6B/3.6B active) added to Open-weight models: AA Intelligence Index 24, strong per-size agentic benchmarks, Harvey's Legal Agent Bench post-training result beating Opus 4.6 and Nemotron 3 Ultra.
```

Frontmatter `sources:` gains `nvidia-nemotron-35-lightning-2026-08-12`; `as_of` moves to 2026-08-12 if that is newer than the live value at apply time.

### wiki/history/state-of/models.md (updated)

Append the spilled oldest entry (re-derive which one is actually oldest at apply time) under the existing `## Archived from current page on 2026-09-07` header.

### wiki/sources/newsletters/nvidia-nemotron-35-lightning-2026-08-12.md (new)

```md
---
title: AINews — Nemotron 3.5 Lightning launch (2026-08-12)
type: source
source_type: newsletter
source_file: raw/newsletters/2026-08-12-ainews-how-to-steal-a-reasoning-trace.md
url: https://www.latent.space/p/ainews-how-to-steal-a-reasoning-trace
published: 2026-08-12
ingested: 2026-09-07
domains: [models]
---

# AINews — Nemotron 3.5 Lightning launch (2026-08-12)

NVIDIA released Nemotron 3.5 Lightning, a 31.6B/3.6B-active MoE positioned for always-on agent workloads, with strong per-size agentic benchmark results and day-0 support across major serving platforms; Harvey's post-training case study on Legal Agent Bench showed a 0%→8.3% jump beating both Claude Opus 4.6 and NVIDIA's own larger Nemotron 3 Ultra.

## Influenced pages
- [Nemotron 3.5 Lightning](../../models/nemotron-35-lightning.md) — new model page
- [State of Models](../../state-of/models.md) — new leader line under Open-weight models

## Key claims extracted
- 31.6B total / 3.6B active MoE, OpenMDW-1.1 license, NVFP4/BF16 weights
- AA Intelligence Index 24; ~670 tok/s median serving (pre-release)
- GDPval-AA v2 Elo 824; Terminal-Bench v2.1 24% — both major jumps over Nemotron 3 Nano
- Harvey: Legal Agent Bench 0%→8.3% post-training, beating Opus 4.6 and Nemotron 3 Ultra; average output cut from 90k to 37k tokens
- Day-0 on Together AI, Ollama, Baseten, vLLM, Perplexity API
```

## Open questions

None — the raw source's Nemotron section is self-contained and unambiguous.
