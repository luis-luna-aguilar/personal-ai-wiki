---
title: Gemini
type: tool
domains: [models]
subcategory: ai-assistant
tags: [google, closed-source]
as_of: 2026-04-23
sources: [gemini-browser-utility-updates, gemini-deep-research-max, ainews-2026-04-22, google-cloud-next-2026]
---

# Gemini

Google's AI assistant product, built on the Gemini model family. Combines conversational AI, search, productivity features, and increasingly agentic research and workflow utilities across browser, desktop, API, and media-generation surfaces.

## Current status (as of 2026-04-23)

**Gemini Enterprise Agent Platform (Cloud Next '26):**

Google is now using Gemini as the umbrella brand over both assistant and enterprise agent surfaces. On the enterprise side, Gemini Enterprise Agent Platform replaces Vertex AI as the unified platform for building, scaling, governing, and optimizing agents.

*Build:*
- Agent Studio: low-code environment for building agents, with export to ADK for full-code customization
- Model Garden: 200+ models including Gemini 3.1 Pro, Gemini 3.1 Flash Image, Gemma 4, and Lyria 3
- Agent Garden: pre-built templates for code modernization, financial analysis, invoice processing, economic research, and more
- Agent Simulation: synthetic pre-ship testing with automatic scoring on task success and safety
- Workspace Intelligence GA: semantic layer over Docs, Sheets, Gmail, and Meet for agents
- Knowledge Catalog: Google's enterprise context layer for agent grounding
- Gemini Embedding 2 GA: unified embeddings across text, image, video, audio, and documents

*Scale:*
- Agent Runtime: sub-second cold starts with support for multi-day agent workflows
- Agent Memory Bank: long-term memory layer with Memory Profiles and custom session IDs that map to internal systems like CRMs
- Agent Sandbox: hardened environment for model-generated code execution and browser-based computer use
- Bidirectional streaming over WebSocket for low-latency audio/video agent interactions

*Govern and optimize:*
- Agent Identity, Agent Registry, and Agent Gateway position Google as a full enterprise control-plane vendor, not only a model provider
- Agent Anomaly Detection and Agent Threat Detection extend governance into runtime monitoring
- Agent Evaluation and Agent Optimizer bring live-traffic autorating, observability, and instruction refinement into the platform
- AP2 (Agent Payment Protocol) adds trusted payment flows to the stack

**Production deployments:**
- Comcast Xfinity: multi-agent customer support on ADK + Agent Runtime
- L'Oréal: MCP-connected multi-LLM agent stack tied to operational systems
- PayPal: AP2 payment flows
- Color Health: screening eligibility and appointment scheduling
- Payhawk: Financial Controller Agent with Memory Bank; 50%+ faster expense submission

**Other Gemini surfaces already tracked here:**
- Deep Research and Deep Research Max available via the Gemini API — see [[tools/gemini-deep-research]] for capabilities and benchmarks; see [[concepts/deep-research]] for the category
- Chrome Skills: reusable Gemini prompts that run as one-click browser workflows
- Native Gemini Mac app

## Strengths

- Deep Google ecosystem integration
- Google is vertically integrating chips, models, agent tooling, governance, and enterprise distribution
- Product cadence now spans both lightweight assistant features and heavyweight enterprise agent infrastructure

## Weaknesses / caveats

- Gemini is increasingly a brand spanning multiple distinct products; the current page now mixes assistant, research, API, and enterprise-platform layers more than is ideal
- Deep Research Max benchmark and quality claims here come from Google's own launch post
- Current page likely needs to split later into separate Gemini assistant, enterprise platform, and developer surfaces once source coverage is deeper

## Recent changes

- [2026-04-23] Cloud Next '26: Gemini Enterprise Agent Platform replaces Vertex AI; Agent Studio, 200+ models, Workspace Intelligence GA, Knowledge Catalog, Gemini Embedding 2 GA, and broader agent governance stack
- [2026-04-22] Added benchmark scores for Deep Research Max (93.3% DeepSearchQA, 85.9% BrowseComp, 54.6% HLE); added collaborative planning and code execution capabilities from AINews coverage
- [2026-04-21] Added Deep Research and Deep Research Max: Gemini API public preview, MCP support, multimodal grounding, and native visual reports
- [2026-04-21] Added Chrome Skills, Gemini 3.1 Flash TTS, and native Mac app
- [2026-04-10] Custom visualizations and notebooks features announced; rolling out to paid accounts

## Sources

- [[sources/newsletters/gemini-browser-utility-updates]]
- [[sources/articles/gemini-deep-research-max]]
- [[sources/articles/google-cloud-next-2026]]
