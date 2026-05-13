---
title: Symphony and Devin for Terminal orchestration
type: source
source_type: newsletter
source_file: raw/newsletters/2026-04-28-major-updates-from-openai-and-devin.md
published: 2026-04-28
ingested: 2026-05-05
domains: [coding, agents]
---

# Symphony and Devin for Terminal orchestration

The Code reports two complementary announcements: OpenAI Symphony as an open-source Codex orchestration specification, and Devin for Terminal as a shell-native agent with local codebase and tool access plus cloud handoff. The through-line is issue-tracker and shell-native coding-agent orchestration.

## Key claims extracted

- OpenAI Symphony: described as an open-source specification for orchestrating Codex agents; standardizes how Codex subagents are defined, invoked, and coordinated
- Devin for Terminal: Cognition AI's Devin agent running inside the terminal with local codebase access, local tool access, and the ability to hand off longer-running tasks to Devin's cloud backend
- Issue-queue integration: both products are framed around pulling tasks from issue trackers (GitHub Issues, Linear) as input to agent workflows
- Shell-native orchestration: the terminal is treated as a first-class orchestration surface, not only a fallback from GUI-first tools

## Caveats

- The Code is a secondary newsletter; Symphony spec details and Devin for Terminal feature specifics should be verified against OpenAI and Cognition primary documentation
- Symphony "open-source specification" framing should be checked — it may refer to a standard/schema rather than a full software release

## Influenced pages

- `wiki/tools/codex.md` — Symphony orchestration spec
- `wiki/state-of/coding.md` — issue-queue and terminal orchestration patterns
