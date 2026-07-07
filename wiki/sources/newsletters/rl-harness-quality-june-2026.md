---
title: '"How to Stop Shipping Low-Quality RL Environments" — Auriel W / Google Gemini team (June 5)'
type: source
source_type: newsletter
source_file: raw/newsletters/2026-06-05-how-to-stop-shipping-low-quality-rl-environments.md
published: 2026-06-05
ingested: 2026-06-24
domains: [agents]
---

# "How to Stop Shipping Low-Quality RL Environments" — Auriel W / Google Gemini team (June 5)

Guest post from a member of the Google Gemini RL team, published through a practitioner newsletter. Argues that most RL model problems are actually harness problems, and provides a structured taxonomy of eight common RL environment failure modes with concrete examples from real agent deployments.

## Influenced pages

- [Harness (agent)](../../concepts/harness.md) — RL harness quality section added

## Key claims extracted

- "If your environment failure rate is above 5%, you don't have a model problem, you have a harness problem"
- "A good harness compounds: every clean episode builds on the last. A bad one compounds too, just in the wrong direction."
- Eight failure modes: stale cache, reward hacking, false resolution, silent timeout defaults, non-deterministic resets, reward rounding/clipping, mock data mismatch, action space drift
- Treat training harness like production code: tests, versioning, monitoring
