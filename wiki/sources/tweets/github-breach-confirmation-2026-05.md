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
