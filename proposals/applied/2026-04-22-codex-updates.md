---
type: proposal
sources:
  - raw/tweets/2026-04-22-openaidevs-2033636701848174967.md
  - raw/tweets/2026-04-22-openaidevs-2039794643513295328.md
  - raw/tweets/2026-04-22-dkundel-2031148366890152296.md
status: pending
created: 2026-04-22
---

# Proposal: Codex updates — subagents, usage-based pricing, PR code review

## Summary

Three Codex updates that close feature gaps with Claude Code: subagents (parallel specialized agents with clean context windows), usage-based pricing for Business and Enterprise (removes fixed seat cost barrier), and PR code review accessible via any ChatGPT subscription.

## Intended changes

- [x] **Update** `wiki/tools/codex.md` — add subagents, usage-based pricing, PR code review
    > **Add to `## Current status`** after existing last bullet:
    > ```markdown
    > - **Subagents in Codex:** parallel specialized agents can now be spun up inside Codex to keep the main context window clean, tackle independent task parts in parallel, and be steered independently as work unfolds
    > - **Usage-based pricing** rolling out for ChatGPT Business and Enterprise plans — no fixed seat costs; teams pay for what they use; lowers the adoption barrier for organizations that want to test at scale before committing
    > - **PR code review via ChatGPT subscription:** connect GitHub, enable Codex code review, then trigger with "@codex review this" on any PR; available on Plus and above
    > ```
    >
    > **Update `as_of: 2026-04-22` in frontmatter.**
    > **Add to `## Recent changes`:**
    > ```
    > - [2026-04-22] Subagents now in Codex; usage-based pricing for Business/Enterprise; PR code review available via ChatGPT subscription
    > ```

- [x] **Create** `wiki/sources/tweets/codex-updates-april-2026.md` — source summary
    > See draft below

## Page drafts

### wiki/sources/tweets/codex-updates-april-2026.md (new)

```md
---
title: Codex updates — subagents, usage-based pricing, PR review
type: source
source_type: tweet
source_file: raw/tweets/2026-04-22-openaidevs-2033636701848174967.md
url: https://x.com/OpenAIDevs/status/2033636701848174967
published: 2026-04-22
ingested: 2026-04-22
domains: [coding]
---

# Codex updates — subagents, usage-based pricing, PR review

Three OpenAI Codex updates from April 2026. Subagents via OpenAI Devs tweet; usage-based pricing via OpenAI Devs tweet; PR code review via dominik kundel tweet.

## Influenced pages

- [[tools/codex]] — three new features added

## Key claims extracted

- Subagents: parallel specialized agents; clean context windows; independent steering
- Usage-based pricing: Business and Enterprise plans; no fixed seat costs
- PR code review: ChatGPT subscription required; connect GitHub; trigger with "@codex review this"; reviews all PRs, just yours, or explicit trigger
```
