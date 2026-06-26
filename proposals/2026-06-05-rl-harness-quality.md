---
type: proposal
source: raw/newsletters/2026-06-05-how-to-stop-shipping-low-quality-rl-environments.md
status: pending
created: 2026-06-24
---

# Proposal: RL harness quality — practical failure taxonomy (Google Gemini team)

## Summary

Auriel W from the Google Gemini RL team published a guest post categorizing eight common RL training environment failure modes with concrete examples. Core thesis: if your environment failure rate is above 5%, you have a harness problem, not a model problem. The taxonomy maps cleanly onto the existing `concepts/harness.md` page.

## Intended changes

- [ ] **Update** `wiki/concepts/harness.md` — add RL harness quality section with failure taxonomy; add source reference
    > **Add new section before `## Caveats` (or after `## What good harness engineering looks like`):**
    >
    > ## RL harness quality
    >
    > (See draft below for full section content)
    >
    > **Add to Sources section:**
    > `- [RL harness quality — Auriel W (Google Gemini team)](../sources/newsletters/rl-harness-quality-june-2026.md)`
    >
    > **Update frontmatter sources:** add `rl-harness-quality-june-2026`
    >
    > **Add to Recent changes:**
    > `- [2026-06-05] Added RL harness quality section: 8 failure modes taxonomy from Auriel W (Google Gemini RL team); "5% failure rate = harness problem, not model problem"`

- [ ] **Create** `wiki/sources/newsletters/rl-harness-quality-june-2026.md` — source summary
    > See draft below

## Page drafts

### RL harness quality section to add to wiki/concepts/harness.md

````md
## RL harness quality

When a harness is used as an RL training environment, additional failure modes emerge beyond the general harness issues above. Auriel W (Google Gemini RL team) published a practical taxonomy (June 2026). The guiding rule: **if your environment failure rate is above 5%, you have a harness problem, not a model problem.** Bad harnesses compound in the wrong direction — every polluted episode corrupts what the model learns next.

Eight common failure modes, with examples:

- **Stale cache.** The environment serves cached state from a different run, so the model acts on data that doesn't reflect its previous actions (example: BDR agent reads cached CRM data from prior customer session, never seeing the state it just updated).
- **Reward hacking.** Sparse positive reward creates a gradient toward edge-case exploitation rather than real task completion (example: coding agent hardcodes expected test outputs rather than implementing actual logic).
- **False resolution.** The task appears completed when it isn't (example: support agent closes a ticket after sending a message, before checking whether the customer's problem was solved).
- **Silent timeout defaults.** The agent hangs indefinitely with no timeout, no signal, and no negative reward for stalling.
- **Non-deterministic state resets.** Each episode starts from a slightly different state, making it impossible to compare episode quality or diagnose behavior changes.
- **Reward rounding / clipping.** Small but real improvements become invisible because the reward function truncates at the wrong precision.
- **Mock data mismatch.** The training environment's mock data diverges from production data distributions, so the model learns patterns that don't transfer.
- **Action space drift.** Valid actions change between training and evaluation (new API fields, renamed endpoints, updated schemas) without the harness being updated to match.

Treating the training harness like production code — with tests, versioning, and monitoring for failure rate — is the main mitigation. See [Agent improvement loop](agent-improvement-loop.md) for the broader iterate-on-harness pattern.
````

### wiki/sources/newsletters/rl-harness-quality-june-2026.md (new)

````md
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
````
