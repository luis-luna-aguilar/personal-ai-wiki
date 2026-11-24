---
type: proposal
source: raw/newsletters/2026-09-16-underwriting-superintelligence-backing-agents-you.md
status: pending
created: 2026-11-24
---

# Proposal: AIUC-1 agent certification backed by insurance

## Summary

### In short
Agent trust is becoming something a company can buy from outside: AIUC's AIUC-1 standard combines audited controls, quarterly adversarial testing run by AIUC itself, and liability insurance written with Lloyd's of London, and it is revised every quarter with Fortune 1000 risk leaders. AIUC raised a $40M Series A on it in September 2026; Lovable, ElevenLabs and Intercom are certified. The proposal adds one compact section on external certification and insurance to Agent autonomy and governance, plus a source page. The one reason to hesitate is scope: AIUC gets no page of its own here, only a governance pattern.

[[#Open questions|Open questions: 1 to answer.]]

- [x] **Approve all** — checking this box approves every item in `## Intended changes` and `## Schema / vocabulary additions` below; the individual boxes may stay empty.

### The source
On 16 September 2026 Latent Space published a long interview with Rune Kvist, cofounder of AIUC and once Anthropic's first product hire, on the day AIUC announced a $40M Series A. His argument is that trust, not capability, now limits agent adoption: an enterprise buying an agent wants to know who pays when it fails, and courts have started answering (the Air Canada ruling held a company to a refund policy its chatbot invented).

AIUC's answer is AIUC-1, a standard for agent security, safety and reliability with six categories, about 51 requirements and 130 controls. Controls come in three kinds: technical ones (configure a groundedness filter), test ones (an independent party checks whether the control actually works), and policy ones (a named person accountable for failures, a plan for telling customers). Auditors such as KPMG and Schellman confirm the evidence exists; AIUC runs the effectiveness tests itself, thousands of simulated jailbreak, hallucination and data-leak attempts each quarter. Certification takes 3 to 10 weeks and lasts a year. A consortium of risk leaders from banks, hospitals and infrastructure operators meets twice a quarter, so the standard changes quarterly; recent revisions added MCP and agent-to-agent concerns. Insurance closes the loop: ElevenLabs bought an agent policy underwritten with Lloyd's, which carries most of the financial risk. Kvist's lesson for builders is that most teams already have guardrails but have never stress-tested them against an adversary.

### What changes
The wiki's governance page covers internal controls (autonomy ladders, controls outside the model) but nothing on outside certification or AI liability insurance.

- **Agent autonomy and governance** gains a subsection, "Certify and insure agents externally", under Governance patterns, and one Recent-changes entry dated 16 September. The page date stays at 12 November because its newer content is untouched.
- One new source page for the interview.

### What to weigh
Whether AIUC deserves its own tool page now, or only after it appears in a second source; the draft keeps it as a pattern on the training page. The interview also previews AIUC moving into frontier-model certification, which is left out as not yet announced.

## Intended changes

- [ ] **Update** `wiki/training/agent-autonomy-and-governance.md` — add the "Certify and insure agents externally" subsection at the end of `## Governance patterns` (after "Treat the model as an insider risk"); add source id to frontmatter and body Sources; adds one Recent-changes entry dated 2026-09-16 (list goes from 7 to 8, no spill)
    > See draft below

- [ ] **Create** `wiki/sources/newsletters/latent-space-aiuc-rune-kvist-2026-09-16.md` — source summary

## Page drafts

### wiki/training/agent-autonomy-and-governance.md (updated)

Frontmatter `sources:` — append `latent-space-aiuc-rune-kvist-2026-09-16`. `as_of` unchanged (2026-11-12).

New subsection, inserted after the "Treat the model as an insider risk" subsection and before `## Open questions`:

```
### Certify and insure agents externally

Enterprise buyers increasingly ask who pays when an agent fails; the Air Canada ruling, which held the airline to a refund policy its chatbot invented, made that a legal question, not a hypothetical. AIUC (cofounder Rune Kvist; $40M Series A, September 2026) sells the answer as one package of standard, testing and insurance. Its AIUC-1 standard for agent security, safety and reliability has six categories and about 51 requirements and 130 controls of three kinds: technical controls (for example, configure a groundedness filter), test controls (an independent party measures whether the control works), and policy controls (a named person accountable for failures, a plan for telling customers). Auditors such as KPMG and Schellman check that the evidence exists; AIUC runs the effectiveness tests itself, thousands of simulated jailbreak, hallucination and data-leak attempts every quarter. Certification takes 3–10 weeks and lasts a year. A consortium of Fortune 1000 risk leaders meets twice a quarter, so the standard is revised quarterly (recent additions: MCP and agent-to-agent risks). Certification pairs with liability cover: ElevenLabs bought an agent insurance policy underwritten with Lloyd's of London, which carries most of the financial risk. Lovable, ElevenLabs and Intercom are certified.

The practical lesson for builders: most teams already have guardrails, but few have stress-tested them against an adversary. This is the outside-assurance counterpart to the insider-risk controls above.
```

`## Recent changes` — adds one entry dated 2026-09-16, placed at the bottom (oldest) of the live list:

```
- [2026-09-16] Added "Certify and insure agents externally": AIUC's AIUC-1 standard (technical, test and policy controls; quarterly adversarial testing by AIUC and quarterly revisions with Fortune 1000 risk leaders) paired with Lloyd's-backed agent liability insurance.
```

`## Sources` — append:

```
- [Latent Space — Underwriting Superintelligence: Rune Kvist on AIUC-1 and agent insurance](../sources/newsletters/latent-space-aiuc-rune-kvist-2026-09-16.md)
```

### wiki/sources/newsletters/latent-space-aiuc-rune-kvist-2026-09-16.md (new)

```
---
title: 'Latent Space — Underwriting Superintelligence: Rune Kvist on AIUC-1 and agent insurance'
type: source
source_type: newsletter
source_file: raw/newsletters/2026-09-16-underwriting-superintelligence-backing-agents-you.md
url: https://www.latent.space/p/aiuc
published: 2026-09-16
ingested: 2026-11-24
domains: [agents]
---

# Latent Space — Rune Kvist on AIUC-1 and agent insurance

Latent Space interview with Rune Kvist, cofounder of AIUC (formerly Anthropic's first product hire), recorded for AIUC's $40M Series A announcement. Kvist argues that trust and liability, not capability, now limit agent adoption, and walks through AIUC-1, AIUC's certification standard for agents, and the insurance AIUC writes with Lloyd's of London alongside it.

## Influenced pages
- [Agent autonomy and governance](../../training/agent-autonomy-and-governance.md) — new "Certify and insure agents externally" subsection

## Key claims extracted
- AIUC announced a $40M Series A on 2026-09-16
- AIUC-1 is a standard for agent security, safety and reliability: six categories, ~51 requirements, ~130 controls
- Three control types: technical (e.g. groundedness filter), third-party test, and policy (named accountable person, customer-notification plan)
- Auditors such as KPMG and Schellman check evidence; AIUC runs quarterly adversarial testing (thousands of simulated jailbreak, hallucination and data-leak attempts)
- Certification takes 3–10 weeks and is valid for a year with quarterly updates
- A consortium of Fortune 1000 risk leaders meets twice a quarter; the standard is revised quarterly (Q2 added MCP and agent-to-agent concerns)
- ElevenLabs bought a first-of-its-kind agent insurance policy with Lloyd's of London as a partner; insurers carry most of the financial risk
- Lovable, ElevenLabs and Intercom have been certified; Cursor and Harvey named as companies working with AIUC
- Most companies have guardrails but have not stress-tested them adversarially
- Air Canada chatbot ruling cited as precedent that companies are bound by what their chatbots promise
- AIUC plans to extend certification to frontier models (previewed, not announced)
```

## Schema / vocabulary additions

None.

## Open questions

- Should AIUC also get its own `wiki/tools/aiuc.md` page now (assumed no: one source, and it is a standards-and-insurance company rather than a tool), or wait until a second source covers it?
	- New page
