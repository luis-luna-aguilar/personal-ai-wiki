---
title: Skyflo
type: tool
domains: [agents, coding]
subcategory: agentic-devops
tags: [open-source, agentic]
as_of: 2026-04-24
sources: [agentic-devops-deep-research]
---

# Skyflo

Skyflo is a self-hosted AI control layer for Kubernetes and CI/CD workflows. Its core product idea is governance, not chat: natural-language intent is translated into typed infrastructure operations, but every mutating tool call pauses for explicit approval and the system verifies the result afterward.

## Current status (as of 2026-04-24)

- Official site describes Skyflo as approval-gated by design
- The platform's control loop is explicit: plan, approve, execute, verify
- Site copy says read operations flow freely while mutating operations require explicit human approval
- Official materials emphasize typed MCP-based execution, auditability, and self-hosted deployment

## Strengths

- One of the clearest concrete expressions of deterministic governance around infrastructure agents
- Strong fit for teams that want agents near production systems without pretending approval gates are optional
- More operationally serious than "chat with kubectl" wrappers

## Weaknesses / caveats

- The approval gate is the point, but it also limits full autonomy
- Current framing is heavily centered on Kubernetes and CI/CD workflows

## Sources

- [Agentic infrastructure and operations](../sources/deep-research/2026-04-24-agentic-devops.md)
