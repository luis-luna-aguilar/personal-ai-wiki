---
type: proposal
source: raw/newsletters/2026-08-29-ainews-openai-shuts-off-cursor.md
status: pending
created: 2026-09-08
---

# Proposal: OpenAI shuts off Cursor's model access

## Summary

### The source

An AINews digest (2026-08-29) reports that, following the close of Cursor's acquisition by SpaceX, OpenAI cut Cursor's access to its models. OpenAI's own blog post on the decision cites "our experience with Elon Musk's companies violating contracts" as the leading reason — a framing AINews says should be taken at face value given the long public history of acrimony between the two companies' leaders (Musk was an early OpenAI backer and funder, and a lawsuit between the parties failed earlier this year). AINews draws a direct parallel to what Anthropic did to Windsurf when Windsurf was being considered for an OpenAI acquisition. The piece also notes the timing works differently than it would have a year ago: Cursor's launch-video appearance alongside GPT-5 made cutting them off a nonstarter back then, but today Claude models are seen as far ahead in coding, GPT-5.6 is a credible OpenAI-side alternative, and Cursor's own SpaceX/xAI ownership gives it Grok 4.6 to lean on — plus a viable Grok Bot competing with Codex/ChatGPT. Cursor's public response was diplomatic: noting OpenAI is only about 5% of its traffic, while not accepting the decision as final.

### What changes

`tools/cursor.md` already documents the June 2026 SpaceX acquisition and the jointly-trained Grok 4.5/4.6 relationship that followed. This proposal adds the model-access cutoff as a new bullet and Recent-changes entry, bumps `as_of` to 2026-08-29, and creates the source summary page (this raw file is also cited by five other proposals in this batch — GLM-5.3, Tencent/Qwen, Microduck, harness-evolution, AI-safety-cluster, and Perplexity Search Index — so its Influenced-pages list is front-loaded with all of them).

### What to weigh

Nothing beyond the sourcing already present on this page — this is straightforwardly a direct update following an established page's existing SpaceX-acquisition thread, with a single, well-explained primary-ish source (AINews' own reporting, not just a relay of someone else's tweet).

## Intended changes

- [x] **Approve all** — checking this box approves every item below; the individual boxes may stay empty.

- [ ] **Update** `wiki/tools/cursor.md` — add OpenAI model-access cutoff bullet, bump `as_of`, add Recent-changes entry
    > See draft below

- [ ] **Create** `wiki/sources/newsletters/ainews-openai-shuts-off-cursor-2026-08-29.md` — source summary

## Page drafts

### wiki/tools/cursor.md (updated)

```md
---
as_of: 2026-08-29
sources: [..., ainews-openai-shuts-off-cursor-2026-08-29]
---

## SpaceX acquisition and Cursor Origin (June 2026)

(... existing bullets unchanged ...)

- **OpenAI cuts model access (August 2026).** Following the close of Cursor's SpaceX acquisition, OpenAI cut Cursor's access to its models, citing "our experience with Elon Musk's companies violating contracts" — mirroring what Anthropic did to Windsurf during OpenAI's earlier acquisition interest there. Cursor's response was diplomatic (OpenAI is only ~5% of its traffic) but didn't accept the decision as final; Cursor now leans on Grok 4.6 via its SpaceX/xAI relationship, while GPT-5.6 remains a live OpenAI-side alternative and Claude models are still seen as the strongest coding option overall.

## Recent changes

- [2026-08-29] OpenAI cuts Cursor's model access following the SpaceX acquisition close, citing contract-violation history with Musk's companies; Cursor leans on Grok 4.6 as a result.
- (... existing entries follow ...)
```

### wiki/sources/newsletters/ainews-openai-shuts-off-cursor-2026-08-29.md (new)

```md
---
title: "[AINews] OpenAI shuts off Cursor"
type: source
source_type: newsletter
source_file: raw/newsletters/2026-08-29-ainews-openai-shuts-off-cursor.md
url: https://www.latent.space/p/ainews-openai-shuts-off-cursor
published: 2026-08-29
ingested: 2026-09-08
domains: [coding, models, agents]
---

# AINews — OpenAI shuts off Cursor

AINews digest covering OpenAI cutting Cursor's model access post-SpaceX-acquisition, GLM-5.3's full open-weighting plus Tencent Hy4-preview/Qwen3.8-Flash, Microduck sales figures, agent harness evolution (Google's "wiki" skill-evolution paper, agents.md fine-tuning, AGY patterns, CommerceAgentBench), a cluster of AI safety/alignment stories (OpenAI/HF incident retrospective, Anthropic automated alignment research, EvoMal), and Artificial Analysis's new Search Index benchmark.

## Influenced pages

- [Cursor](../../tools/cursor.md) — OpenAI model-access cutoff
- [GLM-5.3](../../models/glm-5-3.md) — full GLM-5.3 open-weighting, day-0 vLLM specs
- [Open-weight momentum broadens](../../trends/open-weight-momentum-broadens.md) — Tencent Hy4-preview, Qwen3.8-Flash
- [Physical AI deployment curve](../../trends/physical-ai-deployment.md) — Microduck sales figures, simulator design
- [Harness (agent)](../../concepts/harness.md) — Google's "wiki" skill-evolution paper, agents.md/claude.md fine-tuning, AGY patterns, cloud-resident agent shift
- [Agent safety and alignment research](../../trends/agent-safety-and-alignment-research.md) — Greenblatt's retrospective, Anthropic automated alignment research, EvoMal paper
- [Perplexity Computer](../../tools/perplexity-computer.md) — Artificial Analysis Search Index, Perplexity Search #1

## Key claims extracted

- OpenAI cut Cursor's model access post-SpaceX-acquisition, citing contract-violation history with Musk's companies
- GLM-5.3 (non-Flash) went open-weight with day-0 vLLM support (744B/40B)
- Tencent Hy4-preview (770B/49B) and Qwen3.8-Flash (125B/6B) launched
- Microduck: $2.6M in orders in 24 hours, simulator design details
- Google's "wiki" skill-evolution paper: skills transfer across model families, sometimes beating self-evolved skills
- Redwood's Ryan Greenblatt gave a detailed six-day-investigation account of the OpenAI/Hugging Face incident
- Anthropic published results on Claude autonomously improving smaller-model alignment over 48 hours/1 GPU
- Artificial Analysis launched a Search Index benchmark; Perplexity Search placed #1
```
