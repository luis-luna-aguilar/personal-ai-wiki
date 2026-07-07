---
title: GPT-5.5
type: model
domains: [models, coding, agents, science, cybersecurity]
subcategory: frontier-model
tags: [openai, closed-source]
as_of: 2026-05-18
sources: [openai-gpt-5-5-launch, danshipper-gpt-5-5-vibe-check, gpt-5-5-instant-default-2026-05-06, chatgpt-personal-finance-2026-05]
---

# GPT-5.5

OpenAI's April 2026 frontier model, positioned as "our smartest and most intuitive to use model yet." The launch framing is strongest on terminal/command-line coding, broad knowledge work, math, abstract reasoning, cybersecurity, and early scientific-research use cases. At launch, Claude Opus 4.7 still held some important edges, especially on SWE-Bench Pro, MCP Atlas, FinanceAgent, and practitioner-reported plan quality.

## Current status (as of 2026-05-06)

- Released April 23, 2026; rolling out across ChatGPT and Codex, with API access described as coming soon
- Two variants: GPT-5.5 and GPT-5.5 Pro; OpenAI also frames GPT-5.5 Thinking as the ChatGPT mode for harder tasks
- Codex now runs on GPT-5.5 with a 400K context window; API launch notes a 1M-context offering
- Public benchmark lead on Terminal-Bench 2.0 (82.7%), GDPval (84.9%), ARC-AGI-2 (85.0%), CyberGym (81.8%), and BixBench (80.5%)
- Claude Opus 4.7 still leads on SWE-Bench Pro (64.3% vs 58.6%), MCP Atlas (79.1% vs 75.3%), and FinanceAgent (64.4% vs 60.0%)
- OpenAI says GPT-5.5 reaches better Codex outcomes with fewer tokens than GPT-5.4 and now powers heavy internal weekly usage across many functions
- Secondary May 2026 coverage says GPT-5.5 Instant replaced GPT-5.3 Instant as ChatGPT's default model, with API exposure via `chat-latest`; verify against OpenAI docs before treating specific hallucination-reduction numbers as official.

## Strengths

- Strongest current OpenAI model for agentic coding, terminal work, and broad knowledge-work tasks
- Much stronger abstract reasoning and math positioning than prior GPT-5.4
- Scientific-use framing is no longer speculative: launch materials cite benchmark gains plus concrete research-use anecdotes
- Writing and coding vibe check from Every suggests this is the first OpenAI release in about a year that materially pulls some users back from Claude for daily use

## @Finances personal finance agent (May 2026)

- Activated with `@Finances` inside any ChatGPT conversation (US Pro only, preview)
- Connects to 12,000+ financial providers; grounds answers in the user's actual income and spending data
- Finance benchmark scores: GPT-5.5 Thinking 79/100 on complex personal-finance tasks; GPT-5.5 Pro 82.5/100
- Launch video: 14M+ views in 48 hours
- Analyst framing: potential displacement of dedicated fintech assistant apps

## Weaknesses / caveats

- At launch, Claude Opus 4.7 remained stronger on some higher-fidelity engineering and tool-use evaluations
- Long-context graph-style tasks still show a meaningful Claude lead in OpenAI's own comparison tables
- Practitioner feedback is not all one-way: Every still gives Opus the edge on plan quality, front-end/full-stack product work, and underspecified vibe-coding tasks
- Bio/chem and cybersecurity capability are high enough that OpenAI is pairing broad deployment with tighter safety controls and a gated cyber-access program

## Recent changes

- [2026-05-18] @Finances agent launched: 12,000+ financial providers; personalized money advice grounded in real spending data; GPT-5.5 Thinking 79/100, Pro 82.5/100; US Pro preview; 14M views in 48h
- [2026-05-06] Secondary coverage says GPT-5.5 Instant became ChatGPT's default model, replacing GPT-5.3 Instant; official verification still needed for exact rollout and hallucination claims.
- [2026-04-23] Released; GPT-5.5 supersedes GPT-5.4 as OpenAI's current frontier model and leads on Terminal-Bench 2.0, GDPval, ARC-AGI-2, CyberGym, and BixBench

## Sources

- [Introducing GPT-5.5 — OpenAI](../sources/articles/openai-gpt-5-5-launch.md)
- [Dan Shipper — GPT-5.5 vibe check](../sources/tweets/danshipper-gpt-5-5-vibe-check.md)
- [GPT-5.5 Instant becomes ChatGPT default - secondary coverage](../sources/newsletters/gpt-5-5-instant-default-2026-05-06.md)
