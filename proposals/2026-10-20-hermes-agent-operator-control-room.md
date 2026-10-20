---
type: proposal
source: raw/tweets/2026-05-18-shannholmberg-2055335043904492011.md
triage: proposals/triage/2026-10-19-raw-orphans-sweep.md
status: pending
created: 2026-10-20
---

# Proposal: "How to Become a Hermes Agent Operator" — Shann Holmberg

## Summary

### In short
Running a team of persistent agents is mostly an operations problem, and the fix is a documented control room kept apart from the agents' live state: Shann Holmberg runs a one-person marketing operation on Hermes Agent from a docs-only folder on one VPS that lists every agent, its credentials and its runbook, while each agent's memory, skills and secrets live in its own container. The proposal adds an "Operating a Hermes fleet" section to the Hermes Agent page and a source page. One reason to hesitate: the article is from May 2026, older than the page's current status, so it adds a practice section rather than status.

[[#Open questions|Open questions: 1 to answer.]]

- [ ] **Approve all** — checking this box approves every item in `## Intended changes` and `## Schema / vocabulary additions` below; the individual boxes may stay empty.

### The source
Shann Holmberg, an AI marketer rather than a developer, published this long X Article on 18 May 2026 after a few weeks of running his marketing work on Hermes Agent, Nous Research's open-source persistent agent. Each agent is a folder: a brain (`MEMORY.md` for business facts and `USER.md` for facts about the user, injected at session start), a personality file (`SOUL.md`), and a skills library the agent grows itself. His fleet of specialists (SEO, outbound, content, a routing-only orchestrator) runs as separate Docker containers on one VPS.

The core of the piece is the "agent control room": a folder of docs, rules, runbooks and an environment map that governs the fleet and holds no raw secrets, kept apart from each agent's live runtime (secrets, memory, skills, sessions, cron jobs). In his words, you can rebuild the body from the brain but not the brain from the body. He sets out four levels: one agent; specialists you talk to directly; an orchestrator as an optional front door that reads the control room; and cron-scheduled work. A new agent is warranted only for its own credentials, its own long-term memory, or a separate recurring role. New workflows are grown, not written: run them two or three times on real work so the agent writes the skill, then deploy once they survive a week unattended. His caveats: the defaults feel heavy if you want explicit control, and the upper levels have a real learning curve.

### What changes
The Hermes Agent page covers releases and architecture but not how a practitioner runs a fleet.

- **Hermes Agent** gains an "Operating a Hermes fleet" section after "Key orchestration patterns", plus one Recent-changes entry dated 18 May in date order (7 entries, no spill). Page date stays 1 September.
- New source page for the article.

### What to weigh
The article is five months older than the page's newest claims, so its figures (150,000 stars, 123 skills) are stated as of May and its superseded model picks are left out.

## Intended changes

- [ ] **Update** `wiki/tools/hermes-agent.md` — insert a new `## Operating a Hermes fleet` section between `## Key orchestration patterns` and `## Compared to OpenClaw`; adds one Recent-changes entry dated 2026-05-18 between the 2026-08-29 and 2026-05-13 entries (live list has 6, no spill); append source id and link; `as_of` stays 2026-09-01
    > See draft below

- [ ] **Create** `wiki/sources/tweets/shannholmberg-hermes-agent-operator-2026-05-18.md` — source summary

## Page drafts

### wiki/tools/hermes-agent.md (updated)

Frontmatter `sources:` (append one id; `as_of` unchanged):

```
sources: [ainews-2026-04-21, ainews-2026-04-22, hermes-openclaw-persistent-agents-2026-05-11, ainews-openai-agi-bar-2026-08-28, ainews-fal-h3-max-live-2026-09-01, shannholmberg-hermes-agent-operator-2026-05-18]
```

New section, inserted between `## Key orchestration patterns` and `## Compared to OpenClaw`:

```
## Operating a Hermes fleet

A practitioner setup from Shann Holmberg, who ran a one-person marketing operation on Hermes in May 2026 (when Hermes had about 150K GitHub stars and 123 bundled skills):

- **Agent anatomy.** Each agent is a folder: `MEMORY.md` (stable business facts) and `USER.md` (stable facts about the user) are injected at session start, past sessions sit in a full-text-searchable SQLite store, `SOUL.md` sets the personality, and the skills library grows as the agent writes skills from real work. Several agents can share one brain with different souls.
- **Control room apart from runtime.** A docs-only folder governs the fleet: which agents exist, what each may and may not do, ports, which credentials each references, runbooks, and backups, with no raw secrets. Each agent's live runtime (secrets, memory, skills, sessions, cron jobs) lives in its own container. "You can rebuild the body from the brain. You cannot rebuild the brain from the body."
- **Four levels.** One agent; several specialists you talk to directly; an orchestrator as an optional front door that reads the control room to learn what exists and what needs approval, with a task bus to the specialists; then cron-scheduled work (weekly reports, health checks, backup checks). Prove the specialists before adding an orchestrator.
- **When to add an agent.** Only when the work needs its own credentials, its own long-term memory, or is a separate recurring role. One mega-agent holding every credential and memory loses isolation and clean revocation.
- **Grow workflows, don't write them.** Run a new workflow two or three times on real work so the agent writes the skill, tighten it in a separate workspace, and deploy it on a schedule once it survives a week unattended. Keep a sequential pipeline (his 21-step SEO flow) in one container so later steps keep what earlier steps decided.
```

`## Recent changes` — insert one entry between the 2026-08-29 and 2026-05-13 entries:

```
- [2026-05-18] Practitioner fleet setup (Shann Holmberg): agent control room kept apart from each agent's runtime, four setup levels, new-agent test, prototype-to-production path.
```

`## Sources` — append:

```
- [Shann Holmberg on X — How to Become a Hermes Agent Operator](../sources/tweets/shannholmberg-hermes-agent-operator-2026-05-18.md)
```

### wiki/sources/tweets/shannholmberg-hermes-agent-operator-2026-05-18.md (new)

```
---
title: 'Shann Holmberg on X — "How to Become a Hermes Agent Operator"'
type: source
source_type: tweet
source_file: raw/tweets/2026-05-18-shannholmberg-2055335043904492011.md
url: https://x.com/shannholmberg/status/2055335043904492011
published: 2026-05-18
ingested: 2026-10-20
domains: [agents]
---

# Shann Holmberg on X — "How to Become a Hermes Agent Operator"

Long X Article by Shann Holmberg, an AI marketer, on how he runs his marketing operation on Hermes Agent: the anatomy of a Hermes agent (memory files, soul, self-written skills), his fleet of specialist agents in Docker containers on one VPS, the "agent control room" folder that governs the fleet, four levels of setup from one agent to a scheduled, orchestrated team, a prototype-to-production method for new workflows, and honest trade-offs. He links a public control-room template whose skills let Claude Code or Codex provision the VPS and register the first agent.

## Influenced pages

- [Hermes Agent](../../tools/hermes-agent.md) — "Operating a Hermes fleet" section

## Key claims extracted

- As of May 2026: ~150K GitHub stars, 123 bundled skills, 70+ gateway tools, 300+ models through one subscription, six deployment targets (local, Docker, SSH, Daytona, Singularity, Modal), 20+ messaging surfaces, #1 on OpenRouter for token usage
- Memory at `~/.hermes/memories/`: `MEMORY.md` and `USER.md` injected at session start; sessions in SQLite with full-text recall; `SOUL.md` sets personality
- Closed learning loop: the agent writes new skills as it works; advice is to let it write skills from real work rather than writing them on day one
- Hermes vs OpenClaw framed as "Rails vs Linux": opinionated defaults vs explicit primitives
- Fleet: personal assistant, SEO, outbound, design review, content, a company-brain agent over Slack/email/transcripts, and a routing-only orchestrator, each in its own container
- SEO agent: 21 steps in three phases (research, production, distribution) in one container because the work is sequential
- Control room (`/root/vps-agents`): docs, rules, runbooks, env-map, registry, no raw secrets; live runtime per agent at `/srv/<agent>/data` (secrets, memory, skills, sessions, cron)
- Three paths: control path (manage the fleet), direct path (talk to a specialist), orchestrated path (orchestrator → task bus → specialists)
- Four levels: one agent; direct specialists; orchestrator front door; scheduled automation
- New agent only for its own credentials, its own long-term memory, or a separate recurring role
- Prototype → run 2–3 times on real work → fine-tune in a dedicated workspace → deploy on a VPS schedule after a week unattended
- Trade-offs: defaults feel heavy for explicit-control users; levels 3–4 have a learning curve; the framework does not make a small model a strategist
```

## Open questions

- The control-room pattern (a docs-only governance folder that an orchestrator reads, kept apart from agents' secrets and state) is tool-agnostic. Should it also become a short bullet on Multi-agent coordination, or stay on the Hermes page until a second source describes it (assumed: stay)?
