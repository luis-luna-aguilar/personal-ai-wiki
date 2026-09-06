---
type: proposal
source: proposals/2026-09-05-maintenance-findings.md
status: pending
created: 2026-09-05
---

# Proposal: Maintenance M3 — vocabulary & filing

## Summary

### The source

This is the second cleanup batch from the 2026-09-05 maintenance pass — this time the audit was tags, subcategories, and where things are filed, not facts. It compared every page's `tags:` and `subcategory:` against the two controlled-vocabulary files, and every tool/model page's `domains:` against which dashboards actually list it.

The tag findings are small and mechanical: eight tags in use that were never declared, five declared vendor tags nobody's using, one subcategory with a typo, a handful of tools filed under a subcategory whose own definition doesn't fit them, and a couple of structural odds and ends (a trend page with no domain at all, a history file with an invalid `type:`, five source pages living in the wrong folder for their own `source_type`). All of that is drafted below as straightforward fixes.

The domain-vs-dashboard question is bigger. AGENTS.md's written rule is that a tool belongs on a state-of dashboard if its `domains:` includes that dashboard's domain — no exceptions stated. In practice, 66 pages carry a domain their dashboard doesn't list them under, and 3 sit on a dashboard without the matching domain. Chasing that down turned up something the mechanical count couldn't see: `state-of/agents.md` has its own scoping sentence right under the title restricting it to "coding-adjacent systems when they are also relevant as agent orchestration, framework, or deployment surfaces" — meaning the page has already, deliberately, opted out of the written rule for exactly the cases (Claude Code, Cursor, GPT-5.5, DeepSeek V4) that make up most of the 66. No other dashboard carries that kind of caveat.

### What changes

**Tags:** declares `cognition` as a vendor tag (undeclared but already used on FrontierCode; also missing from Devin and Windsurf, both Cognition products); drops seven tags that duplicate a domain or subcategory instead of naming something reusable; adds five already-declared vendor tags to the pages that should carry them.

**Filing:** fixes Cartesia's subcategory typo; refiles E2B into the sandbox-provider subcategory built for exactly this kind of tool (schema example and **State of Agents** listing both move); refiles the OpenAI Agents SDK the other way, from orchestration into frameworks, since it's an SDK, not a hosted runtime; folds **State of Agents**'s undeclared "Persistent coding agents" section into the two sections it duplicates; widens two subcategories' parent domains so Microsoft Copilot and Orca's placement matches the schema meant to justify it; gives a domainless trend page a domain; drops an invalid `type:` from one history file; relocates five source-summary pages into the folder matching their own `source_type`, fixing every inbound link.

**Dashboards:** adds ten of the cleanest missing entries — Impeccable and Nano Banana 2 on **State of Creative**, a new Document intelligence section on **State of Finance** and **State of Healthcare** (the subcategory exists in schema, on no dashboard yet), OpenAI Privacy Filter on **State of Cybersecurity** — plus three domain additions the other way (Codex, Devin, GPT-Realtime-2), where a tool is already on a dashboard and its own frontmatter just needs to catch up.

### What to weigh

The big one is in Open Questions: whether "everything in the domain" or "leaders only, curated per page" is actually the wiki's policy, since the wiki itself is inconsistent about it. This proposal doesn't resolve that — it fixes the ten clearest cases (tools that fit an existing or clearly-implied dashboard section) and leaves roughly 50 model-vs-tool-shaped-dashboard mismatches for whichever policy gets chosen. Everything else here is close to risk-free: no new facts, just controlled-vocabulary hygiene and file location.

## Intended changes

- [x] **Approve all** — checking this box approves every item in `## Intended changes` and `## Schema / vocabulary additions` below; the individual boxes may stay empty.

- [ ] **Update** `wiki/tools/devin.md`, `wiki/tools/windsurf.md` — add the `cognition` vendor tag (declared below); both are Cognition products per their own page text

- [ ] **Update** `wiki/benchmarks/agents-last-exam.md`, `wiki/benchmarks/frontiercode.md`, `wiki/concepts/agent-labs-vs-model-labs.md`, `wiki/tools/databricks.md`, `wiki/tools/paperclip.md`, `wiki/tools/cartesia.md` — drop 7 undeclared tags that duplicate a domain/subcategory or don't generalize: `benchmark` (redundant with `type: benchmark`), `labor-market`, `competitive-dynamics`, `moats`, `enterprise`, `self-hosted`, `voice` (already the page's domain)

- [ ] **Update** `wiki/tools/seedance-2.md`, `wiki/tools/eleven-v3.md`, `wiki/tools/elevenlabs-scribe.md`, `wiki/models/minimax-m3.md`, `wiki/tools/mistral-document-ai.md`, `wiki/tools/hermes-agent.md` — add 5 already-declared vendor tags that are missing from the pages they describe: `bytedance`, `elevenlabs` (×2 pages), `minimax`, `mistral`, `nousresearch`

- [ ] **Update** `wiki/tools/cartesia.md` — fix `subcategory: voice-model` → `voice-models` (matches the declared schema slug)

- [ ] **Update** `wiki/tools/e2b.md`, `wiki/state-of/agents.md`, `wiki/_schema/subcategories.md` — refile E2B from `agent-framework` to `agent-sandbox-infra` (it's a sandbox runtime, not an SDK); move its dashboard entry to the sandbox section; add it to the subcategory's Examples line

- [ ] **Update** `wiki/tools/openai-agents-sdk.md`, `wiki/state-of/agents.md` — refile from `agent-orchestration` to `agent-framework` (it's a builder's SDK, not a hosted runtime); move its dashboard entry from Agent orchestration to Agent frameworks

- [ ] **Update** `wiki/state-of/agents.md` — fold the "Persistent coding agents" section into Agent frameworks and Agent orchestration: Hermes Agent's line already exists under Agent frameworks (merged, keeping the fuller wording); Devin Auto-Triage moves to Agent orchestration (it's a persistent hosted-supervision case like the other entries there); OpenClaw's unlinked entry moves to Agent frameworks

- [ ] **Update** `wiki/_schema/subcategories.md` — add `agents` to the parent-domain list of `ai-assistant` and `agentic-coding-workspace`, since Microsoft Copilot and Orca (both domain `agents`) already use these subcategories on the agents dashboard

- [ ] **Update** `wiki/trends/llm-as-discovery-channel.md` — add `domains: [models]` (required field, currently empty; the page is about how people use LLMs generally, not any one vertical, so `models` is the closest fit — see Open Questions)

- [ ] **Update** `wiki/history/tools/claude-code.md` — remove the frontmatter block entirely (`type: history` isn't a valid page type; every sibling history file that predates this convention carries no frontmatter at all)

- [ ] **Move** `wiki/sources/articles/claude-code-monitor.md` → `wiki/sources/tweets/claude-code-monitor.md` (its own `source_type: tweet` says so); fix the one inbound link on `wiki/tools/claude-code.md`

- [ ] **Move** `wiki/sources/articles/cursor-pr-demos.md` → `wiki/sources/tweets/cursor-pr-demos.md`; fix the one inbound link on `wiki/tools/cursor.md`

- [ ] **Move** `wiki/sources/articles/langchain-better-harness.md` → `wiki/sources/tweets/langchain-better-harness.md`; fix the five inbound links across `wiki/concepts/agent-improvement-loop.md` and `wiki/concepts/harness.md`

- [ ] **Move** `wiki/sources/articles/openai-pro-100.md` → `wiki/sources/tweets/openai-pro-100.md`; fix the one inbound link on `wiki/tools/codex.md`

- [ ] **Move** `wiki/sources/articles/perplexity-computer-plaid.md` → `wiki/sources/newsletters/perplexity-computer-plaid.md` (its own `source_type: newsletter` says so); fix the one inbound link on `wiki/tools/perplexity-computer.md`

- [ ] **Update** `wiki/state-of/creative.md` — add Impeccable to "Visual design & prototyping" and Nano Banana 2 to "AI image generation"; both carry the `creative` domain and aren't listed

- [ ] **Update** `wiki/state-of/finance.md` — add a new "Document intelligence" section with Mistral Document AI and LandingAI Agentic Document Extraction; the subcategory's schema entry already names `finance` as a parent domain and neither page is on any dashboard

- [ ] **Update** `wiki/state-of/healthcare.md` — add a new "Document intelligence" section with Mistral Document AI (LandingAI doesn't carry the `healthcare` domain, so it's finance-only)

- [ ] **Update** `wiki/state-of/cybersecurity.md` — add OpenAI Privacy Filter to "AI security tooling"; it carries the `cybersecurity` domain and isn't listed anywhere on the page

- [ ] **Update** `wiki/tools/codex.md` — add the `agents` domain (Codex is already listed on `state-of/agents.md` as "Workspace Agents" without it)

- [ ] **Update** `wiki/tools/devin.md` — add the `cybersecurity` domain (Devin is already listed on `state-of/cybersecurity.md`'s Devin Security Swarm entries without it)

- [ ] **Update** `wiki/tools/gpt-realtime-2.md` — add the `models` domain (it's already linked from `state-of/models.md` without it)

## Page drafts

### wiki/tools/devin.md (updated)

Frontmatter `tags:` line:

```yaml
tags: [cognition]
```

### wiki/tools/windsurf.md (updated)

Frontmatter `tags:` line:

```yaml
tags: [cognition, closed-source, agentic]
```

### wiki/benchmarks/agents-last-exam.md (updated)

Frontmatter `tags:` line — drops `benchmark` and `labor-market`:

```yaml
tags: []
```

### wiki/benchmarks/frontiercode.md (updated)

Frontmatter `tags:` line — drops `benchmark`, keeps `cognition` (already present):

```yaml
tags: [cognition]
```

### wiki/concepts/agent-labs-vs-model-labs.md (updated)

Frontmatter `tags:` line — drops `competitive-dynamics` and `moats`:

```yaml
tags: []
```

### wiki/tools/databricks.md (updated)

Frontmatter `tags:` line — drops `enterprise`:

```yaml
tags: [closed-source]
```

### wiki/tools/paperclip.md (updated)

Frontmatter `tags:` line — drops `self-hosted`:

```yaml
tags: [open-source, agentic]
```

### wiki/tools/cartesia.md (updated)

Frontmatter — drops the `voice` tag and fixes the subcategory typo:

```yaml
subcategory: voice-models
tags: []
```

### wiki/tools/seedance-2.md (updated)

Frontmatter `tags:` line:

```yaml
tags: [bytedance, closed-source]
```

### wiki/tools/eleven-v3.md (updated)

Frontmatter `tags:` line:

```yaml
tags: [elevenlabs, closed-source]
```

### wiki/tools/elevenlabs-scribe.md (updated)

Frontmatter `tags:` line:

```yaml
tags: [elevenlabs, closed-source]
```

### wiki/models/minimax-m3.md (updated)

Frontmatter `tags:` line:

```yaml
tags: [minimax, agentic]
```

### wiki/tools/mistral-document-ai.md (updated)

Frontmatter `tags:` line (this file also gets a subcategory-Examples cross-reference below and a new dashboard listing — see the `state-of/finance.md` and `state-of/healthcare.md` drafts):

```yaml
tags: [mistral, closed-source]
```

### wiki/tools/hermes-agent.md (updated)

Frontmatter `tags:` line — Hermes Agent is NousResearch's framework per its own body text ("NousResearch's open-source autonomous agent framework"):

```yaml
tags: [nousresearch, open-source, agentic]
```

### wiki/tools/e2b.md (updated)

Frontmatter subcategory change:

```yaml
subcategory: agent-sandbox-infra
```

### wiki/tools/openai-agents-sdk.md (updated)

Frontmatter subcategory change:

```yaml
subcategory: agent-framework
```

### wiki/_schema/subcategories.md (updated)

`agent-sandbox-infra` Examples line — add E2B:

> **Before:**
> `- **Examples:** [Daytona](../tools/daytona.md), [Modal](../tools/modal.md), [Railway](../tools/railway.md)`
>
> **After:**
> `- **Examples:** [Daytona](../tools/daytona.md), [Modal](../tools/modal.md), [Railway](../tools/railway.md), [E2B](../tools/e2b.md)`

`ai-assistant` and `agentic-coding-workspace` — add `agents` to each Parent domain(s) line:

> **Before (`ai-assistant`):** `- **Parent domain(s):** models`
> **After:** `- **Parent domain(s):** models, agents`
>
> **Before (`agentic-coding-workspace`):** `- **Parent domain(s):** coding`
> **After:** `- **Parent domain(s):** coding, agents`

### wiki/state-of/agents.md (updated)

`### Agent orchestration` section — remove the OpenAI Agents SDK line (moves to Frameworks below):

> **Before:** includes `- [OpenAI Agents SDK](../tools/openai-agents-sdk.md) — model-native harness with native sandbox execution, durable checkpoint / rehydration, and provider-neutral manifests *(as of 2026-04-15)*`
> **After:** that line removed; the rest of the section is unchanged.

`### Agent frameworks` section — add OpenAI Agents SDK, merge in the fuller Hermes Agent wording, add the OpenClaw entry from the folded Persistent-agents section:

```md
### Agent frameworks

SDKs and development kits for building custom agents with tools, multi-agent patterns, and runtime scaffolding.

- [Gemini](../tools/gemini.md) / Gemini API managed agents — Google; hosted managed-agent interface with MCP support, background execution, custom function calling, credential refresh, and Interactions API statefulness *(as of 2026-07-08)*
- [Google ADK](../tools/google-adk.md) — Google; open-source ADK now positioned as the developer layer inside Gemini Enterprise Agent Platform; Agent Studio adds a low-code wrapper, and Model Garden expands the surrounding stack to 200+ models *(as of 2026-04-23)*
- [Hermes Agent](../tools/hermes-agent.md) — NousResearch; open-source; brain+muscle architecture (separate reasoning and execution layers); Kanban supervision dashboard; weekly automated skill pruning; local-first memory; 118 bundled skills *(as of 2026-05-13)*
- [LangChain / LangSmith](../tools/langchain-langsmith.md) — LangChain; open-source agent framework and observability platform; LangSmith Engine closes the trace→improvement loop automatically; SmithDB is a purpose-built agent-trace database *(as of 2026-05-15)*
- [eve](../tools/eve.md) — Vercel; prescriptive agent framework built around model/provider switching, fallbacks, resumability, filesystem agents, skills, compaction, subagents, sandboxes, long-running jobs, observability, and evals *(as of 2026-07-03)*
- [OpenWiki](../tools/openwiki.md) — LangChain; codebase documentation layer for agents, part of the broader move toward maintained, agent-readable context surfaces *(as of 2026-07-02)*
- [OpenAI Agents SDK](../tools/openai-agents-sdk.md) — model-native harness with native sandbox execution, durable checkpoint / rehydration, and provider-neutral manifests *(as of 2026-04-15)*
- **OpenClaw** — viral open-source framework (345K stars); deep messaging-app integrations; **security advisory (May 2026):** 341 malicious registry entries planted in coordinated attack; Microsoft recommends enterprise customers avoid on work machines *(as of 2026-05-13)*
```

`### Agent orchestration` section — add Devin Auto-Triage:

> After the existing `Advisor strategy` line, add:
> `- [Devin Auto-Triage](../tools/devin.md) — Cognition; always-on persistent agent that monitors Slack channels and investigates bugs as reported; parent Devin filters noise and dispatches focused sub-sessions; shared long-term memory for deduplication across repeat reports; early users (Modal) describe it as more useful than homegrown triage automations *(as of 2026-05-19)*`

`### Persistent coding agents` section and its three bullets (Hermes Agent, OpenClaw, Devin Auto-Triage) — **removed entirely**, folded into the two sections above.

`### Agent sandbox / compute infrastructure` section — add E2B:

> **Before (last line):** `- [Railway](../tools/railway.md) — bare-metal deployment platform with copy-on-write production forks, progressive rollouts, and a CLI-first agent interface *(as of 2026-05-20)*`
> **After:** unchanged, followed by:
> `- [E2B](../tools/e2b.md) — isolated sandbox runtime for AI agents; disposable Linux VMs exposed as a programmable execution layer via SDK; command execution, SSH/terminal access, persistence/snapshots, BYOC deployment *(as of 2026-04-24)*`

### wiki/trends/llm-as-discovery-channel.md (updated)

Frontmatter change:

```yaml
domains: [models]
```

### wiki/history/tools/claude-code.md (updated)

Remove the frontmatter block entirely (matches the no-frontmatter convention used by `wiki/history/tools/codex.md` and `wiki/history/state-of/coding.md`):

> **Before:**
> ```
> ---
> title: Claude Code History
> type: history
> as_of: 2026-05-13
> ---
>
> # Claude Code History
> ```
> **After:**
> ```
> # Claude Code History
> ```
> Everything below the heading (the archived entries) is unchanged.

### wiki/sources/tweets/claude-code-monitor.md (new — moved from wiki/sources/articles/claude-code-monitor.md)

```md
---
title: Claude Code Monitor tool announcement
type: source
source_type: tweet
source_file: raw/articles/2026-04-10-xcom-noahzweben-status-2042332268450963774.md
url: https://x.com/noahzweben/status/2042332268450963774
published: 2026-04-10
ingested: 2026-04-10
domains: [coding, agents]
---

# Claude Code Monitor tool announcement

Noah Zweben (Anthropic) announces the Monitor tool for Claude Code: background scripts that wake the agent on events instead of polling. Saves tokens and supports log following, PR polling, and similar use cases.

## Influenced pages

- [Claude Code](../../tools/claude-code.md) — new page created
- [Coding](../../state-of/coding.md) — added terminal-coding-agent subcategory

## Key claims extracted

- Monitor tool lets Claude create background scripts that wake the agent when needed
- Replaces polling in the agent loop — big token saver
- Can follow logs for errors, poll PRs via script, and more
```

### wiki/sources/articles/claude-code-monitor.md — deleted (moved above)

### wiki/sources/tweets/cursor-pr-demos.md (new — moved from wiki/sources/articles/cursor-pr-demos.md)

```md
---
title: Cursor ships PR demo attachments
type: source
source_type: tweet
source_file: raw/tweets/2026-04-10-cursor_ai-2042287192895267212.md
url: https://x.com/cursor_ai/status/2042287192895267212
published: 2026-04-10
ingested: 2026-04-10
domains: [coding]
---

# Cursor ships PR demo attachments

Cursor can now attach demos and screenshots of cloud agent work to the GitHub PRs it opens, letting teams review AI-generated artifacts directly in GitHub.

## Influenced pages

- [Cursor](../../tools/cursor.md) — new recent change, status update

## Key claims extracted

- Cloud agents auto-attach demo videos and screenshots to PRs
- Teams can review AI-generated code changes visually in GitHub
```

### wiki/sources/articles/cursor-pr-demos.md — deleted (moved above)

### wiki/sources/tweets/langchain-better-harness.md (new — moved from wiki/sources/articles/langchain-better-harness.md)

```md
---
title: '"Better Harness: A Recipe for Harness Hill-Climbing with Evals" — LangChain'
type: source
source_type: tweet
source_file: raw/tweets/2026-04-10-vtrivedy10-2041927488918413589.md
url: https://x.com/Vtrivedy10/status/2041927488918413589
published: 2026-04-10
ingested: 2026-04-10
domains: [agents]
---

# Better Harness: A Recipe for Harness Hill-Climbing with Evals

LangChain shares Better-Harness, an open-source prototype for autonomously improving agent harnesses using evals as a hill-climbing signal. Sources evals from hand-curation, production traces, and external datasets; uses optimization/holdout splits to guard against overfitting; iteratively diagnoses failures and proposes scoped harness changes.

## Influenced pages

- [Agent improvement loop](../../concepts/agent-improvement-loop.md) — added Better-Harness section as concrete implementation

## Key claims extracted

- `harness + evals + harness engineering → better agent` (analogous to model training)
- Eval sources: hand-curated, production traces, external datasets
- Optimization/holdout split per behavioral category prevents overfitting
- One scoped change per iteration (may include prompt + tool together)
- Tested with Claude Sonnet 4.6 and GLM-5; near-full generalization to holdout
- Common changes: prompt/instruction updates, tool description edits, new tool additions
- Human review remains a gate — catches overfit instructions and token waste
- Open-sourced as a prototype for builders
```

### wiki/sources/articles/langchain-better-harness.md — deleted (moved above)

### wiki/concepts/agent-improvement-loop.md (updated)

Line 145 link target only:

> **Before:** `["Better Harness: A Recipe for Harness Hill-Climbing with Evals" — LangChain](../sources/articles/langchain-better-harness.md)`
> **After:** `["Better Harness: A Recipe for Harness Hill-Climbing with Evals" — LangChain](../sources/tweets/langchain-better-harness.md)`

### wiki/concepts/harness.md (updated)

Four link targets only (lines 14, 77, 112, 136), same substitution — `../sources/articles/langchain-better-harness.md` → `../sources/tweets/langchain-better-harness.md` in each of:

> `[LangChain's Better-Harness](../sources/tweets/langchain-better-harness.md)` (line 14)
> `[Better-Harness](../sources/tweets/langchain-better-harness.md)` (line 77)
> `[LangChain's Better-Harness](../sources/tweets/langchain-better-harness.md)` (line 112)
> `["Better Harness: A Recipe for Harness Hill-Climbing with Evals" — LangChain](../sources/tweets/langchain-better-harness.md)` (line 136, `## Sources`)

### wiki/sources/tweets/openai-pro-100.md (new — moved from wiki/sources/articles/openai-pro-100.md)

```md
---
title: OpenAI launches $100/mo Pro plan
type: source
source_type: tweet
source_file: raw/tweets/2026-04-10-openai-2042295688323875316.md
url: https://x.com/OpenAI/status/2042295688323875316
published: 2026-04-10
ingested: 2026-04-10
domains: [coding]
---

# OpenAI launches $100/mo Pro plan

OpenAI introduces a $100/month Pro tier for ChatGPT/Codex users who outgrow the $20 Plus plan. Includes 5× Codex usage, exclusive Pro model, unlimited Instant and Thinking models. Launch promo: up to 10× Plus-level Codex usage through May 31, 2026.

## Influenced pages

- [Coding](../../state-of/coding.md) — recent change entry about pricing tier
- [Codex](../../tools/codex.md) — new stub page with pricing

## Key claims extracted

- New $100/month Pro tier (between Plus at $20 and previous $200 Pro)
- 5× more Codex usage than Plus
- Exclusive Pro model access
- Unlimited Instant and Thinking models
- Launch promo: up to 10× Plus usage on Codex through 2026-05-31
```

### wiki/sources/articles/openai-pro-100.md — deleted (moved above)

### wiki/tools/codex.md (updated)

Two changes on this page: the domain addition (this item) and the link-target fix above.

Frontmatter change:

```yaml
domains: [coding, agents, cybersecurity, computer-use]
```

Line 108 link target:

> **Before:** `[OpenAI launches $100/mo Pro plan](../sources/articles/openai-pro-100.md)`
> **After:** `[OpenAI launches $100/mo Pro plan](../sources/tweets/openai-pro-100.md)`

### wiki/sources/newsletters/perplexity-computer-plaid.md (new — moved from wiki/sources/articles/perplexity-computer-plaid.md)

```md
---
title: Perplexity Computer — Plaid financial integrations
type: source
source_type: newsletter
source_file: raw/newsletters/2026-04-10-superhumanai-p-agents-for-your-personal-life-are-here.md
url: https://www.superhuman.ai/p/agents-for-your-personal-life-are-here
published: 2026-04-10
ingested: 2026-04-10
domains: [computer-use, finance]
---

# Perplexity Computer — Plaid financial integrations

Perplexity's Computer feature now connects with 12,000+ financial institutions through Plaid, letting users link all accounts into a single customizable hub. Users can ask questions about their finances and build custom tools for budgeting, spending, or tracking debt/investments. The announcement reportedly attracted 2M+ views.

## Influenced pages

- [Perplexity Computer](../../tools/perplexity-computer.md) — new page created (enriched with web research)
- [State of Computer Use](../../state-of/computer-use.md) — new state-of page created
- [State of Finance](../../state-of/finance.md) — new state-of page seeded

## Key claims extracted

- Computer connects to 12,000+ financial institutions through Plaid
- Users can link accounts, query finances, build custom budgeting/tracking tools
- Announcement had 2M+ views
```

### wiki/sources/articles/perplexity-computer-plaid.md — deleted (moved above)

### wiki/tools/perplexity-computer.md (updated)

Line 56 link target only:

> **Before:** `[Perplexity Computer — Plaid financial integrations](../sources/articles/perplexity-computer-plaid.md)`
> **After:** `[Perplexity Computer — Plaid financial integrations](../sources/newsletters/perplexity-computer-plaid.md)`

### wiki/tools/devin.md (updated — second edit on this page, alongside the `cognition` tag above)

Frontmatter `domains:` change:

```yaml
domains: [coding, agents, cybersecurity]
```

### wiki/tools/gpt-realtime-2.md (updated)

Frontmatter `domains:` change:

```yaml
domains: [voice, models]
```

### wiki/state-of/creative.md (updated)

`### Visual design & prototyping` section — add Impeccable after the existing Figma Agent line:

```md
- [Impeccable](../tools/impeccable.md) — open-source design-agent skill system; encodes domain vocabulary, exact levels of control, and reusable evaluation language so agents make design decisions more reliably rather than one-shot prompting *(as of 2026-07-02)*
```

`### AI image generation` section — add Nano Banana 2 after the existing Muse Image line:

```md
- [Nano Banana 2](../models/nano-banana-2.md) — Google; uses Gemini's world understanding plus real-time web search imagery to generate images reflecting current real-world conditions *(as of 2026-04-22)*
```

### wiki/state-of/finance.md (updated)

New section, added after `### Personal finance AI` and before `### Agent-native commerce and fraud`:

```md
### Document intelligence

AI products specialized for extracting, structuring, querying, or reasoning over documents, PDFs, forms, and tables — as distinct from general-purpose finance assistants.

- [Mistral Document AI](../tools/mistral-document-ai.md) — Mistral; document-intelligence product for extracting and structuring information from PDFs, forms, and enterprise document flows *(as of 2026-04-22)*
- [LandingAI Agentic Document Extraction](../tools/landingai-agentic-document-extraction.md) — LandingAI; agentic extraction for visually complex documents, emphasizing preserved structural context across tables, forms, and segmented layouts *(as of 2026-04-22)*
```

Frontmatter `sources:` — add the two ids already used by these pages if not already present:

```yaml
sources: [perplexity-computer-plaid, hebbia-homepage, legacy-ai-tools-roadmap-xlsx, stripe-agent-native-commerce-fraud-2026-04-29, finance-agent-workflows-2026-05-06, chatgpt-personal-finance-2026-05, thinking-machines-financial-expert-judgment-2026-07-02, superhuman-bridgewater-thinking-machines-2026-07-02, mistral-document-ai, landingai-agentic-document-extraction]
```

### wiki/state-of/healthcare.md (updated)

New section, added after `### Healthcare AI` and before `### Speech to text`:

```md
### Document intelligence

AI products specialized for extracting, structuring, querying, or reasoning over documents, PDFs, forms, and tables — as distinct from general clinical or patient-facing tools.

- [Mistral Document AI](../tools/mistral-document-ai.md) — Mistral; document-intelligence product for extracting and structuring information from PDFs, forms, and enterprise document flows *(as of 2026-04-22)*
```

Frontmatter `sources:` change:

```yaml
sources: [legacy-ai-tools-roadmap-xlsx, dragon-copilot-launch, hippocratic-ai-homepage, tempus-homepage, zocdoc-zo, open-evidence-homepage, konko-kora-homepage, elevenlabs-scribe, 2026-06-16-metalearn-mystery-fatigue-ai, midjourney-medical-scanner-2026-06, ai-healthcare-triage-doctronic-2026-05, mistral-document-ai]
```

### wiki/state-of/cybersecurity.md (updated)

`### AI security tooling` section — add OpenAI Privacy Filter after the existing Gray Swan bullet:

```md
- [OpenAI Privacy Filter](../models/openai-privacy-filter.md) — OpenAI; open-weight (Apache 2.0) PII detection and redaction model, 1.5B total / 50M active MoE; intended to run on-device or on low-cost infrastructure to redact sensitive data before it reaches cloud AI systems *(as of 2026-04-23)*
```

## Schema / vocabulary additions

- [ ] Add new tag `cognition` to `wiki/_schema/tags.md` — vendor/org: Cognition (Devin, Windsurf, FrontierCode)

## Open questions

- **Dashboard inclusion policy.** AGENTS.md says a tool belongs on a state-of page if its `domains:` includes that page's domain — no carve-outs. In practice, `state-of/agents.md` has already opted out of this for coding-adjacent tools via its own scoping sentence ("only includes coding-adjacent systems when they are also relevant as agent orchestration, framework, or deployment surfaces"), and most of the ~66 domain⇔dashboard mismatches the maintenance pass found are exactly the kind of case that sentence excludes: frontier models like GPT-5.5, DeepSeek V4, and Cohere Command A+ carrying the `agents` domain, or coding tools like Claude Code and Cursor, none of which are "orchestration, framework, or deployment surfaces" themselves. A second, related wrinkle: several dashboards (coding.md, agents.md) are structured entirely around tool-shaped subcategories, so even a policy of "everything in the domain" doesn't have an obvious slot for a bare frontier model — the fix there isn't "add a line," it's "decide whether frontier models get a section on tool dashboards at all." This proposal drafts only the ~10 cases where the target is a tool that fits an already-existing (or clearly schema-implied) dashboard section: Impeccable, Nano Banana 2, the two document-intelligence tools, and OpenAI Privacy Filter, plus the three reverse-direction domain additions where a tool is already on a dashboard and just needs its own frontmatter to catch up. Please pick one of:
  1. **Codify what `state-of/agents.md` already does** — amend AGENTS.md's rule to "a tool belongs on a dashboard if its domain matches and the tool is a first-class instance of one of that dashboard's declared subcategories" (this is close to what's already true everywhere except the ~56 remaining mismatches), and leave the model-vs-tool-dashboard cases as permanently out of scope rather than a backlog.
  2. **Take "everything in the domain" literally** — draft a follow-up (M5?) adding the remaining ~56 entries, which will require either inventing frontier-model sections on coding.md/agents.md or trimming `domains:` on pages where the tag was added loosely.
  3. **Something in between** — tell me the rule you actually want and I'll draft the follow-up against that.

  Until this is answered, the remaining ~56 lower-priority mismatches (mostly models on coding.md/agents.md, e.g. GPT-5.5, DeepSeek V4, Cohere Command A+, Claude Code, Cursor) are not drafted anywhere and stay as-is.

- **`llm-as-discovery-channel.md`'s domain.** No domain in `wiki/_schema/domains.md` is a clean fit for "LLMs as a commercial/shopping discovery channel" — it isn't specifically about agents, coding, or any of the vertical domains. I assigned `models` as the least-wrong fit (it's a behavior of foundation models generally, not a tool or vertical). If you'd rather propose a new domain (e.g. `commerce` or `marketing`) or leave this page domain-less by exception, say so instead.

- **`frontier` tag on `wiki/models/claude-fable-5.md`** is a similar case to the seven tags dropped above (redundant with the `frontier-model` subcategory) but wasn't in this proposal's original scope — flagging it here rather than silently expanding scope; can fold into this proposal or a follow-up.
