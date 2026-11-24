---
type: proposal
source: raw/articles/2026-11-24-openaicom-index-coordinated-disclosure-of-critical-vulnerabilities.md
sources:
  - raw/articles/2026-11-24-openaicom-index-coordinated-disclosure-of-critical-vulnerabilities.md
  - raw/newsletters/2026-10-22-ainews-openais-patch-the-planet-program-is-1-of.md
status: pending
created: 2026-11-24
---

# Proposal: PHP2Shell and OpenAI's Patch the Planet response

## Summary

### In short
AI can now find bugs with internet-wide impact, and two labs' models found the same ones independently. PHP2Shell, two flaws in PHP's own engine that allowed pre-auth takeover of WordPress, Drupal and Joomla sites, was found by Calif using GPT-5.6 Sol and separately by Wiz using Gemini 4 Argon. OpenAI then coordinated two months of fixes before disclosure on 21 October. The proposal adds three bullets to **State of Cybersecurity**: the find, the coordinated response, and the $1B Frontline Defenders subsidy. It also adds two source pages. The reason to hesitate is length: the page goes to about 115% of its ceiling.

[[#Open questions|Open questions: 1 to answer.]]

- [x] **Approve all** — checking this box approves every item in `## Intended changes` and `## Schema / vocabulary additions` below; the individual boxes may stay empty.

### The source
On 21 October 2026 OpenAI disclosed two memory-corruption vulnerabilities in the core PHP engine. They were named PHP2Shell, filed as CVE-2026-109618 and CVE-2026-109619, and sit in how PHP handles out-of-memory and fatal errors. The researchers demonstrated remote code execution without logging in against WordPress, Drupal and Joomla, plus Heartbleed-style memory leaks (an attacker reading server memory it should not see).

Credit is split. Ryan Austin of the security firm Calif found the flaws with GPT-5.6 Sol as part of OpenAI's Patch the Planet initiative for open-source maintainers. Wiz, now part of Google Cloud, found and reported both independently, and a Wiz-affiliated account credits Gemini 4 Argon. OpenAI led about two months of coordinated remediation. PHP's maintainers wrote the fix, which needed a major engine change. Partners tested patches and prepared protections, and OpenAI briefed US agencies including CISA and the National Cyber Director's office. Cloudflare put free web-application-firewall rules in front of known exploit paths ahead of the 14:00 UTC release. The NSA advised taking systems offline if they could not be patched in time. OpenAI also released a Codex skill for checking PHP versions.

OpenAI calls it a "Defender's Window" case: to its knowledge, AI found the bugs before attackers did. It expects similar findings to rise sharply and proposes a five-stage response framework for public review: fix upstream, give affected organizations time, involve governments, prepare downstream updates, then publish guidance. AINews, the Latent Space newsletter, adds that viral claims of 1.5 million unpatched servers and site shutdowns were not corroborated.

### What changes
The wiki lists Daybreak as OpenAI's defender-access program but has nothing on Patch the Planet, the Frontline Defenders subsidy or PHP2Shell.

- **State of Cybersecurity** gains two bullets under "Coordinated cyber-defense initiatives": the PHP2Shell discovery with its split credit, and the coordinated response. It also gains a "Daybreak for Frontline Defenders" bullet under "Trusted defensive access". One Recent-changes entry dated 21 October is added. The list is at its cap, so the oldest entry (17 October, Epoch's estimate of the open-weight cyber gap) moves to history. The page date stays 23 November.
- Two new source pages, one for OpenAI's post and one for the AINews story.

### What to weigh
The drafts keep only the credit and response facts that OpenAI's post or AINews's careful chronology support. The uncorroborated outage and server counts appear only on the AINews source page. Every's note that a team matched the find with the one-line prompt "find bad vulnerabilities", and Sarah Guo's CVE-volume figure, are left out of the state-of page as color. The cybersecurity page, already in the warning band at 108% of its ceiling, moves into split-candidate range.

## Intended changes

- [ ] **Update** `wiki/state-of/cybersecurity.md` — two bullets under "Coordinated cyber-defense initiatives" and one under "Trusted defensive access"; add `openai-patch-the-planet-php2shell` and `ainews-php2shell-patch-the-planet-2026-10-22` to `sources:` and body `## Sources`; `as_of` stays 2026-11-23; adds one Recent-changes entry dated 2026-10-21
- [ ] **Spill** `wiki/state-of/cybersecurity.md` → `wiki/history/state-of/cybersecurity.md` — the list is at its cap of 10; the oldest-dated entry falls off (expected: the 2026-10-17 Epoch open-weight cyber-gap entry; the 2026-09-30 Fairwind, GLM-5.3 and 2026-09-24 entries already spilled today)
- [ ] **Create** `wiki/sources/articles/openai-patch-the-planet-php2shell.md` — source summary of OpenAI's post
- [ ] **Create** `wiki/sources/newsletters/ainews-php2shell-patch-the-planet-2026-10-22.md` — source summary of the AINews story

## Page drafts

### wiki/state-of/cybersecurity.md (updated)

Frontmatter: append `openai-patch-the-planet-php2shell, ainews-php2shell-patch-the-planet-2026-10-22` to `sources:`. `as_of` unchanged.

`### Trusted defensive access`: new bullet appended after the "Google Fairwind Program" bullet:

```
- **Daybreak for Frontline Defenders** — OpenAI's $1B commitment of subsidized Daybreak access for organizations with limited security resources that protect essential services; PHP2Shell (below) was found through the related Patch the Planet initiative *(as of 2026-10-21)*
```

`### Coordinated cyber-defense initiatives`: two new bullets appended after the "OpenAI-led cyber-defense coalition (August 2026)" bullet:

```
- **PHP2Shell (October 2026)** — two memory-corruption flaws in PHP's engine (CVE-2026-109618/109619) allowed pre-auth RCE on WordPress, Drupal and Joomla; found independently by Calif with GPT-5.6 Sol under OpenAI's Patch the Planet initiative and by Wiz (Google Cloud), which credits Gemini 4 Argon *(as of 2026-10-21)*
- **Patch the Planet response** — OpenAI led two months of remediation with PHP's maintainers, security providers and US agencies before the 2026-10-21 patch; Cloudflare shipped free WAF rules ahead of it and the NSA advised taking unpatchable systems offline. OpenAI calls it a "Defender's Window" case and proposes a five-stage response framework *(as of 2026-10-21)*
```

`## Recent changes`: adds one entry dated 2026-10-21, inserted in date order between the 2026-10-22 and 2026-10-20 entries; then spills the oldest-dated entry to history (expected: the 2026-10-17 Epoch entry).

```
- [2026-10-21] PHP2Shell: two PHP-engine flaws with pre-auth RCE on major CMSs, found independently via GPT-5.6 Sol (Calif, Patch the Planet) and Gemini 4 Argon (Wiz), disclosed after two months of OpenAI-coordinated remediation; Daybreak for Frontline Defenders ($1B subsidy) added to trusted access.
```

`## Sources`: append

```
- [OpenAI — Patch the Planet: global response coordination as agents uncover critical vulnerabilities](../sources/articles/openai-patch-the-planet-php2shell.md)
- [AINews — PHP2Shell chronology and Patch the Planet](../sources/newsletters/ainews-php2shell-patch-the-planet-2026-10-22.md)
```

### wiki/history/state-of/cybersecurity.md (updated)

Append at the end of the file (the entry is whichever is oldest at apply time; expected). The file already ends with a 2026-11-24 archive block; if applied on that date, add the entry to that block instead of opening a new header:

```
## Archived from current page on <apply date>

- [2026-10-17] Epoch puts open-weight cyber capability 6–7 months behind the closed frontier.
```

### wiki/sources/articles/openai-patch-the-planet-php2shell.md (new)

```
---
title: 'OpenAI — Patch the Planet: global response coordination as agents uncover critical vulnerabilities'
type: source
source_type: article
source_file: raw/articles/2026-11-24-openaicom-index-coordinated-disclosure-of-critical-vulnerabilities.md
url: https://openai.com/index/coordinated-disclosure-of-critical-vulnerabilities/
published: 2026-10-21
ingested: 2026-11-24
domains: [cybersecurity]
---

# OpenAI — Patch the Planet: global response coordination as agents uncover critical vulnerabilities

OpenAI's disclosure of the PHP2Shell vulnerabilities and of the two-month coordinated response it led. Calif found a critical flaw with GPT-5.6 Sol under OpenAI's Patch the Planet initiative, and Wiz independently found and reported both vulnerabilities. PHP's maintainers led the fix and release. OpenAI frames the case as a "Defender's Window", expects similar findings to rise sharply, and asks for feedback on a five-stage response framework for critical bugs in widely used software.

## Influenced pages
- [State of Cybersecurity](../../state-of/cybersecurity.md) — PHP2Shell and Patch the Planet bullets; Daybreak for Frontline Defenders bullet

## Key claims extracted
- Two months of coalition work with maintainers, researchers and security providers preceded disclosure on 2026-10-21; the fix required a major PHP-engine change
- Calif found a flaw using GPT-5.6 Sol (Patch the Planet); Wiz independently discovered and reported both
- OpenAI shared a PHP version checker as a Codex skill
- OpenAI calls it one of the most impactful security issues in recent memory and says AI found the bugs before attackers did
- $1B in subsidized Daybreak access through Daybreak for Frontline Defenders, for organizations with limited security resources protecting essential services
- Proposed five-stage response: validate and fix upstream (including adversarial testing of the patch with frontier models); give affected organizations time; coordinate with governments (White House Super Intelligence Force, ONCD, CISA, international partners); prepare downstream updates; publish guidance and support deployment
- Support for maintainers: Codex for OSS subscriptions, sponsorships such as the Rust Foundation, Patch the Planet hands-on help; additional Daybreak blocking classifiers being calibrated
- Longer-term directions: secure-by-default code, memory-safe migrations, formal verification, stronger isolation
- Open questions posed: disclosure windows, emergency patching by governments, early-notice lists, secure-by-default downstream packages
```

### wiki/sources/newsletters/ainews-php2shell-patch-the-planet-2026-10-22.md (new)

```
---
title: AINews — PHP2Shell chronology and Patch the Planet
type: source
source_type: newsletter
source_file: raw/newsletters/2026-10-22-ainews-openais-patch-the-planet-program-is-1-of.md
url: https://www.latent.space/p/ainews-openais-patch-the-planet-program
published: 2026-10-22
ingested: 2026-11-24
domains: [cybersecurity]
---

# AINews — PHP2Shell chronology and Patch the Planet

AINews's lead story for 2026-10-22 reconstructs the PHP2Shell disclosure from participant posts and separates what the record supports from what it does not. It treats the find as a multi-party discovery rather than one vendor's success, and expects at least a year of similar critical findings.

## Influenced pages
- [State of Cybersecurity](../../state-of/cybersecurity.md) — CVE identifiers, Wiz/Gemini 4 Argon credit, Cloudflare WAF and NSA guidance in the PHP2Shell bullets

## Key claims extracted
- CVE-2026-109618 and CVE-2026-109619, in PHP's handling of out-of-memory conditions and fatal errors; demonstrated pre-auth RCE against WordPress, Drupal and Joomla and "Heartbleed-style" memory disclosure
- Calif's Ryan Austin found them in August 2026 with GPT-5.6 Sol; Wiz (acquired into Google Cloud) found them independently, with a Wiz-affiliated account crediting Gemini 4 Argon for discovery, exploit chain, detector and patch validation
- Cloudflare deployed free-tier WAF mitigations before the 14:00 UTC patch and reported early attacks; the NSA advised preparing to update immediately or taking systems offline
- Viral claims of ~1.5M unpatched servers (attributed to Censys) and shutdowns at several institutions and sites, and reports of an early leak, are not corroborated in the record
- Sarah Guo reports CVEs rising from about 4,000 a month to 15,000 since April (not independently verified)
```

## Schema / vocabulary additions

None.

## Open questions
- These bullets take State of Cybersecurity's body from 2,167 to about 2,306 words, roughly 115% of the 2,000-word ceiling. That makes it a split candidate, though the split is not required. The agent-incident sections have already moved out; the next natural split is "AI developer supply chain attacks" (about 420 words of campaign write-ups plus mitigations), which could become its own trend page with a one-line pointer left behind, bringing the page back to about 1,910 words. Split now as a separate refactor, or leave it?
	- Split
