---
title: Test backlog
type: personal
as_of: 2026-04-10
---

# Test backlog

Things to try or delegate to the team. Linked to wiki pages for context.

## [ ] Cursor cloud agents with PR demo attachments

Cursor's cloud agents can run a task end-to-end and auto-attach a demo video + screenshots to the GitHub PR they open. Teams can review AI-generated work visually without leaving GitHub.

**Why test:** This is a compelling code review workflow for agent-generated PRs. Worth seeing if it fits our review process.

**How:** Kick off a cloud agent task in Cursor, let it open a PR, check if the demo attachment appears in GitHub.

See: [[tools/cursor]]

## [ ] Claude Code Monitor tool in a real project

Run a dev session where Claude Code monitors a dev server or test suite in the background while working on something else.

**Why test:** Token savings + less manual checking during long agent runs.

See: [[tools/claude-code]]

## [ ] Let non-technical customers open PRs in our projects

Ramp reports that non-engineers account for a meaningful share of production-code PRs via internal coding agents. We should explore enabling our customers to open PRs in our projects even when they are not technical.

**Why test:** This could materially widen who can propose product and workflow changes, and shorten the loop from customer need to actionable code.

**How:** Define a safe PR path with strong defaults, scoped permissions, review gates, and agent support so non-technical users can propose changes without needing local setup or engineering fluency.

See: [[training/company-wide-ai-enablement]]
