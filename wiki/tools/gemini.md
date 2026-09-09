---
title: Gemini
type: tool
domains: [models, computer-use, agents]
subcategory: ai-assistant
tags: [google, closed-source]
as_of: 2026-08-26
sources: [gemini-browser-utility-updates, gemini-deep-research-max, ainews-2026-04-22, google-cloud-next-2026, gemini-downloadable-files-2026-04-30, gemini-computer-use-aside-2026-06, gemini-managed-agents-2026-07, google-io-2026-search-blog, ainews-google-io-2026, gemini-personal-agent-superhuman-2026-05, ainews-death-of-params-glm-53-2026-08-20, sundarpichai-gemini-35-transcribe-2026-08-26]
---

# Gemini

Google's AI assistant product, built on the Gemini model family. Combines conversational AI, search, productivity features, and increasingly agentic research and workflow utilities across browser, desktop, API, and media-generation surfaces.

## Current status (as of 2026-07-08)

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

**Downloadable file generation (as of 2026-04-30):**
Gemini now generates downloadable artifacts directly from chat: Google Docs, Sheets, Slides; Microsoft Word, Excel, PowerPoint; PDF, CSV, LaTeX, TXT, RTF, and Markdown. File generation requires no external integration — output downloads inline from the conversation.

**Google I/O 2026 (as of 2026-05-19):**

Google used I/O 2026 to push Gemini toward "agents as the product." Key launches:

- **Gemini 3.5 Flash** went GA globally as the new default AI Mode model, positioned as Google's strongest agentic/coding Flash-tier model yet: 1M context, 65K max output, 4 thinking levels, and thought preservation across turns. Google-quoted benchmarks, as relayed by AINews (Google's launch post not fetched): Terminal-Bench 2.1 76.2%, GDPval-AA 1656 Elo, MCP Atlas 83.6%. Independent Artificial Analysis numbers (per AINews, 2026-05-20) are less flattering for a "Flash" model: Intelligence Index 55 (+9 vs Gemini 3 Flash) but 5.5x costlier than Gemini 3 Flash and 75% costlier than Gemini 3.1 Pro to run on AA's suite, at $1.50 / $9.00 per 1M input/output tokens; Arena placed it #9 overall text and #9 Code Arena: Frontend.
- **Antigravity 2.0**: Google's coding-agent stack expands to an agent-first desktop app (core conversations, artifacts, multi-agent orchestration), a CLI, and an SDK for orchestrating teams of coding agents. Google claims (per AINews) that a joint Antigravity + 3.5 Flash demo built a working OS in 12 hours using 93 parallel sub-agents, 15k+ model requests, and under $1K in API credits.
- **Gemini Spark**: a 24/7 personal background agent running on dedicated Google Cloud VMs that proactively handles Workspace tasks and checks in before major actions; local-device access is planned for summer 2026.
- **Search AI-Mode redesign**: Google's biggest Search-box upgrade in over 25 years — a reimagined, multimodal AI-Mode search box (text, images, files, videos, Chrome tabs), plus generative UI: Search uses Antigravity + Gemini 3.5 Flash to assemble custom layouts, visuals, and simulations on the fly, free for everyone this summer. Persistent mini-apps and dashboards for recurring tasks (e.g. a fitness tracker or a home-move planner) follow in the coming months, first for Google AI Pro/Ultra subscribers in the US. Persistent "information agents" (24/7 monitoring with synthesized updates and the ability to take action) roll out first to Pro/Ultra subscribers this summer; agentic booking expands to local services, including phone calls to businesses on the user's behalf (US, this summer).
- New subscription tier (per AINews): a $100/mo plan was added; Ultra was cut from $250 to $200/mo.

Reception was mixed (per AINews): positive on agentic gains, serving speed, and product integration; Artificial Analysis and several posters flagged the Flash-tier pricing/performance tradeoff and some benchmark caveats.

**Computer use (as of 2026-06-25):**
Gemini 3.5 Flash now has computer use as a built-in developer capability across browser, desktop, and mobile workflows. Newsletter coverage describes it as a standardized action interface exposed through the Gemini API, with human confirmation for sensitive actions and automatic shutdown when prompt-injection behavior is detected.

The significance is productization: Google is putting computer-use primitives into a mainstream Gemini model/API path rather than leaving them as a separate demo or bespoke agent environment.

**Managed agents in Gemini API (as of 2026-07-08):**

Google added hosted-agent primitives to the Gemini API: MCP support for direct access to internal tools and databases, background execution for long-running tasks, custom function calling, and credential refresh across interactions. AINews also describes the Gemini Interactions API as GA and the new default interface for Gemini models and agents, combining models, agents, async execution, tool support, multimodal generation, and managed execution surfaces.

**Other Gemini surfaces already tracked here:**
- Deep Research and Deep Research Max available via the Gemini API — see [Gemini Deep Research](gemini-deep-research.md) for capabilities and benchmarks; see [Deep Research (concept)](../concepts/deep-research.md) for the category
- Chrome Skills: reusable Gemini prompts that run as one-click browser workflows
- Native Gemini Mac app

**Gemini 3.7 Flash cost-efficiency (as of 2026-08-20):** ARC-AGI Prize reports 84.6% on ARC-AGI-2 at $0.25/task and 95.5% on ARC-AGI-1 at $0.12/task; Artificial Analysis separately places it #1 on its AA-AnalystAgent benchmark (spreadsheet/document-heavy quantitative tasks) at $0.54 average cost across 80 tasks — reinforcing its positioning as the "cheap and strong" option in its tier.

**Gemini 3.5 Transcribe (August 2026):** a speech-understanding model with multi-speaker intent detection, automatic 85+ language detection, and custom vocabulary adaptation for specialized jargon; available now via the Gemini API in Google AI Studio and Gemini Enterprise.

## Strengths

- Deep Google ecosystem integration
- Google is vertically integrating chips, models, agent tooling, governance, and enterprise distribution
- Product cadence now spans both lightweight assistant features and heavyweight enterprise agent infrastructure

## Weaknesses / caveats

- Gemini is increasingly a brand spanning multiple distinct products; the current page now mixes assistant, research, API, and enterprise-platform layers more than is ideal
- Deep Research Max benchmark and quality claims here come from Google's own launch post
- Current page likely needs to split later into separate Gemini assistant, enterprise platform, and developer surfaces once source coverage is deeper

## Recent changes

- [2026-08-26] Gemini 3.5 Transcribe launched: multi-speaker intent detection, 85+ languages auto-detected, custom vocabulary adaptation for specialized jargon; available via the Gemini API in Google AI Studio and Gemini Enterprise.
- [2026-08-20] Gemini 3.7 Flash posts strong cost-adjusted benchmarks: 84.6% ARC-AGI-2 at $0.25/task, 95.5% ARC-AGI-1 at $0.12/task, #1 on AA-AnalystAgent at $0.54/task average.
- [2026-07-08] Gemini API managed agents add MCP support, background execution, custom function calling, and credential refresh; AINews frames Interactions API as Google's default stateful interface for models and agents.
- [2026-06-25] Gemini 3.5 Flash adds built-in computer use for browser, desktop, and mobile with sensitive-action confirmations and prompt-injection shutdown behavior.
- [2026-05-19] Google I/O 2026: Gemini 3.5 Flash GA as the new AI Mode default (per AINews: Terminal-Bench 2.1 76.2%; AA flags Intelligence Index 55 but 5.5x costlier than Gemini 3 Flash), Antigravity 2.0 (desktop/CLI/SDK multi-agent coding orchestration), Gemini Spark (24/7 personal background agent on cloud VMs), and a Search AI-Mode redesign with generative UI, mini-apps, and persistent information agents.
- [2026-04-30] Downloadable file generation from chat: Google/Microsoft Office formats, PDF, CSV, LaTeX, TXT, RTF, Markdown — positions Gemini as an artifact-producing workplace assistant, not only conversational AI
- [2026-04-23] Cloud Next '26: Gemini Enterprise Agent Platform replaces Vertex AI; Agent Studio, 200+ models, Workspace Intelligence GA, Knowledge Catalog, Gemini Embedding 2 GA, and broader agent governance stack
- [2026-04-22] Added benchmark scores for Deep Research Max (93.3% DeepSearchQA, 85.9% BrowseComp, 54.6% HLE); added collaborative planning and code execution capabilities from AINews coverage
- [2026-04-21] Added Deep Research and Deep Research Max: Gemini API public preview, MCP support, multimodal grounding, and native visual reports
- [2026-04-21] Added Chrome Skills, Gemini 3.1 Flash TTS, and native Mac app

## Sources

- [Gemini browser and utility updates](../sources/newsletters/gemini-browser-utility-updates.md)
- [Gemini Deep Research and Deep Research Max launch](../sources/articles/gemini-deep-research-max.md)
- [AINews — 2026-04-22 (GPT-Image-2, Hermes, Deep Research Max)](../sources/newsletters/ainews-2026-04-22.md)
- [Google Cloud Next 2026 — TPU v8 and Gemini Enterprise Agent Platform](../sources/articles/google-cloud-next-2026.md)
- [Gemini downloadable file generation](../sources/newsletters/gemini-downloadable-files-2026-04-30.md)
- [Gemini computer use and Aside agentic browser](../sources/newsletters/gemini-computer-use-aside-2026-06.md)
- [Gemini managed agents in the API](../sources/newsletters/gemini-managed-agents-2026-07.md)
- [Google I/O 2026 — AI agents and more (Search blog)](../sources/articles/google-io-2026-search-blog.md)
- [AINews — Google I/O 2026: Gemini 3.5 Flash, Omni, Spark, Antigravity](../sources/newsletters/ainews-google-io-2026.md)
- [Superhuman — Gemini becomes your personal agent](../sources/newsletters/gemini-personal-agent-superhuman-2026-05.md)
- [AINews — Death of Params: Z.ai CEO Jie Tang on GLM 5.3](../sources/newsletters/ainews-death-of-params-glm-53-2026-08-20.md)
- [Sundar Pichai — Gemini 3.5 Transcribe](../sources/tweets/sundarpichai-gemini-35-transcribe-2026-08-26.md)
