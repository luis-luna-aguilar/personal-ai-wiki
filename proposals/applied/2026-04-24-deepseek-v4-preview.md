---
type: proposal
sources:
  - raw/tweets/2026-04-24-deepseek_ai-2047516922263285776.md
  - raw/articles/2026-04-24-huggingfaceco-blog-deepseekv4.md
  - raw/newsletters/2026-04-24-openai-ships-its-most-agentic-model.md
  - raw/newsletters/2026-04-24-ainews-gpt-55-and-openai-codex-superapp.md
status: pending
created: 2026-04-24
---

# Proposal: DeepSeek V4 Preview

## Summary

DeepSeek V4 Preview looks material enough for the current-state wiki rather than a newsletter-only mention. The strongest reusable signal is not merely "1M context" as a headline, but that DeepSeek is explicitly pushing V4 as an open model built for long-running agent workloads: cheaper long-context inference, much smaller KV cache, interleaved thinking across tool calls, dedicated tool-call schema, and competitive agent benchmarks. This fits the existing `coding-model` lane more cleanly than the older generic DeepSeek framing.

## Intended changes

- [x] **Create** `wiki/models/deepseek-v4.md` — new coding/agent model page
- [x] **Update** `wiki/state-of/models.md` — add DeepSeek V4 to `Coding models`; bump `as_of`
- [x] **Update** `wiki/trends/open-weight-momentum-broadens.md` — extend the trend from early-April breadth into a stronger late-April signal around long-context agentic open models
- [x] **Update** `wiki/index.md` — add the model page and refresh the open-weight trend blurb
- [x] **Create** `wiki/sources/articles/deepseek-v4-preview.md` — source summary grounded mainly in the Hugging Face technical writeup, with the official DeepSeek launch tweet as supporting evidence

## Page drafts

### wiki/models/deepseek-v4.md (new)

````md
---
title: DeepSeek V4
type: model
domains: [models, coding, agents]
subcategory: coding-model
tags: [open-weights, agentic]
as_of: 2026-04-24
sources: [deepseek-v4-preview]
---

# DeepSeek V4

DeepSeek's April 2026 preview release for long-context open agent workloads. The key claim is not only bigger context, but cheaper usable context: V4 is explicitly optimized for long-running tool-use traces and agent loops, with much lower KV-cache cost and stronger multi-step tool behavior than the prior generation.

## Current status (as of 2026-04-24)

- Preview release with two open-weight checkpoints: **V4-Pro** (1.6T total / 49B active) and **V4-Flash** (284B total / 13B active)
- 1M-token context window; positioning is heavily agent-oriented rather than only chatbot-oriented
- Hugging Face technical analysis highlights major efficiency gains vs DeepSeek-V3.2: lower per-token FLOPs and much smaller KV cache at long context
- Competitive agent results rather than clean category leadership: Terminal Bench 2.0 67.9, SWE Verified 80.6, MCPAtlas Public 73.6, Toolathlon 51.8
- Uses explicit tool-use shaping: interleaved thinking across tool rounds, a dedicated tool-call schema, and RL infrastructure tuned for sandboxed agent training

## Strengths

- Strongest current DeepSeek signal for long-horizon agent traces rather than only static coding prompts
- Open-weight release with unusually serious attention to long-context economics
- Competitive with frontier closed models on several agent benchmarks without needing a proprietary-only deployment story

## Weaknesses / caveats

- Still a preview release
- Benchmark framing is mixed: competitive, but not obvious state-of-the-art across the board
- Current technical detail comes more from the Hugging Face analysis of the release than from a full first-party DeepSeek blog post in this source set

## Recent changes

- [2026-04-24] Preview released: DeepSeek moves its open-model story toward 1M-context agent workloads, hybrid attention for cheaper long traces, and stronger tool-use positioning

## Sources

- [[sources/articles/deepseek-v4-preview]]
````

### wiki/state-of/models.md (update — diff only)

> **Add under `### Coding models`:**
> ```markdown
> - [[models/deepseek-v4]] — DeepSeek; preview open-weight MoE release built explicitly for long-context agent traces; 1M context, much cheaper KV-cache behavior than prior DeepSeek, and competitive agent benchmark results *(as of 2026-04-24)*
> ```
>
> **Add to `## Recent changes` (prepend):**
> `- [2026-04-24] Added [[models/deepseek-v4]] under \`Coding models\`; DeepSeek's open-weight story now centers on long-context agent workloads, not just cheaper general reasoning`

### wiki/trends/open-weight-momentum-broadens.md (update — diff only)

> **Update frontmatter:**
> - `as_of: 2026-04-24`
> - append `deepseek-v4-preview` to `sources`

> **Replace `## Current signal` bullets with a version that adds:**
> ```markdown
> - **DeepSeek V4** is the clearest late-April signal that open-weight competition is not only broadening, but maturing into serious long-context agent infrastructure. The release emphasizes usable 1M-token traces, lower KV-cache cost, and better tool-use loops rather than only static benchmark wins.
> ```
>
> **Add to `## Recent changes`:**
> `- [2026-04-24] DeepSeek V4 Preview strengthens the trend: open-weight competition now includes explicit architectural work for long-running agent traces, not just cheaper coding models`

### wiki/index.md (update — diff only)

> **Add under `## Models`:**
> ```markdown
> - [[models/deepseek-v4]] — DeepSeek preview release for long-context open agent workloads; 1M context, lower KV-cache cost, and competitive agent benchmark results *(as_of: 2026-04-24)*
> ```
>
> **Update `trends/open-weight-momentum-broadens`:**
> ```markdown
> - [[trends/open-weight-momentum-broadens]] — open-weight competition is spreading beyond coding into multimodal, computer-use, and now more serious long-context agent systems *(as_of: 2026-04-24)*
> ```

### wiki/sources/articles/deepseek-v4-preview.md (new)

````md
---
title: DeepSeek V4 Preview
type: source
source_type: article
source_file: raw/articles/2026-04-24-huggingfaceco-blog-deepseekv4.md
url: https://huggingface.co/blog/deepseekv4
published: 2026-04-24
ingested: 2026-04-24
domains: [models, coding, agents]
---

# DeepSeek V4 Preview

Technical writeup of DeepSeek V4's release, focused on why the model matters for agent workloads rather than just headline benchmark numbers. The central claim is that DeepSeek is attacking the long-context economics problem directly: lower KV-cache footprint, lower per-token inference cost at depth, and post-training choices explicitly tuned for tool-using agents.

## Influenced pages

- [[models/deepseek-v4]] — new page for the release
- [[state-of/models]] — new `Coding models` entry
- [[trends/open-weight-momentum-broadens]] — extends the trend into long-context open agent systems

## Key claims extracted

- DeepSeek V4 ships as V4-Pro and V4-Flash with 1M-token context
- V4 is explicitly framed for long-running agent workflows, not only general chat
- Relative to DeepSeek-V3.2, long-context inference uses much less KV cache and fewer FLOPs per token
- Agent-specific shaping includes preserved reasoning across tool turns, a dedicated tool-call schema, and RL infrastructure for sandboxed tool-use training
- Reported agent benchmarks are competitive with frontier closed models even if not category-leading across every metric
````
