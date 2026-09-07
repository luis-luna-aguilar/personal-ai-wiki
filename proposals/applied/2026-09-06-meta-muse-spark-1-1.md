---
type: proposal
sources:
  - raw/newsletters/2026-07-10-chatgpt-gets-a-work-focused-agent.md
  - raw/newsletters/2026-07-10-gpt-56-beats-fable-5-on-coding.md
  - raw/newsletters/2026-07-11-ainews-not-much-happened-today.md
status: pending
created: 2026-09-06
---

# Proposal: Meta Muse Spark 1.1 — Meta's first paid model

## Summary

### The source

Around 9 July 2026, in the same week as GPT-5.6's launch, Meta Superintelligence Labs quietly shipped Muse Spark 1.1 on a new "Meta Model API" — and for the first time, Meta is charging per token for it. Every prior Meta model has been free open weights (Llama); this one is closed and metered, a real strategic pivot that Meta's own AI chief Alexandr Wang called "very aggressive and attractive" pricing when compared to other frontier models. It's positioned for agentic tasks, coding, and computer use, with a 1M-token context window built for long multi-step work.

Independent numbers are modest rather than frontier-leading: Artificial Analysis scored it 51 on its Intelligence Index (up 8 points from Muse Spark 1.0), which puts it roughly level with GLM-5.2/GPT-5.4/GPT-5.6 Luna and behind Grok 4.5, GPT-5.6 Sol, and Fable 5. Pricing is $1.25/$4.25 per million tokens, median speed ~114 tok/s. Arena placed it #9 on Code Arena: Frontend. Meta's own claims go further — competitiveness with GPT-5.5 and Opus 4.8 on agentic evals, and particular strength on Harvey's Legal Bench, TaxEval, and MedScribe — but those are self-reported and not yet corroborated independently.

### What changes

The wiki's `models/muse-spark.md` page currently only knows the original Muse Spark (Meta's April scaling-philosophy announcement) and July's separate Muse Image/Video launch — nothing about a 1.1 version, paid pricing, or the Meta Model API. This proposal:

- **Muse Spark** gains a new dated section documenting 1.1's launch: the pivot to paid/metered access, the Meta Model API, the 1M context window, the AA Intelligence Index score (with the +8-point trajectory from 1.0), pricing, Arena placement, and Meta's own (unverified) benchmark claims. Page moves to 9 July.
- Three new source pages record the newsletters this draws from.
- `wiki/index.md`'s one-line Muse Spark description gets its date bumped to match.

### What to weigh

Every number beyond the AA Intelligence Index score and Arena placement is Meta's own claim, not independently verified — the draft attributes accordingly. The raw newsletters don't give an exact public launch date for 1.1 itself (only that AINews covered it in its 7/08–7/09 window); 2026-07-09 is inferred from that coverage window, one day off either way is plausible.

## Intended changes

- [x] **Approve all** — checking this box approves every item in `## Intended changes` and `## Schema / vocabulary additions` below; the individual boxes may stay empty.

- [ ] **Update** `wiki/models/muse-spark.md` — add a new "Muse Spark 1.1" section covering the paid Meta Model API launch, pricing, benchmarks, and Meta's own claims; bump `as_of` to 2026-07-09; add a Recent-changes entry; add the three new source ids
    > See draft below

- [ ] **Update** `wiki/index.md` — bump the Muse Spark line's date to match
    > See draft below

- [ ] **Create** `wiki/sources/newsletters/superhuman-chatgpt-work-muse-spark-2026-07.md` — source summary
- [ ] **Create** `wiki/sources/newsletters/the-code-gpt-56-beats-fable-coding-2026-07.md` — source summary
- [ ] **Create** `wiki/sources/newsletters/ainews-gpt-56-rollout-not-much-happened-2026-07-11.md` — source summary

## Page drafts

### wiki/models/muse-spark.md (updated)

Frontmatter:

```yaml
as_of: 2026-07-09
sources: [muse-spark, open-creative-workflows-2026-06, meta-muse-image-video-2026-07, superhuman-chatgpt-work-muse-spark-2026-07, the-code-gpt-56-beats-fable-coding-2026-07, ainews-gpt-56-rollout-not-much-happened-2026-07-11]
```

New section, inserted after "## Muse Image / Muse Video (as of 2026-07-08)" and before "## Recent changes":

```md
## Muse Spark 1.1 — Meta's first paid model (as of 2026-07-09)

Meta shipped Muse Spark 1.1 on a new "Meta Model API" — the first Meta model with per-token pricing rather than open weights, a pivot from its usual Llama approach. Superhuman reports AI chief Alexandr Wang called the pricing "very aggressive and attractive" against other frontier models; the pivot lands as Wall Street pressures Meta to justify its AI infrastructure spend.

- Positioned for agentic tasks, coding, and computer use; 1M-token context window (per The Code)
- Pricing: $1.25 / $4.25 per million input/output tokens; median speed ~114 tok/s (per Artificial Analysis, via AINews)
- Artificial Analysis Intelligence Index: 51, up 8 points from Muse Spark 1.0 — roughly level with GLM-5.2/GPT-5.4/GPT-5.6 Luna, behind Grok 4.5/GPT-5.6 Sol/Claude Fable 5 (per Artificial Analysis, via AINews)
- Arena: #9 on Code Arena: Frontend, with reported strength in instruction-following and longer-query categories (per Artificial Analysis, via AINews)
- Meta's own claims (unverified independently): competitive with GPT-5.5 and Opus 4.8 on agentic evals; strong on Harvey's Legal Bench, TaxEval, and MedScribe (per Superhuman/AINews relaying Meta)
```

Updated `## Recent changes` (full section, new entry inserted in date order above the 2026-07-08 entry):

```md
## Recent changes

- [2026-07-09] Muse Spark 1.1 launches on the new Meta Model API — Meta's first paid, metered model; AA Intelligence Index 51 (+8 vs 1.0); Arena #9 Code Arena: Frontend.
- [2026-07-08] Muse Image launches in Meta AI, Instagram Stories, and WhatsApp; Muse Video previewed; AINews describes an agentic planning/tool-use/self-refinement generation loop.
- [2026-06-24] Superhuman reports Meta Glasses launched with Muse Spark built in; secondary coverage only.
- [2026-04-10] Page created from Meta's Muse Spark introduction post
```

Updated `## Sources` (full section):

```md
## Sources

- [Introducing Muse Spark: Scaling Towards Personal Superintelligence](../sources/articles/muse-spark.md)
- [Open creative workflows and vibe directing](../sources/newsletters/open-creative-workflows-2026-06.md)
- [Meta Muse Image and Muse Video](../sources/newsletters/meta-muse-image-video-2026-07.md)
- [Superhuman — ChatGPT gets a work-focused agent (Muse Spark 1.1)](../sources/newsletters/superhuman-chatgpt-work-muse-spark-2026-07.md)
- [The Code — GPT-5.6 beats Fable 5 on coding (Muse Spark 1.1 detail)](../sources/newsletters/the-code-gpt-56-beats-fable-coding-2026-07.md)
- [AINews — GPT-5.6 rollout, not much happened today (Muse Spark 1.1 benchmarks)](../sources/newsletters/ainews-gpt-56-rollout-not-much-happened-2026-07-11.md)
```

### wiki/index.md (updated)

> **Before:** `- [models/muse-spark](models/muse-spark.md) — Meta multimodal model family; Muse Image/Video add agentic planning, tool use, code execution, and self-refinement before rendering *(as_of: 2026-07-08)*`
> **After:** `- [models/muse-spark](models/muse-spark.md) — Meta multimodal model family; Muse Image/Video add agentic planning, tool use, code execution, and self-refinement before rendering; Muse Spark 1.1 is Meta's first paid model *(as_of: 2026-07-09)*`

### wiki/sources/newsletters/superhuman-chatgpt-work-muse-spark-2026-07.md (new)

```md
---
title: "Superhuman — ChatGPT gets a work-focused agent"
type: source
source_type: newsletter
source_file: raw/newsletters/2026-07-10-chatgpt-gets-a-work-focused-agent.md
url: https://www.superhuman.ai/p/openai-launches-chatgpt-work-a-new-desktop-agent
published: 2026-07-10
ingested: 2026-09-06
domains: [models, agents]
---

# Superhuman — ChatGPT gets a work-focused agent

Superhuman's daily digest leading with OpenAI's ChatGPT Work launch, but also covering Meta's Muse Spark 1.1 as its first-ever paid model, PromptQL's relaunch, GPT-Live's voice upgrade, Anthropic's Claude "hidden thinking space" research, Muse Image's Arena #3 text-to-image ranking, and Chinese labs (Tencent Hy3, Meituan LongCat-2.0) closing the performance gap at lower cost.

## Influenced pages
- [Muse Spark](../../models/muse-spark.md) — Muse Spark 1.1 paid-model pivot

## Key claims extracted
- Muse Spark 1.1 is Meta's first paid model, built for agentic tasks, coding, and computer use, on a new Meta Model API
- Meta AI chief Alexandr Wang called Muse Spark 1.1's pricing "very aggressive and attractive" versus other frontier models
- The pivot comes as Wall Street pressures Meta to justify its AI infrastructure spend
- OpenAI separately launched ChatGPT Work (GPT-5.6-powered cross-app agent) and GPT-Live (a voice model family that listens and speaks simultaneously)
- Anthropic extended Claude Fable 5 access through July 12 and updated Cowork to work across devices
```

### wiki/sources/newsletters/the-code-gpt-56-beats-fable-coding-2026-07.md (new)

```md
---
title: "The Code — GPT-5.6 beats Fable 5 on coding"
type: source
source_type: newsletter
source_file: raw/newsletters/2026-07-10-gpt-56-beats-fable-5-on-coding.md
url: https://codenewsletter.ai/p/openai-unveils-gpt-5-6-meta-debuts-its-first-paid-ai-model
published: 2026-07-10
ingested: 2026-09-06
domains: [models, coding]
---

# The Code — GPT-5.6 beats Fable 5 on coding

The Code's daily digest leading with GPT-5.6's coding benchmarks, but also covering Meta's Muse Spark 1.1 launch, Entire's distributed Git network for coding agents, and Databricks' real-PR coding-agent cost benchmark.

## Influenced pages
- [Muse Spark](../../models/muse-spark.md) — Muse Spark 1.1 specs and positioning

## Key claims extracted
- Muse Spark 1.1 shipped alongside the Meta Model API, moving Meta from open-weight Llama releases to hosted, per-token pricing
- Built for long agentic tasks: plans across parallel subagents and manages a 1M-token context window
- Positioned to help "big projects finish faster"
```

### wiki/sources/newsletters/ainews-gpt-56-rollout-not-much-happened-2026-07-11.md (new)

```md
---
title: "[AINews] not much happened today (2026-07-11)"
type: source
source_type: newsletter
source_file: raw/newsletters/2026-07-11-ainews-not-much-happened-today.md
url: https://www.latent.space/p/ainews-not-much-happened-today-f5c
published: 2026-07-11
ingested: 2026-09-06
domains: [models, agents]
---

# AINews — not much happened today (2026-07-11)

AINews' recap of the day after GPT-5.6's launch: model-tier/effort-level confusion, ChatGPT Work/Codex UX regressions and usage resets, harness-centric competition framing, and Muse Spark 1.1's benchmark placement.

## Influenced pages
- [Muse Spark](../../models/muse-spark.md) — Muse Spark 1.1 AA Intelligence Index and Arena placement

## Key claims extracted
- Artificial Analysis scored Muse Spark 1.1 at 51 on its Intelligence Index, up 8 points from 1.0 — roughly tied with GLM-5.2/GPT-5.4/GPT-5.6 Luna, behind Grok 4.5/GPT-5.6 Sol/Claude Fable 5
- Notable specs: 1M context, median speed ~114 tok/s, pricing $1.25/$4.25 per million input/output tokens, strong token efficiency
- Arena placed it #9 on Code Arena: Frontend, with strong gains in instruction-following and longer-query categories
- Many practitioners called Muse Spark 1.1 the most surprising release of the week, citing strong UI/frontend generation, fast responses, and aggressive pricing
- Meta's compute-heavy bet is starting to show up as cost-effective inference products, raising competitive pressure on OpenAI/Anthropic
