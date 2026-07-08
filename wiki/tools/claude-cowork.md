---
title: Claude Cowork
type: tool
domains: [agents]
subcategory: agent-orchestration
tags: [anthropic, agentic]
as_of: 2026-07-08
sources: [claude-cowork-launch, aakash-gupta-cowork, claude-design-launch, claude-productivity-surfaces, anthropic-desktop-agent-expansion-late-march, anthropic-persistent-workflow-surfaces-february, awsai-cowork-bedrock-2026-04-23, claude-cowork-mobile-2026-07]
---

# Claude Cowork

Anthropic's desktop agent for knowledge work. It works across local files, folders, and workplace applications to complete high-effort, repeatable tasks without the user coordinating each step. Included in Claude Pro ($20/month).

## Current status (as of 2026-07-08)

- Desktop-first agent that works across local files, folders, and everyday applications; now expanded into a cross-device Cowork beta on web and mobile for Max subscribers.
- Users can start delegated work at a desk, monitor it from a phone, and retrieve the final output from any device.
- Scheduled tasks can now run even when the user's computer is closed, strengthening Cowork's position as a background-agent surface rather than only a local desktop app.
- Anthropic extended Fable 5 access on paid plans through 2026-07-12 before moving it to usage credits, making Cowork's economics more usage-sensitive for frontier-model-backed work.
- Positioned for high-effort, repeatable knowledge-work tasks rather than one-off prompt-response use.
- Live Artifacts shipped in April 2026: dashboards, trackers, and reports wired to connectors that auto-refresh on open.

## Vertical workflow bundles (as of 2026-05-14)

Anthropic launched two prebuilt Cowork-based workflow bundles targeting end-users rather than developers:

- **Claude for Small Business** — 15 ready-to-run agentic workflows + 15 skills; integrations with QuickBooks, PayPal, DocuSign; automates payroll planning, invoice chasing, campaign launch, and similar repeatable tasks
- **Claude for Legal Professionals** — 12 one-click workflows for legal document and workflow automation

Both bundles are the clearest signal yet of Anthropic shifting from developer API tools toward direct end-user vertical automation products.

## AWS Bedrock deployment (as of 2026-04-23)

Claude Cowork is now available via Amazon Bedrock in public research preview. The main enterprise implication is deployment shape rather than new end-user behavior: organizations can run Cowork through their own AWS environment, with prompts, files, and model responses kept within the customer's AWS account.

## Why it matters

Cowork pushes agent UX beyond chat and toward delegated desktop work. Live Artifacts also puts competitive pressure on dashboard and internal-tool products by making connected reports and trackers much easier to create inside a general-purpose agent workflow. Alongside [Claude Design](claude-design.md), it also signals a broader Anthropic move toward artifact-first interfaces rather than chat-only interactions.

Cowork now reads less like a one-off desktop shell around Claude and more like Anthropic's bet on a general delegated-computer workflow. The same week introduced persistent sessions and then Channels, which suggests the real product is not "desktop app" versus "terminal app" but a continuous agent that can move between local computer, remote session, and mobile supervision.

Cowork also did not appear from nowhere. The earlier Claude for Word beta suggests Anthropic was already testing document-native, in-app productivity surfaces before the broader desktop knowledge-work push. That makes Cowork look more like expansion of a product direction than a sudden category jump.

## Recent changes

- [2026-07-08] Cowork beta expands to web/mobile for Max subscribers; scheduled tasks can run while the user's computer is closed; Fable 5 access extended through 2026-07-12.
- [2026-05-14] Claude for Small Business and Claude for Legal launched: 27 combined one-click agentic workflows on Cowork, with QuickBooks/PayPal/DocuSign integrations; first direct vertical automation product push
- [2026-04-23] AWS Bedrock public research preview: Cowork now available via Bedrock, keeping prompts, files, and model responses within the customer's AWS account
- [2026-02-25] Cowork added scheduled tasks, making recurring delegated work first-class before the later Dispatch / Channels / Live Artifacts expansion
- [2026-04-21] Added late-March framing: Cowork is positioned as a VM-backed, local-first delegated desktop workflow, not only an April artifact surface

## Sources

- [Claude Cowork — Anthropic product page](../sources/articles/claude-cowork-launch.md)
- [Aakash Gupta — Claude Cowork and dashboard-tool pressure](../sources/tweets/aakash-gupta-cowork.md)
- [Claude Design launch](../sources/tweets/claude-design-launch.md)
- [Claude productivity surfaces](../sources/tweets/claude-productivity-surfaces.md)
- [Anthropic desktop-agent expansion in late March](../sources/newsletters/anthropic-desktop-agent-expansion-late-march.md)
- [Anthropic persistent workflow surfaces in late February](../sources/newsletters/anthropic-persistent-workflow-surfaces-february.md)
- [AWS AI — Claude Cowork now available via Amazon Bedrock](../sources/tweets/awsai-cowork-bedrock-2026-04-23.md)
- [Claude Cowork web/mobile beta](../sources/newsletters/claude-cowork-mobile-2026-07.md)
