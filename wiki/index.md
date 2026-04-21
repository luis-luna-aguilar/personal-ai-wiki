---
title: Wiki Index
type: index
as_of: 2026-04-21
---

# Wiki Index

Catalog of every page in the wiki. This file is the LLM's starting point for every query and every ingest — read it first to find relevant pages before drilling in.

When adding a new wiki page (via a proposal), add its index entry under the correct section. One line per page: wikilink + one-line description + `(as_of: YYYY-MM-DD)`.

---

## State of

Read-me-first dashboards per domain.

- [[state-of/coding]] — current state of AI coding tools and workflows *(as_of: 2026-04-10)*
- [[state-of/models]] — current state of foundation models *(as_of: 2026-04-21)*
- [[state-of/agents]] — current state of agentic systems and tool use *(as_of: 2026-04-21)*
- [[state-of/legal]] — current state of AI in legal practice *(as_of: 2026-04-02)*
- [[state-of/computer-use]] — current state of AI computer-use agents *(as_of: 2026-04-10)*
- [[state-of/finance]] — current state of AI in finance *(as_of: 2026-04-10)*
- [[state-of/science]] — current state of AI in scientific research *(as_of: 2026-04-10)*

## Models

Foundation models. One page per model family or generation.

- [[models/claude-opus-4-7]] — Anthropic flagship multimodal model; #1 Vision & Document Arena; wins in diagram, homework, and OCR *(as_of: 2026-04-21)*
- [[models/composer-2]] — Cursor's in-house frontier coding model; stub *(as_of: 2026-04-02)*
- [[models/kimi-k2-6]] — Moonshot AI open-weight 1T-param MoE; open-source SOTA coding/agent benchmark claims; 300-agent Claw Groups *(as_of: 2026-04-21)*
- [[models/muse-spark]] — Meta's new multimodal model; source emphasizes compute-efficient scaling vs prior Llama 4 Maverick generation *(as_of: 2026-04-10)*

## Tools

Tools and products built on top of models. One page per tool.

- [[tools/claude-managed-agents]] — Anthropic's hosted long-horizon agent runtime concept built around decoupled session, harness, and sandbox abstractions *(as_of: 2026-04-15)*
- [[tools/claude-cowork]] — Anthropic's desktop knowledge-work agent; works across local files, folders, and workplace apps to complete repeatable multi-step tasks *(as_of: 2026-04-21)*
- [[tools/cursor]] — Cursor 3 agentic coding workspace; multi-repo, local↔cloud agent handoff; Bugbot learned-rules loop for PR review *(as_of: 2026-04-10)*
- [[tools/harvey]] — legal AI platform; thin stub from a single editorial source *(as_of: 2026-04-02)*
- [[tools/kiro]] — VS Code-based SDD tool, 3-doc workflow *(as_of: 2025-10-15)*
- [[tools/spec-kit]] — GitHub's CLI SDD scaffolder with slash commands *(as_of: 2025-10-15)*
- [[tools/stripe-cli]] — Stripe CLI's developer-preview `projects` workflow for provisioning and managing app-stack services across providers *(as_of: 2026-04-09)*
- [[tools/shopify-ai-toolkit]] — Shopify's plugin / skills / MCP integration layer for AI-assisted Shopify app development *(as_of: 2026-04-10)*
- [[tools/tessl]] — CLI + MCP framework exploring spec-as-source; private beta *(as_of: 2025-10-15)*
- [[tools/perplexity-computer]] — Perplexity's 19-model orchestration agent; connects to 400+ apps and 12K+ financial institutions *(as_of: 2026-04-10)*
- [[tools/gemini]] — Google's AI chatbot; custom visualizations, notebooks, Google ecosystem integration *(as_of: 2026-04-10)*
- [[tools/claude-code]] — Anthropic's terminal-first AI coding agent; Monitor tool for event-driven background scripts *(as_of: 2026-04-10)*
- [[tools/codex]] — OpenAI's cloud-based coding agent via CLI and ChatGPT; stub with pricing *(as_of: 2026-04-10)*
- [[tools/hermes-agent]] — NousResearch open-source agent framework; 100K+ stars; multi-layer memory, self-improving skills, stateless sub-agent parallelism *(as_of: 2026-04-21)*
- [[tools/openai-agents-sdk]] — OpenAI's updated agent SDK: model-native harness, native sandbox execution, durable checkpoint / rehydration, and provider-neutral manifests *(as_of: 2026-04-15)*

## Benchmarks

Benchmark pages. Current leaderboards and methodology.

_(empty)_

## Workflows

Reusable patterns and recipes.

- [[workflows/advisor-strategy]] — Anthropic's small-executor + Opus-advisor escalation pattern, now a server-side `advisor_20260301` tool on the Claude API *(as_of: 2026-04-09)*

## Concepts

Ideas and techniques (RAG, context engineering, compound engineering, etc.).

- [[concepts/agent-improvement-loop]] — trace-centered workflow for improving AI agents through tracing, evals, review, and regression testing *(as_of: 2026-04-09)*
- [[concepts/functional-emotions]] — emotion-concept representations in LLMs can causally shape behavior without implying subjective feeling *(as_of: 2026-04-02)*
- [[concepts/harness]] — scaffolding that wraps a model into an acting agent; prompts, tools, orchestration, environment, evals *(as_of: 2026-04-15)*
- [[concepts/agentic-thinking]] — proposed successor to reasoning thinking; models that reason in order to act within environments *(as_of: 2026-04-10)*
- [[concepts/spec-driven-development]] — SDD concept, three-level taxonomy, critiques *(as_of: 2025-10-15)*
- [[concepts/curiosity-driven-imagination]] — agent recovery pattern: explore when stuck, learn new steps, and turn the steps into guided rewards *(as_of: 2025-03-06)*
- [[concepts/leworldmodel]] — LeWM: first JEPA to train end-to-end from pixels; SIGReg solves representation collapse; 15M params, 48x faster planning than DINO-WM *(as_of: 2026-03-13)*

## Trends

Things being watched that haven't solidified yet.

- [[trends/agents-reshape-organizations]] — leverage moves from individual to org as autonomous agents take coordination work *(as_of: 2026-04-21)*
- [[trends/ai-in-science]] — AI as force-multiplier for researchers; NASA anomalies, brain MRI, AlphaFold *(as_of: 2026-04-10)*
- [[trends/compute-infrastructure]] — frontier compute scale diverging; Anthropic/AWS 5 GW deal as inflection point *(as_of: 2026-04-21)*
- [[trends/proprietary-data-becomes-model-moat]] — proprietary operational data, domain evals, and narrow training loops may become a stronger moat as model quality converges *(as_of: 2026-04-10)*

## Training

Practical guidance for teaching teams and businesses to use AI well.

- [[training/company-wide-ai-enablement]] — operating patterns for broad AI adoption: defaults, access, social proof, platform-plus-spokes org design, and workflow redesign around agents *(as_of: 2026-04-21)*

## Sources

See `wiki/sources/` — source summaries are not indexed here (they're many and cheap). Use `grep` or Glob when you need them.

---

## Page count

- state-of: 7 (6 populated, 1 skeleton)
- models: 4
- tools: 15
- benchmarks: 0
- workflows: 1
- concepts: 7
- trends: 4
- training: 1

**Total content pages: 39.** The wiki is still in the early stage, but no longer below the initial bootstrap threshold.
