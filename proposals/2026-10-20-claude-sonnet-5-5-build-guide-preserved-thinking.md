---
type: proposal
source: raw/articles/2026-09-29-claudedev-blogbuilding-with-claude-sonne.md
sources:
  - raw/articles/2026-09-29-claudedev-blogbuilding-with-claude-sonne.md
  - raw/articles/2026-09-29-tco-amq2qindpr.md
  - raw/newsletters/2026-09-29-ainews-amd-buys-world-labs-for-82b-as-atlas-s.md
  - raw/newsletters/2026-09-30-ainews-openai-devday-2026-dots-61-sol-ultraf.md
  - raw/newsletters/2026-09-28-vibe-check-sonnet-55-finds-its-place-in-claudes.md
triage: proposals/triage/2026-09-21-to-2026-09-30-ai-digest.md
status: pending
created: 2026-10-20
---

# Proposal: Claude Sonnet 5.5 — build guide, preserved thinking, hands-on verdict

## Summary

### In short

Moving to Sonnet 5.5 is a code migration, not a model-ID swap, and harnesses that edit the conversation between turns now lose reasoning or get errors. Anthropic's build guide lists breaking changes: turning thinking off returns a 400 error, and forced tool choice is gone. The preserved-thinking rules tie Sonnet 5.5 and Haiku 5.5 reasoning to the account that produced it. The proposal adds both to the Sonnet 5.5 page, with the 28 September launch date, independent evals and Every's verdict, and fixes dates on four pages. Reasons to hesitate: page dates move backwards from an ingest-date fallback, and Every's review was read as a free preview only.

[[#Open questions|Open questions: none.]]

### The source

Anthropic released Claude Sonnet 5.5 on 28 September 2026, six days after Opus 5.5 and the day before OpenAI's DevDay. Alongside it came "Building with Claude Sonnet 5.5," a developer guide with the details the launch post leaves out. Thinking is now always on. A request that sets thinking to "disabled" fails with a 400 error, and callers who want less upfront reasoning use a new `between_tools` mode, which works only up to high effort. Forcing a specific tool also fails. Default effort is high on the API and medium in Claude Code. The minimum cacheable prompt drops to 512 tokens. Images use a high-resolution tier that costs about 2.5 times the tokens Sonnet 4.6 charged.

The next day Anthropic's developer account said it was extending "preserved thinking" to block distillation through account switching. The linked API docs set out two separate rules. First, thinking blocks from Sonnet 5.5 and Haiku 5.5 work only in the account that produced them; another account's request silently drops them, and the model rebuilds its reasoning from scratch. Second, a prefix check covers Fable 5.1 and all three 5.5 models: if the system prompt, tools or earlier messages change after a thinking block was produced, that block is invalid. Accounts created on or after 31 August 2026 get a 400 error by default. A softer "drop" mode keeps requests running but, in Anthropic's tests, adds up to 67% more output tokens at max effort.

Launch-week coverage adds the rest. Sonnet 5.5 now powers the free tier on claude.ai. It placed #4 on Code Arena WebDev, and Vals found it terser than Sonnet 5 on every paired task. Every's Vibe Check (free preview) calls it a strong steered partner for prototyping, design and outlining at low or medium effort. Left unattended or pushed to high effort, it overbuilds, and Every saw no consistent coding gain over Sonnet 5.

### What changes

The Sonnet 5.5 page was written today from Anthropic's undated launch post. It has benchmarks and pricing, but no launch date, no migration detail and no outside evaluation.

- **Claude Sonnet 5.5** gains the launch date and free-tier note. A "Building with it" section lists the breaking changes and new defaults. A "Preserved thinking" section covers both rules, plus independent evals and Every's verdict. The cache-read bullet notes the $0.20 launch price. The placeholder Recent-changes entry becomes a dated launch entry, and one entry is added for the preserved-thinking change. The page date moves from 20 October back to 30 September, the newest claim these sources support. This is the agreed exception for fallback dates.
- **State of Models** and the **index**: the Sonnet 5.5 lines gain the launch date, and their date stamps move to 30 September.
- **Sonnet 5 history page** and the **existing launch source page**: date fixes (`published: 2026-09-28`).
- Five new source pages.

### What to weigh

Moving `as_of` backwards breaks the usual rule. It is justified only because the original date was the ingest date. The page's existing cache-read entry (dated 19 October) also carries a fetch date rather than an announcement date; it is left as it is here. The Every review is a paywalled preview.

## Intended changes

- [ ] **Approve all** — checking this box approves every item in `## Intended changes` and `## Schema / vocabulary additions` below; the individual boxes may stay empty.

- [ ] **Update** `wiki/models/claude-sonnet-5-5.md` — launch date, "Building with it" and "Preserved thinking" sections, independent evals, Every verdict; `as_of` 2026-10-20 → 2026-09-30 (fallback-date correction: newest claim from this proposal's sources; never below a later-dated claim already on the live page); sources merged. Recent changes: replaces the placeholder entry dated 2026-10-20 with a launch entry dated 2026-09-28, adds one entry dated 2026-09-29; the live 2026-10-19 entry is kept (3 entries, no spill).
    > See draft below

- [ ] **Update** `wiki/state-of/models.md` — Sonnet 5.5 leader line only (no Recent-changes entry, so no spill)
    > **Before:** `- [Claude Sonnet 5.5](../models/claude-sonnet-5-5.md) — Anthropic middle tier, supersedes Sonnet 5; Terminal-Bench 4.0 70.6%, GDPval-AA 1844 (near Opus 5.5) at $2/$10 and $0.10 cache reads; Opus 5.5 still stronger on open-ended judgment work *(as of 2026-10-20)*`
    > **After:** `- [Claude Sonnet 5.5](../models/claude-sonnet-5-5.md) — Anthropic middle tier, launched 2026-09-28, supersedes Sonnet 5; Terminal-Bench 4.0 70.6%, GDPval-AA 1844 (near Opus 5.5) at $2/$10 and $0.10 cache reads; powers the claude.ai free tier; Opus 5.5 still stronger on open-ended judgment work *(as of 2026-09-30)*`

- [ ] **Update** `wiki/index.md` — Sonnet 5.5 line
    > **Before:** `- [models/claude-sonnet-5-5](models/claude-sonnet-5-5.md) — Anthropic middle-tier Claude 5.5 model, supersedes Sonnet 5; Terminal-Bench 4.0 70.6%, near-Opus GDPval-AA at $2/$10 with $0.10 cache reads *(as_of: 2026-10-20)*`
    > **After:** `- [models/claude-sonnet-5-5](models/claude-sonnet-5-5.md) — Anthropic middle-tier Claude 5.5 model (launched 2026-09-28), supersedes Sonnet 5; Terminal-Bench 4.0 70.6%, near-Opus GDPval-AA at $2/$10; thinking always on, account-bound thinking blocks *(as_of: 2026-09-30)*`

- [ ] **Update** `wiki/history/models/claude-sonnet-5.md` — supersession line: "October 2026" → "2026-09-28"

- [ ] **Update** `wiki/sources/articles/claude-sonnet-5-5-launch.md` — add `published: 2026-09-28`; correct the "no publication date" sentence

- [ ] **Create** `wiki/sources/articles/building-with-claude-sonnet-5-5-2026-09-28.md`
- [ ] **Create** `wiki/sources/articles/claude-api-preserved-thinking-2026-09-29.md`
- [ ] **Create** `wiki/sources/newsletters/ainews-claude-sonnet-5-5-launch-2026-09-29.md`
- [ ] **Create** `wiki/sources/newsletters/ainews-sonnet-5-5-independent-evals-2026-09-30.md`
- [ ] **Create** `wiki/sources/newsletters/every-vibe-check-sonnet-5-5-2026-09-28.md`

## Page drafts

### wiki/models/claude-sonnet-5-5.md (updated)

Full page; unchanged lines are carried over from the live page.

```
---
title: Claude Sonnet 5.5
type: model
domains: [models, coding]
subcategory: frontier-model
tags: [anthropic]
as_of: 2026-09-30
sources: [claude-sonnet-5-5-launch, claude-haiku-5-5-launch-2026-10-19, building-with-claude-sonnet-5-5-2026-09-28, claude-api-preserved-thinking-2026-09-29, ainews-claude-sonnet-5-5-launch-2026-09-29, ainews-sonnet-5-5-independent-evals-2026-09-30, every-vibe-check-sonnet-5-5-2026-09-28]
---

# Claude Sonnet 5.5

Anthropic's middle-tier Claude 5.5 model, launched 2026-09-28, superseding [Claude Sonnet 5](../history/models/claude-sonnet-5.md). It is the faster, cheaper complement to [Claude Opus 5.5](claude-opus-5-5.md): strongest at well-scoped everyday tasks, bug fixing, and polished documents, slides and spreadsheets, while Opus 5.5 stays clearly stronger on open-ended work that needs sustained judgment. It now powers the claude.ai free tier.

## Current status (as of 2026-09-30)

- Available on the Claude Platform as `claude-sonnet-5-5`, and on AWS (including Bedrock), Google Cloud and Microsoft Azure. 1M-token context; 128k max output (300k on the Batches API with a beta header). In Claude Code the `sonnet` alias resolves to it from v2.1.284, at medium effort; the default model stays Opus 5.5.
- Pricing per 1M tokens: $2 input, $10 output (same as Sonnet 5), $2.50 cache writes, $0.10 cache reads ($0.20 at launch). Anthropic says it costs up to 30% less per task than Sonnet 5 and outputs 30%+ faster, its fastest Sonnet yet.
- Launch benchmarks (Sonnet 5.5 / Sonnet 5 / Opus 5.5): Terminal-Bench 4.0 70.6% / 10.3% / 66.4%; CursorBench 4.0 55.5% / 34.1% / 57.8%; GDPval-AA v2.1 1844 / 1449 / 1846; OSWorld 2.1 80.1% / 57.0% / 81.8%. Anthropic says Sonnet 5.5 at Low or Medium effort beats Sonnet 5's best score on several benchmarks at about a tenth of the cost per task.
- Independent evals: #4 on Code Arena WebDev at 1699 (+159 over Sonnet 5); Vals finds it terser than Sonnet 5 on every paired task; Roboflow found it beat GPT-6 Sol on detection at 30% lower cost and 41% lower latency. In one planted-bug test, Sonnet 5.5 at max effort led with 55.5 but took about 6x GPT-6 Astra's turns.
- First Sonnet to launch with Opus-class cyber safeguards (higher-risk cyber tasks fall back to Sonnet 5) and anti-distillation classifiers; biology safeguards unchanged from Sonnet 5. Declines return `stop_reason: "refusal"` with one of five categories.

## Building with it

- **Thinking is always on.** `thinking: disabled` returns a 400 error. Use `between_tools` to skip upfront thinking; it works only at low, medium and high effort and fixes effort for the conversation. Read response blocks by type, since a response can start with a `thinking` block.
- **Breaking changes from Sonnet 5:** forced `tool_choice` (`any` or `tool`) returns a 400 (use `auto` with strict tools); computer use only through the new `computer_toolset_20260801`; Sonnet 5.5 rejects Opus 4.8, Opus 4.7 and Sonnet 5 as advisors, and advice comes back encrypted. `/claude-api migrate` in Claude Code applies the changes.
- **Defaults and tuning:** default effort is high on the API and medium in Claude Code; levels are recalibrated, so re-run effort sweeps. Minimum cacheable prompt is 512 tokens (Sonnet 5: 1,024). High-resolution images cost about 2.5x the tokens Sonnet 4.6 charged. Changing top-level effort between requests invalidates the cache.

## Preserved thinking

Anthropic extended its anti-distillation "preserved thinking" rules on 2026-09-29. Two separate checks apply:

- **Account binding.** Thinking blocks from Sonnet 5.5 and Haiku 5.5 work only in the account that produced them, or a linked one. Sent from another account, they are silently dropped and the model regenerates its reasoning.
- **Prefix check.** On Fable 5.1, Opus 5.5, Sonnet 5.5 and Haiku 5.5, a thinking block is valid only while the system prompt, tools and earlier messages are unchanged. Accounts created on or after 2026-08-31 get a 400 error by default; older accounts only when they opt in. The softer `drop_block` mode keeps requests running but, in Anthropic's tests, raises output tokens by up to 67% at max effort when blocks drop every turn.

The practical rule for any [harness](../concepts/harness.md): keep system and tools fixed per session and treat messages as append-only.

## Evidence from early users

- Base44: across 118 app builds, Sonnet 5.5 matched Opus 5's scores in 3.6 iterations per build against Opus 5's 7.7. Balyasny: about 121k tokens per finance answer against Sonnet 5's 497k.
- Every's Vibe Check: at low and medium effort it is a fast, cheap, responsive partner for prototyping, design and outlining you steer yourself. At high effort or left unattended it overbuilds, and Every's tests showed no consistent coding gain over Sonnet 5. Advice: start at medium and set a time or token budget.

## Recent changes

- [2026-10-19] Cache reads halved from $0.20 to $0.10 per 1M tokens, announced with Haiku 5.5; Anthropic says this makes Sonnet 5.5 about 20% cheaper on most agentic work.
- [2026-09-29] Preserved thinking extended: Sonnet 5.5 and Haiku 5.5 thinking blocks bound to the producing account; prefix check enforced by default for accounts created from 2026-08-31.
- [2026-09-28] Launched as the second Claude 5.5 model, superseding Sonnet 5; build guide lists breaking changes (thinking always on, no forced tool choice); powers the claude.ai free tier.

## Sources

- [Claude Sonnet 5.5 launch](../sources/articles/claude-sonnet-5-5-launch.md)
- [Claude Haiku 5.5 launch](../sources/articles/claude-haiku-5-5-launch-2026-10-19.md)
- [Building with Claude Sonnet 5.5](../sources/articles/building-with-claude-sonnet-5-5-2026-09-28.md)
- [Claude API docs — Preserved thinking](../sources/articles/claude-api-preserved-thinking-2026-09-29.md)
- [AINews — Claude Sonnet 5.5 launch and reactions](../sources/newsletters/ainews-claude-sonnet-5-5-launch-2026-09-29.md)
- [AINews — Sonnet 5.5 independent evals](../sources/newsletters/ainews-sonnet-5-5-independent-evals-2026-09-30.md)
- [Every — Vibe Check: Sonnet 5.5](../sources/newsletters/every-vibe-check-sonnet-5-5-2026-09-28.md)
```

### wiki/state-of/models.md (updated)

Only the Sonnet 5.5 line under "Frontier models" changes:

```
- [Claude Sonnet 5.5](../models/claude-sonnet-5-5.md) — Anthropic middle tier, launched 2026-09-28, supersedes Sonnet 5; Terminal-Bench 4.0 70.6%, GDPval-AA 1844 (near Opus 5.5) at $2/$10 and $0.10 cache reads; powers the claude.ai free tier; Opus 5.5 still stronger on open-ended judgment work *(as of 2026-09-30)*
```

### wiki/index.md (updated)

```
- [models/claude-sonnet-5-5](models/claude-sonnet-5-5.md) — Anthropic middle-tier Claude 5.5 model (launched 2026-09-28), supersedes Sonnet 5; Terminal-Bench 4.0 70.6%, near-Opus GDPval-AA at $2/$10; thinking always on, account-bound thinking blocks *(as_of: 2026-09-30)*
```

### wiki/history/models/claude-sonnet-5.md (updated)

Only the supersession line changes:

```
**Superseded by [Claude Sonnet 5.5](../../models/claude-sonnet-5-5.md), launched 2026-09-28.**
```

### wiki/sources/articles/claude-sonnet-5-5-launch.md (updated)

Frontmatter gains `published: 2026-09-28` (after `url:`). In the summary paragraph, replace "The post carries no publication date; it says Haiku 5.5 "will join the Claude 5.5 family in the coming weeks," so it predates Haiku 5.5. The ingest date (2026-10-20) is used." with:

```
The post itself carries no date; Anthropic's build guide and launch-week coverage date the release to 2026-09-28, before Haiku 5.5, which the post says "will join the Claude 5.5 family in the coming weeks."
```

### wiki/sources/articles/building-with-claude-sonnet-5-5-2026-09-28.md (new)

```
---
title: Building with Claude Sonnet 5.5
type: source
source_type: article
source_file: raw/articles/2026-09-29-claudedev-blogbuilding-with-claude-sonne.md
url: https://claude.dev/blog/building-with-claude-sonnet-5-5/
published: 2026-09-28
ingested: 2026-10-20
domains: [models, coding]
---

# Building with Claude Sonnet 5.5

Anthropic's launch-day developer guide for Sonnet 5.5: when to choose it over Opus 5.5, pricing, model details, a migration path from Sonnet 5 with five breaking changes and one response-shape change, tuning advice, refusal handling and availability.

## Influenced pages
- [Claude Sonnet 5.5](../../models/claude-sonnet-5-5.md) — launch date, "Building with it" section, model details

## Key claims extracted
- Thinking on by default; `thinking: disabled` returns 400; `between_tools` replaces it, only at low/medium/high effort
- Forced `tool_choice` (`any`/`tool`) returns 400; computer use only via `computer_toolset_20260801` (Bedrock still accepts the old tool)
- Sonnet 5.5 executors reject Opus 4.8, Opus 4.7 and Sonnet 5 as advisors; advice comes back encrypted
- Default effort high on the API, medium in Claude Code; effort levels recalibrated
- 1M context; 128k max output, 300k on Batches with a beta header; knowledge cutoff June 2026
- Minimum cacheable prompt 512 tokens; cache reads $0.20 at launch; high-res images ~2.5x the tokens of Sonnet 4.6
- `/claude-api migrate` applies the changes; Claude Code's `sonnet` alias moves to Sonnet 5.5 from v2.1.284
```

### wiki/sources/articles/claude-api-preserved-thinking-2026-09-29.md (new)

```
---
title: 'Claude API docs — Preserved thinking (ClaudeDevs account-switching post)'
type: source
source_type: article
source_file: raw/articles/2026-09-29-tco-amq2qindpr.md
url: https://platform.claude.com/docs/en/build-with-claude/preserved-thinking
published: 2026-09-29
ingested: 2026-10-20
domains: [models, agents]
---

# Claude API docs — Preserved thinking

A ClaudeDevs post (2026-09-29) saying preserved thinking now extends to Sonnet 5.5 to curb distillation through account switching, plus the API docs page it links to. The docs were fetched on 2026-10-20 and already cover Haiku 5.5.

## Influenced pages
- [Claude Sonnet 5.5](../../models/claude-sonnet-5-5.md) — "Preserved thinking" section

## Key claims extracted
- Sonnet 5.5 and Haiku 5.5 thinking blocks work only in the producing account or a linked one; from another account they are dropped silently and the model regenerates its reasoning
- Prefix check on Fable 5.1, Opus 5.5, Sonnet 5.5 and Haiku 5.5: changing the system prompt, tools or earlier messages invalidates later thinking blocks
- Enforced by default (400 error) for accounts created on or after 2026-08-31; older accounts only when they set `prefix_mismatch_behavior`
- `drop_block` mode keeps requests running; dropping blocks every turn raised output tokens 4.6% at low effort and 67.1% at max in Anthropic's tests
- Claude Code, claude.ai, Managed Agents and the Agent SDK are unaffected; append-only integrations are safe
```

### wiki/sources/newsletters/ainews-claude-sonnet-5-5-launch-2026-09-29.md (new)

```
---
title: AINews — Claude Sonnet 5.5 launch and reactions
type: source
source_type: newsletter
source_file: raw/newsletters/2026-09-29-ainews-amd-buys-world-labs-for-82b-as-atlas-s.md
published: 2026-09-29
ingested: 2026-10-20
domains: [models]
---

# AINews — Claude Sonnet 5.5 launch and reactions

The top story of the 2026-09-29 issue (headlined on AMD buying World Labs): the Sonnet 5.5 launch one week after Opus 5.5 and the day before OpenAI DevDay. This page covers the Sonnet 5.5 story only.

## Influenced pages
- [Claude Sonnet 5.5](../../models/claude-sonnet-5-5.md) — free tier, preserved-thinking change, availability

## Key claims extracted
- Sonnet 5.5 now powers the claude.ai free tier (ChatGPT's free tier is still GPT-5.6 Luna)
- Preserved thinking extended against distillation via account switching
- Day-one availability in GitHub Copilot, Cursor, Factory, Devin, Cline and Arena; usage reset valid until Oct 22
```

### wiki/sources/newsletters/ainews-sonnet-5-5-independent-evals-2026-09-30.md (new)

```
---
title: AINews — Sonnet 5.5 independent evals (DevDay issue)
type: source
source_type: newsletter
source_file: raw/newsletters/2026-09-30-ainews-openai-devday-2026-dots-61-sol-ultraf.md
published: 2026-09-30
ingested: 2026-10-20
domains: [models]
---

# AINews — Sonnet 5.5 independent evals (DevDay issue)

The 2026-09-30 issue (headlined on OpenAI DevDay) includes a short block of independent Sonnet 5.5 results. This page covers the Sonnet 5.5 items only.

## Influenced pages
- [Claude Sonnet 5.5](../../models/claude-sonnet-5-5.md) — independent evals

## Key claims extracted
- Code Arena WebDev #4 at 1699 with a blended $8/M, +159 over Sonnet 5
- Vals finds it terser, with fewer visible tokens than Sonnet 5 in 100% of paired tasks
- Roboflow: beats GPT-6 Sol on detection at 30% lower cost and 41% lower latency
- Planted-bug test: Sonnet 5.5 at max led with 55.5 but took ~6x GPT-6 Astra's turns
```

### wiki/sources/newsletters/every-vibe-check-sonnet-5-5-2026-09-28.md (new)

```
---
title: 'Every — Vibe Check: Sonnet 5.5 Finds Its Place in Claude''s Crowded Family'
type: source
source_type: newsletter
source_file: raw/newsletters/2026-09-28-vibe-check-sonnet-55-finds-its-place-in-claudes.md
published: 2026-09-28
ingested: 2026-10-20
domains: [models, coding]
---

# Every — Vibe Check: Sonnet 5.5 Finds Its Place in Claude's Crowded Family

Free preview of Katie Parrott's paywalled Sonnet 5.5 review; the full review was not read. After a week of testing, Every found Sonnet 5.5's job: a fast, cheap, steerable partner at low and medium effort.

## Influenced pages
- [Claude Sonnet 5.5](../../models/claude-sonnet-5-5.md) — hands-on verdict

## Key claims extracted
- At low and medium effort: strong for brainstorming, prototyping and design work you steer; at high effort or unattended it overbuilds
- Built a from-scratch clone of Every's Proof editor at low effort, a job only Fable 5, GPT-6 Astra and Opus 5.5 had managed
- Readability scores ahead of Opus 5.5, but it struggled to connect a full draft
- No consistent coding gain over Sonnet 5 in Every's tests; keep Opus 5.5 for high-detail final builds
```

## Schema / vocabulary additions

None.

## Open questions

None.
