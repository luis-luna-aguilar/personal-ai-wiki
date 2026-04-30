---
title: K8sGPT
type: tool
domains: [agents, coding]
subcategory: agentic-devops
tags: [open-source, cli, agentic]
as_of: 2026-04-24
sources: [agentic-devops-deep-research]
---

# K8sGPT

K8sGPT is a Kubernetes diagnostic tool that scans cluster state and explains problems in plain English. It matters to agentic operations because it acts as a structured diagnostic surface: a way for humans or agents to query Kubernetes issues without translating raw cluster noise manually every time.

## Current status (as of 2026-04-24)

- Official README positions K8sGPT as a tool for scanning, diagnosing, and triaging Kubernetes issues
- Docs pitch it as "Kubernetes SRE superpowers"
- Supports multiple model backends and exposes an MCP-related integration surface in the docs/README
- Available both as CLI tooling and deeper cluster/operator-style usage

## Strengths

- Clear diagnostic use case rather than vague agent-platform positioning
- Useful as a reusable skill surface inside a broader agentic infrastructure stack
- Good bridge between traditional kubectl-heavy ops work and agent-friendly workflows

## Weaknesses / caveats

- Kubernetes-specific rather than a general infrastructure tool
- Best understood as diagnosis/triage infrastructure, not as a full agent runtime or control plane

## Sources

- [Agentic infrastructure and operations](../sources/deep-research/2026-04-24-agentic-devops.md)
