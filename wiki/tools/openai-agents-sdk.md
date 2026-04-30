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

- [The next evolution of the Agents SDK](../sources/articles/openai-agents-sdk-evolution.md)
