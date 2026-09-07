---
type: proposal
source: raw/newsletters/2026-08-07-ainews-amd-buys-taalas.md
status: pending
created: 2026-09-07
---

# Proposal: OpenAI unifies ChatGPT around GPT-5.6 Sol, opens free tier to unlimited Luna, launches Agent Plugins

## Summary

### The source

AINews' August 7 issue ("AMD buys Taalas") carries a dense Twitter recap of an OpenAI product day. The headline move: OpenAI collapsed ChatGPT's separate "Instant" and "Thinking" chat modes into one. GPT-5.6 Sol now powers both for Plus/Pro users, with a new reasoning-effort slider letting people trade speed for depth instead of picking a different model. OpenAI says the updated Sol produces 68% fewer factual-error responses than GPT-5.5 Instant on a high-stakes eval spanning finance, medicine, and law. Free and Go-tier users get a matching upgrade: unlimited text chats with GPT-5.6 Luna, plus a "Think" button for harder questions — read widely as a major consumer-distribution move. ARC Prize independently re-ran GPT-5.6 Luna after its earlier 80% price cut and found capability unchanged at the new lower price: 59.6% on ARC-AGI-2 for $0.18/task and 90.7% on ARC-AGI-1 for $0.07/task.

The same product day also expanded OpenAI's developer surface. Agent Plugins is a new open, cross-client standard — built with AWS, Cursor, GitHub, and Vercel — for packaging Agent Skills and MCP server configs into one shared format, with day-one support across Codex, ChatGPT, Cursor, GitHub Copilot, Kiro, and VS Code. OpenAI also launched Codex Security Review in research preview, aimed at repo-context-aware security review directly on GitHub pull requests.

### What changes

The wiki currently has GPT-5.6 Sol's `as_of` at 2026-07-31 (pricing cuts, self-optimizing infrastructure) and MCP's `as_of` at 2026-06-29 (the stateless protocol RC, Stainless acquisition).

- **GPT-5.6 Sol** gains a new dated section covering the Instant/Thinking unification (reasoning-effort slider, 68% fewer factual errors vs. GPT-5.5 Instant) and the free-tier expansion to unlimited GPT-5.6 Luna with ARC Prize's independent post-price-cut re-test. A new Recent-changes entry is added; page date moves to 7 August.
- **Model Context Protocol** gains a new Current-status bullet and Recent-changes entry for Agent Plugins — the new open standard for packaging Agent Skills + MCP server configs across Codex/ChatGPT/Cursor/GitHub Copilot/Kiro/VS Code. Page date moves to 7 August.
- New source page for this AINews issue's OpenAI-product-day coverage.

### What to weigh

All claims here trace to a single secondary source (AINews' Twitter recap), not OpenAI's own announcement posts directly — the recap does link primary OpenAI tweets, but this proposal doesn't independently verify them. The "68% fewer factual errors" and ARC Prize figures are vendor/third-party claims repeated at one remove. Codex Security Review is noted only in passing (research preview, no further detail in this source) and isn't drafted as its own page — flagging in case a fuller source surfaces later.

## Intended changes

- [x] **Approve all** — checking this box approves every item in `## Intended changes` and `## Schema / vocabulary additions` below; the individual boxes may stay empty.

- [ ] **Update** `wiki/models/gpt-5-6-sol.md` — add ChatGPT unification section, Recent-changes entry, as_of → 2026-08-07, new source id
    > See draft below

- [ ] **Update** `wiki/concepts/mcp.md` — add Agent Plugins bullet, Recent-changes entry, as_of → 2026-08-07, new source id
    > See draft below

- [ ] **Create** `wiki/sources/newsletters/chatgpt-unification-agent-plugins-2026-08-07.md` — source summary

## Page drafts

### wiki/models/gpt-5-6-sol.md (updated)

Frontmatter changes:
```
as_of: 2026-08-07
sources: [metr-gpt-5-6-sol-eval-2026-06, gpt-5-6-sol-preview-launch-2026-06, chatgpt-voice-gpt56-launch-2026-07, ainews-gpt-56-launch-benchmarks-2026-07-10, every-gpt-56-vibe-check-2026-07-09, gpt-56-raising-concerns-2026-07-15, openais-new-model-for-cyber-attacks-2026-07-16, ainews-gpt-56-price-cut-2026-07-31, chatgpt-unification-agent-plugins-2026-08-07]
```

New section, inserted after `## Self-optimizing infrastructure (as of 2026-07-31)` and before `## METR predeployment evaluation`:
```md
## ChatGPT unification and free-tier expansion (as of 2026-08-07)

- OpenAI collapsed ChatGPT's separate "Instant" and "Thinking" chat modes into one: GPT-5.6 Sol now powers both for Plus/Pro users, with a reasoning-effort slider to choose speed vs. comprehensiveness instead of switching models.
- OpenAI says the updated Sol yields 68% fewer factual-error responses than GPT-5.5 Instant on a high-stakes eval spanning finance, medicine, and law.
- Free and Go-tier users get unlimited text chats with GPT-5.6 Luna plus a "Think" button for harder questions — widely read as a major consumer-distribution move.
- ARC Prize independently re-tested GPT-5.6 Luna after its earlier 80% price cut and found capability unchanged at the lower cost: 59.6% on ARC-AGI-2 for $0.18/task, 90.7% on ARC-AGI-1 for $0.07/task.
- These are OpenAI/third-party claims from a single secondary (AINews) recap, not independently verified here.
```

Recent-changes: insert as the newest entry (list is at 6/10, no spill needed):
```
- [2026-08-07] OpenAI unified ChatGPT's Instant/Thinking modes behind GPT-5.6 Sol with a reasoning-effort slider (68% fewer factual errors vs. GPT-5.5 Instant, per OpenAI); free/Go tiers got unlimited GPT-5.6 Luna chat, with ARC Prize confirming unchanged capability at the new lower price.
```

### wiki/concepts/mcp.md (updated)

Frontmatter changes:
```
as_of: 2026-08-07
sources: [anthropic-mcp, legacy-ai-tools-roadmap-xlsx, anthropic-mcp-deployment-surfaces, openai-chatgpt-mcp-surfaces, anthropic-mcp-production-systems, agent-ready-saas-mcp-2026-06, mcp-2026-07-28-stateless-rc, anthropic-acquires-stainless, google-io-agents-agents-agents, ainews-all-model-labs-are-now-agent-labs, chatgpt-unification-agent-plugins-2026-08-07]
```

New bullet, appended to `## Current status (as of 2026-06-29)` (heading text can stay as the section's original date label per existing convention on this page, or be updated to reflect the newest bullet — leave heading date as-is since other bullets remain dated to earlier sources):
```
- OpenAI introduced Agent Plugins (August 2026), an open cross-client standard built with AWS, Cursor, GitHub, and Vercel for packaging Agent Skills and MCP server configs into one shared format, with day-one support across Codex, ChatGPT, Cursor, GitHub Copilot, Kiro, and VS Code — another sign MCP-adjacent packaging is consolidating around shared tooling rather than per-vendor formats.
```

Recent-changes: insert as the newest entry (list is at 2/10, no spill needed):
```
- [2026-08-07] OpenAI launched Agent Plugins, an open cross-client standard for packaging Agent Skills and MCP server configs, with day-one support across Codex, ChatGPT, Cursor, GitHub Copilot, Kiro, and VS Code.
```

### wiki/sources/newsletters/chatgpt-unification-agent-plugins-2026-08-07.md (new)

```md
---
title: AINews — ChatGPT unifies on GPT-5.6 Sol, free tier gets unlimited Luna, Agent Plugins launches
type: source
source_type: newsletter
source_file: raw/newsletters/2026-08-07-ainews-amd-buys-taalas.md
url: https://www.latent.space/p/ainews-amd-buys-taalas
published: 2026-08-07
ingested: 2026-09-07
domains: [models]
---

# AINews — ChatGPT unifies on GPT-5.6 Sol, free tier gets unlimited Luna, Agent Plugins launches

AINews recap of an OpenAI product day: ChatGPT's Instant and Thinking modes merge into one GPT-5.6 Sol experience with a reasoning-effort slider (68% fewer factual errors vs. GPT-5.5 Instant per OpenAI); Free/Go tiers get unlimited GPT-5.6 Luna text chat plus a Think button, with ARC Prize confirming unchanged capability after Luna's 80% price cut (59.6% ARC-AGI-2 at $0.18/task, 90.7% ARC-AGI-1 at $0.07/task); OpenAI also launched Agent Plugins, an open cross-client standard (with AWS, Cursor, GitHub, Vercel) for packaging Agent Skills + MCP configs across Codex/ChatGPT/Cursor/GitHub Copilot/Kiro/VS Code, plus Codex Security Review in research preview for repo-context-aware PR security review. This same issue also covers Muse Spark 1.2's benchmark breakout and AMD's acquisition of Taalas, addressed in separate proposals.

## Influenced pages

- [models/gpt-5-6-sol](../../models/gpt-5-6-sol.md) — new ChatGPT-unification section, Recent-changes entry
- [concepts/mcp](../../concepts/mcp.md) — Agent Plugins bullet, Recent-changes entry

## Key claims extracted

- GPT-5.6 Sol now powers both ChatGPT Instant and Thinking modes for Plus/Pro, with a reasoning-effort slider
- 68% fewer factual-error responses vs. GPT-5.5 Instant on a finance/medicine/law high-stakes eval (OpenAI claim)
- Free/Go tiers get unlimited GPT-5.6 Luna text chat plus a Think button
- ARC Prize re-test of Luna post-price-cut: 59.6% ARC-AGI-2 at $0.18/task, 90.7% ARC-AGI-1 at $0.07/task
- Agent Plugins: open standard (with AWS, Cursor, GitHub, Vercel) packaging Agent Skills + MCP configs; live in Codex, ChatGPT, Cursor, GitHub Copilot, Kiro, VS Code
- Codex Security Review launched in research preview for GitHub PR security review
```

## Open questions

- Codex Security Review is mentioned only in passing in this source — worth a dedicated proposal later if a fuller announcement/source turns up, rather than a placeholder here.
