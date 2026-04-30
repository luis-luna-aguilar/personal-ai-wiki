---
title: GPT-Image-2
type: model
domains: [models]
subcategory: image-generation-model
tags: [openai, closed-source]
as_of: 2026-04-22
sources: [ainews-2026-04-22]
---

# GPT-Image-2

OpenAI's image generation model, launched April 22, 2026 as "ChatGPT Images 2.0." Available simultaneously in ChatGPT, the Codex CLI, and the public API as `gpt-image-2`. First-day #1 in all three Chatbot Arena image categories by a wide margin.

## Current status (as of 2026-04-22)

- #1 Elo in all image arena categories: 1512 text-to-image, 1513 single-image edit, 1464 multi-image edit
- +242 Elo gap over next competitor on text-to-image — displaces Gemini's Nano Banana 2 (Imagen)
- Capabilities: "thinking" mode (self-checks, generates multiple candidates before returning), web search integration for context, text rendering, multi-aspect-ratio layout, image editing, multilingual
- Day-0 ecosystem integrations: Figma, Canva, Hermes Agent, fal
- API access: `gpt-image-2` in the Images API; also surfaced inside Codex agent sessions

## Image as a coding-spec bridge

AINews's editorial framing: image generation is becoming a front end for coding agents. Generate a UI mock or design spec as an image → hand it to Codex, Claude Code, or another agent to implement. This bridges design intent and agentic execution without requiring Figma source files.

## Weaknesses / caveats

- Benchmark scores come from the Chatbot Arena (human preference), not task-accuracy evals — strong signal for perceived quality, weaker for programmatic output correctness
- Closed-source API only; no weights, no local deployment

## Recent changes

- [2026-04-22] Initial page — launched at #1 arena across all image categories

## Sources

- [AINews — 2026-04-22 (GPT-Image-2, Hermes, Deep Research Max)](../sources/newsletters/ainews-2026-04-22.md)
