---
type: proposal
source:
  - raw/newsletters/2026-06-18-ainews-midjourney-medical-scan-your-organs-like.md
  - raw/newsletters/2026-06-18-metas-worst-morale-in-years.md
  - raw/newsletters/2026-05-31-how-we-work-now.md
  - raw/newsletters/2026-05-24-cheap-competence-new-frontier.md
status: pending
created: 2026-07-08
---

# Proposal: Healthcare imaging infrastructure and AI-assisted triage

## Summary

Two approved healthcare signals update different parts of the healthcare dashboard: Midjourney Medical is a speculative but technically detailed imaging-infrastructure signal, while Doctronic/patient-side AI coverage adds practical workflow metrics around prescription renewal and self-triage.

## Intended changes

- [ ] **Update** `wiki/state-of/healthcare.md` - add imaging infrastructure and healthcare triage/operations signals.
- [ ] **Create** `wiki/use-cases/ai-assisted-healthcare-triage.md` - concise use-case page for AI-assisted prescription renewal and patient self-triage.
- [ ] **Create** `wiki/sources/newsletters/midjourney-medical-scanner-2026-06.md` - source summary.
- [ ] **Create** `wiki/sources/newsletters/ai-healthcare-triage-doctronic-2026-05.md` - source summary.
- [ ] **Update** `wiki/index.md` - add the new use-case page.

## Page drafts

### wiki/state-of/healthcare.md (updated sections)

```md
---
title: State of Healthcare
type: state-of
domains: [healthcare]
tags: []
as_of: 2026-06-18
sources: [..., midjourney-medical-scanner-2026-06, ai-healthcare-triage-doctronic-2026-05]
---

## Subcategories

### Medical imaging infrastructure

- **Midjourney Medical Scanner** - prototype full-body ultrasonic CT / ultrasound system; source coverage reports 358,000 ultrasonic elements, large reconstruction workloads, planned spa-like San Francisco deployment, and explicit caveats around FDA path, clinical validation, privacy, and overdiagnosis *(as of 2026-06-18)*

### Healthcare triage and patient operations

- [AI-assisted healthcare triage](../use-cases/ai-assisted-healthcare-triage.md) - prescription-renewal and patient-side self-triage workflows where AI does first-pass recommendation or question generation while clinicians retain final judgment *(as of 2026-05-31)*

## Recent changes

- [2026-06-18] Midjourney Medical Scanner added as a speculative imaging-infrastructure signal with strong validation and regulatory caveats.
- [2026-05-31] Doctronic prescription-renewal pilot and patient-side AI self-triage added as healthcare workflow signals.
```

### wiki/use-cases/ai-assisted-healthcare-triage.md (new)

```md
---
title: AI-assisted healthcare triage
type: use-case
domains: [healthcare]
tags: []
as_of: 2026-05-31
sources: [ai-healthcare-triage-doctronic-2026-05]
---

# AI-assisted healthcare triage

AI-assisted healthcare triage uses a model to organize patient context, recommend a next step, or prepare sharper questions before a clinician or healthcare workflow makes the final decision.

## Current status (as of 2026-05-31)

- Every reports a Doctronic Utah prescription-renewal pilot where AI recommended renewal 72% of the time and physicians agreed with about 9 out of 10 recommendations.
- After second review, the source reports that 97% of recommendations stood.
- A broader patient-side pattern is emerging: patients bring wearable data, labs, symptoms, medications, and LLM-generated questions into medical encounters.
- The useful claim is not that AI replaces clinicians; it shifts scarce value toward situated physician judgment and escalation decisions.

## Proven patterns

- Use AI for first-pass organization and recommendation, not unsupervised final diagnosis.
- Keep a clinician review step for renewals, escalations, ambiguous symptoms, and high-risk conditions.
- Treat sharper patient questions as a feature: better prework can make clinical encounters more targeted.

## Failure modes

- Overtrusting AI reassurance when symptoms require in-person care.
- Overdiagnosis and anxiety from poorly calibrated self-triage.
- Losing accountability when the model, patient, and clinician disagree about next steps.

## Sources

- [AI healthcare triage and Doctronic prescription-renewal pilot](../sources/newsletters/ai-healthcare-triage-doctronic-2026-05.md)
```

### wiki/index.md (updated section)

```md
## Use cases

- [use-cases/ai-assisted-healthcare-triage](use-cases/ai-assisted-healthcare-triage.md) - AI-assisted prescription renewal and patient-side self-triage workflows where AI prepares recommendations/questions and clinicians retain judgment *(as_of: 2026-05-31)*
```

### wiki/sources/newsletters/midjourney-medical-scanner-2026-06.md (new)

```md
---
title: AINews - Midjourney Medical Scanner
type: source
source_type: newsletter
source_file: raw/newsletters/2026-06-18-ainews-midjourney-medical-scan-your-organs-like.md
url: https://www.latent.space/p/ainews-midjourney-medical-scan-your
published: 2026-06-18
ingested: 2026-07-08
domains: [healthcare]
---

# AINews - Midjourney Medical Scanner

AINews summarizes Midjourney's prototype full-body ultrasonic CT scanner and planned spa-like deployment. The source includes detailed engineering claims but also emphasizes unresolved clinical validation, FDA, privacy, cost, throughput, and overdiagnosis questions.

## Influenced pages

- [State of Healthcare](../../state-of/healthcare.md) - medical imaging infrastructure subcategory

## Key claims extracted

- Midjourney presented a prototype full-body ultrasound CT scanner.
- Source coverage reports 358,000 ultrasonic elements, 17 GB/s capture, 40 GB per body slice, and 21 reconstruction servers.
- No clinical sensitivity/specificity numbers were provided; regulatory and diagnostic paths remain uncertain.
```

### wiki/sources/newsletters/ai-healthcare-triage-doctronic-2026-05.md (new)

```md
---
title: AI healthcare triage and Doctronic prescription-renewal pilot
type: source
source_type: newsletter
source_file:
  - raw/newsletters/2026-05-31-how-we-work-now.md
  - raw/newsletters/2026-05-24-cheap-competence-new-frontier.md
published: 2026-05-31
ingested: 2026-07-08
domains: [healthcare]
---

# AI healthcare triage and Doctronic prescription-renewal pilot

Every's late-May coverage describes practical AI healthcare triage patterns, including a Doctronic Utah prescription-renewal pilot and a broader patient-side AI trend where patients use models to organize health data and prepare sharper questions.

## Influenced pages

- [State of Healthcare](../../state-of/healthcare.md) - healthcare triage and patient operations
- [AI-assisted healthcare triage](../../use-cases/ai-assisted-healthcare-triage.md) - use-case page

## Key claims extracted

- The Doctronic pilot reportedly had AI recommend prescription renewal 72% of the time.
- Physicians agreed with about 9 out of 10 AI recommendations, and 97% stood after second review.
- Patient-side AI can shift clinician value toward situated judgment rather than raw medical knowledge.
```

## Open questions

- Should Midjourney Medical remain only on the healthcare dashboard until it has clinical validation, or should it get a dedicated `tools/` page because of its ambition and technical specificity?
