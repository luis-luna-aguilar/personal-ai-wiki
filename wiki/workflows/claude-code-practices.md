---
title: Claude Code practices
type: workflow
domains: [coding, agents]
subcategory: agentic-orchestration-patterns
tags: [anthropic, agentic]
as_of: 2026-05-18
sources: [anthropic-claude-code-best-practices-2026-05, claude-code-ultrareview]
---

# Claude Code practices

How to work with [Claude Code](../tools/claude-code.md) day to day: Anthropic's engineering best practices for context, verification, and the explore-plan-code loop, plus when to use `/ultrareview`, its cloud multi-agent review. Split out of the Claude Code tool page, which keeps the product's current state.

## Best practices (Anthropic engineering)

Anthropic's engineering guidance for getting reliable work out of Claude Code (May 2026).

**Context window management**
- Context window is the #1 resource; performance degrades as it fills; the custom status line tracks context usage for exactly this reason
- Start a new session when context is full rather than continuing in a degraded state

**Verification criteria**
- Always give Claude a way to verify its own work before reporting done: run the tests, take a screenshot, execute a command and check the output
- Without a verification criterion, Claude marks tasks complete based on code inspection alone — missing runtime failures

**Explore-plan-code workflow**
- Step 1 (Explore): Claude reads relevant files in plan mode — no edits permitted
- Step 2 (Plan): Claude writes a plan doc; press Ctrl+G to open it in a text editor for review and editing before any code is written
- Step 3 (Code): Claude implements against the approved plan; commits after each logical unit
- Skip plan mode for small or clearly-scoped tasks — overhead is only worth it for multi-file or uncertain-approach work

**UI verification**
- The Claude Chrome extension lets Claude take screenshots of the running app to verify visual output
- Closes the loop between a code change and the rendered result without requiring a human to look

## /ultrareview

Cloud multi-agent code review, introduced in v2.1.86 as a research preview. Unlike `/review` (single-pass, seconds, runs locally), ultrareview launches a fleet of reviewer agents in a remote sandbox that independently reproduces and verifies each finding before reporting it — so results focus on real bugs rather than style suggestions.

- Runs entirely in a remote cloud sandbox; terminal stays free while it runs
- Many reviewer agents explore the change in parallel, surfacing issues a single-pass review would miss
- Runs as a background task (~5-10 minutes); findings appear as a notification in your session
- Can review the diff between your current branch and the default branch (including uncommitted and staged changes), or a GitHub PR by number (`/ultrareview <PR-number>`)
- Requires authentication with a Claude.ai account — not available with API key only, and not available on Amazon Bedrock, Google Cloud Vertex AI, or Microsoft Foundry
- Not available to organizations with Zero Data Retention enabled

**Pricing:** billed as extra usage, typically $5–$20 per run depending on change size; enable it via `/extra-usage`. Pro and Max got 3 free runs through May 5, 2026; Team and Enterprise never had a free tier. Use `/tasks` to monitor or stop a running review.

Use `/review` for fast feedback while iterating. Use `/ultrareview` before merging a substantial change when you want a deeper pass with independent verification.

## Recent changes

- [2026-10-21] Page created, split out of [Claude Code](../tools/claude-code.md): the "Best practices (Anthropic engineering)" and "/ultrareview" sections.

## Related

- [Claude Code](../tools/claude-code.md) — the tool these practices apply to
- [Agent loop design](agent-loop-design.md) — loop taxonomy mapped onto Claude Code primitives

## Sources

- [Claude Code at scale — Anthropic engineering best practices](../sources/articles/anthropic-claude-code-best-practices-2026-05.md)
- [Find bugs with ultrareview](../sources/articles/claude-code-ultrareview.md)
