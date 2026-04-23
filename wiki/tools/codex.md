---
title: Codex
type: tool
domains: [coding]
subcategory: terminal-coding-agent
tags: [openai, closed-source, agentic]
as_of: 2026-04-22
sources: [openai-pro-100, ainews-2026-04-21, openai-codex-ongoing-tasks, coding-agents-review-and-orchestration-march, codex-security-march, codex-updates-april-2026]
---

# Codex

OpenAI's cloud-based coding agent, accessed via CLI and ChatGPT. Runs tasks asynchronously in a cloud sandbox.

## Current status (as of 2026-04-21)

- Cloud coding agent accessible from ChatGPT and CLI
- OpenAI's March 2026 best-practices guide made the intended operating model unusually explicit: give Codex a clear goal/context/constraints/done-when structure, move durable repo guidance into `AGENTS.md`, connect live external systems with MCP, turn repeated work into skills, and automate workflows only after they are stable manually
- March 2026 also expanded Codex into security review: Codex Security is a research-preview application-security agent that builds repo context, finds vulnerabilities, validates them in sandboxes, and proposes fixes
- OpenAI now frames Codex as broader than code editing: it can use Mac apps, connect to more tools, create images, learn from prior actions, remember work preferences, and take on repeatable tasks
- Product direction increasingly overlaps with computer use and ongoing workflow automation, not just one-shot coding sessions
- **Subagents in Codex:** parallel specialized agents can now be spun up inside Codex to keep the main context window clean, tackle independent task parts in parallel, and be steered independently as work unfolds
- **Usage-based pricing** rolling out for ChatGPT Business and Enterprise plans — no fixed seat costs; teams pay for what they use; lowers the adoption barrier for organizations that want to test at scale before committing
- **PR code review via ChatGPT subscription:** connect GitHub, enable Codex code review, then trigger with "@codex review this" on any PR; available on Plus and above

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

- [2026-04-22] Subagents now in Codex; usage-based pricing for Business/Enterprise; PR code review available via ChatGPT subscription
- [2026-03-09] Codex Security launched in research preview, extending Codex into vulnerability review and validation workflows
- [2026-04-21] OpenAI reframes Codex around app use, memory/preferences, image creation, and repeatable tasks
- [2026-04-21] Codex Chronicle research preview — ambient screen memory; macOS Pro rollout
- [2026-03-11] Best-practices guide codified the AGENTS.md + MCP + skills + automation workflow as the default way to get better Codex results
- [2026-04-10] Page created from OpenAI Pro tier pricing announcement

## Sources

- [[sources/articles/openai-pro-100]]
- [[sources/newsletters/ainews-2026-04-21]]
- [[sources/tweets/openai-codex-ongoing-tasks]]
- [[sources/newsletters/coding-agents-review-and-orchestration-march]]
- [[sources/newsletters/codex-security-march]]
- [[sources/tweets/codex-updates-april-2026]]
