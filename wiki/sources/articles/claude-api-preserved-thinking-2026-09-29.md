---
title: 'Claude API docs — Preserved thinking (ClaudeDevs account-switching post)'
type: source
source_type: article
source_file: raw/articles/2026-09-29-tco-amq2qindpr.md
url: https://platform.claude.com/docs/en/build-with-claude/preserved-thinking
published: 2026-09-29
ingested: 2026-10-20
domains: [models, agents]
---

# Claude API docs — Preserved thinking

A ClaudeDevs post (2026-09-29) saying preserved thinking now extends to Sonnet 5.5 to curb distillation through account switching, plus the API docs page it links to. The docs were fetched on 2026-10-20 and already cover Haiku 5.5.

## Influenced pages
- [Claude Sonnet 5.5](../../models/claude-sonnet-5-5.md) — "Preserved thinking" section

## Key claims extracted
- Sonnet 5.5 and Haiku 5.5 thinking blocks work only in the producing account or a linked one; from another account they are dropped silently and the model regenerates its reasoning
- Prefix check on Fable 5.1, Opus 5.5, Sonnet 5.5 and Haiku 5.5: changing the system prompt, tools or earlier messages invalidates later thinking blocks
- Enforced by default (400 error) for accounts created on or after 2026-08-31; older accounts only when they set `prefix_mismatch_behavior`
- `drop_block` mode keeps requests running; dropping blocks every turn raised output tokens 4.6% at low effort and 67.1% at max in Anthropic's tests
- Claude Code, claude.ai, Managed Agents and the Agent SDK are unaffected; append-only integrations are safe
