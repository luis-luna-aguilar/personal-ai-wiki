---
type: proposal
sources:
  - raw/newsletters/2026-06-24-ainews-claude-tag-multiplayer-proactive-persi.md
  - raw/newsletters/2026-06-24-anthropic-drops-claude-tag.md
  - raw/newsletters/2026-06-24-startup-launches-vibe-directing-platform.md
  - raw/newsletters/2026-06-25-ainews-its-meta-harness-summer.md
  - raw/tweets/2026-07-07-bcherny-2069474681749754272.md
status: pending
created: 2026-07-07
---

# Proposal: Claude Tag as Slack-native agent product

## Summary

Anthropic launched Claude Tag as a distinct beta product/surface for Claude Enterprise and Team users: Claude joins Slack as a named participant with access to selected channels, tools, data, and codebases. The key wiki update is that Anthropic now has a separate Slack-native organizational agent product, distinct from desktop Cowork and terminal Claude Code, aimed at async, multiplayer, permissioned work inside team coordination channels.

## Intended changes

- [x] **Create** `wiki/tools/claude-tag.md` — separate tool page for Anthropic's Slack-native team agent product.
    > Claude Tag should not be folded into Claude Cowork. Cowork remains the desktop / delegated computer-work product; Claude Tag is the Slack-native, multiplayer, channel-embedded product.

- [x] **Update** `wiki/state-of/agents.md` — add Claude Tag as a separate Agent orchestration entry.
    > Keep the Claude Cowork line focused on desktop/delegated-work workflows. Add a separate Claude Tag line for Slack-native multiplayer agent orchestration.

- [x] **Update** `wiki/concepts/harness.md` — add Slack/channel identity as part of the harness boundary.
    > Add pattern: org-embedded agents need explicit identity, channel scoping, permissions, memory boundaries, and auditability; otherwise the harness leaks into organizational confusion and prompt-injection/budget risk.

- [x] **Update** `wiki/index.md` — add the new `tools/claude-tag.md` entry under Tools.
    > See draft below.

- [x] **Create** `wiki/sources/newsletters/claude-tag-slack-agent-2026-06.md` — source summary.
    > See draft below.

## Page drafts

### wiki/tools/claude-tag.md (new)

```markdown
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
```

### wiki/state-of/agents.md (updated snippets)

```markdown
---
as_of: 2026-06-24
sources: [..., claude-tag-slack-agent-2026-06]
---

### Agent orchestration

- [Claude Cowork](../tools/claude-cowork.md) — Anthropic; desktop knowledge-work agent with Live Artifacts; now also the substrate for Claude for Small Business and Claude for Legal workflow bundles *(as of 2026-05-14)*
- [Claude Tag](../tools/claude-tag.md) — Anthropic; Slack-native multiplayer agent product where Claude joins selected channels as a named participant with chosen channel/tool/data/codebase access, async thread work, and in-channel team review *(as of 2026-06-24)*

## Recent changes

- [2026-06-24] Claude Tag beta makes Slack a multiplayer Anthropic agent surface: Claude can be tagged into threads with selected channel/tool/data/codebase access.
```

### wiki/concepts/harness.md (updated snippets)

```markdown
---
as_of: 2026-06-24
sources: [..., claude-tag-slack-agent-2026-06]
---

## What good harness engineering looks like

- **Org-embedded identity and permissioning.** Slack-native and team-channel agents need a legible identity, scoped access to channels/tools/data, audit trails for actions, and memory boundaries that match how the organization actually partitions work. Without that, the harness becomes an organizational risk surface: unclear accountability, prompt-injection exposure, budget opacity, and channel noise.

## Recent changes

- [2026-06-24] Claude Tag coverage adds org-embedded agent identity, permission scoping, and Slack-channel memory boundaries as harness concerns.
```

### wiki/index.md (updated snippet)

```markdown
## Tools

- [tools/claude-tag](tools/claude-tag.md) — Anthropic's Slack-native team agent product; Claude joins selected channels as a named participant with scoped channel/tool/data/codebase access and async thread work *(as_of: 2026-06-24)*
```

### wiki/sources/newsletters/claude-tag-slack-agent-2026-06.md (new)

```markdown
---
title: Claude Tag Slack-native agent launch
type: source
source_type: newsletter
source_file: raw/newsletters/2026-06-24-ainews-claude-tag-multiplayer-proactive-persi.md
url: https://www.anthropic.com/news/introducing-claude-tag
published: 2026-06-24
ingested: 2026-07-07
domains: [agents, coding]
---

# Claude Tag Slack-native agent launch

AINews and related newsletter coverage summarize Anthropic's Claude Tag beta: Claude can be tagged into Slack threads, work in-channel with selected workspace/tool/codebase access, and participate as a multiplayer async teammate rather than a one-user chat surface. The surrounding commentary frames the product as an org-level harness problem: identity, permissions, memory boundaries, budget visibility, and auditability matter as much as raw model capability.

## Influenced pages

- [Claude Tag](../../tools/claude-tag.md) — creates separate Slack-native team-agent product page.
- [State of Agents](../../state-of/agents.md) — updates Anthropic's agent orchestration position.
- [Wiki index](../../index.md) — adds Claude Tag under tools.
- [Harness](../../concepts/harness.md) — adds org-embedded identity and permissioning concerns.

## Key claims extracted

- Claude Tag is in beta for Claude Enterprise and Team plans.
- Claude appears in Slack as a named participant with access selected by administrators.
- The surface supports async thread work, summaries, follow-ups, and long-running delegated work.
- Commentary emphasizes identity, auditability, permission scoping, memory boundaries, budget opacity, and possible Slack noise as the core open questions.
- Anthropic messaging links Claude Tag to Claude Code and broader background-agent workflows.
```

## Schema / vocabulary additions

None.
