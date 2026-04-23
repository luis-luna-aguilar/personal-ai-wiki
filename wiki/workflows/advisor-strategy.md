---
title: Advisor strategy
type: workflow
domains: [agents]
subcategory: agent-orchestration
tags: [anthropic, agentic]
as_of: 2026-04-09
sources: [advisor-strategy]
---

# Advisor strategy

A multi-model agentic pattern: a cheap *executor* (Sonnet or Haiku) runs the task end-to-end — calling tools, iterating — and consults a larger *advisor* (Opus) only when it hits a decision it can't reasonably solve. The advisor returns a plan, correction, or stop signal; it does not call tools and does not produce user-facing output.

Inverts the common sub-agent pattern where a large orchestrator decomposes work and delegates to smaller workers. Here the cheap model drives and frontier reasoning fires only at escalation points, keeping steady-state cost at executor level.

## Current status (as of 2026-04-09)

Shipped by Anthropic as `advisor_20260301`, a server-side tool on the Claude API — the first time a major lab has made escalation-on-demand a first-class API primitive rather than a pattern callers must build themselves. Declared in the `tools` array of a Messages request; handoff happens inside a single `/v1/messages` call with no extra round-trips. Executor and advisor tokens are billed at their respective rates and reported separately in `usage`. `max_uses` caps advisor calls per request. Works alongside other server-side tools (web search, code execution) in the same loop.

## Reported results (Anthropic internal evals)

Vendor numbers, no independent replication yet.

- **Sonnet + Opus-advisor** vs Sonnet alone on SWE-bench Multilingual: **+2.7%** score *and* **−11.9%** cost per task.
- **Haiku + Opus-advisor** on BrowseComp: **41.2%** vs Haiku solo **19.7%** (more than double).
- **Haiku + Opus-advisor** vs **Sonnet alone**: trails by 29 points, costs **85% less** per task — positioned as a strong option for high-volume work.
- Gains also reported on BrowseComp and Terminal-Bench 2.0 for Sonnet+Opus-advisor, specific numbers not quoted.

The Haiku-as-executor result is the most interesting data point: it opens a high-volume / bounded-intelligence niche that previously required a custom orchestrator.

## How it works

1. Start a Messages API request with a cheap executor (`claude-sonnet-4-6` or a Haiku build).
2. Declare the advisor tool:

   ```python
   {
       "type": "advisor_20260301",
       "name": "advisor",
       "model": "claude-opus-4-6",
       "max_uses": 3,
   }
   ```

3. The executor runs its loop; when it invokes `advisor`, the platform routes curated context to Opus, which returns a short plan (typically 400–700 tokens), and the executor resumes.

## Caveats

- Numbers are Anthropic's own evals on their own models. Treat as directional.
- Pattern quality depends on the executor recognising *when* it is stuck — metacognition is not separately benchmarked.
- The advisor cannot call tools. Guidance only — not a fallback for work the executor cannot *execute*, only for decisions it cannot *make*.
- Cost advantage shrinks if the executor over-invokes the advisor; `max_uses` is the only advertised ceiling.
- Tied to Anthropic's server-side tooling today. Multi-vendor advisor setups are still DIY.

## Related

- [[state-of/agents]]

## Recent changes

- [2026-04-09] First content for this page, from Anthropic's "The advisor strategy" launch post and the concurrent release of the `advisor_20260301` server-side tool.

## Sources

- [[sources/articles/advisor-strategy]]
