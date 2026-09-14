---
title: Knowledge architectures
type: concept
domains: [agents]
tags: [knowledge-cluster]
as_of: 2026-09-07
sources: [knowledge-layer-architecture, llm-wikis-paperwiki-2026-07-06, agent-memory-systems-layer-2026-06, femke-plantinga-company-brains-2026-08-27, ontologies-agentic-systems-2026-07-30, dhravyashah-supermemory-company-brain-2026-07-28, posthog-semantic-layer-2026-08-21, deeplethe-utopia-2026-09-09]
---

# Knowledge architectures

"Knowledge architecture" is the wiki's umbrella term for the ways a persistent store of knowledge or memory is put between raw information and the agents and people acting on it. Sources coin a new name for this almost weekly (second brain, company brain, LLM wiki, memory layer), and several of those names describe different things while others describe the same thing at a different scope. This page is the hub that owns the vocabulary: it separates the ideas on three axes, assigns one canonical page to each, and maps every term seen in sources to its canonical page. It carries no claims of its own beyond what those pages already say; rows are added here in the same proposal that creates a new canonical page.

## The three axes

Every system in this cluster can be placed by asking three questions:

1. **Scope.** Whose knowledge is it? One person, one agent, a team, or the whole organization.
2. **What it holds.** Compiled documents, episodic facts extracted from sessions, metric and data-source definitions, formal classes and rules, or a mix.
3. **Who writes it.** A human, an agent, or an agent that proposes and a human that approves.

## Canonical pages

| Canonical page | Scope | What it holds | Who writes it | Examples tracked |
|---|---|---|---|---|
| [Knowledge layer](knowledge-layer.md) | one person or one team | compiled documents: summaries, entity and concept pages, an index, a log | an agent compiles; a human curates the schema and reviews | LLM Wiki, PaperWiki, [OpenWiki](../tools/openwiki.md) |
| [Agent memory](agent-memory.md) | one agent, or one user's agents | episodic facts, preferences, and outcomes extracted from past sessions, managed as a lifecycle (extract, dedupe, reconcile, scope, expire) | the agent, under governed write rules | Supermemory, Engram, mem0, Letta (no tool pages yet) |
| [Company brain](company-brain.md) | the organization | a *system*, not one store: a knowledge layer plus agent memory plus tool access plus a refresh loop that pulls signals, prunes, and answers | hybrid; agents draft, humans gate rule changes | GBrain, Slite Agent, Gorgias Cortex, Lovable capabilities, Cloudflare OS, Supermemory Company Brain |
| [Semantic layer](semantic-layer.md) | the organization's data | definitions only: what each metric means, which tables to trust, how sources join, on top of an existing warehouse with no data copied | agents propose, humans approve; edits reset approval | PostHog semantic layer |
| [Ontologies as agent guardrails](ontology-agent-guardrails.md) | a domain | classes, relations, and axioms used as machine-checked rules that validate or constrain what an agent asserts or does | human-authored packs (schema.org, OWL, FOAF); agent-maintained upkeep is proposed, not proven | Neo4j's three-layer ontology stack, [Utopia](../tools/utopia.md) |

The rows are not rivals. A company brain typically contains a knowledge layer and agent memory; a semantic layer or an ontology can sit under any of them as the governed definitions or rules the others read from.

## Term map

Look a term up here before proposing a page, tag, or subcategory. Aliases update the canonical page's `## Also called` line; only a new row in the table above justifies a new page.

| Term seen in sources | Maps to | Note |
|---|---|---|
| second brain | Knowledge layer (personal scope) | alias; a personal-scope knowledge layer |
| LLM wiki, PaperWiki | Knowledge layer | Karpathy's name for the pattern and a research instance of it |
| knowledge base | depends on use | as a product feature (a Notion workspace, a support KB) it is a document store, not a concept; as a pattern it is a knowledge layer. Concept pages say which |
| wiki memory, maintained context surface | Knowledge layer | descriptive phrasings from newsletter coverage |
| company brain, org brain, GBrain, "the agent's brain" | Company brain | the organization-scope system |
| content brain, brand brain | Company brain (function scope) | a company brain limited to one function, for example marketing |
| memory layer, memory system, long-term memory | Agent memory | aliases |
| ghost memory | Agent memory | not an alias: a named failure mode where stale and current facts are retrieved together |
| context warehouse | Semantic layer | PostHog's product name for the store its semantic layer sits on; a vendor term, not a concept |
| metrics layer, governed metric catalog | Semantic layer | aliases |
| ontology, neurosymbolic AI, OWL/RDF guardrails | Ontologies as agent guardrails | the formal rule layer |
| Neo4j's "semantic layer" | Ontologies as agent guardrails | Emil Eifrem uses "semantic layer" for a shared ontology substrate that agents consume. It is not the metric-definition [semantic layer](semantic-layer.md) above; the collision is noted on both pages |
| knowledge graph | a data structure, not a concept | used by company brains (Zep/Graphiti), by ontology engines ([Utopia](../tools/utopia.md)), and by personal assistants ([Amazon Quick](../tools/amazon-quick.md)). Link to the page whose system uses it |
| context engineering | [Harness](harness.md) | the practice of assembling what goes into a model's context window; a technique, not a store |
| RAG, vector store | a retrieval mechanism, not an architecture | Agent memory and Knowledge layer both contrast themselves with retrieval-only designs |
| world model | the physical or video-prediction sense | canonical on [LeWorldModel](leworldmodel.md), [Cosmos 3](../models/cosmos-3.md), and [Physical AI deployment](../trends/physical-ai-deployment.md). DeepLethe markets [Utopia](../tools/utopia.md) as an "enterprise world model"; that is a marketing alias for an ontology-backed bitemporal knowledge graph and maps to the ontology row, not to this sense |

## How to use this page

- A source that says "we built a second brain / company brain / knowledge base for our agents" is describing one of the rows above. Find the row, update that page, and add the source's wording to its `## Also called` line if it is new.
- A source that introduces a genuinely new combination of scope, contents, and writer gets a new row here in the same proposal that creates its page.
- `## Related` lines on the canonical pages must agree with the table above. When they disagree, this page wins and the Related line is fixed.

## Related

- [Harness](harness.md) — the scaffolding around an acting model; every row above is something a harness can read from or write to
- [Model Context Protocol](mcp.md) — the tool-exposure protocol several company-brain implementations use to give agents access to the underlying systems

## Recent changes

- [2026-09-09] Utopia added as an ontology-row example and as the first recorded "world model" marketing alias, which the term map keeps on the ontology row.
- [2026-09-09] Page created as the vocabulary hub for the knowledge, memory, company-brain, and ontology cluster, after the four existing pages had drifted into contradictory "this vs that" descriptions of each other.
- [2026-08-21] Added the semantic-layer row (governed metric and data-source definitions over an existing warehouse) from PostHog's account, plus "context warehouse" and "metrics layer" term-map rows.
- [2026-07-28] Added Supermemory Company Brain to the Company brain row's tracked examples, mirroring the new production example on that page.

## Sources

- [AI Knowledge Layer](../sources/articles/knowledge-layer-architecture.md)
- [LLM Wikis / PaperWiki — Omar Sar](../sources/tweets/llm-wikis-paperwiki-2026-07-06.md)
- [Agent memory becomes a systems layer](../sources/newsletters/agent-memory-systems-layer-2026-06.md)
- [Femke Plantinga on X — 9 company-brain architectures compared](../sources/tweets/femke-plantinga-company-brains-2026-08-27.md)
- [Ontologies Are So Back: Why AI Agents Are Reviving the Semantic Web](../sources/newsletters/ontologies-agentic-systems-2026-07-30.md)
- [Dhravya Shah on X — How to Build Your Company Brain in 5 Minutes](../sources/tweets/dhravyashah-supermemory-company-brain-2026-07-28.md)
- [PostHog — Building a semantic layer](../sources/tweets/posthog-semantic-layer-2026-08-21.md)
- [deeplethe/utopia (GitHub)](../sources/repos/deeplethe-utopia-2026-09-09.md)
