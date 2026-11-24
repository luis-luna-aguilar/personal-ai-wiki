---
title: Model Hardware Standard
type: concept
domains: [agents, science]
tags: [anthropic, agentic]
as_of: 2026-08-27
sources: [model-hardware-standard-research-preview-2026-08-27]
---

# Model Hardware Standard

The Model Hardware Standard (MHS) is Anthropic's shared specification for AI agents to discover and safely operate physical devices: microscopes, liquid handlers, robot arms, and anything else with a programmable interface. It plays the role for lab and factory equipment that [MCP](mcp.md) plays for software tools: one standard way in, instead of a bespoke integration per device.

## Current status (as of 2026-08-27)

- Research preview opened 27 August 2026 to a first group of research labs and advanced manufacturers; begun with HHMI Janelia. Model-agnostic, and open-sourcing is promised after safety evaluations.
- A standard driver exposes simple read/write commands, makes each device discoverable on a network, and turns plain-language notes about a machine (an arm's weight, its safety limits) into a reference file the agent reads before operating it.
- Agents control devices through MCP, a command line, or code files, and can compile a learned procedure into a deterministic script. In testing, Claude aligned a laser by trial and observation through a camera, then wrote a one-command alignment script.
- Building support: AWS (Strands Robots), Automata, Danaher, Doosan Robotics, MBF Bioscience, QIAGEN, Tecan, Universal Robots; early adopters Hugging Face (LeRobot) and Raspberry Pi.
- Limits Anthropic names: Claude's physical reasoning still needs expert oversight, and devices without a programming interface are not supported yet.

## Why it matters

Anthropic says integration drops from weeks or months to hours or minutes. If that holds, the cost of wiring a [self-driving lab](../trends/ai-in-science.md) or a factory cell for agents falls sharply, and the open question for [physical AI](../trends/physical-ai-deployment.md) shifts from plumbing to validation and safety.

## Related

- [Model Context Protocol](mcp.md) — the software-side connector standard MHS builds on and parallels.
- [Claude app](../tools/claude-app.md) — Claude for Manufacturing defers equipment operation to MHS.

## Sources

- [Anthropic — Previewing the Model Hardware Standard](../sources/articles/model-hardware-standard-research-preview-2026-08-27.md)
