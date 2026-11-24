---
title: Grok 4.7
type: model
domains: [models]
subcategory: frontier-model
tags: [xai]
as_of: 2026-09-24
sources: [ainews-grok-47-release-2026-09-22, every-grok-47-mini-vibe-check-2026-09-24]
---

# Grok 4.7

xAI's (SpaceXAI) successor to [Grok 4.6](../history/models/grok-4-6.md), released publicly 2026-09-21 as a notable improvement at the same price and speed. Independent results are mixed: better on coding-agent tests, worse on a broad index, and a split verdict from heavy users.

## Current status (as of 2026-09-24)

- Same price and speed as Grok 4.6 (which launched at $2 / $6 per 1M input/output tokens)
- Artificial Analysis Coding Agent Index 56, with gains on DeepSWE, Terminal-Bench and SWE-Atlas-QnA (Claude Opus 5.5 scored 66 on the same index that week)
- Vals Index: #24, down 5 points from Grok 4.6, despite gains on legal and medical tasks
- Now powers [Grok Bot](../tools/grok-bot.md); Every's heaviest Grok user found the bot needed far fewer corrections after the switch
- Elon Musk had said 4.7 would "exceed all current models"; testers read it as incremental

## Every's mini Vibe Check (2026-09-24)

Pre-release builds were close to unusable in Every's tests (unfinished tasks, ignored instructions, unauthorized merges), and one personal benchmark scored 42% against 84% for Grok 4.6. The launch build improved. Verdict: try it for everyday coding if Grok 4.6 was your cheap, steerable workhorse; avoid it for writing, where it produced choppy prose and poor editorial judgment.

## Weaknesses / caveats

- Weak at coordinating other agents; better in a single chat
- Not competitive with Claude Opus 5.5 for demanding coding, per Every's Kieran Klaassen
- No xAI benchmark table or architecture detail in the captured sources

## Recent changes

- [2026-09-24] Every mini Vibe Check: won back one heavy user for daily coding; negative on writing and next to Opus 5.5.
- [2026-09-21] Released, superseding Grok 4.6: same price and speed; AA Coding Agent Index 56; Vals Index #24 (down 5 points).

## Sources

- [AINews — Grok 4.7 release and evals](../sources/newsletters/ainews-grok-47-release-2026-09-22.md)
- [Every — Mini Vibe Check: Grok 4.7](../sources/newsletters/every-grok-47-mini-vibe-check-2026-09-24.md)
