---
type: proposal
sources:
  - raw/newsletters/2026-06-12-ainews-loopcraft-the-art-of-stacking-loops.md
  - raw/newsletters/2026-06-16-we-built-our-own-agent-native-tool-it-overhauled.md
  - raw/newsletters/2026-06-16-ainews-satya-on-loopcraft-building-frontier-eco.md
  - raw/newsletters/2026-06-12-the-moral-of-fable.md
status: pending
created: 2026-06-17
---

# Proposal: Loopcraft / agent-native architecture

## Summary

Three converging sources this week crystallized a clear paradigm shift: the unit of work for AI is a *loop*, not a prompt. Satya Nadella's 60M-view essay on "frontier ecosystems" (loop that compounds human + token capital), AINews naming this "Loopcraft," and a detailed Hoop case study (Stella Garber/Every) of building an agent-native tool with Claude API + Slack — all point the same direction. Key insight: give the model tools + let it reason; don't hardcode prompt sequences; bring the tool where people work.

## Intended changes

- [x] **Update** `wiki/training/ai-native-product-building.md` — add Hoop case study and loop-first principle as the concrete agent-native build pattern
- [x] **Update** `wiki/workflows/agentic-orchestration-patterns.md` — add "loop-first design" as a named pattern; add Satya/Loopcraft framing
- [x] **Create** `wiki/sources/newsletters/loopcraft-june-2026.md` — source summary

## Page drafts

### wiki/training/ai-native-product-building.md (updated sections)

> **Frontmatter: update `as_of` to 2026-06-16; add `loopcraft-june-2026` to sources.**

> **Current guidance — add bullets:**

> **After:**
```
- Agent-native product management workflows increasingly look like commandable rituals: ...
```
> **Add:**
```
- Design loops, not prompts. The unit of work is a loop that prompts your agent, not a prompt you craft once. Your job becomes the loop design: what success condition triggers the next step? (Steipete/AINews, June 2026)
- Give the model tools and let it reason; don't hardcode sequences. "If you give a reasoning model simple, powerful tools, it can handle situations you never thought to code for." (Stella Garber/Hoop, Every June 2026)
- Bring the tool where people already work (Slack, email, existing apps) rather than building a new surface people have to learn.
- Treat "frontier ecosystem, not just frontier model" as the guiding architecture goal: build a learning loop where human capital and token capital compound over time (Satya Nadella, June 2026).
```

> **Proven patterns — add new pattern:**

> **After the last bullet in Proven patterns:**
```
- **Loop-first design.** Before writing a single prompt, define what a successful loop looks like: the trigger, the goal condition, the tool set, and the escalation points. A well-designed loop handles variance you never predicted; a one-shot prompt just handles the case you thought of.
```

> **Add new Evidence from practice section (or append to existing if it exists):**

```markdown
## Evidence from practice

- **Hoop / Stella Garber (Every, June 2026):** Built an agent-native customer discovery tool for Hoop in under 10 hours using Claude API + Slack. Stack: Next.js, ShadCN, Supabase, Claude API. Core design decisions: tools were simple (send message, fetch data, write note), model reasoned about which tool to use, Slack was the interface because that's where users already were. Key finding: the agent handled support scenarios the team had never explicitly thought to code for — entirely because the tool set was clear and the model was given space to reason. The team deviated from agent-native only for operations that were genuinely simpler as traditional code.
- **Satya Nadella essay (June 2026, 60M+ views):** "The real opportunity isn't picking the best model. It's building a learning loop where human capital and token capital compound." This shifts the framing from model selection to loop design as the primary product architecture decision.
```

> **Add to ## Sources:**
```
- [Loopcraft and agent-native architecture — June 2026 digest](../sources/newsletters/loopcraft-june-2026.md)
```

### wiki/workflows/agentic-orchestration-patterns.md (updated section)

> **Frontmatter: update `as_of` to 2026-06-16; add `loopcraft-june-2026` to sources.**

> **Current patterns — add new patterns (append to the list):**

```markdown
- **Loop-first design.** Before writing a single prompt, define what a successful loop looks like: trigger → goal condition → tool set → escalation. The loop is the unit of work, not the prompt. A well-designed loop handles variance you never predicted; a prompt just handles the case you imagined. *Source: Steipete/AINews, Satya Nadella essay, Hoop case study (June 2026)*
- **Tool set clarity over prompt complexity.** Give the model a small set of clear, powerful tools and let it reason about which to use. Don't hardcode which tool gets called at each step. "If you give a reasoning model simple, powerful tools, it can handle situations you never thought to code for." More sophisticated prompt sequencing cannot substitute for a clean tool set. *Source: Stella Garber/Hoop, Every (June 2026)*
- **Deploy where the user already works.** The fastest path to agent adoption is integrating into the existing workflow surface (Slack, email, existing dashboards) rather than requiring users to learn a new app. The agent becomes a service within the existing context, not a parallel system to context-switch into. *Source: Hoop/Stella Garber case study, Every (June 2026)*
```

> **Add to ## Where these patterns surfaced:**
```
- Every's Hoop case study (June 2026): Stella Garber built an agent-native product in under 10 hours using simple Claude API + Slack integration; the key insight was tool clarity over prompt complexity — the agent found solutions the team hadn't thought to code for.
- Satya Nadella's June 2026 X essay (60M views) frames the loop as the primary product: build a learning loop where human capital and token capital compound, not just pick the best model.
- AINews coined "Loopcraft" (June 2026) to name the paradigm: designing loops that prompt agents rather than prompting agents directly.
```

> **Add to ## Sources:**
```
- [Loopcraft and agent-native architecture — June 2026 digest](../sources/newsletters/loopcraft-june-2026.md)
```

### wiki/sources/newsletters/loopcraft-june-2026.md (new)

````md
---
title: Loopcraft and agent-native architecture (June 2026)
type: source
source_type: newsletter
source_file: raw/newsletters/2026-06-16-we-built-our-own-agent-native-tool-it-overhauled.md
published: 2026-06-16
ingested: 2026-06-17
domains: [agents, coding]
---

# Loopcraft and agent-native architecture (June 2026)

Three converging sources crystallized a design paradigm: the right unit of AI work is a loop, not a prompt. AINews named this "Loopcraft"; Satya Nadella's 60M-view essay framed it as "frontier ecosystem over frontier model"; Every's Hoop case study provided a concrete build example.

## Influenced pages

- [AI-native product building](../../training/ai-native-product-building.md) — Hoop case study, loop-first principle
- [Agentic orchestration patterns](../../workflows/agentic-orchestration-patterns.md) — loop-first, tool clarity, deploy-where-users-work patterns

## Key claims extracted

- "You shouldn't be prompting coding agents anymore. You should be designing loops that prompt your agents." (Steipete)
- Satya Nadella essay: "frontier ecosystem, not just frontier model" — build a learning loop where human capital + token capital compound
- Hoop (Stella Garber) built agent-native customer discovery tool in <10 hours with Claude API + Slack; handled unanticipated scenarios because tools were clear and model was allowed to reason
- Core stack: Next.js, ShadCN, Supabase, Claude API; Slack as the interface surface
- Key quote: "If you give a reasoning model simple, powerful tools, it can handle situations you never thought to code for"
- Deviated from agent-native only for operations that were genuinely simpler as traditional code
````
