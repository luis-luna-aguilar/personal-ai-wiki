---
type: proposal
sources:
  - raw/newsletters/2026-03-19-minimax-m27-rivals-top-models.md
  - raw/newsletters/2026-03-20-cursor-drops-composer-2.md
  - raw/newsletters/2026-03-23-supermemory-cracks-agent-memory.md
  - raw/tweets/2026-03-23-xcom-mattpocockukstatus203607613292.md
  - raw/tweets/2026-03-23-xcom-emollickstatus2035895233519493.md
status: pending
created: 2026-04-21
---

# Proposal: Skills and plugin packaging in late March

## Summary

The wiki already has the right conceptual direction on harnesses, but this batch adds a more specific late-March signal: the field is converging not only on "better harnesses," but on reusable operating modules as the real abstraction layer. Skills, plugins, hooks, slash commands, and lightweight packaging are becoming how teams distribute judgment, not just how they expose tools.

## Intended changes

- [x] **Update** `wiki/concepts/harness.md` — add the packaging layer more explicitly
  > See snippet below.

- [x] **Update** `wiki/workflows/agentic-orchestration-patterns.md` — add a clearer rule about packaging reusable operating judgment
  > See snippet below.

- [x] **Update** `wiki/state-of/coding.md` — add a `Recent changes` note that this abstraction layer is now solidifying across ecosystems
  > See snippet below.

- [x] **Create** `wiki/sources/newsletters/skills-and-plugin-packaging-late-march.md` — grouped source summary page
  > See full draft below.

## Page drafts

### wiki/concepts/harness.md (updated snippet)

```markdown
## What a harness includes

- **Reusable operating modules** — skills, hook scripts, slash commands, and plugin bundles increasingly act as composable pieces of the harness, not just ad hoc project artifacts

## Why it matters

Late-March sources add a more distribution-oriented layer to this idea: teams do not only want a good harness inside one project. They want reusable packaging for the fuzzy operating judgment that makes the harness good in the first place. That is why plugin marketplaces, skills folders, and installable bundles keep surfacing across coding-agent ecosystems.
```

### wiki/workflows/agentic-orchestration-patterns.md (updated snippet)

```markdown
## Current patterns

- **Package the workflow, not just the tool.** Teams increasingly bundle skills, hooks, MCP wiring, rules, and slash commands into something installable so one person's working agent setup becomes another person's starting point
- **Share skills, not just code.** Reusable skills increasingly package the fuzzy operating judgment that teams want many agents to inherit

## Where these patterns surfaced

- Late-March coding-agent coverage suggests a clear packaging race: marketplaces and skill bundles are becoming the transport layer for agent behavior across teams
- Practitioner commentary also suggests "skill" does not mean the same thing everywhere: some ecosystems package reference-heavy technical instructions, while others package more open-ended problem-solving approaches
```

### wiki/state-of/coding.md (updated snippet)

```markdown
## Recent changes

- [2026-03-23] Late-March signals suggest skills, plugins, hooks, and related packaging are solidifying into the core abstraction layer for coding agents rather than remaining scattered configuration details
```

### wiki/sources/newsletters/skills-and-plugin-packaging-late-march.md (new)

```markdown
---
title: Skills and plugin packaging in late March
type: source
source_type: newsletter
source_file: raw/newsletters/2026-03-20-cursor-drops-composer-2.md
ingested: 2026-04-21
domains: [coding, agents]
---

# Skills and plugin packaging in late March

This source cluster adds a useful refinement to the broader harness story. The field is not only learning that harnesses matter; it is also converging on reusable packaging for the pieces that make a harness work in practice: skills, hooks, MCP setups, slash commands, and installable bundles.

## Influenced pages

- [[concepts/harness]] — adds the packaging/distribution layer more explicitly
- [[workflows/agentic-orchestration-patterns]] — clarifies that teams increasingly package reusable workflow judgment, not only tool access
- [[state-of/coding]] — supports a current-state note that this abstraction layer is solidifying across ecosystems

## Key claims extracted

- Plugin marketplaces are being framed as the missing packaging layer above MCP
- Teams want to distribute skills, hooks, rules, and tool wiring together, not as scattered files
- Viral skill examples suggest reusable workflows can spread as first-class artifacts
- Practitioner commentary suggests "skills" already diverges across ecosystems: some emphasize technical reference/context, others emphasize operating approach
- The durable moat may live in the repeatable workflow packaging and feedback loops around it, not only in raw model quality
```

## Comments

- The sources of this proposal seem wrong, compared with its content