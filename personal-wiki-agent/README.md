# Personal Wiki Agent

Personal Wiki Agent turns this repository into a queryable expert system using Deep Agents as the harness and OpenRouter as the default model gateway.

## Capabilities

- one public tool: `use_personal_wiki`
- full synthesized answers instead of context dumps
- page-level `as_of` metadata for consulted pages
- mandatory `Gaps` section in every response
- local MCP deployment for Claude Desktop
- remote-friendly structure for later ChatGPT-compatible deployment

## Layout

- `app/query_instructions.md` governs query behavior
- `app/config.default.toml` holds safe defaults
- `app/config.local.toml` overrides local behavior
- `app/server.py` exposes the MCP tool
- `app/cli.py` provides local testing
- `app/engine.py` contains the runtime
- `logs/` stores runtime logs and per-query artifacts

## Setup

1. Install dependencies:

```bash
pip install -e ./personal-wiki-agent
```

2. Provide an API key:

```bash
export PERSONAL_WIKI_OPENROUTER_API_KEY="..."
```

The runtime maps `PERSONAL_WIKI_OPENROUTER_API_KEY` to `OPENROUTER_API_KEY` for the underlying provider libraries if needed.

3. Optionally copy and edit local config:

```bash
cp personal-wiki-agent/app/config.local.example.toml \
   personal-wiki-agent/app/config.local.toml
```

## CLI usage

```bash
personal-wiki-agent "What is happening in coding agents?"
personal-wiki-agent "Should I bet on MCP?" --context "I care about interoperability" --include-personal-views --json
```

## MCP usage

Run the local MCP server:

```bash
personal-wiki-agent-mcp
```

By default this starts in `stdio` mode for clients like Claude Desktop that launch the server as a subprocess.

The server exposes one tool named `use_personal_wiki`.

### Manual MCP testing

If you want a local URL to connect to manually, run:

```bash
personal-wiki-agent-mcp --transport streamable-http
```

Default local endpoint:

- `http://127.0.0.1:8000/mcp`

You can also set a custom bind address:

```bash
personal-wiki-agent-mcp --transport streamable-http --host 127.0.0.1 --port 8000
```

For SSE transport:

```bash
personal-wiki-agent-mcp --transport sse --host 127.0.0.1 --port 8000
```

## Configuration

Primary configuration lives in:

- `personal-wiki-agent/app/config.default.toml`
- `personal-wiki-agent/app/config.local.toml`

Secret credentials come from environment variables:

- `PERSONAL_WIKI_OPENROUTER_API_KEY`

### Parameters

#### `[personal_wiki_agent]`

- `provider`: model provider layer. Default: `openrouter`
- `model`: model string passed to Deep Agents / LangChain. Default: `openrouter:anthropic/claude-sonnet-4-6`
- `max_steps`: reserved guardrail for agent-step limits
- `max_steps`: hard cap on Deep Agents / LangGraph recursion for a single query
- `max_files`: hard cap on unique deep file reads through the repo `read_file` tool, excluding the automatic `wiki/index.md` preload
- `max_search_results`: default search limit
- `include_personal_by_default`: whether personal notes are included unless explicitly disabled
- `require_index_first`: whether `wiki/index.md` is preloaded before exploration
- `stale_after_days`: warning threshold for stale pages
- `hard_stale_after_days`: hard stale threshold
- `return_consulted_pages`: whether structured consulted pages are returned
- `return_gaps`: whether structured gaps are returned
- `answer_style`: intended answer style label
- `log_level`: runtime logger level. Recommended values: `INFO`, `DEBUG`
- `log_tool_calls`: whether repo tool calls are written to the runtime log
- `log_model_io`: whether request/response artifacts are written per query
- `persist_query_history`: whether final structured responses are written per query

#### `[personal_wiki_agent.transport]`

- `enable_local_mcp`: local MCP exposure toggle
- `enable_remote_mcp`: remote MCP exposure toggle

#### `[personal_wiki_agent.paths]`

- `repo_root`: repository root, resolved relative to `app/`
- `index_path`: path to `wiki/index.md`
- `personal_root`: path to `personal/`
- `wiki_root`: path to `wiki/`
- `log_path`: path to `wiki/log.md`
- `proposals_root`: path to `proposals/`
- `runtime_logs_dir`: directory for runtime logs and artifacts
- `runtime_log_file`: rotating log file path
- `query_history_dir`: directory for per-query request and response artifacts

## Logging

The agent now writes runtime logs and query artifacts for debugging and behavior verification.

### Log locations

- Main rotating runtime log:
  `personal-wiki-agent/logs/personal-wiki-agent.log`
- Per-query request/response artifacts:
  `personal-wiki-agent/logs/queries/`

### What gets logged

- query start and finish
- tool calls such as `get_index`, `search_repo`, `read_file`, and `get_recent_changes`
- raw model response artifacts
- final structured response artifacts
- parser recovery events when the model wraps JSON in prose or code fences
- file-read counts relative to `max_files`

## Guardrail Enforcement

The following limits are now enforced by the runtime:

- `max_steps`
  Enforced via LangGraph `recursion_limit` on each query invocation. If the agent exceeds that loop budget, the run fails rather than continuing indefinitely.
- `max_files`
  Enforced in the repo `read_file` tool. Once the agent has performed the configured number of unique deep file reads, additional reads are rejected with an explicit error instructing the agent to refine search before reading more files.

Current implementation note:

- `max_files` applies to the custom repo read tool used by this project and excludes the automatic index preload.
- If we later allow Deep Agents' built-in filesystem tools directly, we should also add permission or middleware-level controls so those paths cannot bypass the same cap.

Longer-term caveats and follow-up engineering tasks live in [FUTURE_WORK.md](/Users/luis/Obsidian/AI%20Wiki/personal-wiki-agent/FUTURE_WORK.md:1).

### Typical artifact files

- `<query-id>-request.json`
- `<query-id>-response-raw.json`
- `<query-id>-response-final.json`

## Notes

- The package directory inside the subproject is intentionally `app/` to avoid a nested folder with the same name as the project root.
- The first live CLI run showed that models may wrap JSON in prose and code fences; the runtime now attempts to recover valid JSON from those responses automatically.
