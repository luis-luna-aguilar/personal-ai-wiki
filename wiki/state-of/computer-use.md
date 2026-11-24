---
title: State of Computer Use
type: state-of
domains: [computer-use]
tags: []
as_of: 2026-11-24
sources: [perplexity-computer-plaid, open-weight-momentum-early-april, claude-computer-use-late-march, perplexity-personal-computer, desktop-mobile-computer-use-february, pig-homepage, legacy-ai-tools-roadmap-xlsx, codex-for-work-2026-05-01, amazon-quick-work-context-assistant-2026-04-29, gemini-downloadable-files-2026-04-30, knowledge-work-os-agent-apps-2026-04-28, peekaboo-repo-2026-05-13, website-future-agent-readable-2026-07-02, vercel-agents-new-software-2026-07-03, codex-general-work-agents-2026-07, agent-ready-saas-mcp-2026-06, gemini-computer-use-aside-2026-06, cloudflare-agent-internet-monetization-2026-07, expand-fetch-launch-2026-10, weinstein-computer-use-180-degrees-2026-09-30, cua-spaces-connect-your-agent-docs, trycua-cua-repo-2026-11, ainews-cua-s1-forms-2026-09-19, perplexity-computer-local-mac-2026-10-20, vals-cua-bench-2026-10-13]
---

# State of Computer Use

Current state of AI agents that operate through real application UIs, interact with third-party services, and execute multi-step workflows on behalf of users — going beyond API tool-calling to interact with systems as a human would.

## Subcategories

### Computer use

Autonomous agents that orchestrate models, connect to external services, and execute complex workflows through application interfaces.

- [Perplexity Computer](../tools/perplexity-computer.md) — Perplexity's persistent digital-proxy agent: 19-model orchestration, 400+ app and 12,000+ financial-institution connectivity, remote control from any device; can now also run fully on-device on Apple-silicon Macs with a Perplexity-tuned Qwen model, using no credits, for Pro, Max and Enterprise *(as of 2026-10-20)*
- [Pig](../tools/pig.md) — Windows-focused computer-use platform with product, API, and SDK layers for automating application workflows on Windows machines *(as of 2026-04-22)*
- [Codex](../tools/codex.md) — OpenAI; horizontal computer-work agent across documents, browser flows, and workplace apps. Agents now combine screenshots, accessibility trees, DOM, and Playwright, write code that performs many actions per step, and recover from failures, beating the average person on many tasks; also in the Agents API *(as of 2026-09-30)*
- [Peekaboo](../tools/peekaboo.md) — open-source macOS CLI + MCP server for agent screen capture, UI detection, and action-first GUI automation; v3.0 unified screenshot/UI detection across CLI and MCP and added native agent flows *(as of 2026-05-11)*
- [Cua](../tools/cua.md) — open stack that gives coding agents their own desktops: Cua Spaces runs local or self-hosted macOS/Linux VMs that Claude Code, Codex and Cursor drive over MCP, including nested agent runs with no host credentials copied in *(as of 2026-11-24)*

Computer use is also broadening into thinner action layers: desktop Electron apps exposed through CDP-based skills and mobile app actions exposed through assistant integrations, not only full remote-desktop proxies.

- [Amazon Quick](../tools/amazon-quick.md) — Amazon; desktop work-context assistant that builds a personal knowledge graph from files, calendar, and Slack; integrates with Kiro CLI and Claude Code; caveated — secondary newsletter coverage only, not yet verified against primary Amazon documentation *(as of 2026-04-29)*
- [Gemini](../tools/gemini.md) — Google; Gemini 3.5 Flash adds built-in computer use across browser, desktop, and mobile with API access, sensitive-action confirmation, and prompt-injection-triggered task shutdown; also generates downloadable files directly from chat *(as of 2026-06-25)*
- **Aside** — agentic browser using local on-device browsing history and autofill to act across logged-in websites; benchmark leadership claims remain secondary until primary source is fetched *(as of 2026-06-25)*

**Knowledge-work OS pattern:** Every argues that left-sidebar desktop apps combined with agentic terminals/chat are converging on a common interface shape (Codex, Claude, Cursor). Sticky workflow state across sessions is the emerging switching cost and platform-lock mechanism.

**How far raw computer use still has to go:** on Vals AI's [CUA-bench](../sources/articles/vals-cua-bench-2026-10-13.md), where agents play six commercial games (three held out) from pixels, keyboard and mouse in real time, no tested model averages 20 of 100; GPT-6 Astra leads *(as of 2026-10-13)*.

### Agent-readable web infrastructure

Web surfaces optimized for agents rather than only for humans.

- [Agent-readable web](../concepts/agent-readable-web.md) — sites increasingly serve Markdown or structured machine-readable representations to agents while keeping visual pages for humans; Vercel reports doing this in production *(as of 2026-07-03)*
- **Cloudflare Monetization Gateway** — usage-based paywall for agent-accessed resources such as web pages, proprietary datasets, APIs, and MCP tools; early signal that the agent internet may monetize machine traffic differently from human pageviews *(as of 2026-07-08)*
- **Agent-ready SaaS** — products expose parseable docs, APIs, authentication, and MCP servers so user-chosen agents can operate against the product instead of being forced through weaker in-app assistants *(as of 2026-06-29)*

### Agent web data extraction

The reader side of the agent-readable web: APIs that fetch and clean arbitrary pages for agents.

- [Expand Fetch](../tools/expand-fetch.md) — renders the page like a browser, keeps tables and icons as Markdown, extracts hidden JSON, and snapshots every fetch for citation *(as of 2026-10-14)*

## Recent changes

- [2026-11-24] Added [Cua](../tools/cua.md): Cua Spaces lets coding agents create and drive their own macOS/Linux desktops over MCP, and its open CUA-S1-FORMS model scores form-filling decisions for computer use.
- [2026-10-20] Perplexity Computer can run fully local on Apple-silicon Macs: model, harness and execution on-device across local files and Mac apps, no credits used, open to Pro, Max and Enterprise.
- [2026-10-14] Added `Agent web data extraction` with [Expand Fetch](../tools/expand-fetch.md), the reader-side counterpart to sites serving agent-native Markdown.
- [2026-10-13] Vals AI's CUA-bench: real-time play of six commercial games (three held out) from pixels only; no tested model averages 20 of 100.
- [2026-09-30] OpenAI's Ari Weinstein calls computer use "180 degrees different" from a year ago: self-debugging agents, multi-modal input (accessibility trees, DOM, App Shots), code-writing multi-action steps, GPT-6.1 Sol at ~1/7 of Astra's computer-use cost, and agents testing the software they build.
- [2026-07-08] Cloudflare Monetization Gateway adds an agent-internet monetization signal: metered access for pages, datasets, APIs, and MCP tools.
- [2026-07-03] Added agent-readable web concept: Vercel reports serving Markdown directly to detected agent requests, signaling a split between human and machine website experiences.
- [2026-07-01] Every adds Codex examples outside coding: inbox/CRM cleanup, healthcare coordination, writing setups, meeting notes, and personal folders.
- [2026-06-29] Added agent-ready SaaS framing: products should expose docs, APIs, auth, and MCP servers for external agents.
- [2026-06-25] Gemini 3.5 Flash computer use moves browser/desktop/mobile action into a mainstream Gemini API tool; Aside launches as a browser-native computer-use product.

## Sources

- [Claude computer use in late March](../sources/newsletters/claude-computer-use-late-march.md)
- [Perplexity Personal Computer](../sources/newsletters/perplexity-personal-computer.md)
- [Desktop and mobile computer-use surfaces in late February](../sources/newsletters/desktop-mobile-computer-use-february.md)
- [Pig official product page](../sources/articles/pig-homepage.md)
- [Peekaboo GitHub repo](../sources/repos/peekaboo-repo-2026-05-13.md)
- [The website of the future may assemble itself for you](../sources/newsletters/website-future-agent-readable-2026-07-02.md)
- [Vercel's Andrew Qu on why agents are a new kind of software](../sources/newsletters/vercel-agents-new-software-2026-07-03.md)
- [Codex and Claude Code as general-purpose work agents](../sources/newsletters/codex-general-work-agents-2026-07.md)
- [Agent-ready SaaS and MCP surfaces](../sources/newsletters/agent-ready-saas-mcp-2026-06.md)
- [Gemini computer use and Aside agentic browser](../sources/newsletters/gemini-computer-use-aside-2026-06.md)
- [Cloudflare Monetization Gateway and agent internet monetization](../sources/newsletters/cloudflare-agent-internet-monetization-2026-07.md)
- [Announcing Expand Fetch](../sources/articles/expand-fetch-launch-2026-10.md)
- [Ari Weinstein: computer use is "180 degrees different"](../sources/newsletters/weinstein-computer-use-180-degrees-2026-09-30.md)
- [Cua docs — Connect your agent](../sources/articles/cua-spaces-connect-your-agent-docs.md)
- [trycua/cua GitHub README](../sources/repos/trycua-cua-repo-2026-11.md)
- [Perplexity — Perplexity Computer now runs fully local on Mac](../sources/articles/perplexity-computer-local-mac-2026-10-20.md)
- [Vals AI — CUA-bench leaderboard and methodology](../sources/articles/vals-cua-bench-2026-10-13.md)
