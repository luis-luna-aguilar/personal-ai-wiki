---
type: proposal
source: raw/newsletters/2026-05-23-ainews-all-model-labs-are-now-agent-labs.md
status: pending
created: 2026-08-25
---

# Proposal: AI cybersecurity cuts both ways — Glasswing's 10,000+ vulnerabilities and the GitHub breach

## Summary

Anthropic reported that Project Glasswing and its partners found more than 10,000 high/critical-severity vulnerabilities in essential software within a month of launch — confirmed via Anthropic's own X post, not just secondary newsletter coverage. In the same window, GitHub confirmed a compromised employee device and a poisoned VS Code extension led to internal-repo theft, with GitHub's own account calling the attacker's claimed ~3,800-repo figure "directionally consistent" with its investigation. Both claims are now grounded in primary-source posts from the companies themselves rather than only secondary newsletter recaps.

## Intended changes

- [ ] **Update** `wiki/models/claude-mythos-preview.md` — add the Glasswing 10,000+ vulnerabilities figure; bump `as_of` 2026-05-19 → 2026-05-23 (this is now the newest source-backed claim on the page)
    > See draft below

- [ ] **Update** `wiki/state-of/cybersecurity.md` — update the Claude Mythos Preview leader line with the 10,000+ figure; add a new GitHub breach entry under "AI developer supply chain attacks"
    > See draft below

- [ ] **Create** `wiki/sources/tweets/anthropic-glasswing-10k-vulnerabilities.md` — source summary for Anthropic's official X post

- [ ] **Create** `wiki/sources/tweets/github-breach-confirmation-2026-05.md` — source summary for GitHub's official X thread

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

Add a new bullet to the `## Current status (as of 2026-05-12)` bullet list (heading text left as-is, consistent with existing drift between the heading date and frontmatter `as_of` already on this page):

```md
- **Program-wide results (May 2026):** Anthropic said Project Glasswing and its partners found more than 10,000 high- or critical-severity vulnerabilities in essential software within a month of the program's launch, and warned that the industry will need to adapt to the volume of findings a model at Mythos's capability level can produce.
```

Add new top entry to `## Recent changes`:

```md
- [2026-05-23] Anthropic reported Project Glasswing and partners found 10,000+ high/critical-severity vulnerabilities in essential software within a month of launch; framed as an industry-wide volume-adaptation warning, not just a Cloudflare-specific result.
```

Add to `## Sources`:

```md
- [Anthropic on X — Project Glasswing finds 10,000+ vulnerabilities](../sources/tweets/anthropic-glasswing-10k-vulnerabilities.md)
```

### wiki/state-of/cybersecurity.md (updated)

Frontmatter `sources:` list — append `anthropic-glasswing-10k-vulnerabilities, github-breach-confirmation-2026-05` (as_of stays 2026-07-14; this new content is older than the page's current newest claim).

Update the existing Claude Mythos Preview bullet under `### Frontier model capabilities (offensive)`:

```md
- [Claude Mythos Preview](../models/claude-mythos-preview.md) — Anthropic; restricted preview; autonomously found thousands of zero-days; chains low-severity bugs into working exploits (exploit chain construction); autonomous proof generation loop; partners: Cisco, AWS, Microsoft; Cloudflare used it across 50+ repos (Project Glasswing, May 2026); Anthropic reported Project Glasswing and partners found 10,000+ high/critical-severity vulnerabilities within a month of launch, warning the industry to prepare for this volume of AI-discovered findings *(as of 2026-05-23)*
```

Add a new campaign entry under `### AI developer supply chain attacks`, after the existing "Hugging Face Transformers impersonator" entry:

```md
**GitHub internal repo breach via compromised VS Code extension (May 2026)**
- A compromised employee device running a poisoned VS Code extension let an attacker exfiltrate GitHub-internal repositories; GitHub's own incident updates called the attacker's claimed figure of ~3,800 repos "directionally consistent" with its investigation, not an exact confirmed count
- GitHub rotated critical secrets/credentials overnight, prioritizing the highest-impact credentials first, and said a fuller report would follow once the investigation completed
- Not an AI-specific attack vector, but notable alongside Glasswing's 10,000+ vulnerability haul as a reminder that conventional dev-tooling supply-chain risk (compromised endpoints, compromised extensions) remains a live threat even as AI dramatically raises both offensive and defensive automated capability
```

Add 2 new top entries to `## Recent changes`:

```md
- [2026-05-23] Anthropic reported Project Glasswing and partners found 10,000+ high/critical-severity vulnerabilities in essential software within a month of launch; added as a program-wide figure to the Claude Mythos Preview entry.
- [2026-05-20] Added GitHub internal-repo breach (compromised employee device, poisoned VS Code extension, ~3,800 repos per GitHub's own confirmation) under AI developer supply chain attacks — a non-AI-specific but dev-tooling-relevant counterpoint to Glasswing's offensive findings.
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
url: https://x.com/AnthropicAI
published: 2026-05-23
ingested: 2026-08-25
domains: [cybersecurity, models]
---

# Anthropic on X: Project Glasswing finds 10,000+ vulnerabilities

Official Anthropic (@AnthropicAI) post: "Last month we launched Project Glasswing, our collaborative AI cybersecurity initiative. Since then, we and our partners have found more than ten thousand high- or critical-severity vulnerabilities in essential software."

## Influenced pages
- [Claude Mythos Preview](../../models/claude-mythos-preview.md) — added the 10,000+ figure and bumped as_of
- [State of Cybersecurity](../../state-of/cybersecurity.md) — updated the Claude Mythos Preview leader line

## Key claims extracted
- Project Glasswing launched approximately one month before this post (dates the launch to roughly late April 2026)
- Anthropic and partners found 10,000+ high/critical-severity vulnerabilities in essential software within that month
- Framed by Anthropic as a signal the industry needs to adapt to the volume of findings a model like Claude Mythos Preview can produce
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

GitHub's official account (@github) confirmed a compromised employee device involving a poisoned VS Code extension led to unauthorized access to GitHub-internal repositories. GitHub's own assessment: the attacker's claimed figure of ~3,800 exfiltrated repos is "directionally consistent" with GitHub's investigation. Critical secrets were rotated overnight; a fuller report was promised once the investigation completed.

## Influenced pages
- [State of Cybersecurity](../../state-of/cybersecurity.md) — added as a new entry under AI developer supply chain attacks

## Key claims extracted
- Compromise detected and contained 2026-05-19 (device compromised via a poisoned VS Code extension)
- Only GitHub-internal repositories were exfiltrated, per GitHub's assessment (no customer-repo compromise claimed)
- Attacker's claimed ~3,800 repos is "directionally consistent" with GitHub's own investigation — not an exact confirmed count
- Critical secrets/credentials rotated overnight, highest-impact first
- GitHub said it would publish a fuller report once the investigation was complete (not yet available in this source)
```

## Schema / vocabulary additions

None required — all frontmatter uses existing controlled `domains` (`cybersecurity`, `models`), and no new `subcategory` or `tags` values are introduced.

## Open questions

- **Both headline figures are now primary-sourced**, resolving the triage's verify-first flags: Anthropic's own X post confirms the 10,000+ vulnerability figure directly (not just AINews' recap), and GitHub's own X thread confirms the ~3,800-repo figure as "directionally consistent" with its investigation (not an exact number, and GitHub said a fuller report would follow — none has surfaced in the sources checked here).
- **Cross-proposal dependency.** This proposal links to `wiki/sources/newsletters/anthropic-is-onto-something.md` and `wiki/sources/newsletters/ainews-all-model-labs-are-now-agent-labs.md`, both created by the companion proposal (`2026-08-25-anthropic-agent-infra-harness-mcp.md`) rather than by this one, to avoid two proposals creating the same file. Apply that proposal first (or apply both together) so those links resolve immediately rather than briefly pointing at not-yet-created pages.
- **GitHub's promised "fuller report"** was not located in this ingest — if GitHub published a follow-up postmortem, it would be worth a future lightweight update to firm up the exact repo count and root-cause details.
