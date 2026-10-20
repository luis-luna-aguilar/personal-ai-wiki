---
title: Deep Agents overview
type: source
source_type: article
url: https://docs.langchain.com/oss/python/deepagents/overview
fetched: 2026-10-19
---

# Deep Agents overview

Deep Agents is the easiest way to start building agents and applications that are powered by LLMs—with built-in capabilities for file systems for context management, subagent-spawning, and long-term memory.
Optional capabilities such as [task planning](#task-planning) and [skills](#skills) extend the harness when your use case needs them.
You can use deep agents for any task, including complex, multi-step tasks.
Deep Agents comes with the following capabilities:

* **Take actions in an environment**: Take actions via tools, read and write files, execute code
* **Connect to your data**: Load memories, skills, and domain knowledge at the right moment
* **Manage growing context**: Summarize history and offload large results across long runs
* **Parallelize tasks**: Delegate to general or specialized subagents running in isolated context windows
* **Stay in the loop**: Pause for human approval at critical decision points
* **Improve over time**: Update memory, skills, and prompts based on real usage

See [Core capabilities](#core-capabilities) for a full breakdown of each component.

## Try it

## Quickstart

See the [Quickstart](/oss/python/deepagents/quickstart) and [Customization guide](/oss/python/deepagents/customization) to get started building your own agents and applications with Deep Agents.

## Core capabilities

![Agent harness capabilities by category](https://mintcdn.com/langchain-5e9cc07a/jtty0O--UJOKG0nK/oss/images/agent_harness_capabilities.svg?fit=max&auto=format&n=jtty0O--UJOKG0nK&q=85&s=0ff671d72badd0844826660dfcb04391)
Deep Agents is an [“agent harness”](/oss/python/concepts/products#agent-harnesses-like-the-deep-agents-sdk). It is the same core tool calling loop as other agent frameworks, but with built-in capabilities that make agents reliable for real tasks:
[`deepagents`](https://pypi.org/project/deepagents/) is a standalone library built on top of [LangChain](/oss/python/langchain)’s core building blocks for agents. It uses the [LangGraph](/oss/python/langgraph) runtime for durable execution, streaming, human-in-the-loop, and other features.
[LangChain](/oss/python/langchain) is the framework that provides the core building blocks for your agents.
To learn more about the differences between LangChain, LangGraph, and Deep Agents, see [Frameworks, runtimes, and harnesses](/oss/python/concepts/products). For a side-by-side comparison with Anthropic’s harness, see [Deep Agents vs. Claude Agent SDK](/oss/python/deepagents/comparison).
For building custom agents without these built-in capabilities, consider using LangChain’s [`create_agent`](/oss/python/langchain/agents) or building a custom [LangGraph](/oss/python/langgraph/overview) workflow.

## Execution environment

The execution environment is where an agent acts. It has four layers:

* **[Tools](#tools-and-mcp)**: custom functions, APIs, and databases the agent can call
* **[Virtual filesystem](#virtual-filesystem-access)**: file tools backed by pluggable backends
* **[Filesystem permissions](#filesystem-permissions)**: declarative access control over which paths agents can read or write
* **[Code execution](#code-execution)**: sandboxed shell execution and an in-process JavaScript interpreter

**[Streaming](#streaming)** allows you to keep up with everything happening using typed event streams for messages, tools, values, and delegated tasks.
Pass custom functions, LangChain tools, or tools from any [MCP server](/oss/python/deepagents/tools#mcp-tools) with the `tools=` parameter. Deep Agents fully support the [Model Context Protocol (MCP)](/oss/python/langchain/mcp), letting you connect to databases, APIs, file systems, and more through a standard interface.
For more information on defining custom tools, using MCP servers, and the full list of built-in harness tools, see [Tools](/oss/python/deepagents/tools).

### Virtual filesystem access

The harness provides a configurable virtual filesystem which can be backed by different [pluggable backends](/oss/python/deepagents/backends): in-memory state, local disk, LangGraph store, composite routing, or a custom backend with [permission rules](/oss/python/deepagents/permissions) for read and write access.
The backends support the following file system operations:

The `delete` tool requires `deepagents>=0.7`. Backends that do not support deletion have the tool automatically hidden from the model.

Supported multimodal file extensions

Running without the default filesystem tools

Restricting filesystem tools

The virtual filesystem is used by several other harness capabilities such as skills, memory, code execution, and context management.
You can also use the file system when building custom tools and middleware for Deep Agents.
For more information, see [backends](/oss/python/deepagents/backends). To generate a durable repository wiki that agents can read from the filesystem, see [OpenWiki](/oss/openwiki/overview).

### Filesystem permissions

The harness supports declarative permission rules that control which files and directories the agent can read or write. Permissions apply to the built-in filesystem tools listed above and are evaluated in declaration order with first-match-wins semantics.
Define permissions by passing a list of rules to `permissions=` when creating the agent. Each rule includes:

* `operations`: `"read"` and/or `"write"`
* `paths`: Glob patterns for files or directories
* `mode`: `"allow"` or `"deny"`

Rules are evaluated top to bottom, and the first matching rule wins. If no rule matches, the operation is allowed.
This model lets you restrict agents to specific directories (for example, `/workspace/`), protect sensitive files such as `.env` or credentials, and give subagents narrower access than the parent agent.
Permissions do not apply to [sandbox backends](/oss/python/deepagents/sandboxes), which support arbitrary command execution via the `execute` tool. For custom validation logic, use [backend policy hooks](/oss/python/deepagents/backends#add-policy-hooks).
For the full rule structure, examples, and subagent inheritance, see [Permissions](/oss/python/deepagents/permissions).

### Code execution

Deep Agents supports code execution in two ways:

* [Sandbox backends](/oss/python/deepagents/sandboxes) expose an `execute` tool for shell commands in an isolated environment.
* [Interpreters](/oss/python/deepagents/interpreters) add an `eval` tool that runs JavaScript in a scoped QuickJS runtime.

Use sandbox backends when the agent needs to install dependencies, run tests, call CLIs, or work with an operating-system filesystem. Sandbox backends implement the `SandboxBackendProtocolV2`; when detected, the harness adds the `execute` tool to the agent’s available tools.
Use interpreters when the agent needs a lightweight programmable layer for loops, batching, deterministic data transformations, or programmatic tool calling. Interpreters do not provide shell access, package installs, or filesystem and network access.
For sandbox setup, providers, and file transfer APIs, see [Sandboxes](/oss/python/deepagents/sandboxes). For the QuickJS runtime and programmatic tool calling, see [Interpreters](/oss/python/deepagents/interpreters).

### Streaming

[Event streaming](/oss/python/deepagents/event-streaming) exposes agent runs as typed projections for messages, tool calls, values, and output. Deep Agents add `stream.subagents` so each delegated task gets its own handle with independent message, tool-call, and nested subagent streams.

## Context management

The context management component controls what the agent knows, how long it can operate within token limits, and what it retains across sessions. It has four layers:

* **[Skills](#skills)**: on-demand domain knowledge loaded progressively from skill files
* **[Memory](#memory)**: persistent instructions and preferences loaded at startup from `AGENTS.md` files
* **[Summarization and context offloading](#summarization-and-context-offloading)**: automatic compression of conversation history and large tool results
* **[Prompt caching](#prompt-caching)**: static prompt sections are cache-eligible to speed up inference and reduce cost on supported models

### Skills

Skills package specialized workflows, domain knowledge, and custom instructions for your deep agent.
Each skill follows the [Agent Skills standard](https://agentskills.io/) and lives in a directory with a `SKILL.md` file. Skills can also include scripts, templates, reference docs, and other supporting resources.
Deep Agents load skills with progressive disclosure: the agent reads `SKILL.md` frontmatter at startup, then reads full skill content only when a task needs it. This keeps startup context compact while still making rich capabilities available on demand.
For more information, see [Skills](/oss/python/deepagents/skills).

### Memory

Memory gives your deep agent persistent context across conversations, such as coding style, preferences, conventions, and project guidelines.
Memory uses [`AGENTS.md` files](https://agents.md/) that you pass through the `memory` parameter when creating the agent. Unlike skills, memory files are always loaded, and the content is stored in the configured backend (`StateBackend`, `StoreBackend`, or `FilesystemBackend`).
The agent can also update memory based on interactions and feedback, so preferences and patterns can carry forward without needing to restate them in each thread.
For configuration details and examples, see [Memory](/oss/python/deepagents/customization#memory). To generate a repository wiki that coding agents discover through `AGENTS.md`, see [OpenWiki](/oss/openwiki/overview).

### Summarization and context offloading

The harness manages context so deep agents can handle long-running work within token limits while keeping the most relevant information in scope.
This context flow has four parts:

* **Input context**: System prompt, memory, skills, and tool prompts define what the agent starts with.
* **Compression**: Built-in offloading and summarization compress conversation history and large intermediate results.
* **Isolation**: Subagents quarantine heavy subtasks and return only final results (see [Delegation](#delegation)).
* **Long-term memory**: Persistent storage in the virtual filesystem carries information across threads.

Together, these mechanisms support multi-step tasks that exceed a single context window while reducing manual context trimming and token usage.
For configuration details, see [Context engineering](/oss/python/deepagents/context-engineering). For multimodal inputs and tool outputs, see [Multimodal](/oss/python/deepagents/multimodal).

### Prompt caching

For Anthropic and Amazon Bedrock models, `create_deep_agent` automatically applies prompt caching to static sections of the system prompt—the base agent instructions, memory, and skill content that repeat on every turn. This avoids reprocessing the same tokens across calls, reducing both latency and cost on long-running agents.
Prompt caching is enabled by default when using an Anthropic model, or a Bedrock model (Claude or Nova). No configuration is required.
For other providers, see [Middleware integrations](/oss/python/integrations/middleware) for available provider-specific caching middleware.

## Delegation

The delegation component enables agents to break large problems into smaller, parallelizable units of work. It has two layers:

* **[Task planning](#task-planning)**: an opt-in `write_todos` tool for structured task tracking
* **[Subagents](#subagents)**: ephemeral child agents that handle isolated subtasks

### Task planning

Task planning is an opt-in harness capability that lets agents maintain a structured task list during execution.
Starting in v0.7 task planning is opt-in only. In earlier versions, task planning middleware was included by default.
Planning is often useful for:

* Long or complicated multi-step tasks
* Less capable models that benefit from an explicit accountability tool
* UIs that stream progress from agent state (see [Todo list](/oss/python/deepagents/frontend/todo-list))

Pass [`TodoListMiddleware`](https://reference.langchain.com/python/langchain/agents/middleware/todo/TodoListMiddleware) to the middleware parameter to give the agent a `write_todos` tool for maintaining a structured task list during execution.
Tasks support status tracking (`'pending'`, `'in_progress'`, `'completed'`) and are persisted in agent state. This gives agents a lightweight planning layer for organizing long-running and multi-step work.
For configuration options and behavior details, see [To-do list](/oss/python/langchain/middleware/built-in#to-do-list).

### Subagents

The harness includes a built-in `task` tool that lets the main agent create ephemeral subagents for isolated, long-running, multi-step, or parallel tasks.
Two subagent types are available: synchronous subagents (the default) block the supervisor until they return a single report, and [async subagents](/oss/python/deepagents/async-subagents) run in parallel and support mid-flight steering via launch, check, update, and cancel tools.
Subagent execution provides:

* **Isolated or inherited context**: By default, each invocation creates a new agent instance with its own context (`mode: "isolated"`). Use `mode: "fork"` to inherit the parent’s full conversation history instead. See [Forked subagents](/oss/python/deepagents/subagents#forked-subagents).
* **Autonomous execution**: The subagent runs independently until completion.
* **Single handoff**: It returns one final report to the main agent.
* **Configurable strategy**: Use the [default `general-purpose` subagent](/oss/python/deepagents/subagents#default-subagent) (enabled by default) or define [custom subagents](/oss/python/deepagents/subagents#custom-subagents).
* **Stateless messaging**: Subagents are stateless and cannot send multiple messages back.
* **Context and token efficiency**: Heavy subtask work stays isolated and is compressed into a compact result.

For more information, see [Subagents](/oss/python/deepagents/subagents). To remove the `task` tool, see [Running without subagents](/oss/python/deepagents/subagents#running-without-subagents).

## Steering

The steering component gives humans control over agent behavior at runtime and sets filesystem permissions for agent work.

### Human-in-the-loop

Deep Agents integrate with LangGraph interrupts so you can pause for approval on sensitive tool calls. Enable this behavior with the `interrupt_on` parameter in `create_deep_agent`.
`interrupt_on` accepts a mapping of tool names to interrupt configurations. For example, `interrupt_on={"edit_file": True}` pauses before every edit, letting you approve the call, add guidance, or modify tool inputs before execution.
This gives you a runtime safety and control layer for destructive operations, expensive API calls, and interactive debugging.
For more information, see [Human-in-the-loop](/oss/python/deepagents/human-in-the-loop).

## Get started

---
