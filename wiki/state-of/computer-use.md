---
title: State of Computer Use
type: state-of
domains: [computer-use]
tags: []
as_of: 2026-07-08
sources: [perplexity-computer-plaid, open-weight-momentum-early-april, claude-computer-use-late-march, perplexity-personal-computer, desktop-mobile-computer-use-february, pig-homepage, legacy-ai-tools-roadmap-xlsx, codex-for-work-2026-05-01, amazon-quick-work-context-assistant-2026-04-29, gemini-downloadable-files-2026-04-30, knowledge-work-os-agent-apps-2026-04-28, peekaboo-repo-2026-05-13, website-future-agent-readable-2026-07-02, vercel-agents-new-software-2026-07-03, codex-general-work-agents-2026-07, agent-ready-saas-mcp-2026-06, gemini-computer-use-aside-2026-06, cloudflare-agent-internet-monetization-2026-07]
---

# State of Computer Use

Current state of AI agents that operate through real application UIs, interact with third-party services, and execute multi-step workflows on behalf of users — going beyond API tool-calling to interact with systems as a human would.

## Subcategories

### Computer use

Autonomous agents that orchestrate models, connect to external services, and execute complex workflows through application interfaces.

- [Perplexity Computer](../tools/perplexity-computer.md) — Perplexity's persistent digital-proxy model: always-on dedicated Mac mini environment, remotely controllable from any device, 19-model orchestration, 400+ app and 12,000+ financial-institution connectivity *(as of 2026-04-10)*
- [Pig](../tools/pig.md) — Windows-focused computer-use platform with product, API, and SDK layers for automating application workflows on Windows machines *(as of 2026-04-22)*
- [Codex](../tools/codex.md) — OpenAI; increasingly positioned as a horizontal computer-work agent for documents, spreadsheets, slides, browser flows, research, planning, inbox/CRM cleanup, meeting-note workflows, and connected workplace apps; current evidence remains newsletter synthesis *(as of 2026-07-01)*
- [Peekaboo](../tools/peekaboo.md) — open-source macOS CLI + MCP server for agent screen capture, UI detection, and action-first GUI automation; v3.0 unified screenshot/UI detection across CLI and MCP and added native agent flows *(as of 2026-05-11)*

Computer use is also broadening into thinner action layers: desktop Electron apps exposed through CDP-based skills and mobile app actions exposed through assistant integrations, not only full remote-desktop proxies.

- [Amazon Quick](../tools/amazon-quick.md) — Amazon; desktop work-context assistant that builds a personal knowledge graph from files, calendar, and Slack; integrates with Kiro CLI and Claude Code; caveated — secondary newsletter coverage only, not yet verified against primary Amazon documentation *(as of 2026-04-29)*
- [Gemini](../tools/gemini.md) — Google; Gemini 3.5 Flash adds built-in computer use across browser, desktop, and mobile with API access, sensitive-action confirmation, and prompt-injection-triggered task shutdown; also generates downloadable files directly from chat *(as of 2026-06-25)*
- **Aside** — agentic browser using local on-device browsing history and autofill to act across logged-in websites; benchmark leadership claims remain secondary until primary source is fetched *(as of 2026-06-25)*

**Knowledge-work OS pattern:** Every argues that left-sidebar desktop apps combined with agentic terminals/chat are converging on a common interface shape (Codex, Claude, Cursor). Sticky workflow state across sessions is the emerging switching cost and platform-lock mechanism.

### Agent-readable web infrastructure

Web surfaces optimized for agents rather than only for humans.

- [Agent-readable web](../concepts/agent-readable-web.md) — sites increasingly serve Markdown or structured machine-readable representations to agents while keeping visual pages for humans; Vercel reports doing this in production *(as of 2026-07-03)*
- **Cloudflare Monetization Gateway** — usage-based paywall for agent-accessed resources such as web pages, proprietary datasets, APIs, and MCP tools; early signal that the agent internet may monetize machine traffic differently from human pageviews *(as of 2026-07-08)*
- **Agent-ready SaaS** — products expose parseable docs, APIs, authentication, and MCP servers so user-chosen agents can operate against the product instead of being forced through weaker in-app assistants *(as of 2026-06-29)*

## Recent changes

- [2026-07-08] Cloudflare Monetization Gateway adds an agent-internet monetization signal: metered access for pages, datasets, APIs, and MCP tools.
- [2026-07-03] Added agent-readable web concept: Vercel reports serving Markdown directly to detected agent requests, signaling a split between human and machine website experiences.
- [2026-06-25] Gemini 3.5 Flash computer use moves browser/desktop/mobile action into a mainstream Gemini API tool; Aside launches as a browser-native computer-use product.
- [2026-07-01] Every adds Codex examples outside coding: inbox/CRM cleanup, healthcare coordination, writing setups, meeting notes, and personal folders.
- [2026-06-29] Added agent-ready SaaS framing: products should expose docs, APIs, auth, and MCP servers for external agents.
- [2026-05-11] Added [Peekaboo](../tools/peekaboo.md) as a local macOS computer-use action layer for agents: CLI + MCP screen capture, UI detection, and GUI automation.
- [2026-05-05] Added knowledge-work OS framing: left-sidebar desktop app + agentic terminal is emerging as a universal knowledge-work interface pattern; sticky workflow state creates switching costs
- [2026-05-05] Gemini now generates downloadable files from chat: Google Docs/Sheets/Slides, Microsoft Office formats, PDF, CSV, LaTeX, TXT, RTF, Markdown — artifact-producing assistant behavior
- [2026-05-05] Amazon Quick (caveated): desktop work-context assistant building personal knowledge graph from files/calendar/Slack, integrating with Kiro CLI and Claude Code; secondary coverage only — pending primary Amazon verification
- [2026-05-01] Added [Codex](../tools/codex.md) under `Computer use` as a horizontal computer-work contender; secondary newsletter coverage frames it as targeting docs, sheets, slides, browser flows, and connected workplace apps

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
