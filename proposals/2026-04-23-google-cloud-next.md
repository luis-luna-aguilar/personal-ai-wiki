---
type: proposal
sources:
  - raw/newsletters/2026-04-23-openai-drops-a-privacy-focused-model.md
  - raw/newsletters/2026-04-23-ainews-tasteful-tokenmaxxing.md
  - raw/tweets/2026-04-23-googlecloud-2046995814019469538.md
  - raw/articles/2026-04-23-cloudgooglecom-blog-products-ai-machine-learning-introducing.md
status: pending
created: 2026-04-23
---

# Proposal: Google Cloud Next 2026 — TPU v8 + Gemini Enterprise Agent Platform

## Summary
Google's Cloud Next '26 announcements were substantial: TPU v8 (8t for training at ~3× Ironwood, 8i for inference at 1,152 TPUs/pod, scaling to 1M TPUs); Gemini Enterprise Agent Platform rebrands Vertex AI into an agent-first developer platform with Agent Studio, 200+ models, Workspace Intelligence GA, Knowledge Catalog, and Gemini Embedding 2 GA. Google is vertically integrating chips + models + agent tooling + enterprise control planes.

The full official blog post (fetched April 23) adds significant technical depth beyond the newsletter summaries: a full Build/Scale/Govern/Optimize framework covering Agent Memory Bank (Memory Profiles, custom session IDs), Agent Registry, Agent Gateway (Model Armor), Agent Anomaly Detection (LLM-as-judge), AP2 (Agent Payment Protocol), Agent Optimizer (auto-clusters failures + suggests improved system instructions), Agent Simulation (synthetic pre-ship testing), Agent Garden (pre-built templates), 6T tokens/month through ADK, graph-based multi-agent ADK networks, and Agent Identity (cryptographic per-agent ID). Production deployments confirmed at Comcast, L'Oréal, PayPal, Color Health, Payhawk, Burns & McDonnell, Geotab, and Gurunavi.

## Intended changes

- [x] **Update** `wiki/tools/gemini.md` — major update for Cloud Next announcements; add Gemini Enterprise Agent Platform, new models, Workspace Intelligence, Knowledge Catalog, Gemini Embedding 2; update as_of
- [x] **Update** `wiki/tools/google-adk.md` — note ADK is now part of Gemini Enterprise Agent Platform (Agent Studio); update framing
- [x] **Update** `wiki/trends/compute-infrastructure.md` — add TPU v8 specs; update as_of
- [x] **Update** `wiki/state-of/agents.md` — update Google ADK entry to reflect platform upgrade; prepend Recent changes entry
- [x] **Update** `wiki/state-of/models.md` — note Gemini 3.1 Pro and Gemma 4 under appropriate subcategory; prepend Recent changes entry
- [x] **Create** `wiki/sources/articles/google-cloud-next-2026.md` — source summary

## Open questions

- Should Knowledge Catalog get its own concept page? It's a novel product (no competitor equivalent announced at this scale) and could warrant a `concepts/knowledge-catalog.md` entry once more detail is available.
	- Create it as a tool, Gemini Enterprise's Knowledge Catalog
- The Gemini Enterprise Agent Platform replaces Vertex AI entirely — should `tools/google-adk.md` be renamed to `tools/gemini-enterprise-agent-platform.md`? For now, updating the existing page is safer.
	- No, Vertex was a superset name, this one also is, they are not specific tools.

## Page drafts

### wiki/tools/gemini.md (update — diff only)

> **Replace `## Current status (as of 2026-04-22)` block with:**
> ```markdown
> ## Current status (as of 2026-04-23)
>
> **Gemini Enterprise Agent Platform (Cloud Next '26):**
> Rebrands and replaces Vertex AI as the unified platform for building, scaling, governing, and optimizing agents at scale. Organized around four pillars:
>
> *Build:*
> - Agent Studio: low-code environment for building agents; seamlessly exports to ADK for full-code customization
> - ADK (Agent Development Kit): graph-based multi-agent framework (new); 6 trillion tokens/month processed through ADK; supports complex deterministic and generative orchestration patterns
> - Model Garden: access to 200+ models including Gemini 3.1 Pro, Gemini 3.1 Flash Image, Gemma 4, and Lyria 3
> - Agent Garden: pre-built agent templates (code modernization, financial analysis, invoice processing, economic research, and more) as immediate building blocks
> - Agent Simulation: test agents against synthetic user conversations and virtualized tools before shipping; agents auto-scored on task success and safety across multi-step conversations
> - Workspace Intelligence GA: semantic layer over Docs/Sheets/Gmail/Meet for agents
> - Knowledge Catalog: Google's purpose-built "universal context engine for enterprise"
> - Gemini Embedding 2 GA: unified embedding model across text, image, video, audio, and documents
>
> *Scale:*
> - Agent Runtime: sub-second cold starts; supports multi-day long-running agent workflows
> - Agent Memory Bank: dynamically generates and curates long-term memories from conversations; Memory Profiles for high-accuracy context recall; Custom Session IDs map directly to internal database and CRM records
> - Agent Sessions: persistent session management with custom identifier support
> - Agent Sandbox: hardened environment for model-generated code execution and browser-based computer use; isolated from host systems
> - Bidirectional Streaming via WebSocket for real-time low-latency audio/video agent interactions
>
> *Govern:*
> - Agent Identity: every agent receives a unique cryptographic ID with a clear auditable trail mapped to defined authorization policies
> - Agent Registry: central library of all approved agents, tools, and skills for discovery and governance
> - Agent Gateway: "air traffic control" for the agent ecosystem; enforces security policies and Model Armor protections against prompt injection and data leakage
> - Agent Anomaly Detection: statistical models + LLM-as-judge framework to flag unusual agent reasoning; alongside Agent Threat Detection for malicious activity (reverse shells, known-bad IPs)
> - Agent Security dashboard: Security Command Center integration; maps agent-to-model relationships, automates asset discovery, scans for OS and package vulnerabilities
> - AP2 (Agent Payment Protocol): trusted agent payment flows with step-by-step visibility into intent and payment mandate flows
>
> *Optimize:*
> - Agent Evaluation: continuously scores agents against live traffic using multi-turn autoraters; turnkey dashboards and trace-level Agent Observability
> - Agent Optimizer: automatically clusters real-world failures and suggests refined system instructions to improve accuracy — no manual log-digging required
>
> **Production deployments:**
> - Comcast Xfinity: multi-agent customer support replacing scripted automation; deployed on ADK + Agent Runtime
> - L'Oréal Beauty Tech: MCP-connected to their data platform and core operational applications; multi-LLM
> - PayPal: step-by-step visibility into payment intent via AP2
> - Color Health: breast cancer screening eligibility checking and appointment scheduling via Virtual Cancer Clinic
> - Payhawk Financial Controller Agent: auto-submits expenses using Memory Bank; 50%+ reduction in submission time
> - Burns & McDonnell: decades of project data turned into real-time intelligence via ADK
> - Geotab: Agent Center of Excellence built on ADK across multiple frameworks; accelerated build-test-deploy cycle
> - Gurunavi UMAME!: restaurant discovery with Memory Bank; anticipates preferences from past behavior; projected 30%+ improvement in user satisfaction
>
> **Infrastructure:**
> - API throughput: 16 billion tokens/minute
> - Security agents with Wiz integration
>
> **Deep Research (from prior coverage):**
> - Deep Research and Deep Research Max in paid public preview via Gemini API
> - Built on Gemini 3.1 Pro; benchmark scores (Max variant): 93.3% DeepSearchQA, 85.9% BrowseComp, 54.6% HLE
> - Capabilities: MCP support, multimodal inputs, code execution, collaborative planning, progress streaming
>
> **Other surfaces:**
> - Native charts and infographics generated inline in analytical reports
> - Chrome Skills: reusable Gemini prompts as one-click browser workflows
> - Native Gemini Mac app
> ```

> **Update `as_of` in frontmatter:** `as_of: 2026-04-23`

> **Add to `sources` frontmatter:** `google-cloud-next-2026`

> **Replace `## Recent changes` section:**
> ```markdown
> ## Recent changes
>
> - [2026-04-23] Cloud Next '26: Gemini Enterprise Agent Platform replaces Vertex AI; Agent Studio, 200+ models, Workspace Intelligence GA, Knowledge Catalog, Gemini Embedding 2 GA, 16B tokens/min API throughput
> - [2026-04-22] Added benchmark scores for Deep Research Max (93.3% DeepSearchQA, 85.9% BrowseComp, 54.6% HLE)
> - [2026-04-21] Added Deep Research and Deep Research Max: Gemini API public preview, MCP support, multimodal grounding
> - [2026-04-21] Added Chrome Skills, Gemini 3.1 Flash TTS, and native Mac app
> - [2026-04-10] Custom visualizations and notebooks features announced
> ```

### wiki/tools/google-adk.md (update — diff only)

> **Before** (Current status section):
> ```
> - Official Google framework for custom agent development
> - Open-source and documentation-led rather than hidden behind a hosted-only product
> - Positioned for multi-agent patterns, tool use, and production-oriented agent development
> ```
>
> **After:**
> ```
> - Official Google framework for custom agent development; now positioned as the open-source developer layer within the broader Gemini Enterprise Agent Platform (announced Cloud Next '26)
> - Agent Studio (part of Gemini Enterprise Agent Platform) provides a low-code wrapper over ADK primitives for teams that want a hosted UI rather than raw SDK
> - ADK now graph-based: agents can be organized into networks of sub-agents with clear, reliable logic for how they collaborate on complex problems; supports both deterministic and generative orchestration patterns
> - 6 trillion tokens/month are processed through ADK on Gemini models — confirming production scale
> - Open-source and documentation-led; the ADK layer itself remains available independently of the broader platform
> - Positioned for multi-agent patterns, tool use, and production-oriented agent development on Google infrastructure
> ```

> **Update `as_of`:** `as_of: 2026-04-23`

> **Add to `sources` frontmatter:** `google-cloud-next-2026`

### wiki/trends/compute-infrastructure.md (update — diff only)

> **Before** (Current status section, first bullet):
> `- Anthropic secured up to 5 GW of compute with Amazon alongside a $5B investment, with up to $20B more available`
>
> **After** (prepend Google TPU v8 bullet before Anthropic bullet):
> ```markdown
> - Google TPU v8 announced at Cloud Next '26: split into 8t (training, ~3× compute per pod vs TPU Ironwood) and 8i (inference, 1,152 TPUs/pod for low-latency multi-agent workloads); Google claims scalability to 1 million TPUs in a single cluster with 8t
> - Anthropic secured up to 5 GW of compute with Amazon alongside a $5B investment, with up to $20B more available
> ```

> **Add to `## Recent changes` (prepend):**
> `- [2026-04-23] Added Google TPU v8: 8t training (~3× Ironwood per pod), 8i inference (1,152 TPUs/pod); Google claims 1M-TPU single cluster — the hardware lead is widening`

> **Update `as_of`:** `as_of: 2026-04-23`

> **Add to `sources` frontmatter:** `google-cloud-next-2026`

### wiki/state-of/agents.md (update — diff only)

> **Before** (Agent frameworks section):
> `- [[tools/google-adk]] — Google's open-source Agent Development Kit for building and deploying custom agents; better treated as framework infrastructure than as an end-user assistant *(as of 2026-04-22)*`
>
> **After:**
> `- [[tools/google-adk]] — Google; open-source ADK now positioned as the developer layer inside the Gemini Enterprise Agent Platform; Agent Studio provides a low-code wrapper; 200+ models via Model Garden *(as of 2026-04-23)*`

> **Add to `## Recent changes` (prepend):**
> `- [2026-04-23] Google Cloud Next '26: Gemini Enterprise Agent Platform replaces Vertex AI; ADK absorbed into Agent Studio; Workspace Intelligence GA and Knowledge Catalog deepen enterprise integration`

### wiki/state-of/models.md (update — diff only)

> **Add to `## Recent changes` (prepend):**
> `- [2026-04-23] Google Cloud Next '26: Gemini 3.1 Pro, Gemini 3.1 Flash Image, Gemma 4, Lyria 3 surfaced as current active model stack within Gemini Enterprise Agent Platform; Gemini Embedding 2 GA across text/image/video/audio/doc`

### wiki/sources/articles/google-cloud-next-2026.md (new)

````md
---
title: Google Cloud Next 2026 — TPU v8 and Gemini Enterprise Agent Platform
type: source
source_type: article
source_file: raw/articles/2026-04-23-cloudgooglecom-blog-products-ai-machine-learning-introducing.md
url: https://cloud.google.com/blog/products/ai-machine-learning/introducing-gemini-enterprise-agent-platform
published: 2026-04-23
ingested: 2026-04-23
domains: [agents, models]
---

# Google Cloud Next 2026 — TPU v8 and Gemini Enterprise Agent Platform

Google's Cloud Next '26 announcements synthesized from: AINews (April 23), The Code newsletter (April 23), the official Gemini Enterprise Agent Platform blog post (fetched April 23), and a Google Cloud tweet. (1) TPU v8: split-design 8t (training) and 8i (inference) chips with substantial throughput gains. (2) Gemini Enterprise Agent Platform: Vertex AI's successor, with a full Build/Scale/Govern/Optimize framework for enterprise agents.

## Influenced pages

- [[tools/gemini]] — Gemini Enterprise Agent Platform full component details, new model stack, Knowledge Catalog, Workspace Intelligence, production deployments
- [[tools/google-adk]] — ADK now graph-based; 6T tokens/month; developer layer inside Agent Studio
- [[trends/compute-infrastructure]] — TPU v8 hardware specs
- [[state-of/agents]] — Google's enterprise agent platform upgrade

## Key claims extracted

**Infrastructure:**
- TPU 8t: ~3× compute per pod vs Ironwood; TPU 8i: 1,152 TPUs/pod; 1M-TPU single cluster
- API throughput: 16 billion tokens/minute

**Build:**
- Gemini Enterprise Agent Platform replaces Vertex AI; Agent Studio (low-code), Model Garden (200+ models)
- ADK now graph-based multi-agent; 6 trillion tokens/month processed through ADK
- Agent Garden: pre-built templates (code modernization, financial analysis, invoice processing)
- Agent Simulation: synthetic user conversations for pre-ship testing; auto-scored on task success and safety
- Active model stack: Gemini 3.1 Pro, Gemini 3.1 Flash Image, Gemma 4, Lyria 3

**Scale:**
- Agent Runtime: sub-second cold starts; multi-day long-running workflow support
- Agent Memory Bank: long-term memories from conversations; Memory Profiles; Custom Session IDs map to CRM
- Agent Sandbox: hardened environment for code execution and computer use

**Govern:**
- Agent Identity: unique cryptographic ID per agent with auditable trail
- Agent Registry: central catalog of all approved agents, tools, and skills
- Agent Gateway: "air traffic control" with Model Armor against prompt injection and data leakage
- Agent Anomaly Detection: statistical + LLM-as-judge for unusual reasoning
- AP2 (Agent Payment Protocol): trusted agent payment flows

**Optimize:**
- Agent Optimizer: auto-clusters real-world failures, suggests improved system instructions
- Agent Evaluation: multi-turn autoraters on live traffic; trace-level observability

**Production deployments:**
- Comcast Xfinity: multi-agent customer support on ADK + Agent Runtime
- L'Oréal: MCP-connected to data platform and operational apps; multi-LLM
- PayPal: AP2 for trusted agent payments
- Color Health: breast cancer screening eligibility and appointment scheduling
- Payhawk: Financial Controller Agent with Memory Bank; 50%+ faster expense submission
- Burns & McDonnell: decades of project data into real-time intelligence
- Geotab: Agent Center of Excellence across multiple frameworks
- Gurunavi UMAME!: restaurant discovery with Memory Bank; 30%+ projected UX improvement

**Context:**
- Workspace Intelligence GA: semantic layer over Docs/Sheets/Gmail/Meet
- Knowledge Catalog: universal context engine for enterprise agents
- Gemini Embedding 2 GA: unified embedding across text, image, video, audio, document
- Security agents with Wiz integration
````

## Comments

* Gemini as a tool has grown a lot in this wiki, and I think it is more like a brand now. We could have:
	- a Gemini desktop app
	- the Gemini enterprise service
	- the Gemini CLI
- We need to split them into separate products because they all have very different purposes, and we are putting them in one place, which is not appropriate