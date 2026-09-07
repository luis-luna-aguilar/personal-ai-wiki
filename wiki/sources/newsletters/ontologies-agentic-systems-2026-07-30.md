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
