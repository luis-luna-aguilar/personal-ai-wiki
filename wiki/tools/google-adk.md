---
title: Google ADK
type: tool
domains: [agents]
subcategory: agent-framework
tags: [google, open-source, agentic]
as_of: 2026-04-24
sources: [google-adk, legacy-ai-tools-roadmap-xlsx, google-cloud-next-2026, googlecloudtech-adk-2-orchestration-patterns]
---

# Google ADK

Google ADK is Google's open-source Agent Development Kit for building and running custom agents. It sits in the agent-framework layer: not a consumer assistant, but a developer toolkit for tool calling, agent composition, and deployment patterns.

## Current status (as of 2026-04-24)

- Official Google framework for custom agent development; now positioned as the open-source developer layer inside the broader Gemini Enterprise Agent Platform
- ADK 2.0 is explicitly framed around graph-based workflows: teams can mix deterministic nodes (business rules, compliance checks, branching logic) with AI-driven nodes inside one directed workflow instead of burying procedure in prompts
- Google is pushing a coordinator-specialist model for multi-agent systems rather than "god agents": smaller specialists with separate tools, identity, and memory, routed by a coordinator
- The new Skills framework makes skills first-class reusable building blocks; `SkillToolset` lets agents compose skills as tools, with progressive disclosure so full skill context loads only when invoked
- Google is positioning A2A as the cross-language delegation layer for ADK: Python, TypeScript, Go, and Java agents can discover each other via Agent Cards and hand off work across teams without bespoke protocol glue
- Secure workspaces are part of the runtime story for code-executing agents: sandboxed file access, restricted networking, command allowlists, and hard execution/resource limits
- Google says 6 trillion tokens per month are already processed through ADK on Gemini models, which is meaningful production-scale evidence rather than only framework marketing

## Strengths

- Clear fit for teams that want Google's agent primitives without only using a consumer assistant surface
- Strong interoperability story with adjacent Google ecosystem tools and protocols
- More explicit orchestration story than many agent SDKs: graph control, agent handoff, skill composition, and sandboxing are now described as one coherent stack
- Better fit for heterogeneous enterprise teams because Google is treating cross-language delegation as a first-class capability rather than an afterthought

## Weaknesses / caveats

- Framework layer, not an opinionated end-user product
- Real-world differentiation vs other agent SDKs depends on ecosystem fit more than novelty alone
- The strongest ADK 2.0 details here come from a long Google social thread rather than a cleaner canonical article
- Production-scale claims and architecture examples are still mostly Google-framed rather than independently benchmarked against other SDKs

## Recent changes

- [2026-04-24] ADK 2.0 orchestration details clarified: hybrid graph workflows, coordinator-specialist collaboration, first-class skill composition, cross-language A2A delegation, and sandboxed secure workspaces

## Sources

- [Google Agent Development Kit docs](../sources/articles/google-adk.md)
- [AI Tools & Roadmap legacy workbook](../sources/notes/legacy-ai-tools-roadmap-xlsx.md)
- [Google Cloud Next 2026 — TPU v8 and Gemini Enterprise Agent Platform](../sources/articles/google-cloud-next-2026.md)
