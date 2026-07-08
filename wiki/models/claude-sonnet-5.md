---
title: Claude Sonnet 5
type: model
domains: [models, coding]
subcategory: frontier-model
tags: [anthropic]
as_of: 2026-07-02
sources: [every-sonnet-5-vibe-check-2026-07-02, the-code-devin-security-2026-07-02, every-tale-of-two-models-2026-07-05, claude-sonnet-5-official-2026-06-30]
---

# Claude Sonnet 5

Claude Sonnet 5 is Anthropic's middle-tier Claude 5 model, positioned as a default model for broad daily work: more capable than smaller utility tiers, cheaper on paper than Opus, and more available than Fable for many users.

## Current status (as of 2026-07-02)

- Every's Vibe Check found Sonnet 5 broadly competent at writing, structured knowledge work, and some coding tasks, but hard to prefer over Opus 4.8, Fable 5, or GPT-5.5 for many specific jobs.
- Anthropic's official launch positions Sonnet 5 as its most agentic Sonnet model yet, available across Claude plans, Claude Code, and the API as `claude-sonnet-5`.
- Launch pricing is $2/M input and $10/M output through 2026-08-31, then $3/M input and $15/M output.
- The Code reports the model can cost more per finished task than expected because the same work may tokenize larger and run more reasoning loops.
- Artificial Analysis coverage cited by The Code says high-effort Sonnet 5 can cost about 15% more per task than Opus 4.8, while lower effort settings remain cheaper.
- Ramp Labs' benchmark coverage suggests the extra effort can buy tighter self-correction, so the right comparison is cost per completed task, not token list price.

## Strengths

- Solid default for general drafting, analysis, and medium-complexity coding.
- Better self-correction when effort is raised.
- Useful as an available middle tier when Fable access is constrained or overkill.

## Weaknesses / caveats

- Weak product positioning: many tasks have a cheaper, faster, or stronger model option.
- Cost can exceed the nominally more expensive Opus tier when effort is left high.
- Early Every testing found weaker agentic build performance than stronger Claude models.
- Official launch safety notes say Sonnet 5 has lower hallucination and sycophancy than Sonnet 4.6 and lower malicious capability than current Opus models.

## Recent changes

- [2026-06-30] Official Anthropic launch details added: Claude Code/API availability, `claude-sonnet-5` API name, promotional pricing, effort-level framing, and safety notes.
- [2026-07-02] Every and The Code reported early testing: capable but not clearly best-in-class; cost per task depends heavily on effort and tokenizer behavior.

## Sources

- [Every - Sonnet 5 Vibe Check](../sources/newsletters/every-sonnet-5-vibe-check-2026-07-02.md)
- [The Code - Devin Security / Sonnet 5 cost analysis](../sources/newsletters/the-code-devin-security-2026-07-02.md)
- [Every - A Tale of Two Models](../sources/newsletters/every-tale-of-two-models-2026-07-05.md)
- [Claude Sonnet 5 official launch](../sources/articles/claude-sonnet-5-official-2026-06-30.md)
