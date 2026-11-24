---
title: Cognition — Introducing Fusion in Devin Desktop & CLI
type: source
source_type: article
source_file: raw/articles/2026-11-23-cognitioncom-blog-local-fusion.md
url: https://cognition.com/blog/local-fusion
published: 2026-09-11
ingested: 2026-11-24
domains: [coding, agents]
---

# Cognition — Introducing Fusion in Devin Desktop & CLI

Cognition brings Fusion, its lead-plus-sidekick harness, from Devin Cloud to Devin Desktop and the CLI. The post reports benchmark savings measured with Artificial Analysis and Vals AI, explains why per-prompt model routing falls short, and argues that pricier models can make the pair cheaper per task. Its headline chart was updated on 2026-10-19.

## Influenced pages
- [Devin](../../tools/devin.md) — Fusion availability and current numbers
- [Cost-aware routing evidence](../../training/cost-aware-routing-evidence.md) — per-task vs per-token sidekick finding

## Key claims extracted
- The user picks a frontier lead (planning, ambiguity, review) and a cost-effective sidekick (exploration, implementation, tests). They exchange briefs, results and feedback, not whole conversations, and each keeps its own cached context.
- Artificial Analysis Coding Agent Index (updated 2026-10-19): Fusion with Opus 5.5 + GPT-6 Luna scores 68.1 at 31% lower cost than Claude Code with Opus 5.5 ($9.01 vs $13.04). Astra + SWE-2 runs 39% cheaper than Codex. The recommended pairing is Opus 5.5 + GPT-6 Luna.
- With SWE-2 as sidekick, cost savings against the lead alone: DeepSWE 1.1 −46% / −40%, Terminal-Bench 4.0 −23% / −40%, SWE-Atlas QnA −34% / −37%, Vals Code Migration −41% / −20%, FrontierCode 1.1 Extended −38% / −11% (Fable 5.1-led / Astra-led), at near-equal scores.
- Routing on the initial prompt fails because task difficulty is unknown until the code is investigated, and switching models mid-task breaks prompt caches.
- "Price per task rather than price per token": a GPT-5.6 Luna sidekick ($0.20/Mtok) scored 62.0 at $2.39 per task. A SWE-2 sidekick ($0.75/Mtok, +275%) scored 63.4 at $2.34 (−2%). Fable 5 as lead cost 9% less per session than Opus 4.8 at twice the token price.
- The harness is tuned per pair: how detailed briefs are, whether the sidekick may push back, and whether planning exploration is delegated.
