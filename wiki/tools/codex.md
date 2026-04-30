---
title: Codex
type: tool
domains: [coding, cybersecurity]
subcategory: terminal-coding-agent
tags: [openai, closed-source, agentic]
as_of: 2026-04-24
sources: [openai-pro-100, ainews-2026-04-21, openai-codex-ongoing-tasks, coding-agents-review-and-orchestration-march, codex-security-march, codex-updates-april-2026, openai-gpt-5-5-launch, superhuman-2026-04-23, codex-broader-computer-work-2026-04-24]
---

# Codex

OpenAI's cloud-based agent surface, accessed via CLI and ChatGPT. It started as a coding agent, but current product direction is expanding into a broader computer-work system that can operate across code, browser flows, documents, spreadsheets, and repeatable knowledge-work tasks.

## Current status (as of 2026-04-24)

- Cloud coding agent accessible from ChatGPT and CLI
- OpenAI's March 2026 best-practices guide made the intended operating model unusually explicit: give Codex a clear goal/context/constraints/done-when structure, move durable repo guidance into `AGENTS.md`, connect live external systems with MCP, turn repeated work into skills, and automate workflows only after they are stable manually
- March 2026 also expanded Codex into security review: Codex Security is a research-preview application-security agent that builds repo context, finds vulnerabilities, validates them in sandboxes, and proposes fixes
- OpenAI now frames Codex as broader than code editing: it can use Mac apps, connect to more tools, create images, learn from prior actions, remember work preferences, and take on repeatable tasks
- Product direction increasingly overlaps with computer use and ongoing workflow automation, not just one-shot coding sessions
- **Subagents in Codex:** parallel specialized agents can now be spun up inside Codex to keep the main context window clean, tackle independent task parts in parallel, and be steered independently as work unfolds
- **Usage-based pricing** rolling out for ChatGPT Business and Enterprise plans — no fixed seat costs; teams pay for what they use; lowers the adoption barrier for organizations that want to test at scale before committing
- **PR code review via ChatGPT subscription:** connect GitHub, enable Codex code review, then trigger with "@codex review this" on any PR; available on Plus and above
- GPT-5.5 now powers Codex; OpenAI frames it as more capable while using fewer tokens than GPT-5.4 on the same Codex tasks
- Codex now has a 400K context window on GPT-5.5, and OpenAI describes a Fast mode that trades higher cost for higher speed
- OpenAI reports 85%+ of the company uses Codex weekly across software engineering, finance, communications, marketing, data science, and product work
- Secondary coverage is now converging on the same interpretation OpenAI hinted at earlier in the week: Codex is becoming a broader computer-work agent spanning browser flows, documents, spreadsheets, presentations, and repeatable knowledge-work tasks
- Every's Codex-for-knowledge-work positioning reinforces that the product is being taught and marketed for drafting, research, summarization, parallel task execution, and lightweight internal-tool building — not just code edits

## Workspace Agents (as of 2026-04-23)

Workspace Agents are shareable, Codex-powered team agents that run in Slack and ChatGPT for Business, Enterprise, Edu, and Teachers plans.

- Teams describe a job in natural language and ChatGPT builds the agent
- Agents are shareable with teammates and intended to improve over time
- The launch framing spans automation, research, drafting, coding, and data-analysis jobs
- Scheduled and background execution push Codex beyond one-off interactive sessions
- Launch promotion made the feature free through 2026-05-06 for the covered plan tiers

## Pricing (as of 2026-04-21)

- **Plus** ($20/mo) — baseline Codex usage included
- **Pro** ($100/mo, new) — 5× Codex usage over Plus, exclusive Pro model, unlimited Instant and Thinking models
- **Launch promo:** up to 10× Plus-level Codex usage for Pro subscribers through 2026-05-31

## Codex Chronicle (as of 2026-04-21)

Research preview. Background agents monitor recent screen activity, build memories from screenshots, and store them on-device. Users can inspect and edit stored memories.

- Rollout: Pro users on macOS only; excluding EU, UK, Switzerland
- Shift from explicit chat history to passive ambient context capture
- Competitive framing: Harrison Chase's "memory will be the great lock-in" argument points to accumulated ambient context as a switching cost, not just a convenience

## Recent changes

- [2026-04-24] Secondary coverage hardens the broader product thesis: Codex is being positioned as a computer-work agent for docs, sheets, browser tasks, and recurring knowledge-work workflows, not only software engineering
- [2026-04-23] Workspace Agents launched: shareable Codex-powered team agents for Slack and ChatGPT with scheduled/background execution; GPT-5.5 now powers Codex and OpenAI reports 85%+ internal weekly usage
- [2026-04-22] Subagents now in Codex; usage-based pricing for Business/Enterprise; PR code review available via ChatGPT subscription
- [2026-03-09] Codex Security launched in research preview, extending Codex into vulnerability review and validation workflows
- [2026-04-21] OpenAI reframes Codex around app use, memory/preferences, image creation, and repeatable tasks
- [2026-04-21] Codex Chronicle research preview — ambient screen memory; macOS Pro rollout
- [2026-03-11] Best-practices guide codified the AGENTS.md + MCP + skills + automation workflow as the default way to get better Codex results
- [2026-04-10] Page created from OpenAI Pro tier pricing announcement

## Sources

- [OpenAI launches $100/mo Pro plan](../sources/articles/openai-pro-100.md)
- [AINews — Moonshot Kimi K2.6, Hermes Agent, Codex Chronicle (2026-04-21)](../sources/newsletters/ainews-2026-04-21.md)
- [OpenAI — Codex for (almost) everything](../sources/tweets/openai-codex-ongoing-tasks.md)
- [Coding agents move toward review and concurrent supervision](../sources/newsletters/coding-agents-review-and-orchestration-march.md)
- [Codex Security](../sources/newsletters/codex-security-march.md)
- [Codex updates — subagents, usage-based pricing, PR review](../sources/tweets/codex-updates-april-2026.md)
- [Introducing GPT-5.5 — OpenAI](../sources/articles/openai-gpt-5-5-launch.md)
- [Superhuman — Anthropic's unreleased model got hacked](../sources/newsletters/superhuman-2026-04-23.md)
- [Codex broadens into computer work](../sources/newsletters/codex-broader-computer-work-2026-04-24.md)
