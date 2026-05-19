---
type: proposal
source: raw/articles/2026-05-18-jxnlgithubio-blog-writing-2026-05-10-codex-maxxing.md
status: pending
created: 2026-05-18
---

# Proposal: Codex-maxxing — advanced usage patterns (Jason Liu)

## Summary

Jason Liu (jxnl) published a detailed walkthrough of how he uses Codex for knowledge work beyond coding. Core thesis: Codex becomes a general knowledge-work operating loop when you add durable threads, voice+steering, scheduled Heartbeats, file-backed memory, Goals with verification criteria, and the side panel as a live work surface.

_Note: apply `proposals/2026-05-18-codex-adoption-ecosystem.md` first — it also updates `wiki/tools/codex.md` and creates the history spill file._

## Intended changes

- [x] **Update** `wiki/tools/codex.md` — add source to frontmatter, add Usage patterns section, add Recent changes entry (will require another spill after ecosystem proposal)
    > **Sources frontmatter:** add `codex-maxxing-jxnl-2026-05`
    >
    > **Add new section `## Usage patterns (jxnl, May 2026)` after `## Codex Chronicle`:**
    >
    > ```md
    > ## Usage patterns (jxnl, May 2026)
    >
    > **Durable threads + compaction**
    > Pinned threads compacted over months accumulate preferences, decisions, and history without recreation cost. Cmd+1–9 jumps to pinned threads. Trade-off: revisited threads are not in cache (higher cost), but continuity is worth it for high-value workstreams.
    >
    > **Voice input + steering**
    > Voice gets unedited thinking into Codex — vague context that's "too annoying to type" is natural to say. Steering: inject instructions after a tool call without waiting for the step to finish; queue up intent while the agent is working, then walk away.
    >
    > **Heartbeats (thread-local scheduling)**
    > Tell a thread "keep an eye on this every few hours" and it schedules itself. A thread can have multiple schedules, run until a condition is met, and adjust cadence. Example: Chief of Staff thread runs every 30 min checking Slack/Gmail, drafting replies; monitor loop crosses tool boundaries (Slack feedback → Remotion render → @computer upload).
    >
    > **Goals (autonomous task loops)**
    > Replace multi-turn prompt chains with a verifiable success criterion. Weak: "implement the plan." Strong: "migrate Rich (Python) to Rust, passing all its unit tests" — the test suite is the oracle. Key insight: "LLMs are exceptionally good at looping until they meet specific goals."
    >
    > **Memory as files**
    > Long-running threads need durable memory outside the conversation. Pattern: Obsidian vault (`AGENTS.md` at root instructs the agent to update relevant pages as it learns). Vault as GitHub repo: diffs become a review surface for memory. Why files: forces compression into a form that survives compaction or thread death.
    >
    > **$browser / @chrome / @computer distinction**
    > - `$browser` — local web surfaces the agent inspects and annotates via JavaScript
    > - `@chrome` — signed-in browser state and multiple tabs (e.g., authenticated research sessions)
    > - `@computer` — GUI-only work; blocks the app but is the last resort for no-API tasks
    >
    > **Side panel as work surface**
    > Not just a preview pane: it's where the artifact lives and where annotation + action happen simultaneously. Supports Markdown (commentable), spreadsheets (formula render + edits), CSV, PDFs, slides. In-app browser lets the agent see, control, and annotate web surfaces (Storybook, Remotion Studio, Slidev, Streamlit). Key pattern: a plain `index.html` (no server required) is more durable than a Vite app for rapid iteration; agent can update it on a Heartbeat cadence so a fresh artifact waits on return.
    > ```
    >
    > **Add to Recent changes (top):**
    > `- [2026-05-10] Codex-maxxing usage patterns (jxnl): durable threads, Heartbeats (thread-local scheduling), Goals with verification criteria, memory as files (vault + AGENTS.md), $browser/@chrome/@computer, side panel as live work surface`

- [x] **Spill** `wiki/tools/codex.md` → `wiki/history/tools/codex.md` — second spill after ecosystem proposal; oldest remaining entry falls off
    > After the ecosystem proposal spill, the oldest entry will be:
    > `- [2026-03-11] Best-practices guide codified the AGENTS.md + MCP + skills + automation workflow as the default way to get better Codex results`
    > Append this to `wiki/history/tools/codex.md`.

- [x] **Create** `wiki/sources/articles/codex-maxxing-jxnl-2026-05.md`
    > See draft below

## Page drafts

### wiki/sources/articles/codex-maxxing-jxnl-2026-05.md (new)

```md
---
title: Codex-maxxing — Jason Liu
type: source
source_type: article
source_file: raw/articles/2026-05-18-jxnlgithubio-blog-writing-2026-05-10-codex-maxxing.md
url: https://jxnl.github.io/blog/writing/2026/05/10/codex-maxxing/
published: 2026-05-10
ingested: 2026-05-18
domains: [coding, agents]
---

# Codex-maxxing — Jason Liu

Jason Liu's (jxnl) essay on using Codex as a general knowledge-work operating loop. Thesis: Codex stops being only a coding tool when you combine durable pinned threads (compacted over months), voice input + mid-task steering, Heartbeats (thread-local scheduled recurrence), Goals (autonomous loops against a verifiable success criterion), file-backed memory (Obsidian vault with AGENTS.md), and the side panel as a live work surface. Distinguishes $browser (local JS injection), @chrome (multi-tab authenticated sessions), and @computer (GUI-only fallback). Notes that a plain index.html is more durable than a Vite server for iterable artifact work. Published 2026-05-10.

## Influenced pages

- [Codex](../../tools/codex.md) — new Usage patterns section

## Key claims extracted

- Pinned threads: Cmd+1–9 shortcuts; megathreads compacted over months
- Steering: inject messages after tool calls without waiting
- Heartbeats: thread-local scheduling (Chief of Staff every 30 min; cross-tool monitor loops)
- Goals: give success criteria, not instructions; test suites as oracles
- Memory as files: Obsidian vault + AGENTS.md; GitHub repo for diff-based review
- $browser / @chrome / @computer distinction
- Side panel: commentable Markdown, spreadsheets, in-app browser (Storybook, Remotion, Slidev, Streamlit)
- Plain index.html preferred over Vite for rapid iteration
```
