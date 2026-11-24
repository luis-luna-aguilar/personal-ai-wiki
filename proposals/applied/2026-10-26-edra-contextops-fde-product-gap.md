---
type: proposal
source: raw/tweets/2026-10-26-eugenalpeza-2104936003282546913.md
status: pending
created: 2026-10-26
---

# Proposal: "The FDE boom is a product gap" — ContextOps and executable coverage

## Summary

### In short
Forward-deployed engineers are a stopgap for a missing product: what they really do is translate operators' judgment into agent instructions, and that translation can become a maintained, owner-approved process that operators run themselves. Two former Palantir FDE leads call it ContextOps and propose "executable coverage" as the metric. The proposal adds this as a counter-thesis section on Forward-deployed engineering, maps "ContextOps" in the knowledge-architectures hub to the Knowledge layer, adds one bullet there, and one source page. Reason to hesitate: the hub is already past its length ceiling and the new row grows it further.

[[#Open questions|Open questions: 1 to answer.]]

- [x] **Approve all** — checking this box approves every item in `## Intended changes` and `## Schema / vocabulary additions` below; the individual boxes may stay empty.

### The source
Eugen Alpeza, co-founder and CEO of Edra, published an X Article on 29 September 2026 (464K views). He and his co-founder Yannis led forward-deployed AI engineering at Palantir, and the essay argues the industry is "hiring its way around a missing product". Agents don't know how a company operates, and the people who do have no easy way to teach them, so an FDE sits in the middle: the operator explains, the FDE writes instructions, and every operating change needs the engineer again. The alternative, a context graph connecting a company's records, doesn't close the gap either, because history records mistakes and legitimate exceptions with equal weight.

His example is a telecom's equipment-order history: units of one voltage were usually replaced, but not always, and only the owners of the work could say which departures were mistakes and which were legitimate regional practice the written procedure had never captured. In his reworked version, agents find the pattern, draft a rule with the supporting and non-fitting cases attached, and the supply-chain owner approves it; the rule is tested on representative cases before deployment.

ContextOps is his name for running that continuously: agent instructions with an owner and a version, proposed changes that arrive with evidence, review, tests, deployment and rollback. Executable coverage is the share of cases in a process an agent can handle correctly with current approved procedures, measured on a sample of about a hundred. The learning loop (escalation, resolution with recorded reasoning, proposed update, approval) expands that coverage over time. He rejects fine-tuning on company history, which learns bad habits along with good ones. Edra sells a "GitHub for operators" for this.

### What changes
The FDE page describes the FDE model as how labs win deep enterprise deployments, with no counter-argument.

- **Forward-deployed engineering** gains a section, "The product-gap argument", with the telecom example, ContextOps, executable coverage, the learning loop, and the case against fine-tuning, plus one Current-status bullet pointing to it. Page date moves to 29 September.
- **Knowledge architectures** gains one term-map row: "ContextOps" maps to the Knowledge layer as a maintenance practice, not a store, with a note that its authors contrast it with a context graph. Page date stays 19 October.
- **Knowledge layer** gains one bullet: the operating-rules layer it already mentions now has a named discipline. Page date moves to 29 September.
- One new source page.

### What to weigh
The hub mapping is a judgment call. ContextOps could sit on the Company brain row, whose writers also have "agents draft, humans gate rule changes", but what it maintains is a body of written procedures, compiled documents in the matrix's terms, so it goes on the Knowledge layer row as a practice, the same way "context engineering" maps to Harness. Executable coverage gets no hub row because it is a metric, not an architecture. The new row takes the hub from 111% to about 118% of its ceiling, under the 150% line where a split is required.

## Intended changes

- [ ] **Update** `wiki/training/forward-deployed-engineering.md` — add one Current-status bullet and a new `## The product-gap argument` section after "OpenAI's FDE org in practice"; Current-status stamp and `as_of` move to 2026-09-29; adds one Recent-changes entry dated 2026-09-29 (live list has 2, no spill); append one source id and link
    > See draft below

- [ ] **Update** `wiki/concepts/knowledge-architectures.md` — add one term-map row after the "context engineering" row; adds one Recent-changes entry dated 2026-09-29 (live list has 7, no spill); append one source id and link; `as_of` stays 2026-10-19
    > See draft below

- [ ] **Update** `wiki/concepts/knowledge-layer.md` — add one Current-status bullet; Current-status stamp and `as_of` move to 2026-09-29; adds one Recent-changes entry dated 2026-09-29 (live list has 4, no spill); append one source id and link
    > See draft below

- [ ] **Create** `wiki/sources/tweets/eugenalpeza-fde-boom-product-gap-2026-09-29.md` — source summary

## Page drafts

### wiki/training/forward-deployed-engineering.md (updated)

Frontmatter (changed fields):

```
as_of: 2026-09-29
sources: [fde-race-may-2026, eng-leadership-openai-fde-2026-09-14, eugenalpeza-fde-boom-product-gap-2026-09-29]
```

`## Current status` — heading stamp changes and one bullet is appended:

```
## Current status (as of 2026-09-29)

- A counter-thesis from two former Palantir FDE leads (September 2026): FDE demand is a sign of a missing product, because the work is translating operators' judgment into agent instructions, which operators could maintain themselves (see "The product-gap argument" below).
```

New section, inserted after `## OpenAI's FDE org in practice` and before `## Recent changes`:

```
## The product-gap argument

Eugen Alpeza and Yannis, who led forward-deployed AI engineering at Palantir and now run Edra, argue the industry is "hiring its way around a missing product". An FDE's core job is translation: the operator explains how the company works, the FDE turns that into instructions an agent follows, and every operating change needs the engineer again. Connecting agents to company history (a context graph) does not remove the need, because history records mistakes and legitimate exceptions alike.

- **Worked example.** A telecom's equipment-order history showed units of one voltage usually, but not always, being replaced. Only the owners of the work could say which departures were mistakes (often people unaware the procedure existed) and which were legitimate regional practice the written procedure never captured.
- **ContextOps.** Their name for doing this continuously: agents read case history and draft candidate rules with supporting and contradicting cases attached; the process owner decides which judgments become standing instructions; instructions are tested on representative cases before deployment, carry an owner and a version, and can be rolled back. The process owner is accountable for what the instructions say, and engineering maintains the systems that execute them.
- **Executable coverage.** The share of cases in a process that an agent can handle correctly with current, approved procedures, without someone supplying missing judgment. Measure it on a sample of about a hundred cases before committing a process to agents.
- **The learning loop.** Escalation, resolution with recorded reasoning, a proposed procedure update with evidence, owner approval: each pass expands coverage for every agent using that procedure, and the company owns the loop instead of renting it from an FDE team.
- **Why not fine-tune.** Company history contains bad habits as well as good ones, and every new supplier, region, or policy means retraining. An operator can maintain a written procedure but cannot fine-tune a behaviour out of a model.

The authors' implication for deployment leaders: FDE capacity buys the first translation, and the lasting asset is a process that lets operators change the instructions without an engineer in the middle.
```

`## Recent changes` — insert one entry between the 2026-10-19 and 2026-09-14 entries:

```
- [2026-09-29] Added "The product-gap argument" (Eugen Alpeza, Edra): FDE work as translation operators could own, ContextOps, executable coverage, the escalation-to-procedure learning loop, and the case against fine-tuning on company history.
```

`## Related` — append:

```
- [Knowledge layer](../concepts/knowledge-layer.md) — the maintained, human-approved operating-rules layer that ContextOps keeps current
```

`## Sources` — append:

```
- [Eugen Alpeza on X — The FDE boom is a product gap](../sources/tweets/eugenalpeza-fde-boom-product-gap-2026-09-29.md)
```

### wiki/concepts/knowledge-architectures.md (updated)

Frontmatter `sources:` (append one id; `as_of` unchanged):

```
sources: [knowledge-layer-architecture, llm-wikis-paperwiki-2026-07-06, agent-memory-systems-layer-2026-06, femke-plantinga-company-brains-2026-08-27, ontologies-agentic-systems-2026-07-30, dhravyashah-supermemory-company-brain-2026-07-28, posthog-semantic-layer-2026-08-21, deeplethe-utopia-2026-09-09, helixdb-helix-foundry-2026-10-19, cognition-agent-memory-repo-2026-10, ainews-devin-dreaming-2026-10-06, latent-space-airbnb-inside-out-ai-2026-10-02, eugenalpeza-fde-boom-product-gap-2026-09-29]
```

`## Term map` — insert one row directly after the `| context engineering | ...` row:

```
| ContextOps | Knowledge layer (maintenance practice) | Edra's name for keeping agents' operating procedures current: agents propose rules from case evidence, the process owner approves, and each instruction has an owner, a version, tests, and rollback. A practice, not a store. Its authors contrast it with a context graph (the Company brain alias above), which records mistakes and exceptions alike. See [Forward-deployed engineering](../training/forward-deployed-engineering.md) |
```

`## Recent changes` — insert one entry between the 2026-10-02 and 2026-09-09 entries:

```
- [2026-09-29] Mapped "ContextOps" (Edra) to the Knowledge layer as a maintenance practice for owner-approved, versioned agent procedures, not a new store.
```

`## Sources` — append:

```
- [Eugen Alpeza on X — The FDE boom is a product gap](../sources/tweets/eugenalpeza-fde-boom-product-gap-2026-09-29.md)
```

### wiki/concepts/knowledge-layer.md (updated)

Frontmatter (changed fields):

```
as_of: 2026-09-29
sources: [knowledge-layer-architecture, llm-wikis-paperwiki-2026-07-06, ainews-not-much-happened-2026-07-02, agent-memory-systems-layer-2026-06, karpathy-llm-wiki-gist, rvaniaaaa-second-brain-compiler-2026-08-20, eugenalpeza-fde-boom-product-gap-2026-09-29]
```

`## Current status` — heading stamp changes and one bullet is inserted directly after the "Often paired with a separate human-maintained rules layer…" bullet:

```
## Current status (as of 2026-09-29)

- The operating-rules side now has a named discipline. Edra's "ContextOps" (September 2026) treats an agent's procedures like code: agents propose rule changes from case evidence, the process owner reviews the supporting and contradicting cases and approves, and every instruction has an owner, a version, tests, and rollback. Its metric is executable coverage, the share of a process's cases an agent can handle with current approved procedures (see [Forward-deployed engineering](../training/forward-deployed-engineering.md)).
```

`## Recent changes` — insert one entry above the 2026-09-09 entry:

```
- [2026-09-29] Added Edra's ContextOps as a named discipline for the operating-rules layer: evidence-backed proposals, owner approval, versioned and tested instructions, executable coverage.
```

`## Sources` — append:

```
- [Eugen Alpeza on X — The FDE boom is a product gap](../sources/tweets/eugenalpeza-fde-boom-product-gap-2026-09-29.md)
```

### wiki/sources/tweets/eugenalpeza-fde-boom-product-gap-2026-09-29.md (new)

```
---
title: Eugen Alpeza on X — The FDE boom is a product gap
type: source
source_type: tweet
source_file: raw/tweets/2026-10-26-eugenalpeza-2104936003282546913.md
url: https://x.com/EugenAlpeza/status/2104936003282546913
published: 2026-09-29
ingested: 2026-10-26
domains: [agents]
---

# Eugen Alpeza on X — The FDE boom is a product gap

X Article (464K views) by Eugen Alpeza, co-founder and CEO of Edra and former co-lead of forward-deployed AI engineering at Palantir. Argues that FDE demand is a product gap: the FDE's job is translating operators' judgment into agent instructions, and context graphs of company history don't replace it because history mixes mistakes with legitimate undocumented practice. Proposes ContextOps (turning operational evidence and expert judgment into tested, approved, versioned instructions and keeping them current), executable coverage as the metric, and an escalation → resolution → procedure-update learning loop; rejects fine-tuning on company history. Illustrated with a telecom supply-chain engagement. Edra builds a "GitHub for operators" for this workflow.

## Influenced pages
- [Forward-deployed engineering](../../training/forward-deployed-engineering.md) — new "The product-gap argument" section and Current-status bullet
- [Knowledge architectures](../../concepts/knowledge-architectures.md) — "ContextOps" mapped to the Knowledge layer as a maintenance practice
- [Knowledge layer](../../concepts/knowledge-layer.md) — operating-rules layer gains a named discipline

## Key claims extracted
- Enterprises hire FDEs because agents don't know how the company operates and operators can't easily teach them
- A context graph of company records is more scalable but insufficient: it records both mistakes and legitimate exceptions
- Telecom example: an equipment-replacement voltage rule with exceptions that were partly non-compliance and partly legitimate regional practice
- AI lowers the cost of building and maintaining an agent-friendly procedure base and raises the return on owning one
- ContextOps: turning operational evidence and expert judgment into tested, approved instructions and maintaining them as the business changes; the process owner is accountable, engineering maintains execution
- Executable coverage: share of a process's cases an agent handles correctly with current approved procedures; start by sampling ~100 cases
- Learning loop: escalation → operator resolution with recorded reasoning → agent-proposed procedure update with evidence → owner approval → test and deploy
- Fine-tuning on company history is rejected: it can learn bad habits and must be redone as the business changes
- Agent instructions need an owner, a version, evidence-backed change proposals, tests, deployment, and rollback; operators need to see the cases behind a proposed rule, not only a text diff
```

## Schema / vocabulary additions

None.

## Open questions

- The knowledge-architectures hub goes from 111% to about 118% of its concept ceiling with this row. Should it be split now (for example, moving the term map to its own page), or left in the warning band until it nears 150%?
	- Split it
