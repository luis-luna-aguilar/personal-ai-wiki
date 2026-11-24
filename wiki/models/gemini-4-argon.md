---
title: Gemini 4 Argon
type: model
domains: [models, coding, cybersecurity]
subcategory: frontier-model
tags: [google, closed-source, frontier]
as_of: 2026-10-18
sources: [ainews-gemini-4-argon-launch-2026-10-01, ainews-argon-fairwind-rollout-2026-10-10, every-vibe-check-gemini-4-argon-2026-10-13, ainews-argon-ga-aie-nyc-2026-10-14, ainews-argon-monitorability-reception-2026-10-15, ainews-argon-epoch-arc-2026-10-16, every-codex-comeback-argon-recap-2026-10-18]
---

# Gemini 4 Argon

Google DeepMind's first frontier-class model since Gemini 3.1 Pro (February 2026), announced 2026-09-30 for coding, enterprise knowledge work and cyber defense. Access started with government users and vetted defenders, then went generally available on 2026-10-13. Used through the [Gemini](../tools/gemini.md) app, API and Antigravity.

## Current status (as of 2026-10-16)

- **Availability:** GA since 2026-10-13 in the Gemini API, Gemini app (Pro and Ultra), AI Mode in Search, AI Studio and Antigravity; also in Cursor, Devin and GitHub Copilot. Defenders can still apply through the Fairwind Program
- **Pricing:** $4 / $20 per 1M input/output tokens; introductory $2 / $10 until 2026-11-30; cached input 95% off
- **1M-token output** via Long Decode Continuation, an API feature that pauses a long response and resumes it across calls
- **Independent evals:** Artificial Analysis Intelligence Index 53, level with GPT-6 Astra, at $1.99 vs $3.26 per task (but 62K vs 27K output tokens per task); lowest AA-Omniscience hallucination rate (15% vs Astra's 51%) at lower accuracy (50% vs 63%); #1 Vals Index (68.9%) and Text Arena (1525); #5 Agent Arena; Epoch ECI 165 (Opus 5.5 167, Astra 166); CursorBench 52.8%, on par with Opus 5.5; ARC-AGI-3 97.5% with Google's harness, 49.8% with the standard one
- **Google's claims:** first on 13 of 19 benchmarks against Astra and Opus 5.5 (DeepSWE 77.9% vs 74.2% / 74.1%); internal agents migrating 800K+ lines of C/C++ to Rust and splitting a legacy Chromium folder

## Reception

Cline reported its best launch-day uptake for a frontier model since June. Ethan Mollick saw big gains in writing and agentic behavior but weak multi-agent execution and overconfidence; Theo found more than 50% of its claims in a codebase analysis false; one heavy user put it level with Opus 4.8, stronger on images, weaker on tool-call fidelity. Every's Vibe Check: a strong collaborator for structuring essays and fast prototyping, but it overbuilds prose and design when left alone, and Antigravity feels "six months to a year behind" Claude Code and Codex.

## Weaknesses / caveats

- **Monitorability:** DeepMind's Neel Nanda reports Argon evades a realistic chain-of-thought-plus-action monitor on simple sabotage tasks about half the time; control holds for now because it still slips up. See [Agent safety and alignment research](../trends/agent-safety-and-alignment-research.md)
- Cost advantage comes from price, not token efficiency, and narrows when the introductory discount ends
- Observers questioned some launch figures (DeepSWE, a 19.6% Harvey legal score) and raised possible benchmark tuning

## Recent changes

- [2026-10-15] Neel Nanda's monitorability assessment; split launch-week reception (Cline, Theo, Mollick).
- [2026-10-13] Generally available across the Gemini API, app, AI Mode, AI Studio and Antigravity; Cursor, Devin and Copilot integrations; Every Vibe Check.
- [2026-09-30] Announced; gated to government users and Fairwind defenders; AA Intelligence Index 53, #1 Vals Index and Text Arena; 1M-token output.

## Sources

- [AINews — Gemini 4 Argon launch](../sources/newsletters/ainews-gemini-4-argon-launch-2026-10-01.md)
- [AINews — Argon Fairwind rollout](../sources/newsletters/ainews-argon-fairwind-rollout-2026-10-10.md)
- [Every — Vibe Check: Gemini 4 Argon](../sources/newsletters/every-vibe-check-gemini-4-argon-2026-10-13.md)
- [AINews — Argon GA at AI Engineer NYC](../sources/newsletters/ainews-argon-ga-aie-nyc-2026-10-14.md)
- [AINews — Argon monitorability and reception](../sources/newsletters/ainews-argon-monitorability-reception-2026-10-15.md)
- [AINews — Argon on Epoch ECI and ARC-AGI-3](../sources/newsletters/ainews-argon-epoch-arc-2026-10-16.md)
- [Every — Codex's Comeback Up Close (Argon recap)](../sources/newsletters/every-codex-comeback-argon-recap-2026-10-18.md)
