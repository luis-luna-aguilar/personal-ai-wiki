---
title: Claude Cowork
type: tool
domains: [agents]
subcategory: agent-orchestration
tags: [anthropic, agentic]
as_of: 2026-04-23
sources: [claude-cowork-launch, aakash-gupta-cowork, claude-design-launch, claude-productivity-surfaces, anthropic-desktop-agent-expansion-late-march, anthropic-persistent-workflow-surfaces-february, awsai-cowork-bedrock-2026-04-23]
---

# Claude Cowork

Anthropic's desktop agent for knowledge work. It works across local files, folders, and workplace applications to complete high-effort, repeatable tasks without the user coordinating each step. Included in Claude Pro ($20/month).

## Current status (as of 2026-04-21)

- Desktop-first agent that works where most knowledge work happens: local files, folders, and everyday applications
- Scheduled tasks arrived in late February, letting Cowork run recurring briefs, spreadsheet updates, and similar automations on a cadence while the desktop app stayed open
- Late-March source material frames Cowork as a more user-friendly, VM-backed superset of Claude Code for non-terminal-native users rather than as a separate narrow productivity toy
- Anthropic explicitly tied Cowork to local-first agent workflows: the VM acts as both safety boundary and capability unlock, letting Claude install tools, run scripts, and operate more independently without the dead-end UX of approving every command
- Dispatch, introduced in March, made Cowork persistent: users could assign work from their phone and return later to a still-running desktop conversation
- Anthropic also tuned Cowork differently from Claude Code: longer planning horizons, heavier use of planning / clarification tools, and evaluation against messy knowledge-work tasks rather than only SWE tasks
- Positioned for high-effort, repeatable knowledge-work tasks rather than one-off prompt-response use
- No technical background required, according to Anthropic's product positioning
- Anthropic had already been pushing Claude into document-native productivity surfaces earlier in April via Claude for Word beta, which drafts, edits, and revises documents with tracked changes from a sidebar
- Live Artifacts shipped in April 2026: dashboards, trackers, and reports wired to connectors that auto-refresh on open
- Reported connectors include Slack, Salesforce, Google Drive, Asana, and Jira
- Released in the same product moment as [[tools/claude-design]], Anthropic's research-preview surface for prototypes, slides, and one-pagers

## AWS Bedrock deployment (as of 2026-04-23)

Claude Cowork is now available via Amazon Bedrock in public research preview. The main enterprise implication is deployment shape rather than new end-user behavior: organizations can run Cowork through their own AWS environment, with prompts, files, and model responses kept within the customer's AWS account.

## Why it matters

Cowork pushes agent UX beyond chat and toward delegated desktop work. Live Artifacts also puts competitive pressure on dashboard and internal-tool products by making connected reports and trackers much easier to create inside a general-purpose agent workflow. Alongside [[tools/claude-design]], it also signals a broader Anthropic move toward artifact-first interfaces rather than chat-only interactions.

Cowork now reads less like a one-off desktop shell around Claude and more like Anthropic's bet on a general delegated-computer workflow. The same week introduced persistent sessions and then Channels, which suggests the real product is not "desktop app" versus "terminal app" but a continuous agent that can move between local computer, remote session, and mobile supervision.

Cowork also did not appear from nowhere. The earlier Claude for Word beta suggests Anthropic was already testing document-native, in-app productivity surfaces before the broader desktop knowledge-work push. That makes Cowork look more like expansion of a product direction than a sudden category jump.

## Recent changes

- [2026-04-23] AWS Bedrock public research preview: Cowork now available via Bedrock, keeping prompts, files, and model responses within the customer's AWS account
- [2026-02-25] Cowork added scheduled tasks, making recurring delegated work first-class before the later Dispatch / Channels / Live Artifacts expansion
- [2026-04-21] Added late-March framing: Cowork is positioned as a VM-backed, local-first delegated desktop workflow, not only an April artifact surface
- [2026-04-21] Added earlier April precursor: Claude for Word beta signaled Anthropic's move into in-app document workflows before Cowork / Live Artifacts
- [2026-04-21] Live Artifacts shipped for connected dashboards, trackers, and reports

## Sources

- [[sources/articles/claude-cowork-launch]]
- [[sources/tweets/aakash-gupta-cowork]]
- [[sources/tweets/claude-design-launch]]
- [[sources/tweets/claude-productivity-surfaces]]
- [[sources/newsletters/anthropic-desktop-agent-expansion-late-march]]
- [[sources/newsletters/anthropic-persistent-workflow-surfaces-february]]
- [[sources/tweets/awsai-cowork-bedrock-2026-04-23]]
