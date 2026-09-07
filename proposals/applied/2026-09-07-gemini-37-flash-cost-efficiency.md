---
type: proposal
source: raw/newsletters/2026-08-20-ainews-death-of-params-zai-ceo-jie-tang-on-glm.md
status: pending
created: 2026-09-07
---

# Proposal: Gemini 3.7 Flash posts strong cost-adjusted reasoning numbers

## Summary

### The source
AINews's 2026-08-20 issue reports two new third-party benchmark results for Gemini 3.7 Flash: the ARC-AGI Prize measured it at 84.6% on ARC-AGI-2 at $0.25/task and 95.5% on ARC-AGI-1 at $0.12/task, and Artificial Analysis separately placed it #1 on its AA-AnalystAgent benchmark (spreadsheet/document-heavy quantitative tasks) at an average cost of $0.54 across 80 tasks.

### What changes
The wiki's Gemini tools page tracks the broader Gemini product surface but has no line yet on Gemini 3.7 Flash specifically or these cost-efficiency figures.

- **Gemini** gains one new Current-status bullet and a Recent-changes entry on Gemini 3.7 Flash's cost-adjusted benchmark results. Page date moves to 20 August.
- Its Recent-changes list is already over the 5-entry cap (7 live entries), so this proposal also spills the 3 oldest entries (23, 22, and 21 April) into a new 2026-09-07 archive block in `wiki/history/tools/gemini.md`.
- This raw file's source page is created by the companion Qwen3.8-27B proposal, whose draft already lists this page under its Influenced pages — no separate action needed here.

### What to weigh
Nothing beyond the sourcing noted above — both figures come from third-party benchmark providers (ARC-AGI Prize, Artificial Analysis) relayed through AINews, consistent with how the rest of this page's benchmark data is sourced.

## Intended changes

- [x] **Approve all**

- [ ] **Update** `wiki/tools/gemini.md` — new Current-status bullet, Recent-changes entry, spill of 3 oldest entries to history, as_of bump
    > See draft below

- [ ] **Update** `wiki/history/tools/gemini.md` — new 2026-09-07 archive block with the 3 spilled entries
    > See draft below

## Page drafts

### wiki/tools/gemini.md (updated)

```md
Frontmatter changes: as_of: 2026-08-20; sources: append ainews-death-of-params-glm-53-2026-08-20

## Current status (new bullet, appended)

**Gemini 3.7 Flash cost-efficiency (as of 2026-08-20):** ARC-AGI Prize reports 84.6% on ARC-AGI-2 at $0.25/task and 95.5% on ARC-AGI-1 at $0.12/task; Artificial Analysis separately places it #1 on its AA-AnalystAgent benchmark (spreadsheet/document-heavy quantitative tasks) at $0.54 average cost across 80 tasks — reinforcing its positioning as the "cheap and strong" option in its tier.

## Recent changes (new entry, prepended; existing list re-capped to 5)

- [2026-08-20] Gemini 3.7 Flash posts strong cost-adjusted benchmarks: 84.6% ARC-AGI-2 at $0.25/task, 95.5% ARC-AGI-1 at $0.12/task, #1 on AA-AnalystAgent at $0.54/task average.
- [2026-07-08] Gemini API managed agents add MCP support, background execution, custom function calling, and credential refresh; AINews frames Interactions API as Google's default stateful interface for models and agents.
- [2026-06-25] Gemini 3.5 Flash adds built-in computer use for browser, desktop, and mobile with sensitive-action confirmations and prompt-injection shutdown behavior.
- [2026-05-19] Google I/O 2026: Gemini 3.5 Flash GA as the new AI Mode default (per AINews: Terminal-Bench 2.1 76.2%; AA flags Intelligence Index 55 but 5.5x costlier than Gemini 3 Flash), Antigravity 2.0 (desktop/CLI/SDK multi-agent coding orchestration), Gemini Spark (24/7 personal background agent on cloud VMs), and a Search AI-Mode redesign with generative UI, mini-apps, and persistent information agents.
- [2026-04-30] Downloadable file generation from chat: Google/Microsoft Office formats, PDF, CSV, LaTeX, TXT, RTF, Markdown — positions Gemini as an artifact-producing workplace assistant, not only conversational AI

<!-- The following 3 entries move to wiki/history/tools/gemini.md: -->
<!-- [2026-04-23] Cloud Next '26: Gemini Enterprise Agent Platform replaces Vertex AI ... -->
<!-- [2026-04-22] Added benchmark scores for Deep Research Max ... -->
<!-- [2026-04-21] Added Deep Research and Deep Research Max ... -->
```

### wiki/history/tools/gemini.md (updated)

```md
## Archived from current page on 2026-09-07 (new block)

- [2026-04-23] Cloud Next '26: Gemini Enterprise Agent Platform replaces Vertex AI; Agent Studio, 200+ models, Workspace Intelligence GA, Knowledge Catalog, Gemini Embedding 2 GA, and broader agent governance stack
- [2026-04-22] Added benchmark scores for Deep Research Max (93.3% DeepSearchQA, 85.9% BrowseComp, 54.6% HLE); added collaborative planning and code execution capabilities from AINews coverage
- [2026-04-21] Added Deep Research and Deep Research Max: Gemini API public preview, MCP support, multimodal grounding, and native visual reports
```

## Open questions

None.
