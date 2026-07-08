---
title: Cursor
type: tool
domains: [coding, agents]
subcategory: agentic-coding-workspace
tags: [closed-source, agentic]
as_of: 2026-06-30
sources: [cursor-3-launch, cursor-pr-demos, cursor-bugbot-learning, coding-agent-control-planes, cursor-3-orchestration-bet, late-march-small-coding-models, cursor-cloud-agents-march, cursor-cloud-agents-february, cursor-third-era, ai-security-scanners-2026-05-01, cursor-sdk-agent-runtime-2026-04-30, agent-first-ide-convergence-may-2026, cursor-composer-2-5-launch, spacex-cursor-june-2026, cursor-ios-mobile-app-2026-06]
---

# Cursor

Cursor is an AI coding product from Anysphere. It started life as a VS Code fork focused on inline AI editing and pair programming, and with **Cursor 3** has been rebuilt from scratch as an agent-first workspace: a desktop app that surfaces local and cloud AI coding agents in one sidebar, supports multi-repo work, and lets users hand sessions back and forth between environments. The legacy Cursor IDE mode is still available inside the same product.

The strongest interpretive signal from the early-April reaction cycle is that Cursor 3 was not just a feature release. It was a bet about interface shape: the editor becomes secondary, while dispatching, monitoring, and reviewing agent work becomes the primary experience. That looks increasingly prescient as the broader category moves toward supervision surfaces, but the same sources also emphasize the risk that orchestration UX may outrun what mainstream users actually need today.

## Current status (as of 2026-06-17)

- **Cursor 3** is the current shipped version, announced in the "Meet the new Cursor" post on cursor.com/blog
- Cursor for iOS is in public beta for paid users, letting users launch always-on cloud agents, control desktop agents remotely, use voice and slash commands, receive push notifications/Live Activities, inspect diffs, follow up, and merge PRs from mobile.
- Late-February launch coverage already described the practical surface that the March 6 walkthrough later explained more cleanly: isolated cloud computers, self-testing agents, and video demos as review artifacts
- The March 6 cloud-agents walkthrough made the intended interaction model unusually explicit: remote agents boot their own environment, run the code, test changes, produce demo videos, and expose live remote control over the VM for human verification
- **Cursor 3.1** extends Cursor 3 with a tiled Agents Window for managing multiple agents side by side
- New top-level interface built from scratch (not the VS Code fork) and centered on agents
- Inherently multi-workspace: humans and agents work across multiple repos simultaneously
- Branch selection for cloud agents and improved search/filter controls make the cloud-agent layer feel more like a supervision surface than a background feature
- Cloud agents auto-attach demo videos and screenshots to PRs for visual review *(as of 2026-04-10)*
- **Bugbot** now learns rules from production PR feedback; Cursor reports a 78.13% resolution rate across 50,310 public PRs and 44,000+ learned rules across 110,000+ repos *(as of 2026-04-10)*
- Backed by **Composer 2.5**, Cursor's in-house coding model (upgraded from Composer 2, May 2026): same Kimi K2.5 base, trained with targeted RL + textual hint injection at trajectory problem points, 25× more synthetic tasks than Composer 2, new "feature deletion" task type; pricing: $0.50/M input · $2.50/M output standard, $3.00/M · $15.00/M fast variant; next model in training at SpaceX/Colossus 2 scale (million H100-equivalents)
- Plugin marketplace ("Cursor Marketplace") supports MCPs, skills, and subagents, with one-click install and private team marketplaces
- Legacy "Cursor IDE" mode still available — switch back at any time
- **Cloud development environments** (May 2026): fully configured environments with cloned repos, dependencies, version history, rollback, Dockerfile-based configs, audit logs, and cached builds running 70% faster; agents can trace a Slack-reported issue across all affected repos and open PRs in each simultaneously; isolated secrets per environment
- **SpaceX acquisition (June 2026):** $60B all-stock deal; model co-training with xAI underway; expected to power both Cursor and Grok Build
- **Cursor Origin (June 2026):** agent-native git/code hosting; MCP/API extensible; team-agent collaboration and merge conflict handling built for autonomous agent commits

## What's new in Cursor 3

- **Cloud agents as first-class workers.** The March walkthrough clarifies that the key shift is not just running agents in the cloud, but giving them enough environment control to onboard themselves, execute tests, and return reviewable artifacts instead of speculative diffs.
- **Video-first review.** Cursor increasingly treats demo videos as the first pass on review: not a replacement for diff review, but a faster way to decide which agent output is worth iterating with.
- **Remote control over the agent VM.** Humans can take over the live environment, inspect terminals, and verify behavior directly rather than trusting screenshots or commit messages alone.
- **All your agents in one place.** Local and cloud agents (kicked off from desktop, mobile, web, Slack, GitHub, Linear) appear in one sidebar.
- **Run many agents in parallel.** Cloud agents produce demos and screenshots for the human to verify; same experience as `cursor.com/agents`, now embedded.
- **Local ↔ cloud handoff.** Move a session from cloud to local for hands-on edits; move local → cloud to keep long-running tasks alive while offline.
- **Diffs & PR flow.** New diffs view for editing/reviewing changes; stage, commit, and manage PRs from inside Cursor.
- **Files for understanding code.** Full LSP support — view files, go to definition — when you want to drop down a level.
- **Integrated browser.** Cursor can open, navigate, and prompt against local sites via a built-in browser tool.

## What's new in Cursor 3.1

- **Tiled Agents Window.** Run multiple coding agents in draggable panes and compare outputs without tab-switching.
- **Saved layout.** Cursor remembers how the human wants to supervise ongoing agent work.
- **Branch selection for cloud agents.** More explicit control over where remote work lands.
- **Improved search filters.** Better navigation across the agent workspace.

## The third era thesis

Michael Truell's April 2026 essay defines three eras of AI software development:

1. **Tab autocomplete** — code written keystroke-by-keystroke with AI fill-in
2. **Synchronous agents** — prompt-and-response loops, developer in the loop at every step; practical only for a few agents in parallel (they compete for local machine resources)
3. **Cloud agents** — agents running on their own VMs over hours; developer defines the problem and reviews artifacts (videos, previews, logs) rather than diffs; many in parallel is practical

Internal Cursor data (as of April 2026): 35% of PRs merged internally at Cursor are now created by autonomous cloud agents. Agent users now outnumber Tab users 2:1 (was the reverse in March 2025); agent usage has grown 15× in one year. Truell's profile of a "third era developer": agents write ~100% of their code, they spend time on problem breakdown and artifact review, they spin up multiple agents simultaneously instead of hand-holding one.

## Strengths

- First-class support for orchestrating multiple agents across repos
- Seamless local/cloud session migration is genuinely novel
- Plugin ecosystem (MCPs, skills, subagents) lowers the bar for extending agent behavior
- Drops back to traditional IDE when the user wants direct control

## Weaknesses / caveats

- Closed source; no published benchmark numbers in the launch post
- Vendor framing emphasizes a "third era" narrative — usefulness for everyday brownfield work is not yet demonstrated by external usage reports
- Requires buying into a new mental model (agent sessions as the unit of work) — users coming from the IDE-centric Cursor will need to relearn the surface
- The strongest external commentary on Cursor 3 treats it as a bold orchestration bet, not a settled win; the category direction looks real, but the ideal product shape is still being worked out
- Dan Shipper's vibe check (April 2026) after a week of internal Every testing: fast desktop performance, local↔cloud demo videos are a "wow moment," but "it's still an early product and it's not clear who will love it." The rewrite deprioritizes the IDE, which alienates sizable existing Cursor fans. Summary: "the right strategic move, but an awkward in-between stage."

## Cursor SDK (as of 2026-04-30)

Cursor released a TypeScript SDK that exposes the Cursor agent runtime headlessly — outside the IDE. The SDK enables:

- **CI/CD integration**: run Cursor agents inside automated pipelines without a desktop session
- **Server automations**: trigger agent work from events, webhooks, or scheduled jobs on remote servers
- **Cloud VM deployment**: deploy Cursor-powered agents on cloud compute without a local machine
- **MCP server integration**: use the SDK as a backend behind MCP-compatible tool servers
- **Model swapping**: switch underlying models without changing harness code
- **Embedded product agents**: ship Cursor-powered agents inside other products

The SDK repositions Cursor from a per-seat IDE product toward programmable agent infrastructure.

## SpaceX acquisition and Cursor Origin (June 2026)

SpaceX exercised a previously announced option to acquire Cursor in an all-stock $60B deal. Key implications:

- **Jointly trained model.** SpaceX/xAI and Cursor have been co-training a new model that will power both Cursor and Grok Build.
- **Cursor Origin.** Launched alongside the acquisition news: a git/code hosting product built for agent workloads. Features merge conflict handling optimized for agent-generated commits, MCP/API extensibility, team-agent collaboration surfaces, and audit trails. Designed as the natural storage layer for autonomous agent work.
- **Vertical integration.** The combined stack is model (xAI jointly trained) + IDE (Cursor) + code hosting (Origin), competing with Claude Code + Anthropic (model + terminal agent) and Codex + OpenAI (model + cloud agent).

## Recent changes

- [2026-06-30] Cursor for iOS public beta: launch always-on cloud agents, control desktop agents remotely, voice/slash commands, push notifications, Live Activities, diff review, follow-up, and PR merge from mobile.
- [2026-06-17] SpaceX acquires Cursor in $60B all-stock deal; Cursor Origin launched (agent-native git/code hosting); jointly trained model with xAI coming to Cursor and Grok Build
- [2026-05-18] Composer 2.5: targeted RL with textual hints + KL distillation; 25× synthetic tasks; fast-tier pricing ($3/$15 per M); next model in training at SpaceX/Colossus 2 scale
- [2026-05-14] Cloud development environments: multi-repo agent work with full env config, Dockerfile support, version history, rollback, isolated secrets, 70% faster cached builds; agents can cross-repo trace Slack issues → PRs
- [2026-04-30] Cursor SDK released: TypeScript SDK exposes the Cursor agent runtime headlessly for CI, automations, cloud VMs, MCP servers, model swapping, and embedded product agents; marks transition from IDE seat product toward agent infrastructure platform
- [2026-05-01] Cursor Security Review reported: always-on PR review and scheduled codebase scans; source is AINews secondary coverage, primary Cursor page not yet fetched
- [2026-04-22] Added Truell's third-era data: 35% of Cursor internal PRs from cloud agents; 2:1 agent-to-Tab user ratio; 15× agent usage growth YoY

## Sources

- [Meet the new Cursor (Cursor 3 launch)](../sources/articles/cursor-3-launch.md)
- [Cursor ships PR demo attachments](../sources/articles/cursor-pr-demos.md)
- [Coding agent control planes](../sources/newsletters/coding-agent-control-planes.md)
- [Cursor 3 orchestration bet](../sources/newsletters/cursor-3-orchestration-bet.md)
- [Cursor cloud agents and the supervision workspace thesis](../sources/newsletters/cursor-cloud-agents-march.md)
- [Cursor cloud agents in late February](../sources/newsletters/cursor-cloud-agents-february.md)
- [Michael Truell — "The third era of AI software development"](../sources/tweets/cursor-third-era.md)
- [Cursor SDK as programmable coding-agent runtime](../sources/newsletters/cursor-sdk-agent-runtime-2026-04-30.md)
- [Agent-first IDE convergence — May 2026](../sources/newsletters/agent-first-ide-convergence-may-2026.md)
- [Cursor Composer 2.5 — launch post](../sources/articles/cursor-composer-2-5-launch.md)
- [SpaceX acquires Cursor + Cursor Origin launch (June 2026)](../sources/newsletters/spacex-cursor-june-2026.md)
- [Cursor iOS mobile app public beta](../sources/articles/cursor-ios-mobile-app-2026-06.md)
