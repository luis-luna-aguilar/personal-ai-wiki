---
title: I Vibe Coded a Security Risk
type: source
source_type: newsletter
source_file: raw/newsletters/2026-08-10-i-vibe-coded-a-security-risk.md
url: https://every.to/working-overtime/i-vibe-coded-a-security-risk
published: 2026-08-10
ingested: 2026-09-07
domains: [training]
---

# I Vibe Coded a Security Risk

Every staff writer Katie Parrott describes vibe-coding an MCP connector into her small app Tastemaker with Claude's help, shipping it after only testing that it worked, and later discovering — via an unrelated second opinion from GPT-5.6 Sol — that the connector had a public, unauthenticated registration route. She frames the failure through OpenAI's "task crossover" research and the psychological "illusion of explanatory depth," and lands on three personal rules: learn the field's basics first, get a human expert review, and don't let the same AI's self-assessment be the only evidence a feature is safe.

## Influenced pages

- [training/ai-delegation-management](../../training/ai-delegation-management.md) — new Failure-modes case study on happy-path testing and the illusion of explanatory depth

## Key claims extracted

- OpenAI's "task crossover" research: 16.8% of a studied ~800,000 work-related ChatGPT messages involved doing work outside the user's normal occupation
- A GPT-5.6 Sol review found a live, public, unauthenticated registration route into a Claude-built MCP connector; no evidence surfaced of exploitation before it was pulled
- Psychological framing: the "illusion of explanatory depth" — people feel they understand a mechanism until asked to explain it step by step; AI's fluent explanations make it easy to skip that check
