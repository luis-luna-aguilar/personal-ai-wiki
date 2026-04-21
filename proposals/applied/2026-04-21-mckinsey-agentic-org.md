---
type: proposal
sources:
  - raw/articles/2026-04-21-mckinseycom-ai-is-everywhere-the-agentic-organization-isnt-yet.md
  - raw/tweets/2026-04-21-xcom-polak_jasperstatus204621102772-2.md
status: pending
created: 2026-04-21
---

# Proposal: McKinsey — "AI is Everywhere. The Agentic Organization Isn't Yet."

## Summary

McKinsey Senior Partner Alexis Krivkovich: 80%+ of companies aren't seeing bottom-line ROI from AI investments. The blocker isn't technology — it's that work processes haven't been redesigned around agents. The article introduces a meaningful distinction between "humans in the loop" (agents do parts of a workflow, humans do other parts) vs. "humans above the loop" (agents do the whole workflow, humans provide judgment on top). Also introduces end-to-end workflow reimagination as the unit of value capture, a specific illustration from the American Arbitration Association, and a 75%-of-roles-need-reshaping stat.

## Intended changes

- [x] **Create** `wiki/sources/articles/mckinsey-agentic-org.md` — source summary
    > See draft below

- [x] **Update** `wiki/training/company-wide-ai-enablement.md` — significant additions across multiple sections; bump `as_of`
    > See full updated page draft below

- [x] **Update** `wiki/trends/agents-reshape-organizations.md` — add McKinsey signals to Concrete signals, strengthen the structural argument, add "humans above the loop" to What to watch; bump `as_of`
    > See diff below

## Diffs and drafts

### wiki/training/company-wide-ai-enablement.md (updated — full draft)

The page absorbs enough new material that showing a full updated version is clearer than a snippet diff.

````md
---
title: Company-wide AI enablement
type: training
as_of: 2026-04-21
sources: [ramp-ai-adoption-playbook, mckinsey-agentic-org]
---

# Company-wide AI enablement

Company-wide AI enablement is the practical problem of getting a broad organization — not just engineers — to use AI tools productively. The recurring lesson: adoption is driven less by formal curriculum and more by operating design. But adoption alone is not the goal. More than 80% of companies report AI investments are not yet showing bottom-line impact (McKinsey, 2026). The next step is redesigning work *around* agents, not just putting agents into existing workflows.

## Current guidance

- Start with a clear expectation from leadership that AI use is part of how work gets done
- Lower the activation barrier with one preconfigured agent surface, SSO, and preconnected workplace tools
- Pair a small central platform team with distributed builders in each function
- Make usage and wins visible through demos, shared channels, office hours, and public examples
- Move from point solutions to end-to-end workflow reimagination — the step change in value comes from rethinking an entire process (e.g., insurance underwriting, hire-to-onboard), not from speeding up individual tasks
- Raise performance expectations only as the tooling becomes good enough to support them

## Proven patterns

- **Platform plus spokes.** A central team owns connectors, platforms, skills, and enablement; functional teams build domain workflows on top
- **Product-led teaching.** The first real result matters more than formal training; the tool should teach through immediate usefulness
- **Shared workflow marketplace.** Internal skills or templates let one person's discovery become everyone else's shortcut
- **Visible adoption loops.** Leaderboards, all-hands demos, and team channels turn private experimentation into contagious behavior
- **Exploration budget.** Removing token caps and access restrictions gives people room to discover high-leverage use cases before ROI is obvious
- **End-to-end workflow ownership.** Best use cases cut across multiple teams; redesigning the whole workflow (who owns what, where humans stay in vs. above the loop) beats optimizing individual steps
- **Cross-level redesign teams.** Process reimagination needs both leaders who can identify lighthouse use cases and employees deep in the day-to-day work — not just one or the other

## Failure modes

- Treating AI as a procurement exercise with slow approvals, connector queues, and restrictive access
- Raising expectations before the tools are reliable or easy enough for non-experts
- Centralizing all building work into one overloaded team, or fully decentralizing and accepting redundant re-learning
- Overinvesting in workshops while underinvesting in defaults, tooling, and social proof
- **Running AI pilots inside unchanged processes.** Individual adoption without redesigning the surrounding workflow keeps the organization stuck in pilot mode — one analyst using Claude inside an otherwise unchanged 75-person firm. McKinsey's framing: the blocker is work redesign, not technology
- **Point solutions masquerading as transformation.** Taking one task and using AI to do it faster is not the same as reimagining the workflow end-to-end

## Humans in the loop vs. above the loop

A useful distinction for planning workflow redesign:

- **In the loop**: agents do parts of the process, then hand off to a human who does other parts. The human is a step in the workflow.
- **Above the loop**: agents do most or all of the core process; the human's role is judgment on top — reviewing the output, making the call, catching edge cases. The human supervises the workflow.

Both will coexist. "Above the loop" represents the higher-value state for most knowledge work: not eliminating human judgment, but elevating what humans are doing to where judgment actually matters.

**Illustration (American Arbitration Association):** Agents trained on closed case files to build timelines, review fact bases, examine both sides of an argument, and produce summary decisions — in some cases doing it better than the traditional manual process. A human reviews and approves. The judgment layer remains critical, but the execution work is done end-to-end by agents.

## Evidence from practice

- Ramp: AI usage up 6,300% YoY; 99.5% of employees active on AI tools; 84% using coding agents weekly; 1,500+ apps shipped in six weeks by 800+ builders; non-engineers account for 12% of human-initiated PRs
- Ramp attributes adoption to a preconfigured internal agent (`Glass`), a shared skills marketplace (`Dojo`), and visible social reinforcement
- McKinsey (2026): 80%+ of companies say they're not yet seeing bottom-line impact from AI investments despite massive investment
- McKinsey: 75% of roles need fundamental reshaping right now; nearly half of leaders report skill gaps in their organization

## The junior talent problem

Agentic AI is removing the "grunt work" through which junior employees historically built pattern recognition. If entry-level work disappears entirely, there's a pipeline problem: senior talent runs out within a decade. McKinsey's framing: learning and development should move from a periodic sidecar to the center of the employee journey. Junior employees who start with AI tools from day one don't have 20 years of pattern recognition — but they also don't face the hurdle of disrupting an established career-long workflow.

## Open questions

- Which parts of the Ramp/McKinsey playbook generalize outside high-velocity tech companies with strong internal engineering capacity?
- When does "above the loop" become viable for a given workflow? What's the minimum agent reliability threshold before removing humans from execution entirely?
- How do you evaluate and develop junior employees when the output-producing work is done by agents?
- What is the minimum viable internal platform needed before this pattern works outside companies that can build their own agent layer?

## Sources

- [[sources/articles/ramp-ai-adoption-playbook]]
- [[sources/articles/mckinsey-agentic-org]]
````

### wiki/trends/agents-reshape-organizations.md (diff)

**Add to `## Concrete signals` (new bullet):**

```
- **McKinsey names the bottleneck: workflow redesign, not technology.** "AI is Everywhere. The Agentic Organization Isn't Yet" (McKinsey, 2026) reports that 80%+ of companies are not seeing bottom-line impact from AI investments despite large spending. The diagnosis: companies are running pilots inside unchanged processes rather than redesigning workflows end-to-end. The unlock is "end-to-end workflow reimagination" — rethinking the entire process (e.g., insurance underwriting, hire-to-onboard) rather than speeding up individual tasks. McKinsey introduces the distinction between humans "in the loop" (executing parts of a workflow) vs. "above the loop" (providing judgment over an agent-run process) as the structural end state for knowledge work.
```

**Update `## What to watch` (add bullet):**
```
- Whether "humans above the loop" becomes the dominant framing for redesigned knowledge-work processes — and which functions get there first
```

**Add to `## Recent changes` (prepend):**
```
- [2026-04-21] Added McKinsey (2026) as the strongest third-party signal yet: 80%+ no bottom-line ROI, workflow redesign named as the blocker, "above the loop" distinction introduced
```

**Frontmatter:** add `mckinsey-agentic-org` to `sources:`, update `as_of: 2026-04-21`

## Page drafts

### wiki/sources/articles/mckinsey-agentic-org.md (new)

````md
---
title: McKinsey — "AI is Everywhere. The Agentic Organization Isn't Yet."
type: source
source_type: article
source_file: raw/articles/2026-04-21-mckinseycom-ai-is-everywhere-the-agentic-organization-isnt-yet.md
url: https://www.mckinsey.com/capabilities/people-and-organizational-performance/our-insights/ai-is-everywhere-the-agentic-organization-isnt-yet
published: 2026-04
ingested: 2026-04-21
domains: [agents]
---

# McKinsey — "AI is Everywhere. The Agentic Organization Isn't Yet."

McKinsey Podcast transcript with Senior Partner Alexis Krivkovich. Argues that companies are stuck in AI pilot mode not because technology isn't ready, but because underlying work processes haven't changed. Introduces "humans above the loop" as the structural end state for knowledge work and end-to-end workflow reimagination as the unit of value capture.

## Key claims extracted

- 80%+ of companies not yet seeing bottom-line impact from AI investments (McKinsey research)
- 75% of roles need fundamental reshaping right now
- Nearly half of leaders see skill gaps; most want more training through senior leadership
- The blocker is work redesign, not technology — individual adoption inside unchanged processes = pilot mode
- **Humans in the loop vs. above the loop**: key operational distinction for workflow design
- Best use cases are end-to-end workflow reimagination (insurance underwriting, hire-to-onboard), not point solutions
- American Arbitration Association example: agents trained on case files to produce summary decisions; human provides final judgment
- Management layers may flatten as AI enables wider spans of control
- Rising skills: strategic thinking, systems orientation, judgment, oversight; AI handles research, math, data science execution
- Change management is no longer episodic — perpetual state

## Influenced pages

- [[training/company-wide-ai-enablement]] — major additions: pilot mode failure mode, above-the-loop distinction, McKinsey evidence, junior talent problem
- [[trends/agents-reshape-organizations]] — McKinsey as strongest third-party signal for org redesign thesis
````
