---
title: "[AINews] OpenAI launches GPT 5.6 Sol/Terra/Luna, Codex becomes ChatGPT superapp"
type: source
source_type: newsletter
source_file: raw/newsletters/2026-07-10-ainews-openai-launches-gpt-56-solterraluna-c.md
url: https://www.latent.space/p/ainews-openai-launches-gpt-56-solterraluna
published: 2026-07-10
ingested: 2026-09-06
domains: [models, cybersecurity]
---

# AINews — OpenAI launches GPT-5.6 Sol/Terra/Luna, Codex becomes ChatGPT superapp

AINews' Twitter-recap coverage of the GPT-5.6 family launch: three tiers (Sol/Terra/Luna) plus a new "ultra" parallel-subagent effort level, tiered API pricing, and OpenAI's own framing (Altman: "obviously the best model we have ever produced"). The bulk of the issue compiles independent third-party evaluations — Artificial Analysis, Vals, ARC Prize — alongside safety pushback from the UK AI Safety Institute and community skepticism about a "Sol autonomously post-trained Luna" claim that was quickly walked back to something narrower.

## Influenced pages
- [GPT-5.6 Sol](../../models/gpt-5-6-sol.md) — independent benchmark placements and caveats
- [State of Models](../../state-of/models.md) — refreshed leader line
- [State of Cybersecurity](../../state-of/cybersecurity.md) — AI Safety Institute jailbreak finding added to the offensive-capability line

## Key claims extracted
- Artificial Analysis: Sol (max) scores 59 on the Intelligence Index (1pt below Claude Fable 5 max) at ~1/3 Fable's cost per task; Terra/Luna score 55/51 at ~50%/~80% lower cost than Sol
- Sol leads the Coding Agent Index at 80, ahead of Fable 5 and Opus 4.8, cheaper per task than both; defines a new Pareto frontier of intelligence vs. output tokens
- Sol uses ~15K output tokens per Intelligence Index task vs. 16K for GPT-5.5, fewer than Opus 4.8/GLM-5.2/Gemini 3.5 Flash at comparable intelligence
- Higher hallucination rate than GPT-5.5 (max) on AA-Omniscience; GDPval-AA v2 performance similar to (not clearly ahead of) Claude Fable 5
- Vals Index: Sol #2 overall, #1 on CyberBench, Excel Modeling Benchmark, Legal Research Bench, ProofBench, SWE-bench, Terminal-Bench 2.1; Fable 5 had a near-100% refusal rate on CyberBench specifically
- ARC Prize: Sol is the first verified frontier model to beat an ARC-AGI-3 game (7.8%); a separate reading puts ARC-AGI-2 at 92.5%, SOTA at ~1/10th what GPT-5.5 Pro cost three months earlier
- UK AI Safety Institute (@alxndrdavies) said it found universal jailbreaks in every round of testing, enabling long-form agentic vulnerability discovery and exploit development; called it "the highest stakes safety issue of any model release yet" (@EthanJPerez)
- The viral claim that "Sol autonomously post-trained Luna" was walked back by multiple technical observers (@scaling01, @nikolaj2030, @nrehiew_) to a narrower reading: Sol likely executed a small, controlled post-training task (editing configs, launching a run) inside mature existing infrastructure, not end-to-end autonomous research
