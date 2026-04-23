---
title: Google ADK
type: tool
domains: [agents]
subcategory: agent-framework
tags: [google, open-source, agentic]
as_of: 2026-04-23
sources: [google-adk, legacy-ai-tools-roadmap-xlsx, google-cloud-next-2026]
---

# Google ADK

Google ADK is Google's open-source Agent Development Kit for building and running custom agents. It sits in the agent-framework layer: not a consumer assistant, but a developer toolkit for tool calling, agent composition, and deployment patterns.

## Current status (as of 2026-04-23)

- Official Google framework for custom agent development; now positioned as the open-source developer layer inside the broader Gemini Enterprise Agent Platform
- Agent Studio provides a low-code wrapper over ADK primitives for teams that want a hosted UI rather than only raw SDK usage
- ADK is now framed as graph-based: agents can be organized into networks of sub-agents with deterministic and generative orchestration patterns
- Google says 6 trillion tokens per month are already processed through ADK on Gemini models, which is meaningful production-scale evidence rather than only framework marketing
- Open-source and documentation-led; the ADK layer itself remains available independently of the larger hosted platform
- Positioned for multi-agent patterns, tool use, and production-oriented agent development on Google infrastructure

## Strengths

- Clear fit for teams that want Google's agent primitives without only using a consumer assistant surface
- Strong interoperability story with adjacent Google ecosystem tools and protocols

## Weaknesses / caveats

- Framework layer, not an opinionated end-user product
- Real-world differentiation vs other agent SDKs depends on ecosystem fit more than novelty alone

## Sources

- [[sources/articles/google-adk]]
- [[sources/notes/legacy-ai-tools-roadmap-xlsx]]
- [[sources/articles/google-cloud-next-2026]]
