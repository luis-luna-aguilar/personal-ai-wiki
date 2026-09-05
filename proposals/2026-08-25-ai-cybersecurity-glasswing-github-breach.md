---
type: proposal
sources:
  - raw/tweets/2026-08-25-redirect-7e6ba39a-7572-429a-a8ec-e96cb4006e5d.md
  - raw/tweets/2026-08-25-github-2056949168208552080.md
  - raw/newsletters/2026-05-23-ainews-all-model-labs-are-now-agent-labs.md
status: pending
created: 2026-08-25
---

# Proposal: AI cybersecurity cuts both ways — Glasswing's 10,000+ vulnerabilities and the GitHub breach

## Summary

### The source

On 23 May 2026, a month after launching Project Glasswing — its AI-cybersecurity program built around the restricted Claude Mythos Preview model — Anthropic posted on X that it and partners had found "more than ten thousand high- or critical-severity vulnerabilities in essential software." That one sentence is the whole post as captured; the framing that the industry "will need to adapt to the volume" of findings comes from AINews' recap, not Anthropic's own words.

Four days earlier, on 19 May, GitHub confirmed a breach of its own: an employee device running a poisoned VS Code extension gave an attacker access to GitHub-internal repositories. Over a five-post thread ending 20 May, GitHub said the attacker's claimed haul of roughly 3,800 repositories was "directionally consistent" with its investigation — not an exact count — that critical secrets had been rotated overnight, and that a fuller report would follow. None turned up during this ingest.

### What changes

Both numbers had reached the wiki only via the AINews recap; this grounds them in the companies' own posts. The Mythos page still says "thousands of zero-days" with no program-wide total, and the dashboard's supply-chain section has only Mini Shai-Hulud and the Hugging Face impersonator.

- **Claude Mythos Preview** gains a "Program-wide results" bullet with the 10,000+ figure (AINews' framing attributed), a matching recent-change entry and a source link. Page date moves to 23 May, and the Current status heading — stuck at 12 May — is brought into line. Nothing removed.
- **State of Cybersecurity** extends the Mythos leader line in place with the same figure (no leader swap; GPT-5.5 untouched) and adds a "GitHub internal repo breach" block under AI developer supply chain attacks, flagged as not an AI-specific vector. Recent changes is rewritten as a ten-entry list: two new entries plus the existing eight re-sorted newest-first (the live page has 22 June above 2 July). Ten is exactly the cap, so no history spill; page date stays at its July value.
- Two new tweet source pages, one per company. No schema changes.

### What to weigh

The Anthropic citation is thin: the raw file is a Substack redirect stub with no X permalink and no timestamp, so the source page's URL is the redirect and its 23 May date is inferred from the AINews issue — accept that, or re-fetch the permalink first. Second, a scope call: the GitHub breach sits under "AI developer supply chain attacks" while the draft itself says it is not AI-specific; keep it as a flagged counterpoint, or drop it from the dashboard and keep only the source page. Finally, the dashboard's Recent changes will sit at the cap of ten, so the next ingest touching it needs a spill.

## Intended changes

- [ ] **Approve all** — checking this box approves every item in `## Intended changes` and `## Schema / vocabulary additions` below; the individual boxes may stay empty.

- [x] **Update** `wiki/models/claude-mythos-preview.md` — add the Glasswing 10,000+ vulnerabilities figure; bump `as_of` 2026-05-19 → 2026-05-23 (this is now the newest source-backed claim on the page) and the `## Current status` heading date to match
    > See draft below

- [x] **Update** `wiki/state-of/cybersecurity.md` — update the Claude Mythos Preview leader line with the 10,000+ figure; add a new GitHub breach entry under "AI developer supply chain attacks"; rewrite `## Recent changes` as a full 10-entry newest-first list (2 new + 8 existing reordered; at cap, no spill)
    > See draft below

- [x] **Create** `wiki/sources/tweets/anthropic-glasswing-10k-vulnerabilities.md` — source summary for Anthropic's official X post

- [x] **Create** `wiki/sources/tweets/github-breach-confirmation-2026-05.md` — source summary for GitHub's official X thread

## Page drafts

### wiki/models/claude-mythos-preview.md (updated)

Frontmatter changes:

```md
---
title: Claude Mythos Preview
type: model
domains: [models, cybersecurity, agents]
subcategory: frontier-model
tags: [anthropic, closed-source, beta]
as_of: 2026-05-23
sources: [glasswing, metr-long-horizon-2026-05-12, claude-mythos-m5-bypass-2026-05, cloudflare-glasswing-2026-05, anthropic-glasswing-10k-vulnerabilities]
---
```

Rename the heading `## Current status (as of 2026-05-12)` → `## Current status (as of 2026-05-23)` (brings it into line with frontmatter `as_of`), and add a new bullet to the end of that section's bullet list:

```md
- **Program-wide results (May 2026):** Anthropic said Project Glasswing and its partners found more than 10,000 high- or critical-severity vulnerabilities in essential software within a month of the program's launch; per AINews' recap of the post, Anthropic framed this as a warning that the industry will need to adapt to the volume of findings a model at Mythos's capability level can produce.
```

Add new top entry to `## Recent changes` (4 existing → 5; cap 10, no spill):

```md
- [2026-05-23] Anthropic reported Project Glasswing and partners found 10,000+ high/critical-severity vulnerabilities in essential software within a month of launch — a program-wide figure, not just the Cloudflare result; AINews' recap adds that Anthropic framed it as an industry-wide volume-adaptation warning.
```

Add to `## Sources`:

```md
- [Anthropic on X — Project Glasswing finds 10,000+ vulnerabilities](../sources/tweets/anthropic-glasswing-10k-vulnerabilities.md)
```

### wiki/state-of/cybersecurity.md (updated)

Frontmatter `sources:` list — append `anthropic-glasswing-10k-vulnerabilities, github-breach-confirmation-2026-05` (as_of stays 2026-07-14; this new content is older than the page's current newest claim).

Update the existing Claude Mythos Preview bullet under `### Frontier model capabilities (offensive)`:

```md
- [Claude Mythos Preview](../models/claude-mythos-preview.md) — Anthropic; restricted preview; autonomously found thousands of zero-days; chains low-severity bugs into working exploits (exploit chain construction); autonomous proof generation loop; partners: Cisco, AWS, Microsoft; Cloudflare used it across 50+ repos (Project Glasswing, May 2026); Anthropic reported Project Glasswing and partners found 10,000+ high/critical-severity vulnerabilities within a month of launch (per AINews' recap, framed as a warning that the industry must adapt to this volume of AI-discovered findings) *(as of 2026-05-23)*
```

Add a new campaign entry under `### AI developer supply chain attacks`, after the existing "Hugging Face Transformers impersonator" entry:

```md
**GitHub internal repo breach via compromised VS Code extension (May 2026)**
- A compromised employee device running a poisoned VS Code extension let an attacker exfiltrate GitHub-internal repositories; GitHub's own incident updates called the attacker's claimed figure of ~3,800 repos "directionally consistent" with its investigation, not an exact confirmed count
- GitHub rotated critical secrets/credentials overnight, prioritizing the highest-impact credentials first, and said a fuller report would follow once the investigation completed
- Not an AI-specific attack vector, but notable alongside Glasswing's 10,000+ vulnerability haul as a reminder that conventional dev-tooling supply-chain risk (compromised endpoints, compromised extensions) remains a live threat even as AI dramatically raises both offensive and defensive automated capability
```

Replace the whole `## Recent changes` section with the list below: 2 new entries (2026-05-23, 2026-05-19) inserted, and the existing 8 entries reordered newest-first (the live page has 06-22 above 07-02). Entry text of the existing 8 is unchanged. 10 entries total = cap of 10 (`config.yml → history.recent_changes_cap`), so no spill.

```md
## Recent changes

- [2026-07-14] Devin Security Swarm detailed as Agentic MapReduce (deterministic-selector Plan/Shard, parallel Map, reasoning Reduce, sandboxed Verify); Cognition reported 72% recall on a CVE-pinned benchmark vs. rival scanners, still vendor-run.
- [2026-07-02] Cognition launched Devin Security Swarm, pushing AI-assisted vulnerability detection toward parallel agent workflows that validate exploitability and generate fix PRs.
- [2026-06-22] Gray Swan interview adds AI-native security framing: agents should be treated as untrusted systems; indirect prompt injection, identity, permissions, guardrails, and automated red teaming are core deployment concerns.
- [2026-05-23] Anthropic reported Project Glasswing and partners found 10,000+ high/critical-severity vulnerabilities in essential software within a month of launch; added as a program-wide figure to the Claude Mythos Preview entry (industry-adaptation framing attributed to AINews' recap).
- [2026-05-19] Added GitHub internal-repo breach (compromised employee device, poisoned VS Code extension; attacker's ~3,800-repo claim "directionally consistent" with GitHub's investigation, not confirmed) under AI developer supply chain attacks — a non-AI-specific but dev-tooling-relevant counterpoint to Glasswing's offensive findings.
- [2026-05-19] Cloudflare Project Glasswing: detailed harness architecture (8 stages, ~50 concurrent agents, adversarial validate agent); Mythos exploit chain construction and proof loop confirmed; organic refusals inconsistent as safety boundary; architectural resilience over patch speed as the defender takeaway
- [2026-05-13] OpenAI announced Daybreak as a thin official cyber-defense signal combining frontier models, Codex, and security partners; implementation details remain pending.
- [2026-05-13] Agentic security tooling is becoming a category signal: scanner, monitor, fix-validation, and deployment-risk workflows are being redesigned for software built and operated by agents.
- [2026-05-13] Added `AI developer supply chain attacks`: Mini Shai-Hulud campaign (persistence via .claude/settings.json + .vscode/tasks.json hooks; Guardrails AI v0.10.1 confirmed compromised) and Hugging Face Transformers impersonator; mitigations: minimumReleaseAge, blockExoticSubdeps
- [2026-05-01] Added Claude Security and Cursor Security Review to AI-assisted vulnerability detection; both are secondary-source entries pending primary verification
```

Add to `## Sources`:

```md
- [Anthropic on X — Project Glasswing finds 10,000+ vulnerabilities](../sources/tweets/anthropic-glasswing-10k-vulnerabilities.md)
- [GitHub on X — internal repo breach confirmation](../sources/tweets/github-breach-confirmation-2026-05.md)
```

### wiki/sources/tweets/anthropic-glasswing-10k-vulnerabilities.md (new)

```md
---
title: "Anthropic on X: Project Glasswing finds 10,000+ vulnerabilities"
type: source
source_type: tweet
source_file: raw/tweets/2026-08-25-redirect-7e6ba39a-7572-429a-a8ec-e96cb4006e5d.md
url: https://substack.com/redirect/7e6ba39a-7572-429a-a8ec-e96cb4006e5d?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0
published: 2026-05-23
ingested: 2026-08-25
domains: [cybersecurity, models]
---

# Anthropic on X: Project Glasswing finds 10,000+ vulnerabilities

Official Anthropic (@AnthropicAI) post: "Last month we launched Project Glasswing, our collaborative AI cybersecurity initiative. Since then, we and our partners have found more than ten thousand high- or critical-severity vulnerabilities in essential software."

Citation note: the raw file was captured through the Substack redirect link in AINews' 2026-05-23 issue and contains only the tweet text — no X status permalink and no timestamp. `published` is taken from the date of the AINews issue that linked the post. AINews' recap adds that Anthropic "explicitly warned the industry will need to adapt to the volume of vulnerabilities that models like Claude Mythos Preview can find"; that framing is not in the captured tweet text.

## Influenced pages
- [Claude Mythos Preview](../../models/claude-mythos-preview.md) — added the 10,000+ figure and bumped as_of
- [State of Cybersecurity](../../state-of/cybersecurity.md) — updated the Claude Mythos Preview leader line

## Key claims extracted
- Project Glasswing launched approximately one month before this post (consistent with the wiki's 2026-04-22 launch record)
- Anthropic and partners found 10,000+ high/critical-severity vulnerabilities in essential software within that month
- Per AINews' recap (not in the captured tweet text): Anthropic framed this as a warning that the industry needs to adapt to the volume of findings a model like Claude Mythos Preview can produce
```

### wiki/sources/tweets/github-breach-confirmation-2026-05.md (new)

```md
---
title: "GitHub on X: internal repo breach confirmation"
type: source
source_type: tweet
source_file: raw/tweets/2026-08-25-github-2056949168208552080.md
url: https://x.com/github/status/2056949168208552080
published: 2026-05-19
ingested: 2026-08-25
domains: [cybersecurity]
---

# GitHub on X: internal repo breach confirmation

GitHub's official account (@github) confirmed a compromised employee device involving a poisoned VS Code extension led to unauthorized access to GitHub-internal repositories. The five-post thread began 2026-05-19 (post 1: detection and containment "yesterday", malicious extension version removed, endpoint isolated); posts 2–5 followed on 2026-05-20 with the scope assessment, the ~3,800-repo statement, secret rotation, and the promise of a fuller report. GitHub's own assessment: the attacker's claimed figure of ~3,800 exfiltrated repos is "directionally consistent" with GitHub's investigation so far. Critical secrets were rotated overnight; a fuller report was promised once the investigation completed.

## Influenced pages
- [State of Cybersecurity](../../state-of/cybersecurity.md) — added as a new entry under AI developer supply chain attacks

## Key claims extracted
- Compromise detected and contained 2026-05-18 ("yesterday" relative to the 2026-05-19 post); employee device compromised via a poisoned VS Code extension; malicious extension version removed and endpoint isolated
- GitHub's current assessment (2026-05-20): the activity involved exfiltration of GitHub-internal repositories only
- Attacker's claimed ~3,800 repos is "directionally consistent" with GitHub's investigation so far — not an exact confirmed count
- Critical secrets rotated "yesterday and overnight", highest-impact credentials prioritized first
- GitHub continued analyzing logs, validating rotation, and monitoring for follow-on activity; said it would publish a fuller report once the investigation was complete (not yet available in this source)
```

## Schema / vocabulary additions

None required — all frontmatter uses existing controlled `domains` (`cybersecurity`, `models`), and no new `subcategory` or `tags` values are introduced.

## Open questions

- **Both headline figures are now primary-sourced**, resolving the triage's verify-first flags: Anthropic's own X post confirms the 10,000+ vulnerability figure directly (not just AINews' recap), and GitHub's own X thread confirms the ~3,800-repo figure as "directionally consistent" with its investigation (not an exact number, and GitHub said a fuller report would follow — none has surfaced in the sources checked here). The one piece that remains secondary-only is the "industry must adapt" framing, which is attributed to AINews' recap wherever it appears.
- **GitHub's promised "fuller report"** was not located in this ingest — if GitHub published a follow-up postmortem, it would be worth a future lightweight update to firm up the exact repo count and root-cause details.
