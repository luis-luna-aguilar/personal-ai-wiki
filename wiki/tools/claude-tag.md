---
title: Claude Tag
type: tool
domains: [agents, coding]
subcategory: agent-orchestration
tags: [anthropic, agentic]
as_of: 2026-06-24
sources: [claude-tag-slack-agent-2026-06]
---

# Claude Tag

Anthropic's Slack-native team agent product. Claude Tag lets teams tag Claude into Slack threads, where it can work in-channel as a named participant with selected access to channels, tools, data, and codebases.

## Current status (as of 2026-06-24)

- Beta for Claude Enterprise and Team plans.
- Claude appears in Slack as a named team participant rather than a separate chat app.
- Admins choose which channels, tools, data, and codebases Claude can access.
- Teams can delegate async thread work, summaries, follow-ups, and longer-running tasks while keeping the surrounding discussion visible to the channel.
- Anthropic messaging links Claude Tag to Claude Code and broader background-agent workflows, but the product surface is Slack-native and multiplayer.

## Positioning

Claude Tag should be tracked separately from [Claude Cowork](claude-cowork.md). Cowork is Anthropic's desktop / delegated computer-work product; Claude Tag is the shared Slack-channel agent surface. The distinction matters because the hard problems differ: Claude Tag depends on organizational identity, channel scoping, auditability, memory boundaries, prompt-injection exposure, and budget visibility inside team communication.

## Caveats

- Current evidence is launch and newsletter coverage; there are no independent reliability, security, or token-efficiency evals yet.
- The "65% of code / product PRs" internal claim appears in secondary coverage with denominator and wording ambiguity, so it should not be treated as a benchmark.

## Recent changes

- [2026-06-24] Claude Tag beta launched as a Slack-native Claude product for Enterprise and Team plans, making Anthropic's team-agent surface multiplayer and channel-embedded.

## Sources

- [Claude Tag Slack-native agent launch](../sources/newsletters/claude-tag-slack-agent-2026-06.md)
