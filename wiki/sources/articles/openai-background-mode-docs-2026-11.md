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
- [OpenAI discounted async processing](../../workflows/async-discounted-processing.md) — Flex dropped on new models; discounted completion windows as replacement, guidance and caveats (page renamed from Flex processing)
- [Agent execution runtimes](../../concepts/agent-execution-runtimes.md) — background mode for multi-step agent runs in the model-lab agent APIs bullet
- [GPT-6.1 Terra](../../models/gpt-6-1-terra.md) — discounted completion windows available on Terra

## Key claims extracted
- Completion windows: `soonest` (default, no discount), `2h` (30% below Standard), `8h` (40% below Standard); API targets completion within 2h/8h after acceptance and auto-retries eligible capacity errors
- Starting with GPT-6.2 Astra and Sol, new models launch without Flex processing (`service_tier: flex`)
- Discounted windows in public beta on GPT-6.2 Astra, GPT-6.2 Sol, GPT-6.1 Terra, GPT-6 Luna
- Follow-ups reusing window, `continuation_id`, model and project keep the discount and get higher queue priority
- Discounted windows require Standard processing and no streaming; they share the Batch/Background rate limit; their prompt cache is not reused by normal Standard requests
- Background mode temporarily stores data (encrypted at rest) even with `store: false` or ZDR
- Completion via `response.completed` webhook or polling while `queued`/`in_progress`; cancel is idempotent; streams resume with `starting_after`
