---
type: triage
sources:
  - raw/articles/2026-09-09-cursorcom-blog-scaling-agents.md
  - raw/newsletters/2026-04-17-meta-pivots-from-open-weights-big-pharma-bets-on.md
  - raw/tweets/2026-05-18-shannholmberg-2055335043904492011.md
  - raw/tweets/2026-09-09-undefinedki-2095876609689498067.md
status: pending
---

# Triage: raw files that were never triaged (sweep, 2026-10-19)

`scripts/raw_orphans.py` found raw files that no triage, proposal, or source page accounted for. Two causes, both now fixed: a digest triage file was overwritten twice by later runs with the same name (its records are restored as `applied/2026-09-07-ai-oldest-20-digest-recovered-1.md` and `-recovered-2.md`), and blocked or empty fetches were saved as raw files (`fetch_url.py` now refuses them). Four files have real content and are triaged below. The rest are listed at the end so every raw file is accounted for.

## Signals

- [ ] **[coding]** Cursor's "Scaling long-running autonomous coding": the first-generation agent-swarm post

    **What it is:** Cursor's account of running hundreds of concurrent agents on one project for weeks, writing over a million lines of code: why self-coordination through shared files failed, how the planner/worker split emerged, and what kept long runs on track. It is the first-generation post that the later "self-driving codebases" article builds on.

    **Why it matters:** Most of its lessons already sit on [Long-running agent swarms](../../wiki/workflows/long-running-agent-swarms.md), taken from the later post's recap. Ingesting it mainly adds the primary source and any details the recap dropped.

    **Sources:**
      - `raw/articles/2026-09-09-cursorcom-blog-scaling-agents.md` — full post (1,067 words)

    **Primary URL:** https://cursor.com/blog/scaling-agents
    **Recommended:** lightweight ingest (add as a source of Long-running agent swarms, fill gaps only)

- [ ] **[models]** The Batch, 17 April 2026: Meta's closed model, Big Pharma AI bets, US state AI laws, simulated human cohorts

    **What it is:** A DeepLearning.AI newsletter with four stories: Meta pivoting from open weights to a closed model (Muse Spark: text, image, and speech input up to 262K tokens, three reasoning modes, architecture undisclosed); large pharma companies committing to AI drug discovery; US states moving ahead with their own AI laws; and a method that generates 25 diverse personas per context for simulating human cohorts.

    **Why it matters:** Meta's pivot is already covered on [Muse Spark](../../wiki/models/muse-spark.md). The state-law patchwork could add to [AI governance and policy](../../wiki/trends/ai-governance-and-policy.md), and the cohort method to [Synthetic human simulation](../../wiki/trends/synthetic-human-simulation.md). It is six months old.

    **Sources:**
      - `raw/newsletters/2026-04-17-meta-pivots-from-open-weights-big-pharma-bets-on.md` — full newsletter (4,106 words)

    **Primary URL:** (newsletter email)
    **Recommended:** lightweight ingest, or skip as dated

- [ ] **[agents]** "How to Become a Hermes Agent Operator" — Shann Holmberg

    **What it is:** A long X Article (4,610 words, May 2026) on running [Hermes Agent](../../wiki/tools/hermes-agent.md) as a one-person marketing operation on a single VPS: an "agent control room" template, specialist agents per function, cron-scheduled workflows, and growing from one agent to a team.

    **Why it matters:** A practitioner setup guide for a tool the wiki tracks. It may add a concrete operating pattern to Hermes Agent or to [Multi-agent coordination](../../wiki/workflows/multi-agent-coordination.md).

    **Sources:**
      - `raw/tweets/2026-05-18-shannholmberg-2055335043904492011.md` — full article

    **Primary URL:** https://x.com/shannholmberg/status/2055335043904492011
    **Recommended:** lightweight ingest

- [ ] **[training]** "How to turn AI into a whole team that runs your business" — Yarchi, sponsored by Viktor

    **What it is:** An X Article (4 September 2026, marked as a paid partnership with Viktor.com) on running a small business with AI agents: split the business into lanes, write shared context once, draw an approval line for what needs a person, brief each lane (five copyable briefs), and put the lanes on a schedule. The author says the setup took an afternoon and was run against real files.

    **Why it matters:** A concrete small-business version of the "agents as a team" pattern. Viktor is one of the platforms the [Multiplayer AI](../../wiki/concepts/multiplayer-ai.md) manifesto names. It is sponsored content, so it reads as a vendor walkthrough.

    **Sources:**
      - `raw/tweets/2026-09-09-undefinedki-2095876609689498067.md` — full article (1,475 words)

    **Primary URL:** https://x.com/undefinedKi/status/2095876609689498067
    **Recommended:** lightweight ingest

## Accounted for, nothing to ingest

### Failed fetches (block pages or empty shells)

These raw files hold no source content (bot checks, login walls, 404s, or an empty page). Where the content matters, it reached the wiki through another source.

- `raw/articles/2026-04-21-mckinseycom-capabilities-mckinsey-digital-our-insights-the-a.md` — "Access Denied"; the McKinsey piece is ingested as `mckinsey-agentic-org`
- `raw/articles/2026-04-23-xcom-claudedevs-status-2047086372666921217.md` — X logged-out shell; the linked post is ingested as `anthropic-mcp-production-systems`
- `raw/articles/2026-04-24-openaicom-index-codex-for-almost-everything.md` — Cloudflare "Just a moment" page
- `raw/articles/2026-04-25-api-docsdeepseekcom-news-news250425.md` — 404 page
- `raw/articles/2026-07-07-helpopenaicom-en-articles-20001325-a-preview-of-gpt-56-sol-t.md` — empty shell; GPT-5.6 Sol is covered from other sources
- `raw/articles/2026-07-07-xcom-i-article-2073491212477378560.md` — "JavaScript is not available"
- `raw/tweets/2026-07-06-claudedevs-2074208949205881033.md` — tweet with only a t.co link, no text
- `raw/tweets/2026-09-09-davidondrej1-2093966150124122222.md` — empty page ("Untitled")
- `raw/tweets/2026-04-30-xcom-bryanecanostatus20496597274920.md` — login-walled forward of a claimed Meta Ads MCP/CLI release; never verified and no page cited it, so its source page was removed on 2026-10-19

### Duplicate saves

`python3 scripts/raw_orphans.py` lists 52 raw files that were saved twice under different names (mostly t.co redirects and re-fetched tweets). In each case the other copy is accounted for.
