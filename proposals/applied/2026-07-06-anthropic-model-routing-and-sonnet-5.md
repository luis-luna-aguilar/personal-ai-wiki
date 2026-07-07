---
type: proposal
sources:
  - raw/newsletters/2026-07-02-ainews-not-much-happened-today.md
  - raw/newsletters/2026-07-02-vibe-check-sonnet-5a-model-pitched-for-everyone.md
  - raw/newsletters/2026-07-02-cognition-ships-devin-for-security.md
  - raw/newsletters/2026-07-05-a-tale-of-two-models.md
status: pending
created: 2026-07-06
---

# Proposal: Fable 5 returns and Sonnet 5 changes Anthropic model routing

## Summary

Fable 5 is no longer accurately described as globally suspended: the July 2-5 newsletter batch reports it back online, with visible safety fallback routing to Opus 4.8 for some cyber/biology/chemistry requests. Sonnet 5 also deserves a separate current-state page because multiple sources frame it as competent but awkwardly positioned: cheaper by token rate, but often more expensive per finished task at higher effort.

## Intended changes

- [x] **Update** `wiki/models/claude-fable-5.md` - replace the suspension-current-state with a re-enabled-but-routed status.
    > **Before:** "Access is suspended globally under new U.S. export-control restrictions."
    > **After:** "Access is re-enabled as of 2026-07-02, but Anthropic is applying safety fallback routing that may send some cyber, biology, or chemistry requests to Opus 4.8."

- [x] **Create** `wiki/models/claude-sonnet-5.md` - new model page for the mid-tier Claude 5 release.

- [x] **Update** `wiki/state-of/models.md` - remove stale "Fable suspended" wording; add Sonnet 5 as a middle-tier model with cost/performance caveat.

- [x] **Update** `wiki/state-of/coding.md` - change the Claude Code/Fable line from "suspended" to "available with fallback routing"; note Sonnet 5's cost-per-task caveat.

- [x] **Create** source summaries:
    - `wiki/sources/newsletters/ainews-not-much-happened-2026-07-02.md`
    - `wiki/sources/newsletters/every-sonnet-5-vibe-check-2026-07-02.md`
    - `wiki/sources/newsletters/the-code-devin-security-2026-07-02.md`
    - `wiki/sources/newsletters/every-tale-of-two-models-2026-07-05.md`

## Page drafts

### wiki/models/claude-fable-5.md (snippet)

```md
## Current status (as of 2026-07-02)
- Re-enabled after the June 2026 suspension, with demand immediately returning across coding-tool vendors.
- Anthropic is applying updated safety fallback routing: some cyber, biology, and chemistry requests may route to Opus 4.8 instead of Fable 5.
- Cursor reports Fable 5 still leads its internal coding evals but is the most expensive per completed task.
- Devin, Perplexity, Cursor, and other tooling surfaces restored Fable 5 shortly after relaunch.
- The operational lesson is model-routing resilience: teams should not build critical coding workflows around one frontier model with no fallback.

## Recent changes
- [2026-07-02] Fable 5 returned online; Anthropic added visible safety fallback routing to Opus 4.8 for some sensitive domains; major coding tools restored access.
```

### wiki/models/claude-sonnet-5.md (new)

```md
---
title: Claude Sonnet 5
type: model
domains: [models, coding]
subcategory: frontier-multimodal-model
tags: [anthropic]
as_of: 2026-07-02
sources: [every-sonnet-5-vibe-check-2026-07-02, the-code-devin-security-2026-07-02, every-tale-of-two-models-2026-07-05]
---

# Claude Sonnet 5

Claude Sonnet 5 is Anthropic's middle-tier Claude 5 model, positioned as a default model for broad daily work: more capable than smaller utility tiers, cheaper on paper than Opus, and more available than Fable for many users.

## Current status (as of 2026-07-02)
- Every's Vibe Check found Sonnet 5 broadly competent at writing, structured knowledge work, and some coding tasks, but hard to prefer over Opus 4.8, Fable 5, or GPT-5.5 for many specific jobs.
- The Code reports the model can cost more per finished task than expected because the same work may tokenize larger and run more reasoning loops.
- Artificial Analysis coverage cited by The Code says high-effort Sonnet 5 can cost about 15% more per task than Opus 4.8, while lower effort settings remain cheaper.
- Ramp Labs' benchmark coverage suggests the extra effort can buy tighter self-correction, so the right comparison is cost per completed task, not token list price.

## Strengths
- Solid default for general drafting, analysis, and medium-complexity coding.
- Better self-correction when effort is raised.
- Useful as an available middle tier when Fable access is constrained or overkill.

## Weaknesses / caveats
- Weak product positioning: many tasks have a cheaper, faster, or stronger model option.
- Cost can exceed the nominally more expensive Opus tier when effort is left high.
- Early Every testing found weaker agentic build performance than stronger Claude models.

## Recent changes
- [2026-07-02] Every and The Code reported early testing: capable but not clearly best-in-class; cost per task depends heavily on effort and tokenizer behavior.

## Sources
- [Every - Sonnet 5 Vibe Check](../sources/newsletters/every-sonnet-5-vibe-check-2026-07-02.md)
- [The Code - Devin Security / Sonnet 5 cost analysis](../sources/newsletters/the-code-devin-security-2026-07-02.md)
- [Every - A Tale of Two Models](../sources/newsletters/every-tale-of-two-models-2026-07-05.md)
```

### wiki/state-of/models.md (snippet)

```md
### Frontier multimodal models
- [Claude Fable 5](../models/claude-fable-5.md) - Anthropic's leading coding-capable frontier model; re-enabled with safety fallback routing to Opus 4.8 for some sensitive domains *(as of 2026-07-02)*
- [Claude Sonnet 5](../models/claude-sonnet-5.md) - Anthropic middle-tier default; competent but early testing flags unclear model fit and higher cost per finished task at high effort *(as of 2026-07-02)*

## Recent changes
- [2026-07-02] Fable 5 returned online with safety fallback routing; Sonnet 5 arrived as Anthropic's middle-tier Claude 5 model but early testing questioned its cost/performance positioning.
```

### wiki/state-of/coding.md (snippet)

```md
- [Claude Code](../tools/claude-code.md) - Anthropic terminal coding agent; Fable 5 is available again but sensitive-domain requests may fall back to Opus 4.8, making model-routing resilience part of the coding-agent operating model *(as of 2026-07-02)*

## Recent changes
- [2026-07-02] Fable 5 returned to coding-tool surfaces; Sonnet 5 testing reinforced cost-per-completed-task as a better routing metric than token list price.
```

### Source summaries (new)

```md
---
title: AINews - not much happened today
type: source
source_type: newsletter
source_file: raw/newsletters/2026-07-02-ainews-not-much-happened-today.md
published: 2026-07-02
ingested: 2026-07-06
domains: [models, coding, agents]
---

# AINews - not much happened today

AINews summarizes Fable 5's relaunch, tool-vendor restoration, GLM-5.2/ZCode momentum, OpenWiki, Devin Security Swarm, emerging agent eval tooling, and inference-systems work.

## Influenced pages
- [Claude Fable 5](../../models/claude-fable-5.md) - relaunch and fallback routing
- [GLM-5.2](../../models/glm-5-2.md) - ZCode and APEX-SWE updates
- [Agent evals](../../concepts/agent-evals.md) - eval tooling and reporting layer

## Key claims extracted
- Fable 5 returned online with safety fallback routing to Opus 4.8 for some sensitive requests.
- Cursor, Devin, and Perplexity restored Fable 5 into product surfaces.
- Z.ai launched ZCode around GLM-5.2.
- Agent evaluation and AI incident reporting are emerging as infrastructure layers.
```

```md
---
title: Every - Sonnet 5 Vibe Check
type: source
source_type: newsletter
source_file: raw/newsletters/2026-07-02-vibe-check-sonnet-5a-model-pitched-for-everyone.md
published: 2026-07-02
ingested: 2026-07-06
domains: [models, coding]
---

# Every - Sonnet 5 Vibe Check

Every tested Claude Sonnet 5 across coding, writing, knowledge work, and agent behavior, concluding that it is competent but not clearly preferable to Opus 4.8, Fable 5, or GPT-5.5 for many tasks.

## Influenced pages
- [Claude Sonnet 5](../../models/claude-sonnet-5.md) - positioning and caveats
- [State of Models](../../state-of/models.md) - middle-tier Claude model note

## Key claims extracted
- Sonnet 5 can write, analyze, and code competently.
- Early Every testers found it hard to choose over better-specialized alternatives.
- Coding and agentic-build tests exposed cases where stronger Claude models performed better.
```

```md
---
title: The Code - Cognition ships Devin for Security
type: source
source_type: newsletter
source_file: raw/newsletters/2026-07-02-cognition-ships-devin-for-security.md
published: 2026-07-02
ingested: 2026-07-06
domains: [coding, agents, cybersecurity, models]
---

# The Code - Cognition ships Devin for Security

The Code covers Devin Security Swarm, ZCode for GLM-5.2, Sonnet 5 cost-per-task concerns, Fable 5 orchestration tactics, OpenWiki, and continuous eval pipeline resources.

## Influenced pages
- [Claude Sonnet 5](../../models/claude-sonnet-5.md) - cost-per-task caveat
- [Devin](../../tools/devin.md) - Security Swarm
- [GLM-5.2](../../models/glm-5-2.md) - ZCode ecosystem

## Key claims extracted
- Sonnet 5 can cost more per completed task than its list price implies.
- Devin Security Swarm uses parallel agents, sandbox reproduction, and PR generation for vulnerabilities.
- ZCode is an official GLM-5.2 coding environment with long-running sessions.
```

```md
---
title: Every - A Tale of Two Models
type: source
source_type: newsletter
source_file: raw/newsletters/2026-07-05-a-tale-of-two-models.md
published: 2026-07-05
ingested: 2026-07-06
domains: [models, science]
---

# Every - A Tale of Two Models

Every frames the week as Fable 5's return versus Sonnet 5's underwhelming positioning, and also summarizes Anthropic's Claude Science launch and internal drug-program dogfooding strategy.

## Influenced pages
- [Claude Fable 5](../../models/claude-fable-5.md) - relaunch signal
- [Claude Sonnet 5](../../models/claude-sonnet-5.md) - Vibe Check synthesis
- [Claude Science](../../tools/claude-science.md) - product and dogfooding strategy

## Key claims extracted
- Fable 5 came back online and remains a preferred Every model for ambitious coding/product work.
- Sonnet 5 landed as a competent but hard-to-recommend middle-tier model.
- Anthropic is using internal drug programs to test and improve Claude Science.
```

## Open questions

- Should Sonnet 5 use `frontier-multimodal-model` despite being positioned below Opus/Fable, or should we propose a new `mid-tier-frontier-model` subcategory later if more pages cluster around this tier?
	- just frontier model, all frontier models are multimodal, so refactor this wiki to just make the tags frontier-model.
