---
title: Flex processing
type: workflow
domains: [agents]
subcategory: agent-orchestration
tags: [openai]
as_of: 2026-04-22
sources: [openai-flex-processing, legacy-ai-tools-roadmap-xlsx]
---

# Flex processing

Flex processing is OpenAI's lower-cost asynchronous execution mode for workloads that do not need normal-latency responses. It is best treated as a workflow pattern: trade latency and completion certainty for cheaper large-scale processing.

## Current guidance

- Use Flex when the task is batchable and non-urgent
- Good fit for offline enrichment, lower-priority research jobs, and delayed content generation
- Do not use it for latency-sensitive product paths or tightly interactive loops

## Caveats

- Slower and less deterministic than standard processing
- Retry and failure handling need to be designed explicitly

## Sources

- [[sources/articles/openai-flex-processing]]
- [[sources/notes/legacy-ai-tools-roadmap-xlsx]]

