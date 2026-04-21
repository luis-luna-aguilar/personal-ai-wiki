---
title: Garry Tan on ambiguity gates / confusion protocol
type: source
source_type: tweet
source_file: raw/tweets/2026-04-21-garrytan-2044844654978642320.md
url: https://x.com/garrytan/status/2044844654978642320?s=12
published: 2026-04-21
ingested: 2026-04-21
domains: [agents, coding]
---

# Garry Tan on ambiguity gates / confusion protocol

Garry Tan's post is a compact articulation of a useful orchestration rule: when an agent reaches a genuinely ambiguous fork, the right behavior is to stop and ask rather than continue confidently down an unverified path. The point is not to confirm everything, but to add a targeted ambiguity gate where the cost of guessing wrong is high.

## Influenced pages

- [[workflows/agentic-orchestration-patterns]] — adds ambiguity gates as a reusable orchestration pattern
- [[concepts/harness]] — provides a concrete example of clarification logic as part of harness design

## Key claims extracted

- Published 2026-04-21
- A common AI coding failure mode is confidently choosing the wrong path at an ambiguous decision point
- An ambiguity gate should trigger only on costly forks, not on every step
- Architecture, data modeling, and destructive operations are examples of high-cost ambiguity points
