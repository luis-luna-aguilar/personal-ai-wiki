---
title: 'ScaleDown website crawl (homepage, docs, API reference, research, examples, pricing)'
type: source
source_type: article
source_file: raw/articles/2026-10-19-scaledownai-site-crawl.md
url: https://scaledown.ai/
ingested: 2026-10-19
domains: [models]
---

# ScaleDown website crawl (homepage, docs, API reference, research, examples, pricing)

An 83-page crawl of scaledown.ai and docs.scaledown.ai: model pages, pricing, API reference (classify, decisions, extract, summarize, compress, batch), benchmark methodology and per-provider tables, research notes, examples, guides, DietCode and ScaleDown Agent docs, and four blog posts. Most pages are undated; the blog posts are dated 2026-05-13 to 2026-06-03 and one RAG example February 2025, so no single `published:` date applies.

## Influenced pages

- [ScaleDown](../../models/scaledown.md) — page created
- [State of Models](../../state-of/models.md) — leader bullet under "Specialized utility models"

## Key claims extracted

- Four task models: Classify, Extract, Summarize, Compress; Compress, Extract and Classify are encoder-only (output free), Summarize has a decoder step
- Pricing: $0.05 per 1M text input tokens (all four), $0.15 per 1M image input tokens (not Compress), output free; 1M context (Compress "unlimited"); 1M free tokens for new accounts; 20% off via OpenRouter; blogs say 50M free tokens per agent
- Batch API: `POST /v1/batches` JSONL, extract/summarize/classify only, poll `GET /v1/batches/{id}`, OpenAI ChatCompletion-shaped output
- Decisions API (`POST /v1/scaledown`) is a Jev-compatible layer over Classify (choice, noul, score questions)
- Compress `rate: "auto"` typically achieves 50–70% compression on prose; not recommended under ~500 tokens or for code/JSON; retained fraction below 0.3 risks fact loss on dense content
- Benchmark method: CLINC OOS accuracy, CUAD F1, QMSum ROUGE-L, FinanceBench F1 (end-to-end)
- Average accuracy gains vs provider lineups: OpenAI +8.72%, Anthropic +8.0%, Gemini +9.0%, Grok +7.93%, DeepSeek +19.5%, Qwen +16.71%; 2.2–13.9× faster, 9–161× cheaper
- GLiNER2.5: ScaleDown +15.5 pp classify, +0.2 pp extract; GLiNER faster and free locally; the public GLiNER comparison page returns 404
- Classify blog (2026-05-13): 90.53%, +3.46 points over GPT-5.4 Mini (87.07%) and +10.86 over GPT-5.4 Nano; $0.0008 vs $0.16 run cost
- FinanceBench with o4-mini: F1 0.255 compressed vs 0.199 uncompressed; $7.20 vs $18.50 per 1K calls
- Self-hosted deployment (blog 2026-06-03): containers, VPC or air-gapped, per-deployment license, L40 node serves all four models for moderate workloads
- DietCode plugin (Claude Code, Codex CLI, Cursor) and ScaleDown Agent (MCP server for migrating LLM call sites)
