---
type: proposal
source: raw/newsletters/2026-06-01-why-video-agent-models-are-next-ethan-he-xai-gr.md
status: pending
created: 2026-06-24
---

# Proposal: Video agents as next frontier — LLM-first thesis from xAI's Grok Imagine lead

## Summary

Ethan He (built NVIDIA Cosmos world model, then built Grok Imagine from scratch at xAI in 3 months) argues that video model improvement is driven primarily by the LLM prompt-rewriter/planner component, not by diffusion model advances. The next frontier: "video agents" — LLMs calling video/image generation as a tool, iterating across a full creative task using FFmpeg, editing tools, and multiple generation passes. This mirrors the coding → coding agents arc. Grok Imagine Agent beta is the first public attempt.

## Intended changes

- [x] **Create** `wiki/trends/video-agents-next-frontier.md` — new trend page
    > See draft below

- [x] **Update** `wiki/state-of/creative.md` — add video agents to AI video generation subcategory; add Recent changes entry
    > **Update AI video generation section:**
    >
    > Add after existing Seedance 2.0 and Dream Machine entries:
    > `- **Grok Imagine Agent** — xAI; early beta; first public video agent implementation: LLM plans and iterates using video generation as a tool, calling FFmpeg and editing tools for post-processing; long-form video as a sequence of planned, generated, and edited clips *(as of 2026-06-01)*`
    >
    > **Add to Recent changes:**
    > `- [2026-06-01] Video agents thesis: Ethan He (ex-NVIDIA Cosmos, ex-xAI) argues video model intelligence comes from LLMs not video training; Grok Imagine Agent beta is first public video agent; evolution mirrors coding → coding agents`

- [x] **Create** `wiki/sources/newsletters/video-agents-ethan-he-june-2026.md` — source summary
    > See draft below

## Page drafts

### wiki/trends/video-agents-next-frontier.md (new)

````md
---
title: Video agents as next frontier
type: trend
domains: [creative]
tags: [agentic]
as_of: 2026-06-01
sources: [video-agents-ethan-he-june-2026]
---

# Video agents as next frontier

The thesis: the next major leap in AI video is not a better diffusion model — it's a better agent wrapping existing diffusion models. This mirrors the arc from coding to coding agents, and puts language model intelligence as the primary driver of video quality improvement.

## The core argument

Ethan He (built NVIDIA Cosmos, built Grok Imagine at xAI in 3 months from scratch):

> The visual intelligence in video models mostly comes from language. Video diffusion models are "kinda dumb" — they take instructions literally, generating exactly what's described in minimal detail. The prompt rewriter (a large language model) is what turns a simple user query into a detailed video spec. The intelligence is in the rewriter, not the renderer.

The evidence: in NVIDIA Cosmos, removing the LLM prompt rewriter made outputs CGI-looking and flat. Reintroducing it produced high-quality outputs — without any joint training between the LLM and the diffusion model.

**Implication:** video quality improvements over time are mostly improvements in the LLM layer, not in the video distribution model itself.

## The video agents arc

The evolution from coding tools to coding agents offers a predictive template:
1. GitHub Copilot: AI assists individual code steps
2. Codex / Claude Code: AI runs the full loop autonomously

The video equivalent:
1. Current video gen models: generate a clip from a prompt
2. Video agents: LLM plans a creative task, calls generation as a tool, iterates across multiple passes using editing software (FFmpeg, Photoshop APIs, video editors), and produces production-grade output

**Grok Imagine Agent beta** is the first public implementation in this direction: users can request long-form videos (not possible from a single generation pass); the agent calls multiple generation tools, stitches clips, and iterates.

## World model definition (Ethan He)

Real-time + interactive + long-horizon. This distinguishes a world model (used to simulate, plan, and act over time) from a video generator (produces a fixed clip from a prompt).

## Why it matters

- If most video quality gains are from LLM improvements rather than diffusion improvements, the competitive dynamics in video shift toward language model quality — where frontier labs (Anthropic, OpenAI, Google) have clearest advantages
- The "video agent" frame opens a new product category: creative task automation, not just clip generation
- Production-grade quality threshold (ads, broadcast) is the likely inflection point for enterprise video budgets to move

## What to watch

- Whether video agents reach the "diverge/converge" threshold where they generate production-usable output for ads and professional creative work
- Whether jointly-trained LLM+video models (Gemini Omni approach) beat separate rewriter+generator architectures at production quality
- Ethan He's next move: leaving xAI to work on LLM-side improvements (confirming he believes the leverage is in language, not video)

## Related

- [State of Creative](../state-of/creative.md) — video generation landscape
- [Harness (agent)](../concepts/harness.md) — the same "harness as competitive surface" argument applies to video agents

## Recent changes

- [2026-06-01] Created from Ethan He interview (ex-NVIDIA Cosmos, ex-xAI Grok Imagine); Grok Imagine Agent beta as first implementation

## Sources

- [Latent Space — "Why Video Agent Models Are Next" with Ethan He (June 1)](../sources/newsletters/video-agents-ethan-he-june-2026.md)
````

### wiki/sources/newsletters/video-agents-ethan-he-june-2026.md (new)

````md
---
title: '"Why Video Agent Models Are Next" — Ethan He on Latent Space (June 1)'
type: source
source_type: newsletter
source_file: raw/newsletters/2026-06-01-why-video-agent-models-are-next-ethan-he-xai-gr.md
published: 2026-06-01
ingested: 2026-06-24
domains: [creative, models]
---

# "Why Video Agent Models Are Next" — Ethan He on Latent Space (June 1)

Latent Space interview with Ethan He, who built NVIDIA Cosmos (world model) and then built Grok Imagine at xAI from scratch in 3 months. Covers the LLM-first intelligence thesis for video models, the video agents paradigm, world model definitions, and the technical architecture of diffusion + LLM prompt rewriting.

## Influenced pages

- [Video agents as next frontier](../../trends/video-agents-next-frontier.md) — new page
- [State of Creative](../../state-of/creative.md) — Grok Imagine Agent entry

## Key claims extracted

- LLM prompt rewriter is the primary intelligence source in video models, not the diffusion model itself
- Cosmos 7B video model + LLM rewriter (Llama/Mixtral) — rewriter is larger than the video model
- Video models take instructions literally and produce flat output without detailed LLM-generated specs
- World model = real-time + interactive + long-horizon (Ethan's definition)
- Grok Imagine 0.9: first large-scale audio-video joint generation model; Grok Imagine Agent beta: first video agent product
- Step distillation: 4-8 steps in production vs 100 during training
- Video agents will call diffusion as a tool, plus FFmpeg, editing software, etc. — same as how coding agents call compilers and tests
- "The next Sora won't be a better video model, it'll be a video agent"
- Ethan leaving xAI to work on LLMs, believing language model improvements are where video leverage actually lies
- Timeline: production-grade video agent quality (ads-ready) by end of 2026 (Ethan's prediction)
- SynthID/watermarking: increasingly reversible as models improve; regulatory pressure varies by country
````
