---
title: 'Sparks of Weight-Space Programming — Takehi, Teoh, Zhang, Khattab'
type: source
source_type: article
source_file: raw/articles/2026-11-24-rikiyatgithubio-blog-weight-space-programming.md
url: https://rikiyat.github.io/blog/weight-space-programming/
ingested: 2026-11-24
domains: [models]
---

# Sparks of Weight-Space Programming — Takehi, Teoh, Zhang, Khattab

Research blog post by Rikiya Takehi, Jayden Teoh, Alex Zhang and Omar Khattab (described by Every as MIT researchers), arguing that frontier LLMs can natively read and write neural network weights. The post shows no publication date; a replication dated 3 November 2026 shows it was public by then, and a "Response to Comments" section was added on 12 November.

## The idea
Treat weights like code: read them to understand what a network computes, edit them to change it. The "programmer" is GPT-6 Astra working from a plain-language request, with no gradients and no training loops; some experiments allow a Python kernel and a small budget of forward passes. The authors call it a capability, not a method.

## Results
- **Read:** identified which game a small network was trained on from its weights; could not identify a sycophantic Gemma 3 270M from weights alone, but did from attention patterns on texts it wrote.
- **Fix:** edited 0.016% of Qwen3.5-0.8B's weights to remove its known thinking-loop fault; MATH-500 7.9% → 48.1%, IFEval about 3×, on held-out benchmarks. Could not improve Gemma 3 270M, which rarely loops.
- **Write:** small MinAtar game networks written from scratch outplayed PPO trained for 100M steps; a 1.5M-parameter Go network beat an equal-sized PPO network trained on 20M games when given 50 forward passes.
- Full logs and the edited Qwen model are public; replications and extensions (robot policies, quantum circuits, IWIBench) followed within days.

## Limits (authors' own)
- Capabilities are "exciting but still limited", mainly by context length and harnesses.
- Baselines test narrow claims, not a method ranking; no comparison with human interpretability researchers.

## Influenced pages
- [Weight-space programming](../../concepts/weight-space-programming.md) — new concept page
- [Agent improvement loop](../../concepts/agent-improvement-loop.md) — direct weight edits as an alternative to training runs

## Key claims extracted
- GPT-6 Astra edited 0.016% of Qwen3.5-0.8B's weights; MATH-500 7.9% → 48.1%
- No gradients or training loops were used
- Gemma 3 270M could not be improved; sycophancy not detectable from weights alone
- Weight-space programming is a concept and capability, not a method
