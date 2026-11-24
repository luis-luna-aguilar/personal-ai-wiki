---
title: Claude Tag
type: tool
domains: [agents, coding]
subcategory: agent-orchestration
tags: [anthropic, agentic]
as_of: 2026-10-10
sources: [claude-tag-slack-agent-2026-06, anthropic-human-agent-teams-2026-10, claude-cowork-is-now-claude-2026-09-16]
---

# Claude Tag

Anthropic's Slack-native team agent product. Claude Tag lets teams tag Claude into Slack threads, where it can work in-channel as a named participant with selected access to channels, tools, data, and codebases.

## Current status (as of 2026-10-10)

- Beta for Claude Enterprise and Team plans.
- Claude appears in Slack as a named team participant rather than a separate chat app.
- Admins choose which channels, tools, data, and codebases Claude can access.
- Teams can delegate async thread work, summaries, follow-ups, and longer-running tasks while keeping the surrounding discussion visible to the channel.
- Anthropic messaging links Claude Tag to Claude Code and broader background-agent workflows, but the product surface is Slack-native and multiplayer.
- Anthropic runs its own human-agent teams on it: agents with their own credentials, memory and roles defined in skill files share Slack threads with people, while private work goes to a direct message with @Claude or to Claude.ai and Cowork with personal MCP connectors. One internal engineering team reports agents handling 500 bug fixes independently after autonomy was widened per task type. Anthropic points to agent teams in Claude Code as the other way to build such agents. See [Multiplayer AI](../concepts/multiplayer-ai.md).

## Positioning

Claude Tag should be tracked separately from Cowork in the [Claude app](claude-app.md). Cowork, merged into the main Claude app since 2026-09-16, is Anthropic's single-user delegated-work capability; Claude Tag is the shared Slack-channel agent surface. The distinction matters because the hard problems differ: Claude Tag depends on organizational identity, channel scoping, auditability, memory boundaries, prompt-injection exposure, and budget visibility inside team communication.

## Caveats

- Current evidence is launch and newsletter coverage; there are no independent reliability, security, or token-efficiency evals yet.
- The "65% of code / product PRs" internal claim appears in secondary coverage with denominator and wording ambiguity, so it should not be treated as a benchmark.

## Recent changes

- [2026-10-10] Anthropic published how its own teams run human-agent teams on Claude Tag (public-by-default context, role rosters in skill files, per-task-type autonomy; 500 independent bug fixes on one team).
- [2026-06-24] Claude Tag beta launched as a Slack-native Claude product for Enterprise and Team plans, making Anthropic's team-agent surface multiplayer and channel-embedded.

## Sources

- [Claude Tag Slack-native agent launch](../sources/newsletters/claude-tag-slack-agent-2026-06.md)
- [Lessons from Anthropic on building effective human-agent teams](../sources/articles/anthropic-human-agent-teams-2026-10.md)
- [Claude Cowork and chat are now one Claude](../sources/articles/claude-cowork-is-now-claude-2026-09-16.md)
