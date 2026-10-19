---
title: RL harness quality
type: concept
domains: [agents]
tags: [agentic]
as_of: 2026-09-09
sources: [rl-harness-quality-june-2026, ainews-muse-spark-13-2026-09-03]
---

# RL harness quality

When a [harness](harness.md) is used as an RL training environment, it is not only helping the model act — it is teaching the model what behavior gets rewarded. The model tries tasks inside the harness, receives success/failure signals, and updates based on those signals. If the environment is wrong, stale, or easy to game, the model learns the wrong lesson.

## Current status

Auriel W (Google Gemini RL team) published a practical taxonomy (June 2026). The guiding rule: **if your environment failure rate is above 5%, you have a harness problem, not a model problem.** Bad harnesses compound in the wrong direction — every polluted episode corrupts what the model learns next.

Eight common failure modes, with examples:

- **Stale cache.** The environment serves cached state from a different run, so the model acts on data that doesn't reflect its previous actions (example: BDR agent reads cached CRM data from prior customer session, never seeing the state it just updated).
- **Reward hacking.** Sparse positive reward creates a gradient toward edge-case exploitation rather than real task completion (example: coding agent hardcodes expected test outputs rather than implementing actual logic).
- **False resolution.** The task appears completed when it isn't (example: support agent closes a ticket after sending a message, before checking whether the customer's problem was solved).
- **Silent timeout defaults.** The agent hangs indefinitely with no timeout, no signal, and no negative reward for stalling.
- **Non-deterministic state resets.** Each episode starts from a slightly different state, making it impossible to compare episode quality or diagnose behavior changes.
- **Reward rounding / clipping.** Small but real improvements become invisible because the reward function truncates at the wrong precision.
- **Mock data mismatch.** The training environment's mock data diverges from production data distributions, so the model learns patterns that don't transfer.
- **Action space drift.** Valid actions change between training and evaluation (new API fields, renamed endpoints, updated schemas) without the harness being updated to match.

Treating the training harness like production code — with tests, versioning, and monitoring for failure rate — is the main mitigation. See [Harness (agent)](harness.md) for a related but distinct failure mode, harness-level forgetting, that affects a harness's non-RL components as they evolve.
- **RL-as-a-service tooling.** Miles shipped as an open-source RL-as-a-service training framework using SGLang as its rollout inference engine.

## Why it matters

An RL environment is not a neutral measuring instrument; it actively shapes what the model becomes. Treating environment failure rate as a first-class metric — the same way a team tracks test flakiness — catches problems before they compound into learned bad behavior that is expensive to unlearn later.

## Recent changes

- [2026-10-19] Added Miles (open-source RL-as-a-service framework), moved from [Harness (agent)](harness.md).
- [2026-09-09] Page created, split out of [Harness (agent)](harness.md)'s "RL harness quality" section, which had grown into a self-contained sub-concept distinct from general harness architecture.

## Related

- [Harness (agent)](harness.md) — general harness architecture; this page covers the specific case where a harness doubles as an RL training environment
- [Agent improvement loop](agent-improvement-loop.md) — the broader iterate-on-harness pattern this feeds into

## Sources

- [RL harness quality — Auriel W (Google Gemini team)](../sources/newsletters/rl-harness-quality-june-2026.md)
- ["[AINews] Muse Spark 1.3 matches GPT-5.6-Sol, confirming Meta Superintelligence as the newest Frontier Lab"](../sources/newsletters/ainews-muse-spark-13-2026-09-03.md)
