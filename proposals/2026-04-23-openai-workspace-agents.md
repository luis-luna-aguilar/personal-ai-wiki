---
type: proposal
sources:
  - raw/newsletters/2026-04-23-openai-drops-a-privacy-focused-model.md
  - raw/newsletters/2026-04-23-anthropics-unreleased-model-got-hacked.md
  - raw/newsletters/2026-04-23-ainews-tasteful-tokenmaxxing.md
status: pending
created: 2026-04-23
---

# Proposal: OpenAI Workspace Agents

## Summary
OpenAI launched Workspace Agents — Codex-powered, shareable team agents that run in Slack and ChatGPT, with scheduled and background execution. Free through May 6 for Business, Enterprise, Edu, and Teachers plans. Represents platform-level team-agent infrastructure, directly competitive with Claude Cowork and Google's Gemini Enterprise Agent Platform.

## Intended changes

- [x] **Update** `wiki/tools/codex.md` — add Workspace Agents section; update Recent changes
- [x] **Update** `wiki/state-of/agents.md` — add OpenAI workspace agents to Agent orchestration UIs; prepend Recent changes entry
- [x] **Create** `wiki/sources/newsletters/superhuman-2026-04-23.md` — source summary (shared; covers workspace agents, tokenmaxxing, Privacy Filter)

## Page drafts

### wiki/tools/codex.md (update — diff only)

Add the following section after the existing `## Current status` section, before `## Pricing`:

> **Insert new section:**
> ```markdown
> ## Workspace Agents (as of 2026-04-23)
>
> Workspace Agents are shareable, Codex-powered agents available to Business, Enterprise, Edu, and Teachers plans. Free to use through 2026-05-06.
>
> - Teams describe a job in natural language and ChatGPT builds the agent
> - Agents are shareable with teammates and designed to be improved over time
> - Operate across Slack, email, documents, and code — not just single-turn chat
> - Support scheduled and background execution; not limited to synchronous sessions
> - 5 types of agents supported: (automation, research, drafting, coding, data analysis per launch post)
> ```

> **Add to `## Recent changes` (prepend):**
> `- [2026-04-23] Workspace Agents launched: shareable Codex-powered team agents for Slack/ChatGPT; scheduled/background execution; free through 2026-05-06 for Business/Enterprise/Edu/Teachers`

### wiki/state-of/agents.md (update — diff only)

> **Before** (Agent orchestration UIs section — first entry):
> `- [[tools/claude-design]] — Anthropic; research-preview artifact-generation surface for prototypes, slides, and one-pagers...`
>
> **After** (insert new OpenAI entry at the top of Agent orchestration UIs):
> ```markdown
> - [[tools/codex]] (Workspace Agents) — OpenAI; Codex-powered shareable team agents in Slack and ChatGPT; scheduled/background execution; shareable across teammates; Business/Enterprise/Edu *(as of 2026-04-23)*
> ```

> **Add to `## Recent changes` (prepend):**
> `- [2026-04-23] Added OpenAI Workspace Agents to Agent orchestration UIs; Codex-powered, Slack-integrated, background-capable team agents — parallel move to Google's Gemini Enterprise Agent Platform same day`

### wiki/sources/newsletters/superhuman-2026-04-23.md (new)

````md
---
title: Superhuman — Anthropic's unreleased model got hacked
type: source
source_type: newsletter
source_file: raw/newsletters/2026-04-23-anthropics-unreleased-model-got-hacked.md
url: https://www.superhuman.ai/p/chatgpt-gets-24-7-shareable-agents
published: 2026-04-23
ingested: 2026-04-23
domains: [models, agents]
---

# Superhuman — Anthropic's unreleased model got hacked

General-audience AI newsletter covering the April 22-23 window. Lead stories: OpenAI workspace agents, Claude Mythos unauthorized access report, SpaceX/Cursor $60B deal. Secondary coverage: tokenmaxxing debate (Jensen Huang, Reid Hoffman), OpenAI Privacy Filter, Claude interactive diagrams.

## Influenced pages

- [[tools/codex]] — workspace agents details
- [[models/claude-mythos-preview]] — unauthorized access report (third-party platform, Anthropic denies system compromise)
- [[training/company-wide-ai-enablement]] — tokenmaxxing debate (Jensen Huang, Reid Hoffman middle ground)
- [[models/openai-privacy-filter]] — Privacy Filter confirmation

## Key claims extracted

- OpenAI workspace agents: Codex-powered, shareable, background-capable, free through May 6
- Claude Mythos: unauthorized group accessed via third-party platform by guessing API endpoint from naming conventions; Anthropic says no internal system compromise
- SpaceX: right to acquire Cursor at $60B or pay $10B; "working closely" partnership
- Tokenmaxxing: Jensen Huang "deeply alarmed" if engineers not burning tokens; Reid Hoffman middle ground: track how, not how much
- Claude interactive charts/diagrams now available to paid Anthropic plans
````
