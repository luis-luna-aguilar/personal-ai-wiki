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
