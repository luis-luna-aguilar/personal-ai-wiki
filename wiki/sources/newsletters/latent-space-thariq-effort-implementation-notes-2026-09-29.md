---
title: 'Latent Space — Thariq Shihipar on effort and implementation notes'
type: source
source_type: newsletter
source_file: raw/newsletters/2026-09-29-claude-codes-next-era-thariq-shihipar-anthropi.md
url: https://www.latent.space/p/thariq
published: 2026-09-29
ingested: 2026-10-20
domains: [coding]
---

# Latent Space — Thariq Shihipar on effort and implementation notes

The effort segment of Latent Space's interview with Anthropic's Thariq Shihipar ("Claude Code's next era"). He previews his effort blog post and adds a prompting tip the post does not carry: ask Claude for implementation or decision notes, because most failures he read in high-effort eval transcripts were cases where the model considered the correct solution and decided against it. The interview's other stories (Claude Mods, agent security, Pacing the Frontier) are covered by other source pages.

## Influenced pages

- [AI enablement — software development](../../training/ai-enablement-software-development.md) — implementation-notes tip in the effort bullet

## Key claims extracted

- Effort is mostly spent on verification and edge-case testing, so it changes security evals a lot and ordinary software engineering much less
- Spending more time on the initial prompt and context avoids expensive redo cycles that eat usage
- Most high-effort eval failures are the model considering the right fix and rejecting it; implementation notes let the user catch and reverse those decisions
- Thariq expects frontier models to become cheaper than small models on many simple tasks because they need less verification
