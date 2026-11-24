---
title: Knowledge architectures
type: concept
domains: [agents]
tags: [knowledge-cluster]
as_of: 2026-10-28
sources: [knowledge-layer-architecture, llm-wikis-paperwiki-2026-07-06, agent-memory-systems-layer-2026-06, femke-plantinga-company-brains-2026-08-27, ontologies-agentic-systems-2026-07-30, dhravyashah-supermemory-company-brain-2026-07-28, posthog-semantic-layer-2026-08-21, deeplethe-utopia-2026-09-09, helixdb-helix-foundry-2026-10-19, cognition-agent-memory-repo-2026-10, latent-space-airbnb-inside-out-ai-2026-10-02, fabio-rovai-open-ontologies-2026-10-28, thorstenball-how-i-work-with-agents-2026-10-25]
---

# Knowledge architectures

"Knowledge architecture" is the wiki's umbrella term for the ways a persistent store of knowledge or memory is put between raw information and the agents and people acting on it. Sources coin a new name for this almost weekly (second brain, company brain, LLM wiki, memory layer), and several of those names describe different things while others describe the same thing at a different scope. This page is the hub that owns the vocabulary: it separates the ideas on three axes, assigns one canonical page to each, and, through its [term map](knowledge-term-map.md), maps every term seen in sources to its canonical page. It carries no claims of its own beyond what those pages already say; rows are added here in the same proposal that creates a new canonical page.

## The three axes

Every system in this cluster can be placed by asking three questions:

1. **Scope.** Whose knowledge is it? One person, one agent, a team, or the whole organization.
2. **What it holds.** Compiled documents, episodic facts extracted from sessions, metric and data-source definitions, formal classes and rules, or a mix.
3. **Who writes it.** A human, an agent, or an agent that proposes and a human that approves.

## Canonical pages

| Canonical page | Scope | What it holds | Who writes it | Examples tracked |
|---|---|---|---|---|
| [Knowledge layer](knowledge-layer.md) | one person or one team | compiled documents: summaries, entity and concept pages, an index, a log | an agent compiles; a human curates the schema and reviews | LLM Wiki, PaperWiki, [OpenWiki](../tools/openwiki.md) |
| [Agent memory](agent-memory.md) | one agent, or one user's agents | episodic facts, preferences, and outcomes extracted from past sessions, managed as a lifecycle (extract, dedupe, reconcile, scope, expire) | the agent, under governed write rules | Supermemory, Engram, mem0, Letta, Cognition's Agent Memory Repo (no tool pages yet) |
| [Company brain](company-brain.md) | the organization | a *system*, not one store: a knowledge layer plus agent memory plus tool access plus a refresh loop that pulls signals, prunes, and answers | hybrid; agents draft, humans gate rule changes | GBrain, Slite Agent, Gorgias Cortex, Lovable capabilities, Cloudflare OS, Supermemory Company Brain, Airbnb Everest, Amp's shared threads |
| [Semantic layer](semantic-layer.md) | the organization's data | definitions only: what each metric means, which tables to trust, how sources join, on top of an existing warehouse with no data copied | agents propose, humans approve; edits reset approval | PostHog semantic layer |
| [Semantic layer](semantic-layer.md), local data-workspace variant | one person, over the organization's data | copied snapshots of the organization's records, matched across sources into one graph of objects and relationships, queried with SQL | an agent proposes the matching model and changes; the user confirms | [Helix Foundry](../tools/helix-foundry.md) |
| [Ontologies as agent guardrails](ontology-agent-guardrails.md) | a domain | classes, relations, and axioms used as machine-checked rules that validate or constrain what an agent asserts or does | human-authored packs (schema.org, OWL, FOAF); agent-maintained upkeep is proposed, not proven | Neo4j's three-layer ontology stack, [Utopia](../tools/utopia.md), [Open Ontologies](../tools/open-ontologies.md) (change control for the ontology itself) |

The data-workspace row is a variant of the semantic layer: both give agents one governed view of an organization's data to answer from, but the workspace copies the records and matches them across sources instead of only defining metrics over a warehouse that stays in place. The rows are not rivals. A company brain typically contains a knowledge layer and agent memory; a semantic layer or an ontology can sit under any of them as the governed definitions or rules the others read from.

## Term map

The table that maps every term seen in sources (second brain, LLM wiki, context graph, memory repo, dreaming, ContextOps, world model, and the rest) to its canonical page lives on its own page, [Knowledge term map](knowledge-term-map.md). Look a term up there before proposing a page, tag, or subcategory: an alias updates the canonical page's `## Also called` line and adds a term-map row, and only a new row in the matrix above justifies a new page.

## How to use this page

- A source that says "we built a second brain / company brain / knowledge base for our agents" is describing one of the rows above. Find the row, update that page, and add the source's wording to its `## Also called` line and to the [term map](knowledge-term-map.md) if it is new.
- A source that introduces a genuinely new combination of scope, contents, and writer gets a new row here in the same proposal that creates its page.
- `## Related` lines on the canonical pages must agree with the table above. When they disagree, this page wins and the Related line is fixed.

## Related

- [Knowledge term map](knowledge-term-map.md) — the lookup table from every source term to its canonical page in the matrix above
- [Harness](harness.md) — the scaffolding around an acting model; every row above is something a harness can read from or write to
- [Model Context Protocol](mcp.md) — the tool-exposure protocol several company-brain implementations use to give agents access to the underlying systems

## Recent changes

- [2026-11-23] Split the term map out to [Knowledge term map](knowledge-term-map.md); this page keeps the three axes, the canonical-pages matrix, and a pointer. Recent-changes entries about term-map rows moved with it.
- [2026-10-28] Open Ontologies added as an ontology-row example (change control for the ontology itself).
- [2026-10-25] Added Amp's shared threads to the Company brain row's examples; the "company memory" mapping is on the [term map](knowledge-term-map.md).
- [2026-10-19] Added a local data-workspace variant row under the semantic layer (one person, copied and matched organization records, SQL answers) with Helix Foundry as its example.
- [2026-10-06] Added Cognition's Agent Memory Repo to the Agent memory row's examples.
- [2026-10-02] Added Airbnb's Everest to the Company brain row's examples.
- [2026-09-09] Utopia added as an ontology-row example.
- [2026-09-09] Page created as the vocabulary hub for the knowledge, memory, company-brain, and ontology cluster, after the four existing pages had drifted into contradictory "this vs that" descriptions of each other.
- [2026-08-21] Added the semantic-layer row (governed metric and data-source definitions over an existing warehouse) from PostHog's account.
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
- [HelixDB/helix-foundry (GitHub)](../sources/repos/helixdb-helix-foundry-2026-10-19.md)
- [Cognition — Agent Memory Repo](../sources/articles/cognition-agent-memory-repo-2026-10.md)
- [Latent Space — Inside-Out AI: Rebuilding Airbnb](../sources/newsletters/latent-space-airbnb-inside-out-ai-2026-10-02.md)
- [fabio-rovai/open-ontologies (GitHub)](../sources/repos/fabio-rovai-open-ontologies-2026-10-28.md)
- [Thorsten Ball (@thorstenball) — How I work with Agents](../sources/tweets/thorstenball-how-i-work-with-agents-2026-10-25.md)
