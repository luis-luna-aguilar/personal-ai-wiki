---
type: proposal
source: raw/newsletters/2026-05-20-ainews-google-io-2026-gemini-35-flash-omni.md
status: pending
created: 2026-08-25
---

# Proposal: Google I/O 2026 — Gemini 3.5 Flash, Antigravity 2.0, Gemini Spark, Search AI-Mode

## Summary

Google I/O 2026 (May 19, 2026) launched Gemini 3.5 Flash GA, a redesigned agentic AI-Mode Search box with on-the-fly generative UI, Antigravity 2.0 (desktop/CLI/SDK multi-agent coding orchestration), and Gemini Spark (a 24/7 personal background agent). This proposal was flagged `verify-first` in triage because `tools/gemini.md` already has newer (2026-06-25 and 2026-07-08) entries covering Gemini 3.5 Flash's computer-use capability and Gemini API managed agents — **verification finding: those newer entries do NOT cover the I/O-era details below** (the specific benchmark numbers, the Artificial Analysis cost critique, Antigravity 2.0, Gemini Spark, or the Search AI-Mode redesign), so this is genuinely new/uncaptured content, added as a dated subsection rather than a page rewrite. Andrej Karpathy's move to Anthropic (reported in the same news cycle) is excluded — it's a separate signal being handled elsewhere.

## Verification notes

- Fetched the primary source directly: `https://blog.google/products-and-platforms/products/search/search-io-2026/` (Google's own May 19, 2026 post) — confirms the AI-Mode redesign, Gemini 3.5 Flash as the new AI Mode default, Antigravity-powered generative UI/mini-apps in Search, "information agents" (24/7 background monitoring), and expanded Personal Intelligence. This primary source does **not** use the name "Gemini Spark" — that name is confirmed instead by both AINews and Superhuman's newsletter coverage, which link to a separate Google blog post (`blog.google/innovation-and-ai/products/gemini-app/next-evolution-gemini-app/`) introducing Gemini Spark as a 24/7 personal agent running on dedicated Google Cloud VMs.
- Checked `wiki/tools/gemini.md` (as_of 2026-07-08): its "Computer use (as of 2026-06-25)" and "Managed agents in Gemini API (as of 2026-07-08)" sections are later developments that assume Gemini 3.5 Flash already exists — they do not carry the I/O benchmark numbers, the AA cost critique, Antigravity, or Gemini Spark. Nothing on the current page is being contradicted or regressed; this only fills a gap dated *before* the page's existing content.
- Checked `wiki/state-of/models.md` and `wiki/state-of/agents.md` — neither lists Gemini 3.5 Flash or Antigravity as bullets today (only an unlinked "Gemini 3.1 Pro" text bullet exists in state-of/models.md). Both state-of pages are already at or near their `recent_changes_cap` (10) from unrelated recent entries, so to avoid an unnecessary spill cascade this proposal deliberately scopes the update to `tools/gemini.md` only, where there is headroom (6 of 10 slots used). See Open Questions.

## Intended changes

- [ ] **Update** `wiki/tools/gemini.md` — add a new dated subsection covering Google I/O 2026 (Gemini 3.5 Flash GA + benchmarks + AA cost critique, Antigravity 2.0, Gemini Spark, Search AI-Mode redesign), a new Recent changes entry, and 3 new source references
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

New subsection — insert into `## Current status` between the existing "Downloadable file generation (as of 2026-04-30)" paragraph and the existing "Computer use (as of 2026-06-25)" paragraph:

```md
**Google I/O 2026 (as of 2026-05-19):**

Google used I/O 2026 to push Gemini toward "agents as the product." Key launches:

- **Gemini 3.5 Flash** went GA globally as the new default AI Mode model, positioned as Google's strongest agentic/coding Flash-tier model yet: 1M context, 65K max output, 4 thinking levels, and thought preservation across turns. Google-quoted benchmarks: Terminal-Bench 2.1 76.2%, GDPval-AA 1656 Elo, MCP Atlas 83.6%. Independent Artificial Analysis numbers are less flattering for a "Flash" model: Intelligence Index 55 (+9 vs Gemini 3 Flash) but 5.5x costlier than Gemini 3 Flash and 75% costlier than Gemini 3.1 Pro to run on AA's suite, at $1.50 / $9.00 per 1M input/output tokens; Arena placed it #9 overall text and #9 Code Arena: Frontend.
- **Antigravity 2.0**: Google's coding-agent stack expands to a desktop app, CLI, and SDK for orchestrating teams of coding agents (multi-agent orchestration, scheduled tasks, native voice). A joint Antigravity + 3.5 Flash demo built a working OS in 12 hours using 93 parallel sub-agents, 15k+ model requests, and under $1K in API credits.
- **Gemini Spark**: a 24/7 personal background agent running on dedicated Google Cloud VMs that proactively handles Workspace tasks and checks in before major actions; local-device access is planned for summer 2026.
- **Search AI-Mode redesign**: Google's biggest Search-box upgrade in over 25 years — a reimagined, multimodal AI-Mode search box, plus generative UI: Search uses Antigravity + Gemini 3.5 Flash to build custom mini-apps, dashboards, and visualizations on the fly for recurring tasks (e.g. a fitness tracker or a home-move planner), rolling out to everyone this summer. Persistent "information agents" (24/7 monitoring with synthesized updates and the ability to take action) roll out first to Google AI Pro/Ultra subscribers this summer.
- New subscription tier: a $100/mo plan was added; Ultra was cut from $250 to $200/mo.

Reception was mixed: independent observers (Artificial Analysis, several ML Twitter accounts) flagged the Flash-tier pricing/performance tradeoff, and Every's own coverage called the keynote "not flashy" despite framing it as strategically important.
```

Recent changes — insert new bullet in chronological position (between the existing 2026-06-25 and 2026-04-30 entries):

```md
## Recent changes

- [2026-07-08] Gemini API managed agents add MCP support, background execution, custom function calling, and credential refresh; AINews frames Interactions API as Google's default stateful interface for models and agents.
- [2026-06-25] Gemini 3.5 Flash adds built-in computer use for browser, desktop, and mobile with sensitive-action confirmations and prompt-injection shutdown behavior.
- [2026-05-19] Google I/O 2026: Gemini 3.5 Flash GA as the new AI Mode default (Terminal-Bench 2.1 76.2%; AA flags Intelligence Index 55 but 5.5x costlier than Gemini 3 Flash), Antigravity 2.0 (desktop/CLI/SDK multi-agent coding orchestration), Gemini Spark (24/7 personal background agent on cloud VMs), and a Search AI-Mode redesign with generative-UI mini-apps and persistent information agents.
- [2026-04-30] Downloadable file generation from chat: Google/Microsoft Office formats, PDF, CSV, LaTeX, TXT, RTF, Markdown — positions Gemini as an artifact-producing workplace assistant, not only conversational AI
- [2026-04-23] Cloud Next '26: Gemini Enterprise Agent Platform replaces Vertex AI; Agent Studio, 200+ models, Workspace Intelligence GA, Knowledge Catalog, Gemini Embedding 2 GA, and broader agent governance stack
- [2026-04-22] Added benchmark scores for Deep Research Max (93.3% DeepSearchQA, 85.9% BrowseComp, 54.6% HLE); added collaborative planning and code execution capabilities from AINews coverage
- [2026-04-21] Added Deep Research and Deep Research Max: Gemini API public preview, MCP support, multimodal grounding, and native visual reports
```
(the 7th entry — [2026-04-21] Added Chrome Skills, Gemini 3.1 Flash TTS, and native Mac app — stays; no spill needed, 7 of 10 slots used)

Sources section — add three new lines:

```md
## Sources

- [Gemini browser and utility updates](../sources/newsletters/gemini-browser-utility-updates.md)
- [Gemini Deep Research and Deep Research Max launch](../sources/articles/gemini-deep-research-max.md)
- [Google Cloud Next 2026 — TPU v8 and Gemini Enterprise Agent Platform](../sources/articles/google-cloud-next-2026.md)
- [Gemini downloadable file generation](../sources/newsletters/gemini-downloadable-files-2026-04-30.md)
- [Gemini computer use and Aside agentic browser](../sources/newsletters/gemini-computer-use-aside-2026-06.md)
- [Gemini managed agents in the API](../sources/newsletters/gemini-managed-agents-2026-07.md)
- [Google I/O 2026 — AI agents and more (Search blog)](../sources/articles/google-io-2026-search-blog.md)
- [AINews — Google I/O 2026: Gemini 3.5 Flash, Omni, Spark, Antigravity](../sources/newsletters/ainews-google-io-2026.md)
- [Superhuman — Gemini becomes your personal agent](../sources/newsletters/gemini-personal-agent-superhuman-2026-05.md)
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

Google's own Search-team blog post from I/O 2026 (VP Search Elizabeth Reid). Announces Gemini 3.5 Flash as the new default AI Mode model, a redesigned multimodal AI-Mode search box (Google's biggest Search-box upgrade in 25+ years), persistent "information agents" that monitor topics 24/7, expanding agentic booking to new task categories, generative UI/mini-apps built with Google Antigravity + Gemini 3.5 Flash's agentic coding, and expanded Personal Intelligence (Gmail/Photos/Calendar connections) across nearly 200 countries.

## Influenced pages

- [Gemini](../../tools/gemini.md) — new Google I/O 2026 dated subsection

## Key claims extracted

- Gemini 3.5 Flash became the default AI Mode model globally, starting May 19, 2026
- New AI-Mode search box: multimodal input (text/image/file/video/Chrome tabs), described as the biggest Search-box upgrade in over 25 years
- Search "information agents": persistent, 24/7 background monitoring with synthesized updates; rolling out to Google AI Pro/Ultra subscribers this summer
- Agentic booking expanded to local experiences/services, including phone calls to businesses on the user's behalf for select categories (US, this summer)
- Generative UI: Search can build custom mini-apps, dashboards, and trackers on the fly using "the power of Google Antigravity and the agentic coding capabilities of Gemini 3.5 Flash"
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

AINews' consolidated recap of Google I/O 2026 (covering the May 18-19, 2026 window), combining Google's own announcement claims with third-party benchmark data (Artificial Analysis, Chatbot Arena) and social reaction. The most technically detailed source for Gemini 3.5 Flash's specs/benchmarks and the AA cost critique, plus a fuller description of the Antigravity 2.0 and Gemini Spark launches than Google's own Search-team post.

## Influenced pages

- [Gemini](../../tools/gemini.md) — new Google I/O 2026 dated subsection

## Key claims extracted

- Gemini 3.5 Flash: GA today across Gemini app, Search AI Mode, Gemini API, AI Studio, Antigravity, Android Studio, enterprise; 1M context, 65K max output, 4 thinking levels, thought preservation across turns; pricing $1.50/$9.00 per 1M input/output tokens
- Google-quoted benchmarks: Terminal-Bench 2.1 76.2%, GDPval-AA 1656 Elo, MCP Atlas 83.6%; Google claims 4x faster than comparable frontier models, up to 12x faster in Antigravity
- Artificial Analysis: Intelligence Index 55 (+9 vs Gemini 3 Flash), MMMU-Pro 84%, hallucination rate 61% (31-pt drop vs Gemini 3 Flash), but 5.5x costlier than Gemini 3 Flash and 75% costlier than Gemini 3.1 Pro on AA's suite
- Arena: #9 overall Text Arena, #9 Code Arena: Frontend, score 1507 (+70 over Gemini 3 Flash)
- Antigravity 2.0: desktop app (multi-agent orchestration, artifacts), CLI, SDK; Managed Agents in Gemini API give a single API call a hosted Linux sandbox (Bash/Python/Node, browsing, custom skills, repo/GCS mounts); demo built a functioning OS in 12 hours with 93 parallel sub-agents, 15k+ requests, 2.6B tokens, <$1K credits
- Gemini Spark: 24/7 personal AI agent on cloud VMs, checks in before major actions
- Search: redesigned AI-powered search box; generative UI/simulations via Antigravity + 3.5 Flash; information agents (persistent monitoring) rolling out to Pro/Ultra this summer
- New pricing ladder: $100/mo plan added; Ultra cut from $250 to $200/mo
- SynthID pushed across Search/Gemini/Chrome/hardware, with partner adoption from OpenAI, NVIDIA, Kakao, ElevenLabs
- Reception mixed: positive on agentic gains/serving speed/product integration; negative/skeptical on price inflation relative to earlier Flash models and some benchmark caveats (weak Terminal-Bench Hard, mediocre MRCR/ARC-AGI-2 cited by some posters)
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

- Should `state-of/models.md` also get a Gemini 3.5 Flash bullet under "Coding models," and/or `state-of/agents.md` an Antigravity 2.0 bullet under "Agent orchestration" / "Agentic coding workspace"? Both state-of pages are effectively at their `recent_changes_cap` (10) already from unrelated entries — `state-of/agents.md` in fact already has 13 Recent-changes entries, over cap, which looks like a pre-existing lint gap outside this proposal's scope. I scoped this proposal to `tools/gemini.md` only to avoid compounding that. Happy to add the state-of bullets in a follow-up if you'd like them now instead.
- "Gemini Spark" is confirmed as a real product name via two independent newsletters (both linking to a Google blog post I did not independently fetch — `blog.google/innovation-and-ai/products/gemini-app/next-evolution-gemini-app/`). I fetched and read Google's Search-team I/O post directly, but not this specific Gemini-app post. If you want Gemini Spark corroborated against Google's own product page directly, I can fetch it before applying.
- Every's two pieces in the original triage source list (`google-io-agents-agents-agents.md`, `notes-from-the-foothills-of-the-singularity.md`) turned out to be link-only newsletter forwards (teaser text, not full article bodies) in the raw files — I did not use them as sources here since they added no independently readable content beyond what AINews/Superhuman/the primary blog already cover.
