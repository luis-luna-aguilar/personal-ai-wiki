---
title: "The Code — GPT-5.6 Sol wins over developers; Cursor drops side chat; eval data is the real moat"
type: source
source_type: newsletter
source_file: raw/newsletters/2026-07-13-apple-just-sued-openai.md
url: https://codenewsletter.ai/p/openai-s-gpt-5-6-sol-wins-over-developers-cursor-drops-side-chat
published: 2026-07-13
ingested: 2026-09-06
domains: [training, agents]
---

# The Code — GPT-5.6 Sol wins over developers; Cursor drops side chat; eval data is the real moat

The Code's July 13 issue covers GPT-5.6 Sol's strong opening weekend, Cursor's 3.11 release (side chats), and an "Insight" section arguing that with five new frontier models launching in a month, model routing has become both necessary and commoditized — the differentiator is a team's own eval data, not the router itself. The issue's main story (Apple's lawsuit against OpenAI) is a separate, unrelated signal not actioned here.

## Influenced pages

- [Cursor](../../tools/cursor.md) — side chats, transcript search, cloud-agent hooks
- [Codex](../../tools/codex.md) — GPT-5.6 Sol weekend usage / combined Codex+Work user count corroboration
- [Cost-aware AI task routing](../../training/cost-aware-ai-task-routing.md) — added the eval-data-as-moat evidence bullet

## Key claims extracted

- Cursor shipped "side chats" in its 3.11 release: `/side` or `/btw` starts a parallel conversation that inherits the main chat's context, for researching libraries or double-checking decisions while the main agent keeps working; @-mention the side chat later to bring its answers back into the main thread
- The same release adds transcript search and cloud-agent hooks
- GPT-5.6 Sol went public on Thursday (July 9); developers praised its long agentic runs and subagent orchestration over the launch weekend; usage hit double the previous record, and OpenAI temporarily removed its five-hour usage cap in response to demand
- Codex and ChatGPT Work had 6M active users combined at the time of writing, per Codex lead Thibault Sottiaux
- Cognition's Devin Fusion switches models mid-task; Cognition's own benchmark claims it holds top-tier coding performance while cutting cost by 35%
- Not Diamond trains custom routers from a customer's own uploaded eval data (real prompts plus scored answers); this technology powers OpenRouter's "Auto" mode
- The argument: routing is now a commodity (OpenRouter, Azure, generic open-source routers all offer one); the durable asset is the eval data that defines "good" for a specific workload, since models themselves become commodities weekly
- Recommended starting point cited: Hamel Husain's guide to evals (hamel.dev/blog/posts/evals/)
