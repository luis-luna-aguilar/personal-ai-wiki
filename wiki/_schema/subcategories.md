# Subcategories — controlled vocabulary

Valid values for the `subcategory:` field in frontmatter. A page has at most one subcategory.

Subcategories group tools, models, and workflows into cohorts of comparable things. They are the structure used by state-of pages to avoid forcing a single winner — each subcategory can have multiple top players.

## Current subcategories

Declared slugs: `spec-driven-development`, `agentic-coding-workspace`, `agent-orchestration-ui`, `agent-orchestration`, `coding-model`, `frontier-multimodal-model`, `legal-ai`, `model-orchestration`, `agentic-devops`, `computer-use`, `ai-assistant`, `terminal-coding-agent`, `agent-toolkits`, `agentic-orchestration-patterns`

### spec-driven-development
- **Parent domain(s):** coding
- **Applies to types:** tool | workflow | concept
- **Definition:** Tools and workflows where a structured natural-language spec is authored before (and often alongside) code, intended as the primary artifact guiding AI coding agents.
- **Examples:** [[tools/kiro]], [[tools/spec-kit]], [[tools/tessl]], [[concepts/spec-driven-development]]

### agentic-coding-workspace
- **Parent domain(s):** coding
- **Applies to types:** tool
- **Definition:** Coding tools whose primary UI is built around managing one or more AI coding agents (local and/or cloud), rather than file-centric editing with AI assistance bolted on.
- **Examples:** [[tools/cursor]]

### agent-orchestration-ui
- **Parent domain(s):** agents
- **Applies to types:** tool
- **Definition:** Surfaces (desktop, web, mobile, chat-integration) that let a human supervise, hand off, and merge work across multiple AI agents running in parallel.
- **Examples:** [[tools/cursor]]

### agent-orchestration
- **Parent domain(s):** agents
- **Applies to types:** tool
- **Definition:** Platforms that run or coordinate long-horizon agents across one or more execution environments, with durable state and orchestration separated from any single local process or container.
- **Examples:** [[tools/claude-managed-agents]]

### coding-model
- **Parent domain(s):** models, coding
- **Applies to types:** model
- **Definition:** A foundation model trained or specialized for code generation, completion, or agentic coding tasks.
- **Examples:** [[models/composer-2]]

### frontier-multimodal-model
- **Parent domain(s):** models
- **Applies to types:** model
- **Definition:** General-purpose frontier models competing on broad multimodal capability rather than narrow specialization.
- **Examples:** [[models/muse-spark]]

### legal-ai
- **Parent domain(s):** legal
- **Applies to types:** tool
- **Definition:** End-to-end AI products built specifically for legal workflows (matters, contracts, research, drafting), as distinct from generic horizontal assistants applied to legal use cases.
- **Examples:** [[tools/harvey]]

### model-orchestration
- **Parent domain(s):** agents
- **Applies to types:** workflow | concept
- **Definition:** Patterns that combine models of different sizes or costs inside a single agentic task — e.g. a small executor escalating to a larger advisor, or a large orchestrator delegating to small workers. Concerned with how an agent is internally structured, not with the user-facing surface.
- **Examples:** [[workflows/advisor-strategy]]

### agentic-devops
- **Parent domain(s):** coding, agents
- **Applies to types:** tool
- **Definition:** CLI-native tools that provision and manage third-party app infrastructure and credentials across multiple providers, in workflows designed to be executable by humans or agents.
- **Examples:** [[tools/stripe-cli]]

### computer-use
- **Parent domain(s):** computer-use
- **Applies to types:** tool
- **Definition:** Autonomous agents that orchestrate models, connect to external services, and execute complex workflows through application interfaces — going beyond API tool-calling to interact with systems as a human would.
- **Examples:** [[tools/perplexity-computer]]

### ai-assistant
- **Parent domain(s):** models
- **Applies to types:** tool
- **Definition:** General-purpose AI assistant products that combine conversational AI, search, and productivity features into a consumer or enterprise interface.
- **Examples:** [[tools/gemini]]

### terminal-coding-agent
- **Parent domain(s):** coding, agents
- **Applies to types:** tool
- **Definition:** CLI-based AI coding agents that run in the terminal, operating autonomously across file editing, shell commands, and tool use without a graphical IDE.
- **Examples:** [[tools/claude-code]], [[tools/codex]]

### agent-toolkits
- **Parent domain(s):** coding
- **Applies to types:** tool
- **Definition:** Toolkits that package a specific developer platform's docs, schemas, validation, and related capabilities for AI coding tools via plugins, skills, or MCP servers.
- **Examples:** [[tools/shopify-ai-toolkit]]

### agentic-orchestration-patterns
- **Parent domain(s):** agents
- **Applies to types:** workflow | concept
- **Definition:** Reusable design patterns for orchestrating one or more agents across planning, delegation, evaluation, ambiguity handling, and recovery.
- **Examples:** [[workflows/agentic-orchestration-patterns]]

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
