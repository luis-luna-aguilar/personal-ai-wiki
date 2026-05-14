---
title: Agent skill methodology
type: training
domains: [agents]
tags: [perplexity, agentic]
as_of: 2026-05-13
sources: [perplexity-agent-skill-methodology-2026-05-12, agent-html-artifacts-2026-05-13, agent-skills-context-evals-2026-05-13]
---

# Agent skill methodology

How to build agent skills that work reliably in production and stay maintainable over time. Based on Perplexity's published internal methodology, adapted here for non-technical business teams.

## Current guidance

The core problem: skills written as long procedures become stale, redundant, or broken as the model improves or the task changes. Perplexity's answer is an evals-first, principles-based approach: first define what good and bad behavior looks like, then write the smallest skill that reliably nudges the agent toward the right behavior.

## Proven patterns

**1. Write test cases before writing the skill**
Write 5-10 test cases before writing the skill body. Include:
- Positive cases: requests that should invoke this skill
- Negative cases: similar requests that should not invoke this skill

For a customer-support triage skill, positive cases might include "this customer wants a refund after a damaged delivery" or "this subscriber is asking why they were charged twice." Negative cases might include "write a friendly apology email" or "summarize this customer interview," which need a different skill.

**2. Use natural user language for triggers**
Phrase triggers the way employees or customers actually talk, not the way an internal process document names the workflow:
- Good: "help with a refund request," "figure out who should handle this customer issue," "prepare me for tomorrow's client meeting"
- Bad: "invoke refund_triage_workflow" or "customer_escalation_classifier"

**3. Write principles, not procedures**
The model usually knows how to draft, summarize, search, and ask follow-up questions. The skill should tell it what matters:
- Good: "When a customer asks for a refund, first identify the policy, the customer's stated reason, and whether there is missing information. If policy is unclear, route to a human instead of promising an outcome."
- Bad: "Step 1: open the policy document. Step 2: search for refund. Step 3: copy the paragraph. Step 4..."

**4. Codify production failures as standing instructions**
When the agent fails in production, add the lesson directly to the skill file. This turns each failure into durable training material.
- Example: "Do not offer account credits when the customer is asking for a legal or compliance exception. Escalate those cases."

**5. Cut every line the agent would get right without it**
Before shipping, delete every instruction the model would probably follow on its own. Extra lines add noise and make failures harder to diagnose.
- Test: would a careful teammate reading this think "of course"? Cut it.

**6. Use progressive disclosure for references**
Keep the trigger and core principle small; link deeper references, examples, schemas, and tool docs so they load only when the skill is invoked.

**7. Regression-test skills after model changes**
When a team switches default models, run the skill's positive and negative cases again. A skill that helped one model may be redundant, harmful, or under-specified for the next.

## Failure modes

- **Procedure rot:** detailed steps become wrong as policies, tools, or model behavior changes; principles last longer.
- **Trigger overlap:** the skill fires on the wrong request; negative test cases catch this early.
- **Skill bloat:** every incident adds another line, but nobody removes obsolete guidance; schedule pruning after production reviews or model upgrades.
- **Unclear escalation:** the skill tries to answer cases that should go to a human, especially around refunds, compliance, privacy, legal, finance, or employee issues.
- **Artifact maximalism:** HTML is useful for review and interaction, but making every agent output HTML can waste tokens and make version control noisy. Keep Markdown for durable, versioned knowledge and use HTML when the artifact changes the review behavior.

## Evidence from practice

- Perplexity reports this methodology was developed from internal production failures and adopted as a company-wide skill-writing standard.
- The 5-step cycle (test cases, triggers, principles, failure codification, pruning) is documented in a public Perplexity research post and summarized in Every's May 12 newsletter.

## Open questions

- How much of the test-case writing can non-technical teams own directly, versus needing an AI operations lead to translate examples into evals?
- What is the right pruning cadence: weekly, monthly, after every production incident, or after each model upgrade?
- How should teams share reusable business skills without leaking private policy, customer, or employee context?

## Sources

- [Perplexity agent skill methodology](../sources/newsletters/perplexity-agent-skill-methodology-2026-05-12.md)
- [Agent-generated HTML artifacts](../sources/tweets/agent-html-artifacts-2026-05-13.md)
- [Agent skills, context loading, evals, and migration discipline](../sources/newsletters/agent-skills-context-evals-2026-05-13.md)
