---
title: Context editing
type: concept
domains: [agents]
tags: [agentic]
as_of: 2026-10-26
sources: [ainews-fal-h3-max-live-2026-09-01, ainews-openai-shuts-off-cursor-2026-08-29, tamaratran-fast-jev-compaction, protocol-preserving-context-trimming-2026-09]
---

# Context editing

Context editing is how an agent manages what stays in its context window while a task runs: replacing an ever-growing transcript with explicit state, pruning or summarizing old tool output, and deciding which edits to the context help the task. It works inside one session, which separates it from [agent memory](agent-memory.md) (knowledge kept between sessions) and from a [knowledge layer](knowledge-layer.md) (a compiled corpus shared across agents). The broader practice of assembling a model's context is context engineering, covered on [Harness (agent)](harness.md).

## Also called

In-loop context management, context pruning. Compaction names its most common step: shrinking the transcript when the window fills, by summary or by deletion.

## Current status (as of 2026-10-26)

- Late-August 2026 research moves context management inside the agent's working loop: explicit mutable state instead of growing transcripts (WikiSkill / SKILL.state), RL credit assigned to individual context edits (ContextPilot), and a Google DeepMind ablation where a persistent knowledge store compiled from traces carried much of the gain.
- Compaction is splitting into summary and deletion. Claude Code's built-in compaction summarizes; the public fast-jev-compaction plugin (October 2026) deletes stale tool calls instead, so whatever it keeps stays verbatim.

## Research and tools

- **Mutable state instead of growing transcripts.** WikiSkill / SKILL.state (Google DeepMind and collaborators) replaces ever-growing conversation histories with explicit mutable state plus persistent skill knowledge, reporting better long-horizon accuracy at lower cumulative token use.
- **Training agents to edit their own context.** Tencent's ContextPilot assigns RL reward at the level of specific context edits rather than final task outcome — a more targeted credit-assignment scheme for long-horizon tasks.
- **A persistent knowledge store carries much of the gain.** Google DeepMind researchers separated three layers: raw execution traces, a persistent accumulated-knowledge store (a "wiki"), and executable skills distilled from it. In ablation the store itself carried much of the measured gain, and the distilled skills transferred across model families, sometimes beating skills a model evolved for itself. That supports portable knowledge and skills over fine-tunes, which often fail to amortize when open base models change this fast. In the [Knowledge architectures](knowledge-architectures.md) vocabulary this store is closer to a [knowledge layer](knowledge-layer.md) than to per-agent episodic memory, though here the agent compiles it from its own traces.
- **Compaction by deletion instead of summary.** The public [fast-jev-compaction](../tools/fast-jev-compaction.md) plugin and npm package (October 2026) replaces Claude Code's compaction summary with pruning. It sends TypeSafe's [Jev](../models/jev.md) decision model the whole conversation, with tool results shortened to size notes, and gets two keep probabilities per tool call: is the call still worth knowing about, and is its output still needed word for word. Below the threshold the output is cut to its first 300 characters or the call is removed with its result. User and assistant text, the first message, and the newest messages are never touched, and everything kept stays verbatim, so the file paths, exact errors, and constraints a summary can lose survive. It falls back to the built-in summary when it cannot remove enough. The author's caveat: a keep probability is not proof a result is safe to delete, though the agent can re-run the tool.
- **Trim by protocol, not by recency.** A September 2026 paper compared five ways to trim an agent's context in multi-step tool workflows. Recency, relevance and summarization saved about 60% of tokens, but task success fell to 66.6–77.3%. Keeping protocol-critical state intact and compressing the rest reached 92.2%, and adding an adaptive budget guardrail reached 96.0% success with 56.0% token savings. Keeping 25% or less of the context raised the odds of failure 10.92-fold against keeping half or more, and complex workflows needed more of it.

## Related

- [Agent memory](agent-memory.md) — knowledge kept between sessions; this page covers what happens inside one
- [Harness (agent)](harness.md) — context engineering as part of harness design
- [Knowledge layer](knowledge-layer.md) — the shared compiled corpus the DeepMind knowledge store resembles
- [fast-jev-compaction](../tools/fast-jev-compaction.md) — the deletion-only compaction plugin

## Recent changes

- [2026-11-24] Page created, split out of [Agent memory](agent-memory.md): the "Context editing and persistent state" section and its Current-status bullet.
- [2026-10-26] Added deletion-only compaction ([fast-jev-compaction](../tools/fast-jev-compaction.md)): a decision model scores each tool call and result for keeping, and kept messages stay verbatim instead of being summarized.
- [2026-10-19] Added a "Context editing and persistent state" section (WikiSkill/SKILL.state, ContextPilot, Google's trace → knowledge-store → skill ablation), moved from [Harness (agent)](harness.md).
- [2026-09-15] Added protocol-preserving context trimming: keeping identifiers, constraints and open commitments intact beats recency and summarization trimming on task success at similar token savings.

## Sources

- [AINews — OpenAI shuts off Cursor](../sources/newsletters/ainews-openai-shuts-off-cursor-2026-08-29.md)
- [AINews — Fal's H3 Max Live breaks the infinite videogen barrier](../sources/newsletters/ainews-fal-h3-max-live-2026-09-01.md)
- [tamaratran/fast-jev-compaction (GitHub)](../sources/repos/tamaratran-fast-jev-compaction.md)
- [Protocol-Preserving Context Trimming for Agentic Workflows (arXiv)](../sources/papers/protocol-preserving-context-trimming-2026-09.md)
