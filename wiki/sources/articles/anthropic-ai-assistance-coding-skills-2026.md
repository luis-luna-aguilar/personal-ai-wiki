---
title: How AI assistance impacts the formation of coding skills
type: source
source_type: article
source_file: raw/articles/2026-09-06-anthropiccom-research-ai-assistance-coding-skills.md
url: https://www.anthropic.com/research/AI-assistance-coding-skills
published: 2026-07-16
ingested: 2026-09-06
domains: [training]
---

# How AI assistance impacts the formation of coding skills

Anthropic's own randomized controlled trial (arXiv 2601.20245, Shen & Tamkin): 52 mostly-junior software engineers learned Trio, an unfamiliar Python async library, either with or without an AI coding assistant, then took a comprehension quiz. The AI group scored 50% vs. 67% for the hand-coding group (Cohen's *d*=0.738, p=0.01) — a gap concentrated in debugging questions. Qualitative analysis found the outcome depended on *how* people used the assistant: three low-scoring interaction patterns involved heavy AI reliance with little independent verification (full delegation, progressive delegation, AI-driven debugging); three high-scoring patterns combined AI use with active comprehension-checking (generate-then-ask-questions, code-plus-explanation requests, conceptual-only queries). Anthropic frames the core finding as: using AI didn't guarantee worse learning outcomes, but careless AI use did.

## Influenced pages

- [Anti-autopilot review friction](../../training/anti-autopilot-review-friction.md) — confirmed primary sourcing for the existing 50%-vs-67% finding, added interaction-pattern taxonomy

## Key claims extracted

- 52 mostly-junior developers, RCT design, learning Trio (Python async library)
- AI group: 50% quiz score; hand-coding group: 67% (Cohen's d=0.738, p=0.01)
- Largest score gap on debugging questions specifically
- Three low-scoring interaction patterns (avg quiz <40%): AI delegation, progressive AI reliance, iterative AI debugging
- Three high-scoring interaction patterns (avg quiz 65%+): generation-then-comprehension, hybrid code-explanation, conceptual inquiry
- Underlying paper: arXiv 2601.20245 (Shen & Tamkin, "How AI Impacts Skill Formation")
