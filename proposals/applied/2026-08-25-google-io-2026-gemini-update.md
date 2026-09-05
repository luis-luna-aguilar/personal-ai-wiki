---
type: proposal
sources:
  - raw/newsletters/2026-05-20-ainews-google-io-2026-gemini-35-flash-omni.md
  - raw/articles/2026-08-25-bloggoogle-products-and-platforms-products-search-search-io.md
  - raw/newsletters/2026-05-20-gemini-becomes-your-personal-agent.md
status: pending
created: 2026-08-25
---

# Proposal: Google I/O 2026 — Gemini 3.5 Flash, Antigravity 2.0, Gemini Spark, Search AI-Mode

## Summary

### The source

On 19 May 2026 Google used I/O to push Gemini toward "agents as the product." The centerpiece was **Gemini 3.5 Flash**, GA that day and now the default AI Mode model: 1M context, 65K output, four thinking levels, $1.50/$9.00 per million tokens. Google's own numbers, relayed by AINews: Terminal-Bench 2.1 76.2%, MCP Atlas 83.6%. Alongside it came Antigravity 2.0 — a desktop app, CLI and SDK for orchestrating teams of coding agents, whose demo, per Google, built a working OS in 12 hours with 93 parallel sub-agents for under $1K — and Gemini Spark, a 24/7 personal agent on Google Cloud VMs that checks in before major actions. Elizabeth Reid's Search blog adds a multimodal AI-Mode box, generative UI free for everyone this summer, and Antigravity-built mini-apps plus "information agents" for Pro/Ultra. A $100/mo plan appeared; Ultra dropped to $200.

Reception was mixed. Artificial Analysis (via AINews) scores 3.5 Flash at Intelligence Index 55, nine points above Gemini 3 Flash, but 5.5x costlier to run and 75% costlier than Gemini 3.1 Pro — a hard sell for a "Flash." Arena has it #9 in text and frontend code.

### What changes

The Gemini page carries June and July developments that assume 3.5 Flash exists, but the launch, Antigravity and Spark appear nowhere; State of Models has only an unlinked Gemini 3.1 Pro line.

- **Gemini** gains a dated "Google I/O 2026" block in Current status covering the five launches; one Recent changes entry (8 of 10, no spill); four source links, one repairing an April source listed but never linked. Its stale status heading is corrected to the page's 8 July date. Nothing is removed.
- **State of Models** gains a linked Gemini 3.5 Flash leader line under Frontier models beside Gemini 3.1 Pro, dated 20 May; the page stays at 2 July. Its Recent changes list is at cap and the I/O entry would be the oldest, so it goes straight to history.
- Three source pages: Google's Search-blog post, the AINews recap and Superhuman's newsletter. No schema changes.

### What to weigh

Every benchmark, the AA critique and the pricing ladder come solely from AINews — Google's launch post was not fetched — and "Gemini Spark" rests on two newsletters linking to an unfetched Google post. The Frontier-models slot is arguable, since Google pitches this as an agentic/coding model. If you'd rather see the I/O entry live, spill the 29 May Opus 4.8 entry instead. Antigravity stays off State of Coding (Gemini lacks the coding domain; no Antigravity page exists), and a Spark bullet on State of Agents, already over cap, is your call.

## Verification notes

- Fetched the primary source directly: `https://blog.google/products-and-platforms/products/search/search-io-2026/` (Google's own May 19, 2026 post) — confirms the AI-Mode redesign, Gemini 3.5 Flash as the new AI Mode default, Antigravity-powered generative UI (free for everyone this summer) and mini-apps (coming months, Pro/Ultra US first), "information agents" (24/7 background monitoring, Pro/Ultra this summer), agentic booking incl. phone calls, and expanded Personal Intelligence. This primary source does **not** use the name "Gemini Spark" — that name is confirmed instead by both AINews and Superhuman's newsletter coverage, which link to a separate Google blog post (`blog.google/innovation-and-ai/products/gemini-app/next-evolution-gemini-app/`) introducing Gemini Spark as a 24/7 personal agent running on dedicated Google Cloud VMs.
- Checked `wiki/tools/gemini.md` (as_of 2026-07-08): its "Computer use (as of 2026-06-25)" and "Managed agents in Gemini API (as of 2026-07-08)" sections are later developments that assume Gemini 3.5 Flash already exists — they do not carry the I/O benchmark numbers, the AA cost critique, Antigravity, or Gemini Spark. Nothing on the current page is being contradicted or regressed; this only fills a gap dated *before* the page's existing content. Recent changes has 7 of 10 slots used.
- Checked `wiki/state-of/models.md` and `wiki/state-of/agents.md` — neither lists Gemini 3.5 Flash or Antigravity as bullets today (only an unlinked "Gemini 3.1 Pro" text bullet exists in state-of/models.md). `tools/gemini.md` carries `domains: [models, computer-use, agents]`, so the model belongs on `state-of/models.md`; that page is at cap (10), handled via the Spill item. `state-of/agents.md` already carries a newer Gemini line (2026-07-08) and is over cap (13 entries, pre-existing); `state-of/coding.md` is not a domain of the Gemini page. See Review flags / Open questions.

## Intended changes

- [x] **Approve all** — checking this box approves every item in `## Intended changes` and `## Schema / vocabulary additions` below; the individual boxes may stay empty.

- [ ] **Update** `wiki/tools/gemini.md` — fix the `## Current status` heading date, add a new dated subsection covering Google I/O 2026 (Gemini 3.5 Flash GA + benchmarks + AA cost critique, Antigravity 2.0, Gemini Spark, Search AI-Mode redesign), a new Recent changes entry (8 of 10), 3 new source IDs, and 4 `## Sources` lines
    > See draft below

- [ ] **Update** `wiki/state-of/models.md` — add a Gemini 3.5 Flash leader line under "Frontier models" and 2 source IDs
    > See draft below

- [ ] **Spill** `wiki/state-of/models.md` → `wiki/history/state-of/models.md` — record the `[2026-05-19]` Google I/O 2026 Recent-changes entry directly in history (it would be the 11th entry and the oldest by date; live list stays at 10)
    > See draft below

- [ ] **Create** `wiki/sources/articles/google-io-2026-search-blog.md` — primary Google source summary

- [ ] **Create** `wiki/sources/newsletters/ainews-google-io-2026.md` — AINews source summary

- [ ] **Create** `wiki/sources/newsletters/gemini-personal-agent-superhuman-2026-05.md` — Superhuman source summary

## Page drafts

### wiki/tools/gemini.md (updated)

Frontmatter `sources:` list — add three new IDs:

```yaml
sources: [gemini-browser-utility-updates, gemini-deep-research-max, ainews-2026-04-22, google-cloud-next-2026, gemini-downloadable-files-2026-04-30, gemini-computer-use-aside-2026-06, gemini-managed-agents-2026-07, google-io-2026-search-blog, ainews-google-io-2026, gemini-personal-agent-superhuman-2026-05]
```

Section heading — replace the stale heading so it matches the frontmatter `as_of`:

```md
## Current status (as of 2026-07-08)
```

New subsection — insert into `## Current status` between the existing "Downloadable file generation (as of 2026-04-30)" paragraph and the existing "Computer use (as of 2026-06-25)" paragraph:

```md
**Google I/O 2026 (as of 2026-05-19):**

Google used I/O 2026 to push Gemini toward "agents as the product." Key launches:

- **Gemini 3.5 Flash** went GA globally as the new default AI Mode model, positioned as Google's strongest agentic/coding Flash-tier model yet: 1M context, 65K max output, 4 thinking levels, and thought preservation across turns. Google-quoted benchmarks, as relayed by AINews (Google's launch post not fetched): Terminal-Bench 2.1 76.2%, GDPval-AA 1656 Elo, MCP Atlas 83.6%. Independent Artificial Analysis numbers (per AINews, 2026-05-20) are less flattering for a "Flash" model: Intelligence Index 55 (+9 vs Gemini 3 Flash) but 5.5x costlier than Gemini 3 Flash and 75% costlier than Gemini 3.1 Pro to run on AA's suite, at $1.50 / $9.00 per 1M input/output tokens; Arena placed it #9 overall text and #9 Code Arena: Frontend.
- **Antigravity 2.0**: Google's coding-agent stack expands to an agent-first desktop app (core conversations, artifacts, multi-agent orchestration), a CLI, and an SDK for orchestrating teams of coding agents. Google claims (per AINews) that a joint Antigravity + 3.5 Flash demo built a working OS in 12 hours using 93 parallel sub-agents, 15k+ model requests, and under $1K in API credits.
- **Gemini Spark**: a 24/7 personal background agent running on dedicated Google Cloud VMs that proactively handles Workspace tasks and checks in before major actions; local-device access is planned for summer 2026.
- **Search AI-Mode redesign**: Google's biggest Search-box upgrade in over 25 years — a reimagined, multimodal AI-Mode search box (text, images, files, videos, Chrome tabs), plus generative UI: Search uses Antigravity + Gemini 3.5 Flash to assemble custom layouts, visuals, and simulations on the fly, free for everyone this summer. Persistent mini-apps and dashboards for recurring tasks (e.g. a fitness tracker or a home-move planner) follow in the coming months, first for Google AI Pro/Ultra subscribers in the US. Persistent "information agents" (24/7 monitoring with synthesized updates and the ability to take action) roll out first to Pro/Ultra subscribers this summer; agentic booking expands to local services, including phone calls to businesses on the user's behalf (US, this summer).
- New subscription tier (per AINews): a $100/mo plan was added; Ultra was cut from $250 to $200/mo.

Reception was mixed (per AINews): positive on agentic gains, serving speed, and product integration; Artificial Analysis and several posters flagged the Flash-tier pricing/performance tradeoff and some benchmark caveats.
```

Recent changes — full section with the new `[2026-05-19]` bullet inserted in reverse-chronological position (8 of 10 slots used; no spill):

```md
## Recent changes

- [2026-07-08] Gemini API managed agents add MCP support, background execution, custom function calling, and credential refresh; AINews frames Interactions API as Google's default stateful interface for models and agents.
- [2026-06-25] Gemini 3.5 Flash adds built-in computer use for browser, desktop, and mobile with sensitive-action confirmations and prompt-injection shutdown behavior.
- [2026-05-19] Google I/O 2026: Gemini 3.5 Flash GA as the new AI Mode default (per AINews: Terminal-Bench 2.1 76.2%; AA flags Intelligence Index 55 but 5.5x costlier than Gemini 3 Flash), Antigravity 2.0 (desktop/CLI/SDK multi-agent coding orchestration), Gemini Spark (24/7 personal background agent on cloud VMs), and a Search AI-Mode redesign with generative UI, mini-apps, and persistent information agents.
- [2026-04-30] Downloadable file generation from chat: Google/Microsoft Office formats, PDF, CSV, LaTeX, TXT, RTF, Markdown — positions Gemini as an artifact-producing workplace assistant, not only conversational AI
- [2026-04-23] Cloud Next '26: Gemini Enterprise Agent Platform replaces Vertex AI; Agent Studio, 200+ models, Workspace Intelligence GA, Knowledge Catalog, Gemini Embedding 2 GA, and broader agent governance stack
- [2026-04-22] Added benchmark scores for Deep Research Max (93.3% DeepSearchQA, 85.9% BrowseComp, 54.6% HLE); added collaborative planning and code execution capabilities from AINews coverage
- [2026-04-21] Added Deep Research and Deep Research Max: Gemini API public preview, MCP support, multimodal grounding, and native visual reports
- [2026-04-21] Added Chrome Skills, Gemini 3.1 Flash TTS, and native Mac app
```

Sources section — add three new lines, plus the previously missing `ainews-2026-04-22` link so the body matches the frontmatter:

```md
## Sources

- [Gemini browser and utility updates](../sources/newsletters/gemini-browser-utility-updates.md)
- [Gemini Deep Research and Deep Research Max launch](../sources/articles/gemini-deep-research-max.md)
- [AINews — 2026-04-22 (GPT-Image-2, Hermes, Deep Research Max)](../sources/newsletters/ainews-2026-04-22.md)
- [Google Cloud Next 2026 — TPU v8 and Gemini Enterprise Agent Platform](../sources/articles/google-cloud-next-2026.md)
- [Gemini downloadable file generation](../sources/newsletters/gemini-downloadable-files-2026-04-30.md)
- [Gemini computer use and Aside agentic browser](../sources/newsletters/gemini-computer-use-aside-2026-06.md)
- [Gemini managed agents in the API](../sources/newsletters/gemini-managed-agents-2026-07.md)
- [Google I/O 2026 — AI agents and more (Search blog)](../sources/articles/google-io-2026-search-blog.md)
- [AINews — Google I/O 2026: Gemini 3.5 Flash, Omni, Spark, Antigravity](../sources/newsletters/ainews-google-io-2026.md)
- [Superhuman — Gemini becomes your personal agent](../sources/newsletters/gemini-personal-agent-superhuman-2026-05.md)
```

### wiki/state-of/models.md (updated)

Frontmatter `sources:` list — append two new IDs at the end of the existing list (unchanged otherwise; `as_of` stays 2026-07-02):

```yaml
sources: [..., outputmaxxing-amp-compute-utilization-2026-06, google-io-2026-search-blog, ainews-google-io-2026]
```

"Frontier models" subcategory — insert a new bullet directly after the existing `**Gemini 3.1 Pro**` line (existing lines unchanged):

```md
- **Gemini 3.1 Pro** — Google; Arena (May 2026): close second overall; leads creative writing *(as of 2026-05-13)*
- [Gemini 3.5 Flash](../tools/gemini.md) — Google; GA 2026-05-19 as the default AI Mode model and Google's agentic/coding Flash tier; 1M context, $1.50/$9.00 per 1M tokens; per AINews: Google-quoted Terminal-Bench 2.1 76.2% / MCP Atlas 83.6%, Artificial Analysis Intelligence Index 55 but 5.5x costlier than Gemini 3 Flash on AA's suite, Arena #9 text / #9 Code Arena: Frontend *(as of 2026-05-20)*
```

`## Recent changes` — no change to the live list (10 entries, at cap). The new entry is recorded in history instead; see the Spill draft below.

### wiki/history/state-of/models.md (updated — spill)

Append a new archive block at the end of the file (do not reformat existing blocks); if applied on a later date, use that date in the header:

```md
## Archived from current page on 2026-08-25

- [2026-05-19] Google I/O 2026: Gemini 3.5 Flash GA as default AI Mode model, added under Frontier models (per AINews: Terminal-Bench 2.1 76.2%, AA Intelligence Index 55 but 5.5x costlier than Gemini 3 Flash, Arena #9 text)
```

### wiki/sources/articles/google-io-2026-search-blog.md (new)

```md
---
title: Google I/O 2026 — AI agents and more (Search)
type: source
source_type: article
source_file: raw/articles/2026-08-25-bloggoogle-products-and-platforms-products-search-search-io.md
url: https://blog.google/products-and-platforms/products/search/search-io-2026/
published: 2026-05-19
ingested: 2026-08-25
domains: [models, agents]
---

# Google I/O 2026 — AI agents and more (Search)

Google's own Search-team blog post from I/O 2026 (VP Search Elizabeth Reid). Announces Gemini 3.5 Flash as the new default AI Mode model, a redesigned multimodal AI-Mode search box (Google's biggest Search-box upgrade in 25+ years), persistent "information agents" that monitor topics 24/7, expanding agentic booking to new task categories, generative UI and mini-apps built with Google Antigravity + Gemini 3.5 Flash's agentic coding, and expanded Personal Intelligence (Gmail/Photos/Calendar connections) across nearly 200 countries.

## Influenced pages

- [Gemini](../../tools/gemini.md) — new Google I/O 2026 dated subsection
- [State of Models](../../state-of/models.md) — new Gemini 3.5 Flash leader line under Frontier models

## Key claims extracted

- Gemini 3.5 Flash became the default AI Mode model globally, starting May 19, 2026
- New AI-Mode search box: multimodal input (text/image/file/video/Chrome tabs), described as the biggest Search-box upgrade in over 25 years
- Search "information agents": persistent, 24/7 background monitoring with synthesized updates and the ability to take action; launching first for Google AI Pro/Ultra subscribers this summer
- Agentic booking expanded to local experiences/services, including phone calls to businesses on the user's behalf for select categories (home repair, beauty, pet care); rolling out to everyone in the US this summer
- Generative UI: Search assembles custom layouts, interactive visuals, tables, graphs, and simulations on the fly using "the power of Google Antigravity and the agentic coding capabilities of Gemini 3.5 Flash"; available to everyone in Search this summer, free of charge
- Custom mini-apps, dashboards, and trackers for recurring tasks (built with Antigravity) arrive "in the coming months," starting with Google AI Pro/Ultra subscribers in the US
- Personal Intelligence in AI Mode expanding to ~200 countries/98 languages, no subscription required; Gmail/Google Photos connections live, Google Calendar coming soon
```

### wiki/sources/newsletters/ainews-google-io-2026.md (new)

```md
---
title: "AINews — Google I/O 2026: Gemini 3.5 Flash, Omni, Spark, and Antigravity"
type: source
source_type: newsletter
source_file: raw/newsletters/2026-05-20-ainews-google-io-2026-gemini-35-flash-omni.md
url: https://www.latent.space/p/ainews-google-io-2026-gemini-35-flash
published: 2026-05-20
ingested: 2026-08-25
domains: [models, agents]
---

# AINews — Google I/O 2026: Gemini 3.5 Flash, Omni, Spark, and Antigravity

AINews' consolidated recap of Google I/O 2026 (covering the May 18-19, 2026 window), combining Google's own announcement claims with third-party benchmark data (Artificial Analysis, Chatbot Arena) and social reaction. The most technically detailed source for Gemini 3.5 Flash's specs/benchmarks and the AA cost critique, plus a fuller description of the Antigravity 2.0 and Gemini Spark launches than Google's own Search-team post. Google's own Gemini 3.5 Flash launch post was not fetched for this ingest; all benchmark, demo, and pricing figures below are as relayed by AINews.

## Influenced pages

- [Gemini](../../tools/gemini.md) — new Google I/O 2026 dated subsection
- [State of Models](../../state-of/models.md) — new Gemini 3.5 Flash leader line under Frontier models

## Key claims extracted

- Gemini 3.5 Flash: GA today across Gemini app, Search AI Mode, Gemini API, AI Studio, Antigravity, Android Studio, enterprise; 1M context, 65K max output, 4 thinking levels (minimal/low/medium/high), thought preservation across turns; pricing $1.50/$9.00 per 1M input/output tokens, 90% discount on cached input
- Google-quoted benchmarks: Terminal-Bench 2.1 76.2%, GDPval-AA 1656 Elo, MCP Atlas 83.6%; Google claims 4x faster than comparable frontier models, up to 12x faster in Antigravity; Gemini 3.5 Pro said to be coming next month
- Artificial Analysis: Intelligence Index 55 (+9 vs Gemini 3 Flash), >280 output tok/s, MMMU-Pro 84%, hallucination rate 61% (31-pt drop vs Gemini 3 Flash), but 5.5x costlier than Gemini 3 Flash and 75% costlier than Gemini 3.1 Pro on AA's suite
- Arena: #9 overall Text Arena, #9 Code Arena: Frontend, score 1507 (+70 over Gemini 3 Flash), top score in its price tier
- Antigravity 2.0: agent-first desktop app (core conversations, artifacts, multi-agent orchestration), CLI, SDK; Managed Agents in Gemini API give a single API call a hosted Linux sandbox (Bash/Python/Node, browsing, custom markdown-defined skills, repo/GCS mounts); Google-claimed demo built a functioning OS in 12 hours with 93 parallel sub-agents, 15k+ requests, 2.6B tokens, <$1K credits
- Gemini Spark: 24/7 personal AI agent on dedicated Google Cloud VMs, allowing long-running tasks while user devices are closed; checks with users before major actions
- Gemini app: "Neural Expressive" design language, inline Gemini Live voice, Daily Brief digest, macOS app
- Search: redesigned AI-powered search box; generative UI/simulations via Antigravity + 3.5 Flash; information agents (persistent monitoring) rolling out to Pro/Ultra this summer
- New pricing ladder: $100/mo plan added; Ultra cut from $250 to $200/mo
- SynthID pushed across Search/Gemini/Chrome/hardware, with partner adoption from OpenAI, NVIDIA, Kakao, ElevenLabs
- Reception mixed: positive on agentic gains/serving speed/product integration; negative/skeptical on price inflation relative to earlier Flash models, GPT-5.5-medium comparisons, and benchmark caveats (weak TerminalBench-Hard, mediocre MRCR/ARC-AGI-2 cited by some posters); Gemini CLI vs Antigravity CLI naming confusion
```

### wiki/sources/newsletters/gemini-personal-agent-superhuman-2026-05.md (new)

```md
---
title: "Superhuman — Gemini becomes your personal agent"
type: source
source_type: newsletter
source_file: raw/newsletters/2026-05-20-gemini-becomes-your-personal-agent.md
url: https://www.superhuman.ai/p/gemini-gets-24-7-agentic-superpowers
published: 2026-05-20
ingested: 2026-08-25
domains: [models, agents]
---

# Superhuman — Gemini becomes your personal agent

Superhuman's consumer-oriented recap of Google I/O 2026's Gemini updates, confirming Gemini Spark and Gemini Omni by name with direct links to Google's own product blog posts, alongside brief unrelated items (Karpathy joining Anthropic — handled as a separate signal; Creatify's ad-generation agent).

## Influenced pages

- [Gemini](../../tools/gemini.md) — corroborates the Gemini Spark naming and description

## Key claims extracted

- Gemini Spark: a 24/7 personal agent that proactively handles tasks across Workspace, with local computer access coming summer 2026 (linking to `blog.google/innovation-and-ai/products/gemini-app/next-evolution-gemini-app/`)
- Gemini Omni: a model that "creates anything from any input," described as "Nano Banana, but for video" (linking to `blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-omni/`)
- Gemini app also got an updated design, macOS app, and a Daily Brief agent, all built on Gemini 3.5 (linking to `blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-5/`)
- Andrej Karpathy announced joining Anthropic's pretraining team (noted here for completeness; tracked as a separate triage signal, not part of this proposal)
```

## Open questions

- `state-of/models.md` now gets a Gemini 3.5 Flash bullet (under "Frontier models"; see Review flags for the placement and spill choice). Should `state-of/agents.md` also get an Antigravity 2.0 / Gemini Spark bullet under "Agent orchestration"? It already carries a newer Gemini line (2026-07-08) and has 13 Recent-changes entries, over cap — a pre-existing lint gap outside this proposal's scope. And should Antigravity enter `state-of/coding.md`? That requires either a new `tools/antigravity.md` page or adding `coding` to the Gemini page's domains. Happy to draft either in a follow-up.
- "Gemini Spark" is confirmed as a real product name via two independent newsletters (both linking to a Google blog post I did not independently fetch — `blog.google/innovation-and-ai/products/gemini-app/next-evolution-gemini-app/`). I fetched and read Google's Search-team I/O post directly, but not this specific Gemini-app post nor the Gemini 3.5 Flash launch post that carries the benchmark numbers. If you want these corroborated against Google's own pages directly, I can fetch them before applying.
- Every's two pieces in the original triage source list (`google-io-agents-agents-agents.md`, `notes-from-the-foothills-of-the-singularity.md`) turned out to be link-only newsletter forwards (teaser text, not full article bodies) in the raw files — I did not use them as sources here since they added no independently readable content beyond what AINews/Superhuman/the primary blog already cover.
