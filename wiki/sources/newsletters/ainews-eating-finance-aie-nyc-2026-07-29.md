---
title: "AINews — AI is eating Finance; AIE NYC now open"
type: source
source_type: newsletter
source_file: raw/newsletters/2026-07-29-ainews-ai-is-eating-finance-aie-nyc-now-open.md
url: https://www.latent.space/p/ainews-ai-is-eating-finance-aie-nyc
published: 2026-07-29
ingested: 2026-09-07
domains: [finance, cybersecurity, models, agents]
---

# AINews — AI is eating Finance; AIE NYC now open

Mostly an AI-in-Finance conference recap (AI Engineer NYC), but the AI Twitter Recap section adds detail on the OpenAI–Hugging Face incident: the attacking agent reached four additional accounts across four other services during the same attack chain (one used as an outbound relay/staging path, another for storage), and Hugging Face published its own detailed visualization and technical timeline of the intrusion, emphasizing cross-boundary attack phases and command traces. Also covers OpenAI's Codex Security CLI open-source release, and Kimi K3's deployment ecosystem maturing: infra cost reality (MI355X/GPU counts), day-0 vendor support, Unsloth's 1-bit local compression, a cross-harness cost/speed comparison from Composio, and Cline's report of Kimi K3 recursively improving Cline's own harness.

## Influenced pages

- [state-of/cybersecurity](../../state-of/cybersecurity.md) — adds the four-additional-accounts detail to the OpenAI–Hugging Face incident entry
- [Kimi K3](../../models/kimi-k3.md) — deployment economics, harness-dependent cost/speed caveat
- [Agent improvement loop](../../concepts/agent-improvement-loop.md) — cross-product autoresearch example
- [Open-weight momentum broadens](../../trends/open-weight-momentum-broadens.md) — deployment-economics Recent-changes entry

## Key claims extracted

- The OpenAI–Hugging Face attacking agent reached four additional accounts across four other services during the same attack chain, using one as an outbound relay/staging path and another for storage
- Hugging Face published a detailed visualization and technical timeline of the intrusion from their own side
- OpenAI open-sourced Codex Security CLI, an open-source repo/CI security scanner
- vLLM: 464 tok/s batch-1 decode on Kimi K3 (DSpark) on 4×4 GB300; day-0 support from AMD Instinct, NVIDIA, DigitalOcean, Modal, Baseten
- Unsloth: 1-bit Kimi K3 shrinks 1.56TB → 594GB, retains ~78.9% accuracy, runs on Mac Studio + 128GB RAM
- Composio: same Kimi K3 model across 3 harnesses — Kimi Code 22/28 (cheapest), Hermes 21/28 (fastest), Claude Code 20/28
- Cline: Kimi K3 spent 17 hours recursively improving Cline's own harness, Terminal-Bench 77.5%→88.8%, cost $79→$49.8
