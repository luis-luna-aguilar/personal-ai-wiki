---
title: Claude Opus 4.7 (archived)
type: model
domains: [models]
subcategory: frontier-model
tags: [anthropic, closed-source]
as_of: 2026-05-13
sources: [ainews-2026-04-21, every-opus-4-7-vibe-check, vectorlab-opus-4-7-flop, claude-design-launch, openai-gpt-5-5-launch, danshipper-gpt-5-5-vibe-check, opus-4-7-tokenizer-economics-2026-04-30, opus-47-reels-us-back-in]
---

# Claude Opus 4.7 (archived)

**Superseded by [Claude Opus 4.8](../../models/claude-opus-4-8.md) (June 2026).**

Claude Opus 4.7 was Anthropic's flagship multimodal model before Opus 4.8. It appeared stronger than 4.6 on explicit coding, document, and visual artifact tasks, but early practitioner reactions described a more literal, less gap-filling model whose real-world reliability depended more heavily on prompt quality and reasoning mode.

## Historical status (as of 2026-04-21)

- #1 in Vision & Document Arena, with wins in diagram, homework, and OCR categories
- Stronger on well-specified coding and interface, slide, and document generation tasks
- Powered [Claude Design](../../tools/claude-design.md), Anthropic's research-preview surface for prototypes, slides, and one-pagers
- Hands-on reviews described a sharper "say exactly what you mean" bias than Opus 4.6
- Multiple reports described regressions in long-context retrieval, adaptive-reasoning behavior, or general reliability on loosely specified work
- New tokenizer appeared to increase effective token usage on some workloads versus 4.6

## Strengths

- Explicit, tightly scoped coding and artifact-generation tasks
- Document-heavy and visually structured workloads
- Better self-checking and verification behavior when the task is concretely framed

## Weaknesses / caveats

- More literal and less willing to infer missing intent than 4.6
- Mixed early reports on long-context retrieval and practical reliability
- Cost and usage could feel higher in practice because the tokenizer mapped the same inputs to more tokens on some content types
- GPT-5.5 led Opus 4.7 on Terminal-Bench 2.0, GDPval, ARC-AGI-2, CyberGym, and writing momentum in Every's vibe check; Opus kept edges on SWE-Bench Pro, MCP Atlas, FinanceAgent, long-context graph tasks, plan quality, and some front-end/full-stack work
- **Fast mode** (May 2026, research preview): 2.5x faster output at ~6x the per-token cost; same model depth as standard Opus 4.7; available via API and Claude Code

## Recent changes

- [2026-06-03] Archived after Claude Opus 4.8 superseded it
- [2026-05-13] Fast mode shipped (research preview): 2.5x faster at ~6x cost; vibe checks report practitioners returning from Codex for planning and creative work
- [2026-04-30] Tokenizer economics reported: Opus 4.7 tokenizer may produce more tokens per character than 4.6 for code-heavy and symbol-dense inputs, raising real agent-loop costs
- [2026-04-23] GPT-5.5 released; OpenAI retakes several public benchmark categories, while Opus 4.7 retains stronger SWE-Bench Pro, MCP Atlas, FinanceAgent, long-context, and planning-quality signals
- [2026-04-21] Arena results: #1 Vision & Document; +4 over Opus 4.6

## Sources

- [AINews — Moonshot Kimi K2.6, Hermes Agent, Codex Chronicle (2026-04-21)](../../sources/newsletters/ainews-2026-04-21.md)
- [Every — Vibe Check: Opus 4.7 Stopped Reading Between the Lines](../../sources/newsletters/every-opus-4-7-vibe-check.md)
- [Vector Lab — Opus 4.7 is a Flop](../../sources/newsletters/vectorlab-opus-4-7-flop.md)
- [Claude Design launch](../../sources/tweets/claude-design-launch.md)
- [Opus 4.7 tokenizer economics](../../sources/newsletters/opus-4-7-tokenizer-economics-2026-04-30.md)
- [Opus 4.7 Reels Us Back In — Every (Context Window)](../../sources/newsletters/opus-47-reels-us-back-in.md)
