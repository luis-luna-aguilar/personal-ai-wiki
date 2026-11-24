---
title: Microsoft Copilot
type: tool
domains: [agents]
subcategory: ai-assistant
tags: [microsoft, closed-source]
as_of: 2026-11-18
sources: [microsoft-copilot-agent-mode-office, microsoft-word-legal-agent, copilot-cowork-ga-june-2026, ainews-mai-build-june-2026, satya-nadella-no-priors-june-2026, every-copilot-seat-in-org-chart-2026-09-25, every-nadella-ignite-own-model-2026-11-18]
---

# Microsoft Copilot

Microsoft's assistant surface across Microsoft 365. Since September 2026 it is one Copilot app with three tabs: Home (chat plus Word, Excel and PowerPoint with shared context), Code (non-developers build and share small apps), and Autopilot (persistent, goal-driven agents that sit in the org chart). Its pitch is that the documents, conversations and permissions an enterprise agent needs already live in Microsoft 365.

## Current status (as of 2026-11-18)

- **Ignite (2026-11-17):** the full Office apps now run inside Copilot instead of Copilot sitting in an Office sidebar, and Copilot Workspaces lets people and their agents work from shared context; Nadella says former team leads become individual contributors who manage agents on token budgets (per Every's roundtable report)
- **One Copilot app (launched 2026-09-23):** replaces the separate consumer and work chat apps; features roll out in previews and the early-access program over the coming months
- **Autopilot** is now the user-facing persistent agent: it draws on the last 30 days of work, the org chart and the calendar, keeps private memories of preferences and corrections, works under a user-given name (e.g. "Dot (Ryan's Autopilot)") that colleagues can tag in Teams, and runs Routines such as daily briefings; shown "reporting" to its owner in the org chart; off by default, billed in usage credits. (Microsoft first announced Autopilot at Build in June as a hosted long-running agent runtime.)
- Office inside Copilot holds context across apps: Copilot knows which document and slide the user is on
- Agentic mode in Word, Excel, and PowerPoint has been GA and the default since April 2026; [Microsoft Word Legal Agent](microsoft-word-legal-agent.md) is a domain-specific example (contract review with playbook redlines, Frontier program)
- **Copilot Cowork GA (June 2026):** available to all Microsoft 365 users with model choice and usage-based billing; Microsoft claims 30-40% cheaper per prompt than Claude Cowork
- **MAI-Code-1-Flash** powers GitHub Copilot and VS Code since Build (June 2026); Microsoft may also explore hosted DeepSeek variants as cheaper backends
- Microsoft runs about 16,000 internal evals built from common workflows and pushes customers toward company-specific evals (see [Evals for workflow and task agents](../training/evals-for-agentic-work.md))

## Strengths

- Deep native integration into the most common enterprise productivity canvas
- Stronger agentic claim than generic chat-assistant marketing because the actions happen inside the document/workbook/presentation itself
- Fits a real control-and-review model instead of fully opaque automation

## Weaknesses / caveats

- Enterprise permissions cut both ways: in a hands-on test at launch, Copilot found both files for a Word-to-Excel table move but lacked permission to edit the workbook, and a Chat-to-Code handoff was blocked the same way; whether it works on day one depends on the customer's IT setup
- Nadella calls the AI agent "the new massive insider risk"; Autopilot's governance (own permissions, org-chart visibility) is Microsoft's answer, not yet proven at scale
- Always-on agents spend tokens around the clock; Microsoft says Autopilot has to "clear a higher bar" than on-demand tools to justify the cost

## Recent changes

- [2026-11-17] Ignite: full Office apps run inside Copilot; Copilot Workspaces for shared human-agent context; Microsoft also launched MAI Licensed Weights (see [Proprietary data becomes model moat](../trends/proprietary-data-becomes-model-moat.md))
- [2026-09-25] One Copilot app launched 2026-09-23 with Home, Code and Autopilot tabs; Autopilot agents are named, persistent, org-chart-visible and usage-billed; hands-on test hit permission blocks on cross-app tasks
- [2026-06-17] Copilot Cowork GA: available to all Microsoft 365 users; model choice, usage-based billing; Microsoft claims 30-40% cheaper per prompt than Claude Cowork; DeepSeek backend option reportedly under consideration
- [2026-06-03] Build 2026: MAI-Code-1-Flash in Copilot/VS Code; Microsoft Autopilot hosted agent runtime; Scout (always-on personal agent across M365)
- [2026-05-01] Microsoft Word Legal Agent added in Frontier: domain-specific contract-review and redlining agent inside Word with deterministic document-edit resolution
- [2026-04-22] Agentic mode in Word, Excel, and PowerPoint becomes generally available and the default experience

## Sources

- [Copilot's agentic capabilities in Word, Excel, and PowerPoint are generally available](../sources/articles/microsoft-copilot-agent-mode-office.md)
- [Word: Legal Agent in Frontier](../sources/articles/microsoft-word-legal-agent.md)
- [Microsoft Copilot Cowork generally available (June 2026)](../sources/newsletters/copilot-cowork-ga-june-2026.md)
- [AINews — Microsoft Build 2026, MAI-Thinking-1 and MAI family (June 3)](../sources/newsletters/ainews-mai-build-june-2026.md)
- [Satya Nadella on No Priors x Latent Space (June 3)](../sources/newsletters/satya-nadella-no-priors-june-2026.md)
- [Every — Copilot Gets a Seat in the Org Chart](../sources/newsletters/every-copilot-seat-in-org-chart-2026-09-25.md)
- [Every — Microsoft's CEO Wants Every Company to Own Its Own Model](../sources/newsletters/every-nadella-ignite-own-model-2026-11-18.md)
