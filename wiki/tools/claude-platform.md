---
title: Claude Platform
type: tool
domains: [agents]
subcategory: agent-orchestration
tags: [anthropic, closed-source]
as_of: 2026-11-17
sources: [claude-code-fast-mode-default-2026-05, claude-managed-agents-updates-2026-05, ainews-poolside-nvidia-2026-08-21, claude-sonnet-5-5-launch, claude-haiku-5-5-launch-2026-10-19, claude-platform-linked-billing-2026-11-17]
---

# Claude Platform

Anthropic's developer platform: the Claude API, the Console where organizations manage workspaces, usage and billing, and the hosted services built on top of them, such as [Claude Managed Agents](claude-managed-agents.md). Models ship here under their API ids (for example `claude-sonnet-5-5`, `claude-haiku-5-5`) alongside AWS, Google Cloud and Microsoft Azure.

## Current status (as of 2026-11-17)

- **Linked billing (beta, 17 November 2026).** Third-party platforms bill Claude usage to the customer's own organization instead of taking an API key. An Owner, Admin or Billing user approves the link once, sets a monthly spend limit per platform (or a default), sees spend per platform in Console, draws down an existing commitment or pays as it goes, and can unlink at any time. 19 launch platforms, including Linear, Warp, Asana, Factory and Ramp; supporting platforms are listed on Claude Marketplace.
- **Usage visibility.** Platforms see each linked customer's requests, tokens and models in Console or through the Usage and Cost Analytics API (beta). Console also shows prompt-cache hit/miss diagnostics (May 2026).
- **API tools GA (August 2026):** computer use, browser tool, Skills API and Files API, plus an AG-UI adapter for Managed Agents.
- **Admin controls.** MCP tunnels for Managed Agents and the Messages API are managed from Console workspace settings.
- **Defaults and credits.** Sonnet 5.5 defaults to High effort on the Platform (Medium in Claude Code and the apps). Max and Team subscriptions get monthly Platform API credits: $100 (Max 5x), $200 (Max 20x), up to $500 pooled (Team).

## Weaknesses / caveats

- Linked-billing requests run in the platform's organization, so the customer's IP allowlists, encryption keys and data-retention settings do not apply to them.

## Recent changes

- [2026-11-17] Linked billing launched in beta: organization links with per-platform spend limits replace shared API keys.
- [2026-10-07] Monthly Platform API credits added for Max and Team subscriptions.
- [2026-08-21] Computer use, browser tool, Skills API and Files API reach GA.
- [2026-05-20] MCP tunnels managed from Console workspace settings.
- [2026-05-19] Console adds prompt-cache diagnostics.

## Related

- [Claude Managed Agents](claude-managed-agents.md) - hosted agent runtime on the Platform.
- [Cost-aware AI task routing](../training/cost-aware-ai-task-routing.md) - linked billing as an AI FinOps control.

## Sources

- [Linked billing on the Claude Platform](../sources/articles/claude-platform-linked-billing-2026-11-17.md)
- [AINews — Poolside reverse execuhire (Claude Platform GA)](../sources/newsletters/ainews-poolside-nvidia-2026-08-21.md)
- [Claude Haiku 5.5 launch](../sources/articles/claude-haiku-5-5-launch-2026-10-19.md)
- [Claude Sonnet 5.5 launch](../sources/articles/claude-sonnet-5-5-launch.md)
- [New in Claude Managed Agents: self-hosted sandboxes and MCP tunnels](../sources/articles/claude-managed-agents-updates-2026-05.md)
- [Claude Code Fast mode becomes default + spec-drift logging](../sources/newsletters/claude-code-fast-mode-default-2026-05.md)
