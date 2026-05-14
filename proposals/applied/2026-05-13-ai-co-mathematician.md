---
type: proposal
sources:
  - raw/newsletters/2026-05-13-ainews-the-end-of-finetuning.md
status: pending
created: 2026-05-13
---

# Proposal: Google DeepMind AI Co-Mathematician — 48% FrontierMath Tier 4

## Summary

Google DeepMind released an AI Co-Mathematician: an asynchronous, stateful research workbench for mathematicians supporting ideation, literature discovery, computational analysis, theorem verification, and formal outputs. Reports 48% on FrontierMath Tier 4 — research-level math authored by 64 mathematicians to be beyond olympiad-style. In the same week, physics-intern (a related DeepMind system) improved Gemini 3.1 Pro from 17.7% → 31.4% on CritPt by decomposing problems into specialized subagents.

## Intended changes

- [x] **Update** `wiki/state-of/science.md` — add AI Co-Mathematician under `Frontier models used in science` and note the physics-intern result; update `as_of` and `sources`
    > See diff snippets below

- [x] **Create** `wiki/sources/newsletters/ai-co-mathematician-2026-05-13.md`
    > See draft below

## Open questions

- Primary URL for AI Co-Mathematician is listed as "Google DeepMind blog — verify" in the triage. Apply without the URL or hold for verification?
	- Feedback: The paper is here https://arxiv.org/abs/2605.06651

## Page drafts

### wiki/state-of/science.md — diff snippets

**Frontmatter `as_of`:**
> **Before:** `as_of: 2026-04-23`
> **After:** `as_of: 2026-05-13`

**Frontmatter `sources` — append:**
> Add `ai-co-mathematician-2026-05-13`

**Frontier models used in science section — append after the GPT-5.5 line:**

```markdown
- **AI Co-Mathematician** — Google DeepMind; asynchronous, stateful research workbench for mathematicians; supports ideation, literature discovery, computational analysis, theorem verification, and formal proof outputs; 48% on FrontierMath Tier 4 (research-level math above olympiad-style, authored by 64 mathematicians) *(as of 2026-05-13)*
```

**Recent changes — prepend:**
```
- [2026-05-13] Added AI Co-Mathematician (Google DeepMind): 48% FrontierMath Tier 4; asynchronous stateful workbench for mathematicians; physics-intern (related) boosted Gemini 3.1 Pro from 17.7% → 31.4% on CritPt via specialized subagent decomposition
```

### wiki/sources/newsletters/ai-co-mathematician-2026-05-13.md (new)

```markdown
---
title: Google DeepMind AI Co-Mathematician and physics-intern
type: source
source_type: newsletter
source_file: raw/newsletters/2026-05-13-ainews-the-end-of-finetuning.md
published: 2026-05-13
ingested: 2026-05-13
domains: [science, models]
---

# Google DeepMind AI Co-Mathematician and physics-intern

AINews newsletter dated May 13, 2026. Covers AI Co-Mathematician and physics-intern as part of the same agentic science-systems theme.

## Influenced pages

- [State of Science](../../state-of/science.md) — AI Co-Mathematician added to `Frontier models used in science`

## Key claims extracted

### AI Co-Mathematician
- Developer: Google DeepMind
- Type: asynchronous, stateful research workbench (not a one-shot query tool)
- Capabilities: ideation, literature discovery, computational analysis, theorem verification, formal proof outputs
- Benchmark: 48% on FrontierMath Tier 4
  - FrontierMath Tier 4: research-level mathematics problems authored by 64 mathematicians specifically to be above olympiad-style difficulty
- Status: announced/released (exact public availability status unconfirmed in newsletter; verify against DeepMind blog)

### physics-intern (related system)
- Developer: Google DeepMind
- Task: improved Gemini 3.1 Pro performance on CritPt (critical-point physics benchmark)
- Before: 17.7% → After: 31.4%
- Mechanism: decomposes the problem into specialized subagents rather than running a single generalist pass
- Framing: reinforces the "agentic decomposition improves specialized domain performance" thesis
```

