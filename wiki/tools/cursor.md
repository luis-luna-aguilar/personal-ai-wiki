---
title: Cursor
type: tool
domains: [coding, agents]
subcategory: agentic-coding-workspace
tags: [closed-source, agentic]
as_of: 2026-04-22
sources: [cursor-3-launch, cursor-pr-demos, cursor-bugbot-learning, coding-agent-control-planes, cursor-3-orchestration-bet, late-march-small-coding-models, cursor-cloud-agents-march, cursor-cloud-agents-february, cursor-third-era]
---

# Cursor

Cursor is an AI coding product from Anysphere. It started life as a VS Code fork focused on inline AI editing and pair programming, and with **Cursor 3** has been rebuilt from scratch as an agent-first workspace: a desktop app that surfaces local and cloud AI coding agents in one sidebar, supports multi-repo work, and lets users hand sessions back and forth between environments. The legacy Cursor IDE mode is still available inside the same product.

The strongest interpretive signal from the early-April reaction cycle is that Cursor 3 was not just a feature release. It was a bet about interface shape: the editor becomes secondary, while dispatching, monitoring, and reviewing agent work becomes the primary experience. That looks increasingly prescient as the broader category moves toward supervision surfaces, but the same sources also emphasize the risk that orchestration UX may outrun what mainstream users actually need today.

## Current status (as of 2026-04-14)

- **Cursor 3** is the current shipped version, announced in the "Meet the new Cursor" post on cursor.com/blog
- Late-February launch coverage already described the practical surface that the March 6 walkthrough later explained more cleanly: isolated cloud computers, self-testing agents, and video demos as review artifacts
- The March 6 cloud-agents walkthrough made the intended interaction model unusually explicit: remote agents boot their own environment, run the code, test changes, produce demo videos, and expose live remote control over the VM for human verification
- **Cursor 3.1** extends Cursor 3 with a tiled Agents Window for managing multiple agents side by side
- New top-level interface built from scratch (not the VS Code fork) and centered on agents
- Inherently multi-workspace: humans and agents work across multiple repos simultaneously
- Branch selection for cloud agents and improved search/filter controls make the cloud-agent layer feel more like a supervision surface than a background feature
- Cloud agents auto-attach demo videos and screenshots to PRs for visual review *(as of 2026-04-10)*
- **Bugbot** now learns rules from production PR feedback; Cursor reports a 78.13% resolution rate across 50,310 public PRs and 44,000+ learned rules across 110,000+ repos *(as of 2026-04-10)*
- Backed by [[models/composer-2|Composer 2]], Cursor's own coding model for complex long-horizon tasks; late-March coverage adds reported 61.7 TerminalBench 2.0, 73.7 SWE-bench Multilingual, low input-token pricing, and the now-disclosed Kimi-k2.5 base-model lineage
- Plugin marketplace ("Cursor Marketplace") supports MCPs, skills, and subagents, with one-click install and private team marketplaces
- Legacy "Cursor IDE" mode still available — switch back at any time

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

## Recent changes

- [2026-04-22] Added Truell's third-era data: 35% of Cursor internal PRs from cloud agents; 2:1 agent-to-Tab user ratio; 15× agent usage growth YoY
- [2026-04-22] Added Shipper vibe check: promising direction, awkward transition, early-product caveats
- [2026-02-25] Cursor cloud agents rolled out with isolated VMs, self-testing, and demo-video review before the later March walkthrough made the product thesis explicit
- [2026-03-06] Cloud-agents walkthrough made Cursor's thesis explicit: remote agents should test their own changes, return demo videos, and hand humans a supervision surface instead of just a diff
- [2026-04-14] Cursor 3.1 added a tiled Agents Window, saved layouts, branch selection for cloud agents, and stronger supervision controls for parallel agent work
- [2026-04-10] Bugbot learned rules: production PR feedback now turns into active review rules; Cursor reports 78.13% resolution across 50,310 public PRs
- [2026-04-10] Cloud agents now auto-attach demo videos and screenshots to GitHub PRs
- [2026-04-02] Cursor 3 announced — rebuilt agent-first interface, multi-repo, local↔cloud handoff, Composer 2, plugin marketplace

## Sources

- [[sources/articles/cursor-3-launch]]
- [[sources/articles/cursor-pr-demos]]
- [[sources/newsletters/coding-agent-control-planes]]
- [[sources/newsletters/cursor-3-orchestration-bet]]
- [[sources/newsletters/cursor-cloud-agents-march]]
- [[sources/newsletters/cursor-cloud-agents-february]]
- [[sources/tweets/cursor-third-era]]
