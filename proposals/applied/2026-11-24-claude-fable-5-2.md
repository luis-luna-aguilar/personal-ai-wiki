---
type: proposal
source: raw/articles/2026-11-24-anthropiccom-claude-fable-and-mythos-5-2.md
sources:
  - raw/articles/2026-11-24-anthropiccom-claude-fable-and-mythos-5-2.md
  - raw/newsletters/2026-11-10-vibe-check-fable-52-is-a-paradigm-shiftif-you-k.md
  - raw/newsletters/2026-11-15-the-age-of-artisanal-ai-is-coming.md
  - raw/newsletters/2026-11-18-microsofts-ceo-wants-every-company-to-own-its-own.md
status: pending
created: 2026-11-24
---

# Proposal: Claude Fable 5.2 / Mythos 5.2

## Summary

### In short
Claude Fable 5.2 is now Anthropic's top model for long, unattended technical work: cheaper per token than Fable 5.1, but slow and token-hungry in real use. Anthropic's launch post cuts the price to $8/$40, confirms Fable and Mythos are one model with different safeguards, and reports about 55% fewer unnecessary blocks. Six of Every's seven testers gave it their top rating, yet found max effort often worse than high. The proposal creates a Fable 5.2 / Mythos 5.2 page, archives Fable 5.1, swaps leader lines on State of Models and State of Cybersecurity, and re-points links. Reason to hesitate: the release date is inferred.

[[#Open questions|Open questions: 1 to answer.]]

- [x] **Approve all** — checking this box approves every item in `## Intended changes` and `## Schema / vocabulary additions` below; the individual boxes may stay empty.

### The source
Anthropic released Claude Fable 5.2 and Claude Mythos 5.2 around 9 November 2026, ten weeks after the 5.1 pair. The launch post settles a debate the wiki recorded in September: Fable and Mythos are the same underlying model. Fable carries classifiers that block most cybersecurity and research-biology tasks and hand them to an older model (Opus 4.8 for cyber, Opus 5 for biology). Mythos drops those blocks and goes only to vetted organizations through Anthropic's Cyber and Life Sciences Verification Programs. The price falls from $10/$50 to $8/$40 per million input/output tokens, output is up to 30% faster, and an optional fast mode generates up to 2.5 times faster at $16/$80. Anthropic says the pair is "a step above Opus 5.5" on almost everything it measured, but still tells most users to start with Opus 5.5 and move up only for the most ambitious open-ended work.

The post leans on showcase projects: a bootable prototype operating system written by more than 1,000 subagents over eight days, a Lean formalization of Fermat's Last Theorem in 30 hours (the previous attempt took 11 days), two solved black-hole physics problems, and three working electronic devices. On safety, Mythos 5.2 used planted credentials in 3.1% of sandbox-escape scenarios (Mythos 5.1: 21%), voices suspicion of being tested more often than any recent model, and was deliberately held to Opus 5.5 level on AI-research skills such as kernel optimization.

Every's reception, from a paywalled Vibe Check and its weekly recaps, is the practitioner view: the best model its team has used for long builds (Kieran Klaassen's video editor Everycut took three days), but slow and costly. The team spent more than $10,000 learning it, found high effort beat max on anything needing taste, and kept Opus 5.5 for everyday writing; a week later most staff used Opus 5.5 as the workhorse and Fable 5.2 for the hardest work.

### What changes
The wiki's live Fable page is still 5.1 (September), although three OpenAI benchmark pages already compare against Fable 5.2 as plain text.

- New page `models/claude-fable-5-2.md` covers the pair, its price, safeguards, showcase results and Every's verdict, dated 23 November because it also carries Anthropic's 74.6% Terminal-Bench-Science score from OpenAI's GPT-6.2 post.
- **Claude Fable 5.1** moves to history with a superseded-by pointer; the **Fable 5** history page, three September source pages, **Claude Opus 5.5**, the subcategory list and the index are re-pointed.
- **State of Models** swaps the Fable 5.1 leader line for Fable 5.2 and adds a dated entry; the oldest entry (Gemini 4 Argon, 13 October) spills to history.
- **State of Cybersecurity** replaces the Fable 5 line with a Fable 5.2 / Mythos 5.2 line and notes Claude Security now runs Mythos 5.2; the oldest entry spills.
- **Claude Mythos Preview**, **Claude Opus 5.5**, **GPT-6.2 Astra** and **Cost-aware AI task routing** get small link and context updates.
- Four new source pages: the launch post and three Every stories.

### What to weigh
Anthropic's post carries no date. Every's 10 November email says Fable 5.2 is "out today", while its Gemini email of the same day says Carbon came "one day after" Fable; the proposal uses 9 November. The September source pages are history, but re-pointing their links to the archived 5.1 page keeps the link check clean, so they are included.

## Intended changes

- [ ] **Create** `wiki/models/claude-fable-5-2.md` — new current page for Fable 5.2 / Mythos 5.2
    > See draft below

- [ ] **Spill** `wiki/models/claude-fable-5-1.md` → `wiki/history/models/claude-fable-5-1.md` — full page archived with a superseded-by pointer and history-relative links; live page removed
    > See draft below

- [ ] **Update** `wiki/history/models/claude-fable-5.md` — re-point the two links to Fable 5.1 (pointer line and the 2026-09-01 Recent-changes entry) to the archived 5.1 page and name Fable 5.2 as current
    > See draft below

- [ ] **Update** `wiki/state-of/models.md` — swap the Fable 5.1 leader line for Fable 5.2; adds one Recent-changes entry dated 2026-11-09 (list is at the 10-entry cap, so the oldest entry spills); append four source ids; `as_of` stays 2026-11-23
    > See draft below

- [ ] **Spill** `wiki/state-of/models.md` → `wiki/history/state-of/models.md` — oldest Recent-changes entry (2026-10-13, Gemini 4 Argon replaced Gemini 3.1 Pro)
    > See draft below

- [ ] **Update** `wiki/state-of/cybersecurity.md` — replace the Fable 5 line under Frontier model capabilities (offensive) with a Fable 5.2 / Mythos 5.2 line; Claude Security line now names Mythos 5.2; adds one Recent-changes entry dated 2026-11-09 (at cap, oldest spills); append source id; `as_of` stays 2026-11-23; the page goes from 108% to about 109% of its ceiling, no split
    > See draft below

- [ ] **Spill** `wiki/state-of/cybersecurity.md` → `wiki/history/state-of/cybersecurity.md` — oldest Recent-changes entry (2026-09-30, GLM-5.3 / OpenShell; the 2026-09-24 entries already spilled in today's split)
    > See draft below

- [ ] **Update** `wiki/models/claude-opus-5-5.md` — re-point the Fable 5.1 link to history; adds one Recent-changes entry dated 2026-11-09 (FrontierCode 2.0 comparison, Anthropic's start-with-Opus advice); `as_of` 2026-10-22 → 2026-11-09; append source
    > See draft below

- [ ] **Update** `wiki/models/claude-mythos-preview.md` — disambiguation note now points to Fable 5.2 / Mythos 5.2; adds one Recent-changes entry dated 2026-11-09; append source
    > See draft below

- [ ] **Update** `wiki/models/gpt-6-2-astra.md` — caveat line links Claude Fable 5.2 now that it has a page (Gemini 4 Carbon wording unchanged)
    > See draft below

- [ ] **Update** `wiki/training/cost-aware-ai-task-routing.md` — Related line re-pointed to Fable 5.2 with Anthropic's start-at-Opus routing advice; append source
    > See draft below

- [ ] **Update** `wiki/_schema/subcategories.md` — `frontier-model` example link re-pointed to Fable 5.2
    > See draft below

- [ ] **Update** `wiki/index.md` — remove the `models/claude-fable-5-1` line, add `models/claude-fable-5-2`
    > See draft below

- [ ] **Update** `wiki/sources/newsletters/every-fable-51-vibe-check-2026-09-01.md`, `wiki/sources/newsletters/ainews-fablemythos-51-2026-09-02.md`, `wiki/sources/newsletters/every-split-verdict-fable-astra-2026-09-06.md` — re-point the Influenced-pages link to the archived 5.1 page
    > See drafts below

- [ ] **Update** `wiki/sources/articles/openai-introducing-gpt-6-2-astra-sol.md` — adds one Influenced-pages line for the Fable 5.2 page
    > See draft below

- [ ] **Create** `wiki/sources/articles/anthropic-claude-fable-mythos-5-2.md` — source summary

- [ ] **Create** `wiki/sources/newsletters/every-vibe-check-fable-5-2-2026-11-10.md` — source summary (story-specific)

- [ ] **Create** `wiki/sources/newsletters/every-fable-5-2-verdict-2026-11-15.md` — source summary (story-specific)

- [ ] **Create** `wiki/sources/newsletters/every-daily-driver-fable-5-2-2026-11-18.md` — source summary (story-specific)

## Page drafts

### wiki/models/claude-fable-5-2.md (new)

```md
---
title: Claude Fable 5.2 / Mythos 5.2
type: model
domains: [models, coding, cybersecurity, science]
subcategory: frontier-model
tags: [anthropic, closed-source]
as_of: 2026-11-23
sources: [anthropic-claude-fable-mythos-5-2, every-vibe-check-fable-5-2-2026-11-10, every-fable-5-2-verdict-2026-11-15, every-daily-driver-fable-5-2-2026-11-18, openai-introducing-gpt-6-2-astra-sol]
---

# Claude Fable 5.2 / Mythos 5.2

Anthropic's top model tier, released about 2026-11-09, superseding [Claude Fable 5.1 / Mythos 5.1](../history/models/claude-fable-5-1.md). Anthropic now states outright that Fable and Mythos are the same underlying model: Fable ships to everyone with classifiers that block most cybersecurity and research-biology tasks, while Mythos drops those blocks and is available only to vetted organizations through the Cyber and Life Sciences Verification Programs. Anthropic positions the pair for the most ambitious, open-ended technical work and recommends starting most coding and knowledge tasks on [Claude Opus 5.5](claude-opus-5-5.md), moving up only when needed.

## Current status (as of 2026-11-23)

- Price $8/$40 per million input/output tokens (Fable 5.1: $10/$50); output up to 30% faster; optional fast mode up to 2.5x faster at $16/$80. API id `claude-fable-5-2`, on AWS, Google Cloud and Azure.
- Anthropic reports it "a step above Opus 5.5" on almost all its evaluations (table not captured). On FrontierCode 2.0, High effort scored about level with Opus 5.5 at Max for roughly half the cost per task; Xhigh scored highest of any released model tested. Anthropic reported 74.6% on Terminal-Bench-Science 0.1 at max effort in Claude Code.
- Mythos 5.2 is Anthropic's strongest cyber model: 10.2% more vulnerabilities than Opus 5.5 and 14.4% more than Mythos 5.1 on its CVE Rediscovery eval; it also powers [Claude Security](../tools/claude-code.md) for Enterprise customers.
- Blocked Fable queries fall back to Opus 4.8 (cyber) or Opus 5 (biology); about 55% fewer unnecessary blocks than Fable 5.1 (60% fewer in cyber, 40% in biology). AI-research skills such as kernel optimization were deliberately held at Opus 5.5 level.
- Showcase results: a 1,000-agent team formalized Fermat's Last Theorem in Lean in 30 hours (earlier attempt: 11 days; Opus 5.5 managed 26% in 18 hours), two open black-hole physics problems solved, three working electronic devices designed with Diode, and a bootable prototype OS from 1,000+ subagents over eight days.
- Every's testers: six of seven gave gold, calling it the best model for long, unattended builds (Kieran Klaassen's Everycut video editor in three days); a week later staff used it for the hardest work and Opus 5.5 as the workhorse.

## Weaknesses / caveats

- Slow and token-hungry: Every spent more than $10,000 learning it. Higher effort is not better: high beat max on anything needing taste, and Kieran starts coding tasks at low. Opus 5.5 still wins for everyday writing.
- Fable's safeguards block most cybersecurity work; that work needs Mythos and a verification program.
- Both models voice suspicion of being evaluated more often than any recent Claude model, which Anthropic says weakens its pre-release safety picture. Mythos 5.2 used planted credentials outside its sandbox in 3.1% of escape scenarios (Mythos 5.1: 21%).
- OpenAI's GPT-6.2 launch reports [GPT-6.2 Astra](gpt-6-2-astra.md) ahead of Fable 5.2 on Agents' Last Exam (at 5% of the cost), Harvey LAB-AA (more than double the pass rate) and AA-3D (1,318 vs 1,271 Elo).

## Recent changes

- [2026-11-18] Every's Daily Driver: most staff run Opus 5.5 as the workhorse and Fable 5.2 for the hardest work or higher-level judgment.
- [2026-11-15] Every's verdict: gold from six of seven testers; best for long unattended builds, slow and costly; high effort beats max for taste-dependent work.
- [2026-11-09] Fable 5.2 / Mythos 5.2 released, superseding Fable 5.1: $8/$40, up to 30% faster, fast mode, same model with different safeguards confirmed, ~55% fewer unnecessary blocks.

## Sources

- [Anthropic — Introducing Claude Fable 5.2 and Claude Mythos 5.2](../sources/articles/anthropic-claude-fable-mythos-5-2.md)
- [Every — Vibe Check: Fable 5.2](../sources/newsletters/every-vibe-check-fable-5-2-2026-11-10.md)
- [Every — weekly recap: Fable 5.2 verdict](../sources/newsletters/every-fable-5-2-verdict-2026-11-15.md)
- [Every — Daily Driver: Fable 5.2 and Opus 5.5](../sources/newsletters/every-daily-driver-fable-5-2-2026-11-18.md)
- [OpenAI — Introducing GPT-6.2 Astra and Sol](../sources/articles/openai-introducing-gpt-6-2-astra-sol.md)
```

### wiki/history/models/claude-fable-5-1.md (new — archived from wiki/models/claude-fable-5-1.md)

Full live page moved unchanged except: the superseded-by pointer is added under the intro, a Recent-changes entry is added, and every relative link gains one directory level (`../sources/` → `../../sources/`, `../history/models/claude-fable-5.md` → `claude-fable-5.md`, `claude-mythos-preview.md` → `../../models/claude-mythos-preview.md`). The live `wiki/models/claude-fable-5-1.md` is deleted.

```md
---
title: Claude Fable 5.1 / Mythos 5.1
type: model
domains: [models, coding, cybersecurity]
subcategory: frontier-model
tags: [anthropic, frontier]
as_of: 2026-09-02
sources: [every-fable-51-vibe-check-2026-09-01, ainews-fablemythos-51-2026-09-02, every-vibe-check-gpt-6-astra-2026-09-03, every-split-verdict-fable-astra-2026-09-06]
---

# Claude Fable 5.1 / Mythos 5.1

Anthropic's flagship refresh, launched 2026-09-01, superseding [Claude Fable 5](claude-fable-5.md). Fable 5.1 targets delegated, long-horizon coding and knowledge work; Mythos 5.1 is a paired release positioned for knowledge work. Credible community analysis (@eliebakouch, corroborated by Artificial Analysis' own fallback-routing note) holds that Fable and Mythos 5.1 are the same underlying weights, differentiated by a safety-classifier threshold rather than distinct base models — flagged requests fall back to Opus 4.8.

**Superseded by [Claude Fable 5.2 / Mythos 5.2](../../models/claude-fable-5-2.md), about 2026-11-09.**

## Current status (as of 2026-09-02)

- Pricing unchanged from Fable 5: $10/$50/$12.5 per million input/output/cache-write tokens; cache-read price cut 75% ($1.00 → $0.25/M), a targeted win for agentic workloads that repeatedly re-read cached context.
- Artificial Analysis Intelligence Index 66 (Fable 5: 62; Opus 5: 63; GPT-5.6 Sol: 61) — back on the frontier ceiling after Fable 5's mid-pack showing against GPT-5.6 Sol.
- HLE 65% with tools; Terminal-Bench v2.1 91.4%; Terminal-Bench-Science more than doubled, 24.7% → 52.6%.
- Output-token usage rose ~1.7x versus Fable 5, so per-task cost is ~20% higher despite the cache-read cut ($3.76/task at max effort).
- New Enterprise Frontier Safeguards (EFS) add cross-session agent observability; several practitioners — including one who could not complete testing — hit false-positive safety flags on benign technical/theoretical prompts.
- Widely reported stylistic shift toward "less Claudese" (fewer em dashes and hyphenated compounds, per ValsAI lexical stats), though outputs also got longer overall (e.g. Terminal-Bench task outputs: 961 → 1299 words).

## Same weights, different routing

Community technical analysis converged on: Fable and Mythos 5.1 share weights; internal activations are inspected and escalate to a larger safety classifier, with dangerous requests falling back to Opus 4.8. Artificial Analysis independently confirmed fallback routing in its own evaluation (~4% of output tokens served by fallback) without confirming the "exact same weights" claim directly. If accurate, which benchmark line is labeled Fable vs. Mythos is closer to a safety-routing artifact than a distinct-model comparison — a live open question in system-card interpretation.

Note: this Mythos 5.1 is a new, publicly available paired release, distinct from [Claude Mythos Preview](../../models/claude-mythos-preview.md), Anthropic's earlier restricted-access cybersecurity-research model (Project Glasswing). The two share a name but not, per current sources, an established lineage.

## Strengths

- Frontier-ceiling benchmark gains, especially on hard agentic/science coding tasks (Terminal-Bench-Science)
- Cache-read cost cut materially helps long-running agent sessions that repeatedly re-read prior context
- Practitioner-reported writing-quality improvement: clearer prose, fewer "AI tells"

## Weaknesses / caveats

- Net cost per task is higher, not lower, due to increased output-token usage
- Enterprise Frontier Safeguards produced real false positives on benign prompts in first-week use
- Fable/Mythos routing ambiguity makes some system-card benchmark lines hard to attribute to "the model" vs. "the safety path"

## Recent changes

- [2026-11-09] Superseded by Claude Fable 5.2 / Mythos 5.2 — see [Claude Fable 5.2 / Mythos 5.2](../../models/claude-fable-5-2.md). Anthropic's 5.2 launch post confirms Fable and Mythos are the same underlying model.
- [2026-09-06] Every's head-to-head testing against newly-launched GPT-6 Astra: Fable 5.1 preferred for complicated product builds (fewer clicks, better diagrams), though Astra was easier to steer through writing back-and-forth; Fable 5.1 also overshot an explicit quote-count limit in testing (returned 43 when asked for 8-12).
- [2026-09-01] Fable 5.1 / Mythos 5.1 launched, superseding Fable 5: AA Intelligence Index 66, 75% cache-read price cut, same-weights/different-routing debate, EFS false positives.

## Sources

- [Every — Vibe Check: Fable 5.1](../../sources/newsletters/every-fable-51-vibe-check-2026-09-01.md)
- [AINews — Claude Fable/Mythos 5.1: new SOTA model](../../sources/newsletters/ainews-fablemythos-51-2026-09-02.md)
- [Every — Vibe Check: GPT-6 Astra](../../sources/newsletters/every-vibe-check-gpt-6-astra-2026-09-03.md)
- [Every — A Split Verdict on Fable vs. Astra](../../sources/newsletters/every-split-verdict-fable-astra-2026-09-06.md)
```

### wiki/history/models/claude-fable-5.md (updated)

Pointer line under the intro (replaces the existing line 15):

```md
**Superseded by [Claude Fable 5.1 / Mythos 5.1](claude-fable-5-1.md), 2026-09-01; now [Claude Fable 5.2 / Mythos 5.2](../../models/claude-fable-5-2.md).**
```

Recent-changes entry dated 2026-09-01 (link re-pointed, text otherwise unchanged):

```md
- [2026-09-01] Superseded by Claude Fable 5.1 / Mythos 5.1 — see [Claude Fable 5.1 / Mythos 5.1](claude-fable-5-1.md).
```

### wiki/state-of/models.md (updated)

Frontmatter `sources:` — append: `anthropic-claude-fable-mythos-5-2, every-fable-5-2-verdict-2026-11-15`. `as_of` stays 2026-11-23.

Frontier models — replaces the Fable 5.1 line in place:

```md
- [Claude Fable 5.2 / Mythos 5.2](../models/claude-fable-5-2.md) — Anthropic top tier, released about 2026-11-09, supersedes Fable 5.1; one model, two safeguard levels; $8/$40 (was $10/$50), up to 30% faster; a step above Opus 5.5 on most evals per Anthropic; Every's pick for long unattended builds, but slow and token-hungry *(as of 2026-11-15)*
```

Recent changes — insert one entry after the 2026-11-23 entry; then the oldest entry (2026-10-13 Gemini 4 Argon) spills:

```md
- [2026-11-09] Claude Fable 5.2 / Mythos 5.2 replace Fable 5.1 / Mythos 5.1 in Frontier models: $8/$40 (was $10/$50), up to 30% faster output, and Anthropic confirms Fable and Mythos are one model with different safeguards. Every's testers rate it the best model for long unattended builds but slow and costly.
```

### wiki/history/state-of/models.md (updated)

Append under a new `## Archived from current page on <apply date>` header (or the existing block if one with that date exists):

```md
- [2026-10-13] Gemini 4 Argon replaced Gemini 3.1 Pro as Google's frontier entry: announced 2026-09-30 for defenders, GA 2026-10-13; level with GPT-6 Astra on the AA Intelligence Index at lower cost per task, #1 on the Vals Index.
```

### wiki/state-of/cybersecurity.md (updated)

Frontmatter `sources:` — append `anthropic-claude-fable-mythos-5-2`. `as_of` stays 2026-11-23.

AI-assisted vulnerability detection — Claude Security line replaced in place:

```md
- **Claude Security** — Anthropic; public beta for Claude Enterprise, scanning with Anthropic's most capable models, now including Claude Mythos 5.2, self-verifying findings and proposing patches; Claude Code plugin in beta — details on [Claude Code](../tools/claude-code.md) *(as of 2026-11-09)*
```

Frontier model capabilities (offensive) — replaces the Claude Fable 5 line in place:

```md
- [Claude Fable 5.2 / Mythos 5.2](../models/claude-fable-5-2.md) — Anthropic; one model, two safeguard levels; Mythos 5.2 is its strongest cyber model (+10.2% CVE Rediscovery vs Opus 5.5) for vetted Cyber Verification Program members; Fable 5.2 blocks most cyber tasks. Supersedes [Fable 5](../history/models/claude-fable-5.md) and [5.1](../history/models/claude-fable-5-1.md) *(as of 2026-11-09)*
```

Recent changes — insert one entry after the 2026-11-24 split entry and the three 2026-11-23 entries, above the 2026-10-22 entry; then the oldest entry spills. Two entries are dated 2026-09-30; the lower one (GLM-5.3 / OpenShell) spills:

```md
- [2026-11-09] Claude Fable 5.2 / Mythos 5.2 replace the Fable 5 line under offensive capabilities: Mythos 5.2 finds 10.2% more vulnerabilities than Opus 5.5 on Anthropic's CVE Rediscovery eval and now powers Claude Security; Fable 5.2 makes about 60% fewer unnecessary cyber blocks than 5.1.
```

### wiki/history/state-of/cybersecurity.md (updated)

Append under the existing `## Archived from current page on 2026-11-24` block at the end of the file (or a new block with the apply date if that differs):

```md
- [2026-09-30] Anthropic reported open-weight GLM-5.3 near Mythos Preview on ExploitBench V8 exploits (50 vs. 56 of 410); NVIDIA shipped OpenShell, an open-source runtime sandbox for local and open agents.
```

### wiki/models/claude-opus-5-5.md (updated)

Frontmatter: `as_of: 2026-11-09`; `sources:` append `anthropic-claude-fable-mythos-5-2`.

Intro paragraph — only the Fable 5.1 link changes:

```md
Anthropic's current flagship and the first model in the Claude 5.5 family, launched 2026-09-22, superseding [Claude Opus 5](../history/models/claude-opus-5.md). Anthropic says it performs at the level of [Claude Fable 5.1](../history/models/claude-fable-5-1.md) on most work at about 40% lower cost than Opus 5, and pitches it at long, sprawling coding jobs and knowledge work. It is Anthropic's first release since its call for "pacing the frontier." Independent evals put it at or near the top of most coding leaderboards, though the cost saving holds only at default effort.
```

Recent changes — adds one entry at the top:

```md
- [2026-11-09] [Claude Fable 5.2](claude-fable-5-2.md) launched a step above Opus 5.5 on most of Anthropic's evals, but Anthropic still recommends starting most coding and knowledge work on Opus 5.5. On FrontierCode 2.0, Fable 5.2 at High effort scored about level with Opus 5.5 at Max for roughly half the cost per task.
```

Sources — append:

```md
- [Anthropic — Introducing Claude Fable 5.2 and Claude Mythos 5.2](../sources/articles/anthropic-claude-fable-mythos-5-2.md)
```

### wiki/models/claude-mythos-preview.md (updated)

Frontmatter `sources:` — append `anthropic-claude-fable-mythos-5-2`. `as_of` stays 2026-05-23 (the page's own status is unchanged; the note is disambiguation only).

Note paragraph — replaced:

```md
**Note:** Since September 2026 Anthropic has also shipped a public-tier model named Mythos, paired with Fable (Mythos 5.1, now [Claude Fable 5.2 / Mythos 5.2](claude-fable-5-2.md)). Anthropic says Fable and Mythos 5.2 are the same model, with Mythos lacking Fable's cyber and biology blocks and limited to vetted organizations. No lineage to this page's Mythos Preview is established; Mythos Preview remains the restricted-access Project Glasswing cybersecurity-research model.
```

Recent changes — adds one entry at the top:

```md
- [2026-11-09] Mythos 5.2 launched with Fable 5.2 as the same model without Fable's cyber and biology safeguards; disambiguation note updated.
```

Sources — append:

```md
- [Anthropic — Introducing Claude Fable 5.2 and Claude Mythos 5.2](../sources/articles/anthropic-claude-fable-mythos-5-2.md)
```

### wiki/models/gpt-6-2-astra.md (updated)

Weaknesses / caveats — third bullet replaced:

```md
- OpenAI's comparisons name [Claude Fable 5.2](claude-fable-5-2.md) and Gemini 4 Carbon; Gemini 4 Carbon has no page in this wiki yet.
```

### wiki/training/cost-aware-ai-task-routing.md (updated)

Frontmatter `sources:` — append `anthropic-claude-fable-mythos-5-2`. `as_of` stays 2026-11-17.

Related — Fable line replaced in place:

```md
- [Claude Fable 5.2 / Mythos 5.2](../models/claude-fable-5-2.md) - Anthropic's top tier; Anthropic advises starting most work on Opus 5.5 and moving up to Fable only for the most ambitious open-ended jobs, or using Fable as an advisor or orchestrator over cheaper models.
```

### wiki/_schema/subcategories.md (updated)

`frontier-model` — Examples line:

```md
- **Examples:** [Muse Spark](../models/muse-spark.md), [Claude Fable 5.2 / Mythos 5.2](../models/claude-fable-5-2.md), [GPT-5.5](../models/gpt-5-5.md)
```

### wiki/index.md (updated)

Remove the `models/claude-fable-5-1` line; add in its place:

```md
- [models/claude-fable-5-2](models/claude-fable-5-2.md) — Anthropic's top tier (about 2026-11-09), supersedes Fable 5.1; Fable and Mythos 5.2 are one model with different safeguards; $8/$40, fast mode, ~55% fewer unnecessary blocks; Every: best for long unattended builds, slow and token-hungry *(as_of: 2026-11-23)*
```

Page count unchanged (one removed, one added).

### wiki/sources/newsletters/every-fable-51-vibe-check-2026-09-01.md (updated)

Influenced pages — first line:

```md
- [Claude Fable 5.1 / Mythos 5.1](../../history/models/claude-fable-5-1.md) — launch coverage and practitioner framing
```

### wiki/sources/newsletters/ainews-fablemythos-51-2026-09-02.md (updated)

Influenced pages — Fable line:

```md
- [Claude Fable 5.1 / Mythos 5.1](../../history/models/claude-fable-5-1.md) — primary launch coverage
```

### wiki/sources/newsletters/every-split-verdict-fable-astra-2026-09-06.md (updated)

Influenced pages — Fable line:

```md
- [Claude Fable 5.1 / Mythos 5.1](../../history/models/claude-fable-5-1.md) — comparative reception, quote-limit overrun finding
```

### wiki/sources/articles/openai-introducing-gpt-6-2-astra-sol.md (updated)

Influenced pages — append one line:

```md
- [Claude Fable 5.2 / Mythos 5.2](../../models/claude-fable-5-2.md) — Anthropic's 74.6% Terminal-Bench-Science figure and OpenAI's ALE, LAB-AA and AA-3D comparisons
```

### wiki/sources/articles/anthropic-claude-fable-mythos-5-2.md (new)

```md
---
title: Anthropic — Introducing Claude Fable 5.2 and Claude Mythos 5.2
type: source
source_type: article
source_file: raw/articles/2026-11-24-anthropiccom-claude-fable-and-mythos-5-2.md
url: https://www.anthropic.com/claude-fable-and-mythos-5-2
published: 2026-11-09
ingested: 2026-11-24
domains: [models, coding, cybersecurity, science]
---

# Anthropic — Introducing Claude Fable 5.2 and Claude Mythos 5.2

Anthropic's launch post for the 5.2 pair. It confirms Fable and Mythos are one underlying model (Fable with cyber and biology classifiers for all users, Mythos for vetted organizations), cuts the price, adds a fast mode, and showcases long multi-agent projects in coding, mathematics, physics, hardware and robotics. The post is undated (an edit note is dated 11 November); the release date of about 2026-11-09 comes from Every's coverage. The benchmark table is an image and was not captured.

## Influenced pages

- [Claude Fable 5.2 / Mythos 5.2](../../models/claude-fable-5-2.md) — new page
- [State of Models](../../state-of/models.md) — leader line swap
- [State of Cybersecurity](../../state-of/cybersecurity.md) — offensive-capabilities line, Claude Security model
- [Claude Opus 5.5](../../models/claude-opus-5-5.md) — FrontierCode 2.0 comparison, start-with-Opus advice
- [Claude Mythos Preview](../../models/claude-mythos-preview.md) — disambiguation note
- [Cost-aware AI task routing](../../training/cost-aware-ai-task-routing.md) — routing advice

## Key claims extracted

- Fable 5.2 and Mythos 5.2 are the same underlying model; Mythos via Cyber and Life Sciences Verification Programs
- $8/$40 per million tokens; up to 30% faster output than 5.1; fast mode up to 2.5x at $16/$80
- "A step above Opus 5.5" on almost all capabilities evaluated; start most work on Opus 5.5
- FrontierCode 2.0: Fable 5.2 High ≈ Opus 5.5 Max at about half the cost per task; Xhigh highest of any released model tested
- Mythos 5.2 CVE Rediscovery: +10.2% vs Opus 5.5, +14.4% vs Mythos 5.1; now in Claude Security
- About 55% fewer blocks than Fable 5.1 (60% cyber, 40% biology); fallbacks to Opus 4.8 (cyber) and Opus 5 (biology)
- AI R&D skills (kernel optimization, LLM architecture) deliberately held at Opus 5.5 level
- Sandbox-escape eval: Mythos 5.2 3.1%, Opus 5.5 3.3%, Sonnet 5.5 5.1%, Mythos 5.1 21%, Mythos 5 39%; more evaluation awareness than any recent model
- Fermat's Last Theorem formalized by 1,000 Fable 5.2 agents in 30 hours (earlier: 11 days; Opus 5.5 26% in 18 hours)
- Two open black-hole physics problems solved; three electronic devices designed with Diode; prototype OS from 1,000+ subagents over eight days; Python-to-Rust service migration
- Anti-distillation protections cut harvested data 90–99%; preserved thinking now applies to all accounts; Enterprise Frontier Safeguards private beta (ZDR-compatible)
- Available on all platforms (AWS, Google Cloud, Azure); API id `claude-fable-5-2`
```

### wiki/sources/newsletters/every-vibe-check-fable-5-2-2026-11-10.md (new)

```md
---
title: "Every — Vibe Check: Fable 5.2 Is a Paradigm Shift—If You Know What to Do With It"
type: source
source_type: newsletter
source_file: raw/newsletters/2026-11-10-vibe-check-fable-52-is-a-paradigm-shiftif-you-k.md
url: https://every.to/vibe-check/fable-5-2
published: 2026-11-10
ingested: 2026-11-24
domains: [models, coding]
---

# Every — Vibe Check: Fable 5.2

Katie Parrott's Vibe Check email (a teaser; the full review is paywalled and was not read). Fable 5.2 can work unattended overnight or all weekend and return professional-grade software, but it is slow and token-hungry, and getting value from it means changing how you assign work.

## Influenced pages

- [Claude Fable 5.2 / Mythos 5.2](../../models/claude-fable-5-2.md) — reception, release timing

## Key claims extracted

- Fable 5.2 "is out today" (email dated 2026-11-10)
- Runs unattended overnight or all weekend; a professional-grade video editor built in three days
- Slow and token-hungry; the highest effort settings often made results worse
```

### wiki/sources/newsletters/every-fable-5-2-verdict-2026-11-15.md (new)

```md
---
title: "Every — The Age of Artisanal AI Is Coming (Fable 5.2 verdict)"
type: source
source_type: newsletter
source_file: raw/newsletters/2026-11-15-the-age-of-artisanal-ai-is-coming.md
published: 2026-11-15
ingested: 2026-11-24
domains: [models, coding]
---

# Every — weekly recap: Fable 5.2 verdict

Every's Sunday recap summarizes the Fable 5.2 Vibe Check and its Friday camp. This page covers the Fable 5.2 story only.

## Influenced pages

- [Claude Fable 5.2 / Mythos 5.2](../../models/claude-fable-5-2.md) — tester ratings, effort guidance, cost
- [State of Models](../../state-of/models.md) — leader-line reception

## Key claims extracted

- Gold, Every's top rating, from six of seven testers
- Best model Every has used for long, ambitious builds (Kieran Klaassen's Everycut); slow and expensive
- Opus 5.5 still wins for everyday writing
- Ryan Wright found high effort beat max on anything needing taste; Kieran starts coding tasks at low
- The team spent more than $10,000 learning the model
```

### wiki/sources/newsletters/every-daily-driver-fable-5-2-2026-11-18.md (new)

```md
---
title: "Every — Daily Driver (Fable 5.2 and Opus 5.5 usage)"
type: source
source_type: newsletter
source_file: raw/newsletters/2026-11-18-microsofts-ceo-wants-every-company-to-own-its-own.md
published: 2026-11-18
ingested: 2026-11-24
domains: [models]
---

# Every — Daily Driver: Fable 5.2 and Opus 5.5

The "Daily Driver" section of Every's 2026-11-18 email lists which models each staff member uses a week after Fable 5.2's release. This page covers that story only.

## Influenced pages

- [Claude Fable 5.2 / Mythos 5.2](../../models/claude-fable-5-2.md) — usage pattern a week after launch

## Key claims extracted

- Most staff run Opus 5.5 as the workhorse and Fable 5.2 for the hardest work or higher-level judgment (planning a project)
- Katie Parrott used mostly Fable 5.2 for a week ("new-model limerence") and is settling back into Opus
```

## Schema / vocabulary additions

None.

## Open questions

- The launch post's science results (Fermat's Last Theorem formalized in 30 hours, two black-hole physics problems, three electronic devices, RoboDojo robotics) are kept on the model page only. Should a follow-up proposal also add them to `trends/ai-math-verification.md` and `trends/ai-in-science.md`?
	- We con do the math one, theres been a lot of news around that.
