---
title: OpenAI discounted async processing
type: workflow
domains: [agents]
subcategory: agent-orchestration
tags: [openai]
as_of: 2026-11-23
sources: [openai-flex-processing, legacy-ai-tools-roadmap-xlsx, openai-background-mode-docs-2026-11]
---

# OpenAI discounted async processing

OpenAI's lower-cost asynchronous execution for workloads that do not need normal-latency responses: trade latency and completion certainty for cheaper large-scale processing. As of November 2026 the route on new models is a discounted completion window in Responses API background mode. New models from GPT-6.2 onward launch without Flex processing, which remains only on older models.

## Also called

Flex processing (retired for new models).

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

- [2026-11-23] Renamed from "Flex processing" (`workflows/flex-processing.md`) now that most of the page covers its replacement.
- [2026-11-23] New models from GPT-6.2 launch without Flex; added Responses API background mode with discounted `2h`/`8h` completion windows (30%/40% off) as the replacement, plus continuation IDs, webhooks and limits.

## Sources

- [OpenAI Flex processing guide](../sources/articles/openai-flex-processing.md)
- [AI Tools & Roadmap legacy workbook](../sources/notes/legacy-ai-tools-roadmap-xlsx.md)
- [OpenAI API docs — Background mode](../sources/articles/openai-background-mode-docs-2026-11.md)
