---
type: proposal
source: raw/tweets/2026-10-26-signulll-2100968622508175704.md
status: pending
created: 2026-10-26
---

# Proposal: signüll — browser use is a commodity

## Summary

### In short
Browser automation is turning into a commodity with no moat, and its value may shrink further as the few sites that carry most web traffic expose agent tools directly, although the long tail of portals will keep needing a browser. That is signüll's argument and the replies' rebuttal, quoting a Browser Use plus Jev demo that found flights in 7 seconds for under half a cent. The proposal adds the argument to Agent-readable web, updates its State of Computer Use line, and adds a source page. Reason to hesitate: the demo numbers come from a quoted post whose video was not read.

[[#Open questions|Open questions: none.]]

- [ ] **Approve all** — checking this box approves every item in `## Intended changes` and `## Schema / vocabulary additions` below; the individual boxes may stay empty.

### The source
On 18 September 2026 the commentator signüll posted (77K views) that "browser use is a commodity tool": there is no secret sauce in an agent that can open Chrome, log in, click buttons and submit a form. He expects it to become close to useless for two reasons. The web is extremely top-heavy, with roughly 98% of traffic going to about 100 domains by his count, and those sites will have to offer agent tools directly if they want to survive.

He was quoting Gregor Zunic, founder of Browser Use, who two days earlier announced a tiny open-source browser agent pairing Browser Use with Jev, TypeSafe's fast decision model. Zunic's post lists the design in three phrases (a new action space every step, the page's DOM as the state, a small model as a fallback for typing) and claims the agent found flights in 7 seconds at a cost of $0.0039, shown in a real-time video.

The replies are the useful counterweight. Several argue that 98% of traffic is not 98% of workflows: government portals, internal tools and the long tail of sites will keep needing a browser for years, and most products will not ship an MCP server or a CLI. Others point to WebMCP, which they say is on its way into Chrome, as the thing that would make browser automation a relic on the sites that adopt it.

### What changes
Agent-readable web describes sites serving Markdown, APIs and MCP servers to agents, plus fetch APIs for sites that don't, but not the argument that this makes browser automation itself a shrinking commodity.

- **Agent-readable web** gains one Current-status bullet with the commodity argument, the traffic-concentration claim, the long-tail rebuttal and the quoted Browser Use demo, and a What-to-watch line on WebMCP adoption. Page date stays 14 October.
- **State of Computer Use** extends the Agent-readable web line under its infrastructure subcategory with the commodity argument and adds a Recent-changes entry. The list is at its cap, so its oldest entry (Gemini generating downloadable files, 5 May) moves to history. Page date stays 14 October.
- One new source page for the post.

### What to weigh
The 7-second and $0.0039 figures are quoted from Zunic's post as signüll reposted it; the video and the Browser Use repository were not read. The proposal records them as the demo's claims and does not create a Browser Use page or a browser-agent subcategory from one quoted post.

## Intended changes

- [ ] **Update** `wiki/concepts/agent-readable-web.md` — add one Current-status bullet and one What-to-watch line; adds one Recent-changes entry dated 2026-09-18 (live list has 4, no spill); append one source id and link; `as_of` stays 2026-10-14
    > See draft below

- [ ] **Update** `wiki/state-of/computer-use.md` — extend the Agent-readable web leader line; adds one Recent-changes entry dated 2026-09-18 (live list has 10, at the cap); append one source id; `as_of` stays 2026-10-14
    > See draft below

- [ ] **Spill** `wiki/state-of/computer-use.md` → `wiki/history/state-of/computer-use.md` — the oldest Recent-changes entry (expected: [2026-05-05] Gemini downloadable files) moves to history
    > See draft below

- [ ] **Create** `wiki/sources/tweets/signulll-browser-use-commodity-2026-09-18.md` — source summary

## Page drafts

### wiki/concepts/agent-readable-web.md (updated)

Frontmatter `sources:` (append one id; `as_of` unchanged):

```
sources: [website-future-agent-readable-2026-07-02, vercel-agents-new-software-2026-07-03, agent-ready-saas-mcp-2026-06, cloudflare-agent-internet-monetization-2026-07, expand-fetch-launch-2026-10, signulll-browser-use-commodity-2026-09-18]
```

`## Current status` — append one bullet after the Expand Fetch bullet:

```
- The same shift feeds an argument that browser automation is becoming a commodity. signüll (September 2026) argues there is no durable moat in an agent that opens Chrome, logs in, and submits a form, and that browser use will matter less because the web is top-heavy (he puts ~98% of traffic on ~100 domains) and those sites will expose agent tools directly. Replies counter that 98% of traffic is not 98% of workflows: government portals and the long tail will need a browser for years. The post quotes a Browser Use demo pairing its open-source agent with TypeSafe's Jev decision model (a fresh action space each step, DOM state, a small-model fallback for typing) that reportedly found flights in 7 seconds for $0.0039.
```

`## What to watch` — append:

```
- Whether WebMCP, which commentators describe as on its way into Chrome, reaches enough adoption to make browser automation unnecessary on the sites that ship it, and how long the long tail of portals keeps needing a browser.
```

`## Recent changes` — insert one entry between the 2026-10-14 and 2026-07-08 entries:

```
- [2026-09-18] signüll argues browser use is a commodity that top sites will route around with agent tools; replies counter with long-tail and government-portal workflows; Browser Use + Jev demo quoted at 7 s / $0.0039 per flight search.
```

`## Sources` — append:

```
- [signüll on X — browser use is a commodity tool](../sources/tweets/signulll-browser-use-commodity-2026-09-18.md)
```

### wiki/state-of/computer-use.md (updated)

Frontmatter `sources:` — append one id (`signulll-browser-use-commodity-2026-09-18`) to the live list; `as_of` unchanged.

`### Agent-readable web infrastructure` — the Agent-readable web line becomes:

```
- [Agent-readable web](../concepts/agent-readable-web.md) — sites increasingly serve Markdown or structured machine-readable representations to agents while keeping visual pages for humans; the shift fuels an argument that browser automation is a moatless commodity, contested for long-tail sites *(as of 2026-09-18)*
```

`## Recent changes` — insert one entry between the 2026-09-30 and 2026-07-08 entries, then remove the oldest entry (see Spill):

```
- [2026-09-18] signüll calls browser use a commodity tool that top sites will make unnecessary with direct agent tools; replies argue long-tail and government sites will still need browsers.
```

### wiki/history/state-of/computer-use.md (updated — spill)

Append at the end of the file:

```

## Archived from current page on 2026-10-26

- [2026-05-05] Gemini now generates downloadable files from chat: Google Docs/Sheets/Slides, Microsoft Office formats, PDF, CSV, LaTeX, TXT, RTF, Markdown — artifact-producing assistant behavior
```

### wiki/sources/tweets/signulll-browser-use-commodity-2026-09-18.md (new)

```
---
title: signüll on X — browser use is a commodity tool
type: source
source_type: tweet
source_file: raw/tweets/2026-10-26-signulll-2100968622508175704.md
url: https://x.com/signulll/status/2100968622508175704
published: 2026-09-18
ingested: 2026-10-26
domains: [computer-use, agents]
---

# signüll on X — browser use is a commodity tool

Quote-post (77K views) arguing browser automation has no durable moat and will become far less useful because web traffic is concentrated on ~100 domains that will expose agent tools directly. Quotes Gregor Zunic (Browser Use founder, 2026-09-16) announcing a small open-source browser agent combining Browser Use with TypeSafe's Jev: a new action space every step, DOM state space, a small-LLM fallback for typing, a flight search in 7 seconds for $0.0039. Replies push back that traffic share is not workflow share (long tail, government portals, products without MCP or CLI) and point to WebMCP in Chrome as the eventual replacement on sites that adopt it.

## Influenced pages
- [Agent-readable web](../../concepts/agent-readable-web.md) — commodity argument, long-tail rebuttal, quoted Browser Use + Jev demo, WebMCP watch item
- [State of Computer Use](../../state-of/computer-use.md) — Agent-readable web line extended; Recent-changes entry

## Key claims extracted
- Browser use is a commodity: no secret sauce in logging into a website and completing a task
- ~98% of web traffic goes to ~100 domains (author's figure); those sites will introduce agent tools directly
- Quoted (Zunic, 2026-09-16): Browser Use + Jev browser agent found flights in 7 s for $0.0039; new action space every step, DOM state space, small LLM fallback to type; open source
- Replies: 98% of traffic is not 98% of workflows; government portals and the long tail still need a browser; most products won't have MCP/CLI
- Replies: WebMCP is "well on its way" to release in Chrome and would make browser use a relic on adopting sites
```

## Schema / vocabulary additions

None.

## Open questions

None.
