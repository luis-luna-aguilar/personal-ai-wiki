# Subcategories — controlled vocabulary

Valid values for the `subcategory:` field in frontmatter. A page has at most one subcategory.

Subcategories group tools, models, and workflows into cohorts of comparable things. They are the structure used by state-of pages to avoid forcing a single winner — each subcategory can have multiple top players.

## Current subcategories

Declared slugs: `spec-driven-development`, `agentic-coding-workspace`, `agent-orchestration`, `coding-model`, `frontier-multimodal-model`, `legal-ai`, `agentic-devops`, `computer-use`, `ai-assistant`, `terminal-coding-agent`, `agent-toolkits`, `agentic-orchestration-patterns`, `agent-native-documents`, `autonomous-research-agent`, `image-generation-model`, `agent-framework`, `science-agent-platform`, `speech-to-text`, `voice-models`, `ai-video-generation`, `ai-avatar-video`, `ui-generation`, `document-intelligence`, `healthcare-ai`, `finance-ai`, `deep-research-tool`, `utility-model`, `visual-design-prototyping`, `agent-eval-tooling`

### spec-driven-development
- **Parent domain(s):** coding
- **Applies to types:** tool | workflow | concept
- **Definition:** Tools and workflows where a structured natural-language spec is authored before (and often alongside) code, intended as the primary artifact guiding AI coding agents.
- **Examples:** [Kiro](../tools/kiro.md), [spec-kit](../tools/spec-kit.md), [Tessl Framework](../tools/tessl.md), [Spec-Driven Development (SDD)](../concepts/spec-driven-development.md)

### agentic-coding-workspace
- **Parent domain(s):** coding
- **Applies to types:** tool
- **Definition:** Coding tools whose primary UI is built around managing one or more AI coding agents (local and/or cloud), rather than file-centric editing with AI assistance bolted on.
- **Examples:** [Cursor](../tools/cursor.md)

### agent-orchestration
- **Parent domain(s):** agents
- **Applies to types:** tool | workflow
- **Definition:** Platforms, surfaces, and patterns for running, supervising, or internally routing AI agents — spanning hosted runtimes, human-supervision UIs, and multi-model coordination patterns within a single agentic task.
- **Examples:** [Claude Managed Agents](../tools/claude-managed-agents.md), [Claude Cowork](../tools/claude-cowork.md), [Advisor strategy](../workflows/advisor-strategy.md)

### coding-model
- **Parent domain(s):** models, coding
- **Applies to types:** model
- **Definition:** A foundation model trained or specialized for code generation, completion, or agentic coding tasks.
- **Examples:** [Composer 2](../models/composer-2.md)

### frontier-multimodal-model
- **Parent domain(s):** models
- **Applies to types:** model
- **Definition:** General-purpose frontier models competing on broad multimodal capability rather than narrow specialization.
- **Examples:** [Muse Spark](../models/muse-spark.md)

### legal-ai
- **Parent domain(s):** legal
- **Applies to types:** tool
- **Definition:** End-to-end AI products built specifically for legal workflows (matters, contracts, research, drafting), as distinct from generic horizontal assistants applied to legal use cases.
- **Examples:** [Harvey](../tools/harvey.md)

### agentic-devops
- **Parent domain(s):** coding, agents
- **Applies to types:** tool
- **Definition:** Tools and control planes that let humans or agents provision, diagnose, operate, verify, and safely mutate infrastructure through repeatable, auditable interfaces — spanning provisioning CLIs, Kubernetes diagnostics, approval-gated execution layers, and post-deploy verification.
- **Examples:** [Stripe CLI](../tools/stripe-cli.md), [Kagent](../tools/kagent.md), [K8sGPT](../tools/k8sgpt.md), [Skyflo](../tools/skyflo.md), [Checkly](../tools/checkly.md)

### computer-use
- **Parent domain(s):** computer-use
- **Applies to types:** tool
- **Definition:** Autonomous agents that orchestrate models, connect to external services, and execute complex workflows through application interfaces — going beyond API tool-calling to interact with systems as a human would.
- **Examples:** [Perplexity Computer](../tools/perplexity-computer.md)

### ai-assistant
- **Parent domain(s):** models
- **Applies to types:** tool
- **Definition:** General-purpose AI assistant products that combine conversational AI, search, and productivity features into a consumer or enterprise interface.
- **Examples:** [Gemini](../tools/gemini.md)

### terminal-coding-agent
- **Parent domain(s):** coding, agents
- **Applies to types:** tool
- **Definition:** CLI-based AI coding agents that run in the terminal, operating autonomously across file editing, shell commands, and tool use without a graphical IDE.
- **Examples:** [Claude Code](../tools/claude-code.md), [Codex](../tools/codex.md)

### agent-toolkits
- **Parent domain(s):** coding, agents
- **Applies to types:** tool
- **Definition:** Toolkits that package a specific developer platform's docs, schemas, validation, and related capabilities for AI coding tools via plugins, skills, or MCP servers.
- **Examples:** [Shopify AI Toolkit](../tools/shopify-ai-toolkit.md)

### agentic-orchestration-patterns
- **Parent domain(s):** agents
- **Applies to types:** workflow | concept
- **Definition:** Reusable design patterns for orchestrating one or more agents across planning, delegation, evaluation, ambiguity handling, and recovery.
- **Examples:** [Agentic orchestration patterns](../workflows/agentic-orchestration-patterns.md)

### agent-native-documents
- **Parent domain(s):** agents
- **Applies to types:** tool
- **Definition:** Document editors and shared writing surfaces built for humans and agents to draft, revise, comment, and maintain the same working artifacts.
- **Examples:** [Proof](../tools/proof.md)

### autonomous-research-agent
- **Parent domain(s):** agents
- **Applies to types:** tool
- **Definition:** Agents that run a closed loop over a research or experimentation process — reading sources, designing experiments, executing jobs, evaluating results, and iterating — with minimal human steering.
- **Examples:** [HF ml-intern](../tools/hf-ml-intern.md)

### image-generation-model
- **Parent domain(s):** models
- **Applies to types:** model
- **Definition:** Models specialized for text-to-image generation, image editing, and visual synthesis tasks, distinct from general-purpose multimodal models.
- **Examples:** [GPT-Image-2](../models/gpt-image-2.md)

### agent-framework
- **Parent domain(s):** agents
- **Applies to types:** tool
- **Definition:** SDKs and development kits for building, running, and testing custom agents, including orchestration primitives, tool integration, and runtime patterns.
- **Examples:** [Google ADK](../tools/google-adk.md)

### agent-eval-tooling
- **Parent domain(s):** agents
- **Applies to types:** tool
- **Definition:** Platforms and frameworks specialized for evaluating, tracing, and monitoring AI agent and LLM pipeline behavior — covering dataset management, assertion-based testing, LLM-as-a-judge scoring, and production observability.
- **Examples:** [Braintrust](../tools/braintrust.md), [Promptfoo](../tools/promptfoo.md), [Langfuse](../tools/langfuse.md)

### science-agent-platform
- **Parent domain(s):** science, agents
- **Applies to types:** tool
- **Definition:** Platforms built to run or supervise agentic research workflows across literature review, experimentation, hypothesis generation, or scientific knowledge work.
- **Examples:** [FutureHouse](../tools/futurehouse.md)

### speech-to-text
- **Parent domain(s):** agents, healthcare, voice
- **Applies to types:** tool
- **Definition:** Products focused primarily on transcription, speech recognition, and converting audio into structured text for downstream human or agent workflows.
- **Examples:** [ElevenLabs Scribe](../tools/elevenlabs-scribe.md)

### voice-models
- **Parent domain(s):** agents, voice
- **Applies to types:** tool
- **Definition:** AI voice products centered on expressive text-to-speech, speech-to-speech conversation, or voice cloning as a primary interface or output surface.
- **Examples:** [Hume EVI 3](../tools/hume-evi-3.md), [Eleven v3](../tools/eleven-v3.md)

### ai-video-generation
- **Parent domain(s):** creative
- **Applies to types:** tool
- **Definition:** Tools for generating or editing video from prompts, images, or clips, including systems that add synchronized audio or produce end-to-end media artifacts.
- **Examples:** [Seedance 2.0](../tools/seedance-2.md), [Dream Machine](../tools/dream-machine.md)

### ai-avatar-video
- **Parent domain(s):** creative
- **Applies to types:** tool
- **Definition:** Products built around synthetic presenters, talking avatars, or reusable digital personas for videos, communication, or marketing.
- **Examples:** [HeyGen](../tools/heygen.md)

### ui-generation
- **Parent domain(s):** creative, coding
- **Applies to types:** tool
- **Definition:** Tools that generate UI layouts, interface artifacts, or design-to-code drafts from prompts, screenshots, or structured instructions.
- **Examples:** [Stitch](../tools/stitch.md)

### document-intelligence
- **Parent domain(s):** agents, finance, healthcare
- **Applies to types:** tool
- **Definition:** AI products specialized for extracting, structuring, querying, or reasoning over documents, PDFs, forms, and tables.
- **Examples:** [Mistral Document AI](../tools/mistral-document-ai.md), [LandingAI Agentic Document Extraction](../tools/landingai-agentic-document-extraction.md)

### healthcare-ai
- **Parent domain(s):** healthcare
- **Applies to types:** tool
- **Definition:** End-to-end AI products built specifically for clinical, provider, patient, or healthcare-operations workflows rather than generic horizontal assistants.
- **Examples:** [Dragon Copilot](../tools/dragon-copilot.md), [OpenEvidence](../tools/open-evidence.md)

### finance-ai
- **Parent domain(s):** finance
- **Applies to types:** tool
- **Definition:** AI products specialized for financial analysis, modeling, investment workflows, or finance-specific knowledge work.
- **Examples:** [Hebbia](../tools/hebbia.md)

### visual-design-prototyping
- **Parent domain(s):** creative, agents
- **Applies to types:** tool
- **Definition:** Tools for collaborative visual design, prototyping, slides, one-pagers, and marketing assets through conversational AI, going beyond UI layout generation into full design-to-artifact workflows.
- **Examples:** [Claude Design](../tools/claude-design.md)

### deep-research-tool
- **Parent domain(s):** agents
- **Applies to types:** tool
- **Definition:** Tools that autonomously plan, search, read, synthesize, and iterate across many sources to produce longer-horizon research outputs rather than answer in a single pass.
- **Examples:** [OpenAI Deep Research](../tools/openai-deep-research.md), [Gemini Deep Research](../tools/gemini-deep-research.md)

### utility-model
- **Parent domain(s):** models
- **Applies to types:** model
- **Definition:** Small, narrow-purpose models built to solve a specific infrastructure or pipeline task (e.g. PII redaction, classification, embedding) rather than general-purpose generation or reasoning.
- **Examples:** [OpenAI Privacy Filter](../models/openai-privacy-filter.md)

### Format

Each entry follows this shape:

```
### <subcategory-slug>
- **Parent domain(s):** coding, agents
- **Applies to types:** tool | model | workflow
- **Definition:** one sentence describing what belongs here
- **Examples:** (examples appear here as the wiki fills)
```

## Adding a new subcategory

1. Propose in a proposal file under "Schema / vocabulary additions".
2. Include the parent domain(s), which types it applies to, and a one-sentence definition.
3. Once approved, append the entry here as part of applying the proposal.

## Rules

- Subcategory slugs are lowercase, hyphenated. Examples: `terminal-coding-agent`, `ide-pair-programming`, `autonomous-coding-agent`.
- A subcategory belongs to 1+ domains. A tool inherits its state-of placement from its subcategory's domains.
- Subcategories can be created with a single member. They're the unit of categorization, not a popularity contest.
- Subcategories are rarely deleted. If all members become obsolete, the subcategory stays as a historical record.
