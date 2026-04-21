---
type: proposal
sources:
  - raw/newsletters/2026-04-15-notions-token-town-5-rebuilds-100-tools-mcp-v.md
  - raw/newsletters/2026-04-18-ainews-the-two-sides-of-openclaw.md
  - raw/tweets/2026-04-21-garrytan-2044844654978642320.md
  - raw/tweets/2026-04-21-mattpocockuk-2044723788743360833.md
status: pending
created: 2026-04-21
---

# Proposal: Agentic orchestration patterns

## Summary

This batch sharpens a pattern the wiki only partly captures today: agent quality is increasingly coming from orchestration discipline rather than just better base models. Notion's "software factory" discussion, AINews' simple-harness / strong-evals synthesis, Garry Tan's ambiguity-gate example, and Matt Pocock's DDD / ADR framing all point to reusable orchestration patterns that should live in the wiki as a provider-agnostic workflow page.

## Intended changes

- [x] **Create** `wiki/workflows/agentic-orchestration-patterns.md` — reusable patterns for multi-agent systems and agent-supervised work
  > See full draft below.

- [x] **Update** `wiki/concepts/harness.md` — add a practical "what good harness engineering looks like" section
  > Add bullets on ambiguity gates, explicit scoped context, failure-metadata replanning, and eval-driven simplification.

- [x] **Update** `wiki/index.md` — add the workflow page and refresh counts
  > Add:
  > `- [[workflows/agentic-orchestration-patterns]] — reusable patterns for multi-agent systems: ambiguity gates, scoped context, failure-aware replanning, demos-over-memos, and eval-driven harness simplification *(as_of: 2026-04-21)*`

## Schema / vocabulary additions

- [x] **Add subcategory `agentic-orchestration-patterns`** to `wiki/_schema/subcategories.md`
  > ```
  > ### agentic-orchestration-patterns
  > - **Parent domain(s):** agents
  > - **Applies to types:** workflow | concept
  > - **Definition:** Reusable design patterns for orchestrating one or more agents across planning, delegation, evaluation, ambiguity handling, and recovery.
  > - **Examples:** [[workflows/agentic-orchestration-patterns]]
  > ```

## Page drafts

### wiki/workflows/agentic-orchestration-patterns.md (new)

```md
---
title: Agentic orchestration patterns
type: workflow
domains: [agents]
subcategory: agentic-orchestration-patterns
tags: [agentic]
as_of: 2026-04-21
sources: [notion-token-town, ainews-openclaw-2026-04-18]
---

# Agentic orchestration patterns

Reusable patterns for getting better behavior from one or more agents without depending on a single provider or model family. The central lesson from recent sources: simple harnesses, strong evals, explicit boundaries, and safer escalation logic often matter more than increasingly elaborate agent scaffolds.

## Current patterns

- **Ambiguity gates.** When the cost of guessing wrong is high, stop and ask instead of auto-continuing. Good for architecture forks, destructive operations, or underspecified user requests.
- **Scoped context, not global context.** Inject only the files, rules, or project context a sub-agent actually needs; keep the rest out of the loop to avoid context bleed.
- **Failure-aware replanning.** Don't blindly retry. Feed structured failure metadata back into the orchestrator so it can generate a different plan.
- **Eval-driven simplification.** Prefer the simplest harness that passes evals. A cleaner representation layer and stronger verification often beat "smarter-looking" orchestration.
- **Demos over memos.** Prototype working flows behind flags or internal demos before locking in a long design-document process.
- **Self-rebuild culture.** In fast-moving agent systems, teams must be willing to replace their own scaffolding repeatedly as model and environment capabilities change.

## Where these patterns surfaced

- Notion's AI team describes repeated rebuilds, internal-first prototyping, and careful decisions about when to use MCP versus tighter custom integrations.
- AINews' synthesis frames the current frontier as "simple harness, strong evals, model-agnostic scaffolding."
- Garry Tan's "confusion protocol" example shows ambiguity gating as a productized safety and productivity pattern.
- Matt Pocock's DDD/ADR framing suggests domain language and decision records make large codebases more navigable for both humans and agents.

## Failure modes

- Letting all agents share one bloated context by default
- Retrying the same failed plan with slightly different wording
- Confusing visible complexity in the harness with actual robustness
- Building cool tools with no concrete user journey or evaluation target

## Sources

- [[sources/newsletters/notion-token-town]]
- [[sources/newsletters/ainews-openclaw-2026-04-18]]
```

## Open questions

- If approved, do you want the Hermes-specific patterns later folded into this page as source-attributed examples, with the Hermes tool page kept shorter?
	- Please do this
