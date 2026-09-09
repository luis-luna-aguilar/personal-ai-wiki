---
title: Agent safety and alignment research
type: trend
domains: [agents]
tags: []
as_of: 2026-08-29
sources: [ainews-openai-shuts-off-cursor-2026-08-29]
---

# Agent safety and alignment research

The trend: as agents get more autonomous and more widely deployed, labs are publishing more research specifically aimed at measuring and improving agent-level alignment and safety, distinct from the cybersecurity attack-surface and incident-response content tracked on [State of Cybersecurity](../state-of/cybersecurity.md).

## Current signal

- **Anthropic: automated alignment research (August 2026):** Anthropic published results on Claude autonomously improving the alignment of smaller models over 48 hours on a single GPU, including a case where Sonnet 5 post-trained an early Opus 4.8 checkpoint to safety scores approaching production Opus. Anthropic explicitly caveats that this only works insofar as failures are measurable — subtle or rare failures may remain invisible to the benchmark. Anthropic also released the automated alignment research setup for others to build on.
- **Google DeepMind: double-blind frontier evals pilot (August 2026):** a pilot for double-blind evaluation of frontier AI, using a secure environment where neither test prompts nor model weights are revealed to either side — a procedural step toward making external evals possible without either party having full visibility into the other's assets.
- **EvoMal: shared skill libraries as malware-propagation channels:** a paper warns that shared agent-skill libraries can become self-poisoning malware-propagation channels for coding agents — a supply-chain-adjacent risk distinct from the traditional package-registry supply-chain attacks already tracked on [State of Cybersecurity](../state-of/cybersecurity.md).

## Why it matters

These three data points share a theme: as agent autonomy increases, both the *methods* for verifying agent safety (double-blind evals) and the *attack surface* introduced by agent-specific artifacts (shared skill libraries, self-improving alignment loops) are becoming distinct research areas in their own right, rather than being fully covered by traditional model-safety or cybersecurity framing.

## What to watch

- Whether Anthropic's automated-alignment-research setup gets adopted or replicated by other labs
- Results from Google DeepMind's double-blind evals pilot once concluded
- Whether EvoMal-style skill-library poisoning is observed in production rather than only described theoretically

## Recent changes

- [2026-08-29] Page created: Anthropic's automated alignment research (Claude improving smaller-model alignment in 48h/1 GPU), Google DeepMind's double-blind evals pilot, and the EvoMal skill-library malware-propagation warning.

## Related

- [State of Cybersecurity](../state-of/cybersecurity.md) — attack-surface, incident-response, and defensive-tooling coverage this page's research complements

## Sources

- [AINews — OpenAI shuts off Cursor](../sources/newsletters/ainews-openai-shuts-off-cursor-2026-08-29.md)
