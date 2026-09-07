---
type: proposal
source: raw/newsletters/2026-08-03-the-best-ai-agent-builder-is-trapped-inside-micros.md
status: pending
created: 2026-09-07
---

# Proposal: Codex hits 10M users, Claude Code holds 63% share, and Microsoft's buried agent builder

## Summary

### The source

Every consultant Mike Taylor opens a 2026-08-03 piece on Microsoft Copilot Studio with a coding-tool adoption aside: in the nine months from May 2025 to February 2026, Claude Code became the most popular AI coding tool, reaching 63% of respondents in Pragmatic Engineer's developer survey, while Microsoft-owned GitHub Copilot lost the lead in the category it invented back in 2021 — a year and a half before ChatGPT-3 shipped. He also notes that Codex usage "shot up from 6 million to 10 million users in a week," which he attributes to the new GPT-5.6 Sol model plus lingering uncertainty over Anthropic's Fable access. The rest of the piece — mostly paywalled — argues that Microsoft's Copilot Studio, a separate no-code agent-builder product from the consumer Copilot app and from GitHub Copilot, is a genuinely capable tool for wiring data connectors into AI agents, buried behind a confusing multi-step provisioning flow spanning several different Microsoft admin portals and product names; Taylor counted more than 80 products carrying the "Copilot" name.

### What changes

The wiki's `state-of/coding.md` currently shows Codex at "an estimated 6-7M users" and doesn't carry a market-share figure for Claude Code.

- **State of Coding** updates the Codex line to reflect growth to roughly 10M users within a week of the GPT-5.6 Sol launch, and adds the 63%-share figure to the Claude Code line; gains one Recent-changes entry noting both figures plus a brief, clearly-caveated mention of the Copilot Studio account. Page date moves to 3 August.

### What to weigh

The Copilot Studio material is a single secondary account (Every, mostly paywalled) rather than a benchmark or vendor-disclosed figure, so it's kept to one caveated clause in Recent changes rather than a full leaderboard entry — it doesn't cleanly fit `state-of/coding.md`'s subcategory structure either, since Copilot Studio is a general no-code agent builder, not a coding-specific tool. The 6M→10M Codex figure and the 63% Claude Code figure are both attributed to named sources (an X post citation and the Pragmatic Engineer survey respectively) but neither is independently verified by this proposal beyond what the newsletter reports.

## Intended changes

- [x] **Approve all** — checking this box approves every item in `## Intended changes` and `## Schema / vocabulary additions` below; the individual boxes may stay empty.

- [ ] **Update** `wiki/state-of/coding.md` — update Codex and Claude Code subcategory lines, add one Recent-changes entry, bump `as_of` to 2026-08-03
    > See draft below

- [ ] **Create** `wiki/sources/newsletters/every-copilot-studio-microsoft-2026-08-03.md` — source summary

## Page drafts

### wiki/state-of/coding.md (updated)

Frontmatter changes:
```yaml
as_of: 2026-08-03
sources: [sdd-3-tools-fowler, cursor-3-launch, stripe-cli, claude-code-monitor, openai-pro-100, cursor-pr-demos, shopify-ai-toolkit, cursor-bugbot-learning, claude-code-routines, openai-codex-ongoing-tasks, orca-homepage, coding-agent-control-planes, claude-code-leak-architecture, cursor-3-orchestration-bet, skills-and-plugin-packaging-late-march, cursor-cloud-agents-march, claude-code-scheduled-tasks-march, codex-security-march, agentic-devops-deep-research, cursor-sdk-agent-runtime-2026-04-30, symphony-devin-terminal-orchestration-2026-04-28, end-of-finetuning-debate-2026-05-13, claude-code-goal-fastmode-fleetview-2026-05-13, claude-code-agent-view-2026-05-13, model-harness-fit-2026-05-13, agent-first-ide-convergence-may-2026, dynamic-workflows-claude-code, fable-ban-june-2026, spacex-cursor-june-2026, ainews-frontiercode-june-2026, ainews-not-much-happened-2026-07-02, every-sonnet-5-vibe-check-2026-07-02, the-code-devin-security-2026-07-02, every-tale-of-two-models-2026-07-05, claude-code-getting-started-with-loops-2026-06-30, claude-sonnet-5-official-2026-06-30, cursor-ios-mobile-app-2026-06, devinai-blog-windsurf-adaptive, devinai-blog-agentic-map-reduce, cognitioncom-blog-devin-fusion, every-copilot-studio-microsoft-2026-08-03]
```

`### Terminal coding agent` — replace the Claude Code and Codex lines:

Before:
```md
- [Claude Code](../tools/claude-code.md) — Anthropic; terminal-first agent expanding toward supervised multi-session workflows; now supports Sonnet 5 as a broadly available agentic default while Fable 5 remains the high-capability but fallback-routed tier, making model-routing resilience part of the coding-agent operating model *(as of 2026-07-02)*
- [Codex](../tools/codex.md) — OpenAI; folded into a new ChatGPT desktop "superapp" (Chat/Work/Codex modes) in July 2026, drawing power-user backlash but reaching an estimated 6-7M users; remote SSH GA; parallel subagents keep the main context clean on independent task parts *(as of 2026-07-14)*
```

After:
```md
- [Claude Code](../tools/claude-code.md) — Anthropic; terminal-first agent expanding toward supervised multi-session workflows; now supports Sonnet 5 as a broadly available agentic default while Fable 5 remains the high-capability but fallback-routed tier, making model-routing resilience part of the coding-agent operating model; most-used AI coding tool at 63% of respondents per Pragmatic Engineer's May 2025-Feb 2026 developer survey *(as of 2026-08-03)*
- [Codex](../tools/codex.md) — OpenAI; folded into a new ChatGPT desktop "superapp" (Chat/Work/Codex modes) in July 2026, drawing power-user backlash; usage reportedly grew from ~6-7M to an estimated 10M users within a week of the GPT-5.6 Sol launch; remote SSH GA; parallel subagents keep the main context clean on independent task parts *(as of 2026-08-03)*
```

`## Recent changes` — insert this entry at the top (newest first):
```md
- [2026-08-03] Codex usage reportedly grew from ~6-7M to ~10M users within a week of the GPT-5.6 Sol launch; Pragmatic Engineer's May 2025-Feb 2026 survey found Claude Code the most-used AI coding tool at 63% of respondents, with GitHub Copilot losing the category lead it held since inventing it in 2021; separately, an Every hands-on account described Microsoft's Copilot Studio (no-code agent builder, distinct from the consumer Copilot app and GitHub Copilot) as capable but confusingly onboarded — secondary account, mostly paywalled.
```
This brings the list to exactly 10 entries (the page's cap) — no spill needed yet; the next new entry will spill the current oldest (`[2026-06-17] SpaceX acquires Cursor...`) to `wiki/history/state-of/coding.md`.

### wiki/sources/newsletters/every-copilot-studio-microsoft-2026-08-03.md (new)

```md
---
title: "The Best AI Agent Builder Is Trapped Inside Microsoft"
type: source
source_type: newsletter
source_file: raw/newsletters/2026-08-03-the-best-ai-agent-builder-is-trapped-inside-micros.md
url: https://every.to/also-true-for-humans/the-best-ai-agent-builder-is-trapped-inside-microsoft
published: 2026-08-03
ingested: 2026-09-07
domains: [coding]
---

# The Best AI Agent Builder Is Trapped Inside Microsoft

Every's Mike Taylor argues Microsoft Copilot Studio — a no-code agent builder distinct from the consumer Copilot app and from GitHub Copilot, one of 80+ products carrying the "Copilot" name — is a genuinely capable tool for wiring enterprise data connectors into AI agents, but buried behind a confusing multi-portal purchase and provisioning flow. In passing, he cites two coding-tool adoption datapoints: Claude Code reached 63% of respondents in Pragmatic Engineer's May 2025-Feb 2026 developer survey, the most of any AI coding tool, with GitHub Copilot losing the lead in the category it invented in 2021; and Codex usage grew from roughly 6-7M to an estimated 10M users within a week, attributed to the GPT-5.6 Sol model launch and uncertainty over Anthropic's Fable access. Most of the piece, including the Copilot Studio interview and onboarding walkthrough, is paywalled.

## Influenced pages

- [State of Coding](../../state-of/coding.md) — Codex user-growth figure, Claude Code market-share figure, Copilot Studio caveated note

## Key claims extracted

- Claude Code: 63% of respondents in Pragmatic Engineer's May 2025-Feb 2026 survey, most-used AI coding tool
- GitHub Copilot (Microsoft) lost the category lead it held since inventing it in 2021
- Codex usage grew from ~6-7M to ~10M users within a week, attributed to GPT-5.6 Sol launch
- Microsoft Copilot Studio: no-code agent builder, distinct product from consumer Copilot app and GitHub Copilot; described as capable but confusingly onboarded (secondary, mostly-paywalled account)
```
