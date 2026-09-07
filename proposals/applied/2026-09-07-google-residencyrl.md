---
type: proposal
source: raw/newsletters/2026-08-13-ainews-spacexai-grok-46-and-grok-bot.md
status: pending
created: 2026-09-07
---

# Proposal: Google's ResidencyRL lifts diagnostic accuracy under adversarial telehealth conditions

## Summary

### The source

Buried in the "Benchmarks, Research Directions, and AI-for-Science" section of AINews's 2026-08-13 digest is a one-line item summarizing a thread (by X user kimmonismus) about Google's ResidencyRL work: training Gemini 3.5 Flash over 49,870 simulated telehealth encounters raised diagnostic accuracy under adversarial conditions from 81% to 88%, and cut missed red flags by 31%. That is the entirety of what the digest reports — there is no link to a Google paper, blog post, or technical writeup, and no detail on what "adversarial conditions" means operationally, how the simulated encounters were built, or whether this reflects a shipped product or an internal research result. The claim reaches the wiki secondhand, through a newsletter's compressed recap of a tweet thread.

### What changes

`state-of/healthcare.md` currently has no entry for RL-trained diagnostic/triage accuracy work — its closest existing content is the "AI-assisted healthcare triage" use-case entry (prescription renewal and patient-side self-triage) and the "Patient-side AI" bullet about frontier models matching PCP visits.

- **State of Healthcare** gains one new bullet under "Healthcare triage and patient operations" naming the ResidencyRL result (RL-trained Gemini 3.5 Flash, 49,870 simulated telehealth encounters, 81%→88% diagnostic accuracy under adversarial conditions, missed red flags down 31%), with a Recent-changes entry dated 2026-08-13 and the page date moving to 2026-08-13 (from 2026-07-22).
- New source page for the AINews digest issue, since no page currently covers this raw file.

### What to weigh

This is a thin, secondary source: one sentence in a newsletter, summarizing a tweet thread, about work with no public Google paper or post attached. There's no way to verify the 49,870-encounter figure, the accuracy numbers, or what counts as "adversarial conditions" beyond trusting the thread's characterization. I've kept the wiki bullet close to what the digest actually says rather than embellishing it, and would treat this as a signal to watch for a primary Google writeup rather than a settled result.

## Intended changes

- [x] **Approve all** — checking this box approves every item below; the individual boxes may stay empty.

- [ ] **Update** `wiki/state-of/healthcare.md` — new bullet under "Healthcare triage and patient operations", Recent-changes entry, as_of bump to 2026-08-13
    > See draft below

- [ ] **Create** `wiki/sources/newsletters/ainews-spacexai-grok-46-and-grok-bot-2026-08-13.md` — source summary for the AINews digest issue

## Page drafts

### wiki/state-of/healthcare.md (updated)

```md
---
title: State of Healthcare
type: state-of
domains: [healthcare]
tags: []
as_of: 2026-08-13
sources: [legacy-ai-tools-roadmap-xlsx, dragon-copilot-launch, hippocratic-ai-homepage, tempus-homepage, zocdoc-zo, open-evidence-homepage, konko-kora-homepage, elevenlabs-scribe, 2026-06-16-metalearn-mystery-fatigue-ai, midjourney-medical-scanner-2026-06, ai-healthcare-triage-doctronic-2026-05, mistral-document-ai, bfl-flux-3-2026-07-24, ainews-spacexai-grok-46-and-grok-bot-2026-08-13]
---

### Healthcare triage and patient operations

- [AI-assisted healthcare triage](../use-cases/ai-assisted-healthcare-triage.md) — prescription-renewal and patient-side self-triage workflows where AI does first-pass recommendation or question generation while clinicians retain final judgment *(as of 2026-05-31)*
- **Google ResidencyRL** — RL-trained Gemini 3.5 Flash over 49,870 simulated telehealth encounters; diagnostic accuracy under adversarial conditions rose from 81% to 88%, missed red flags down 31%; known only via a secondary summary thread, no primary Google writeup yet *(as of 2026-08-13)*

## Recent changes

- [2026-08-13] Added Google's ResidencyRL — RL training over simulated telehealth encounters lifted diagnostic accuracy under adversarial conditions from 81% to 88% (secondary source; no primary writeup).
- [2026-07-22] Health in ChatGPT rolled out in the U.S. — connects Apple Health and medical records, with encryption and training/ad-targeting exclusions for connected health data.
- [2026-06-18] Midjourney Medical Scanner added as a speculative imaging-infrastructure signal with strong validation and regulatory caveats.
- [2026-05-31] Doctronic prescription-renewal pilot and patient-side AI self-triage added as healthcare workflow signals.
- [2026-06-16] Added "Patient-side AI" subcategory — frontier models documented to match/exceed PCP visits for ambiguous symptoms (Amy Deng, MetaLearn)
- [2026-04-22] Created the `healthcare` domain and added initial pages for clinical voice, medical knowledge, patient-access, and healthcare operations tools from the legacy workbook exception
```

(Only the `## Subcategories → Healthcare triage and patient operations` block, frontmatter, and `## Recent changes` change; all other sections are unchanged.)

### wiki/sources/newsletters/ainews-spacexai-grok-46-and-grok-bot-2026-08-13.md (new)

```md
---
title: "[AINews] SpaceXAI Grok 4.6 and Grok @Bot"
type: source
source_type: newsletter
source_file: raw/newsletters/2026-08-13-ainews-spacexai-grok-46-and-grok-bot.md
url: https://www.latent.space/p/ainews-spacexai-grok-46-and-grok
published: 2026-08-13
ingested: 2026-09-07
domains: [healthcare]
---

# [AINews] SpaceXAI Grok 4.6 and Grok @Bot

AINews digest for 2026-08-11/12, covering a same-day "Frontier Model Day" cluster (Grok 4.6, Qwen3.8-Max, DeepSeek V4 Pro, Microsoft MAI-Thinking-1), open multimodal/edge model releases, inference/compression tooling, agent-harness commentary, and a research recap section that includes a one-line summary of Google's ResidencyRL clinical-RL result.

## Influenced pages

- [State of Healthcare](../../state-of/healthcare.md) — new ResidencyRL bullet under Healthcare triage and patient operations

## Key claims extracted

- Google's ResidencyRL: training Gemini 3.5 Flash over 49,870 simulated telehealth encounters raised diagnostic accuracy under adversarial conditions from 81% to 88%
- Missed red flags reduced by 31%
- Reported via a secondary summary thread (kimmonismus); no primary Google paper or blog post linked
```

## Open questions

- If a primary Google writeup for ResidencyRL surfaces later, worth revisiting this bullet with harder numbers/methodology rather than leaving it at the secondary-source level of detail.
```
