---
type: proposal
source: raw/articles/2026-11-24-blograilwaycom-p-security-disclosure-wednesday-october-21st.md
sources:
  - raw/articles/2026-11-24-blograilwaycom-p-security-disclosure-wednesday-october-21st.md
  - raw/newsletters/2026-10-22-keeping-up-with-ai-is-a-full-time-job.md
status: pending
created: 2026-11-24
---

# Proposal: Railway credential exposure and an agent-run cleanup

## Summary

### In short
Deployment platforms that store customers' API keys have become a route to AI inference providers. Railway said an attacker may have decrypted some of its customers' stored secrets, and it called the breach part of a series of attacks on platform companies aimed at those providers. The same incident shows agents being useful in the cleanup: Every used Codex and its company agent to track every key that needed rotating. The proposal adds the incident to **State of Cybersecurity** and **Railway**, plus two source pages. The reason to hesitate is length: the cybersecurity page rises to about 114% of its ceiling.

[[#Open questions|Open questions: 1 to answer.]]

- [x] **Approve all** — checking this box approves every item in `## Intended changes` and `## Schema / vocabulary additions` below; the individual boxes may stay empty.

### The source
On Wednesday 21 October 2026 Railway, a deployment platform, posted a security disclosure. It had detected unusual activity on the systems that store customers' environment variables, the settings where apps keep secrets such as API keys and database passwords. An unauthorized party may have accessed the encrypted variables and, for some of them, obtained the decrypted contents. Railway said it believed this was part of a series of attacks on platform companies aimed at compromising AI inference providers, and it asked those providers to revoke keys proactively. It thought the impact might be limited to some users but told everyone to rotate every stored variable and registry credential. At the same time it paused all deployments, so new keys could not be rolled out. Customers had to choose between disabling old keys and breaking their apps, or leaving exposed keys live.

Every, a Railway customer, described its response in its 22 October newsletter. Willie Williams, its head of platform, had Codex build a shared list of every password and key Every stored on Railway, each with a likely owner. The Every Agent then checked the list every hour and posted how many items each person still had to fix. Williams estimates the list alone would have taken a few hours by hand, and someone would have had to chase progress across time zones into the night.

### What changes
The **Railway** page covers the platform's agent-era bets and a May outage, but not this breach. **State of Cybersecurity** tracks supply-chain attacks through npm and extensions, not through the platforms that hold the keys.

- **State of Cybersecurity** gains a "Railway environment-variable breach" block in the supply-chain section: three bullets covering the breach, the rotate-versus-deploy bind, and Every's agent-run cleanup. It gains one Recent-changes entry dated 21 October. The list is at its cap, so the oldest entry (17 October, Epoch's estimate of the open-weight cyber gap) moves to history. The page date stays 23 November.
- **Railway** gains the incident under Weaknesses / caveats and a Recent-changes entry. Page date moves to 21 October.
- `wiki/index.md` refreshes the Railway line. Two new source pages.

### What to weigh
Railway's notice is the first-day disclosure. The raw file holds no follow-up on how many accounts were affected or how the attack worked, so the drafts keep Railway's own hedges ("may have", "a subset of users"). The cybersecurity page, already in the warning band at 108% of its ceiling, moves into split-candidate range.

## Intended changes

- [ ] **Update** `wiki/state-of/cybersecurity.md` — new "Railway environment-variable breach" block under "AI developer supply chain attacks", before `**Mitigations**`; add `railway-security-disclosure-2026-10-21` and `every-railway-response-agents-2026-10-22` to `sources:` and body `## Sources`; `as_of` stays 2026-11-23; adds one Recent-changes entry dated 2026-10-21
- [ ] **Spill** `wiki/state-of/cybersecurity.md` → `wiki/history/state-of/cybersecurity.md` — the list is at its cap of 10; the oldest-dated entry falls off (expected: the 2026-10-17 Epoch open-weight cyber-gap entry; the 2026-09-30 Fairwind, GLM-5.3 and 2026-09-24 entries already spilled today)
- [ ] **Update** `wiki/tools/railway.md` — incident bullet under Weaknesses / caveats; `as_of` → 2026-10-21; adds one Recent-changes entry dated 2026-10-21; add sources
- [ ] **Update** `wiki/index.md` — refresh the `tools/railway` line
- [ ] **Create** `wiki/sources/articles/railway-security-disclosure-2026-10-21.md` — source summary of Railway's notice
- [ ] **Create** `wiki/sources/newsletters/every-railway-response-agents-2026-10-22.md` — source summary of Every's story

## Page drafts

### wiki/state-of/cybersecurity.md (updated)

Frontmatter: append `railway-security-disclosure-2026-10-21, every-railway-response-agents-2026-10-22` to `sources:`. `as_of` unchanged.

`### AI developer supply chain attacks`: new block inserted after the "npm preinstall-stealer campaign (August 2026)" block and before `**Mitigations**`:

```
**Railway environment-variable breach (October 2026)**
- On 2026-10-21 [Railway](../tools/railway.md) said an unauthorized party may have decrypted some customers' stored environment variables (API keys, database and registry credentials), and called it part of a series of attacks on platform companies aimed at compromising AI inference providers, which it asked to revoke keys
- Railway told every user to rotate all stored secrets while pausing all deployments, so customers had to choose between breaking apps and leaving exposed keys live
- Agent-run cleanup: Every had Codex list each exposed credential with a likely owner, and its company agent posted hourly per-person counts of what was left to rotate
```

`## Recent changes`: adds one entry dated 2026-10-21, inserted in date order between the 2026-10-22 and 2026-10-20 entries; then spills the oldest-dated entry to history (expected: the 2026-10-17 Epoch entry).

```
- [2026-10-21] Railway disclosed that customers' stored secrets may have been decrypted in an attack it ties to a campaign against AI inference providers; added to supply-chain attacks with Every's agent-run credential cleanup.
```

`## Sources`: append

```
- [Railway — Security Disclosure: Wednesday October 21st](../sources/articles/railway-security-disclosure-2026-10-21.md)
- [Every — The agents on Every's Railway response team](../sources/newsletters/every-railway-response-agents-2026-10-22.md)
```

### wiki/history/state-of/cybersecurity.md (updated)

Append at the end of the file (the entry is whichever is oldest at apply time; expected). The file already ends with a 2026-11-24 archive block; if applied on that date, add the entry to that block instead of opening a new header:

```
## Archived from current page on <apply date>

- [2026-10-17] Epoch puts open-weight cyber capability 6–7 months behind the closed frontier.
```

### wiki/tools/railway.md (updated)

Frontmatter: `as_of: 2026-10-21`; `sources: [railway-agent-native-cloud-2026-05-20, railway-security-disclosure-2026-10-21, every-railway-response-agents-2026-10-22]`.

`## Weaknesses / caveats`: new first bullet:

```
- Security incident on 2026-10-21: an unauthorized party may have accessed customers' encrypted environment variables and decrypted some (API keys, database and registry credentials). Railway tied it to a series of attacks on platform companies aimed at AI inference providers, told all users to rotate stored secrets, and paused all deployments while investigating, so new keys could not be rolled out. See [State of Cybersecurity](../state-of/cybersecurity.md)
```

`## Recent changes`: adds one entry dated 2026-10-21 at the top:

```
- [2026-10-21] Security disclosure: customer environment variables possibly decrypted; all users told to rotate secrets while deployments were paused
```

`## Sources`: append

```
- [Railway — Security Disclosure: Wednesday October 21st](../sources/articles/railway-security-disclosure-2026-10-21.md)
- [Every — The agents on Every's Railway response team](../sources/newsletters/every-railway-response-agents-2026-10-22.md)
```

### wiki/index.md (updated)

```
- [tools/railway](tools/railway.md) — bare-metal deployment platform rebuilding for agents; copy-on-write production forks, Central Station, "the pull request is dying"; October 2026 breach exposed stored customer secrets *(as_of: 2026-10-21)*
```

### wiki/sources/articles/railway-security-disclosure-2026-10-21.md (new)

```
---
title: 'Railway — Security Disclosure: Wednesday October 21st'
type: source
source_type: article
source_file: raw/articles/2026-11-24-blograilwaycom-p-security-disclosure-wednesday-october-21st.md
url: https://blog.railway.com/p/security-disclosure-wednesday-october-21st
published: 2026-10-21
ingested: 2026-11-24
domains: [cybersecurity]
---

# Railway — Security Disclosure: Wednesday October 21st

Railway's same-day notice that it detected anomalous activity on systems storing customer environment variables. An unauthorized party may have accessed the encrypted variables and, for some, obtained decrypted contents. Railway links the attack to a series targeting platform companies to compromise AI inference providers.

## Influenced pages
- [State of Cybersecurity](../../state-of/cybersecurity.md) — Railway breach block under supply-chain attacks
- [Railway](../../tools/railway.md) — incident added to caveats

## Key claims extracted
- Detected 2026-10-21; environment variables may contain API keys and database and registry credentials
- Believed to be part of a series of attacks on platform companies aimed at compromising AI inference providers; upstream providers were notified to revoke all keys proactively
- Impact may be limited to a subset of users, but all users were told to roll every environment variable and private registry credential and review logs
- All deployments paused during the investigation; affected accounts to be contacted directly
```

### wiki/sources/newsletters/every-railway-response-agents-2026-10-22.md (new)

```
---
title: Every — The agents on Every's Railway response team
type: source
source_type: newsletter
source_file: raw/newsletters/2026-10-22-keeping-up-with-ai-is-a-full-time-job.md
published: 2026-10-22
ingested: 2026-11-24
domains: [cybersecurity, agents]
---

# Every — The agents on Every's Railway response team

An item in Every's 2026-10-22 newsletter on how Every, a Railway customer, responded to the breach. Its agents built and tracked the credential-rotation list instead of a person doing it by hand.

## Influenced pages
- [State of Cybersecurity](../../state-of/cybersecurity.md) — agent-run cleanup bullet
- [Railway](../../tools/railway.md) — source for the incident

## Key claims extracted
- Railway's pause on app updates left customers choosing between disabling old keys and breaking apps, or keeping them live and exposed
- Head of platform Willie Williams used Codex to build a shared list of passwords and API keys Every stored on Railway, each with a likely owner
- The Every Agent reviewed the list hourly and posted how many entries each person still had to resolve
- Williams estimates the list alone would have taken a few hours by hand, plus a dedicated person tracking progress across time zones
```

## Schema / vocabulary additions

None.

## Open questions
- This block takes State of Cybersecurity's body from 2,167 to about 2,273 words, roughly 114% of the 2,000-word ceiling. That makes it a split candidate, though the split is not required. The agent-incident sections have already moved out; the next natural split is "AI developer supply chain attacks" (about 420 words of campaign write-ups plus mitigations, about 525 with the Railway block), which could become its own trend page with a one-line pointer left behind, bringing the page back to about 1,770 words. Split now as a separate refactor, or leave it?
	- Already mentioned split
