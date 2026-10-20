---
type: proposal
source: raw/newsletters/2026-10-14-crossing-the-threshold-how-openai-and-anthropic-a.md
triage: proposals/triage/2026-10-11-to-2026-10-20-ai-digest.md
status: pending
created: 2026-10-20
---

# Proposal: AIE NYC finance track — where to place agent controls

## Summary

### In short
In regulated finance, safe agent autonomy comes from where controls and human judgment sit, not from how many approvals are stacked up: blanket sign-offs cause "approval fatigue" and add risk. Speakers from OpenAI, Anthropic, Two Sigma and Bloomberg converged on one pattern: classifiers route only consequential calls to people, agents propose changes rather than make them, and deterministic checks, logs and kill switches sit outside the model. The proposal adds a practitioner subsection to Agent autonomy and governance and two product lines to State of Finance. One reason to hesitate: the Bloomberg advice largely repeats Satya Nadella's insider-risk controls, already on the page.

[[#Open questions|Open questions: 1 to answer.]]

### The source
Latent Space's write-up of the finance keynotes at AI Engineer New York, published 14 October 2026, argues one thesis: safe autonomy depends on where you put controls and human judgment, not on how many restrictions you impose. Joseph Kim, who heads ChatGPT for Financial Services at OpenAI, described a "threshold of usefulness", the point where a model is capable and reliable enough to save an analyst time, and predicted that in 2027 agents will handle investment idea generation and trading. He treats traceability (checking where a number came from) as part of the product and frames when a human stays in the loop as a product-design question: what must the user still control, review or approve?

John Feminella, SVP Architecture at the hedge fund Two Sigma, presented five composable controls, each doing one job, that together let agents run with real autonomy. He attacked "approval fatigue": a person asked to approve everything slows the work and stops paying attention. His answer is auto-mode classifiers that settle routine calls and send people only the consequential ones, with deterministic rules for clear-cut cases. Anthropic's Keon Shahab described a three-part "trust layer": an identity and permissions layer saying whom the agent acts as, a sandbox and approval layer so someone signs off before it acts, and checks that the agent still works as variables change. His example is a trade-break investigation agent that proposes order amendments for human approval but never makes them. Bloomberg's Andrey Rybka walked through real agent incidents, including an agent that obeyed instructions hidden in a marketplace review and stocked a product, and argued for "deterministic controls outside the model": scoped credentials, tool-call checks, egress limits, audit trails, budgets and kill switches. The write-up does not list Feminella's five controls individually.

### What changes
The governance page already has an autonomy ladder and Nadella's six external-control principles, but no practitioner account of placing approvals; State of Finance was last updated in July.

- **Agent autonomy and governance** gains a short subsection, "Place controls where they enable autonomy", under Governance patterns: approval fatigue, classifier-versus-rule routing, the propose-not-act boundary, the three-part trust layer, and Bloomberg's external controls, cross-referenced to Nadella's list rather than repeating it. Page date moves to 14 October.
- **State of Finance** gains two Finance AI lines, ChatGPT for Financial Services and Claude for Financial Advisors, plus a Recent-changes entry. Page date moves to 14 October.
- One new source page for the write-up.

### What to weigh
Claude for Financial Advisors is mentioned only in passing (announced "last month"), so its line is thin. The AINews issue the triage cited adds only that the keynotes happened, so it gets no source page here.

## Intended changes

- [ ] **Approve all** — checking this box approves every item in `## Intended changes` and `## Schema / vocabulary additions` below; the individual boxes may stay empty.

- [ ] **Update** `wiki/training/agent-autonomy-and-governance.md` — new `###` subsection under `## Governance patterns`, placed before "Treat the model as an insider risk"; adds one Recent-changes entry dated 2026-10-14 (5 of 10, no spill); merge source; `as_of` 2026-10-11 → 2026-10-14.

- [ ] **Update** `wiki/state-of/finance.md` — two new lines under `### Finance AI`; adds one Recent-changes entry dated 2026-10-14 (7 of 10, no spill); merge source; `as_of` 2026-07-02 → 2026-10-14.

- [ ] **Create** `wiki/sources/newsletters/latent-space-crossing-the-threshold-2026-10-14.md` — source summary.

## Page drafts

### wiki/training/agent-autonomy-and-governance.md (updated)

Frontmatter: `as_of: 2026-10-14`; append `latent-space-crossing-the-threshold-2026-10-14` to `sources:`.

Insert after the last `## Governance patterns` bullet ("Measure at the workflow level…") and before `### Treat the model as an insider risk`:

```
### Place controls where they enable autonomy

Finance practitioners at AI Engineer New York (October 2026) argued that safe autonomy depends on where controls and human judgment sit, not on how many approvals are added.

- **Approval fatigue is a risk, not a safeguard.** A person asked to approve everything slows the work and stops paying attention to the decisions that matter (John Feminella, Two Sigma).
- **Route by case type.** Classifiers settle routine calls and escalate only consequential or ambiguous ones to a person; deterministic rules handle clear-cut cases. Two Sigma runs this as one of five composable controls, each doing one job.
- **Propose, don't act, at the boundary.** Anthropic's trade-break investigation agent proposes order amendments for a human to approve and never writes them itself.
- **Build one trust layer, then deploy many agents.** Anthropic's three parts: identity and permissions (whom the agent acts as), a sandbox and approval layer (who signs off before it acts), and regression checks (does it still work when variables change).
- **Keep enforcement outside the model.** Bloomberg's incident list, including an agent that obeyed instructions hidden in a marketplace review and stocked a product, leads to scoped credentials, tool-call checks, egress limits, audit logs, budgets, and kill switches, plus input validation and provenance tracking. This is the practitioner form of the insider-risk principles below.
- **Treat human-in-the-loop as product design.** OpenAI's Joseph Kim: decide what the user must still control, review, or approve, and build traceability (where each number came from) into the interface.
```

`## Recent changes` — insert after the two 2026-10-19 entries (date order, newest first):

```
- [2026-10-14] Added "Place controls where they enable autonomy" from AIE NYC finance keynotes: approval fatigue, classifier-versus-rule routing (Two Sigma), propose-not-act and a three-part trust layer (Anthropic), deterministic controls outside the model (Bloomberg), HITL as product design (OpenAI).
```

`## Sources` — append:

```
- [Latent Space — Crossing the Threshold: autonomy and safety in financial agents](../sources/newsletters/latent-space-crossing-the-threshold-2026-10-14.md)
```

### wiki/state-of/finance.md (updated)

Frontmatter: `as_of: 2026-10-14`; append `latent-space-crossing-the-threshold-2026-10-14` to `sources:`.

Under `### Finance AI`, append:

```
- **ChatGPT for Financial Services** — OpenAI; builds source traceability (where each number came from) into review; OpenAI's Joseph Kim predicts agents will do investment idea generation and trading in 2027 *(as of 2026-10-14)*
- **Claude for Financial Advisors** — Anthropic; announced September 2026; advisors connect their own systems to Claude plus a set of workflow skills; Anthropic pairs it with an identity, approval, and regression "trust layer" for financial agents *(as of 2026-10-14)*
```

`## Recent changes` — insert at top:

```
- [2026-10-14] AIE NYC finance keynotes: OpenAI (ChatGPT for Financial Services), Anthropic (Claude for Financial Advisors), Two Sigma, and Bloomberg converge on placing controls (classifier routing, propose-not-act, deterministic checks outside the model) rather than stacking approvals; guidance on [Agent autonomy and governance](../training/agent-autonomy-and-governance.md).
```

`## Sources` — append:

```
- [Latent Space — Crossing the Threshold: autonomy and safety in financial agents](../sources/newsletters/latent-space-crossing-the-threshold-2026-10-14.md)
```

### wiki/sources/newsletters/latent-space-crossing-the-threshold-2026-10-14.md (new)

```
---
title: "Latent Space — Crossing the Threshold: How OpenAI and Anthropic Approach Autonomy and Safety in Financial Agents"
type: source
source_type: newsletter
source_file: raw/newsletters/2026-10-14-crossing-the-threshold-how-openai-and-anthropic-a.md
url: https://www.latent.space/p/crossing-the-threshold
published: 2026-10-14
ingested: 2026-10-20
domains: [finance, agents]
---

# Latent Space — Crossing the Threshold: autonomy and safety in financial agents

Write-up of the AI Engineer New York finance keynotes from OpenAI, Two Sigma, Anthropic, and Bloomberg. Central thesis: safe agent autonomy depends on where controls and human judgment are placed, not on how many restrictions are imposed.

## Influenced pages

- [Agent autonomy and governance](../../training/agent-autonomy-and-governance.md) — "Place controls where they enable autonomy" subsection
- [State of Finance](../../state-of/finance.md) — ChatGPT for Financial Services and Claude for Financial Advisors lines

## Key claims extracted

- OpenAI (Joseph Kim, Head of ChatGPT for Financial Services): "threshold of usefulness" where a model becomes reliable enough to save time; predicts 2027 agents doing investment idea generation and trading and less reliance on Excel/PowerPoint; traceability built into review; HITL is a product-design question
- Two Sigma (John Feminella, SVP Architecture): five composable controls; "approval fatigue" holds back innovation and adds risk; auto-mode classifiers handle routine calls and escalate important ones; deterministic rules for clear cases; "brakes let you go fast and stop safely"
- Anthropic (Belinda Neal, Keon Shahab): Claude for Financial Advisors announced the prior month; trust layer = identity/permissions, sandbox plus approval layer, stability as variables change; trade-break agent proposes order amendments, never makes them
- Bloomberg (Andrey Rybka): real agent incidents, including prompt injection via a marketplace review that led an agent to stock a product; defenses: scoped identities and credentials, tool-call controls, outbound traffic limits, audit trails, budgets, kill switches, input validation, provenance tracking, human approval for high-value actions; "deterministic controls outside the model"
```

## Schema / vocabulary additions

None.

## Open questions

- Should the Bloomberg bullet be folded into the existing "Treat the model as an insider risk" list as practitioner examples instead of sitting in the new subsection (assumed no; it stays with the other finance practitioners)?
