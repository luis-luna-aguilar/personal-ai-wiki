---
type: proposal
source: raw/deep-research/2026-04-23 Agents Evals.md
status: pending
created: 2026-04-24
---

# Proposal: Autonomy ladder and eval-gated permission governance

## Summary

The autonomy ladder frames agent deployment as a staged progression where each level up requires passing an eval suite that proves the agent can handle the expanded authority. This is a useful governance model for the "when do we trust the agent to do more?" question, and is directly applicable to the existing `company-wide-ai-enablement.md` training page.

The five-level structure is well-established in agent safety literature. The specific named abstraction ("Authority Graph") and precise pass-rate thresholds (e.g., 95% over 100 traces) are from the research report and are hedged accordingly in the draft below.

## Intended changes

- [x] **Update** `wiki/training/company-wide-ai-enablement.md` — add a new "## Autonomy ladder" section under Proven patterns; update `as_of` and `sources`
    > See diff below

- [x] **Update** `wiki/training/anti-autopilot-review-friction.md` — add one bullet to Proven patterns: escalation evals as a review friction forcing function; update `as_of` and `sources`
    > See diff below

## Diffs

### wiki/training/company-wide-ai-enablement.md — new section

Add this as a new top-level section after `## Failure modes`, before `## Humans in the loop vs. above the loop`:

````md
## Autonomy ladder

A practical governance model for expanding what an agent is allowed to do: treat autonomy not as a binary switch but as a staged ladder where each step up requires eval evidence that the agent can handle the broader authority safely.

**Five levels:**

| Level | Name | What the agent can do |
|---|---|---|
| 0 | Read-only assistant | Synthesizes, proposes, retrieves. Human executes everything. |
| 1 | Human-mediated actions | Drafts artifacts (emails, code, notes). Human reviews and executes. |
| 2 | Guarded actions | Executes low-risk actions autonomously (update a safe CRM field, add internal notes). High-risk actions require explicit human approval. |
| 3 | Conditional autonomy | Manages multi-step workflows autonomously but pauses at predefined high-risk checkpoints. |
| 4/5 | High to full autonomy | Executes end-to-end within strict policy boundaries. Reports to humans only on completion or unresolvable anomaly. |

**Promoting between levels requires eval evidence, not just elapsed time.** To move an agent from Level 1 to Level 2, the eval suite must prove the agent reliably adheres to role-based access controls and policy boundaries. To move to Level 3, the agent must pass escalation evals: inject adversarial and out-of-scope queries into the test suite and measure whether the agent triggers a human handoff rather than hallucinating an action. The failure mode being tested is: does the agent know what it doesn't know?

**Practical permission controls:** Transitions are enforced mechanically, not by judgment alone. Common mechanisms: pass-rate thresholds over a rolling window of consecutive traces (e.g., 95% success before a Level 2 → 3 promotion), cost-based throttling (dollar-per-hour or monthly credit limits that freeze agent spending if a runaway loop is detected), and False Escalation Rate tracking (cases where the agent escalated but the human approved without changes — a reviewer fatigue indicator). Specific thresholds should be calibrated per organization; the values cited in the research report are directional, not universal.

**The practical implication for enablement:** Don't deploy a new agent at Level 3 or 4 because the vendor demo looked good. Start at Level 1, build an eval suite, and promote based on measured evidence. The enablement question becomes: "what eval evidence would make us comfortable giving this agent more authority?"
````

Update frontmatter:
- `as_of: 2026-04-23`
- Add `agents-evals-deep-research` to `sources:` list

### wiki/training/anti-autopilot-review-friction.md — one new bullet

Add to `## Proven patterns`:

````md
- **Escalation evals as a forcing function.** Before granting an agent autonomous action, test whether it knows when *not* to act. Inject adversarial examples and out-of-scope requests into the eval suite and verify the agent reliably triggers a human handoff rather than hallucinating a response. This is a structural check — it forces you to define the edge cases before the agent encounters them in production, which is a form of review friction applied at the design stage rather than the deployment stage.
````

Update frontmatter:
- `as_of: 2026-04-23`
- Add `agents-evals-deep-research` to `sources:` list

## Open questions

- Is the "False Escalation Rate" term worth including by name, or should it just be described in plain language? It's from the report and may be report-normalized.
	- just plain language
- The "Authority Graph" is intentionally omitted from the draft because it appears to be a report-synthesized abstraction without a strong primary source. If the user wants it included, it should be clearly attributed as a report framing.
	- ok
