---
type: proposal
source: raw/newsletters/2026-05-15-you-can-now-access-codex-on-phone.md
status: pending
created: 2026-05-18
---

# Proposal: Agentic coding "trap" — skill atrophy and the supervision paradox

## Summary

Lars Faye's viral essay "Agentic Coding is a Trap" (topped Hacker News) argues that the orchestration model — human plans, AI builds — erodes the exact coding skills needed to supervise AI effectively. Anthropic cited a 47% drop in debugging ability among engineers using AI heavily. Django co-creator Simon Willison admits he no longer has a clear mental map of apps he builds with agents. Faye's position is nuanced: he uses LLMs for specs and ad-hoc tasks, but opposes handing over implementation. Counter-data: Airbnb ships 64% of production PRs with agents using a 15-minute playbook.

## Intended changes

- [x] **Update** `wiki/training/ai-enablement-software-development.md` — add supervision paradox / skill atrophy as a named failure mode; add Faye essay and Airbnb counter-evidence to Evidence from practice; update `as_of` and sources
    > **as_of:** `2026-05-13` → `2026-05-15`
    >
    > **Add to Failure modes section:**
    > ```markdown
    > - **Skill atrophy through orchestration delegation.** Handing the implementation entirely to agents erodes the coding skills needed to supervise AI effectively — a "supervision paradox." Anthropic's own internal study found a 47% drop in debugging ability among engineers using AI heavily. Simon Willison (Django co-creator): no longer has a clear mental map of apps he builds with agents. Lars Faye's "Agentic Coding is a Trap" (Hacker News #1, May 2026): the orchestration model works until it collapses because the human has lost enough fluency to catch agent errors early. The fix is not abandoning AI, but being selective: LLMs for specs, drafts, and ad-hoc tasks; human-written implementation for core complexity. Faye uses LLMs himself — he opposes full implementation hand-off specifically.
    > ```
    >
    > **Add to Evidence from practice:**
    > ```markdown
    > - Lars Faye (May 2026, viral essay): "Agentic Coding is a Trap" — 47% debugging ability drop (Anthropic internal study); Willison's "no mental map" confirmation; Faye's prescription: keep implementation, use AI for specs and ad-hoc tasks
    > - Airbnb counter-pattern (May 2026): 64% of production PRs shipped with agents using a 15-minute playbook — high AI adoption without the orchestration-only model Faye critiques
    > ```
    >
    > **Add to sources list:** `agentic-coding-trap-may-2026`

- [x] **Create** `wiki/sources/newsletters/agentic-coding-trap-may-2026.md` — source summary

## Page drafts

### wiki/sources/newsletters/agentic-coding-trap-may-2026.md (new)

```markdown
---
title: "Agentic Coding is a Trap — Lars Faye essay (May 2026)"
type: source
source_type: newsletter
source_file: raw/newsletters/2026-05-15-you-can-now-access-codex-on-phone.md
published: 2026-05-15
ingested: 2026-05-18
domains: [coding]
---

# Agentic Coding is a Trap — Lars Faye essay (May 2026)

The Code newsletter covered Lars Faye's Hacker News #1 essay arguing that the "human plans, AI builds" orchestration model creates a supervision paradox: it erodes the exact coding skills needed to supervise AI output. Evidence: Anthropic's internal 47% debugging ability drop, Willison's "no mental map" admission. Counter-data: Airbnb's 64% of PRs from agents using a 15-minute playbook — high adoption without full implementation hand-off.

## Influenced pages

- [AI enablement — software development](../../training/ai-enablement-software-development.md) — skill atrophy failure mode added; evidence updated

## Key claims extracted

- Lars Faye essay "Agentic Coding is a Trap": orchestration model collapses because human loses coding fluency over time
- Supervision paradox: need coding skills to supervise AI, but heavy AI use erodes those skills
- Anthropic internal study: 47% drop in debugging ability among heavy AI users
- Simon Willison (Django co-creator): "no longer has a clear mental map of the apps he builds using agents"
- Faye uses LLMs for specs and ad-hoc tasks — opposes full implementation hand-off specifically
- Airbnb counter: 64% of production PRs from agents, 15-minute playbook — high-functioning counter-example
- Essay primary URL: https://larsfaye.com/articles/agentic-coding-is-a-trap
```

## Feedback

- I dont agree with the fix, its irresponsible to go slower, the real fix is to carefully study the PRs like other engineering practices study the manuals of machines they purchase. They didn't build them, but they studied this. Developers are used to learn by doing, but that hasn't been the standard in other industries, and its time for us to adapt. Please write an article about this topic in my personal notes, which ill use as a draft for publication. And put in there your opinion on the topic, if you think other engineerings have to relay more on docs than us.