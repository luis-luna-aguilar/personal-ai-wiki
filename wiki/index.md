---
title: Wiki Index
type: index
as_of: 2026-04-24
---

# Wiki Index

Catalog of every page in the wiki. This file is the LLM's starting point for every query and every ingest — read it first to find relevant pages before drilling in.

When adding a new wiki page, add its index entry under the correct section. One line per page: wikilink + one-line description + `(as_of: YYYY-MM-DD)`.

---

## State of

Read-me-first dashboards per domain.

- [[state-of/coding]] — current state of AI coding tools and workflows *(as_of: 2026-04-22)*
- [[state-of/models]] — current state of foundation models *(as_of: 2026-04-23)*
- [[state-of/agents]] — current state of agentic systems and tool use *(as_of: 2026-04-23)*
- [[state-of/legal]] — current state of AI in legal practice *(as_of: 2026-04-22)*
- [[state-of/computer-use]] — current state of AI computer-use agents *(as_of: 2026-04-22)*
- [[state-of/finance]] — current state of AI in finance *(as_of: 2026-04-22)*
- [[state-of/science]] — current state of AI in scientific research *(as_of: 2026-04-23)*
- [[state-of/creative]] — current state of AI creative tools across video, avatar, slides, and UI generation *(as_of: 2026-04-22)*
- [[state-of/healthcare]] — current state of AI in healthcare workflows, medical knowledge, and patient operations *(as_of: 2026-04-22)*
- [[state-of/cybersecurity]] — current state of AI applied to cybersecurity: attack surfaces, vulnerability detection, and frontier model capability *(as_of: 2026-04-23)*
- [[state-of/voice]] — current state of AI voice tools: text-to-speech, speech-to-speech, and speech-to-text *(as_of: 2026-04-23)*

## Models

Foundation models. One page per model family or generation.

- [[models/claude-mythos-preview]] — Anthropic restricted-preview model; autonomous zero-day discovery; Project Glasswing; not publicly available *(as_of: 2026-04-22)*
- [[models/claude-opus-4-7]] — Anthropic flagship multimodal model; still strong on SWE-Bench Pro, MCP Atlas, and planning-heavy work despite new GPT-5.5 competition *(as_of: 2026-04-23)*
- [[models/composer-2]] — Cursor's in-house coding model for complex long-horizon engineering work; late-March sources add benchmarks, pricing claims, and Kimi-k2.5 lineage *(as_of: 2026-03-23)*
- [[models/deepseek-v4]] — DeepSeek preview release for long-context open agent workloads; 1M context, lower KV-cache cost, and competitive agent benchmark results *(as_of: 2026-04-24)*
- [[models/gpt-5-5]] — OpenAI frontier model for coding, knowledge work, science, and cyber tasks; GPT-5.4 now archived to history *(as_of: 2026-04-23)*
- [[models/glm-5-1]] — open-weight coding/agent model contender from the early-April open-model wave *(as_of: 2026-04-08)*
- [[models/gpt-image-2]] — OpenAI image generation model; #1 across image-arena categories by a wide Elo margin *(as_of: 2026-04-22)*
- [[models/kimi-k2-6]] — Moonshot AI open-weight 1T-param MoE; strong coding and agent benchmark claims *(as_of: 2026-04-21)*
- [[models/nano-banana-2]] — Google image generation model; Gemini world understanding + real-time web search grounding *(as_of: 2026-04-22)*
- [[models/minimax-m2-7]] — open-weight coding and agent model with unusually strong late-March cost/performance claims *(as_of: 2026-03-22)*
- [[models/muse-spark]] — Meta's new multimodal model; source emphasizes compute-efficient scaling *(as_of: 2026-04-10)*
- [[models/openai-privacy-filter]] — OpenAI open-weight MoE for on-device PII detection and redaction; 1.5B-total / 50M-active; Apache 2.0 *(as_of: 2026-04-23)*
- [[models/qwen-3-6-27b]] — Alibaba dense 27B open-weight; beats prior 397B MoE on all coding benchmarks; runs under 20 GB RAM *(as_of: 2026-04-23)*
- [[models/qwen-3-6-35b-a3b]] — Alibaba open-weight MoE coding/agent model; 24GB-class local baseline; benchmark lead now held by 27B dense sibling *(as_of: 2026-04-22)*

## Tools

Tools and products built on top of models. One page per tool.

- [[tools/claude-code]] — Anthropic's terminal-first AI coding agent; monitoring and routines push it toward supervised multi-session workflows *(as_of: 2026-04-22)*
- [[tools/claude-cowork]] — Anthropic's desktop knowledge-work agent; now also available in public research preview via Amazon Bedrock *(as_of: 2026-04-23)*
- [[tools/claude-design]] — Anthropic's research-preview artifact-generation surface for prototypes, slides, and one-pagers *(as_of: 2026-04-21)*
- [[tools/claude-managed-agents]] — Anthropic's hosted long-horizon agent runtime; now adds file-backed built-in memory with shared stores and enterprise audit controls *(as_of: 2026-04-24)*
- [[tools/agentrial]] — statistical multi-trial eval framework for agent reliability, trajectory attribution, and CI regression gates *(as_of: 2026-04-24)*
- [[tools/braintrust]] — eval dataset management and trace-to-dataset conversion for agent pipelines *(as_of: 2026-04-23)*
- [[tools/browserbase]] — cloud browser infrastructure for browser agents, automated testing, and proof-artifact capture *(as_of: 2026-04-24)*
- [[tools/checkly]] — synthetic verification and Monitoring as Code built around Playwright and API checks *(as_of: 2026-04-24)*
- [[tools/codex]] — OpenAI's cloud-based agent surface; still coding-first, but increasingly framed as a broader computer-work system for docs, browser flows, sheets, and repeatable tasks *(as_of: 2026-04-24)*
- [[tools/cursor]] — Cursor 3.1 agentic coding workspace with tiled supervision, local↔cloud handoff, and Bugbot learned rules *(as_of: 2026-04-14)*
- [[tools/openai-deep-research]] — OpenAI's deep research agent; multi-step web research; available via ChatGPT and API *(as_of: 2026-04-22)*
- [[tools/gemini-deep-research]] — Gemini Deep Research and Deep Research Max; most benchmarked public implementation; MCP support for internal data *(as_of: 2026-04-22)*
- [[tools/dragon-copilot]] — Microsoft's clinician-facing voice assistant for healthcare documentation and workflow automation *(as_of: 2026-04-22)*
- [[tools/dream-machine]] — Luma's generative-video surface for creation and editing workflows *(as_of: 2026-04-22)*
- [[tools/e2b]] — isolated sandbox runtime for agent code execution, tests, and verification loops *(as_of: 2026-04-24)*
- [[tools/eleven-v3]] — expressive text-to-speech model optimized for high-control generated voice output *(as_of: 2026-04-22)*
- [[tools/elevenlabs-scribe]] — speech-to-text product line for real-time and enterprise transcription workflows *(as_of: 2026-04-22)*
- [[tools/futurehouse]] — science-agent platform for research and discovery workflows *(as_of: 2026-04-22)*
- [[tools/gemini]] — Gemini umbrella page covering Google's assistant surfaces plus the new Gemini Enterprise Agent Platform *(as_of: 2026-04-23)*
- [[tools/genspark-slides]] — AI slides workflow inside Genspark's broader agent/content product surface *(as_of: 2026-04-22)*
- [[tools/google-adk]] — Google's open-source agent framework; ADK 2.0 now clearly centers graph workflows, coordinator-specialist routing, A2A handoffs, and sandboxed execution *(as_of: 2026-04-24)*
- [[tools/harvey]] — legal AI platform; thin stub from a single editorial source *(as_of: 2026-04-02)*
- [[tools/hebbia]] — finance-oriented AI knowledge-work platform for document-heavy analysis *(as_of: 2026-04-22)*
- [[tools/hermes-agent]] — NousResearch open-source agent framework with memory, replanning, and recursive agent patterns *(as_of: 2026-04-22)*
- [[tools/heygen]] — synthetic-avatar video platform for communication, training, and marketing *(as_of: 2026-04-22)*
- [[tools/hf-ml-intern]] — Hugging Face open-source autonomous ML post-training agent *(as_of: 2026-04-22)*
- [[tools/hippocratic-ai]] — safety-focused healthcare agent company centered on medical workflows *(as_of: 2026-04-22)*
- [[tools/hume-evi-3]] — speech-to-speech voice model emphasizing emotional and empathic conversation *(as_of: 2026-04-22)*
- [[tools/gstack]] — Garry Tan's open-source Claude Code config; 23 slash commands simulating a virtual engineering team; 810× pace claim *(as_of: 2026-04-22)*
- [[tools/kiro]] — VS Code-based spec-driven development tool built around a 3-doc workflow *(as_of: 2025-10-15)*
- [[tools/k8sgpt]] — Kubernetes diagnostics and triage tool usable by humans and agents *(as_of: 2026-04-24)*
- [[tools/kagent]] — Kubernetes-native runtime and governance layer for production AI agents *(as_of: 2026-04-24)*
- [[tools/kora]] — healthcare operations assistant for scheduling and patient-service workflows *(as_of: 2026-04-22)*
- [[tools/langfuse]] — open-source LLM observability and eval tracing platform *(as_of: 2026-04-23)*
- [[tools/landingai-agentic-document-extraction]] — agentic document-intelligence system for forms, tables, and visually complex PDFs *(as_of: 2026-04-22)*
- [[tools/microsoft-copilot]] — Microsoft's assistant surface across Microsoft 365; now agentic by default in Word, Excel, and PowerPoint *(as_of: 2026-04-22)*
- [[tools/microsoft-foundry-agents]] — Microsoft's hosted enterprise agent runtime with per-session VM isolation, persistent resume, and governance controls *(as_of: 2026-04-23)*
- [[tools/mistral-document-ai]] — document-intelligence product for extracting and structuring enterprise documents *(as_of: 2026-04-22)*
- [[tools/open-evidence]] — physician-oriented medical evidence and clinical-question tool *(as_of: 2026-04-22)*
- [[tools/openai-agents-sdk]] — OpenAI's updated agent SDK with native sandbox, checkpoints, and provider-neutral manifests *(as_of: 2026-04-15)*
- [[tools/orca]] — open-source worktree IDE for supervising multiple coding agents across isolated branches *(as_of: 2026-04-21)*
- [[tools/perplexity-computer]] — Perplexity's 19-model orchestration agent connected to apps and financial institutions *(as_of: 2026-04-10)*
- [[tools/pig]] — Windows-focused computer-use platform with product, API, and SDK layers *(as_of: 2026-04-22)*
- [[tools/promptfoo]] — assertion-based CLI eval framework for LLM outputs and agent tool routing *(as_of: 2026-04-23)*
- [[tools/proof]] — Every's web document editor for shared human/agent drafting and revision *(as_of: 2026-03-15)*
- [[tools/stagehand]] — browser automation framework for AI agents and browser self-verification loops *(as_of: 2026-04-24)*
- [[tools/seedance-2]] — ByteDance Seed's multimodal audio-video generation product *(as_of: 2026-04-22)*
- [[tools/shopify-ai-toolkit]] — Shopify's plugin / skills / MCP integration layer for AI-assisted app development *(as_of: 2026-04-10)*
- [[tools/skyflo]] — approval-gated AI control layer for Kubernetes and CI/CD operations *(as_of: 2026-04-24)*
- [[tools/spec-kit]] — GitHub's CLI SDD scaffolder with slash commands *(as_of: 2025-10-15)*
- [[tools/stitch]] — Google's UI-generation surface at the design-to-code boundary *(as_of: 2026-04-22)*
- [[tools/stripe-cli]] — Stripe CLI `projects` workflow for provisioning and managing app-stack services *(as_of: 2026-04-09)*
- [[tools/tempus]] — AI-enabled healthcare and precision-medicine platform with physician-facing workflow surfaces *(as_of: 2026-04-22)*
- [[tools/tessl]] — CLI + MCP framework exploring spec-as-source; private beta *(as_of: 2025-10-15)*
- [[tools/uipath-maestro]] — enterprise orchestration layer for agents, robots, people, and long-running workflows *(as_of: 2026-04-22)*
- [[tools/wilson]] — in-house-legal-focused AI product for contract review, redlines, and workflow support *(as_of: 2026-04-22)*
- [[tools/zo]] — Zocdoc's AI phone assistant for scheduling and patient-access workflows *(as_of: 2026-04-22)*

## Benchmarks

Benchmark pages. Current leaderboards and methodology.

- [[benchmarks/swe-bench]] — de facto standard software engineering benchmark; leaderboard of model SWE-bench Verified/Pro/Multilingual scores *(as_of: 2026-04-23)*
- [[benchmarks/swe-polybench]] — Amazon Science benchmark for multilingual and broader software engineering evaluation *(as_of: 2026-04-23)*
- [[benchmarks/osworld]] — computer-use benchmark across Ubuntu, Windows, and macOS; exposes GUI grounding gap *(as_of: 2026-04-23)*
- [[benchmarks/webarena]] — stateful web navigation benchmark across realistic web environments *(as_of: 2026-04-23)*
- [[benchmarks/tau-bench]] — policy adherence benchmark; introduces pass^k multi-trial reliability metric *(as_of: 2026-04-23)*
- [[benchmarks/gaia]] — generalized AI agent benchmark for multimodal reasoning, web browsing, and tool use *(as_of: 2026-04-23)*
- [[benchmarks/toolbench]] — enterprise API-chaining benchmark across 16,000+ real RESTful APIs *(as_of: 2026-04-23)*
- [[benchmarks/terminal-bench]] — CLI and system-administration benchmark in isolated container environments *(as_of: 2026-04-23)*

## Workflows

Reusable patterns and recipes.

- [[workflows/advisor-strategy]] — Anthropic's small-executor + Opus-advisor escalation pattern *(as_of: 2026-04-09)*
- [[workflows/agentic-orchestration-patterns]] — reusable patterns for multi-agent systems: ambiguity gates, scoped context, hybrid graphs, coordinator-specialist routing, and failure-aware replanning *(as_of: 2026-04-24)*
- [[workflows/flex-processing]] — lower-cost asynchronous processing pattern for non-urgent OpenAI workloads *(as_of: 2026-04-22)*
- [[workflows/skillify-agent-reliability]] — Garry Tan's pattern for turning agent failures into permanent tested skills; 10-step checklist and "thin harness / fat skills" architecture *(as_of: 2026-04-23)*

## Concepts

Ideas and techniques.

- [[concepts/a2a]] — Google protocol for communication and delegation between agents across systems *(as_of: 2026-04-22)*
- [[concepts/agent-evals]] — taxonomy of agent evaluation categories and the trajectory-vs-result distinction *(as_of: 2026-04-23)*
- [[concepts/agent-improvement-loop]] — trace-centered workflow for improving AI agents through tracing, evals, regression testing, and eval-suite upkeep *(as_of: 2026-04-24)*
- [[concepts/agent-memory]] — long-term agent memory as a retrieval-and-reasoning problem *(as_of: 2026-03-23)*
- [[concepts/agentic-thinking]] — proposed successor to reasoning thinking; models that reason in order to act *(as_of: 2026-04-10)*
- [[concepts/curiosity-driven-imagination]] — agent recovery pattern: explore when stuck, learn new steps, and turn them into guided rewards *(as_of: 2025-03-06)*
- [[concepts/functional-emotions]] — emotion-concept representations in LLMs can causally shape behavior without implying subjective feeling *(as_of: 2026-04-02)*
- [[concepts/harness]] — scaffolding that wraps a model into an acting agent: prompts, tools, orchestration, environment, evals *(as_of: 2026-04-21)*
- [[concepts/knowledge-layer]] — compiled, maintained context layer between raw sources and agents *(as_of: 2026-04-21)*
- [[concepts/leworldmodel]] — LeWM JEPA world model with SIGReg and much faster planning than DINO-WM *(as_of: 2026-03-13)*
- [[concepts/deep-research]] — category concept for longer-horizon research agents that plan, search, synthesize, and iterate *(as_of: 2026-04-22)*
- [[concepts/mcp]] — open protocol for exposing tools, resources, and prompts to AI hosts and agents; now with clearer local-vs-remote deployment guidance *(as_of: 2026-04-23)*
- [[concepts/spec-driven-development]] — SDD concept, three-level taxonomy, and critiques *(as_of: 2025-10-15)*
- [[concepts/slopsquatting]] — supply-chain attack via LLM-hallucinated package names; 19.7% hallucination rate (USENIX 2025) *(as_of: 2026-04-22)*
- [[concepts/quantization]] — LLM weight compression: 4× smaller, 2× faster, 5-10% accuracy loss; makes local deployment practical *(as_of: 2026-04-22)*

## Trends

Things being watched that haven't solidified yet.

- [[trends/agents-reshape-organizations]] — leverage moves from individual to org as autonomous agents take coordination work *(as_of: 2026-04-21)*
- [[trends/ai-in-science]] — biology and drug discovery provide the clearest current signal *(as_of: 2026-04-21)*
- [[trends/compute-infrastructure]] — frontier compute scale diverging across Anthropic/AWS and Google's TPU v8 push *(as_of: 2026-04-23)*
- [[trends/open-weight-momentum-broadens]] — open-weight competition is spreading beyond coding into multimodal, computer-use, and now more serious long-context agent systems *(as_of: 2026-04-24)*
- [[trends/proprietary-data-becomes-model-moat]] — proprietary operational data and domain evals may become stronger moats as model quality converges *(as_of: 2026-04-10)*
- [[trends/restricted-frontier-deployment]] — frontier labs may increasingly withhold or selectively deploy their highest-capability systems *(as_of: 2026-04-08)*
- [[trends/voice-becomes-agent-interface]] — voice, texting, and real-time audio are becoming agent surfaces rather than side features *(as_of: 2026-03-30)*

## Training

Practical guidance for teaching teams and businesses to use AI well.

- [[training/ai-native-product-building]] — practical guidance for the post-vibe-coding bottleneck shift *(as_of: 2026-03-23)*
- [[training/ai-style-guides]] — how to externalize editorial taste and anti-patterns so AI writing stops drifting generic *(as_of: 2026-03-19)*
- [[training/anti-autopilot-review-friction]] — deliberate review friction to stop fluent AI output from being accepted without independent judgment *(as_of: 2026-04-23)*
- [[training/agentic-infrastructure-operations]] — safe operating patterns for infrastructure agents: read-only diagnosis, propose-only plans, approval-gated mutations, sandboxing, and post-deploy verification *(as_of: 2026-04-24)*
- [[training/company-wide-ai-enablement]] — operating patterns for broad AI adoption, agent governance, and staged autonomy *(as_of: 2026-04-23)*
- [[training/ai-enablement-software-development]] — engineering-specific AI adoption: critique loops, AI-native hiring, CI/CD bottlenecks, and junior talent pipeline risk *(as_of: 2026-04-23)*
- [[training/evals-for-agentic-software-development]] — eval stack for coding agents: deterministic gates, sandboxed execution, QA artifact capture, browser self-verification, MVES, and trace mining *(as_of: 2026-04-24)*
- [[training/evals-for-agentic-work]] — eval patterns for workflow and task agents: pass^k reliability, task-specific metrics, simulated users *(as_of: 2026-04-23)*

## Sources

See `wiki/sources/` — source summaries are not indexed here. Use `grep` or Glob when you need them.

---

## Page count

- state-of: 11
- models: 14
- tools: 57
- benchmarks: 8
- workflows: 4
- concepts: 15
- trends: 7
- training: 8

**Total content pages: 124.** The wiki is still in the early stage, but no longer below the initial bootstrap threshold.
