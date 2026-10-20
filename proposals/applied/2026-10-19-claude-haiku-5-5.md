---
type: proposal
source: raw/articles/2026-10-19-anthropiccom-claude-haiku-5-5.md
status: pending
created: 2026-10-19
---

# Proposal: Claude Haiku 5.5

## Summary

### In short

Anthropic's small tier is now a credible subagent and high-volume workhorse, not just a cheap fallback: Haiku 5.5 costs about 75% less to run than Haiku 4.5 on average while scoring 72.4% on OSWorld 2.1 and 1620 on GDPval-AA, within reach of Sonnet 5.5 on several benchmarks. The proposal adds a model page, a new "Small / fast models" section on State of Models, and one routing bullet on the cost-aware routing training page. Reasons to hesitate: it needs a new subcategory, and the page carries no publication date.
[[#Open questions|Open questions: 2 to answer.]]

### The source

Anthropic's launch page introduces Claude Haiku 5.5, which it calls the cheapest, fastest and most capable small model it has released. Anthropic pitches it at high-volume, cost-sensitive work: summaries, context compaction (shrinking a long agent conversation so it fits the context window), database queries, classification, live customer support and browser use. It also pitches Haiku as a subagent working under Opus 5.5 or Sonnet 5.5 on coding tasks. It is the first Haiku with an adjustable effort setting, so users can trade cost against intelligence the way they already do with the larger Claude models.

The benchmark table puts Haiku 5.5 far ahead of Haiku 4.5 and ahead of OpenAI's GPT-6 Luna on every row where Luna is reported. Sonnet 5.5 still leads on all of them, with the widest gap on Terminal-Bench 4.0 (39.2% against 70.6%). Anthropic says so plainly: Sonnet and Opus remain the better choices for complex agentic coding, and Haiku suits narrowly scoped tasks that used to cost too much to run on Claude. Pricing has two tiers split at 100,000-token prompts. Below that line, Haiku costs $0.10 input and $0.50 output per million tokens, against $1 and $5 for Haiku 4.5, and Anthropic says prompts of that size made up about 90% of the old Haiku's requests. Six launch customers report results. Cognition says Devin Fusion keeps a FrontierCode score of 66.2 with Haiku as the "sidekick" under Opus 5.5 while cutting cost and latency, and Rogo describes Haiku pulling single figures out of 10-K filings while a bigger model builds the deck.

The same page halves Sonnet 5.5's cache-read price, adds monthly API credits for Max and Team subscribers, and puts computer-use and browser-use support into the Python and TypeScript SDKs in beta.

### What changes

The wiki has no Haiku page, current or archived. Its State of Models page has no section for small general-purpose models, and the cost-aware routing page talks about "small models" without naming a current Anthropic option.

- New page `models/claude-haiku-5-5.md` with the launch benchmarks and both pricing tiers exactly as stated, the effort setting, availability, the safeguards positioning and two customer data points.
- **State of Models** gains a "Small / fast models" section with Haiku 5.5 as its only entry, plus one Recent-changes entry. The list is at its cap of 10, so the July 31 Inkling-Small entry moves to the history page. Page date moves to 19 October.
- **Cost-aware AI task routing** gains one evidence bullet: Anthropic's own split between Haiku for scoped work and Sonnet or Opus for complex agentic coding, plus the Cognition sidekick result. Page date moves to 19 October.
- One new source page, which also records the Sonnet 5.5 price cut, the API credits and the SDK beta.

### What to weigh

The source page carries no date, so 19 October (the fetch date) is used everywhere. The new subcategory `small-model` is needed because `utility-model` means narrow single-task models and `frontier-model` means top-capability models, and Haiku is neither. The routing page goes from about 2,390 to about 2,470 body words, just under its 2,500-word ceiling, so the next addition there will need a split. The source names Sonnet 5.5, Opus 5.5 and GPT-6 Luna, which the wiki has no pages for. They appear here as plain text without links.

## Intended changes

- [x] **Approve all** — checking this box approves every item in `## Intended changes` and `## Schema / vocabulary additions` below; the individual boxes may stay empty.

- [ ] **Create** `wiki/models/claude-haiku-5-5.md` — new model page, subcategory `small-model`

- [ ] **Update** `wiki/state-of/models.md` — add a `### Small / fast models` section (after `### Specialized utility models`) with the Haiku 5.5 line; adds one Recent-changes entry dated 2026-10-19; append source id to `sources:`; `as_of` 2026-09-08 → 2026-10-19
    > **After (new line):** `- [Claude Haiku 5.5](../models/claude-haiku-5-5.md) — Anthropic; cheapest/fastest Claude tier, ~75% cheaper than Haiku 4.5; OSWorld 2.1 72.4%, GDPval-AA 1620; first Haiku with effort control; aimed at subagent, compaction, and high-volume work *(as of 2026-10-19)*`

- [ ] **Spill** `wiki/state-of/models.md` → `wiki/history/state-of/models.md` — Recent changes is at the cap of 10; spills the oldest entry (`[2026-07-31] Thinking Machines shipped Inkling-Small…`) under a new `## Archived from current page on <apply date>` header

- [ ] **Update** `wiki/training/cost-aware-ai-task-routing.md` — adds one bullet at the end of `### Model and harness selection wins`; adds one Recent-changes entry dated 2026-10-19; appends source id to `sources:` and one link to `## Sources`; adds one `## Related` line; `as_of` 2026-09-07 → 2026-10-19

- [ ] **Create** `wiki/sources/articles/claude-haiku-5-5-launch-2026-10-19.md` — source summary

## Page drafts

### wiki/models/claude-haiku-5-5.md (new)

```md
---
title: Claude Haiku 5.5
type: model
domains: [models]
subcategory: small-model
tags: [anthropic]
as_of: 2026-10-19
sources: [claude-haiku-5-5-launch-2026-10-19]
---

# Claude Haiku 5.5

Anthropic's smallest, fastest and cheapest current Claude model, built for high-volume, cost-sensitive work: summaries, context compaction, database queries, classification, live customer support, browser use, and subagent roles under Opus 5.5 or Sonnet 5.5.

## Current status (as of 2026-10-19)

- Available on the Claude Platform as `claude-haiku-5-5`, and on AWS, Google Cloud and Microsoft Azure.
- First Haiku-class model with an adjustable effort setting (Low through Max).
- Pricing per 1M tokens, prompts up to / over 100k tokens: input $0.10 / $0.50, output $0.50 / $2.50, cache writes $0.125 / $0.625, cache reads $0.01 / $0.05 (Haiku 4.5: $1.00 / $5.00 / $1.25 / $0.10). Anthropic says it costs around 75% less than Haiku 4.5 on average, and that prompts up to 100k made up about 90% of Haiku 4.5 requests.
- Launch benchmarks (Haiku 5.5 / Haiku 4.5 / GPT-6 Luna / Sonnet 5.5): GDPval-AA v2.1 1620 / 735 / 1437 / 1840; AA-Briefcase v1.1 1578 / 614 / 1336 / 1824; OSWorld 2.1 offline subset 72.4% / 15.7% / 48.9% / 83.9%; Humanity's Last Exam 45.9% no tools, 57.4% with tools (Sonnet 5.5: 56.9% / 64.5%); Terminal-Bench 4.0 39.2% / 0.0% / 16.4% / 70.6%; FrontierCode 1.1 (Main) 46.4% / — / 42.4% / 52.1% (xhigh); Chartography 46.4% / 6.4% / 29.1% / 61.6% (no tools).
- Anthropic says Sonnet 5.5 and Opus 5.5 remain the better choice for complex agentic coding. Haiku 5.5 targets narrowly scoped tasks that were previously too expensive to run on Claude.

## Evidence from early users

- Cognition: with Haiku 5.5 as the "sidekick" under an Opus 5.5 lead, Devin Fusion holds a FrontierCode score of 66.2 while cutting cost and latency.
- AlphaSense: on 400 document-QA queries (a workload of about 8M calls a week), Haiku 5.5 scored 0.84 against Haiku 4.5's 0.76.

## Safety

- Anthropic reports far fewer misaligned behaviors than Haiku 4.5 and a lower willingness to cooperate with misuse.
- Its cyber safeguards are stricter than Haiku 4.5's but looser than recent larger models'. They allow more defensive tasks than Sonnet 5.5's safeguards and still block penetration testing. Its biology safeguards match those of Sonnet 5, Sonnet 5.5 and Opus 5.

## Related

- [Advisor strategy](../workflows/advisor-strategy.md) — the cheap-executor / expensive-advisor pattern Haiku is pitched for.
- [Cost-aware AI task routing](../training/cost-aware-ai-task-routing.md) — where Haiku fits in a routing ladder.

## Recent changes

- [2026-10-19] Launched: about 75% cheaper than Haiku 4.5, first Haiku with effort control, large benchmark gains over Haiku 4.5.

## Sources

- [Claude Haiku 5.5 launch](../sources/articles/claude-haiku-5-5-launch-2026-10-19.md)
```

### wiki/state-of/models.md (updated)

Frontmatter changes:

```yaml
as_of: 2026-10-19
sources: [<existing list unchanged>, claude-haiku-5-5-launch-2026-10-19]
```

New section, inserted directly after `### Specialized utility models` and its entry:

```md
### Small / fast models

General-purpose models built for low cost and low latency on high-volume work, subagent roles, and compaction, rather than top-end capability.

- [Claude Haiku 5.5](../models/claude-haiku-5-5.md) — Anthropic; cheapest/fastest Claude tier, ~75% cheaper than Haiku 4.5; OSWorld 2.1 72.4%, GDPval-AA 1620; first Haiku with effort control; aimed at subagent, compaction, and high-volume work *(as of 2026-10-19)*
```

`## Recent changes`: add one entry at the top. The oldest entry (dated 2026-07-31) is removed, which leaves 10.

```md
- [2026-10-19] Claude Haiku 5.5 launched; new Small / fast models section. About 75% cheaper than Haiku 4.5, OSWorld 2.1 72.4% and Terminal-Bench 4.0 39.2% (Sonnet 5.5: 83.9% / 70.6%), first Haiku with an effort setting.
- [2026-09-03] GPT-6 Astra launched (OpenAI): new flagship, but not a clean win — Fable 5.1 leads AA's coding-agent and intelligence indices, Astra leads token efficiency and cost-per-task; full rollout completed 2026-09-08; system card discloses a sharp CoT-monitorability decline.
- [2026-09-03] Muse Spark 1.3 launched: AA Intelligence Index #3 in the world, parity with GPT-5.6 Sol/Opus 5 on several evals, open weights still pending.
- [2026-09-01] Claude Fable 5.1 / Mythos 5.1 launched, superseding Fable 5: AA Intelligence Index 66 (was 62), 75% cache-read price cut, same-weights/different-safety-routing debate between the two paired model names.
- [2026-08-20] GLM-5.3 launched, superseding GLM-5.2: same 753B/40B MoE footprint and price, +246 GDPval-AA v2, ties Kimi K3 on AA Intelligence Index — gains attributed to post-training RL rather than scale.
- [2026-08-13] Grok 4.6 launched, superseding Grok 4.5: AA Intelligence Index 61, 88.4% Terminal-Bench v2.1, unchanged $2/$6 pricing; powers new Grok Bot AI-teammate product.
- [2026-08-13] Qwen3.8-Max shipped open weights (2.4T/~95B active MoE), text-only initial drop; day-0 vLLM/Together/Baseten support.
- [2026-08-13] DeepSeek V4 Pro reached general availability at $0.435/$0.87 pricing, +15.8% Terminal-Bench over preview; capability reception mixed versus Kimi/Flash.
- [2026-08-12] Nemotron 3.5 Lightning (NVIDIA, 31.6B/3.6B active) added to Open-weight models: AA Intelligence Index 24, strong per-size agentic benchmarks, Harvey's Legal Agent Bench post-training result beating Opus 4.6 and Nemotron 3 Ultra.
- [2026-08-04] Qwen3.8-Max (Alibaba, 2.4T/~95B active) added to Open-weight models: #4 Frontend Code Arena, SWE-bench 87.3%, Terminal-Bench 2.1 67.4; open weights promised for Max + a 27B sibling; license reportedly restricts use in US/EU/UK/Korea.
```

### wiki/history/state-of/models.md (updated)

Append at the end of the file:

```md

## Archived from current page on 2026-10-19

- [2026-07-31] Thinking Machines shipped Inkling-Small (276B/12B MoE, Intelligence Index 40), a near-flagship-capability sibling to Inkling at roughly a quarter the active footprint.
```

### wiki/training/cost-aware-ai-task-routing.md (updated)

Frontmatter changes:

```yaml
as_of: 2026-10-19
sources: [<existing list unchanged>, claude-haiku-5-5-launch-2026-10-19]
```

Append as the last bullet of `### Model and harness selection wins`:

```md
- **Anthropic's own tier split for Haiku 5.5.** Anthropic positions Haiku 5.5 for scoped, high-volume work such as compaction, summarization and subagents, and keeps Sonnet 5.5 and Opus 5.5 for complex agentic coding (Terminal-Bench 4.0: 39.2% against Sonnet 5.5's 70.6%). Haiku is cheapest on prompts under 100k tokens ($0.10/$0.50 per 1M), which made up about 90% of Haiku 4.5's requests. Cognition reports Devin Fusion holds FrontierCode 66.2 with Haiku 5.5 as the sidekick under an Opus 5.5 lead, at lower cost and latency. See [Claude Haiku 5.5](../models/claude-haiku-5-5.md).
```

`## Recent changes`: add one entry at the top. The list then has 3 entries, under the cap.

```md
- [2026-10-19] Added Anthropic's Haiku 5.5 / Sonnet 5.5 / Opus 5.5 tier split and Cognition's Haiku-sidekick result to Model and harness selection wins.
```

`## Related`: add one line.

```md
- [Claude Haiku 5.5](../models/claude-haiku-5-5.md) - Anthropic's current cheap/fast tier, pitched for subagent, compaction and high-volume routing slots.
```

`## Sources`: append one line.

```md
- [Anthropic — Claude Haiku 5.5 launch](../sources/articles/claude-haiku-5-5-launch-2026-10-19.md)
```

### wiki/sources/articles/claude-haiku-5-5-launch-2026-10-19.md (new)

```md
---
title: Claude Haiku 5.5 launch
type: source
source_type: article
source_file: raw/articles/2026-10-19-anthropiccom-claude-haiku-5-5.md
url: https://www.anthropic.com/claude-haiku-5-5
ingested: 2026-10-19
domains: [models]
---

# Claude Haiku 5.5 launch

Anthropic's launch page for Claude Haiku 5.5 presents it as its cheapest, fastest and most capable small model, built for high-volume, cost-sensitive tasks and subagent roles under Opus 5.5 and Sonnet 5.5. It includes a benchmark table against Haiku 4.5, GPT-6 Luna and Sonnet 5.5, two-tier pricing split at 100k-token prompts, quotes from six launch customers, and safety notes. The same page announces a Sonnet 5.5 cache-read price cut, monthly API credits for Max and Team subscribers, and computer-use and browser-use support in the Claude SDKs. The page carries no publication date; the fetch date (2026-10-19) is used.

## Influenced pages
- [Claude Haiku 5.5](../../models/claude-haiku-5-5.md) — new page: benchmarks, pricing, effort control, availability, safety
- [State of Models](../../state-of/models.md) — new Small / fast models section
- [Cost-aware AI task routing](../../training/cost-aware-ai-task-routing.md) — Anthropic tier split and Cognition sidekick result

## Key claims extracted
- Haiku 5.5 is available on all platforms (AWS, Google Cloud, Microsoft Azure) and on the Claude Platform as `claude-haiku-5-5`.
- It costs around 75% less to run than Haiku 4.5 on average. Per 1M tokens, for prompts up to / over 100k: input $0.10 / $0.50, output $0.50 / $2.50, cache writes $0.125 / $0.625, cache reads $0.01 / $0.05. Prompts up to 100k made up around 90% of requests to Haiku 4.5.
- Benchmarks (Haiku 5.5 / Haiku 4.5 / GPT-6 Luna / Sonnet 5.5): GDPval-AA v2.1 1620 / 735 / 1437 / 1840; AA-Briefcase v1.1 1578 / 614 / 1336 / 1824; OSWorld 2.1 offline subset 72.4% / 15.7% / 48.9% / 83.9%; HLE no tools 45.9% / 10.2% / — / 56.9%, with tools 57.4% / 18.7% / — / 64.5%; Terminal-Bench 4.0 39.2% / 0.0% / 16.4% / 70.6%; FrontierCode 1.1 (Main) 46.4% / — / 42.4% / 52.1% (xhigh); Chartography 46.4% / 6.4% / 29.1% / 61.6%.
- It is the first Haiku-class model with an adjustable effort setting.
- Anthropic says Sonnet 5.5 and Opus 5.5 remain the better choices for complex agentic coding. Haiku suits narrowly scoped tasks such as compaction, summarization and subagent work.
- Customer reports: Asana saw over 30% lower task latency and up to 2.5x faster inference per agent turn; HubSpot got 92.8% on its CRM suite, the best score it has seen; AlphaSense got 0.84 against 0.76 for Haiku 4.5 on 400 document-QA queries; Box saw +11 points over Haiku 4.5 at about half the latency; Cognition's Devin Fusion holds FrontierCode 66.2 with Haiku 5.5 as sidekick under Opus 5.5.
- Safety: Anthropic reports large alignment gains over Haiku 4.5. Cyber safeguards are stricter than Haiku 4.5's but looser than recent larger models', and penetration testing is still blocked. Biology safeguards match Sonnet 5, Sonnet 5.5 and Opus 5.
- Sonnet 5.5 cache reads cut 50%, from $0.20 to $0.10 per 1M tokens, which Anthropic says makes Sonnet 5.5 around 20% cheaper on most agentic tasks.
- New monthly API credits on the Claude Platform: $100 for Max 5x, $200 for Max 20x, and up to $500 pooled for Team.
- The Claude Python and TypeScript SDKs add computer-use and browser-use support in beta.
```

## Schema / vocabulary additions

- [ ] Add new subcategory `small-model` to `wiki/_schema/subcategories.md`. Append `small-model` to the `Declared slugs` line and add this block after `### utility-model`:

```md
### small-model
- **Parent domain(s):** models
- **Applies to types:** model
- **Definition:** Small, fast, low-cost general-purpose models positioned for high-volume work, subagent roles, and context compaction rather than top-end capability; distinct from `utility-model` (narrow single-task models) and `frontier-model`.
- **Examples:** [Claude Haiku 5.5](../models/claude-haiku-5-5.md)
```

## Open questions

- If you decline the `small-model` subcategory, the fallback is `frontier-model`, with Haiku listed under Frontier models next to Gemini 3.5 Flash. Should Gemini 3.5 Flash later move to the new Small / fast models section? This proposal leaves it where it is.
	- Small model is fine. Flash is also a small model.
- The source implies Sonnet 5 and Opus 5 have been superseded by Sonnet 5.5 and Opus 5.5, and it halves Sonnet 5.5's cache-read price. The wiki has neither 5.5 page. This proposal records those facts only on the source page. Should they go on the existing Sonnet 5 / Opus 5 pages now, or wait for a dedicated Sonnet 5.5 / Opus 5.5 source?
	- We create new pages and archive the old versions, right? thats the pattern here
