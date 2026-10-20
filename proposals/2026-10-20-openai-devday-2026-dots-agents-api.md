---
type: proposal
source: raw/newsletters/2026-09-30-ainews-openai-devday-2026-dots-61-sol-ultraf.md
sources:
  - raw/newsletters/2026-09-30-ainews-openai-devday-2026-dots-61-sol-ultraf.md
  - raw/newsletters/2026-09-29-vibe-check-openai-devday-2026.md
  - raw/newsletters/2026-09-30-how-sam-altman-uses-dots-to-take-back-his-time.md
  - raw/newsletters/2026-09-30-why-dwarkesh-is-wrong-about-computer-use-how-ope.md
  - raw/newsletters/2026-10-01-ainews-gemini-4-argon-gdms-answer-to-astrafab.md
  - raw/newsletters/2026-10-04-chatgpt-wants-to-be-your-operating-system.md
  - raw/newsletters/2026-10-06-ainews-reflection-beam-501b-a23b-american-open.md
  - raw/newsletters/2026-10-10-ainews-typesafejev-at-100m-arr-75b-valuati.md
triage: proposals/triage/2026-09-21-to-2026-09-30-ai-digest.md
status: pending
created: 2026-10-20
---

# Proposal: OpenAI DevDay 2026 — dots, Spaces, the Agents API and Codex plan changes

## Summary

### In short

OpenAI now sells the always-on agent with its own computer as ChatGPT's main mode, and early users say it is useful but not yet reliable. At DevDay on 29 September it shipped dots, GPT-6 Astra agents on a private Linux cloud computer with 4,000+ connectors, plus an Agents API that hands developers the Codex harness. Dan Shipper's dot caught a calendar clash but dropped messages and lost its browser. The proposal creates a ChatGPT dots page and updates Codex, State of Agents and Agent runtime platforms. The reason to hesitate is scope: GPT-6.1 Sol, Decisions API and Intelligent UI are left out.

[[#Open questions|Open questions: 2 to answer.]]

### The source

OpenAI's DevDay on 29 September 2026 shipped 22 products and features; AINews's same-day roundup led with dots. A dot is an always-on agent, powered by GPT-6 Astra, that gets its own Linux virtual computer in the cloud. It reaches 4,000+ apps plus Slack and Teams, and the user writes three lists: what it may do alone, what needs approval, and what it must never do. Dots ship to Pro, Business Premium and Enterprise. The main dot's own work does not count against plan usage, but Codex tasks it spawns do. Companion launches were Space and Pages, shared documents, slides and spreadsheets where humans and agents edit together and a dot can be tagged in a comment.

Every's Dan Shipper made his dot, Boo, his main way of using ChatGPT. It caught a flight change that clashed with a meeting proposed in a Slack thread he had not read. It also dropped messages and lost its browser; his verdict is big ambition, unreliable execution. Sam Altman told Shipper his dot triages his mornings and builds several versions of a feature overnight from voice notes. On the developer side, API product lead Nikunj Handa told Latent Space that the new Agents API ships the Codex harness with computer use and compaction built in. The Responses API gained async tool calls (the model keeps reasoning while a tool runs), mid-turn steering over WebSockets, guaranteed 30-minute cache hits with a 12-hour tier in preview, and cache pre-warming.

The plan changes caused trouble. Plans were re-tiered to Plus 1x, Pro $100 5x, Pro $200 10x and a new Pro $500 25x, which roughly halved the old $200 plan's value. A capacity squeeze followed. On 5 October Codex lead Tibo pledged an improvement or a usage reset every day for 28 days, starting with a speed increase of about 50%.

### What changes

The wiki covers Grok Bot and Claude Tag as "agents with their own computer" but has nothing on dots, Spaces or the Agents API. Its Codex pricing section still describes the April $100 Pro launch.

- New page `tools/chatgpt-dots.md` covers dots, Space and Pages, the permission model, plan access, and the mixed hands-on verdicts. Page date 6 October.
- **Codex** gains a DevDay status bullet (cloud environments that run with the laptop closed, Ultrafast, Windows sandbox). Its outdated Pricing section is replaced by a Plans and capacity section covering the re-tiering, Sign in with ChatGPT, the capacity squeeze and the 28-day pledge. Three Recent-changes entries are added and the three oldest move to history. Page date stays 19 October.
- **Agent runtime platforms** gains a bullet on model-lab agent APIs: the Agents API and the Responses API caching and compaction primitives. Page date moves to 30 September.
- **State of Agents** adds a dots line under Agent orchestration. One Recent-changes entry is added and the oldest moves to history.
- The index gains one line. Eight story-specific source pages are added.

### What to weigh

Scope is the main call. GPT-6.1 Sol, the Decisions API and the computer-use half of the Latent Space interview are covered by other triage signals, so this proposal touches them only in passing. GPT-6 Intelligent UI (8 October) and ChatGPT Sites hosting MCP servers are left out because no wiki page fits them. The Every Dots vibe check is paywalled, so its verdict comes from Every's own summaries.

## Intended changes

- [ ] **Approve all** — checking this box approves every item in `## Intended changes` and `## Schema / vocabulary additions` below; the individual boxes may stay empty.

- [ ] **Create** `wiki/tools/chatgpt-dots.md` — new tool page for OpenAI's always-on agents, with Space/Pages
- [ ] **Update** `wiki/tools/codex.md` — new Current-status bullet and heading date; replace `## Pricing (as of 2026-04-21)` with `## Plans and capacity (as of 2026-10-06)`; adds three Recent-changes entries dated 2026-10-09, 2026-10-05 and 2026-09-29; appends six source ids and links
- [ ] **Spill** `wiki/tools/codex.md` → `wiki/history/tools/codex.md` — the list goes from 10 to 13, so the three oldest entries (2026-05-16, 2026-05-15, 2026-05-10) move to history
- [ ] **Update** `wiki/concepts/agent-runtime-platforms.md` — one Current-status bullet, one Execution-runtimes bullet, one Recent-changes entry dated 2026-09-30, two sources; `as_of` → 2026-09-30
- [ ] **Update** `wiki/state-of/agents.md` — add the ChatGPT dots line under Agent orchestration; adds one Recent-changes entry dated 2026-09-29; appends two source ids
- [ ] **Spill** `wiki/state-of/agents.md` → `wiki/history/state-of/agents.md` — the list goes from 10 to 11, so the oldest entry (2026-07-08, Claude Cowork beta) moves to history
- [ ] **Update** `wiki/index.md` — add `tools/chatgpt-dots` under Tools
- [ ] **Create** `wiki/sources/newsletters/ainews-openai-devday-2026-dots-2026-09-30.md`
- [ ] **Create** `wiki/sources/newsletters/every-vibe-check-openai-devday-2026-09-29.md`
- [ ] **Create** `wiki/sources/newsletters/every-sam-altman-dots-ultrafast-2026-09-30.md`
- [ ] **Create** `wiki/sources/newsletters/latent-space-openai-api-agents-api-2026-09-30.md`
- [ ] **Create** `wiki/sources/newsletters/ainews-devday-agent-stack-recap-2026-10-01.md`
- [ ] **Create** `wiki/sources/newsletters/every-chatgpt-operating-system-dots-2026-10-04.md`
- [ ] **Create** `wiki/sources/newsletters/ainews-openai-capacity-squeeze-codex-pledge-2026-10-06.md`
- [ ] **Create** `wiki/sources/newsletters/ainews-codex-windows-sandbox-2026-10-10.md`

## Page drafts

### wiki/tools/chatgpt-dots.md (new)

```md
---
title: ChatGPT dots
type: tool
domains: [agents]
subcategory: agent-orchestration
tags: [openai, agentic, closed-source]
as_of: 2026-10-06
sources: [ainews-openai-devday-2026-dots-2026-09-30, every-vibe-check-openai-devday-2026-09-29, every-sam-altman-dots-ultrafast-2026-09-30, latent-space-openai-api-agents-api-2026-09-30, every-chatgpt-operating-system-dots-2026-10-04, ainews-openai-capacity-squeeze-codex-pledge-2026-10-06]
---

# ChatGPT dots

OpenAI's always-on personal agents inside ChatGPT, launched at DevDay on 2026-09-29. Each dot runs on [GPT-6 Astra](../models/gpt-6-astra.md) and has its own Linux virtual computer in the cloud, so it can run desktop applications and a browser, not only call APIs. It is OpenAI's entry in the always-on agent category alongside [Grok Bot](grok-bot.md), [Meta Muse](meta-muse.md) and [Claude Tag](claude-tag.md).

## Current status (as of 2026-10-06)

- Connects to 4,000+ apps and sits in Slack and Teams; connecting the user's own machine is optional
- The user sets three boundaries: what the dot may do on its own, what needs approval, and what it must never do
- Available on Pro, Business Premium and Enterprise. The primary dot's own work does not draw on plan usage, but Codex tasks it spawns (bug triage, failing builds, PRs) do. Critics note it starts at the $100 Pro plan.
- Companion launches: **Space** and **Pages**, ChatGPT-native documents, slides and spreadsheets shared by humans and agents. A dot can be tagged in a comment, and Every reports edits land faster than an agent working in Google Docs.

## Hands-on reports

- **Dan Shipper (Every):** his dot became his main way of using ChatGPT. It caught a flight change that clashed with a meeting proposed in a Slack thread he had not read. It also dropped messages, tripped over permissions, often could not reach its browser and made him log in to services twice. His verdict: try it if you live in ChatGPT; users happy with Grok Bot, Muse or Instinct should wait a week or two.
- **Sam Altman:** his dot triages urgent issues each morning and alerts him only when something matters. He leaves it voice notes at night and it builds several versions of a feature for him to review.
- **Early testers:** proactive errands such as negotiating with customer service to cut about $500 a year in charges. OpenAI's computer-use lead describes a two-hour meal-prep order done in 15 minutes.

## Why it matters

OpenAI's framing is ChatGPT as the operating system for work: agents, documents and partner apps all running inside it. Dots move the always-on agent from a startup and second-tier product category into ChatGPT itself. The reliability gap reported in week one is the open question.

## Recent changes

- [2026-10-05] Capacity squeeze after DevDay; critics note dots require the $100+ Pro plan.
- [2026-10-04] Every's Dots vibe check: main way Shipper uses ChatGPT, but drops messages and loses its computer connection.
- [2026-09-29] Launched at OpenAI DevDay with Space and Pages; GPT-6 Astra, own Linux cloud computer, 4,000+ connectors, three-tier permission rules.

## Sources

- [AINews — OpenAI DevDay 2026: dots and platform changes](../sources/newsletters/ainews-openai-devday-2026-dots-2026-09-30.md)
- [Every — Vibe Check: OpenAI DevDay 2026](../sources/newsletters/every-vibe-check-openai-devday-2026-09-29.md)
- [Every — How Sam Altman uses dots to take back his time](../sources/newsletters/every-sam-altman-dots-ultrafast-2026-09-30.md)
- [Latent Space — OpenAI's API stack after DevDay (Nikunj Handa)](../sources/newsletters/latent-space-openai-api-agents-api-2026-09-30.md)
- [Every — ChatGPT wants to be your operating system](../sources/newsletters/every-chatgpt-operating-system-dots-2026-10-04.md)
- [AINews — OpenAI capacity squeeze and the Codex 28-day pledge](../sources/newsletters/ainews-openai-capacity-squeeze-codex-pledge-2026-10-06.md)
```

### wiki/tools/codex.md (updated)

Frontmatter: `sources:` appends `ainews-openai-devday-2026-dots-2026-09-30, every-sam-altman-dots-ultrafast-2026-09-30, ainews-devday-agent-stack-recap-2026-10-01, every-vibe-check-openai-devday-2026-09-29, ainews-openai-capacity-squeeze-codex-pledge-2026-10-06, ainews-codex-windows-sandbox-2026-10-10`. `as_of` stays 2026-10-19.

Current status: heading changes from `(as of 2026-08-12)` to `(as of 2026-10-09)`; one bullet is added after the "Mobile app, Remote SSH…" bullet:

```md
- DevDay (2026-09-29): Codex cloud environments keep running with the laptop closed; refreshed CLI with worktrees and `/agents`; Security Cloud; **Ultrafast** mode, up to 8x faster generation (about 300 tok/s) at 6x the price, which SemiAnalysis says runs on NVIDIA GPUs at low batch size, not Cerebras. A Windows sandbox built on Microsoft Execution Containers followed on 2026-10-09. Dots ([ChatGPT dots](chatgpt-dots.md)) hand bug triage, failing builds and PRs to Codex.
```

Replace the whole `## Pricing (as of 2026-04-21)` section with:

```md
## Plans and capacity (as of 2026-10-06)

- **Re-tiering at DevDay:** Plus 1x, Pro $100 5x, Pro $200 10x, and a new Pro $500 25x. That roughly halves the old Pro $200's value and drew heavy backlash. Ultrafast in Codex and ChatGPT is limited to the $500 tier and eligible Enterprise/Edu plans.
- **Sign in with ChatGPT:** plan quota can be spent in about 15 partner apps, including Devin, T3 Code, Nous Portal/Hermes, OpenCode, Pi and Amp.
- **Capacity squeeze (early October):** new $200 sign-ups were reportedly paused and limits effectively halved. SemiAnalysis's limit test found Claude subscriptions deliver 5x+ more API-equivalent value than OpenAI plans.
- **Response:** on 2026-10-05 Codex lead Tibo pledged an improvement or a full reset every day for 28 days. Day one raised default speed for GPT-6 Astra and GPT-6.1 Sol by about 50% (about 30 to 50 tok/s) across subscriptions and Sign in with ChatGPT partners.
- **Sentiment:** Altman says he only prompts on Ultrafast because the speed changes his iteration loop. DHH says GPT-6.1 Sol made Codex his primary tool over Claude.
```

Recent changes: adds three entries below the 2026-10-19 entry, then spills the three oldest (2026-05-16, 2026-05-15, 2026-05-10). Resulting list:

```md
## Recent changes

- [2026-10-19] Added OpenAI's maintenance-pass pattern: short evidence-first prompts for dead code, stale experiments and CI cost, run on GPT-6 Astra and GPT-6.1 Sol in Codex.
- [2026-10-09] Windows sandbox mode built on Microsoft Execution Containers (faster setup, network enforcement, granular file controls); Pro-only composer predictions in beta; DHH switches to Codex as his primary tool.
- [2026-10-05] Capacity squeeze after DevDay: new $200 sign-ups reportedly paused and limits cut; Tibo pledges a Codex improvement or reset every day for 28 days, starting with a ~50% default speed increase.
- [2026-09-29] DevDay: cloud environments that run with the laptop closed, CLI with worktrees and `/agents`, Security Cloud, Ultrafast (up to 8x faster at 6x price), Sign in with ChatGPT for partner apps, and plan re-tiering with a new $500 Pro tier.
- [2026-08-12] ChatGPT desktop app ships for Linux in preview (Ubuntu, Debian, Fedora; x64/ARM64); the desktop app can now import and sync projects, chats, skills, and plugins from other agents into ChatGPT Work and Codex with automatic updates — read as an effort to cut agent-switching friction and make Codex/Desktop an integration hub.
- [2026-08-04] Independent architecture teardown of ChatGPT Work: persistent cloud microVM specs, deliberate split between agent-owned scratch space and product-managed continuity (Personal Context/Library/Projects), browser-service tool-call model, two-tier Scheduled Tasks, Plugin Directory discovery gap, and 10M-user milestone three weeks post-launch.
- [2026-07-14] OpenAI folded Codex into a new ChatGPT desktop "superapp" (Chat/Work/Codex modes); power users pushed back hard, but usage estimates put Codex around 6-7M users by mid-July, roughly 10x growth year-to-date.
- [2026-07-11] Rollout friction: 36-plus model/effort configuration combinations drew complaints; OpenAI ran multiple usage-limit resets and rolled the context limit back from 372K to 272K.
- [2026-07-01] Every frames Codex as a general-purpose workspace agent for inbox, CRM, healthcare coordination, writing, meeting-note, and personal knowledge workflows.
- [2026-05-19] Zoom plugin (meeting-to-task context handoffs), keep-Mac-awake for long-running remote sessions, additional mobile remote-execution improvements
```

Sources: append

```md
- [AINews — OpenAI DevDay 2026: dots and platform changes](../sources/newsletters/ainews-openai-devday-2026-dots-2026-09-30.md)
- [Every — Vibe Check: OpenAI DevDay 2026](../sources/newsletters/every-vibe-check-openai-devday-2026-09-29.md)
- [Every — How Sam Altman uses dots to take back his time](../sources/newsletters/every-sam-altman-dots-ultrafast-2026-09-30.md)
- [AINews — DevDay agent stack recap](../sources/newsletters/ainews-devday-agent-stack-recap-2026-10-01.md)
- [AINews — OpenAI capacity squeeze and the Codex 28-day pledge](../sources/newsletters/ainews-openai-capacity-squeeze-codex-pledge-2026-10-06.md)
- [AINews — Codex Windows sandbox and DHH's switch](../sources/newsletters/ainews-codex-windows-sandbox-2026-10-10.md)
```

### wiki/history/tools/codex.md (updated)

Append (if the live file has no block dated today, open one):

```md

## Archived from current page on <apply date>

- [2026-05-16] 4M+ WAU, 5× messages/user, 1M+ app downloads; Ollama Codex support; MagicPath canvas; /goal as portable MCP; Zed subscription parity; VS Code/Copilot team confirms harness-over-model thesis
- [2026-05-15] Mobile preview in ChatGPT app: steer Codex sessions from iOS/Android while agent runs on devbox; Remote SSH GA; CI/CD hooks; scoped tokens; 30-day enterprise switch promo (2 months free)
- [2026-05-10] Codex-maxxing usage patterns (jxnl): durable threads, Heartbeats (thread-local scheduling), Goals with verification criteria, memory as files (vault + AGENTS.md), $browser/@chrome/@computer, side panel as live work surface
```

### wiki/concepts/agent-runtime-platforms.md (updated)

Frontmatter: `as_of: 2026-09-30`; `sources:` appends `latent-space-openai-api-agents-api-2026-09-30, ainews-openai-devday-2026-dots-2026-09-30`.

Current status: heading changes to `(as of 2026-09-30)`; add as the last bullet:

```md
- Model labs now ship their own harness as an API: OpenAI's Agents API gives developers the Codex harness with computer use and compaction built in.
```

Execution runtimes: add after the "Managed-agent platform primitives" bullet:

```md
- **Model-lab agent APIs.** OpenAI's Agents API (DevDay, 2026-09-29) packages the Codex harness, including the same computer-use implementation the models are trained on, and runs OpenAI's own Codex Security and meeting-notes features. The lower-level Responses API gained async tool calls (the model keeps reasoning while a tool runs), mid-turn steering over WebSockets, guaranteed 30-minute cache hits with a paid 12-hour tier in preview for single long-lived agent threads, cache pre-warming, and server-side compaction at a token threshold, with a manual `/compact` that big coding agents prefer. API lead Nikunj Handa calls the right level of abstraction (memory, storage) an open question.
```

Recent changes: adds one entry at the top:

```md
- [2026-09-30] Added model-lab agent APIs: OpenAI's Agents API (Codex harness with computer use and built-in compaction) and the Responses API's async tools, mid-turn steering, cache guarantees and pre-warming.
```

Sources: append

```md
- [Latent Space — OpenAI's API stack after DevDay (Nikunj Handa)](../sources/newsletters/latent-space-openai-api-agents-api-2026-09-30.md)
- [AINews — OpenAI DevDay 2026: dots and platform changes](../sources/newsletters/ainews-openai-devday-2026-dots-2026-09-30.md)
```

### wiki/state-of/agents.md (updated)

Frontmatter: `sources:` appends `ainews-openai-devday-2026-dots-2026-09-30, every-chatgpt-operating-system-dots-2026-10-04`. `as_of` stays 2026-10-19.

Agent orchestration: add after the Grok Bot line:

```md
- [ChatGPT dots](../tools/chatgpt-dots.md) — OpenAI; always-on GPT-6 Astra agents, each with its own Linux cloud computer, 4,000+ connectors, Slack/Teams presence and do-alone / ask-first / never rules; launched at DevDay with shared Space docs; early reviews find it useful but unreliable *(as of 2026-10-04)*
```

Recent changes: adds one entry between the 2026-10-09 and 2026-09-09 entries, then spills the oldest (2026-07-08, Claude Cowork beta):

```md
- [2026-09-29] Added [ChatGPT dots](../tools/chatgpt-dots.md) to Agent orchestration: OpenAI's always-on agents with their own cloud computers, joining Grok Bot and Claude Tag in the always-on agent category.
```

### wiki/history/state-of/agents.md (updated)

Append under the existing `## Archived from current page on 2026-10-20` block if apply happens today, otherwise under a new block for the apply date:

```md
- [2026-07-08] Claude Cowork beta expands to web/mobile and strengthens scheduled background work, making Cowork a cross-device agent surface rather than only a desktop app.
```

### wiki/index.md (updated)

Add under Tools, after the `tools/grok-bot` line if present, otherwise after `tools/codex`:

```md
- [tools/chatgpt-dots](tools/chatgpt-dots.md) — OpenAI's always-on agents in ChatGPT (DevDay 2026): GPT-6 Astra, own Linux cloud computer, 4,000+ connectors, three-tier permission rules, Space/Pages shared docs; mixed early reviews *(as_of: 2026-10-06)*
```

### wiki/sources/newsletters/ainews-openai-devday-2026-dots-2026-09-30.md (new)

```md
---
title: "AINews — OpenAI DevDay 2026: dots, Ultrafast and platform changes"
type: source
source_type: newsletter
source_file: raw/newsletters/2026-09-30-ainews-openai-devday-2026-dots-61-sol-ultraf.md
url: https://www.latent.space/p/ainews-openai-devday-2026-dots-61
published: 2026-09-30
ingested: 2026-10-20
domains: [agents, coding]
---

# AINews — OpenAI DevDay 2026: dots, Ultrafast and platform changes

AINews's same-day roundup of OpenAI DevDay (2026-09-29). This page covers the dots, platform and plan story; GPT-6.1 Sol benchmarks in the same issue are a separate story.

## Influenced pages

- [ChatGPT dots](../../tools/chatgpt-dots.md) — new page
- [Codex](../../tools/codex.md) — DevDay Codex features, Ultrafast, Sign in with ChatGPT, plan re-tiering
- [Agent runtime platforms](../../concepts/agent-runtime-platforms.md) — Agents API
- [State of Agents](../../state-of/agents.md) — dots line

## Key claims extracted

- Dots: GPT-6 Astra agents with their own cloud computer, 4,000+ apps, Slack/Teams; user-set do-alone / approval / never rules; Pro, Business Premium, Enterprise
- Primary dot's direct work does not draw on plan usage; Codex tasks it spawns do
- Space and Pages: shared human/agent workspaces
- Ultrafast: up to 8x faster (300 tok/s) in Codex, 6x in the API, at 6x price
- Codex: cloud environments that run with the laptop closed, CLI with worktrees and /agents, Security Cloud
- Sign in with ChatGPT for partner apps (Devin, Nous Portal/Hermes, T3 Code); B2B Marketplace via Baseten
- Plans re-tiered to Plus 1x / Pro 100 5x / Pro 200 10x / Pro 500 25x; heavy backlash
```

### wiki/sources/newsletters/every-vibe-check-openai-devday-2026-09-29.md (new)

```md
---
title: "Every — Vibe Check: OpenAI DevDay 2026"
type: source
source_type: newsletter
source_file: raw/newsletters/2026-09-29-vibe-check-openai-devday-2026.md
url: https://every.to/vibe-check
published: 2026-09-29
ingested: 2026-10-20
domains: [agents]
---

# Every — Vibe Check: OpenAI DevDay 2026

Dan Shipper's free preview of his DevDay review: the five launches that matter and a one-paragraph verdict. The full review is subscriber-only.

## Influenced pages

- [ChatGPT dots](../../tools/chatgpt-dots.md) — hands-on verdict, Space
- [Codex](../../tools/codex.md) — partner-app plan usage

## Key claims extracted

- OpenAI's plan: ChatGPT as the operating system for work
- Dots became Shipper's main way to use ChatGPT; caught a flight/meeting clash from an unread Slack thread; also dropped messages, tripped on permissions, often could not reach its browser
- Space: edits land faster than an agent in Google Docs; dots can be tagged in comments
- Plus/Pro plans now work in about 15 partner apps, counting against existing limits
```

### wiki/sources/newsletters/every-sam-altman-dots-ultrafast-2026-09-30.md (new)

```md
---
title: "Every — How Sam Altman Uses Dots to Take Back His Time"
type: source
source_type: newsletter
source_file: raw/newsletters/2026-09-30-how-sam-altman-uses-dots-to-take-back-his-time.md
published: 2026-09-30
ingested: 2026-10-20
domains: [agents]
---

# Every — How Sam Altman Uses Dots to Take Back His Time

Laura Entis's write-up of Dan Shipper's Every Podcast interview with Sam Altman, recorded at DevDay.

## Influenced pages

- [ChatGPT dots](../../tools/chatgpt-dots.md) — Altman's usage
- [Codex](../../tools/codex.md) — Ultrafast sentiment

## Key claims extracted

- Altman's dot triages his mornings and alerts him only to urgent issues
- He leaves voice notes before bed; the dot builds several versions of a feature overnight
- He only prompts on Ultrafast, which burns plan usage at 8x the standard rate, for instant feedback
- Altman expects a paid frontier in intelligence or speed to persist
```

### wiki/sources/newsletters/latent-space-openai-api-agents-api-2026-09-30.md (new)

```md
---
title: "Latent Space — OpenAI's API stack after DevDay (Nikunj Handa)"
type: source
source_type: newsletter
source_file: raw/newsletters/2026-09-30-why-dwarkesh-is-wrong-about-computer-use-how-ope.md
url: https://www.latent.space/p/devday-2026
published: 2026-09-30
ingested: 2026-10-20
domains: [agents]
---

# Latent Space — OpenAI's API stack after DevDay (Nikunj Handa)

Second half of Latent Space's DevDay episode: OpenAI API product lead Nikunj Handa on the developer stack. The first half (Ari Weinstein on computer use) is a separate story.

## Influenced pages

- [Agent runtime platforms](../../concepts/agent-runtime-platforms.md) — model-lab agent APIs
- [ChatGPT dots](../../tools/chatgpt-dots.md) — each dot gets its own Linux cloud computer

## Key claims extracted

- Agents API ships the Codex harness with computer use and built-in compaction; OpenAI's Codex Security and meeting-notes features run on it
- Responses API: async tool calls, mid-turn steering over WebSockets
- Caching: 30-minute cache-hit guarantee; 12-hour tier in preview (higher cache-write price); cache pre-warming; cache diagnostics tool
- Compaction: server-side auto-compaction at a token threshold, or manual /compact, which the Codex harness uses; file-based compaction experiments
- Open question: how much memory and storage abstraction belongs in the API
```

### wiki/sources/newsletters/ainews-devday-agent-stack-recap-2026-10-01.md (new)

```md
---
title: "AINews — DevDay agent stack recap (Ultrafast hardware, usage limits)"
type: source
source_type: newsletter
source_file: raw/newsletters/2026-10-01-ainews-gemini-4-argon-gdms-answer-to-astrafab.md
url: https://www.latent.space/p/ainews-gemini-4-argon-gdms-answer
published: 2026-10-01
ingested: 2026-10-20
domains: [agents, coding]
---

# AINews — DevDay agent stack recap (Ultrafast hardware, usage limits)

Day-after DevDay notes in the AINews Gemini 4 Argon issue. This page covers only the OpenAI story.

## Influenced pages

- [Codex](../../tools/codex.md) — Ultrafast hardware

## Key claims extracted

- Ultrafast quoted at up to 300 tok/s; SemiAnalysis says it runs on NVIDIA GPUs at low batch size, not Cerebras
- ChatGPT Sites can host MCP servers and turn them into installable plugins
- Users report one-off credits worth about $2,500 and complain about cut usage limits
```

### wiki/sources/newsletters/every-chatgpt-operating-system-dots-2026-10-04.md (new)

```md
---
title: "Every — ChatGPT Wants to Be Your Operating System"
type: source
source_type: newsletter
source_file: raw/newsletters/2026-10-04-chatgpt-wants-to-be-your-operating-system.md
published: 2026-10-04
ingested: 2026-10-20
domains: [agents]
---

# Every — ChatGPT Wants to Be Your Operating System

Every's Sunday Context Window issue. This page covers its summaries of the two DevDay vibe checks (DevDay and Dots) and the Altman podcast.

## Influenced pages

- [ChatGPT dots](../../tools/chatgpt-dots.md) — Dots vibe check verdict
- [State of Agents](../../state-of/agents.md) — dots line

## Key claims extracted

- Dots and Space are the workspace; plugin extensions and a subscription usable in 16 partner apps connect other software
- Dots vibe check: main way Shipper uses ChatGPT; dot caught a flight/meeting clash; drops messages, loses its computer connection, requires logging in to every service twice
- Verdict: try dots if you live in ChatGPT; Grok Bots, Muse or Instinct users should stay put a week or two
```

### wiki/sources/newsletters/ainews-openai-capacity-squeeze-codex-pledge-2026-10-06.md (new)

```md
---
title: "AINews — OpenAI capacity squeeze and the Codex 28-day pledge"
type: source
source_type: newsletter
source_file: raw/newsletters/2026-10-06-ainews-reflection-beam-501b-a23b-american-open.md
url: https://www.latent.space/p/ainews-reflection-beam-501b-a23b
published: 2026-10-06
ingested: 2026-10-20
domains: [agents, coding]
---

# AINews — OpenAI capacity squeeze and the Codex 28-day pledge

The subscription-value and capacity story from the AINews Reflection Beam issue (covering 3–5 October).

## Influenced pages

- [Codex](../../tools/codex.md) — plans and capacity
- [ChatGPT dots](../../tools/chatgpt-dots.md) — plan-gating criticism

## Key claims extracted

- SemiAnalysis: Claude subscriptions deliver 5x+ more API-equivalent value than OpenAI plans
- New $200 sign-ups reportedly paused; usage limits effectively halved
- Tibo pledged a meaningful Codex improvement or full reset every day for 28 days
- Day 1: GPT-6 Astra and GPT-6.1 Sol default speed ~30 → ~50 TPS across subscriptions and Sign in with ChatGPT partners (OpenCode, Pi, Amp, Devin)
- Friction: banked Codex resets expire without timezone adjustment; dots limited to $100+ Pro plans
```

### wiki/sources/newsletters/ainews-codex-windows-sandbox-2026-10-10.md (new)

```md
---
title: "AINews — Codex Windows sandbox and DHH's switch"
type: source
source_type: newsletter
source_file: raw/newsletters/2026-10-10-ainews-typesafejev-at-100m-arr-75b-valuati.md
url: https://www.latent.space/p/ainews-typesafejev-at-100m-arr-75b
published: 2026-10-10
ingested: 2026-10-20
domains: [coding]
---

# AINews — Codex Windows sandbox and DHH's switch

The Codex updates from the AINews issue covering 8–9 October.

## Influenced pages

- [Codex](../../tools/codex.md) — Windows sandbox, composer predictions, DHH

## Key claims extracted

- Windows sandbox mode built on Microsoft Execution Containers (MXC): faster setup, network enforcement, granular file controls
- Composer predictions (suggested next message) in beta for Pro only
- DHH says GPT-6.1 Sol made Codex his primary tool over Claude
```

## Schema / vocabulary additions

None.

## Open questions

- Should Space and Pages get their own entry under State of Agents' "Agent-native documents" subcategory (next to Proof and Notion), or stay inside the dots page as drafted?
- The Codex page's ChatGPT Work section records Brockman's statement that Work will merge into Chat by year-end. Dots may be that merge, but no source says so. Should the dots page link the two?
