# Future Work

This document captures implementation caveats, known limitations, and likely next engineering tasks for the Personal Wiki Agent.

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

