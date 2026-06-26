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
