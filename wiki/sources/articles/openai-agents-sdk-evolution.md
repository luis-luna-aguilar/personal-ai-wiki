---
title: The next evolution of the Agents SDK
type: source
source_type: article
source_file: raw/articles/2026-04-16-openaicom-index-the-next-evolution-of-the-agents-sdk.md
url: https://openai.com/index/the-next-evolution-of-the-agents-sdk/
published: 2026-04-15
ingested: 2026-04-16
domains: [agents]
---

# The next evolution of the Agents SDK

OpenAI's product post turns the Agents SDK into a clearer statement about what production agent infrastructure should include. The core additions are a more capable model-native harness, native sandbox execution, and a design that keeps the harness separate from compute so agent runs can be safer, more durable, and easier to scale.

## Influenced pages

- [OpenAI Agents SDK](../../tools/openai-agents-sdk.md) — new tool page for the SDK's updated role in the agent-runtime stack
- [Agents](../../history/state-of/agents.md) — adds OpenAI as another serious `agent-orchestration` entry beside Anthropic Managed Agents
- [Harness (agent)](../../concepts/harness.md) — adds a concrete vendor example of the harness as memory + orchestration + filesystem + execution-boundary infrastructure

## Key claims extracted

- Published 2026-04-15
- Agents SDK now includes a model-native harness for file and tool-based agent work
- Harness primitives explicitly include configurable memory, sandbox-aware orchestration, Codex-like filesystem tools, MCP, skills, AGENTS.md, shell, and `apply_patch`
- Native sandbox execution supports both built-in and third-party providers
- New `Manifest` abstraction describes portable workspaces across local files and cloud storage
- OpenAI argues harness and compute should be separated for security, durability, and scale
- Runs can recover from sandbox loss through snapshotting and rehydration
- The new capabilities are generally available in Python via standard API pricing; TypeScript is planned

## Notes

- The raw fetch saved a Cloudflare verification placeholder instead of the article body. Claims above were verified directly against the official OpenAI page at the recorded URL during proposal drafting.
