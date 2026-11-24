---
type: proposal
source: raw/articles/2026-11-23-developersopenaicom-api-docs-guides-background.md
status: pending
created: 2026-11-23
---

# Proposal: OpenAI background mode and discounted completion windows

## Summary

### In short
On OpenAI's newest models, cheap asynchronous work now means a background request with a completion deadline, because Flex processing is gone. From GPT-6.2 onward, new models launch without Flex. Builders instead pick a 2-hour or 8-hour completion window, at 30% or 40% off Standard token prices, and multi-step agent runs keep that discount across follow-up requests. The proposal rewrites the Flex processing page around this change and adds one sentence to Agent execution runtimes. The one reason to hesitate is the date: the docs page has none, so the proposal dates it to today's ingest.

[[#Open questions|Open questions: 1 to answer.]]

- [x] **Approve all** — checking this box approves every item in `## Intended changes` and `## Schema / vocabulary additions` below; the individual boxes may stay empty.

### The source
The source is OpenAI's "Background mode" guide for the Responses API, captured on 23 November 2026. Background mode lets an application send a long-running request, get a response ID straight back, and collect the result later. It does not hold a connection open while the model works. The result arrives through a webhook (OpenAI calls the application's endpoint when the response completes) or by polling the response ID until it reaches a final status. Requests can be canceled, and a streamed background response can be resumed from its last event if the connection drops.

The new part is the completion window. The default, `soonest`, runs as fast as possible at normal prices. A `2h` or `8h` window tells OpenAI the answer can wait. OpenAI then targets completion within that time, retries capacity errors itself and charges 30% or 40% less per token. The windows are in public beta on GPT-6.2 Astra, GPT-6.2 Sol, GPT-6.1 Terra and GPT-6 Luna. The guide says plainly that new models from GPT-6.2 onward ship without Flex processing, OpenAI's earlier cheap-but-slow tier, and points long-running work to these windows instead. For agent runs that take several turns, such as a model asking the application to look up a document and then continuing, each follow-up reuses the window and an application-chosen `continuation_id`. That keeps the discount and gets higher queue priority. The guide lists the conditions. Discounted requests must use Standard processing and cannot stream. They share the Batch API's rate limit. Their prompt cache is not shared with normal requests. Background mode also stores request data temporarily, even under Zero Data Retention.

### What changes
The wiki's Flex processing page, last dated April, still presents Flex as OpenAI's low-cost async option. Agent execution runtimes lists the Responses API's DevDay agent features but says nothing about background work.

- **Flex processing** is rewritten around the shift. Flex stays documented for older models, and a new section covers discounted completion windows as the route on new models: when to use 2h versus 8h, webhook or polling, continuation IDs for agent runs, and the conditions above. The page gains a Recent-changes section. Page date moves to 23 November.
- **Agent execution runtimes** adds one sentence on background mode to its model-lab agent APIs bullet and a Recent-changes entry. Page date and Current-status date move to 23 November.
- One new source page for the guide.

### What to weigh
The guide carries no publication date, so every date here is the 23 November ingest date, and the change may be a few weeks older. The page keeps the title "Flex processing" even though most of its guidance now concerns its replacement. The open question asks whether to rename it.

## Intended changes

- [ ] **Update** `wiki/workflows/flex-processing.md` — rewrite body around Flex's replacement on new models; add a Recent changes section with one entry dated 2026-11-23; `as_of` 2026-04-22 → 2026-11-23; append source id `openai-background-mode-docs-2026-11`
    > See draft below

- [ ] **Update** `wiki/concepts/agent-execution-runtimes.md` — one sentence appended to the "Model-lab agent APIs" bullet; adds one Recent-changes entry dated 2026-11-23 (list at 6, no spill); `as_of` and Current-status date 2026-10-07 → 2026-11-23; append source id and Sources line
    > See draft below

- [ ] **Update** `wiki/index.md` — refresh the flex-processing and agent-execution-runtimes descriptions and dates
    > See draft below

- [ ] **Create** `wiki/sources/articles/openai-background-mode-docs-2026-11.md` — source summary

## Page drafts

### wiki/workflows/flex-processing.md (updated)

Full page (it is short):

```md
---
title: Flex processing
type: workflow
domains: [agents]
subcategory: agent-orchestration
tags: [openai]
as_of: 2026-11-23
sources: [openai-flex-processing, legacy-ai-tools-roadmap-xlsx, openai-background-mode-docs-2026-11]
---

# Flex processing

Flex processing is OpenAI's lower-cost asynchronous execution mode for workloads that do not need normal-latency responses: trade latency and completion certainty for cheaper large-scale processing. As of November 2026 it applies only to older models. New models from GPT-6.2 onward launch without Flex, and OpenAI points long-running work to discounted completion windows in Responses API background mode instead.

## Current status (as of 2026-11-23)

- Flex (`service_tier: flex`) remains for models released before GPT-6.2; GPT-6.2 Astra and Sol and later models do not offer it.
- The replacement is a background request (`background: true`) with `background_options.completion_window` set to `2h` (30% below Standard token rates) or `8h` (40% below). OpenAI targets completion inside the window and retries capacity errors itself. The default `soonest` window has no discount.
- Discounted windows are in public beta on GPT-6.2 Astra, GPT-6.2 Sol, GPT-6.1 Terra and GPT-6 Luna.

## Current guidance

- Use a discounted window, or Flex on older models, when the task is non-urgent: overnight document review (`8h`), same-day ticket analysis before a meeting (`2h`), offline enrichment, delayed content generation.
- For independent requests you can submit together up front, use the Batch API; use background mode when each step depends on the previous result.
- Multi-step agent runs: send each follow-up (for example a function-call result) with the same model, service tier, window and an application-chosen `continuation_id`. Follow-ups keep the discount and get higher queue priority. If the prior response has expired, replay the saved input and full output instead of `previous_response_id`.
- Learn about completion through a webhook (`response.completed`; verify signatures, deduplicate by `webhook-id`) or by polling the response ID while it is `queued` or `in_progress`. Cancel with `POST /v1/responses/{id}/cancel`.
- Do not use either for latency-sensitive product paths or tightly interactive loops.

## Caveats

- Discounted windows require Standard processing (`service_tier: default`; `auto` qualifies only if Standard is chosen) and no streaming. Only `soonest` background requests can stream, with resume from the last `sequence_number`.
- `2h`/`8h` requests share the Batch/Background rate limit with Batch API jobs, counted on input tokens at submission.
- Prompt-cache entries made by `2h`/`8h` requests cannot be reused by normal Standard requests.
- Background mode stores request data temporarily (encrypted at rest) even with `store: false` or Zero Data Retention.
- Flex remains slower and less deterministic than standard processing, and retry and failure handling need explicit design.

## Recent changes

- [2026-11-23] New models from GPT-6.2 launch without Flex; added Responses API background mode with discounted `2h`/`8h` completion windows (30%/40% off) as the replacement, plus continuation IDs, webhooks and limits.

## Sources

- [OpenAI Flex processing guide](../sources/articles/openai-flex-processing.md)
- [AI Tools & Roadmap legacy workbook](../sources/notes/legacy-ai-tools-roadmap-xlsx.md)
- [OpenAI API docs — Background mode](../sources/articles/openai-background-mode-docs-2026-11.md)
```

### wiki/concepts/agent-execution-runtimes.md (updated)

Frontmatter: `as_of: 2026-10-07` → `as_of: 2026-11-23`; append `openai-background-mode-docs-2026-11` to `sources:`. Heading `## Current status (as of 2026-10-07)` → `## Current status (as of 2026-11-23)`.

"Model-lab agent APIs" bullet — append after "…calls the right level of abstraction (memory, storage) an open question.":

```md
By November 2026 background mode covers multi-step agent runs: the application sends each turn as an asynchronous request, learns of completion by webhook or polling, and links follow-ups with a `continuation_id`; choosing a `2h` or `8h` completion window cuts token prices 30% or 40%, and these windows replace Flex processing on new models ([Flex processing](../workflows/flex-processing.md)).
```

Recent changes — insert directly below the existing 2026-11-23 split entry (newest first):

```md
- [2026-11-23] Added Responses API background mode for multi-step agent runs (continuation IDs, webhook or polling) with discounted `2h`/`8h` completion windows replacing Flex on new models.
```

Sources — append:

```md
- [OpenAI API docs — Background mode](../sources/articles/openai-background-mode-docs-2026-11.md)
```

### wiki/index.md (updated)

Replace the flex-processing line:

```md
- [workflows/flex-processing](workflows/flex-processing.md) — lower-cost asynchronous processing for non-urgent OpenAI workloads; Flex on older models, discounted `2h`/`8h` background completion windows (30%/40% off) on GPT-6.2 and later *(as_of: 2026-11-23)*
```

In the agent-execution-runtimes line, change "model-lab agent APIs (OpenAI Agents API)" to "model-lab agent APIs (OpenAI Agents API, Responses background mode)" and `as_of: 2026-10-07` → `as_of: 2026-11-23`.

### wiki/sources/articles/openai-background-mode-docs-2026-11.md (new)

```md
---
title: OpenAI API docs — Background mode
type: source
source_type: article
source_file: raw/articles/2026-11-23-developersopenaicom-api-docs-guides-background.md
url: https://developers.openai.com/api/docs/guides/background
ingested: 2026-11-23
domains: [agents]
---

# OpenAI API docs — Background mode

OpenAI's guide to running long Responses API requests asynchronously, including multi-step agent runs. The application sets `background: true`, keeps the response ID, and learns of completion by webhook or polling; requests can be canceled, and `soonest` background streams can resume from the last event. The guide introduces completion windows (`soonest`, `2h`, `8h`), with the longer two discounting token prices, and states that new models from GPT-6.2 launch without Flex processing. The docs page carries no publication date; captured 2026-11-23.

## Influenced pages
- [Flex processing](../../workflows/flex-processing.md) — Flex dropped on new models; discounted completion windows as replacement, guidance and caveats
- [Agent execution runtimes](../../concepts/agent-execution-runtimes.md) — background mode for multi-step agent runs in the model-lab agent APIs bullet

## Key claims extracted
- Completion windows: `soonest` (default, no discount), `2h` (30% below Standard), `8h` (40% below Standard); API targets completion within 2h/8h after acceptance and auto-retries eligible capacity errors
- Starting with GPT-6.2 Astra and Sol, new models launch without Flex processing (`service_tier: flex`)
- Discounted windows in public beta on GPT-6.2 Astra, GPT-6.2 Sol, GPT-6.1 Terra, GPT-6 Luna
- Follow-ups reusing window, `continuation_id`, model and project keep the discount and get higher queue priority
- Discounted windows require Standard processing and no streaming; they share the Batch/Background rate limit; their prompt cache is not reused by normal Standard requests
- Background mode temporarily stores data (encrypted at rest) even with `store: false` or ZDR
- Completion via `response.completed` webhook or polling while `queued`/`in_progress`; cancel is idempotent; streams resume with `starting_after`
```

## Schema / vocabulary additions

None.

## Open questions

- The Flex processing page now mostly describes its replacement. Should it be renamed (for example `workflows/async-discounted-processing.md`, "OpenAI discounted async processing") with inbound links re-pointed, or keep its current title? Assumed keep for now.
	- Yes, rename
