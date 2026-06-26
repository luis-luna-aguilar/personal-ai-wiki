---
title: Microsoft Copilot
type: tool
domains: [agents]
subcategory: ai-assistant
tags: [microsoft, closed-source]
as_of: 2026-06-17
sources: [microsoft-copilot-agent-mode-office, microsoft-word-legal-agent, copilot-cowork-ga-june-2026]
---

# Microsoft Copilot

Microsoft's cross-application assistant surface inside Microsoft 365. The April 2026 signal is that Copilot is no longer only a passive sidebar helper: in Word, Excel, and PowerPoint it is now explicitly agentic by default, taking multi-step native actions inside the application canvas while keeping review and control with the user.

## Current status (as of 2026-06-17)

- Agentic capabilities in Word, Excel, and PowerPoint are generally available and now the default experience
- Copilot can take multi-step, app-native actions directly in documents, worksheets, and presentations rather than only answer questions or suggest steps
- Microsoft emphasizes control: users review changes, keep what they want, and preserve structure/style preferences
- Work IQ is part of the grounding story, using Microsoft work signals to improve context and output quality
- Microsoft explicitly frames Copilot as multi-model and cross-app consistent, not tied to one single model/provider
- Current rollout spans Microsoft 365 Copilot, Microsoft 365 Premium, and also Personal / Family plans
- [Microsoft Word Legal Agent](microsoft-word-legal-agent.md) is an example of domain-specific depth inside the Copilot surface: a contract-review agent in Word with playbook-based redlines, tracked-change output, and a deterministic document-edit resolution layer; available through the Frontier program for US Windows users
- **Copilot Cowork GA (June 2026):** generally available to any Microsoft 365 user globally; model choice, usage-based billing, cost management controls
- Microsoft claims Copilot Cowork runs 30-40% cheaper per prompt than Anthropic's Claude Cowork — primarily a pricing rather than capability differentiation
- Follow-up: Microsoft may explore Microsoft-hosted DeepSeek variants as cheaper optional backends; framed as sustainable pricing alternative to unlimited-use tiers

## Strengths

- Deep native integration into the most common enterprise productivity canvas
- Stronger agentic claim than generic chat-assistant marketing because the actions happen inside the document/workbook/presentation itself
- Fits a real control-and-review model instead of fully opaque automation

## Weaknesses / caveats

- Current source is a Microsoft product post; independent operator evidence is still thin
- The page is intentionally narrow to the April 2026 Office-app signal, not a full history of all Copilot surfaces

## Recent changes

- [2026-06-17] Copilot Cowork GA: available to all Microsoft 365 users; model choice, usage-based billing; Microsoft claims 30-40% cheaper per prompt than Claude Cowork; DeepSeek backend option reportedly under consideration
- [2026-05-01] Microsoft Word Legal Agent added in Frontier: domain-specific contract-review and redlining agent inside Word with deterministic document-edit resolution
- [2026-04-22] Agentic mode in Word, Excel, and PowerPoint becomes generally available and the default experience

## Sources

- [Copilot's agentic capabilities in Word, Excel, and PowerPoint are generally available](../sources/articles/microsoft-copilot-agent-mode-office.md)
- [Word: Legal Agent in Frontier](../sources/articles/microsoft-word-legal-agent.md)
- [Microsoft Copilot Cowork generally available (June 2026)](../sources/newsletters/copilot-cowork-ga-june-2026.md)
