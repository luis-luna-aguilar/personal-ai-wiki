---
type: proposal
status: applied
created: 2026-04-23
---

# Proposal: Personal Wiki Agent Framework Research (Deep Agents, Goose, MCP deployment)

## Summary

This proposal captures the framework and deployment research done while designing the Personal Wiki Agent. The most important conclusions:

- **Deep Agents** looks like the best harness fit for building a dedicated `use_personal_wiki` agent with planning, file tools, subagents, permissions, and a strong custom contract.
- **Goose** is a serious alternative when the priority is local-first deployment on Luis's own machine with MCP and a desktop/CLI agent product already in place.
- **Pydantic AI** and **smolagents** remain useful comparison points, but they are not important enough for first-pass standalone wiki coverage.
- **Claude Desktop** supports local MCP servers directly.
- **ChatGPT** currently documents remote MCP/custom connectors rather than localhost-only desktop attachment, so remote exposure may be required for ChatGPT use.

Only the reusable parts belong in the wiki. The framework choice for the Personal Wiki Agent itself is an implementation decision for the `personal-wiki-agent/` subproject, not durable wiki knowledge.

## Research URLs

- Deep Agents overview: https://docs.langchain.com/oss/python/deepagents/overview
- Deep Agents models: https://docs.langchain.com/oss/python/deepagents/models
- Deep Agents subagents: https://docs.langchain.com/oss/python/deepagents/subagents
- LangChain MCP adapters: https://docs.langchain.com/oss/python/langchain/mcp
- LangGraph repo: https://github.com/langchain-ai/langgraph
- Goose providers: https://block.github.io/goose/docs/getting-started/providers/
- Goose repo: https://github.com/block/goose
- Pydantic AI model overview: https://pydantic.dev/docs/ai/models/overview/
- Pydantic AI OpenRouter model docs: https://pydantic.dev/docs/ai/api/models/openrouter/
- Pydantic AI MCP overview: https://pydantic.dev/docs/ai/mcp/overview/
- Pydantic AI MCP client: https://pydantic.dev/docs/ai/mcp/client/
- Pydantic AI MCP server: https://pydantic.dev/docs/ai/mcp/server/
- smolagents docs: https://huggingface.co/docs/smolagents/index
- smolagents repo: https://github.com/huggingface/smolagents
- OpenRouter LangChain integration: https://openrouter.ai/docs/guides/community/langchain
- Claude Desktop local MCP help: https://support.anthropic.com/en/articles/10949351-getting-started-with-model-context-protocol-mcp-on-claude-for-desktop
- Claude remote MCP help: https://support.anthropic.com/en/articles/11175166-getting-started-with-custom-integrations-using-remote-mcp
- OpenAI MCP docs: https://platform.openai.com/docs/mcp
- OpenAI tools/remote MCP guide: https://platform.openai.com/docs/guides/tools-remote-mcp
- ChatGPT connectors help: https://help.openai.com/en/articles/11487775-connectors-in-chatgpt

## Intended changes

- [x] **Update** `wiki/workflows/agentic-orchestration-patterns.md` — add a brief general note that Deep Agents represents a batteries-included harness direction while Goose represents a local-agent-product direction
- [x] **Update** `wiki/concepts/mcp.md` — append a practical note on local-vs-remote MCP deployment surfaces across Claude Desktop and ChatGPT
- [x] **Create** source summary pages only for the primary sources actually used in the reusable wiki updates

## Recommended ingest order

1. Deep Agents docs + LangGraph repo
2. Goose docs + repo
3. Claude/OpenAI MCP deployment docs
4. Pydantic AI and smolagents only if broader reusable framework coverage becomes warranted later

## Key claims extracted

### Deep Agents

- Deep Agents is described by LangChain as an “agent harness”
- Built-in capabilities include planning, filesystem context management, subagent spawning, permissions, skills, and long-term memory
- Deep Agents work with any LangChain chat model that supports tool calling
- This makes Deep Agents the strongest fit for a dedicated Personal Wiki Agent with one public tool and a repo-specific harness

### Goose

- Goose is an open-source desktop app, CLI, and API for general-purpose local agents
- Supports OpenRouter and MCP directly
- Better fit when the main requirement is “run this on my own computer as a local agent host”
- More product-like and less narrowly specialized than Deep Agents

### Pydantic AI

- Pydantic AI is model-agnostic and explicitly supports OpenRouter
- Supports MCP both as client and server
- Strong Python-native option if the project values Python ergonomics and MCP clarity over a more opinionated prebuilt harness

### smolagents

- smolagents is open source and Apache 2.0 licensed
- Model-agnostic; supports OpenAI-compatible configuration
- Supports MCP tools
- Lightweight and promising, but still more minimal and experimental than the main recommendation

### MCP deployment reality

- Claude Desktop supports local MCP servers running on the user's machine
- Anthropic distinguishes local Claude Desktop MCP from remote MCP connectors used through Claude cloud surfaces
- ChatGPT currently documents custom connectors around remote MCP servers, not localhost-only desktop attachment
- This suggests a likely split: local MCP first for Claude Desktop, remote MCP later for ChatGPT compatibility

## Resolved decisions

- Do **not** create standalone `wiki/tools/` pages for these frameworks in the first pass. They are better captured as a comparative framework-selection page because the current need is implementation choice, not broad tool-catalog coverage.
- Keep the MCP deployment guidance on `wiki/concepts/mcp.md`, not on a separate workflow page.
- Skip OpenRouter's own Agent SDK for now.
- Narrow the first-pass ingest to **Deep Agents**, **Goose**, and the **Claude/OpenAI MCP deployment docs**. Keep Pydantic AI and smolagents as secondary comparison notes unless they become active implementation candidates.
- Do **not** ingest the Personal Wiki Agent framework-selection decision itself into the wiki. That belongs in project-local docs for `personal-wiki-agent/`, not in the knowledge base.

## Suggested reusable wiki coverage

- `wiki/concepts/mcp.md`: practical note on local vs remote MCP deployment surfaces across Claude Desktop and ChatGPT
- `wiki/workflows/agentic-orchestration-patterns.md`: short note that current agent systems are splitting between batteries-included harnesses and local-agent products
- Project-local docs inside `personal-wiki-agent/`: the actual framework decision, rationale, and implementation choice

## Notes for application

- These sources were researched live on the web and have **not** yet been fetched into `raw/`
- Before applying this proposal to the wiki, fetch the primary docs/pages you want to treat as source-of-record
- The lean reusable first pass should ingest only the sources needed for **MCP deployment guidance** and any very short general framing added to `agentic-orchestration-patterns`
- The Personal Wiki Agent framework decision itself should be documented outside the wiki

## Comments

- let's not ingest the workflow on the personal wiki agent framework selection. That's an operational task that has nothing to do with knowledge. It's just a decision made based on knowledge but it's not knowledge itself 
