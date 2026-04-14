---
type: proposal
source: raw/articles/2026-04-10-cursorcom-blog-bugbot-learning.md
status: pending
created: 2026-04-10
---

# Proposal: Cursor Bugbot learned rules

## Summary

Cursor says Bugbot now learns directly from production PR feedback instead of improving only through offline experiments. The strongest claims are concrete: resolution rate improved from 52% at Bugbot's July 2025 launch to **78.13%** across **50,310** public PRs, with learned rules generated from developer reactions, replies, and human reviewer comments; more than **110,000 repos** have enabled learning, producing **44,000+ learned rules**.

This is more than a routine feature bullet. It is a clear product example of the agent-improvement loop already represented elsewhere in the wiki: production traces and human feedback becoming structured instructions that shape future behavior.

## Intended changes

- [x] **Update** `wiki/tools/cursor.md` — add Bugbot learned-rules update and refresh `as_of`
  > See diff snippet below.

- [x] **Update** `wiki/concepts/agent-improvement-loop.md` — add Bugbot as a concrete product example of learning from live signals
  > See diff snippet below.

- [x] **Update** `wiki/state-of/coding.md` — refresh the Cursor line and add a recent-change note
  > See diff snippet below.

- [x] **Create** `wiki/sources/articles/cursor-bugbot-learning.md` — source summary page
  > See full draft below.

- [x] **Update** `wiki/index.md` — refresh the Cursor entry date
  > See diff snippet below.

## Page drafts

### wiki/sources/articles/cursor-bugbot-learning.md (new)

```markdown
---
title: Bugbot now self-improves with learned rules
type: source
source_type: article
source_file: raw/articles/2026-04-10-cursorcom-blog-bugbot-learning.md
url: https://cursor.com/blog/bugbot-learning
ingested: 2026-04-10
domains: [coding, agents]
---

# Bugbot now self-improves with learned rules

Cursor describes Bugbot's shift from purely offline improvement to a live learning loop based on production PR feedback. The core mechanism is simple: Bugbot turns reactions, replies, and human-reviewer comments from merged PRs into candidate rules, promotes rules that earn positive signal, and disables rules that consistently perform poorly.

## Influenced pages

- [[tools/cursor]] — adds a substantive Bugbot product update and refreshes current status
- [[concepts/agent-improvement-loop]] — adds a concrete example of a production system turning live feedback into structured agent improvements
- [[state-of/coding]] — refreshes Cursor's line with the Bugbot signal

## Key claims extracted

- Cursor says Bugbot's resolution rate improved from 52% at launch to 78.13%
- The comparison table in the source covers 50,310 public PRs for Bugbot
- Cursor compares Bugbot against Greptile, CodeRabbit, GitHub Copilot, Codex, and Gemini Code Assist in the same post
- Cursor says Bugbot previously improved only through offline experiments
- The new learning loop uses reactions to Bugbot comments, replies to Bugbot comments, and human reviewer comments
- Candidate rules are promoted or disabled based on future signal from incoming PRs
- Cursor says 110,000+ repos have enabled learning and generated 44,000+ learned rules

## Caveats

- The ranking and resolution-rate comparison are vendor-reported
- The source covers only public repositories and uses an LLM judge to determine whether comments were addressed
- The post is product-focused and does not publish full methodology details beyond the brief description captured here
```

### wiki/tools/cursor.md (updated snippet)

```markdown
---
title: Cursor
type: tool
domains: [coding, agents]
subcategory: agentic-coding-workspace
tags: [closed-source, agentic]
as_of: 2026-04-10
sources: [cursor-3-launch, cursor-pr-demos, cursor-bugbot-learning]
---

## Current status (as of 2026-04-10)

- **Cursor 3** is the current shipped version, announced in the "Meet the new Cursor" post on cursor.com/blog
- New top-level interface built from scratch (not the VS Code fork) and centered on agents
- Inherently multi-workspace: humans and agents work across multiple repos simultaneously
- Cloud agents auto-attach demo videos and screenshots to PRs for visual review *(as of 2026-04-10)*
- **Bugbot** now learns rules from production PR feedback; Cursor reports a 78.13% resolution rate across 50,310 public PRs and 44,000+ learned rules across 110,000+ repos *(as of 2026-04-10)*
- Backed by [[models/composer-2|Composer 2]], Cursor's own frontier coding model with high usage limits
- Plugin marketplace ("Cursor Marketplace") supports MCPs, skills, and subagents, with one-click install and private team marketplaces
- Legacy "Cursor IDE" mode still available — switch back at any time

## Recent changes

- [2026-04-10] Bugbot learned rules: production PR feedback now turns into active review rules; Cursor reports 78.13% resolution across 50,310 public PRs
- [2026-04-10] Cloud agents now auto-attach demo videos and screenshots to GitHub PRs
- [2026-04-02] Cursor 3 announced — rebuilt agent-first interface, multi-repo, local↔cloud handoff, Composer 2, plugin marketplace

## Sources

- [[sources/articles/cursor-3-launch]]
- [[sources/articles/cursor-pr-demos]]
- [[sources/articles/cursor-bugbot-learning]]
```

### wiki/concepts/agent-improvement-loop.md (updated snippet)

```markdown
---
as_of: 2026-04-10
sources: [trace-agent-improvement-loop, langchain-better-harness, cursor-bugbot-learning]
---

## Current status (as of 2026-04-10)

- LangChain frames tracing as the foundation for systematic agent improvement, not just debugging
- The loop spans both staging and production, with production traces treated as the most valuable source of real failures
- Online evals, offline evals, and human review are complementary layers
- The concept is broader than any one vendor, even though the source article is product-adjacent
- LangChain's Better-Harness (open-sourced 2026-04-10) automates the loop: sources evals, splits optimization/holdout sets, iteratively diagnoses failures from traces, and proposes targeted harness changes with overfitting guards
- Cursor's Bugbot provides a product example of the same pattern: reactions, replies, and reviewer comments become candidate rules that are promoted or disabled based on later production signal

## Product example: Bugbot learned rules

Cursor's Bugbot shows what the improvement loop looks like when shipped inside a user-facing product. Instead of relying only on offline experiments, Bugbot turns feedback from merged PRs into candidate rules, evaluates those rules on later PRs, activates rules that keep earning good signal, and disables rules that perform poorly. That is the same core loop in more operational form: production traces plus human feedback become structured changes to the harness.

## Recent changes

- [2026-04-10] Added Cursor Bugbot as a production example of live feedback turning into agent rules
- [2026-04-10] Added Better-Harness section — LangChain's autonomous harness hill-climbing system
- [2026-04-09] Page created from LangChain's conceptual guide "The Agent Improvement Loop Starts with a Trace"
```

### wiki/state-of/coding.md (updated snippet)

```markdown
---
as_of: 2026-04-10
sources: [sdd-3-tools-fowler, cursor-3-launch, stripe-cli, claude-code-monitor, openai-pro-100, cursor-pr-demos, shopify-ai-toolkit, cursor-bugbot-learning]
---

### Agentic coding workspace

- [[tools/cursor]] — Cursor 3 is a unified agent workspace with multi-repo, local↔cloud handoff, plugin marketplace, and Bugbot learned rules from production PR feedback; Cursor reports 78.13% resolution across 50,310 public PRs *(as of 2026-04-10)*

## Recent changes

- [2026-04-10] Cursor Bugbot learned rules: production PR feedback now turns into active review rules; Cursor reports 78.13% resolution across 50,310 public PRs
- [2026-04-10] Added `agent-toolkits` subcategory with [[tools/shopify-ai-toolkit]]
- [2026-04-10] Added `terminal-coding-agent` subcategory with [[tools/claude-code]] and [[tools/codex]]
- [2026-04-10] OpenAI launches $100/mo Pro tier — 5× Codex usage, exclusive Pro model, launch promo through 2026-05-31
- [2026-04-09] Added `agentic-devops` subcategory with [[tools/stripe-cli]] after ingesting the `projects.dev` launch page
```

### wiki/index.md (updated snippet)

```markdown
## Tools

- [[tools/cursor]] — Cursor 3 agentic coding workspace; multi-repo, local↔cloud agent handoff; Bugbot learned-rules loop for PR review *(as_of: 2026-04-10)*
```

## Schema / vocabulary additions

- None proposed.

## Open questions

- I kept this as a `Cursor` update, not a separate `Bugbot` tool page. That seems right given the current source, but if Bugbot accumulates more standalone sources later it may deserve its own page.
