---
title: 'Claude — Building agents: When to fold subagents into your main agent loop'
type: source
source_type: article
source_file: raw/articles/2026-11-23-claudecom-resources-articles-building-agents-when-to-fold-su.md
url: https://claude.com/resources/articles/building-agents-when-to-fold-subagents-into-your-main-agent-loop
ingested: 2026-11-24
domains: [agents]
---

# Claude — Building agents: When to fold subagents into your main agent loop

Anthropic Applied AI guide arguing that many enterprise agents built as an orchestrator over team-owned specialist subagents do better as one agent loop with skills (progressive disclosure of procedure) and tool search (progressive disclosure of tools). It names the org-chart failure modes, describes the target single-loop design, and gives a staged migration: build a small end-to-end eval, fold subagents in one at a time, keep a subagent only when the folded version scores worse. The page carries no date; the wiki dates it 2026-10-24 from the forward.

## Influenced pages
- [Agent loop design](../../workflows/agent-loop-design.md) — new "Folding subagents into one loop" section
- [Multi-agent coordination](../../workflows/multi-agent-coordination.md) — "Fold before you split" bullet

## Key claims extracted
- Across several enterprise deployments, a single agent with skills frequently beat one-prompt and subagent designs on quality, often at lower cost and latency per task; one customer saw roughly 2x faster runtime
- One company's dozen specialist subagents made a consistent on-brand experience hard and added latency
- Org-chart failure modes: context management across agents, subagent sprawl, the Frankenprompt, unvetted localized evals, latency
- Keep subagents when there is measurable context-bloat degradation, parallel discardable contexts, or tool-selection / instruction conflicts
- Target loop: one model, one context, open tool loop with harness budgets and write gates; parallel tool batches; plan written and revised by the same model
- Skills hold procedure; tools hold hard limits, approvals, per-user permissions and mid-conversation lookups
- Tool choice tends to degrade past 30–50 tool definitions; group tools by user intent and use tool search with deferred loading
- Central team owns system prompt and end-to-end evals; 10 golden examples suffice to start; each team ships evals with its skills
- Fold by shared context starting with the most-used subagents; merge tightly coupled pairs; compare flipped tasks and run each task more than once
- Claude Code reduced its system prompt for advanced models by over 80%, partly through progressive disclosure
- Tooling: single-agent-loop migration kit; `/claude-api build-eval`, `prompt-audit`, `hillclimb`, `cost-optimize`; `/skill-creator`; `/skill-doctor`
