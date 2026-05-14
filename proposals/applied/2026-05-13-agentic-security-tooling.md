---
type: proposal
sources:
  - raw/newsletters/2026-05-05-bold-claim-by-anthropics-co-founder.md
  - raw/newsletters/2026-05-04-openai-made-coding-fun-again.md
  - raw/newsletters/2026-05-04-ainews-the-other-vs-the-utility.md
  - raw/newsletters/2026-04-26-codex-moves-beyond-coding.md
status: pending
created: 2026-05-13
---

# Proposal: Agentic security tooling category

## Summary

Claude Security, Vercel DeepSec, Codex security plugins, and agent-run vulnerability monitoring appear as a recurring category. The useful update is that security tooling is being redesigned for agent-built and agent-operated software, not only for human security teams.

## Intended changes

- [x] **Update** `wiki/state-of/cybersecurity.md` — add Vercel DeepSec and agent-run monitoring as caveated secondary signals
    > Add under `AI-assisted vulnerability detection`: `- **Vercel DeepSec** — secondary May 2026 coverage describes security scanning/review for agent-built applications; pending primary verification *(as of 2026-05-04)*`
    >
    > Add a note: `The category is shifting from one-off scanners toward agent-compatible security loops: vulnerability monitoring, fix validation, supply-chain checks, and deployment-risk review inside coding-agent workflows.`

- [x] **Update** `wiki/training/evals-for-agentic-software-development.md` — add security eval loop
    > Add: `Security checks should be treated as agent eval gates where possible: dependency freshness, known vulnerability scans, secret scans, supply-chain policy checks, and post-fix validation should produce artifacts the agent and reviewer can inspect.`

- [x] **Create** `wiki/sources/newsletters/agentic-security-tooling-2026-05-13.md`
    > See draft below

## Page drafts

### wiki/sources/newsletters/agentic-security-tooling-2026-05-13.md (new)

```markdown
---
title: Agentic security tooling category — May 2026
type: source
source_type: newsletter
source_file: raw/newsletters/2026-05-05-bold-claim-by-anthropics-co-founder.md
published: 2026-05-05
ingested: 2026-05-13
domains: [cybersecurity, coding, agents]
---

# Agentic security tooling category — May 2026

May 2026 coverage mentions Claude Security, Vercel DeepSec, Codex security plugins, and workflows for agent-run vulnerability monitoring. The broader signal is that security tooling is being adapted for software that agents build, modify, and operate.

## Influenced pages

- [State of Cybersecurity](../../state-of/cybersecurity.md)
- [Evals for agentic software development](../../training/evals-for-agentic-software-development.md)

## Key claims extracted

- AI security tooling is becoming a recurring product category.
- The category includes scanners, review agents, vulnerability monitoring, and fix validation.
- Primary verification is needed for individual vendor features named in secondary newsletter coverage.
```

