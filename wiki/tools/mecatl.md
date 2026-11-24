---
title: Mecatl
type: tool
domains: [agents]
subcategory: agent-framework
tags: [open-source, agentic]
as_of: 2026-10-07
sources: [latent-space-stacklok-mecatl-2026-10-07]
---

# Mecatl

Mecatl is Stacklok's open-source "cloud-native harness", started on GitHub in June 2026. Stacklok was co-founded by Kubernetes co-creators Craig McLuckie and Joe Beda and pivoted from software supply-chain security to Kubernetes-based agent infrastructure. Mecatl rebuilds the coding-agent harness to run as server infrastructure that an enterprise operates centrally, rather than as a desktop tool moved into a VM. The name is an Aztec word for a cord or rope, pronounced "MEH-kah-tl".

## Current status (as of 2026-10-07)

- **Loop separated from everything it touches.** The agent loop runs independently of the client, model provider, state store, and execution environment. Sensitive operations (tool calls, bash) are split from the loop, and session management and memory move out of JSONL files on disk into managed systems.
- **Why not lift and shift.** Beda argues that desktop-first harnesses run the loop, local execution, and session state in one process, or one set of tightly coupled processes, even when they are pluggable. Moving that into a container or sandbox breaks the agent's lifecycle, for example pausing it safely while it waits for a person.
- **Enterprise governance.** Stacklok expects companies to own and govern agent conversations the way they govern email, and wants to reduce their dependence on frontier-lab harnesses such as Codex, Claude Code, and GitHub Copilot.
- **Surrounding stack.** Mecatl sits beside ToolHive (open-source MCP server management, now with a Kubernetes gateway, registry, and operator) and an AI Gateway for access control, budgets, reporting, and provider routing (not yet open source). The commercial product is the "enterprise spine": identity, authorization, policy, and auditing across the open-source parts. Customers are mostly regulated industries such as banks, semiconductor companies, and telcos.

## Why it matters

Mecatl is the clearest open-source statement of the cloud-native harness position on [Agent runtime platforms](../concepts/agent-runtime-platforms.md): the harness becomes a set of separately managed parts, as Kubernetes did for containers. [Pi](pi.md) Durable reaches a similar split from the opposite end, by making a minimal desktop harness crash-proof.

## Recent changes

- [2026-10-07] Page created from Latent Space's interview with McLuckie and Beda.

## Related

- [Agent runtime platforms](../concepts/agent-runtime-platforms.md) — durable and cloud-native harnesses
- [Pi](pi.md) — the minimal open-source harness Mecatl is contrasted with

## Sources

- [Latent Space — Can a cloud-native harness make agents reliable beyond the desktop? (Stacklok)](../sources/newsletters/latent-space-stacklok-mecatl-2026-10-07.md)
