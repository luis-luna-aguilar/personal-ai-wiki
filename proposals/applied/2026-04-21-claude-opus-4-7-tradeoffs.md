---
type: proposal
sources:
  - raw/newsletters/2026-04-17-vibe-check-opus-47-stopped-reading-between-the-l.md
  - raw/newsletters/2026-04-21-opus-47-is-a-flop.md
  - raw/newsletters/2026-04-18-ainews-the-two-sides-of-openclaw.md
  - raw/tweets/2026-04-21-bcherny-2044822408826380440.md
status: pending
created: 2026-04-21
---

# Proposal: Claude Opus 4.7 — capability gains with reliability tradeoffs

## Summary

The wiki currently captures Opus 4.7 mainly as an arena winner on document-heavy workloads. This batch adds the missing operator view: 4.7 appears stronger on explicit coding and visual artifact generation, but noticeably more literal, more mode-sensitive, and less reliable than 4.6 in loosely specified or long-context workflows. The right update is not to demote it outright, but to make the caveats first-class.

## Intended changes

- [x] **Update** `wiki/models/claude-opus-4-7.md` — expand from single benchmark win to a balanced current-status page
  > Add explicit tradeoffs: better self-verification / coding on well-specified tasks, but more literal behavior, mixed long-context reports, tokenizer inflation, and noisier real-world usage.

- [x] **Update** `wiki/state-of/models.md` — keep Opus 4.7 as a frontier leader, but make the description less one-dimensional
  > Replace the current line:
  > `- [[models/claude-opus-4-7]] — Anthropic; #1 Vision & Document Arena ...`
  >
  > With:
  > `- [[models/claude-opus-4-7]] — Anthropic flagship; stronger on explicit coding, document, and visual artifact tasks, but early user reports describe more literal behavior and mixed long-context reliability *(as of 2026-04-21)*`

- [x] **Create** `wiki/sources/newsletters/every-opus-4-7-vibe-check.md` — source summary for the strongest hands-on review in this batch
  > See draft below.

- [x] **Create** `wiki/sources/newsletters/vectorlab-opus-4-7-flop.md` — source summary for the strongest skeptical synthesis in this batch
  > See draft below.

## Page drafts

### wiki/models/claude-opus-4-7.md (updated snippet)

```md
---
title: Claude Opus 4.7
type: model
domains: [models]
subcategory: frontier-multimodal-model
tags: [anthropic, closed-source]
as_of: 2026-04-21
sources: [ainews-2026-04-21, every-opus-4-7-vibe-check, vectorlab-opus-4-7-flop]
---

# Claude Opus 4.7

Anthropic's current flagship multimodal model. It appears stronger than 4.6 on explicit coding, document, and visual artifact tasks, but early practitioner reactions describe a more literal, less gap-filling model whose real-world reliability depends more heavily on prompt quality and reasoning mode.

## Current status (as of 2026-04-21)

- #1 in Vision & Document Arena, with wins in diagram, homework, and OCR categories
- Stronger on well-specified coding and interface / slide / document generation tasks
- Hands-on reviews describe a sharper "say exactly what you mean" bias than Opus 4.6
- Multiple reports describe regressions in long-context retrieval, adaptive-reasoning behavior, or general reliability on loosely specified work
- New tokenizer appears to increase effective token usage on some workloads versus 4.6

## Strengths

- Explicit, tightly scoped coding and artifact-generation tasks
- Document-heavy and visually structured workloads
- Better self-checking / verification behavior when the task is concretely framed

## Weaknesses / caveats

- More literal and less willing to infer missing intent than 4.6
- Mixed early reports on long-context retrieval and practical reliability
- Cost / usage can feel higher in practice because the tokenizer maps the same inputs to more tokens on some content types

## Recent changes

- [2026-04-21] Added operator-view caveats: stronger explicit-task performance, but more literal behavior and mixed reliability reports
- [2026-04-21] Arena results: #1 Vision & Document; +4 over Opus 4.6
```

### wiki/sources/newsletters/every-opus-4-7-vibe-check.md (new)

```md
---
title: Every — Vibe Check: Opus 4.7 Stopped Reading Between the Lines
type: source
source_type: newsletter
source_file: raw/newsletters/2026-04-17-vibe-check-opus-47-stopped-reading-between-the-l.md
ingested: 2026-04-21
domains: [models, coding]
---

# Every — Vibe Check: Opus 4.7 Stopped Reading Between the Lines

Every's hands-on review of Opus 4.7 across coding, writing, and knowledge work. Core claim: 4.7 is often better on explicit, well-specified tasks, but worse at inferring intent or "reading between the lines," making it more prompt-sensitive than 4.6.

## Key claims extracted

- Best results came from tightly specified coding and artifact tasks
- 4.7 produced stronger coding and slide-deck outcomes in some tests
- 4.6 was preferred in some writing and P&L-style judgment tasks
- The review frames the model shift as a dial-back in eagerness / implicit inference rather than a simple quality increase
```

### wiki/sources/newsletters/vectorlab-opus-4-7-flop.md (new)

```md
---
title: Vector Lab — Opus 4.7 is a Flop
type: source
source_type: newsletter
source_file: raw/newsletters/2026-04-21-opus-47-is-a-flop.md
ingested: 2026-04-21
domains: [models, coding]
---

# Vector Lab — Opus 4.7 is a Flop

Vector Lab's skeptical synthesis of Opus 4.7. The piece argues that 4.7 is at best a sidegrade: smarter in some coding situations, but less trustworthy overall because of adaptive-thinking misses, increased tokenization cost, and weaker behavior outside coding/STEM tasks.

## Key claims extracted

- Practical reliability is framed as worse than Opus 4.6 despite raw capability gains
- Adaptive thinking is blamed for under-reasoning in some non-coding tasks
- Tokenizer changes are described as materially increasing real-world cost
- The strongest positive claim is still around coding intelligence, not broad usability
```

## Open questions

- Do you want Opus 4.7's page to keep the "current flagship" framing if later evidence continues to split this sharply between benchmark strength and operator trust?
	- This is a tricky questions, but lets keep it for now.
