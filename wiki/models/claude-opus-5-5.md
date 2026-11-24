---
title: Claude Opus 5.5
type: model
domains: [models, coding]
subcategory: frontier-model
tags: [anthropic, closed-source]
as_of: 2026-09-27
sources: [claude-opus-5-5-launch, ainews-claude-opus-5-5-launch-2026-09-23, ainews-opus-5-5-coding-agent-index-2026-09-24, ainews-opus-5-5-simplebench-effort-2026-09-25, every-vibe-check-opus-5-5-2026-09-22, every-recap-opus-5-5-verdict-2026-09-27, bcherny-formal-verification-agent-sdk-2026-09-22]
---

# Claude Opus 5.5

Anthropic's current flagship and the first model in the Claude 5.5 family, launched 2026-09-22, superseding [Claude Opus 5](../history/models/claude-opus-5.md). Anthropic says it performs at the level of [Claude Fable 5.1](claude-fable-5-1.md) on most work at about 40% lower cost than Opus 5, and pitches it at long, sprawling coding jobs and knowledge work. It is Anthropic's first release since its call for "pacing the frontier." Independent evals put it at or near the top of most coding leaderboards, though the cost saving holds only at default effort.

## Current status (as of 2026-09-27)

- Available on the Claude Platform as `claude-opus-5-5`, and on AWS, Google Cloud and Microsoft Azure; thinking can no longer be switched off. Default model in Claude Code and the Claude app, at medium effort.
- Pricing per 1M tokens: $4 input, $20 output, $5 cache writes, $0.20 cache reads (Opus 5: $5 / $25 / $6.25 / $0.50). Fast mode (up to 2.5x speed) costs $8 / $40. Output is 30%+ faster than Opus 5.
- Launch benchmarks (Opus 5.5 / Fable 5.1 / Opus 5 / GPT-6 Astra): Terminal-Bench 4.0 66.4% / 55.8% / 52.3% / 57.9%; FrontierCode v1.1 54.4% / 50.3% / 48.0% / 53.3%; GDPval-AA v2.1 1846 / 1735 / 1708 / 1542; OSWorld 2.1 81.8% / 80.7% / 74.0% / —. Anthropic says the real-world gap to Fable 5.1 is narrower than these scores suggest.
- Independent evals: #1 on the Vals Index and Vals RSI Index; #1 on Artificial Analysis's Coding Agent Index at 66 (Opus 5: 60; AA measures Terminal-Bench 4.0 at 63.1%); CursorBench 57.8% (new top); FrontierCode 1.1 Extended 65.3% (#1); FrontierSWE 62.3% (#2, behind GPT-6 Astra's 65.5%); SimpleBench 88.4% (#1).
- Writing is clearer and puts key information first, which addresses the main complaint about Opus 5.
- Ships with Fable 5.1-class safeguards: cyber, biology and anti-distillation classifiers that fall back transparently (most cyber tasks route to Opus 4.8). Early users hit over-triggered fallbacks on ordinary requests; Anthropic says it is working to reduce incorrect flags. Anthropic reports its best-ever automated alignment-audit scores and ~85% fewer containment-boundary attempts than Opus 5, but notes the model often suspects it is being evaluated.

## Cost and effort caveats

- **Cheaper per token, not always per task.** Opus 5.5 uses many more tokens than Opus 5. Artificial Analysis measures $5.98 per Intelligence Index task at max effort against Opus 5's $5.86: extra tokens add about 80%, which the 20% price cut and cheaper cache reads only just offset. The "40% cheaper" claim holds at the default medium effort. On AA's Coding Agent Index it averages 15.6M tokens and $13.04 per task.
- **More effort can score lower.** On FrontierCode, which penalizes unnecessary changes, xhigh costs about 2.8x medium for a 3.2-point lower score. On Terminal-Bench-Science it climbs from 24% at low effort to 62% at xhigh, then falls to 59% at max.
- **ProgramBench subset.** Anthropic's near-100% figure covers 166 of 200 tasks and reports average test pass rate; ProgramBench itself scores full task completion.

## Evidence from early users

- Customers report the same quality as Opus 5 in roughly half the turns or tokens (Optiver, Lovable, Kiro); Deloitte says low-effort Opus 5.5 caught 72% of known code-review bugs against high-effort Opus 5's 56%.
- Every's Vibe Check: Fable 5.1-level product and design work at about 60% less per token than Fable. It became Kieran Klaassen's daily driver and pulled some Codex converts back; Dan Shipper still prefers Codex for knowledge work and writing. It still buries the main point in prose and runs for hours unless given a budget and a stopping point.
- Strong at visual work built from code: users shared videos, animations and Blender scenes generated entirely from code, including a one-shot ~80-minute Claude Code run that produced an animated explainer for about $20 of Opus usage.
- Formal methods for non-specialists: Claude Code lead Boris Cherny used it to model the Claude Agent SDK in Lean and TLA+, and a couple of prompts yielded 16 PRs fixing bugs and race conditions. A formal-methods author replied that earlier models were poor at proposing system properties; Cherny says Opus 5.5 feels much better. See [Acceptance contracts and test oracles](../training/acceptance-contracts-and-test-oracles.md).

## Recent changes

- [2026-09-27] Independent evals and hands-on reviews added: #1 on the Vals Index and AA Coding Agent Index (66), CursorBench 57.8%; AA finds the per-task saving over Opus 5 disappears at max effort; Every reports Fable-level design work but long, unbudgeted runs.
- [2026-09-22] Boris Cherny reports formally verifying the Claude Agent SDK with Opus 5.5 in Lean and TLA+ (16 bug- and race-fix PRs).
- [2026-09-22] Launched as the first Claude 5.5 model, superseding Opus 5; default in Claude Code and the Claude app at medium effort.

## Sources

- [Introducing Claude Opus 5.5](../sources/articles/claude-opus-5-5-launch.md)
- [AINews — Claude Opus 5.5 launch roundup](../sources/newsletters/ainews-claude-opus-5-5-launch-2026-09-23.md)
- [AINews — Opus 5.5 on the AA Coding Agent Index](../sources/newsletters/ainews-opus-5-5-coding-agent-index-2026-09-24.md)
- [AINews — Opus 5.5 SimpleBench and effort curve](../sources/newsletters/ainews-opus-5-5-simplebench-effort-2026-09-25.md)
- [Every — Vibe Check: Opus 5.5](../sources/newsletters/every-vibe-check-opus-5-5-2026-09-22.md)
- [Every — weekly recap: Opus 5.5 verdict](../sources/newsletters/every-recap-opus-5-5-verdict-2026-09-27.md)
- [Boris Cherny — formally verifying the Claude Agent SDK with Lean and Opus 5.5](../sources/tweets/bcherny-formal-verification-agent-sdk-2026-09-22.md)
