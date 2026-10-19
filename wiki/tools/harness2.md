---
title: Harness²
type: tool
domains: [agents]
subcategory: agent-framework
tags: [google, open-source, agentic]
as_of: 2026-10-09
sources: [harness2-recursive-harnessing-2026-10]
---

# Harness²

Google Cloud AI Research's open-source framework (Apache 2.0) for recursive agent harnessing. It improves a frozen model's harness on each new task without an answer key, and learns from that process to improve later tasks. Released 9 October 2026 with its paper. It is a research release, "not an officially supported Google product."

## Current status (as of 2026-10-09)

- **How it works:** each task gets one or more propose-probe-compose rounds. An editor writes a general-habits edit and a domain edit, both run on the same task, and only the edits that behave better than the reference run are kept. A lessons library (`EXPERIENCE.md` per adopted harness) carries forward to later tasks. See [Automated harness optimization](../concepts/automated-harness-optimization.md#recursive-harnessing-without-ground-truth).
- **Editable components:** system prompt, guardrails, memory, skills, tool guidance, scripts, subagents, and a middleware plugin, each mounted as a file.
- **Supports:** parallel and sequential recursion (`--k`, `--mode`), with OpenCode (default) and Codex executors. Includes setup for the JobBench, LAB, and WorkBuddy-Bench benchmarks, and a credential-free local demo (`harness2-demo`).
- **Reported results:** one round improved every benchmark in all four model–harness setups, with gains of up to +11.5 points on WorkBuddy-Bench (GLM-5 under OpenCode, 64.2→75.7).
- **Requirements:** Linux, Python 3.12, and uv; model-backed runs need Node.js 20+ and the Google Cloud CLI (Vertex AI).

## Caveats

- Executors run with unrestricted network access, and Codex runs with its sandbox disabled. Configure network restrictions before evaluating, because public benchmark rubrics are reachable online.
- Every round adds executions and editor sessions, which costs extra inference.

## Recent changes

- [2026-10-09] Page created from the Harness² paper and repository release.

## Sources

- [Harness²: Recursive Agent Harnessing for an Open World — Google Cloud AI Research](../sources/papers/harness2-recursive-harnessing-2026-10.md)
