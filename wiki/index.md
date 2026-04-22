---
title: Wiki Index
type: index
as_of: 2026-04-22
---

# Wiki Index

Catalog of every page in the wiki. This file is the LLM's starting point for every query and every ingest — read it first to find relevant pages before drilling in.

When adding a new wiki page (via a proposal), add its index entry under the correct section. One line per page: wikilink + one-line description + `(as_of: YYYY-MM-DD)`.

---

## State of

Read-me-first dashboards per domain.

- [[state-of/coding]] — current state of AI coding tools and workflows *(as_of: 2026-04-21)*
- [[state-of/models]] — current state of foundation models *(as_of: 2026-04-21)*
- [[state-of/agents]] — current state of agentic systems and tool use *(as_of: 2026-04-21)*
- [[state-of/legal]] — current state of AI in legal practice *(as_of: 2026-04-02)*
- [[state-of/computer-use]] — current state of AI computer-use agents *(as_of: 2026-04-10)*
- [[state-of/finance]] — current state of AI in finance *(as_of: 2026-04-10)*
- [[state-of/science]] — current state of AI in scientific research *(as_of: 2026-04-21)*

## Models

Foundation models. One page per model family or generation.

- [[models/claude-opus-4-7]] — Anthropic flagship multimodal model; stronger on explicit coding, document, and visual artifact tasks, but with reported reliability tradeoffs *(as_of: 2026-04-21)*
- [[models/composer-2]] — Cursor's in-house coding model for complex long-horizon engineering work; late-March sources add benchmarks, pricing claims, and Kimi-k2.5 lineage *(as_of: 2026-03-23)*
- [[models/gpt-5-4]] — OpenAI frontier model for reasoning, browsing, coding, and agent-style work; strong overall, but still not the clear winner on writing or design *(as_of: 2026-03-08)*
- [[models/glm-5-1]] — open-weight coding/agent model contender from the early-April open-model wave *(as_of: 2026-04-08)*
- [[models/kimi-k2-6]] — Moonshot AI open-weight 1T-param MoE; open-source SOTA coding/agent benchmark claims; 300-agent Claw Groups *(as_of: 2026-04-21)*
- [[models/minimax-m2-7]] — open-weight coding and agent model with unusually strong late-March cost/performance claims for tool-heavy work *(as_of: 2026-03-22)*
- [[models/muse-spark]] — Meta's new multimodal model; source emphasizes compute-efficient scaling vs prior Llama 4 Maverick generation *(as_of: 2026-04-10)*
- [[models/qwen-3-6-35b-a3b]] — Alibaba open-weight coding model; practical local-agent threshold on roughly 24GB-class hardware *(as_of: 2026-04-21)*

## Tools

Tools and products built on top of models. One page per tool.

- [[tools/claude-managed-agents]] — Anthropic's hosted long-horizon agent runtime concept built around decoupled session, harness, and sandbox abstractions *(as_of: 2026-04-15)*
- [[tools/claude-cowork]] — Anthropic's desktop knowledge-work agent; works across local files, folders, and workplace apps to complete repeatable multi-step tasks *(as_of: 2026-04-21)*
- [[tools/claude-design]] — Anthropic's research-preview artifact-generation surface for prototypes, slides, and one-pagers *(as_of: 2026-04-21)*
- [[tools/cursor]] — Cursor 3.1 agentic coding workspace; tiled Agents Window, branch-aware cloud-agent control, local↔cloud handoff, and Bugbot learned-rules loop for PR review *(as_of: 2026-04-14)*
- [[tools/harvey]] — legal AI platform; thin stub from a single editorial source *(as_of: 2026-04-02)*
- [[tools/kiro]] — VS Code-based SDD tool, 3-doc workflow *(as_of: 2025-10-15)*
- [[tools/spec-kit]] — GitHub's CLI SDD scaffolder with slash commands *(as_of: 2025-10-15)*
- [[tools/stripe-cli]] — Stripe CLI's developer-preview `projects` workflow for provisioning and managing app-stack services across providers *(as_of: 2026-04-09)*
- [[tools/shopify-ai-toolkit]] — Shopify's plugin / skills / MCP integration layer for AI-assisted Shopify app development *(as_of: 2026-04-10)*
- [[tools/tessl]] — CLI + MCP framework exploring spec-as-source; private beta *(as_of: 2025-10-15)*
- [[tools/perplexity-computer]] — Perplexity's 19-model orchestration agent; connects to 400+ apps and 12K+ financial institutions *(as_of: 2026-04-10)*
- [[tools/proof]] — Every's web document editor for shared human/agent drafting, revision, and document collaboration *(as_of: 2026-03-15)*
- [[tools/gemini]] — Google's AI assistant; custom visualizations, notebooks, Chrome Skills, Gemini 3.1 Flash TTS, and native Mac app *(as_of: 2026-04-21)*
- [[tools/claude-code]] — Anthropic's terminal-first AI coding agent; Monitor plus hosted routines push it toward supervised multi-session workflows *(as_of: 2026-04-21)*
- [[tools/codex]] — OpenAI's cloud-based coding agent via CLI and ChatGPT; increasingly framed around app use, memory, and repeatable ongoing tasks *(as_of: 2026-04-21)*
- [[tools/hermes-agent]] — NousResearch open-source agent framework; 100K+ stars; multi-layer memory, self-improving skills, stateless sub-agent parallelism *(as_of: 2026-04-21)*
- [[tools/openai-agents-sdk]] — OpenAI's updated agent SDK: model-native harness, native sandbox execution, durable checkpoint / rehydration, and provider-neutral manifests *(as_of: 2026-04-15)*
- [[tools/orca]] — open-source worktree IDE for supervising multiple coding agents across isolated branches, terminals, diffs, and review flows *(as_of: 2026-04-21)*

## Benchmarks

Benchmark pages. Current leaderboards and methodology.

_(empty)_

## Workflows

Reusable patterns and recipes.

- [[workflows/advisor-strategy]] — Anthropic's small-executor + Opus-advisor escalation pattern, now a server-side `advisor_20260301` tool on the Claude API *(as_of: 2026-04-09)*
- [[workflows/agentic-orchestration-patterns]] — reusable patterns for multi-agent systems: ambiguity gates, scoped context, failure-aware replanning, demos-over-memos, and eval-driven harness simplification *(as_of: 2026-04-21)*

## Concepts

Ideas and techniques (RAG, context engineering, compound engineering, etc.).

- [[concepts/agent-memory]] — long-term agent memory as a retrieval-and-reasoning problem, not only a vector-database problem *(as_of: 2026-03-23)*
- [[concepts/agent-improvement-loop]] — trace-centered workflow for improving AI agents through tracing, evals, review, and regression testing *(as_of: 2026-04-09)*
- [[concepts/functional-emotions]] — emotion-concept representations in LLMs can causally shape behavior without implying subjective feeling *(as_of: 2026-04-02)*
- [[concepts/harness]] — scaffolding that wraps a model into an acting agent; prompts, tools, orchestration, environment, evals *(as_of: 2026-04-21)*
- [[concepts/agentic-thinking]] — proposed successor to reasoning thinking; models that reason in order to act within environments *(as_of: 2026-04-10)*
- [[concepts/knowledge-layer]] — compiled, maintained context layer between raw sources and agents; distinct from naive retrieval over raw files *(as_of: 2026-04-21)*
- [[concepts/spec-driven-development]] — SDD concept, three-level taxonomy, critiques *(as_of: 2025-10-15)*
- [[concepts/curiosity-driven-imagination]] — agent recovery pattern: explore when stuck, learn new steps, and turn the steps into guided rewards *(as_of: 2025-03-06)*
- [[concepts/leworldmodel]] — LeWM: first JEPA to train end-to-end from pixels; SIGReg solves representation collapse; 15M params, 48x faster planning than DINO-WM *(as_of: 2026-03-13)*

## Trends

Things being watched that haven't solidified yet.

- [[trends/agents-reshape-organizations]] — leverage moves from individual to org as autonomous agents take coordination work *(as_of: 2026-04-21)*
- [[trends/ai-in-science]] — biology and drug discovery now provide the clearest current signal: Noetik and GPT-Rosalind *(as_of: 2026-04-21)*
- [[trends/compute-infrastructure]] — frontier compute scale diverging; Anthropic/AWS 5 GW deal as inflection point *(as_of: 2026-04-21)*
- [[trends/open-weight-momentum-broadens]] — open-weight competition is spreading beyond coding into multimodal and computer-use systems *(as_of: 2026-04-07)*
- [[trends/proprietary-data-becomes-model-moat]] — proprietary operational data, domain evals, and narrow training loops may become a stronger moat as model quality converges *(as_of: 2026-04-10)*
- [[trends/restricted-frontier-deployment]] — frontier labs may increasingly withhold or selectively deploy their highest-capability systems rather than ship them broadly *(as_of: 2026-04-08)*
- [[trends/voice-becomes-agent-interface]] — voice, texting, and real-time audio are becoming agent surfaces rather than side features *(as_of: 2026-03-30)*

## Training

Practical guidance for teaching teams and businesses to use AI well.

- [[training/ai-native-product-building]] — practical guidance for the post-vibe-coding bottleneck shift: reliability, debugging, distribution, and product judgment *(as_of: 2026-03-23)*
- [[training/ai-style-guides]] — how to externalize editorial taste and anti-patterns so AI writing stops drifting generic *(as_of: 2026-03-19)*
- [[training/anti-autopilot-review-friction]] — deliberate review friction to stop fluent AI output from being accepted without independent judgment *(as_of: 2026-04-21)*
- [[training/company-wide-ai-enablement]] — operating patterns for broad AI adoption: defaults, access, social proof, platform-plus-spokes org design, and workflow redesign around agents *(as_of: 2026-04-21)*

## Sources

See `wiki/sources/` — source summaries are not indexed here (they're many and cheap). Use `grep` or Glob when you need them.

---

## Page count

- state-of: 7 (6 populated, 1 skeleton)
- models: 8
- tools: 18
- benchmarks: 0
- workflows: 2
- concepts: 9
- trends: 7
- training: 4

**Total content pages: 55.** The wiki is still in the early stage, but no longer below the initial bootstrap threshold.
