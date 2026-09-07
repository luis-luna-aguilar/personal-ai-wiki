---
title: Codex
type: tool
domains: [coding, agents, cybersecurity, computer-use]
subcategory: terminal-coding-agent
tags: [openai, closed-source, agentic]
as_of: 2026-08-12
sources: [openai-pro-100, ainews-2026-04-21, openai-codex-ongoing-tasks, coding-agents-review-and-orchestration-march, codex-security-march, codex-updates-april-2026, openai-gpt-5-5-launch, superhuman-2026-04-23, codex-broader-computer-work-2026-04-24, codex-for-work-2026-05-01, symphony-devin-terminal-orchestration-2026-04-28, openai-daybreak-2026-05-13, codex-mobile-may-2026, codex-adoption-ecosystem-2026-05, codex-maxxing-jxnl-2026-05, codex-zoom-mobile-2026-05, codex-general-work-agents-2026-07, every-urge-to-merge-2026-07-14, ainews-devin-fusion-router-moat-2026-07-14, chatgpt-work-launch-2026-08-04, unsloth-desktop-chatgpt-linux-2026-08-12]
---

# Codex

OpenAI's cloud-based agent surface, accessed via CLI, ChatGPT, and mobile. It started as a coding agent, but current product direction is expanding into a broader computer-work system that can operate across code, browser flows, documents, spreadsheets, inboxes, CRM cleanup, healthcare coordination, meeting notes, and repeatable knowledge-work tasks.

## Current status (as of 2026-07-14)

- **Folded into a ChatGPT "superapp" (July 2026):** OpenAI merged the standalone Codex app into a new ChatGPT desktop app with three modes — Chat (questions), Work (longer cross-tool assignments), and Codex (developer workflows); the previous ChatGPT app was relabeled "ChatGPT Classic." The move drew immediate backlash from power users (Theo Browne called it a "generational fumble"; Reddit threads described "mayhem" — duplicate apps, buried chats and projects, broken plugins, unclear usage limits). OpenAI course-corrected publicly with multiple usage-limit resets and, per Codex lead Thibault Sottiaux, a rollback of the context limit from 372K back down to 272K after it caused billing/usage side effects. Despite the rocky rollout, usage grew fast: chaining Fidji Simo's March disclosure (2M Codex users, an estimated 550K-700K on January 1) with a July tweet reporting 6M users on July 12 and 7M roughly a day later, AINews estimates Codex has grown around 10x year-to-date — compared with Claude Code's last public figure of roughly 2M weekly users and $2.5B ARR from February.
- 4M+ weekly active users; 5× messages/user growth; 1M+ app downloads in first week of launch
- Ollama added Codex app support, enabling local/open-model launch paths alongside cloud Codex
- MagicPath canvas now ships natively inside Codex for visual task planning
- /goal command extracted into portable MCP/slash-command form by community (@secemp9) — now usable outside ChatGPT
- Zed editor supports ChatGPT/Codex on existing ChatGPT subscription (same rate-limit model)
- GitHub Copilot App: agent merge feature; terminal commands get AI-generated risk assessment badges with explanations
- VS Code/Copilot team: "experience shaped by coding harness — context assembly, tool use, execution loops, memory — more than by the base model alone" — the harness-over-model thesis confirmed by a lab-adjacent team
- Cloud coding agent accessible from ChatGPT and CLI
- OpenAI's March 2026 best-practices guide made the intended operating model unusually explicit: give Codex a clear goal/context/constraints/done-when structure, move durable repo guidance into `AGENTS.md`, connect live external systems with MCP, turn repeated work into skills, and automate workflows only after they are stable manually
- March 2026 also expanded Codex into security review: Codex Security is a research-preview application-security agent that builds repo context, finds vulnerabilities, validates them in sandboxes, and proposes fixes
- OpenAI now frames Codex as broader than code editing: it can use Mac apps, connect to more tools, create images, learn from prior actions, remember work preferences, and take on repeatable tasks
- Product direction increasingly overlaps with computer use and ongoing workflow automation, not just one-shot coding sessions
- **Subagents in Codex:** parallel specialized agents can now be spun up inside Codex to keep the main context window clean, tackle independent task parts in parallel, and be steered independently as work unfolds
- **Usage-based pricing** rolling out for ChatGPT Business and Enterprise plans — no fixed seat costs; teams pay for what they use; lowers the adoption barrier for organizations that want to test at scale before committing
- **PR code review via ChatGPT subscription:** connect GitHub, enable Codex code review, then trigger with "@codex review this" on any PR; available on Plus and above
- GPT-5.5 now powers Codex; OpenAI frames it as more capable while using fewer tokens than GPT-5.4 on the same Codex tasks
- Codex now has a 400K context window on GPT-5.5, and OpenAI describes a Fast mode that trades higher cost for higher speed
- OpenAI reports 85%+ of the company uses Codex weekly across software engineering, finance, communications, marketing, data science, and product work
- Secondary coverage is now converging on the same interpretation OpenAI hinted at earlier in the week: Codex is becoming a broader computer-work agent spanning browser flows, documents, spreadsheets, presentations, and repeatable knowledge-work tasks
- Every's Codex-for-knowledge-work positioning reinforces that the product is being taught and marketed for drafting, research, summarization, parallel task execution, and lightweight internal-tool building — not just code edits
- May 2026 secondary coverage continues to frame Codex as a workflow surface beyond coding: browser-pane work, docs, sheets, inbox triage, product-management commands, and repeatable command packs.
- OpenAI's Daybreak announcement explicitly places Codex inside cyber-defense infrastructure alongside frontier models and security partners; details are thin pending a fuller official source.
- **Mobile preview** (May 2026): Codex accessible from the ChatGPT iOS/Android app; users can start tasks, review diffs, approve commands, and steer running sessions remotely while the agent continues on a laptop or devbox
- Zoom plugin (May 2026): agents can receive meeting context directly from Zoom — handoff pattern for meeting → task delegation without manual copy-paste
- "Keep Mac awake" support: longer-running Codex jobs continue without interruption when supervising from the phone app; prevents laptop sleep from terminating sessions
- Remote SSH now generally available for managed remote environments
- CI/CD hooks and scoped programmatic access tokens added for Business/Enterprise automation
- Enterprise switch promo: 2 months free Codex for teams switching from competitors within 30 days (launched May 14)
- nanoGPT speedrun (Prime Intellect, ~10K runs, ~14K H200 hours): both Opus 4.7 (2,930 steps) and GPT-5.5 (2,950) beat the human baseline (2,990); agents relied on existing human research and did not produce original ideas
- Every's July 2026 coverage adds nontechnical examples: inbox zero, CRM enrichment from emails/transcripts, family healthcare coordination, writing/workspace setups, and personal folders synced from meetings and voice notes.

## Workspace Agents (as of 2026-04-23)

Workspace Agents are shareable, Codex-powered team agents that run in Slack and ChatGPT for Business, Enterprise, Edu, and Teachers plans.

- Teams describe a job in natural language and ChatGPT builds the agent
- Agents are shareable with teammates and intended to improve over time
- The launch framing spans automation, research, drafting, coding, and data-analysis jobs
- Scheduled and background execution push Codex beyond one-off interactive sessions
- Launch promotion made the feature free through 2026-05-06 for the covered plan tiers

## Usage patterns (jxnl, May 2026)

**Durable threads + compaction**
Pinned threads compacted over months accumulate preferences, decisions, and history without recreation cost. Cmd+1–9 jumps to pinned threads. Trade-off: revisited threads are not in cache (higher cost), but continuity is worth it for high-value workstreams.

**Voice input + steering**
Voice gets unedited thinking into Codex — vague context that's "too annoying to type" is natural to say. Steering: inject instructions after a tool call without waiting for the step to finish; queue up intent while the agent is working, then walk away.

**Heartbeats (thread-local scheduling)**
Tell a thread "keep an eye on this every few hours" and it schedules itself. A thread can have multiple schedules, run until a condition is met, and adjust cadence. Example: Chief of Staff thread runs every 30 min checking Slack/Gmail, drafting replies; monitor loop crosses tool boundaries (Slack feedback → Remotion render → @computer upload).

**Goals (autonomous task loops)**
Replace multi-turn prompt chains with a verifiable success criterion. Weak: "implement the plan." Strong: "migrate Rich (Python) to Rust, passing all its unit tests" — the test suite is the oracle. Key insight: "LLMs are exceptionally good at looping until they meet specific goals."

**Memory as files**
Long-running threads need durable memory outside the conversation. Pattern: Obsidian vault (`AGENTS.md` at root instructs the agent to update relevant pages as it learns). Vault as GitHub repo: diffs become a review surface for memory. Why files: forces compression into a form that survives compaction or thread death.

**$browser / @chrome / @computer distinction**
- `$browser` — local web surfaces the agent inspects and annotates via JavaScript
- `@chrome` — signed-in browser state and multiple tabs (e.g., authenticated research sessions)
- `@computer` — GUI-only work; blocks the app but is the last resort for no-API tasks

**Side panel as work surface**
Not just a preview pane: it's where the artifact lives and where annotation + action happen simultaneously. Supports Markdown (commentable), spreadsheets (formula render + edits), CSV, PDFs, slides. In-app browser lets the agent see, control, and annotate web surfaces (Storybook, Remotion Studio, Slidev, Streamlit). Key pattern: a plain `index.html` (no server required) is more durable than a Vite app for rapid iteration; agent can update it on a Heartbeat cadence so a fresh artifact waits on return.

## Pricing (as of 2026-04-21)

- **Plus** ($20/mo) — baseline Codex usage included
- **Pro** ($100/mo, new) — 5× Codex usage over Plus, exclusive Pro model, unlimited Instant and Thinking models
- **Launch promo:** up to 10× Plus-level Codex usage for Pro subscribers through 2026-05-31

## Codex Chronicle (as of 2026-04-21)

Research preview. Background agents monitor recent screen activity, build memories from screenshots, and store them on-device. Users can inspect and edit stored memories.

- Rollout: Pro users on macOS only; excluding EU, UK, Switzerland
- Shift from explicit chat history to passive ambient context capture
- Competitive framing: Harrison Chase's "memory will be the great lock-in" argument points to accumulated ambient context as a switching cost, not just a convenience

## ChatGPT Work architecture (as of 2026-08-04)

A detailed independent teardown of Work — the ChatGPT mode OpenAI folded Codex into on 2026-07-14 — clarifies how the product actually holds state across tasks.

- Each Work task runs inside a persistent, isolated cloud microVM (Pro: 8 CPUs/20GB RAM/64GB disk; Plus: 14GB RAM), with the agent operating a separately hosted, persistent-profile Chrome browser through tool calls rather than a local browser on the same machine.
- Continuity across tasks deliberately does **not** live on the computer the way it does in OpenClaw. Each task gets its own `/workspace/scratch` directory, but cross-task context flows through product-managed services instead: Personal Context (queries prior chat/Work history on demand), the Library (a canonical file store distinct from each thread's local copy — the two can silently diverge if a file changes in the Library after a thread already has a local copy), and Projects (standing instructions plus source files, supplied to new tasks but not represented as a real directory).
- The user's "memory" supplied to each task is a product-maintained synthesized profile; the agent can reason from it but can't edit it or write OpenClaw-style memory files other tasks load by default.
- Early proactive-task suggestions: Work can surface a pre-authored prompt drawn from calendar/email context (e.g. a meeting-prep brief) at the start of a new conversation, though the user still has to select and run it — full unprompted autonomy isn't there yet.
- Scheduled Tasks come in two forms: a standalone automation that opens a fresh task from a saved prompt each run, and a heartbeat-triggered automation that resumes a specific existing thread with its context intact (heartbeats work in the desktop app but aren't yet exposed in Work on the web).
- The Plugin Directory has scaled past 1,000 plugins (apps, skills, app templates) but has a real discovery gap: Work doesn't suggest an installed-but-relevant plugin for a task, even when the user names the target service directly.
- Three weeks after the July 9 launch, Work plus Codex had reportedly crossed 10 million users; Greg Brockman has confirmed Work and regular Chat will merge into one product by the end of 2026.

## Recent changes

- [2026-08-12] ChatGPT desktop app ships for Linux in preview (Ubuntu, Debian, Fedora; x64/ARM64); the desktop app can now import and sync projects, chats, skills, and plugins from other agents into ChatGPT Work and Codex with automatic updates — read as an effort to cut agent-switching friction and make Codex/Desktop an integration hub.
- [2026-08-04] Independent architecture teardown of ChatGPT Work: persistent cloud microVM specs, deliberate split between agent-owned scratch space and product-managed continuity (Personal Context/Library/Projects), browser-service tool-call model, two-tier Scheduled Tasks, Plugin Directory discovery gap, and 10M-user milestone three weeks post-launch.
- [2026-07-14] OpenAI folded Codex into a new ChatGPT desktop "superapp" (Chat/Work/Codex modes); power users pushed back hard, but usage estimates put Codex around 6-7M users by mid-July, roughly 10x growth year-to-date.
- [2026-07-11] Rollout friction: 36-plus model/effort configuration combinations drew complaints; OpenAI ran multiple usage-limit resets and rolled the context limit back from 372K to 272K.
- [2026-07-01] Every frames Codex as a general-purpose workspace agent for inbox, CRM, healthcare coordination, writing, meeting-note, and personal knowledge workflows.
- [2026-05-19] Zoom plugin (meeting-to-task context handoffs), keep-Mac-awake for long-running remote sessions, additional mobile remote-execution improvements
- [2026-05-10] Codex-maxxing usage patterns (jxnl): durable threads, Heartbeats (thread-local scheduling), Goals with verification criteria, memory as files (vault + AGENTS.md), $browser/@chrome/@computer, side panel as live work surface
- [2026-05-16] 4M+ WAU, 5× messages/user, 1M+ app downloads; Ollama Codex support; MagicPath canvas; /goal as portable MCP; Zed subscription parity; VS Code/Copilot team confirms harness-over-model thesis
- [2026-05-15] Mobile preview in ChatGPT app: steer Codex sessions from iOS/Android while agent runs on devbox; Remote SSH GA; CI/CD hooks; scoped tokens; 30-day enterprise switch promo (2 months free)
- [2026-04-28] OpenAI Symphony: described as an open-source Codex orchestration spec for defining, invoking, and coordinating Codex subagents; issue-tracker integration as the primary input surface; secondary coverage from The Code newsletter — verify spec details against primary OpenAI documentation

## Sources

- [OpenAI launches $100/mo Pro plan](../sources/tweets/openai-pro-100.md)
- [AINews — Moonshot Kimi K2.6, Hermes Agent, Codex Chronicle (2026-04-21)](../sources/newsletters/ainews-2026-04-21.md)
- [OpenAI — Codex for (almost) everything](../sources/tweets/openai-codex-ongoing-tasks.md)
- [Coding agents move toward review and concurrent supervision](../sources/newsletters/coding-agents-review-and-orchestration-march.md)
- [Codex Security](../sources/newsletters/codex-security-march.md)
- [Codex updates — subagents, usage-based pricing, PR review](../sources/tweets/codex-updates-april-2026.md)
- [Introducing GPT-5.5 — OpenAI](../sources/articles/openai-gpt-5-5-launch.md)
- [Superhuman — Anthropic's unreleased model got hacked](../sources/newsletters/superhuman-2026-04-23.md)
- [Codex broadens into computer work](../sources/newsletters/codex-broader-computer-work-2026-04-24.md)
- [Symphony and Devin for Terminal orchestration](../sources/newsletters/symphony-devin-terminal-orchestration-2026-04-28.md)
- [OpenAI Daybreak for cyber defenders](../sources/tweets/openai-daybreak-2026-05-13.md)
- [Codex mobile preview + enterprise push — May 2026](../sources/newsletters/codex-mobile-may-2026.md)
- [Codex adoption + ecosystem expansion — AINews coverage](../sources/newsletters/codex-adoption-ecosystem-2026-05.md)
- [Codex-maxxing — Jason Liu](../sources/articles/codex-maxxing-jxnl-2026-05.md)
- [Codex Zoom plugin + keep-Mac-awake — AINews (May 2026)](../sources/newsletters/codex-zoom-mobile-2026-05.md)
- [Codex and Claude Code as general-purpose work agents](../sources/newsletters/codex-general-work-agents-2026-07.md)
- [Every — The Urge to Merge (ChatGPT and Codex)](../sources/newsletters/every-urge-to-merge-2026-07-14.md)
- [AINews — Codex usage growth, coding-agent cost/perf tradeoffs, and Devin Fusion](../sources/newsletters/ainews-devin-fusion-router-moat-2026-07-14.md)
- [ChatGPT Work architecture teardown](../sources/newsletters/chatgpt-work-launch-2026-08-04.md)
- [Local AI tooling: Unsloth Desktop, ChatGPT desktop for Linux](../sources/newsletters/unsloth-desktop-chatgpt-linux-2026-08-12.md)
