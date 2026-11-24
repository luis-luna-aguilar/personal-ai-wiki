---
title: Knowledge term map
type: concept
domains: [agents]
tags: [knowledge-cluster]
as_of: 2026-10-19
sources: [llm-wikis-paperwiki-2026-07-06, agent-memory-systems-layer-2026-06, femke-plantinga-company-brains-2026-08-27, ontologies-agentic-systems-2026-07-30, posthog-semantic-layer-2026-08-21, deeplethe-utopia-2026-09-09, helixdb-helix-foundry-2026-10-19, cognition-agent-memory-repo-2026-10, ainews-devin-dreaming-2026-10-06, latent-space-airbnb-inside-out-ai-2026-10-02, every-agent-claude-managed-agents-2026-10-08, latent-space-runway-worldprompt-2026-09-25, eugenalpeza-fde-boom-product-gap-2026-09-29]
---

# Knowledge term map

The lookup table for the knowledge, memory, company-brain, and ontology cluster: every term seen in sources, mapped to its canonical page in the [Knowledge architectures](knowledge-architectures.md) matrix. Look a term up here before proposing a page, tag, or subcategory. An alias updates the canonical page's `## Also called` line and gets a row here; a term that names a new cell in the matrix gets its row here in the same change that adds the cell to the hub. No term is left unmapped. Where a row and the hub disagree, the hub wins.

## Term map

| Term seen in sources | Maps to | Note |
|---|---|---|
| second brain | Knowledge layer (personal scope) | alias; a personal-scope knowledge layer |
| LLM wiki, PaperWiki | Knowledge layer | Karpathy's name for the pattern and a research instance of it |
| knowledge base | depends on use | as a product feature (a Notion workspace, a support KB) it is a document store, not a concept; as a pattern it is a knowledge layer. Concept pages say which |
| wiki memory, maintained context surface | Knowledge layer | descriptive phrasings from newsletter coverage |
| company brain, org brain, GBrain, "the agent's brain" | Company brain | the organization-scope system |
| content brain, brand brain | Company brain (function scope) | a company brain limited to one function, for example marketing |
| context graph, organizational context graph | Company brain | Airbnb's name for Everest, an organization-wide graph of codebase and project context that agents and engineers query. Not the same as "knowledge graph" below, which is a data structure; a context graph names the organization-scope system |
| memory layer, memory system, long-term memory | Agent memory | aliases |
| ghost memory | Agent memory | not an alias: a named failure mode where stale and current facts are retrieved together |
| memory repo, Agent Memory Repo | Agent memory | Cognition's open git-and-markdown format for one user's agent memory. Its `MEMORY.md` index and linked pages look like a knowledge layer, but agents write it from their own sessions, one sourced fact per line, so it sits on the agent-memory row |
| dreaming, dreams | Agent memory (lifecycle step) | an offline pass that prunes, links, or rewrites stored memories between sessions, as in Cognition's Devin Dreaming and the Dreams feature of [Claude Managed Agents](../tools/claude-managed-agents.md). The [company brain](company-brain.md)'s "dreaming & pruning" function is the same step at organization scope. A step, not a store |
| context warehouse | Semantic layer | PostHog's product name for the store its semantic layer sits on; a vendor term, not a concept |
| metrics layer, governed metric catalog | Semantic layer | aliases |
| ontology, neurosymbolic AI, OWL/RDF guardrails | Ontologies as agent guardrails | the formal rule layer |
| Neo4j's "semantic layer" | Ontologies as agent guardrails | Emil Eifrem uses "semantic layer" for a shared ontology substrate that agents consume. It is not the metric-definition [semantic layer](semantic-layer.md) above; the collision is noted on both pages |
| knowledge graph | a data structure, not a concept | used by company brains (Zep/Graphiti), by ontology engines ([Utopia](../tools/utopia.md)), by personal assistants ([Amazon Quick](../tools/amazon-quick.md)), and by local data workspaces ([Helix Foundry](../tools/helix-foundry.md)). Link to the page whose system uses it |
| "one ontology" over company data, local-first data workspace | Semantic layer, local data-workspace variant | Helix Foundry's marketing term for the model it suggests by matching the same customers and records across connected sources. It has no axioms or machine-checked rules, so it is not the ontology row's sense; it is the matrix's data-workspace variant of the semantic layer. See [Helix Foundry](../tools/helix-foundry.md) |
| context engineering | [Harness](harness.md) | the practice of assembling what goes into a model's context window; a technique, not a store |
| ContextOps | Knowledge layer (maintenance practice) | Edra's name for keeping agents' operating procedures current: agents propose rules from case evidence, the process owner approves, and each instruction has an owner, a version, tests, and rollback. A practice, not a store. Its authors contrast it with a context graph (the Company brain alias above), which records mistakes and exceptions alike. See [Forward-deployed engineering](../training/forward-deployed-engineering.md) |
| company agent, shared company agent | [Multiplayer AI](multiplayer-ai.md), outside this cluster | one agent a whole organization shares in team chat (Every Agent). Its memory folders and saved skills are [agent memory](agent-memory.md) at company scope; it is a company brain only if it also carries a knowledge layer and a refresh loop |
| RAG, vector store | a retrieval mechanism, not an architecture | Agent memory and Knowledge layer both contrast themselves with retrieval-only designs |
| world model, interface world model | the physical or video-prediction sense | canonical on [LeWorldModel](leworldmodel.md), [Cosmos 3](../models/cosmos-3.md), and [Physical AI deployment](../trends/physical-ai-deployment.md). Runway's "interface world model" is the same sense applied to software: a video model that renders a UI as pixels and predicts the result of each click. DeepLethe markets [Utopia](../tools/utopia.md) as an "enterprise world model"; that is a marketing alias for an ontology-backed bitemporal knowledge graph and maps to the ontology row, not to this sense |

## Related

- [Knowledge architectures](knowledge-architectures.md) — the hub: the three axes and the canonical-pages matrix every row here points into

## Recent changes

- [2026-11-23] Page created, split out of [Knowledge architectures](knowledge-architectures.md)'s "Term map" section.
- [2026-10-19] Mapped Helix Foundry's "one ontology" to the semantic layer's local data-workspace variant rather than to the ontology row, and added Helix Foundry to the knowledge-graph row.
- [2026-10-08] Mapped "company agent" (Every Agent) to Multiplayer AI, outside the cluster, with its memory part pointed at Agent memory.
- [2026-10-06] Mapped "memory repo / Agent Memory Repo" and "dreaming / dreams" (Cognition's Devin Dreaming, Anthropic's Managed Agents Dreams) to Agent memory.
- [2026-10-02] Added "context graph" (Airbnb's Everest) as a Company brain alias.
- [2026-09-29] Mapped "ContextOps" (Edra) to the Knowledge layer as a maintenance practice for owner-approved, versioned agent procedures, not a new store.
- [2026-09-25] Mapped Runway's "interface world model" (video-generated software UIs) to the world-model row's video-prediction sense.
- [2026-09-09] Recorded Utopia's "enterprise world model" as the first "world model" marketing alias, kept on the ontology row.
- [2026-08-21] Added "context warehouse" and "metrics layer" rows (PostHog), both mapped to the Semantic layer.

## Sources

- [LLM Wikis / PaperWiki — Omar Sar](../sources/tweets/llm-wikis-paperwiki-2026-07-06.md)
- [Agent memory becomes a systems layer](../sources/newsletters/agent-memory-systems-layer-2026-06.md)
- [Femke Plantinga on X — 9 company-brain architectures compared](../sources/tweets/femke-plantinga-company-brains-2026-08-27.md)
- [Ontologies Are So Back: Why AI Agents Are Reviving the Semantic Web](../sources/newsletters/ontologies-agentic-systems-2026-07-30.md)
- [PostHog — Building a semantic layer](../sources/tweets/posthog-semantic-layer-2026-08-21.md)
- [deeplethe/utopia (GitHub)](../sources/repos/deeplethe-utopia-2026-09-09.md)
- [HelixDB/helix-foundry (GitHub)](../sources/repos/helixdb-helix-foundry-2026-10-19.md)
- [Cognition — Agent Memory Repo](../sources/articles/cognition-agent-memory-repo-2026-10.md)
- [AINews — Devin Dreaming and Agent Memory Repo](../sources/newsletters/ainews-devin-dreaming-2026-10-06.md)
- [Latent Space — Inside-Out AI: Rebuilding Airbnb](../sources/newsletters/latent-space-airbnb-inside-out-ai-2026-10-02.md)
- [Every — Why We Handed Our Agent's Infrastructure to Anthropic](../sources/newsletters/every-agent-claude-managed-agents-2026-10-08.md)
- [Latent Space — Runway's WorldPrompt and the engineering of real-time worlds](../sources/newsletters/latent-space-runway-worldprompt-2026-09-25.md)
- [Eugen Alpeza on X — The FDE boom is a product gap](../sources/tweets/eugenalpeza-fde-boom-product-gap-2026-09-29.md)
