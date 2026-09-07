---
title: "The Urge to Merge (ChatGPT and Codex)"
type: source
source_type: newsletter
source_file: raw/newsletters/2026-07-14-the-urge-to-merge-chatgpt-and-codex.md
url: https://every.to/context-window/the-urge-to-merge-chatgpt-and-codex
published: 2026-07-14
ingested: 2026-09-06
domains: [coding, agents]
---

# The Urge to Merge (ChatGPT and Codex)

Every's Katie Parrott on the ChatGPT/Codex merge backlash and Anthropic's countermoves during the same week — plus a practical workflow for using an expensive model (Fable 5) as the planner/reviewer over a cheaper model (Sonnet, or GPT-5.6 Sol across labs) as the executor. The `url` above is inferred from Every's "Context Window" column naming pattern; a distinct "view online" permalink was not present in the plain-text capture.

## Influenced pages
- [Codex](../../tools/codex.md) — the ChatGPT-desktop merge and backlash
- [Claude Code](../../tools/claude-code.md) — Anthropic's countermoves

## Key claims extracted
- OpenAI merged the standalone Codex app into the new ChatGPT desktop app (three modes: Chat, Work, Codex); the previous ChatGPT app was relabeled "ChatGPT Classic"
- Developer/YouTuber Theo Browne called the merge a "generational fumble"; Reddit threads described "mayhem" — duplicate apps, buried chats/projects, broken plugins, unclear limits
- ChatGPT has 800M+ weekly users vs. Codex's ~5M weekly users at the time of the merge — OpenAI is betting the merge trades some power-user alienation for a much larger audience
- Anthropic reset Claude's 5-hour and weekly usage allowances; pushed Fable 5's paid-plan promotional cutoff from July 7 → 12 → 19 while keeping Claude Code's weekly limits 50% higher throughout; added an in-app browser to Claude Code desktop; merged Chat and Cowork into one "home" tab
- Workflow: use an expensive model (Fable 5) as planner/reviewer delegating bounded implementation work to a cheaper model (Sonnet inside Claude Code, or GPT-5.6 Sol via Codex) — includes concrete `.claude/agents/` and `.claude/skills/` setup snippets
- A cited paper (arXiv 2607.08010) reported a 53% agent error-rate drop after the agent stopped rewriting code from scratch and instead saved and reused working solutions as tools
