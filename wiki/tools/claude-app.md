---
title: Claude app
type: tool
domains: [agents]
subcategory: agent-orchestration
tags: [anthropic, agentic]
as_of: 2026-11-12
sources: [claude-cowork-launch, aakash-gupta-cowork, claude-design-launch, claude-productivity-surfaces, anthropic-desktop-agent-expansion-late-march, anthropic-persistent-workflow-surfaces-february, awsai-cowork-bedrock-2026-04-23, claude-cowork-mobile-2026-07, claude-cowork-is-now-claude-2026-09-16, claudeai-cowork-chat-merge-2026-09-16, claude-for-manufacturing-2026-11-12]
---

# Claude app

Anthropic's unified Claude app, where chat and Cowork, its delegated knowledge-work agent, became one product on 2026-09-16. Cowork's capabilities are alive inside it: Claude works across local files, folders, and workplace applications to complete high-effort, repeatable tasks without the user coordinating each step, and handing over a long-running task (a report, a deck, a recurring job) works from any conversation. Included in Claude Pro ($20/month).

## Also called

Formerly Claude Cowork (a separate app until 2026-09-16); Anthropic still uses "Cowork" for the delegated-work capability.

## Current status (as of 2026-10-23)

- **One Claude.** Cowork and chat merged on 2026-09-16. Anthropic says users struggled to decide where a task belonged and lost context moving between surfaces; Claude now works out what a task needs and uses the context, skills, and connectors already in the conversation.
- **Rollout.** Pro and Max first, on web, desktop, and mobile, with nothing to turn on; Team and Free to follow. Generally available for Claude Enterprise since 2026-10-23.
- **Background work.** Tasks keep running after the laptop closes, progress can be checked from a phone, and a task can be scheduled to recur ("every Monday"). By default Claude asks before taking an action; users can let it keep working and check in only when something needs a closer look.
- **Docs, Slides, and Design in the conversation.** Claude Docs (co-written documents) and Claude Slides (Claude-drafted decks) launched with the merge, and [Claude Design](claude-design.md) now works inside conversations. Users edit directly, present from Claude, or download PowerPoint/PDF; each output lives at one shareable link. All three are in beta on paid plans, and Enterprise admins choose when to enable them.
- **Carry-over.** Existing Cowork chats, projects, artifacts, connectors, and skills stay where users left them.

## Cowork capabilities (as of 2026-07-08)

Cowork's state as a separate app; its capabilities carried into the Claude app:

- Desktop-first agent that works across local files, folders, and everyday applications; now expanded into a cross-device Cowork beta on web and mobile for Max subscribers.
- Users can start delegated work at a desk, monitor it from a phone, and retrieve the final output from any device.
- Scheduled tasks can now run even when the user's computer is closed, strengthening Cowork's position as a background-agent surface rather than only a local desktop app.
- Anthropic extended Fable 5 access on paid plans through 2026-07-12 before moving it to usage credits, making Cowork's economics more usage-sensitive for frontier-model-backed work.
- Positioned for high-effort, repeatable knowledge-work tasks rather than one-off prompt-response use.
- Live Artifacts shipped in April 2026: dashboards, trackers, and reports wired to connectors that auto-refresh on open.

## Vertical workflow bundles (as of 2026-11-12)

Anthropic packages prebuilt workflows, skills, and connectors for specific industries, aimed at end users rather than developers. The first two launched as Cowork-based bundles; Claude for Manufacturing is described as a Claude plugin for Team and Enterprise plans, without naming the surface it runs in.

- **Claude for Small Business** — 15 ready-to-run agentic workflows + 15 skills; integrations with QuickBooks, PayPal, DocuSign; automates payroll planning, invoice chasing, campaign launch, and similar repeatable tasks
- **Claude for Legal Professionals** — 12 one-click workflows for legal document and workflow automation
- **Claude for Manufacturing** (2026-11-12) — 17 skills for plant teams: quoting a new job, investigating a failed inspection, diagnosing a breakdown, sourcing from another supplier, comparing designs in Autodesk Fusion, and production reporting. Connectors to Autodesk Fusion, Infor, Microsoft 365, and Oracle NetSuite; systems without a connector are covered by saving regular exports to Microsoft 365. Every skill ends in a person's review, with figures linked back to source data. The Infor connector only reads; changes in Infor go through Infor's own plugin, after the user approves, within that user's Infor permissions. Does not operate equipment (Anthropic points to its [Model Hardware Standard](../concepts/model-hardware-standard.md) research preview for that). Setup: install on a Team or Enterprise plan and say "Set us up"; Claude asks which systems the team uses, tests the connectors, and reports which skills can't fully run yet.

Together the bundles are the clearest signal yet of Anthropic shifting from developer API tools toward direct end-user vertical automation products.

## AWS Bedrock deployment (as of 2026-04-23)

Claude Cowork is now available via Amazon Bedrock in public research preview. The main enterprise implication is deployment shape rather than new end-user behavior: organizations can run Cowork through their own AWS environment, with prompts, files, and model responses kept within the customer's AWS account.

## Why it matters

The merge turns Cowork from a destination into a capability of the main app: the user no longer picks "chat" or "agent", and outputs (docs, decks, designs) live next to the conversation that made them. It is the same direction as OpenAI's plan to fold ChatGPT Work into regular Chat (see [Codex](codex.md)).

Cowork pushes agent UX beyond chat and toward delegated desktop work. Live Artifacts also puts competitive pressure on dashboard and internal-tool products by making connected reports and trackers much easier to create inside a general-purpose agent workflow. Alongside [Claude Design](claude-design.md), it also signals a broader Anthropic move toward artifact-first interfaces rather than chat-only interactions.

Cowork now reads less like a one-off desktop shell around Claude and more like Anthropic's bet on a general delegated-computer workflow. The same week introduced persistent sessions and then Channels, which suggests the real product is not "desktop app" versus "terminal app" but a continuous agent that can move between local computer, remote session, and mobile supervision.

Cowork also did not appear from nowhere. The earlier Claude for Word beta suggests Anthropic was already testing document-native, in-app productivity surfaces before the broader desktop knowledge-work push. That makes Cowork look more like expansion of a product direction than a sudden category jump.

## Recent changes

- [2026-11-12] Claude for Manufacturing launched: 17-skill plugin for plant teams (quoting, failed-inspection investigation, breakdown diagnosis, sourcing, Fusion design comparison, production reporting) with Autodesk Fusion, Infor, Microsoft 365, and Oracle NetSuite connectors; every skill ends in human review; Infor writes via Infor's own plugin under the user's permissions; Team and Enterprise plans.
- [2026-10-23] Unified Claude (chat plus Cowork) generally available for Claude Enterprise.
- [2026-09-16] Cowork and chat merged into one Claude app (Pro/Max rollout over several weeks); Claude Docs and Claude Slides launched and Claude Design moved into conversations, all three in beta on paid plans; existing Cowork work carried over. Page renamed from Claude Cowork to Claude app on 2026-11-23.
- [2026-07-08] Cowork beta expands to web/mobile for Max subscribers; scheduled tasks can run while the user's computer is closed; Fable 5 access extended through 2026-07-12.
- [2026-05-14] Claude for Small Business and Claude for Legal launched: 27 combined one-click agentic workflows on Cowork, with QuickBooks/PayPal/DocuSign integrations; first direct vertical automation product push
- [2026-04-23] AWS Bedrock public research preview: Cowork now available via Bedrock, keeping prompts, files, and model responses within the customer's AWS account
- [2026-04-21] Added late-March framing: Cowork is positioned as a VM-backed, local-first delegated desktop workflow, not only an April artifact surface
- [2026-02-25] Cowork added scheduled tasks, making recurring delegated work first-class before the later Dispatch / Channels / Live Artifacts expansion

## Sources

- [Claude Cowork — Anthropic product page](../sources/articles/claude-cowork-launch.md)
- [Aakash Gupta — Claude Cowork and dashboard-tool pressure](../sources/tweets/aakash-gupta-cowork.md)
- [Claude Design launch](../sources/tweets/claude-design-launch.md)
- [Claude productivity surfaces](../sources/tweets/claude-productivity-surfaces.md)
- [Anthropic desktop-agent expansion in late March](../sources/newsletters/anthropic-desktop-agent-expansion-late-march.md)
- [Anthropic persistent workflow surfaces in late February](../sources/newsletters/anthropic-persistent-workflow-surfaces-february.md)
- [AWS AI — Claude Cowork now available via Amazon Bedrock](../sources/tweets/awsai-cowork-bedrock-2026-04-23.md)
- [Claude Cowork web/mobile beta](../sources/newsletters/claude-cowork-mobile-2026-07.md)
- [Claude Cowork and chat are now one Claude](../sources/articles/claude-cowork-is-now-claude-2026-09-16.md)
- [Claude (@claudeai) — Claude Cowork and chat are merging into one Claude](../sources/tweets/claudeai-cowork-chat-merge-2026-09-16.md)
- [Claude for Manufacturing: AI plugin for plant teams](../sources/articles/claude-for-manufacturing-2026-11-12.md)
