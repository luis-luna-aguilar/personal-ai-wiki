---
type: proposal
source: raw/tweets/2026-04-09-langchain-2039028327030079565.md
status: pending
created: 2026-04-09
---

# Proposal: LangChain trace-centered agent improvement loop

## Summary

LangChain posted a tweet pointing to a new conceptual guide: "The Agent Improvement Loop Starts with a Trace." The public X fetch only captured the teaser, so this proposal uses the linked article for the substantive claims: tracing is framed as the foundational primitive for improving agents, with a loop of traces → evals / human feedback → targeted fixes → offline validation → redeploy.

This reads more like a concept ingest than a product-launch ingest. The strongest wiki move is to add a concept page for the agent improvement loop, plus lightweight source summaries for both the tweet signal and the linked article.

## Intended changes

- [x] **Create** `wiki/concepts/agent-improvement-loop.md` — new concept page for the trace-centered improvement loop, online/offline eval split, and human-review role
    > See draft below.

- [x] **Create** `wiki/sources/tweets/langchain-trace-loop.md` — lightweight source summary for the LangChain tweet that surfaced the guide
    > See draft below.

- [x] **Create** `wiki/sources/articles/trace-agent-improvement-loop.md` — source summary for the linked conceptual guide
    > See draft below.

- [x] **Update** `wiki/index.md` — add the new concept page and refresh counts
    > See draft below.

## Page drafts

### wiki/concepts/agent-improvement-loop.md (new)

```markdown
---
title: Agent improvement loop
type: concept
domains: [agents]
tags: [agentic]
as_of: 2026-04-09
sources: [langchain-trace-loop, trace-agent-improvement-loop]
---

# Agent improvement loop

A trace-centered workflow for making agents better over time: collect traces of real behavior, enrich them with automated evals and human feedback, identify recurring failure patterns, make targeted prompt / code / workflow changes, validate them offline, then redeploy and repeat.

The core claim from LangChain's guide is that traces are not just a debugging artifact. They are the behavioral record that makes systematic agent improvement possible.

## Current status (as of 2026-04-09)

- LangChain is explicitly framing **tracing** as the foundational primitive for agent improvement, not a sidecar observability feature
- The loop spans both pre-production and production; production traces are treated as the most valuable source of real failure modes
- Online evals, offline evals, and human annotation are presented as complementary layers, not substitutes for each other
- The concept is vendor-promoted and closely tied to [[LangSmith]] in the source material, but the underlying loop is broader than any one product

## The loop

1. **Build and improve** — inspect failing or low-scoring traces, identify patterns, and make targeted prompt, code, routing, or workflow changes.
2. **Observe and debug (pre-production)** — run the updated agent in staging and confirm from traces that the intended fix behaves correctly.
3. **Offline evals** — turn recurring failures and annotated examples into reproducible test cases and datasets; compare before vs after results before shipping.
4. **Deploy** — ship the updated agent.
5. **Observe (in production)** — collect traces from real usage: inputs, outputs, tool calls, trajectories, latency, and token usage.
6. **Online evals and insights** — continuously score traces and cluster them into usage patterns, failure modes, and edge cases.
7. **Human annotations** — reviewers add ratings, corrections, and comments that improve the evaluators and create better offline datasets.

Each cycle compounds because better traces lead to better evals, which lead to better fixes, which create a better next generation of traces.

## Why traces matter

Traditional software is documented primarily by code. In agentic systems, code describes what the system is *allowed* to do, while traces show what it *actually did* on a real run with a real input and a real sequence of decisions.

A useful trace includes more than the final response. It captures the full trajectory: model calls, tool invocations, retrieval steps, intermediate outputs, and decision order. Once reviewers or evaluators enrich that trace, it becomes actionable evidence rather than a mere log.

## Online vs offline evals

- **Online evals** monitor live behavior continuously. They help surface drift, edge cases, and traces that should be reviewed by humans.
- **Offline evals** test a proposed fix against curated datasets before deployment. They are the guardrail against regressions.

The practical pattern is: use online signals to find what is going wrong, then encode those failure modes into offline evals so the next fix is measurable before it ships.

## Where human review still matters

The guide is explicit that automation does not remove the need for human judgment. Domain experts are still needed for nuanced failure modes where an LLM judge or deterministic check can miss the real issue. Reviewers can also create ground-truth outputs, calibrate online evaluators, and attach natural-language comments that help cluster failures later.

## Caveats

- This is a conceptual guide from LangChain, not an independent survey of tooling or a benchmark study.
- The article positions [[LangSmith]] as the natural platform that connects tracing, evals, insights, and annotation. The workflow itself is broader than LangSmith, but the source is product-adjacent.
- The strongest claim is about process discipline, not about a new algorithmic breakthrough.

## Recent changes

- [2026-04-09] Page created from LangChain's conceptual guide "The Agent Improvement Loop Starts with a Trace"

## Sources

- [[sources/tweets/langchain-trace-loop]]
- [[sources/articles/trace-agent-improvement-loop]]
```

### wiki/sources/tweets/langchain-trace-loop.md (new)

```markdown
---
title: LangChain tweet linking trace-centered agent improvement guide
type: source
source_type: tweet
source_file: raw/tweets/2026-04-09-langchain-2039028327030079565.md
url: https://x.com/LangChain/status/2039028327030079565
ingested: 2026-04-09
domains: [agents]
---

# LangChain tweet linking trace-centered agent improvement guide

LangChain posted a lightweight teaser for a new conceptual guide on agent improvement. The tweet's substantive claim is that the improvement loop starts with a trace: teams inspect what an agent actually did, enrich those traces with evals and human feedback, turn recurring failures into test cases, validate fixes, and repeat.

The public X fetch in `raw/tweets/` only captured the teaser page, so the linked article is the main factual source for the detailed claims.

## Influenced pages

- [[concepts/agent-improvement-loop]] — new concept page capturing the trace-centered loop

## Key claims extracted

- LangChain is promoting a conceptual frame: the agent improvement loop starts with tracing.
- The tweet links directly to a longer blog / docs-style guide with the detailed workflow.
- The post emphasizes three follow-on steps after tracing: evals, human feedback, and validation before redeploy.
```

### wiki/sources/articles/trace-agent-improvement-loop.md (new)

```markdown
---
title: The Agent Improvement Loop Starts with a Trace — LangChain
type: source
source_type: article
source_file: raw/articles/2026-04-09-langchaincom-conceptual-guides-traces-start-agent-improvemen.md
url: https://www.langchain.com/conceptual-guides/traces-start-agent-improvement-loop
ingested: 2026-04-09
domains: [agents]
---

# The Agent Improvement Loop Starts with a Trace — LangChain

LangChain argues that traces are the foundational primitive for improving agents. The guide lays out a seven-step loop: inspect traces, enrich them with automated evals and human review, turn recurring failures into offline test cases, validate fixes before release, deploy, collect new production traces, and repeat from a stronger baseline.

The article is part conceptual framework, part product positioning for LangSmith as the platform that ties together tracing, online evaluators, insights, annotation queues, datasets, and coding-agent access from the terminal.

## Influenced pages

- [[concepts/agent-improvement-loop]] — new concept page for the trace-centered improvement loop

## Key claims extracted

- In agentic systems, code shows what the system is allowed to do; traces show what it actually did on a real run.
- A useful trace includes the full execution trajectory: model calls, tool calls, retrieval steps, intermediate outputs, and decision sequence.
- The proposed loop is: build/improve, observe/debug in pre-production, run offline evals, deploy, observe in production, run online evals / insights, then add human annotations.
- Production traces are especially valuable because they expose real failure modes rather than hypothetical ones.
- Online evals are for continuous monitoring and surfacing failure patterns; offline evals are for validating a proposed fix before release.
- Human annotation is still needed for nuanced domains, calibrating evaluators, and creating ground-truth datasets.
- Recurring failures should become permanent offline tests so future changes do not reintroduce solved problems.
- LangSmith's online evaluators, Insights Agent, annotation queues, and CLI / Skills are positioned as the integrated implementation of this loop.
- The article claims LangSmith Skills can materially improve coding-agent performance on LangChain's internal eval set, but the number is vendor-reported and product-adjacent.

## Caveats

- Conceptual guide plus product positioning, not a neutral market map.
- No competitive comparison of tracing / eval platforms.
- Some performance claims are vendor-reported rather than independently replicated.
```

### wiki/index.md (updated)

```markdown
---
title: Wiki Index
type: index
as_of: 2026-04-09
---

# Wiki Index

Catalog of every page in the wiki. This file is the LLM's starting point for every query and every ingest — read it first to find relevant pages before drilling in.

When adding a new wiki page (via a proposal), add its index entry under the correct section. One line per page: wikilink + one-line description + `(as_of: YYYY-MM-DD)`.

---

## State of

Read-me-first dashboards per domain.

- [[state-of/coding]] — current state of AI coding tools and workflows *(as_of: 2026-04-09)*
- [[state-of/models]] — current state of foundation models *(as_of: —)*
- [[state-of/agents]] — current state of agentic systems and tool use *(as_of: 2026-04-09)*
- [[state-of/legal]] — current state of AI in legal practice *(as_of: 2026-04-09)*

## Models

Foundation models. One page per model family or generation.

- [[models/composer-2]] — Cursor's in-house frontier coding model; stub *(as_of: 2026-04-09)*

## Tools

Tools and products built on top of models. One page per tool.

- [[tools/cursor]] — Cursor 3 agentic coding workspace; multi-repo, local↔cloud agent handoff *(as_of: 2026-04-09)*
- [[tools/harvey]] — legal AI platform; thin stub from a single editorial source *(as_of: 2026-04-09)*
- [[tools/kiro]] — VS Code-based SDD tool, 3-doc workflow *(as_of: 2026-04-09)*
- [[tools/spec-kit]] — GitHub's CLI SDD scaffolder with slash commands *(as_of: 2026-04-09)*
- [[tools/stripe-cli]] — Stripe CLI's developer-preview `projects` workflow for provisioning and managing app-stack services across providers *(as_of: 2026-04-09)*
- [[tools/tessl]] — CLI + MCP framework exploring spec-as-source; private beta *(as_of: 2026-04-09)*

## Benchmarks

Benchmark pages. Current leaderboards and methodology.

_(empty)_

## Workflows

Reusable patterns and recipes.

- [[workflows/advisor-strategy]] — Anthropic's small-executor + Opus-advisor escalation pattern, now a server-side `advisor_20260301` tool on the Claude API *(as_of: 2026-04-09)*

## Concepts

Ideas and techniques (RAG, context engineering, compound engineering, etc.).

- [[concepts/agent-improvement-loop]] — trace-centered workflow for improving agents through evals, annotation, and regression testing *(as_of: 2026-04-09)*
- [[concepts/spec-driven-development]] — SDD concept, three-level taxonomy, critiques *(as_of: 2026-04-09)*

## Trends

Things being watched that haven't solidified yet.

- [[trends/agents-reshape-organizations]] — leverage moves from individual to org as autonomous agents take coordination work *(as_of: 2026-04-09)*

## Sources

See `wiki/sources/` — source summaries are not indexed here (they're many and cheap). Use `grep` or Glob when you need them.

---

## Page count

- state-of: 4 (3 populated, 1 skeleton)
- models: 1
- tools: 6
- benchmarks: 0
- workflows: 1
- concepts: 2
- trends: 1

**Total content pages: 11.** The wiki is in the bootstrap phase (<30 pages) — categorization discipline is relaxed.
```

## Schema / vocabulary additions

None.

## Open questions

- Should this stay as a concept-only ingest, or do you want a follow-up proposal that also creates a `LangSmith` tool page and a new observability/evals subcategory under `agents`?
	-  we keep it as is 
- The concept draft references `[[LangSmith]]` in prose because the article heavily centers it. If you want to avoid a red link here, I should either remove that wikilink or draft the corresponding tool page next.
	-  please remove that link. There is no page for that 

## Comments

- The tweet is a means to an end. What matters is really what's in the article and the concepts and stuff. Even mentioning the tweet in the proposal makes no sense; it doesn't matter where the information came from, The wiki is about the information itself.

- When I was reading the concept of the agent improvement loop, I was thinking of traces like logs for apps. I was thinking of all that and at some point you started talking about capturing the model calls and tool invocations. I realized it is about tracing when using AI models in systems and applications. That was not clear in the intro of the article so it needs to be clear 

- I think that concept page can be more concise. It's too long to say or to describe one concept. We can be more concise 

- If a tweet just points to an article and the article actually contains the body of the information, the tweet is irrelevant. I think we can just get rid of that as a source and adjust our LM instructions to consider that. If a tweet has an article that backs it up, we can ignore the tweet's content and just register it as an article 

- We're supposed to show only the diff in the index so that I can clearly see what changed, or in any other page that was updated. You are sending me the whole index. That's not cool. Stick to the instructions please 
