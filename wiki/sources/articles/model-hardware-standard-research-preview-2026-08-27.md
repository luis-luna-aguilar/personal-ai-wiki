---
title: Anthropic — Previewing the Model Hardware Standard
type: source
source_type: article
source_file: raw/articles/2026-11-23-anthropiccom-news-model-hardware-standard-research-preview.md
url: https://www.anthropic.com/news/model-hardware-standard-research-preview
published: 2026-08-27
ingested: 2026-11-23
domains: [agents, science]
---

# Anthropic — Previewing the Model Hardware Standard

Anthropic's announcement of a research preview of the Model Hardware Standard (MHS), a shared specification for AI agents to safely operate physical devices, begun with HHMI Janelia and opened first to research labs and advanced manufacturers. A standard driver gives any programmable device simple read/write commands, network discoverability, and a generated reference file describing what it measures, what can be adjusted, and which safety limits are enforced. Agents control devices via MCP, a command line, or code files. Anthropic plans safety evaluations with partners before open-sourcing the standard.

## Influenced pages
- [Model Hardware Standard](../../concepts/model-hardware-standard.md) — new concept page: definition, mechanism, partners, limits
- [Physical AI deployment curve](../../trends/physical-ai-deployment.md) — short current-status bullet and What-to-watch note linking the MHS page
- [AI in Science](../../trends/ai-in-science.md) — short self-driving-labs mention of MHS as shared instrument plumbing
- [Claude app](../../tools/claude-app.md) — Claude for Manufacturing bullet's MHS clause links the MHS page

## Key claims extracted
- Research preview opened 2026-08-27 to a first group of scientific research labs and advanced manufacturers; began as a collaboration between Anthropic and HHMI Janelia Research Campus.
- Lets agents operate multiple lab and manufacturing instruments (microscopes, liquid handlers, robotic arms) in parallel; examples range from routine drug-discovery experiments to laser calibration on a quantum computer.
- Hardware setup typically takes weeks or months; Anthropic says MHS reduces integration to hours or minutes. Agents can reason through each experimental step, update parameters in real time, and in some cases recover from hardware errors without intervention.
- Works with any device that has a programmable interface; model-agnostic; any agent harness can access it through standard protocols such as MCP.
- Standard driver uses read/write primitives and makes devices discoverable in a standard format. Natural-language tags (written by the user or via an agent interview) capture characteristics code can't show, such as a robot arm's weight; the driver generates a reference file of measurable quantities, adjustable settings, and enforced safety limits.
- Three control mechanisms: MCP, command line, code files (APIs). The agent can chain driver commands into code files for long-running or fast operations without reasoning at each step.
- In testing, Claude adjusted a laser, observed the beam through a camera, iterated, then wrote a deterministic script that aligns the laser as a single command.
- Vendors adding support: AWS (Strands Robots, private pre-release package for participants), Automata (LINQ), Danaher (exploring), Doosan Robotics (robot-arm QA and multi-robot coordination), MBF Bioscience (ScanImage driver), QIAGEN (QIAsymphony Connect proof of concept), Tecan (Fluent liquid handlers), Universal Robots (plans support). Early adopters: Hugging Face (LeRobot), Raspberry Pi (Camera MHS Driver).
- Limits: Claude's spatial and physical reasoning still requires expert oversight (Genentech had to guide Claude to recognize foaming errors as physical failures); devices without a programming interface are not yet supported.
- Anthropic will build safety evaluations with launch partners, is developing a physical safety roadmap, and will release research-preview findings as deployment guidance when it open-sources MHS.
