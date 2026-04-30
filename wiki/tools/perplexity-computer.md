---
title: Perplexity Computer
type: tool
domains: [computer-use, finance]
subcategory: computer-use
tags: [perplexity, closed-source]
as_of: 2026-04-10
sources:
  - perplexity-computer-plaid
  - perplexity-personal-computer
---

# Perplexity Computer

Autonomous AI agent launched 2026-02-25 that orchestrates 19 different AI models to complete complex, multi-step workflows in the background. Rather than relying on a single model, Computer is an orchestration layer that routes each part of a task to the model best suited for that type of work.

## Current status (as of 2026-04-10)

- Exclusively available on Perplexity Max ($200/month); 10,000 credits/month, consumption varies by task complexity
- Enterprise tier at $325/seat/month with security controls and audit logs
- Connects to 400+ applications (Slack, Gmail, GitHub, Notion) and 12,000+ financial institutions via Plaid
- Personal Computer, launched 2026-03-11, frames the product as a persistent digital proxy: an always-on Mac mini environment with ongoing access to files, apps, and sessions that can still be remotely controlled from any device

## How it works

1. **Goal input** — user describes objective in natural language
2. **Task decomposition** — system breaks goals into subtasks
3. **Model selection** — routes to specialized models (Claude Opus 4.6 for coding, Gemini for research, GPT-5.2 for long-context, Grok for lightweight tasks, Veo 3.1 for video)
4. **Parallel execution** — sub-agents run simultaneously
5. **Continuous optimization** — system monitors quality and self-corrects before delivering results

## Strengths

- Multi-model orchestration avoids single-model bottlenecks; each subtask gets the best-fit model
- Deep third-party integrations (400+ apps, 12,000+ financial institutions via Plaid)
- Can run for hours or months on long-horizon tasks
- Dedicated-machine model makes "always-on agent" behavior more concrete than a normal chat surface
- Local-ish Personal Computer variant addresses privacy-sensitive and continuity-sensitive workloads better than purely ephemeral sessions

## Weaknesses / caveats

- $200/month price point limits adoption to power users and enterprises
- Credit-based consumption model makes cost unpredictable for complex workflows
- Multi-model routing adds latency and potential failure modes vs. single-model agents

## Recent changes

- [2026-04-10] Plaid integration connects to 12,000+ financial institutions; users can build custom budgeting/tracking tools
- [2026-03-11] Perplexity Personal Computer launched — local Mac Mini variant for on-device agent workloads
- [2026-02-25] Perplexity Computer launched with 19-model orchestration, Max-tier exclusive

## Sources

- [Perplexity Computer — Plaid financial integrations](../sources/articles/perplexity-computer-plaid.md)
- [Perplexity Personal Computer](../sources/newsletters/perplexity-personal-computer.md)
