---
type: proposal
source: raw/articles/2026-04-16-openaicom-index-the-next-evolution-of-the-agents-sdk.md
status: pending
created: 2026-04-16
---

# Proposal: OpenAI updates the Agents SDK

## Summary
OpenAI's April 15, 2026 product post reframes the Agents SDK as standardized infrastructure for long-horizon agents, not just a thin orchestration library. The main additions are a more capable model-native harness, native sandbox execution, and explicit separation between harness and compute for security, durability, and scale.

**Fetch note:** `scripts/fetch_url.py` saved a Cloudflare placeholder page in `raw/articles/2026-04-16-openaicom-index-the-next-evolution-of-the-agents-sdk.md`. The proposal below is still based on the official OpenAI page at the same URL, verified directly during triage processing.

## Intended changes

- [x] **Create** `wiki/tools/openai-agents-sdk.md` — new tool page for OpenAI's model-native agent runtime / SDK
    > See draft below

- [x] **Update** `wiki/state-of/agents.md` — add OpenAI under `Agent orchestration`
    > **Before:** only `[[tools/claude-managed-agents]]` appears under `Agent orchestration`
    > **After:** add `[[tools/openai-agents-sdk]] — OpenAI's updated SDK combines a model-native harness with native sandbox execution, durable checkpoint / rehydration, provider-neutral manifests, and built-in support for MCP, skills, AGENTS.md, shell, and apply_patch *(as of 2026-04-15)*`

- [x] **Update** `wiki/concepts/harness.md` — add a concrete vendor example of a harness as production infrastructure rather than just prompt/tool glue
    > **Add snippet:** `OpenAI's April 15, 2026 Agents SDK post gives a concrete vendor example of this broader definition: the harness includes configurable memory, sandbox-aware orchestration, Codex-like filesystem tools, MCP, skills, AGENTS.md, shell, and apply_patch. OpenAI explicitly argues the harness should stay separate from compute so credentials remain outside execution sandboxes and runs can survive sandbox failure via snapshotting and rehydration.`

- [x] **Create** `wiki/sources/articles/openai-agents-sdk-evolution.md` — source summary for the official OpenAI post
    > See draft below

- [x] **Update** `wiki/index.md` — add `[[tools/openai-agents-sdk]]` under Tools and refresh counts / `as_of`
    > **Before:** no OpenAI Agents SDK entry
    > **After:** `- [[tools/openai-agents-sdk]] — OpenAI's updated agent SDK: model-native harness, native sandbox execution, durable checkpoint / rehydration, and provider-neutral manifests *(as_of: 2026-04-15)*`

## Page drafts

### wiki/tools/openai-agents-sdk.md (new)

```md
---
title: OpenAI Agents SDK
type: tool
domains: [agents]
subcategory: agent-orchestration
tags: [openai, closed-source, agentic]
as_of: 2026-04-15
sources: [openai-agents-sdk-evolution]
---

# OpenAI Agents SDK

OpenAI's Agents SDK is an API-side toolkit for building long-running agents that can inspect files, run commands, edit code, and operate inside controlled sandboxes. As of the April 15, 2026 update, OpenAI is positioning it less as a thin orchestration wrapper and more as standardized agent infrastructure built around a model-native harness plus native sandbox execution.

## Current status (as of 2026-04-15)

- Model-native harness for agent loops working across files, tools, and computer-like environments
- Native sandbox execution with support for built-in or third-party providers including Blaxel, Cloudflare, Daytona, E2B, Modal, Runloop, and Vercel
- `Manifest` abstraction defines portable workspaces across local files and storage sources such as S3, GCS, Azure Blob, and Cloudflare R2
- Harness primitives now explicitly include configurable memory, sandbox-aware orchestration, Codex-like filesystem tools, MCP, skills, AGENTS.md, shell, and `apply_patch`
- OpenAI emphasizes separation between harness and compute for security, durability, and scale: credentials stay out of execution sandboxes; runs can recover via snapshotting and rehydration; work can span one or many isolated sandboxes
- Generally available via the API on standard token and tool-use pricing

## Why it matters

This pushes OpenAI deeper into the agent-runtime layer rather than only models and raw APIs. The practical claim is that developers should not have to assemble their own long-running agent stack from scratch just to get safe code execution, resumability, and model-aligned orchestration.

It also gives a concrete example of what "harness" now means in frontier agent systems: not just prompt plus tool descriptions, but memory, execution policies, workspace shaping, environment boundaries, and failure recovery.

## Weaknesses / caveats

- The current source is a vendor product post; there is no third-party reliability or adoption data yet
- Python launches first; TypeScript support is only planned
- This page captures the platform shape better than operational limits, pricing details by provider, or comparative performance

## Recent changes

- [2026-04-15] OpenAI adds model-native harness and native sandbox execution; positions the SDK as standardized long-horizon agent infrastructure

## Sources

- [[sources/articles/openai-agents-sdk-evolution]]
```

### wiki/sources/articles/openai-agents-sdk-evolution.md (new)

```md
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

- [[tools/openai-agents-sdk]] — new tool page for the SDK's updated role in the agent-runtime stack
- [[state-of/agents]] — adds OpenAI as another serious `agent-orchestration` entry beside Anthropic Managed Agents
- [[concepts/harness]] — adds a concrete vendor example of the harness as memory + orchestration + filesystem + execution-boundary infrastructure

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
```

## Open questions

- Should `OpenAI Agents SDK` live only under `agents`, or also under `coding` because the post explicitly includes code editing, shell, and `apply_patch` workflows?
- Do you want this kept as one tool page, or split later into `OpenAI Agents SDK` vs a broader OpenAI agent-runtime page if more launch posts pile up?

## Comments

- 