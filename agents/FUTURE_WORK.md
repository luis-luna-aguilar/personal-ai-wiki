# Future Work

This document captures implementation caveats, known limitations, and likely next engineering tasks for the Agents MCP.

## Retired: Neo4j ontology prototype (2026-07-16)

`agents/ontology/` and `agents/mcp/ontology/` (the Neo4j-backed open-ontology compiler, manual Codex extraction via JSON work packets) have been archived to `agents/attic/ontology/` and `agents/attic/mcp-ontology/` — not deleted, full git history preserved. Rationale: stalled since 2026-05-14 (~17 of ~200 wiki pages processed), and its design philosophy ("no fixed closed ontology... traversal over strict ontology purity," explicitly no validation/evidence layer) is the opposite of the SHACL/OWL-validated Fuseki knowledge-graph layer deployed the same day (`knowledge-graph/`, see its `README.md`) — running both risks silent drift between two graphs describing the same wiki. The `use_personal_wiki` MCP tool's `ontology_search`/`ontology_expand`/`ontology_actions` methods were removed from `agents/mcp/engine.py`'s tool list (dead code otherwise — their import target no longer exists); the `agents-ontology` console script and `neo4j` dependency were removed from `agents/pyproject.toml`. `agents/mcp/tools/ontology.py` (the thin engine-facing wrapper) archived alongside as `agents/attic/mcp-tools-ontology.py`. If a graph-backed ontology is wanted again, prefer extending the `knowledge-graph/` layer (SPARQL/SHACL, already live at `:3031/aiwiki`) over reviving this prototype.

## Guardrail Caveats

- `max_files` is enforced only on this project's custom `read_file` tool.
  If future versions expose Deep Agents' built-in filesystem tools directly, those tools could bypass the current cap unless equivalent middleware or permission-layer limits are added.

- `max_steps` is enforced via LangGraph `recursion_limit`.
  This is a practical loop budget, not a semantic guarantee about “reasoning steps” in the human sense. A single model turn may still do substantial work before the next graph step boundary.

- The automatic `wiki/index.md` preload is intentionally excluded from the `max_files` count.
  If preload behavior changes later, the guardrail accounting should be revisited so file-count semantics stay predictable.

- `max_search_results` currently limits returned search results, not overall agent curiosity.
  The agent can still issue multiple search calls within the step budget. If search churn becomes a problem, add a per-query search-call counter similar to the file-read counter.

## Logging Caveats

- Logging currently captures query lifecycle, tool calls, raw responses, and normalized outputs, but not a full low-level execution trace.
  If deeper debugging becomes necessary, add structured event logs for each tool request/response pair or enable more detailed middleware instrumentation.

- Logs are file-based and local-first.
  If remote deployment becomes important, decide whether logs remain local, move to a central sink, or become configurable by transport mode.

## Runtime Follow-Ups

- Evaluate whether the agent should use a structured response format supported directly by Deep Agents or LangChain provider strategies instead of relying on JSON-in-text parsing.
- Add explicit tests for:
  - prose-wrapped JSON recovery
  - fenced JSON recovery
  - leading-slash repo path handling
  - `max_files` enforcement
  - `max_steps` exhaustion behavior
- Consider adding a per-query search-call budget in addition to `max_search_results`.
- Decide whether recent changes should eventually include richer synthesis over `wiki/log.md` and `proposals/applied/` together rather than simple collection.

## Deployment Follow-Ups

- Claude Desktop local MCP is the first deployment target.
- If ChatGPT integration becomes a priority, add a remote-compatible MCP deployment path and document how logging, auth, and secrets differ from local mode.

