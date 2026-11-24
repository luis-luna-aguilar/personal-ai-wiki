---
title: Cognition — Bringing Devin Cloud to your terminal
type: source
source_type: article
source_file: raw/articles/2026-10-20-devinai-blog-devin-cloud-in-your-terminal.md
url: https://devin.ai/blog/devin-cloud-in-your-terminal
published: 2026-09-21
ingested: 2026-10-20
domains: [coding, agents]
---

# Cognition — Bringing Devin Cloud to your terminal

Cognition's launch post for running and steering Devin Cloud sessions from the Devin CLI, with two-way handoff between local and cloud work and SSH access to the agent's VM.

## Influenced pages

- [Devin](../../tools/devin.md) — new "Devin Cloud in the terminal" subsection
- [Agent runtime platforms](../../concepts/agent-runtime-platforms.md) — cloud-resident agents

## Key claims extracted

- `devin --cloud` or `/cloud` creates, steers, resumes and watches cloud sessions; sessions outlive the terminal
- `/handoff` sends a local task to Devin's cloud VM; in a cloud session it brings the PR branch back to a local checkout and local session
- `/open web|desktop` and `devin --cloud --resume <url>` move between views
- `devin ssh` connects to the agent's VM (edit code, forward ports, scp)
- Free SWE-2 sessions until 8 October
