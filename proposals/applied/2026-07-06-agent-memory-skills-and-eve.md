---
type: proposal
sources:
  - raw/newsletters/2026-07-02-ainews-not-much-happened-today.md
  - raw/newsletters/2026-07-02-skill-engineering-and-the-case-against-one-shot-ai.md
  - raw/newsletters/2026-07-03-vercels-andrew-qu-on-why-agents-are-a-new-kind-of.md
status: pending
created: 2026-07-06
---

# Proposal: Agent memory, skill engineering, and Vercel eve

## Summary

Three approved topics converge around maintained context: OpenWiki and wiki memory for codebases, skill engineering as portable operating knowledge, and Vercel's eve as a framework for resumable agent software. This proposal creates lightweight tool pages for OpenWiki, Impeccable, and eve, and updates the existing knowledge-layer and skill-methodology pages.

## Intended changes

- [x] **Create** `wiki/tools/openwiki.md` - LangChain codebase documentation for agents.
- [x] **Create** `wiki/tools/impeccable.md` - open-source design skills system.
- [x] **Create** `wiki/tools/eve.md` - Vercel agent framework.
- [x] **Update** `wiki/concepts/knowledge-layer.md` - add maintained codebase docs and memory reconciliation.
- [x] **Update** `wiki/training/agent-skill-methodology.md` - add cross-harness skill engineering guidance from Impeccable and Vercel.
- [x] **Update** `wiki/state-of/agents.md` - add eve under agent frameworks and OpenWiki/skills as context-layer signals.
- [x] **Create** source summaries:
    - `wiki/sources/newsletters/skill-engineering-impeccable-2026-07-02.md`
    - `wiki/sources/newsletters/vercel-agents-new-software-2026-07-03.md`
- [x] **Update** `wiki/index.md` - add new tool pages.

## Page drafts

### wiki/tools/openwiki.md (new)

```md
---
title: OpenWiki
type: tool
domains: [agents, coding]
subcategory: agent-toolkits
tags: [open-source, agentic]
as_of: 2026-07-02
sources: [ainews-not-much-happened-2026-07-02, the-code-devin-security-2026-07-02]
---

# OpenWiki

OpenWiki is a LangChain tool for generating and maintaining agent-consumable documentation for a codebase. It fits the emerging "wiki memory" pattern: agents need maintained, inspectable knowledge layers rather than only raw transcripts or retrieval over stale files.

## Current status (as of 2026-07-02)
- AINews reports launch usage around `openwiki --init`.
- The Code frames it as a CLI that writes and maintains codebase documentation for agents.
- The tool is relevant to teams trying to make codebase context durable across threads and agents.

## Strengths
- Gives agents a structured codebase map that can be inspected and updated.
- Aligns with wiki-style memory rather than opaque vector-only recall.

## Weaknesses / caveats
- Current proposal is based on newsletter coverage; fetch the repository before applying detailed command or architecture claims.

## Recent changes
- [2026-07-02] LangChain launched OpenWiki as an agent-readable codebase documentation tool.

## Sources
- [AINews - not much happened today](../sources/newsletters/ainews-not-much-happened-2026-07-02.md)
- [The Code - Cognition ships Devin for Security](../sources/newsletters/the-code-devin-security-2026-07-02.md)
```

### wiki/tools/impeccable.md (new)

```md
---
title: Impeccable
type: tool
domains: [creative, agents]
subcategory: visual-design-prototyping
tags: [open-source, agentic]
as_of: 2026-07-02
sources: [skill-engineering-impeccable-2026-07-02]
---

# Impeccable

Impeccable is an open-source design-agent skill system. Its skill-engineering method: encode domain vocabulary, exact levels of control, and reusable evaluation language so agents can make design decisions more reliably.

## Current status (as of 2026-07-02)
- Presented as an example of skill engineering for design agents.
- Emphasizes steerable design vocabulary and reusable constraints rather than one-shot prompting.
- Relevant to cross-harness skills because the same design judgment can be packaged for multiple agent environments.

## Strengths
- Turns fuzzy design preferences into explicit reusable instructions.
- Useful as a concrete example of "skills as portable operating knowledge."

## Weaknesses / caveats
- Current source is newsletter coverage; verify repository details before treating it as a durable tool page.

## Recent changes
- [2026-07-02] Added as an emerging design-agent skill system and methodology example.

## Sources
- [The Code - Skill engineering and the case against one-shot AI](../sources/newsletters/skill-engineering-impeccable-2026-07-02.md)
```

### wiki/tools/eve.md (new)

```md
---
title: eve
type: tool
domains: [agents]
subcategory: agent-framework
tags: [agentic]
as_of: 2026-07-03
sources: [vercel-agents-new-software-2026-07-03]
---

# eve

eve is Vercel's framework for building agents, described by Andrew Qu as the result of Vercel turning hard-won v0 and internal-agent patterns into reusable primitives.

## Current status (as of 2026-07-03)
- Built around agent primitives Vercel found missing: model/provider switching, fallbacks, resumability, filesystem agents, skills, compaction, subagents, sandboxes, and long-running jobs.
- Deploying eve to Vercel is described as providing observability and evaluations out of the box.
- Vercel frames agents as a new kind of software with dynamic interfaces and outputs, not just web apps with an AI layer.

## Strengths
- Strong platform fit: Vercel is building eve from production experience with v0 and internal agents.
- Emphasizes resumability, long-running work, and current product knowledge through skills.

## Weaknesses / caveats
- Current source is interview coverage rather than official docs.
- It is not yet clear how much of the framework is public, stable, or broadly adopted.

## Recent changes
- [2026-07-03] Andrew Qu described eve as Vercel's prescriptive agent framework.

## Sources
- [Vercel's Andrew Qu on why agents are a new kind of software](../sources/newsletters/vercel-agents-new-software-2026-07-03.md)
```

### wiki/concepts/knowledge-layer.md (snippet)

```md
## Current status (as of 2026-07-06)
- Wiki-style memory is moving from personal agent folders into explicit tooling: LangChain's OpenWiki generates and maintains codebase docs meant for agents to consume.
- Maintained memory is distinct from retrieval-only memory. Weaviate's Engram framing points toward extracting candidate memories, reconciling them against existing memory, and committing a cleaned version so contradictions are resolved before query time.
- The common design direction is inspectable, editable, permission-aware knowledge that agents can share across sessions instead of hidden vector recall or one giant transcript.

## Recent changes
- [2026-07-02] OpenWiki and Engram-style memory reconciliation reinforced the shift from raw logs/retrieval toward maintained, agent-readable knowledge layers.
```

### wiki/training/agent-skill-methodology.md (snippet)

```md
## Current guidance
- Treat skills as portable operating knowledge, not only prompt snippets. Vercel uses skills to forward-correct stale model knowledge about deprecated products, while Impeccable-style design skills encode domain vocabulary and levels of control.
- Good skills name the decision language the agent should use: quality adjectives, acceptable ranges, examples, anti-examples, and what "do not auto-fix" means in that domain.
- Cross-harness skills should avoid tool-specific assumptions unless the skill is explicitly packaged for one runtime.

## Recent changes
- [2026-07-03] Vercel eve interview and Impeccable coverage reinforced skills as a current-knowledge and domain-judgment layer across agent harnesses.
```

### Source summaries (new)

```md
---
title: The Code - Skill engineering and the case against one-shot AI
type: source
source_type: newsletter
source_file: raw/newsletters/2026-07-02-skill-engineering-and-the-case-against-one-shot-ai.md
published: 2026-07-02
ingested: 2026-07-06
domains: [agents, creative, training]
---

# The Code - Skill engineering and the case against one-shot AI

The Code covers skill engineering as a reusable method for improving agent behavior, including Impeccable as a design-agent example.

## Influenced pages
- [Agent skill methodology](../../training/agent-skill-methodology.md) - portable operating knowledge
- [Impeccable](../../tools/impeccable.md) - design skill system

## Key claims extracted
- One-shot prompting is too brittle for repeated high-quality design work.
- Skills can encode domain vocabulary, constraints, and control levels.
- Design agents benefit from explicit steerability rather than generic taste prompts.
```

```md
---
title: Vercel's Andrew Qu on why agents are a new kind of software
type: source
source_type: newsletter
source_file: raw/newsletters/2026-07-03-vercels-andrew-qu-on-why-agents-are-a-new-kind-of.md
published: 2026-07-03
ingested: 2026-07-06
domains: [agents, computer-use]
---

# Vercel's Andrew Qu on why agents are a new kind of software

Latent Space interviews Andrew Qu on Vercel's agent work, eve, skills, resumability, agent-readable websites, and Vercel's shift toward making the platform itself agent-friendly.

## Influenced pages
- [eve](../../tools/eve.md) - Vercel agent framework
- [Agent skill methodology](../../training/agent-skill-methodology.md) - skills as current knowledge
- [Agent-readable web](../../trends/agent-readable-web.md) - Markdown/machine-readable website experiences

## Key claims extracted
- Agents need primitives beyond web apps: context, tools, resumability, long-running work, skills, and sandboxes.
- Vercel serves Markdown directly when it detects agent requests.
- Vercel sees agents as both a product category and a capability embedded across the platform.
```

## Open questions

- If OpenWiki becomes central, should it use `agent-toolkits` or should we later add a narrower `agent-knowledge-layer` subcategory?
	- Keep it as is.
