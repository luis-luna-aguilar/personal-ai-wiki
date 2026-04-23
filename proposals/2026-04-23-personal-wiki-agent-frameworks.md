---
type: proposal
status: pending
created: 2026-04-23
---

# Proposal: Personal Wiki Agent Framework Research (Deep Agents, Goose, Pydantic AI, smolagents, MCP deployment)

## Summary

This proposal captures the framework and deployment research done while designing the Personal Wiki Agent. The most important conclusions:

- **Deep Agents** looks like the best harness fit for building a dedicated `use_personal_wiki` agent with planning, file tools, subagents, permissions, and a strong custom contract.
- **Goose** is a serious alternative when the priority is local-first deployment on Luis's own machine with MCP, OpenRouter, and a desktop/CLI agent product already in place.
- **Pydantic AI** is a strong Python-native alternative with explicit OpenRouter and MCP support, but feels more framework-like than harness-like.
- **smolagents** is open source (Apache 2.0), model-agnostic, and OpenRouter-compatible, but remains more lightweight and experimental than the main recommendation.
- **Claude Desktop** supports local MCP servers directly.
- **ChatGPT** currently documents remote MCP/custom connectors rather than localhost-only desktop attachment, so remote exposure may be required for ChatGPT use.

This material is not yet represented in the wiki and is directly relevant to the new `personal-wiki-agent/` subproject.

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
- OpenRouter Agent SDK landing page: https://openrouter.ai/sdk
- Claude Desktop local MCP help: https://support.anthropic.com/en/articles/10949351-getting-started-with-model-context-protocol-mcp-on-claude-for-desktop
- Claude remote MCP help: https://support.anthropic.com/en/articles/11175166-getting-started-with-custom-integrations-using-remote-mcp
- OpenAI MCP docs: https://platform.openai.com/docs/mcp
- OpenAI tools/remote MCP guide: https://platform.openai.com/docs/guides/tools-remote-mcp
- ChatGPT connectors help: https://help.openai.com/en/articles/11487775-connectors-in-chatgpt

## Intended changes

- [x] **Create** `wiki/tools/deep-agents.md` — new tool page for LangChain's Deep Agents harness
- [x] **Create** `wiki/tools/goose.md` — new tool page for Goose as an open-source local agent platform
- [x] **Create** `wiki/tools/pydantic-ai.md` — new tool page for provider-agnostic Python agent framework with MCP/OpenRouter support
- [x] **Create** `wiki/tools/smolagents.md` — new tool page for Hugging Face's lightweight open-source agent library
- [x] **Update** `wiki/workflows/agentic-orchestration-patterns.md` — add note that Deep Agents represents a “batteries-included harness” direction while Goose represents a local-agent-product direction
- [x] **Update** `wiki/concepts/mcp.md` — append a practical note on local-vs-remote MCP deployment surfaces across Claude Desktop and ChatGPT
- [x] **Create** one or more `wiki/sources/articles/*.md` or `wiki/sources/repos/*.md` summary pages after the relevant primary sources are fetched into `raw/`

## Recommended ingest order

1. Deep Agents docs + LangGraph repo
2. Goose docs + repo
3. Pydantic AI OpenRouter + MCP docs
4. smolagents docs + repo
5. Claude/OpenAI MCP deployment docs

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
- Strong Python-native option if the project values Python ergonomics and MCP/OpenRouter clarity over a more opinionated prebuilt harness

### smolagents

- smolagents is open source and Apache 2.0 licensed
- Model-agnostic; supports OpenRouter-style OpenAI-compatible configuration
- Supports MCP tools
- Lightweight and promising, but still more minimal and experimental than the main recommendation

### MCP deployment reality

- Claude Desktop supports local MCP servers running on the user's machine
- Anthropic distinguishes local Claude Desktop MCP from remote MCP connectors used through Claude cloud surfaces
- ChatGPT currently documents custom connectors around remote MCP servers, not localhost-only desktop attachment
- This suggests a likely split: local MCP first for Claude Desktop, remote MCP later for ChatGPT compatibility

## Open questions

- Should these framework pages live under `wiki/tools/` individually, or should some of them be covered by a single comparative workflow/concept page?
	-  let's skip the month as tools because they are 
- Should the MCP deployment guidance live only on `wiki/concepts/mcp.md`, or also on a new workflow page about “deploying personal knowledge agents”?
	-  let's keep it in concept 
- Should OpenRouter's own Agent SDK be represented, or is it less important than the other frameworks because the current implementation decision moved to Deep Agents?
	-  let's skip this one
- Do we want to ingest all four frameworks now, or only the two that matter most for the Personal Wiki Agent decision: Deep Agents and Goose?
	- Hello Sam 

## Suggested page shapes

### wiki/tools/deep-agents.md

- What it is
- Why it matters as an agent harness
- Built-in primitives: planning, filesystems, subagents, permissions, skills
- Fit for provider-agnostic specialized agents
- Caveats

### wiki/tools/goose.md

- What it is
- Why it matters as a local-first open-source agent platform
- OpenRouter + MCP support
- Desktop/CLI/API surface
- Caveats

### wiki/tools/pydantic-ai.md

- What it is
- Why it matters as a Python-native model-agnostic framework
- OpenRouter support
- MCP client/server support
- Caveats

### wiki/tools/smolagents.md

- What it is
- Why it matters as a minimal open-source agent library
- OpenRouter/OpenAI-compatible support
- MCP support
- Caveats: lightweight, more experimental

## Notes for application

- These sources were researched live on the web and have **not** yet been fetched into `raw/`
- Before applying this proposal to the wiki, fetch the primary docs/pages you want to treat as source-of-record
- If you want the leanest first pass, ingest only **Deep Agents**, **Goose**, and the **Claude/OpenAI MCP deployment docs**
