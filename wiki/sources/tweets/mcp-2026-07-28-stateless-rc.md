---
title: "MCP 2026-07-28 release candidate: stateless protocol"
type: source
source_type: tweet
source_file: raw/tweets/2026-08-25-redirect-e9187825-ab02-42eb-ac5f-ad4d73f120dc.md
url: https://x.com/dsp_
published: 2026-05-22
ingested: 2026-08-25
domains: [agents]
---

# MCP 2026-07-28 release candidate: stateless protocol

David Soria Parra (an MCP protocol maintainer) announced the release candidate for the MCP 2026-07-28 protocol revision. The headline change: MCP becomes stateless — no handshake, no session ID, and any request can hit any server instance. The RC also adds first-class extensions (MCP Apps, Tasks), auth hardening, and a proper deprecation policy. AINews's recap reads the statelessness as a big operational shift for infra teams (easier scaling, simpler load balancing, fewer sticky-session concerns).

## Influenced pages
- [Model Context Protocol](../../concepts/mcp.md) — added the stateless RC as a protocol-evolution update

## Key claims extracted
- MCP 2026-07-28 RC removes handshake and session-ID requirements; any request can hit any server instance
- Adds MCP Apps and Tasks as first-class protocol extensions
- Adds auth hardening and a "proper deprecation policy"
- The operational reading (easier scaling, simpler load balancing, fewer sticky sessions) is AINews's gloss, not part of the tweet text
- The "2026-07-28" string names the protocol revision, not its announcement date. The tweet text was captured only from the fetched page title (the raw file is a Substack redirect whose body is a reply, not the original post), so `url:` is the author's profile and `published:` is inferred from the AINews issue that carried it (2026-05-23, covering the prior day) — not read from the tweet itself. Grounded in an MCP maintainer's account, not an official MCP spec-repo changelog
