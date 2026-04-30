---
title: Claude Opus 4.7
type: model
domains: [models]
subcategory: frontier-multimodal-model
tags: [anthropic, closed-source]
as_of: 2026-04-23
sources: [ainews-2026-04-21, every-opus-4-7-vibe-check, vectorlab-opus-4-7-flop, claude-design-launch, openai-gpt-5-5-launch, danshipper-gpt-5-5-vibe-check]
---

# Claude Opus 4.7

Anthropic's current flagship multimodal model. It appears stronger than 4.6 on explicit coding, document, and visual artifact tasks, but early practitioner reactions describe a more literal, less gap-filling model whose real-world reliability depends more heavily on prompt quality and reasoning mode.

## Current status (as of 2026-04-21)

- #1 in Vision & Document Arena, with wins in diagram, homework, and OCR categories
- Stronger on well-specified coding and interface, slide, and document generation tasks
- Powers [Claude Design](../tools/claude-design.md), Anthropic's research-preview surface for prototypes, slides, and one-pagers
- Hands-on reviews describe a sharper "say exactly what you mean" bias than Opus 4.6
- Multiple reports describe regressions in long-context retrieval, adaptive-reasoning behavior, or general reliability on loosely specified work
- New tokenizer appears to increase effective token usage on some workloads versus 4.6

## Strengths

- Explicit, tightly scoped coding and artifact-generation tasks
- Document-heavy and visually structured workloads
- Better self-checking and verification behavior when the task is concretely framed

## Weaknesses / caveats

- More literal and less willing to infer missing intent than 4.6
- Mixed early reports on long-context retrieval and practical reliability
- Cost and usage can feel higher in practice because the tokenizer maps the same inputs to more tokens on some content types
- GPT-5.5 now leads Opus 4.7 on Terminal-Bench 2.0, GDPval, ARC-AGI-2, CyberGym, and writing momentum in Every's vibe check; Opus still keeps real edges on SWE-Bench Pro, MCP Atlas, FinanceAgent, long-context graph tasks, plan quality, and some front-end/full-stack work

## Recent changes

- [2026-04-23] GPT-5.5 released; OpenAI retakes several public benchmark categories, while Opus 4.7 retains stronger SWE-Bench Pro, MCP Atlas, FinanceAgent, long-context, and planning-quality signals
- [2026-04-21] Added operator-view caveats: stronger explicit-task performance, but more literal behavior and mixed reliability reports
- [2026-04-21] Arena results: #1 Vision & Document; +4 over Opus 4.6

## Sources

- [AINews — Moonshot Kimi K2.6, Hermes Agent, Codex Chronicle (2026-04-21)](../sources/newsletters/ainews-2026-04-21.md)
- [Every — Vibe Check: Opus 4.7 Stopped Reading Between the Lines](../sources/newsletters/every-opus-4-7-vibe-check.md)
- [Vector Lab — Opus 4.7 is a Flop](../sources/newsletters/vectorlab-opus-4-7-flop.md)
- [Claude Design launch](../sources/tweets/claude-design-launch.md)
