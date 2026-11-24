---
title: Claude Sonnet 5.5
type: model
domains: [models, coding]
subcategory: frontier-model
tags: [anthropic]
as_of: 2026-10-07
sources: [claude-sonnet-5-5-launch, claude-haiku-5-5-launch-2026-10-19, building-with-claude-sonnet-5-5-2026-09-28, claude-api-preserved-thinking-2026-09-29, ainews-claude-sonnet-5-5-launch-2026-09-29, ainews-sonnet-5-5-independent-evals-2026-09-30, every-vibe-check-sonnet-5-5-2026-09-28, ainews-claude-haiku-5-5-2026-10-08]
---

# Claude Sonnet 5.5

Anthropic's middle-tier Claude 5.5 model, launched 2026-09-28, superseding [Claude Sonnet 5](../history/models/claude-sonnet-5.md). It is the faster, cheaper complement to [Claude Opus 5.5](claude-opus-5-5.md): strongest at well-scoped everyday tasks, bug fixing, and polished documents, slides and spreadsheets, while Opus 5.5 stays clearly stronger on open-ended work that needs sustained judgment. It now powers the claude.ai free tier.

## Current status (as of 2026-10-07)

- Available on the Claude Platform as `claude-sonnet-5-5`, and on AWS (including Bedrock), Google Cloud and Microsoft Azure. 1M-token context; 128k max output (300k on the Batches API with a beta header). In Claude Code the `sonnet` alias resolves to it from v2.1.284, at medium effort; the default model stays Opus 5.5.
- Pricing per 1M tokens: $2 input, $10 output (same as Sonnet 5), $2.50 cache writes, $0.10 cache reads ($0.20 at launch). Anthropic says it costs up to 30% less per task than Sonnet 5 and outputs 30%+ faster, its fastest Sonnet yet.
- Launch benchmarks (Sonnet 5.5 / Sonnet 5 / Opus 5.5): Terminal-Bench 4.0 70.6% / 10.3% / 66.4%; CursorBench 4.0 55.5% / 34.1% / 57.8%; GDPval-AA v2.1 1844 / 1449 / 1846; OSWorld 2.1 80.1% / 57.0% / 81.8%. Anthropic says Sonnet 5.5 at Low or Medium effort beats Sonnet 5's best score on several benchmarks at about a tenth of the cost per task.
- Independent evals: #4 on Code Arena WebDev at 1699 (+159 over Sonnet 5); Vals finds it terser than Sonnet 5 on every paired task; Roboflow found it beat GPT-6 Sol on detection at 30% lower cost and 41% lower latency. In one planted-bug test, Sonnet 5.5 at max effort led with 55.5 but took about 6x GPT-6 Astra's turns.
- First Sonnet to launch with Opus-class cyber safeguards (higher-risk cyber tasks fall back to Sonnet 5) and anti-distillation classifiers; biology safeguards unchanged from Sonnet 5. Declines return `stop_reason: "refusal"` with one of five categories.

## Building with it

- **Thinking is always on.** `thinking: disabled` returns a 400 error. Use `between_tools` to skip upfront thinking; it works only at low, medium and high effort and fixes effort for the conversation. Read response blocks by type, since a response can start with a `thinking` block.
- **Breaking changes from Sonnet 5:** forced `tool_choice` (`any` or `tool`) returns a 400 (use `auto` with strict tools); computer use only through the new `computer_toolset_20260801`; Sonnet 5.5 rejects Opus 4.8, Opus 4.7 and Sonnet 5 as advisors, and advice comes back encrypted. `/claude-api migrate` in Claude Code applies the changes.
- **Defaults and tuning:** default effort is high on the API and medium in Claude Code; levels are recalibrated, so re-run effort sweeps. Minimum cacheable prompt is 512 tokens (Sonnet 5: 1,024). High-resolution images cost about 2.5x the tokens Sonnet 4.6 charged. Changing top-level effort between requests invalidates the cache.

## Preserved thinking

Anthropic extended its anti-distillation "preserved thinking" rules on 2026-09-29. Two separate checks apply:

- **Account binding.** Thinking blocks from Sonnet 5.5 and Haiku 5.5 work only in the account that produced them, or a linked one. Sent from another account, they are silently dropped and the model regenerates its reasoning.
- **Prefix check.** On Fable 5.1, Opus 5.5, Sonnet 5.5 and Haiku 5.5, a thinking block is valid only while the system prompt, tools and earlier messages are unchanged. Accounts created on or after 2026-08-31 get a 400 error by default; older accounts only when they opt in. The softer `drop_block` mode keeps requests running but, in Anthropic's tests, raises output tokens by up to 67% at max effort when blocks drop every turn.

The practical rule for any [harness](../concepts/harness.md): keep system and tools fixed per session and treat messages as append-only.

## Evidence from early users

- Base44: across 118 app builds, Sonnet 5.5 matched Opus 5's scores in 3.6 iterations per build against Opus 5's 7.7. Balyasny: about 121k tokens per finance answer against Sonnet 5's 497k.
- Every's Vibe Check: at low and medium effort it is a fast, cheap, responsive partner for prototyping, design and outlining you steer yourself. At high effort or left unattended it overbuilds, and Every's tests showed no consistent coding gain over Sonnet 5. Advice: start at medium and set a time or token budget.

## Recent changes

- [2026-10-07] Cache reads halved from $0.20 to $0.10 per 1M tokens, announced with Haiku 5.5; Anthropic says this makes Sonnet 5.5 about 20% cheaper on most agentic work.
- [2026-09-29] Preserved thinking extended: Sonnet 5.5 and Haiku 5.5 thinking blocks bound to the producing account; prefix check enforced by default for accounts created from 2026-08-31.
- [2026-09-28] Launched as the second Claude 5.5 model, superseding Sonnet 5; build guide lists breaking changes (thinking always on, no forced tool choice); powers the claude.ai free tier.

## Sources

- [Claude Sonnet 5.5 launch](../sources/articles/claude-sonnet-5-5-launch.md)
- [Claude Haiku 5.5 launch](../sources/articles/claude-haiku-5-5-launch-2026-10-19.md)
- [Building with Claude Sonnet 5.5](../sources/articles/building-with-claude-sonnet-5-5-2026-09-28.md)
- [Claude API docs — Preserved thinking](../sources/articles/claude-api-preserved-thinking-2026-09-29.md)
- [AINews — Claude Sonnet 5.5 launch and reactions](../sources/newsletters/ainews-claude-sonnet-5-5-launch-2026-09-29.md)
- [AINews — Sonnet 5.5 independent evals](../sources/newsletters/ainews-sonnet-5-5-independent-evals-2026-09-30.md)
- [Every — Vibe Check: Sonnet 5.5](../sources/newsletters/every-vibe-check-sonnet-5-5-2026-09-28.md)
- [AINews — Claude Haiku 5.5 launch and Artificial Analysis evals](../sources/newsletters/ainews-claude-haiku-5-5-2026-10-08.md)
