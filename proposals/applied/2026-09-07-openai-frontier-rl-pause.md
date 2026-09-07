---
type: proposal
source: raw/newsletters/2026-08-19-ainews-memory-prices-up-500-in-12-months.md
status: pending
created: 2026-09-07
---

# Proposal: OpenAI pauses some frontier RL training for two weeks over safety/security hardening

## Summary

### The source
AINews's 2026-08-19 issue reports that OpenAI paused part of its frontier RL training — holding back its largest planned run — for two weeks to strengthen workload/network isolation, continuous security testing, and multistage monitoring before proceeding. Reported implementation detail is unusually concrete: monitoring adds roughly 20% overhead, sampled-token monitoring can page safety/security/research teams within about 30 minutes, and higher-risk tool-using inference may ship with active monitors attached from the start. Sam Altman framed the pause as capabilities outpacing safety/alignment readiness; Greg Brockman said confidence in safety will increasingly set the pace of frontier scaling. OpenAI clarified the slowdown mainly affects farther-out releases, not models already near shipping.

### What changes
The wiki's restricted-frontier-deployment trend already tracks OpenAI's Astra capability-threshold gating (announced 2026-08-08) and its resolution as GPT-5.6-Cyber (2026-08-11); this is a distinct, earlier-stage pattern — a training-time pause for infrastructure hardening, not a release-stage capability classification.

- **Restricted frontier deployment** gains a new dated subsection on this training-pause pattern, a new Recent-changes entry, and its page date moves to 19 August. Its Recent-changes list is already over the 5-entry cap (9 live entries), so this proposal also spills the 5 oldest entries (dated 30 June through 22 April) to a new `wiki/history/trends/restricted-frontier-deployment.md` file, bringing the live section back to 5.
- The AINews issue's source page is created by a companion proposal for the Qwen3.8-27B signal, whose draft already lists this page under its Influenced pages — no separate action needed here.

### What to weigh
The quantified monitoring details (20% overhead, ~30-minute paging) come from OpenAI's own disclosure as relayed by AINews, not a fetched primary OpenAI statement — treat as a reported claim, consistent with how this page already caveats similarly-sourced entries (e.g. the Astra classification, also newsletter-relayed).

## Intended changes

- [x] **Approve all**

- [ ] **Update** `wiki/trends/restricted-frontier-deployment.md` — new dated subsection, Recent-changes entry, spill of 5 oldest entries to history, as_of bump
    > See draft below

- [ ] **Create** `wiki/history/trends/restricted-frontier-deployment.md` — new history file with the 5 spilled entries
    > See draft below

## Page drafts

### wiki/trends/restricted-frontier-deployment.md (updated)

```md
Frontmatter changes: as_of: 2026-08-19; sources: append ainews-memory-prices-openai-pause-2026-08-19

## Training-time safety pause as a new restriction pattern (August 2026) — new subsection, inserted after "Capability-threshold gating before release (August 2026)"

OpenAI paused part of its frontier RL training — holding its largest planned run — for two weeks to strengthen workload/network isolation, continuous security testing, and multistage monitoring before proceeding. This is a distinct pattern from the capability-threshold gating tracked above: rather than classifying a specific near-release model (Astra) against the Preparedness Framework, this is a pause on training infrastructure itself, applied earlier in the pipeline and not tied to one named model. Reported implementation detail: monitoring adds roughly 20% overhead, sampled-token monitoring can page safety/security/research teams within ~30 minutes, and higher-risk tool-using inference may ship with active monitors attached from the start. Sam Altman framed it as capabilities outpacing safety/alignment readiness; Greg Brockman said confidence in safety will increasingly set the pace of frontier scaling. OpenAI clarified the slowdown mainly affects farther-out releases, not models already near shipping.

## Recent changes (new entry, prepended; existing list re-capped to 5)

- [2026-08-19] OpenAI pauses part of its frontier RL training for two weeks to harden workload/network isolation, security testing, and monitoring — a training-time pause distinct from the Astra capability-threshold classification below, affecting farther-out releases only.
- [2026-08-11] OpenAI launched GPT-5.6-Cyber under an expanded Daybreak initiative, restricted to approved defenders — the resolution of Astra's capability-threshold gating below.
- [2026-08-08] OpenAI classified its forthcoming Astra model as unable to rule out Critical cyber capability under its Preparedness Framework, pausing internal activities pending strengthened controls ahead of any release — a new pre-release capability-threshold-gating example for this trend.
- [2026-07-09] Superhuman reports the GPT-5.6/Sol restricted-preview access restriction lifted after the US Commerce Department ended it, clearing the family for public rollout (no OpenAI statement captured). OpenAI's June 26 primary announcement captured, confirming the preview terms.
- [2026-07-02] Fable 5 returned online after its export-control suspension, with added safety fallback routing (some cyber/bio/chem requests route to Opus 4.8) — the resolution referenced above corrects the 2026-07-09 entry's "first resolution" framing, since this predates it.

<!-- The following 5 entries move to wiki/history/trends/restricted-frontier-deployment.md: -->
<!-- [2026-06-30] Every strategy framing added ... -->
<!-- [2026-06-29] Newsletter coverage reports OpenAI GPT-5.6/Sol restricted preview ... -->
<!-- [2026-06-26] METR's GPT-5.6 Sol evaluation ... -->
<!-- [2026-06-17] Fable 5 / Mythos 5 suspended globally ... -->
<!-- [2026-04-22] Glasswing disclosed publicly ... -->
```

### wiki/history/trends/restricted-frontier-deployment.md (new)

```md
# Restricted Frontier Deployment — History

## Archived from current page on 2026-09-07

- [2026-06-30] Every strategy framing added: teams should model regulatory and access shocks as explicit AI strategy assumptions.
- [2026-06-29] Newsletter coverage reports OpenAI GPT-5.6/Sol restricted preview for coding/cybersecurity via vetted API and Codex access; official source capture still needed.
- [2026-06-26] METR's GPT-5.6 Sol evaluation reinforces restricted frontier deployment as a safety/evaluation workflow, not only a product availability decision.
- [2026-06-17] Fable 5 / Mythos 5 suspended globally under US government export controls — first regulatory rather than voluntary restriction; UK carve-out denied; 76 security experts protest (FreeFable.org)
- [2026-04-22] Glasswing disclosed publicly: Mythos Preview found thousands of zero-days across major OSes and browsers autonomously; confirmed restricted deployment with partner program (Cisco, AWS, Microsoft)
```

## Open questions

None beyond the sourcing caveat above.
