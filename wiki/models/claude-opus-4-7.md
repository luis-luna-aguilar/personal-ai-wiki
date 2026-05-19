---
title: Claude Opus 4.7
type: model
domains: [models]
subcategory: frontier-multimodal-model
tags: [anthropic, closed-source]
as_of: 2026-05-13
sources: [ainews-2026-04-21, every-opus-4-7-vibe-check, vectorlab-opus-4-7-flop, claude-design-launch, openai-gpt-5-5-launch, danshipper-gpt-5-5-vibe-check, opus-4-7-tokenizer-economics-2026-04-30, opus-47-reels-us-back-in]
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
- Cost and usage can feel higher in practice because the tokenizer maps the same inputs to more tokens on some content types — particularly code, structured text, and symbol-dense inputs; OpenRouter and Simon Willison analysis (secondary) suggests this effect raises real agent-loop costs for code-heavy workloads despite unchanged per-token sticker pricing
- GPT-5.5 now leads Opus 4.7 on Terminal-Bench 2.0, GDPval, ARC-AGI-2, CyberGym, and writing momentum in Every's vibe check; Opus still keeps real edges on SWE-Bench Pro, MCP Atlas, FinanceAgent, long-context graph tasks, plan quality, and some front-end/full-stack work
- **Fast mode** (May 2026, research preview): 2.5× faster output at ~6× the per-token cost; same model depth as standard Opus 4.7; available via API and Claude Code
- Quality vibe shift: several Every team members who migrated to Codex after GPT-5.5 are returning; practitioner framing — Opus 4.7 feels like a "senior magazine editor," Codex like an "AP fact checker"; Opus remains stronger on planning, creative, and multi-step work

## Recent changes

- [2026-05-13] Fast mode shipped (research preview): 2.5× faster at ~6× cost; vibe checks report practitioners returning from Codex for planning and creative work
- [2026-04-30] Tokenizer economics reported: Opus 4.7 tokenizer may produce more tokens per character than 4.6 for code-heavy and symbol-dense inputs, raising real agent-loop costs (secondary coverage from OpenRouter/Willison; primary Anthropic analysis not yet available)
- [2026-04-23] GPT-5.5 released; OpenAI retakes several public benchmark categories, while Opus 4.7 retains stronger SWE-Bench Pro, MCP Atlas, FinanceAgent, long-context, and planning-quality signals
- [2026-04-21] Added operator-view caveats: stronger explicit-task performance, but more literal behavior and mixed reliability reports
- [2026-04-21] Arena results: #1 Vision & Document; +4 over Opus 4.6

## Sources

- [AINews — Moonshot Kimi K2.6, Hermes Agent, Codex Chronicle (2026-04-21)](../sources/newsletters/ainews-2026-04-21.md)
- [Every — Vibe Check: Opus 4.7 Stopped Reading Between the Lines](../sources/newsletters/every-opus-4-7-vibe-check.md)
- [Vector Lab — Opus 4.7 is a Flop](../sources/newsletters/vectorlab-opus-4-7-flop.md)
- [Claude Design launch](../sources/tweets/claude-design-launch.md)
- [Opus 4.7 tokenizer economics](../sources/newsletters/opus-4-7-tokenizer-economics-2026-04-30.md)
- [Opus 4.7 Reels Us Back In — Every (Context Window)](../sources/newsletters/opus-47-reels-us-back-in.md)
