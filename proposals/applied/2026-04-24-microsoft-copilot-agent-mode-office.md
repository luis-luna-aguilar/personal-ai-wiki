---
type: proposal
sources:
  - raw/articles/2026-04-24-microsoftcom-en-us-microsoft-365-blog-2026-04-22-copilots-ag.md
  - raw/newsletters/2026-04-24-gpt-55-is-here.md
status: pending
created: 2026-04-24
---

# Proposal: Microsoft Copilot Agent Mode in Office Apps

## Summary

Microsoft's official post is substantive enough to justify first-pass wiki coverage. The key signal is not "Copilot got smarter," but that agentic behavior is now the default experience inside Word, Excel, and PowerPoint: Copilot takes multi-step native actions directly on documents, worksheets, and slides, with review/control preserved for the user. This looks like a real enterprise knowledge-work agent surface and complements, rather than duplicates, Foundry Hosted Agents.

## Intended changes

- [x] **Create** `wiki/tools/microsoft-copilot.md` — new tool page for Microsoft's cross-app AI assistant surface
- [x] **Update** `wiki/state-of/agents.md` — add Microsoft Copilot under `Agent orchestration`
- [x] **Update** `wiki/index.md` — add the new tool entry
- [x] **Create** `wiki/sources/articles/microsoft-copilot-agent-mode-office.md` — source summary

## Page drafts

### wiki/tools/microsoft-copilot.md (new)

````md
---
title: Microsoft Copilot
type: tool
domains: [agents]
subcategory: ai-assistant
tags: [microsoft, closed-source]
as_of: 2026-04-22
sources: [microsoft-copilot-agent-mode-office]
---

# Microsoft Copilot

Microsoft's cross-application assistant surface inside Microsoft 365. The April 2026 signal is that Copilot is no longer only a passive sidebar helper: in Word, Excel, and PowerPoint it is now explicitly agentic by default, taking multi-step native actions inside the application canvas while keeping review and control with the user.

## Current status (as of 2026-04-22)

- Agentic capabilities in Word, Excel, and PowerPoint are generally available and now the default experience
- Copilot can take multi-step, app-native actions directly in documents, worksheets, and presentations rather than only answer questions or suggest steps
- Microsoft emphasizes control: users review changes, keep what they want, and preserve structure/style preferences
- Work IQ is part of the grounding story, using Microsoft work signals to improve context and output quality
- Microsoft explicitly frames Copilot as multi-model and cross-app consistent, not tied to one single model/provider
- Current rollout spans Microsoft 365 Copilot, Microsoft 365 Premium, and also Personal / Family plans

## Strengths

- Deep native integration into the most common enterprise productivity canvas
- Stronger agentic claim than generic chat-assistant marketing because the actions happen inside the document/workbook/presentation itself
- Fits a real control-and-review model instead of fully opaque automation

## Weaknesses / caveats

- Current source is a Microsoft product post; independent operator evidence is still thin
- The page is intentionally narrow to the April 2026 Office-app signal, not a full history of all Copilot surfaces

## Recent changes

- [2026-04-22] Agentic mode in Word, Excel, and PowerPoint becomes generally available and the default experience

## Sources

- [[sources/articles/microsoft-copilot-agent-mode-office]]
````

### wiki/state-of/agents.md (update — diff only)

> **Add under `### Agent orchestration`:**
> ```markdown
> - [[tools/microsoft-copilot]] — Microsoft; agentic default mode inside Word, Excel, and PowerPoint; takes multi-step native actions in documents, worksheets, and presentations while users stay in control *(as of 2026-04-22)*
> ```
>
> **Add to `## Recent changes` (prepend):**
> `- [2026-04-22] Microsoft Copilot's agentic mode in Word, Excel, and PowerPoint reached GA/default status; Microsoft is now pushing agent behavior directly into Office's core work canvas, not only hosted runtimes like Foundry`

### wiki/index.md (update — diff only)

> **Add under `## Tools`:**
> ```markdown
> - [[tools/microsoft-copilot]] — Microsoft's assistant surface across Microsoft 365; now agentic by default in Word, Excel, and PowerPoint *(as_of: 2026-04-22)*
> ```

### wiki/sources/articles/microsoft-copilot-agent-mode-office.md (new)

````md
---
title: Copilot's agentic capabilities in Word, Excel, and PowerPoint are generally available
type: source
source_type: article
source_file: raw/articles/2026-04-24-microsoftcom-en-us-microsoft-365-blog-2026-04-22-copilots-ag.md
url: https://www.microsoft.com/en-us/microsoft-365/blog/2026/04/22/copilots-agentic-capabilities-in-word-excel-and-powerpoint-are-generally-available/
published: 2026-04-22
ingested: 2026-04-24
domains: [agents]
---

# Copilot's agentic capabilities in Word, Excel, and PowerPoint are generally available

Microsoft product post describing Copilot's shift from passive assistance to default in-app agentic action inside Word, Excel, and PowerPoint. The practical signal is that Microsoft's main office-work assistant is now framed as taking multi-step native actions directly on the work canvas.

## Influenced pages

- [[tools/microsoft-copilot]] — new page for the Office-app agentic surface
- [[state-of/agents]] — Microsoft gains a second meaningful agents entry beyond Foundry

## Key claims extracted

- Agentic capabilities in Word, Excel, and PowerPoint are generally available and default
- Copilot takes multi-step native actions directly in the application canvas
- User control and review remain central to the interaction model
- Work IQ provides grounding from Microsoft work signals
- Microsoft frames Copilot as a multi-model system rather than a single-model product
````
