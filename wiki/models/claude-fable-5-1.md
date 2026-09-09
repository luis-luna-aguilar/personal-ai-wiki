---
title: Claude Fable 5.1 / Mythos 5.1
type: model
domains: [models, coding, cybersecurity]
subcategory: frontier-model
tags: [anthropic, frontier]
as_of: 2026-09-02
sources: [every-fable-51-vibe-check-2026-09-01, ainews-fablemythos-51-2026-09-02]
---

# Claude Fable 5.1 / Mythos 5.1

Anthropic's flagship refresh, launched 2026-09-01, superseding [Claude Fable 5](../history/models/claude-fable-5.md). Fable 5.1 targets delegated, long-horizon coding and knowledge work; Mythos 5.1 is a paired release positioned for knowledge work. Credible community analysis (@eliebakouch, corroborated by Artificial Analysis' own fallback-routing note) holds that Fable and Mythos 5.1 are the same underlying weights, differentiated by a safety-classifier threshold rather than distinct base models — flagged requests fall back to Opus 4.8.

## Current status (as of 2026-09-02)

- Pricing unchanged from Fable 5: $10/$50/$12.5 per million input/output/cache-write tokens; cache-read price cut 75% ($1.00 → $0.25/M), a targeted win for agentic workloads that repeatedly re-read cached context.
- Artificial Analysis Intelligence Index 66 (Fable 5: 62; Opus 5: 63; GPT-5.6 Sol: 61) — back on the frontier ceiling after Fable 5's mid-pack showing against GPT-5.6 Sol.
- HLE 65% with tools; Terminal-Bench v2.1 91.4%; Terminal-Bench-Science more than doubled, 24.7% → 52.6%.
- Output-token usage rose ~1.7x versus Fable 5, so per-task cost is ~20% higher despite the cache-read cut ($3.76/task at max effort).
- New Enterprise Frontier Safeguards (EFS) add cross-session agent observability; several practitioners — including one who could not complete testing — hit false-positive safety flags on benign technical/theoretical prompts.
- Widely reported stylistic shift toward "less Claudese" (fewer em dashes and hyphenated compounds, per ValsAI lexical stats), though outputs also got longer overall (e.g. Terminal-Bench task outputs: 961 → 1299 words).

## Same weights, different routing

Community technical analysis converged on: Fable and Mythos 5.1 share weights; internal activations are inspected and escalate to a larger safety classifier, with dangerous requests falling back to Opus 4.8. Artificial Analysis independently confirmed fallback routing in its own evaluation (~4% of output tokens served by fallback) without confirming the "exact same weights" claim directly. If accurate, which benchmark line is labeled Fable vs. Mythos is closer to a safety-routing artifact than a distinct-model comparison — a live open question in system-card interpretation.

Note: this Mythos 5.1 is a new, publicly available paired release, distinct from [Claude Mythos Preview](claude-mythos-preview.md), Anthropic's earlier restricted-access cybersecurity-research model (Project Glasswing). The two share a name but not, per current sources, an established lineage.

## Strengths

- Frontier-ceiling benchmark gains, especially on hard agentic/science coding tasks (Terminal-Bench-Science)
- Cache-read cost cut materially helps long-running agent sessions that repeatedly re-read prior context
- Practitioner-reported writing-quality improvement: clearer prose, fewer "AI tells"

## Weaknesses / caveats

- Net cost per task is higher, not lower, due to increased output-token usage
- Enterprise Frontier Safeguards produced real false positives on benign prompts in first-week use
- Fable/Mythos routing ambiguity makes some system-card benchmark lines hard to attribute to "the model" vs. "the safety path"

## Recent changes

- [2026-09-01] Fable 5.1 / Mythos 5.1 launched, superseding Fable 5: AA Intelligence Index 66, 75% cache-read price cut, same-weights/different-routing debate, EFS false positives.

## Sources

- [Every — Vibe Check: Fable 5.1](../sources/newsletters/every-fable-51-vibe-check-2026-09-01.md)
- [AINews — Claude Fable/Mythos 5.1: new SOTA model](../sources/newsletters/ainews-fablemythos-51-2026-09-02.md)
