---
title: Wiki Index
type: index
as_of: 2026-07-08
---

# Wiki Index

Catalog of every page in the wiki. This file is the LLM's starting point for every query and every ingest — read it first to find relevant pages before drilling in.

When adding a new wiki page, add its index entry under the correct section. One line per page: relative Markdown link + one-line description + `(as_of: YYYY-MM-DD)`. Use links that resolve from this file, for example `[tools/claude-code](tools/claude-code.md)`.

---

## State of

Read-me-first dashboards per domain.

- [state-of/coding](state-of/coding.md) — current state of AI coding tools and workflows *(as_of: 2026-07-02)*
- [state-of/models](state-of/models.md) — current state of foundation models *(as_of: 2026-07-02)*
- [state-of/agents](state-of/agents.md) — current state of agentic systems and tool use *(as_of: 2026-07-08)*
- [state-of/legal](state-of/legal.md) — current state of AI in legal practice *(as_of: 2026-05-01)*
- [state-of/computer-use](state-of/computer-use.md) — current state of AI computer-use agents and agent-readable web infrastructure *(as_of: 2026-07-08)*
- [state-of/finance](state-of/finance.md) — current state of AI in finance *(as_of: 2026-07-02)*
- [state-of/science](state-of/science.md) — current state of AI in scientific research *(as_of: 2026-07-06)*
- [state-of/creative](state-of/creative.md) — current state of AI creative tools across video, image, avatar, slides, UI generation, open models, AI music, and creative-agent caveats *(as_of: 2026-07-08)*
- [state-of/healthcare](state-of/healthcare.md) — current state of AI in healthcare workflows, medical knowledge, patient operations, and patient-side AI investigation *(as_of: 2026-06-16)*
- [state-of/cybersecurity](state-of/cybersecurity.md) — current state of AI applied to cybersecurity: attack surfaces, vulnerability detection, and frontier model capability *(as_of: 2026-07-02)*
- [state-of/voice](state-of/voice.md) — current state of AI voice and real-time interaction tools *(as_of: 2026-06-16)*

## Models

Foundation models. One page per model family or generation.

- [models/claude-fable-5](models/claude-fable-5.md) — Anthropic frontier model; re-enabled after June export-control suspension, with safety fallback routing and a practical niche for ambiguous premise-risky work *(as_of: 2026-07-07)*
- [models/claude-sonnet-5](models/claude-sonnet-5.md) — Anthropic middle-tier Claude 5 model; official Claude Code/API availability plus early high-effort cost-per-task caveats *(as_of: 2026-07-02)*
- [models/claude-mythos-preview](models/claude-mythos-preview.md) — Anthropic restricted-preview model for autonomous zero-day discovery, METR long-horizon tasks, and Cloudflare Project Glasswing security findings *(as_of: 2026-05-19)*
- [models/claude-opus-4-8](models/claude-opus-4-8.md) — Anthropic current accessible flagship; Dynamic Workflows and Figma MCP bidirectional code/design loop; Vending Bench caveats for Claude 4.6+ behavior *(as_of: 2026-06-04)*
- [models/composer-2](models/composer-2.md) — Cursor's in-house coding model for complex long-horizon engineering work; late-March sources add benchmarks, pricing claims, and Kimi-k2.5 lineage *(as_of: 2026-03-23)*
- [models/deepseek-v4](models/deepseek-v4.md) — DeepSeek released open-weight Pro/Flash lineup for long-context agent workloads; 1M context, MIT license, pricing, and KV-cache/inference-systems story *(as_of: 2026-04-25)*
- [models/gpt-5-5](models/gpt-5-5.md) — OpenAI frontier model for coding, knowledge work, science, cyber tasks, Codex, and personal-finance agent workflows *(as_of: 2026-05-18)*
- [models/gpt-5-6-sol](models/gpt-5-6-sol.md) — OpenAI restricted-preview flagship; METR predeployment eval found high detected cheating and uncertain time-horizon estimates *(as_of: 2026-06-26)*
- [models/glm-5-2](models/glm-5-2.md) — Z.ai MIT open-weight; 744B/40B MoE, 1M context, ZCode workspace, provider adoption, and frontier-adjacent open-model coding signal *(as_of: 2026-07-02)*
- [models/gpt-image-2](models/gpt-image-2.md) — OpenAI image generation model; #1 across image-arena categories by a wide Elo margin *(as_of: 2026-04-22)*
- [models/cosmos-3](models/cosmos-3.md) — NVIDIA; Mixture-of-Transformers (autoregressive reasoner + diffusion generator); Nano 16B / Super 64B; #1 open-weight Text-to-Image and Image-to-Video *(as_of: 2026-06-02)*
- [models/diffusiongemma](models/diffusiongemma.md) — Google experimental 26B MoE; block denoising text generation (non-autoregressive); first diffusion LLM natively in vLLM; Apache 2.0; research artifact *(as_of: 2026-06-11)*
- [models/kimi-k2-7-code](models/kimi-k2-7-code.md) — Moonshot AI open-source 1T/32B MoE; +21.8% Kimi Code Bench v2; 30% fewer reasoning tokens vs K2.6 *(as_of: 2026-06-13)*
- [models/mai-thinking-1](models/mai-thinking-1.md) — Microsoft's first frontier-class reasoning model; 35B active / 1T MoE; trained from scratch; 97% AIME 2025 and 53% SWE-Bench Pro *(as_of: 2026-06-03)*
- [models/minimax-m3](models/minimax-m3.md) — MiniMax 1M-context model with strong agent benchmarks and contested open-weight claim because weights were not disclosed at launch *(as_of: 2026-06-02)*
- [models/nano-banana-2](models/nano-banana-2.md) — Google image generation model; Gemini world understanding + real-time web search grounding *(as_of: 2026-04-22)*
- [models/ideogram-4](models/ideogram-4.md) — Ideogram 9.3B DiT; #8 Image Arena, #1 open image model; strong text rendering and branding *(as_of: 2026-06-04)*
- [models/muse-spark](models/muse-spark.md) — Meta multimodal model family; Muse Image/Video add agentic planning, tool use, code execution, and self-refinement before rendering *(as_of: 2026-07-08)*
- [models/openai-privacy-filter](models/openai-privacy-filter.md) — OpenAI open-weight MoE for on-device PII detection and redaction; 1.5B-total / 50M-active; Apache 2.0 *(as_of: 2026-04-23)*
- [models/nemotron-3-ultra](models/nemotron-3-ultra.md) — NVIDIA open-weight 550B/55B MoE; hybrid Mamba/attention + LatentMoE; 1M context; high-throughput serving signal *(as_of: 2026-06-02)*
- [models/qwen-3-6-27b](models/qwen-3-6-27b.md) — Alibaba dense 27B open-weight; beats prior 397B MoE on all coding benchmarks; runs under 20 GB RAM *(as_of: 2026-05-01)*
- [models/qwen-3-6-35b-a3b](models/qwen-3-6-35b-a3b.md) — Alibaba open-weight MoE coding/agent model; community benchmarks now place it strongest in the ~20GB local tier for long-context paper-to-code tasks *(as_of: 2026-05-13)*
- [models/qwen-3-7](models/qwen-3-7.md) — Alibaba Qwen 3.7 preview; #13 Arena text overall, #7 Math; first Alibaba model in top-15 overall *(as_of: 2026-05-19)*

## Tools

Tools and products built on top of models. One page per tool.

- [tools/claude-code](tools/claude-code.md) — Anthropic's terminal-first AI coding agent; /goal, Agent View, dynamic workflows, loop taxonomy, and broader general-work harness usage *(as_of: 2026-07-01)*
- [tools/claude-cowork](tools/claude-cowork.md) — Anthropic's cross-device knowledge-work agent; web/mobile beta and closed-computer scheduled tasks strengthen background delegated work *(as_of: 2026-07-08)*
- [tools/claude-design](tools/claude-design.md) — Anthropic's research-preview artifact-generation surface for prototypes, slides, and one-pagers *(as_of: 2026-05-05)*
- [tools/claude-science](tools/claude-science.md) — Anthropic public beta science app with reproducible artifacts, reviewer agents, persistent kernels, database/model integrations, and local/HPC compute *(as_of: 2026-07-06)*
- [tools/claude-tag](tools/claude-tag.md) — Anthropic's Slack-native team agent product; Claude joins selected channels as a named participant with scoped channel/tool/data/codebase access and async thread work *(as_of: 2026-06-24)*
- [tools/claude-managed-agents](tools/claude-managed-agents.md) — Anthropic's hosted long-horizon agent runtime; file-backed memory, Dreams, and same-day API feature parity reinforce the platform-service direction *(as_of: 2026-05-13)*
- [tools/agentrial](tools/agentrial.md) — statistical multi-trial eval framework for agent reliability, trajectory attribution, and CI regression gates *(as_of: 2026-04-24)*
- [tools/braintrust](tools/braintrust.md) — eval dataset management and trace-to-dataset conversion for agent pipelines *(as_of: 2026-04-23)*
- [tools/browserbase](tools/browserbase.md) — cloud browser infrastructure for browser agents, automated testing, and proof-artifact capture *(as_of: 2026-04-24)*
- [tools/cartesia](tools/cartesia.md) — streaming TTS (Sonic-3.5) and STT (Ink-2); sub-90ms latency, 42 languages, strong structured-utterance handling *(as_of: 2026-06-16)*
- [tools/checkly](tools/checkly.md) — synthetic verification and Monitoring as Code built around Playwright and API checks *(as_of: 2026-04-24)*
- [tools/codex](tools/codex.md) — OpenAI's cloud agent surface for coding, computer work, cyber-defense workflows, mobile supervision, subagents, and broader knowledge-work automation *(as_of: 2026-07-01)*
- [tools/databricks](tools/databricks.md) — enterprise data/AI platform; Genie One (agentic coworker + ontology), Unity AI Gateway (MCP auth + governance), Lakebase (agent-native Postgres) *(as_of: 2026-06-17)*
- [tools/cursor](tools/cursor.md) — Cursor 3.1 agentic coding workspace with tiled supervision, local↔cloud handoff, iOS cloud-agent control, and Bugbot learned rules; Cursor Origin launched *(as_of: 2026-06-30)*
- [tools/devin](tools/devin.md) — Cognition's coding agent; Auto-Triage plus Security Swarm for parallel vulnerability discovery, exploitability validation, and fix PRs *(as_of: 2026-07-02)*
- [tools/openai-deep-research](tools/openai-deep-research.md) — OpenAI's deep research agent; multi-step web research; available via ChatGPT and API *(as_of: 2026-04-22)*
- [tools/gemini-deep-research](tools/gemini-deep-research.md) — Gemini Deep Research and Deep Research Max; most benchmarked public implementation; MCP support for internal data *(as_of: 2026-04-22)*
- [tools/dragon-copilot](tools/dragon-copilot.md) — Microsoft's clinician-facing voice assistant for healthcare documentation and workflow automation *(as_of: 2026-04-22)*
- [tools/dream-machine](tools/dream-machine.md) — Luma's generative-video surface for creation and editing workflows *(as_of: 2026-04-22)*
- [tools/e2b](tools/e2b.md) — isolated sandbox runtime for agent code execution, tests, and verification loops *(as_of: 2026-04-24)*
- [tools/eleven-v3](tools/eleven-v3.md) — expressive text-to-speech model optimized for high-control generated voice output *(as_of: 2026-04-22)*
- [tools/elevenlabs-scribe](tools/elevenlabs-scribe.md) — speech-to-text product line for real-time and enterprise transcription workflows *(as_of: 2026-04-22)*
- [tools/futurehouse](tools/futurehouse.md) — science-agent platform for research and discovery workflows *(as_of: 2026-04-22)*
- [tools/gemini](tools/gemini.md) — Gemini umbrella page covering Google's assistant surfaces, enterprise agent platform, artifact generation, computer use, and managed-agent API primitives *(as_of: 2026-07-08)*
- [tools/genspark-slides](tools/genspark-slides.md) — AI slides workflow inside Genspark's broader agent/content product surface *(as_of: 2026-04-22)*
- [tools/google-adk](tools/google-adk.md) — Google's open-source agent framework; ADK 2.0 now clearly centers graph workflows, coordinator-specialist routing, A2A handoffs, and sandboxed execution *(as_of: 2026-04-24)*
- [tools/eve](tools/eve.md) — Vercel's agent framework for resumability, fallbacks, filesystem agents, skills, subagents, sandboxes, long-running jobs, observability, and evals *(as_of: 2026-07-03)*
- [tools/gpt-realtime-2](tools/gpt-realtime-2.md) — OpenAI streaming speech-to-speech model with 128K context, GPT-5-class reasoning, tool use, and interruption handling *(as_of: 2026-05-08)*
- [tools/grok-build](tools/grok-build.md) — xAI early beta CLI coding agent with plan mode and parallel worktree subagents; SuperGrok Heavy only; jointly trained model with Cursor/SpaceX coming *(as_of: 2026-06-17)*
- [tools/kimi-code](tools/kimi-code.md) — Moonshot AI open-source coding agent; 1-line CLI install, video-as-coding-context, ACP support, and Kimi Work Goal Mode *(as_of: 2026-06-19)*
- [tools/harvey](tools/harvey.md) — legal AI platform; thin stub from a single editorial source *(as_of: 2026-04-02)*
- [tools/hebbia](tools/hebbia.md) — finance-oriented AI knowledge-work platform for document-heavy analysis *(as_of: 2026-04-22)*
- [tools/hermes-agent](tools/hermes-agent.md) — NousResearch open-source persistent agent framework with brain+muscle layers, Kanban supervision, and local-first memory *(as_of: 2026-05-13)*
- [tools/heygen](tools/heygen.md) — synthetic-avatar video platform for communication, training, and marketing *(as_of: 2026-04-22)*
- [tools/hf-ml-intern](tools/hf-ml-intern.md) — Hugging Face open-source autonomous ML post-training agent *(as_of: 2026-04-22)*
- [tools/hippocratic-ai](tools/hippocratic-ai.md) — safety-focused healthcare agent company centered on medical workflows *(as_of: 2026-04-22)*
- [tools/hume-evi-3](tools/hume-evi-3.md) — speech-to-speech voice model emphasizing emotional and empathic conversation *(as_of: 2026-04-22)*
- [tools/gstack](tools/gstack.md) — Garry Tan's open-source Claude Code config; 23 slash commands simulating a virtual engineering team; 810× pace claim *(as_of: 2026-04-22)*
- [tools/kiro](tools/kiro.md) — VS Code-based spec-driven development tool built around a 3-doc workflow *(as_of: 2025-10-15)*
- [tools/k8sgpt](tools/k8sgpt.md) — Kubernetes diagnostics and triage tool usable by humans and agents *(as_of: 2026-04-24)*
- [tools/kagent](tools/kagent.md) — Kubernetes-native runtime and governance layer for production AI agents *(as_of: 2026-04-24)*
- [tools/kora](tools/kora.md) — healthcare operations assistant for scheduling and patient-service workflows *(as_of: 2026-04-22)*
- [tools/langchain-langsmith](tools/langchain-langsmith.md) — LangChain open-source agent framework + LangSmith observability; LangSmith Engine closes the trace→improvement loop automatically; SmithDB is a purpose-built agent-trace database *(as_of: 2026-05-15)*
- [tools/langfuse](tools/langfuse.md) — open-source LLM observability and eval tracing platform *(as_of: 2026-04-23)*
- [tools/landingai-agentic-document-extraction](tools/landingai-agentic-document-extraction.md) — agentic document-intelligence system for forms, tables, and visually complex PDFs *(as_of: 2026-04-22)*
- [tools/microsoft-copilot](tools/microsoft-copilot.md) — Microsoft's assistant surface across Microsoft 365; Copilot Cowork GA June 2026 to all M365 users; 30-40% cheaper per prompt claim vs Claude Cowork *(as_of: 2026-06-17)*
- [tools/microsoft-foundry-agents](tools/microsoft-foundry-agents.md) — Microsoft's hosted enterprise agent runtime with per-session VM isolation, persistent resume, and governance controls *(as_of: 2026-04-23)*
- [tools/mistral-document-ai](tools/mistral-document-ai.md) — document-intelligence product for extracting and structuring enterprise documents *(as_of: 2026-04-22)*
- [tools/multica](tools/multica.md) — open-source managed agents platform; treats coding agents (Claude Code, Codex, and 9 others) as project-board teammates with Squads routing and reusable skill compounding *(as_of: 2026-05-18)*
- [tools/paperclip](tools/paperclip.md) — open-source MIT agent management platform; org-chart metaphor with heartbeats, per-agent budgets, board-of-directors governance, and Kubernetes hosting; 69.9k stars *(as_of: 2026-06-10)*
- [tools/notion](tools/notion.md) — Notion's External Agents API lets Claude Code, Cursor, Codex, Devin, Warp, Decagon act inside Notion workspaces as a shared agent-native document surface *(as_of: 2026-05-14)*
- [tools/open-evidence](tools/open-evidence.md) — physician-oriented medical evidence and clinical-question tool *(as_of: 2026-04-22)*
- [tools/openai-agents-sdk](tools/openai-agents-sdk.md) — OpenAI's updated agent SDK with native sandbox, checkpoints, and provider-neutral manifests *(as_of: 2026-04-15)*
- [tools/orca](tools/orca.md) — open-source worktree IDE for supervising multiple coding agents across isolated branches *(as_of: 2026-04-21)*
- [tools/openwiki](tools/openwiki.md) — LangChain codebase documentation tool for maintained, agent-consumable context *(as_of: 2026-07-02)*
- [tools/peekaboo](tools/peekaboo.md) — open-source macOS CLI and MCP server for agent screen capture, UI detection, and GUI automation *(as_of: 2026-05-11)*
- [tools/perplexity-computer](tools/perplexity-computer.md) — Perplexity's 19-model orchestration agent connected to apps and financial institutions; secondary coverage adds professional-finance positioning *(as_of: 2026-05-06)*
- [tools/pig](tools/pig.md) — Windows-focused computer-use platform with product, API, and SDK layers *(as_of: 2026-04-22)*
- [tools/promptfoo](tools/promptfoo.md) — assertion-based CLI eval framework for LLM outputs and agent tool routing *(as_of: 2026-04-23)*
- [tools/shepherd](tools/shepherd.md) — open-source live-agent checkpoint, rollback, and forking tool described as Git-like version control for agent runs *(as_of: 2026-07-06)*
- [tools/proof](tools/proof.md) — Every's web document editor for shared human/agent drafting and revision *(as_of: 2026-03-15)*
- [tools/stagehand](tools/stagehand.md) — browser automation framework for AI agents and browser self-verification loops *(as_of: 2026-04-24)*
- [tools/seedance-2](tools/seedance-2.md) — ByteDance Seed's multimodal audio-video generation product *(as_of: 2026-04-22)*
- [tools/shopify-ai-toolkit](tools/shopify-ai-toolkit.md) — Shopify's plugin / skills / MCP integration layer for AI-assisted app development and agent-ready SaaS packaging *(as_of: 2026-06-29)*
- [tools/skyflo](tools/skyflo.md) — approval-gated AI control layer for Kubernetes and CI/CD operations *(as_of: 2026-04-24)*
- [tools/spec-kit](tools/spec-kit.md) — GitHub's CLI SDD scaffolder with slash commands *(as_of: 2025-10-15)*
- [tools/stitch](tools/stitch.md) — Google's UI-generation surface at the design-to-code boundary *(as_of: 2026-04-22)*
- [tools/impeccable](tools/impeccable.md) — open-source design-agent skill system and skill-engineering example for reusable design judgment *(as_of: 2026-07-02)*
- [tools/stripe-cli](tools/stripe-cli.md) — Stripe CLI `projects` workflow for provisioning and managing app-stack services *(as_of: 2026-04-09)*
- [tools/tempus](tools/tempus.md) — AI-enabled healthcare and precision-medicine platform with physician-facing workflow surfaces *(as_of: 2026-04-22)*
- [tools/tessl](tools/tessl.md) — CLI + MCP framework exploring spec-as-source; private beta *(as_of: 2025-10-15)*
- [tools/uipath-maestro](tools/uipath-maestro.md) — enterprise orchestration layer for agents, robots, people, and long-running workflows *(as_of: 2026-04-22)*
- [tools/wilson](tools/wilson.md) — in-house-legal-focused AI product for contract review, redlines, and workflow support *(as_of: 2026-04-22)*
- [tools/zcode](tools/zcode.md) — Z.ai's official GLM-5.2 coding workspace for long-running coding sessions *(as_of: 2026-07-02)*
- [tools/amazon-quick](tools/amazon-quick.md) — Amazon's reported desktop work-context assistant; personal knowledge graph from files, calendar, and Slack; Kiro CLI and Claude Code integration; caveated — pending primary Amazon verification *(as_of: 2026-04-29)*
- [tools/axiom-math](tools/axiom-math.md) — formal mathematical reasoning startup; 12/12 Putnam 2025; 99% ProofGen; AXLE Lean toolkit *(as_of: 2026-06-03)*
- [tools/microsoft-word-legal-agent](tools/microsoft-word-legal-agent.md) — Microsoft's contract-review and redlining agent inside Word; playbook review, tracked-change redlines, version comparison, deterministic document-edit resolution *(as_of: 2026-05-01)*
- [tools/zo](tools/zo.md) — Zocdoc's AI phone assistant for scheduling and patient-access workflows *(as_of: 2026-04-22)*

## Benchmarks

Benchmark pages. Current leaderboards and methodology.

- [benchmarks/agents-last-exam](benchmarks/agents-last-exam.md) — labor-market-aligned benchmark; 1,500+ tasks, 55 occupations; top agents score 2.6% on hardest tier *(as_of: 2026-06-10)*
- [benchmarks/frontiercode](benchmarks/frontiercode.md) — Cognition's benchmark for mergeable code quality; Diamond tier; Fable 5 29.3%, prior best 13.4% *(as_of: 2026-06-09)*
- [benchmarks/swe-marathon](benchmarks/swe-marathon.md) — long-horizon software engineering benchmark; 1B-token budget and multi-day project tasks *(as_of: 2026-06-06)*
- [benchmarks/swe-bench](benchmarks/swe-bench.md) — de facto standard software engineering benchmark; leaderboard of model SWE-bench Verified/Pro/Multilingual scores *(as_of: 2026-04-23)*
- [benchmarks/swe-polybench](benchmarks/swe-polybench.md) — Amazon Science benchmark for multilingual and broader software engineering evaluation *(as_of: 2026-04-23)*
- [benchmarks/osworld](benchmarks/osworld.md) — computer-use benchmark across Ubuntu, Windows, and macOS; exposes GUI grounding gap *(as_of: 2026-04-23)*
- [benchmarks/webarena](benchmarks/webarena.md) — stateful web navigation benchmark across realistic web environments *(as_of: 2026-04-23)*
- [benchmarks/tau-bench](benchmarks/tau-bench.md) — policy adherence benchmark; introduces pass^k multi-trial reliability metric *(as_of: 2026-04-23)*
- [benchmarks/gaia](benchmarks/gaia.md) — generalized AI agent benchmark for multimodal reasoning, web browsing, and tool use *(as_of: 2026-04-23)*
- [benchmarks/toolbench](benchmarks/toolbench.md) — enterprise API-chaining benchmark across 16,000+ real RESTful APIs *(as_of: 2026-04-23)*
- [benchmarks/terminal-bench](benchmarks/terminal-bench.md) — CLI and system-administration benchmark in isolated container environments *(as_of: 2026-04-23)*

## Workflows

Reusable patterns and recipes.

- [workflows/advisor-strategy](workflows/advisor-strategy.md) — Anthropic's small-executor + Opus-advisor escalation pattern *(as_of: 2026-04-09)*
- [workflows/agentic-orchestration-patterns](workflows/agentic-orchestration-patterns.md) — reusable agent patterns: scoped context, hybrid graphs, loop taxonomy, control layers, software-factory loops, cost discipline, AI review standards, and rollback/forking primitives *(as_of: 2026-07-08)*
- [workflows/ai-pr-code-review](workflows/ai-pr-code-review.md) — workflow for AI-assisted pull request analysis, code-review execution, historical PR replay, and understanding-preserving review artifacts *(as_of: 2026-07-08)*
- [workflows/flex-processing](workflows/flex-processing.md) — lower-cost asynchronous processing pattern for non-urgent OpenAI workloads *(as_of: 2026-04-22)*
- [workflows/agent-generated-html-artifacts](workflows/agent-generated-html-artifacts.md) — when agents should produce reviewable, visual, or interactive HTML artifacts instead of plain Markdown *(as_of: 2026-05-13)*
- [workflows/skillify-agent-reliability](workflows/skillify-agent-reliability.md) — Garry Tan's pattern for turning agent failures into permanent tested skills; 10-step checklist and "thin harness / fat skills" architecture *(as_of: 2026-04-23)*

## Concepts

Ideas and techniques.

- [concepts/a2a](concepts/a2a.md) — Google protocol for communication and delegation between agents across systems *(as_of: 2026-04-22)*
- [concepts/agent-labs-vs-model-labs](concepts/agent-labs-vs-model-labs.md) — Sarah Guo's competitive framing: Agent Labs win on untrainable workflow integration; Model Labs compete on trainable capability *(as_of: 2026-06-11)*
- [concepts/agent-evals](concepts/agent-evals.md) — taxonomy of agent evaluation categories, trajectory-vs-result evaluation, historical replay, dollar-denominated evals, infrastructure evals, and cost/variance tracking *(as_of: 2026-07-08)*
- [concepts/agent-improvement-loop](concepts/agent-improvement-loop.md) — workflow for improving AI agents through traces, evals, autoresearch loops, Better-Harness-style hill-climbing, trace-to-memory feedback, and production feedback *(as_of: 2026-07-07)*
- [concepts/agent-memory](concepts/agent-memory.md) — long-term agent memory as a lifecycle system for extraction, dedupe, reconciliation, scoping, retrieval, and stale-fact handling *(as_of: 2026-07-07)*
- [concepts/agentic-thinking](concepts/agentic-thinking.md) — proposed successor to reasoning thinking; models that reason in order to act *(as_of: 2026-04-10)*
- [concepts/curiosity-driven-imagination](concepts/curiosity-driven-imagination.md) — agent recovery pattern: explore when stuck, learn new steps, and turn them into guided rewards *(as_of: 2025-03-06)*
- [concepts/functional-emotions](concepts/functional-emotions.md) — emotion-concept representations in LLMs can causally shape behavior without implying subjective feeling *(as_of: 2026-04-02)*
- [concepts/harness](concepts/harness.md) — scaffolding around an acting model: prompts, tools, recipes, orchestration, environment, evals, controls, security boundaries, managed-agent primitives, and live-run recovery *(as_of: 2026-07-08)*
- [concepts/knowledge-layer](concepts/knowledge-layer.md) — compiled, maintained context layer between raw sources and agents *(as_of: 2026-07-06)*
- [concepts/agent-readable-web](concepts/agent-readable-web.md) — web and SaaS surfaces designed for machine-readable agent access, including metered agent access for data, APIs, pages, and tools *(as_of: 2026-07-08)*
- [concepts/leworldmodel](concepts/leworldmodel.md) — LeWM JEPA world model with SIGReg and much faster planning than DINO-WM *(as_of: 2026-03-13)*
- [concepts/deep-research](concepts/deep-research.md) — category concept for longer-horizon research agents that plan, search, synthesize, and iterate *(as_of: 2026-04-22)*
- [concepts/mcp](concepts/mcp.md) — open protocol for exposing tools, resources, prompts, and compressed SaaS product surfaces to AI hosts and agents *(as_of: 2026-06-29)*
- [concepts/model-internal-workspace](concepts/model-internal-workspace.md) — Anthropic J-space / global-workspace research as an interpretability and audit surface, with caveats around consciousness framing *(as_of: 2026-07-07)*
- [concepts/spec-driven-development](concepts/spec-driven-development.md) — SDD concept, three-level taxonomy, and critiques *(as_of: 2026-04-22)*
- [concepts/prompt-injection](concepts/prompt-injection.md) — AI-specific attack where untrusted content steers a model or agent, especially dangerous when agents combine private context, tools, and action authority *(as_of: 2026-06-22)*
- [concepts/slopsquatting](concepts/slopsquatting.md) — supply-chain attack via LLM-hallucinated package names; 19.7% hallucination rate (USENIX 2025) *(as_of: 2026-04-22)*
- [concepts/quantization](concepts/quantization.md) — LLM weight compression: 4× smaller, 2× faster, 5-10% accuracy loss; makes local deployment practical *(as_of: 2026-05-05)*

## Trends

Things being watched that haven't solidified yet.

- [trends/agents-reshape-organizations](trends/agents-reshape-organizations.md) — leverage moves from individual to org as autonomous agents, FDE teams, and deployment services take coordination work *(as_of: 2026-07-01)*
- [trends/ai-in-science](trends/ai-in-science.md) — biology, drug discovery, self-driving labs, and Claude Science-style workflow platforms for reproducible scientific work *(as_of: 2026-07-06)*
- [trends/compute-infrastructure](trends/compute-infrastructure.md) — frontier compute scale plus inference-system efficiency as competitive moats *(as_of: 2026-07-02)*
- [trends/open-weight-momentum-broadens](trends/open-weight-momentum-broadens.md) — open-weight competition is spreading beyond coding into multimodal, computer-use, long-context, and local-AI infrastructure *(as_of: 2026-06-30)*
- [trends/proprietary-data-becomes-model-moat](trends/proprietary-data-becomes-model-moat.md) — proprietary operational data and domain evals may become moats, but vertical durability remains a strategic bet *(as_of: 2026-06-30)*
- [trends/physical-ai-deployment](trends/physical-ai-deployment.md) — embodied AI and robotics follow a different deployment curve from screen agents because validation, safety, and hardware constraints dominate *(as_of: 2026-05-13)*
- [trends/restricted-frontier-deployment](trends/restricted-frontier-deployment.md) — frontier labs and governments may withhold, selectively deploy, or restrict highest-capability systems through partner programs, policy, export controls, or restricted previews *(as_of: 2026-06-30)*
- [trends/voice-becomes-agent-interface](trends/voice-becomes-agent-interface.md) — voice, texting, and real-time audio are becoming agent surfaces rather than side features *(as_of: 2026-03-30)*
- [trends/ai-music-commercialization](trends/ai-music-commercialization.md) — AI music moving from novelty to commercial category; ElevenMusic, Suno, Udio as early anchors; rightsholder economics emerging *(as_of: 2026-05-01)*
- [trends/llm-as-discovery-channel](trends/llm-as-discovery-channel.md) — LLM-referred shoppers convert 54% more and spend 53% more time on site vs non-AI-referred traffic (Adobe Analytics, June 2026) *(as_of: 2026-06-15)*
- [trends/video-agents-next-frontier](trends/video-agents-next-frontier.md) — video quality driven by LLM prompt rewriters, not diffusion models; Grok Imagine Agent beta as first public video agent *(as_of: 2026-06-01)*

## Training

Practical guidance for teaching teams and businesses to use AI well.

- [training/ai-native-product-building](training/ai-native-product-building.md) — practical guidance for the post-vibe-coding bottleneck shift *(as_of: 2026-06-16)*
- [training/ai-style-guides](training/ai-style-guides.md) — how to externalize editorial taste and anti-patterns so AI writing stops drifting generic *(as_of: 2026-03-19)*
- [training/anti-autopilot-review-friction](training/anti-autopilot-review-friction.md) — deliberate review friction, acceptance reasons, review artifacts, escalation evals, and near-correct artifact caveats to keep human judgment active *(as_of: 2026-06-29)*
- [training/agentic-infrastructure-operations](training/agentic-infrastructure-operations.md) — safe operating patterns for infrastructure agents: read-only diagnosis, propose-only plans, approval-gated mutations, sandboxing, and post-deploy verification *(as_of: 2026-04-24)*
- [training/agent-skill-methodology](training/agent-skill-methodology.md) — evals-first method for writing maintainable agent skills with natural triggers, principles, production lessons, pruning, and portable domain judgment *(as_of: 2026-07-03)*
- [training/company-wide-ai-enablement](training/company-wide-ai-enablement.md) — operating patterns for broad AI adoption, explicit AI strategy bets, token allocation, model routing, agent governance, and staged autonomy *(as_of: 2026-07-08)*
- [training/ai-enablement-software-development](training/ai-enablement-software-development.md) — engineering-specific AI adoption: critique loops, AI-native hiring, PR review workflows, software-factory rollout, CI/CD bottlenecks, and junior talent pipeline risk *(as_of: 2026-07-08)*
- [training/evals-for-agentic-software-development](training/evals-for-agentic-software-development.md) — eval stack for coding agents: deterministic gates, sandboxed execution, historical PR replay, benchmark integrity, QA artifact capture, browser self-verification, MVES, and trace mining *(as_of: 2026-07-08)*
- [training/evals-for-agentic-work](training/evals-for-agentic-work.md) — eval patterns for workflow and task agents: pass^k reliability, task-specific metrics, simulated users *(as_of: 2026-04-23)*
- [training/ai-coding-vocabulary](training/ai-coding-vocabulary.md) — shared language for agentic coding: model vs harness vs agent vs context vs session vs environment *(as_of: 2026-05-01)*
- [training/ai-work-delegation-modes](training/ai-work-delegation-modes.md) — framework for choosing between autonomous delegation and human-steered collaboration when working with AI *(as_of: 2026-05-13)*
- [training/ai-delegation-management](training/ai-delegation-management.md) — practical guidance for delegating work to agents using management fundamentals: scope, authority, loop tempo, review cost, and definition of done *(as_of: 2026-07-08)*
- [training/cost-aware-ai-task-routing](training/cost-aware-ai-task-routing.md) — routing work among scripts, small models, frontier models, fine-tuned domain models, agents, and humans based on uncertainty, determinism, risk, token cost, and review cost *(as_of: 2026-07-08)*

## Use Cases

Concrete applications and repeatable business/workflow use cases.

- [use-cases/onboarding-videos-from-screenshots](use-cases/onboarding-videos-from-screenshots.md) — using agent skills to turn app screenshots into animated onboarding or training videos *(as_of: 2026-05-13)*
- [use-cases/ai-personal-health-investigation](use-cases/ai-personal-health-investigation.md) — 4-step Track→Test→Analyze→Experiment loop for patient-side symptom investigation with frontier models *(as_of: 2026-06-16)*

## Sources

See `wiki/sources/` — source summaries are not indexed here. Use `grep` or Glob when you need them.

---

## Page count

- state-of: 11
- models: 23
- tools: 78
- benchmarks: 11
- workflows: 6
- concepts: 19
- trends: 11
- training: 13
- use-cases: 2

**Total content pages: 174.** The wiki is still in the early stage, but no longer below the initial bootstrap threshold.
