---
type: proposal
source: raw/newsletters/2026-07-30-ontologies-are-so-back-why-ai-agents-are-reviving.md
status: pending
created: 2026-09-07
---

# Proposal: Ontologies as agent guardrails

## Summary

### The source

Latent Space's July 30 recap covers a talk by Frank Coyle — a UC Berkeley computer science professor who teaches generative AI and LLMs — given at the AI Engineer World's Fair. Coyle's argument is that while LLMs are strong probabilistic reasoners, agentic systems that act in loops need something more deterministic to keep them from drifting off track: ontologies. An ontology, in the simplest framing he uses, is "data as graphs" — a structured description of the entities and relationships in a domain, a concept he traces back to Aristotle and, more directly, to Semantic-Web-era standards like Schema.org, RDFS, and OWL. His practical point is that these standards are already baked into LLM training data, so a team can prompt for them rather than inventing a domain ontology from scratch, and he demonstrated a Claude agent using an ontology to validate its own reasoning after a tool call. Neo4j CEO Emil Eifrem added a production framing: three ontology layers (business-facing concepts, technical/metadata, and runtime execution traces) let agents run on a shared semantic substrate instead of each agent being hand-wired to its own data sources. OpenLink's Kingsley Idehen, building an "agent with RDF memory," framed the pairing as ontologies giving language "computable context." The piece is candid about the historical failure mode — ontology maintenance is why the 1990s/2000s Semantic Web vision never took off — and reports one proposed fix (an agent maintaining its own ontology as it hits edge cases) without treating it as solved. The wider context: 2026 AI Engineer World's Fair speakers converged on the view that fully automated "software factories" still need guardrails and a human in the loop, and this is offered as a concrete mechanism for that.

### What changes

The wiki has no existing page on ontologies, knowledge graphs, or "neurosymbolic AI" as an agent-guardrail technique — the two nearest neighbors, `concepts/harness.md` and `concepts/knowledge-layer.md`, cover different ground (general harness scaffolding, and compiled context for retrieval, respectively).

- New page `concepts/ontology-agent-guardrails.md`: defines ontologies in plain language, covers the "logical guardrail" pitch (an OWL axiom as a machine-enforced rule versus a prompt instruction the model can drift from), Eifrem's three-layer production framing, the reuse-existing-standards advantage, and the unresolved maintenance-problem caveat. Linked from both `harness.md` and `knowledge-layer.md` as a related-but-distinct idea.
- New source page for the Latent Space recap.
- `wiki/index.md` gains one new line under the Concepts section.

### What to weigh

This is a single conference-talk recap (one newsletter, secondary reporting on Coyle's talk plus a handful of practitioner quotes) with no benchmark or head-to-head comparison showing ontology-guardrails outperforming other control mechanisms — treat the page as reporting a framework being discussed, not a proven technique. I chose to create a new concept page rather than extend `harness.md` or `knowledge-layer.md`: the ontology-as-formal-rule-layer idea is a specific, nameable technique ("neurosymbolic AI") distinct enough from general harness scaffolding or compiled-context retrieval to warrant its own page, similar to how `prompt-injection.md` stands alone as a specific harness-security concern rather than being folded into `harness.md`. Given the user's explicit interest in this topic, the page runs longer than the usual 150-300 word concept-page target (worth noting since it's a deliberate exception, not scope creep).

## Intended changes

- [x] **Approve all** — checking this box approves every item in `## Intended changes` and `## Schema / vocabulary additions` below; the individual boxes may stay empty.

- [ ] **Create** `wiki/concepts/ontology-agent-guardrails.md` — new concept page
    > See draft below

- [ ] **Create** `wiki/sources/newsletters/ontologies-agentic-systems-2026-07-30.md` — source summary

- [ ] **Update** `wiki/index.md` — add new concepts entry
    > See draft below

## Page drafts

### wiki/concepts/ontology-agent-guardrails.md (new)

```md
---
title: Ontologies as agent guardrails
type: concept
domains: [agents]
tags: [agentic]
as_of: 2026-07-30
sources: [ontologies-agentic-systems-2026-07-30]
---

# Ontologies as agent guardrails

An ontology is a structured description of a domain's concepts and how they relate to each other — "data as graphs," in AI Engineer World's Fair speaker Frank Coyle's phrasing, or more formally "a description of data structure – of classes, properties, and relationships in a domain of knowledge" (Oxford Semantic Technologies). The idea predates AI by decades — it traces back to Aristotle, and more directly to Semantic-Web-era standards like Schema.org, RDFS, and OWL (Web Ontology Language) — but it's resurfacing as a specific technique for constraining agentic systems: use a formal ontology as a rule set an agent's reasoning or output can be checked against, rather than relying on the LLM's own judgment to stay on track. Pairing a probabilistic LLM with a symbolic, rule-based ontology layer is being called "neurosymbolic AI" — not a new architecture, but the practice of tying neural-network reasoning to a rule-based system (a knowledge graph, an RDFS/OWL reasoner) that can validate or override the model's output.

## Current status (as of 2026-07-30)

- Pitched as a "logical guardrail" for agent loops, which can otherwise silently go off the rails: "an OWL axiom is a rule a machine enforces," in Coyle's framing, versus a prompt instruction, which an LLM can drift from over a long loop.
- A practical advantage: established ontologies (Schema.org, FOAF, Dublin Core, RDFS, OWL) are already present in LLM training data, so a team can prompt for them directly instead of designing a domain ontology from scratch.
- Neo4j's Emil Eifrem described three ontology layers used to run agents at scale: a business-facing ontology (an organization's key concepts), a technical ontology (metadata for every data source and asset in the enterprise), and execution traces (runtime signals from the agents themselves) — together forming a shared substrate that lets agents stay "thin" (consuming one shared semantic layer) instead of "thick" (each agent manually wired to its own data sources).
- Coyle demonstrated a Claude agent using an ontology to validate its own reasoning after a tool call — a concrete example of using the ontology as a post-hoc check rather than only as upfront context.
- The known failure mode is maintenance: ontology upkeep is exactly why the 1990s/2000s Semantic Web vision never reached broad adoption. One proposed mitigation, from AI developer Prasenjit Sarkar, is having the agent maintain its own ontology as part of its operation — updating definitions as it hits edge cases — which changes the character of the maintenance problem without eliminating it.

## Why it matters

This gives the wiki's informal "agent loops go off the rails" problem a named, concrete mitigation: a formal, machine-checkable rule layer sitting alongside the LLM rather than another prompt instruction the model can still drift from. It's a different kind of control mechanism than orchestration design, tool selection, or eval scoring — closer to a validation layer with teeth — and it's worth tracking as its own idea because "neurosymbolic AI" is a specific, citable framing likely to keep recurring as agent loops get longer and more autonomous.

## Caveats

- Single-source: one conference-talk recap (AI Engineer World's Fair, via Latent Space) plus a handful of practitioner quotes (Neo4j's Eifrem, OpenLink's Kingsley Idehen, developer Prasenjit Sarkar). No benchmark or head-to-head comparison yet showing ontology-guardrails outperforming other control mechanisms.
- The maintenance-problem critique is real and unresolved; "the agent maintains its own ontology" is a proposed direction, not a demonstrated solution.

## Related

- [Harness (agent)](harness.md) — ontologies sit inside what this page calls the control/evaluation layer, but as a distinct, formally rule-based mechanism rather than prompts, evals, or permission logic
- [Knowledge layer](knowledge-layer.md) — a related but different structured-knowledge idea: knowledge-layer is compiled context for retrieval, this page is a formal rule layer for validation and constraint

## Recent changes

- [2026-07-30] Page created from Frank Coyle's AI Engineer World's Fair talk on ontologies as agent guardrails (via Latent Space recap).

## Sources

- [Ontologies Are So Back: Why AI Agents Are Reviving the Semantic Web](../sources/newsletters/ontologies-agentic-systems-2026-07-30.md)
```

### wiki/sources/newsletters/ontologies-agentic-systems-2026-07-30.md (new)

```md
---
title: "Ontologies Are So Back: Why AI Agents Are Reviving the Semantic Web"
type: source
source_type: newsletter
source_file: raw/newsletters/2026-07-30-ontologies-are-so-back-why-ai-agents-are-reviving.md
url: https://www.latent.space/p/ontologies-agentic-systems
published: 2026-07-30
ingested: 2026-09-07
domains: [agents]
---

# Ontologies Are So Back: Why AI Agents Are Reviving the Semantic Web

Latent Space recap of an AI Engineer World's Fair talk by UC Berkeley's Frank Coyle, arguing that agentic systems need ontologies as "logical guardrails" alongside LLM reasoning, plus commentary from Neo4j's Emil Eifrem on three ontology layers for running agents at scale, OpenLink's Kingsley Idehen on building an "agent with RDF memory," and developer Prasenjit Sarkar on the ontology-maintenance problem.

## Influenced pages

- [Ontologies as agent guardrails](../../concepts/ontology-agent-guardrails.md) — new concept page

## Key claims extracted

- Coyle: agentic systems need ontologies as "logical guardrails"; defines an ontology simply as "data as graphs"
- Established ontologies (Schema.org, FOAF, Dublin Core, RDFS, OWL) are already present in LLM training data and can be prompted for directly rather than built from scratch
- Neo4j's Eifrem: three ontology layers for agents at scale — business-facing, technical/metadata, and execution traces
- OWL axioms function as machine-enforced rules that can check and constrain LLM reasoning — the pairing is called "neurosymbolic AI"
- Coyle demonstrated a Claude agent using an ontology to validate its own reasoning after a tool call
- Ontology maintenance was the historical failure mode behind the Semantic Web's lack of adoption; Sarkar proposes agents maintaining their own ontology as a partial mitigation
```

### wiki/index.md (updated)

```md
- [concepts/ontology-agent-guardrails](concepts/ontology-agent-guardrails.md) — ontologies and OWL/RDF reasoners as a machine-enforced rule layer that checks and constrains LLM agent reasoning, distinct from prompt-level instructions ("neurosymbolic AI") *(as_of: 2026-07-30)*
```

Insert as a new line under the `## Concepts` section, after the `concepts/quantization` entry (the current last line in that section).
