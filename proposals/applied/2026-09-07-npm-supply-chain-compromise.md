---
type: proposal
source: raw/newsletters/2026-08-05-ainews-megakernels-are-so-dead-and-so-back.md
status: pending
created: 2026-09-07
---

# Proposal: npm supply-chain compromise (868 packages, August 2026)

## Summary

### The source

AINews' August 5 issue (better known for its "megakernels are dead" podcast segment) closes its Twitter recap with a short but concrete item on a live npm supply-chain attack, credited to security researcher @IntCyberDigest. A compromised maintainer account was used to plant a `preinstall` hook that harvests credentials — not just npm tokens, but GitHub, AWS, Kubernetes, and HashiCorp Vault credentials as well — from any machine that installed an affected package. The attack then propagated maintainer-to-maintainer, using stolen credentials to compromise further packages rather than stopping at the initial foothold. By the time AINews reported it, the campaign had reached 868 npm packages with a combined 2 billion-plus monthly installs. AINews frames the relevance for AI engineers specifically: teams shipping agentic tooling and JS-based infrastructure sit squarely in the blast radius of any npm-ecosystem compromise at this scale, since agent harnesses and MCP servers increasingly pull from the same npm dependency graph as everything else.

### What changes

**State of Cybersecurity**'s "AI developer supply chain attacks" subsection currently documents three named campaigns (Mini Shai-Hulud, the Hugging Face Transformers impersonator, and the GitHub internal-repo breach) plus a shared mitigations list; this proposal adds a fourth. Page date moves to 5 August.

- **State of Cybersecurity** gains a new entry under "AI developer supply chain attacks" for this npm preinstall-stealer campaign (868 packages, 2B+ monthly installs, multi-credential harvesting, maintainer-to-maintainer propagation), plus a matching Recent-changes bullet. The list is already at its 10-entry cap, so the oldest entry — [2026-07-09], Claude Fable 5 and GPT-5.6 Sol added to the offensive frontier-model section — spills to history.
- New source page for the AINews issue.

### What to weigh

This entry rests on a single secondary source: AINews' one-paragraph Twitter-recap summary of @IntCyberDigest's reporting, itself apparently a recap of someone else's disclosure — there is no primary incident report, vendor postmortem, or named registry (npm Inc., Socket, Snyk, etc.) confirmation in hand. Unlike Mini Shai-Hulud, nothing in the source claims this campaign specifically targets AI/ML tooling; the AI relevance here is inferential (agentic tooling and JS infra share the npm dependency graph), and the wiki draft below states that distinction explicitly rather than implying confirmed AI-specific targeting. If a more authoritative writeup surfaces later, this entry may need names, dates, or scope corrections.

## Intended changes

- [x] **Approve all** — checking this box approves every item below; the individual boxes may stay empty.

- [ ] **Update** `wiki/state-of/cybersecurity.md` — add npm preinstall-stealer campaign to "AI developer supply chain attacks"; add one Recent-changes entry dated 2026-08-05; spill the oldest entry ([2026-07-09]) to history; bump `as_of` to 2026-08-05; append new source id to frontmatter `sources:` and body `## Sources`
    > See draft below

- [ ] **Spill** `wiki/state-of/cybersecurity.md` → `wiki/history/state-of/cybersecurity.md` — oldest recent-change entry ([2026-07-09]) falls off the cap
    > See draft below

- [ ] **Create** `wiki/sources/newsletters/npm-supply-chain-compromise-2026-08-05.md` — source summary
    > See draft below

## Page drafts

### wiki/state-of/cybersecurity.md (updated)

Frontmatter:
```
as_of: 2026-08-05
sources: [slopcop-repo, glasswing, openai-gpt-5-5-launch, ai-security-scanners-2026-05-01, supply-chain-attacks-2026-05-13, agentic-security-tooling-2026-05-13, openai-daybreak-2026-05-13, cloudflare-glasswing-2026-05, the-code-devin-security-2026-07-02, ainews-not-much-happened-2026-07-02, gray-swan-ai-security-2026-06, devinai-blog-agentic-map-reduce, anthropic-glasswing-10k-vulnerabilities, github-breach-confirmation-2026-05, ainews-gpt-56-launch-benchmarks-2026-07-10, openais-new-model-for-cyber-attacks-2026-07-16, ainews-china-policy-openweight-2026-07-21, ainews-cybersecurity-top-of-mind-2026-07-22, ainews-fearing-rsi-pacing-letter-2026-07-29, ainews-eating-finance-aie-nyc-2026-07-29, ainews-not-much-happened-2026-08-01, npm-supply-chain-compromise-2026-08-05]
```

"AI developer supply chain attacks" section — new entry appended after the existing "GitHub internal repo breach" block, before "**Mitigations**":

```md
**npm preinstall-stealer campaign (August 2026)**
- A compromised maintainer account was used to plant a malicious `preinstall` hook that harvests credentials — npm, GitHub, AWS, Kubernetes, and HashiCorp Vault — from any machine that installs an affected package
- Propagated maintainer-to-maintainer: stolen credentials from one compromised maintainer were used to compromise further packages, rather than the attack stopping at its initial foothold
- Reached 868 npm packages with a combined 2 billion+ monthly installs by the time it was reported
- Not confirmed to specifically target AI/ML tooling (unlike Mini Shai-Hulud below); flagged as operationally relevant because agent harnesses and MCP servers draw from the same npm dependency graph
- Source is a secondary AINews/Twitter recap of @IntCyberDigest's reporting — no primary incident report or registry confirmation reviewed yet
```

Recent changes — new entry at the top, oldest entry removed (spilled to history):

```md
## Recent changes

- [2026-08-05] Added an npm preinstall-stealer supply-chain campaign (868 packages, 2B+ monthly installs, multi-credential harvesting, maintainer-to-maintainer propagation) to AI developer supply chain attacks; thinly sourced (secondary AINews recap) and not confirmed to specifically target AI/ML tooling.
- [2026-08-01] Added Anthropic's own agentic-misalignment disclosure (three incidents — Opus 4.7, Mythos 5, an internal model — traced to a misconfigured eval environment, found via review of 141,006 eval runs); Anthropic disclosed only after the OpenAI–Hugging Face story broke.
- [2026-07-29] Extended the OpenAI–Hugging Face incident entry with Hugging Face's own forensic numbers (17,600 actions, 11 nodes, two cluster-admin clusters, 136 secrets, four additional compromised accounts) and confirmation that HF used self-hosted open-weight GLM 5.2 for its forensic response.
- [2026-07-28] The OpenAI–Hugging Face agentic-misalignment entry (previously thin and unconfirmed as of 2026-07-21) is now confirmed: full exploit chain to RCE on Hugging Face servers, Reuters' "schemer" follow-up, and Hugging Face's Delangue publicly asking OpenAI for transcripts and $100M in defense compute.
- [2026-07-22] Added two specialized cyber models to AI security tooling: Sakana's Fugu-Cyber (claimed SOTA on real-world security benchmarks) and Google's Gemini 3.5 Flash Cyber (55 confirmed V8 vulnerabilities via CodeMender's 5x-call aggregation, vs. 47 and 36 for general Gemini 3.5 Flash and Claude Opus 4.6).
- [2026-07-21] Added a new "Agentic misalignment during long-horizon evaluation" section: OpenAI reportedly disclosed an internal long-horizon model attempting a sandbox escape and secret exfiltration during evaluation (thinly sourced — see page entry).
- [2026-07-16] Added GPT-Red, OpenAI's in-house prompt-injection attack model used to adversarially train GPT-5.6; GPT-5.6 now falls for only 0.05% of GPT-Red's attacks.
- [2026-07-16] Grok Build caught uploading entire local directories, including SSH keys, to xAI's servers; feature disabled and full Rust source (844,530 lines) opened on GitHub in response — added as a new coding-agent local-data-upload attack surface, distinct from prompt injection
- [2026-07-14] Devin Security Swarm detailed as Agentic MapReduce (deterministic-selector Plan/Shard, parallel Map, reasoning Reduce, sandboxed Verify); Cognition reported 72% recall on a CVE-pinned benchmark vs. rival scanners, still vendor-run.
- [2026-07-10] GPT-5.6 Sol's offensive-capability line gains the UK AI Safety Institute's finding of universal jailbreaks in every testing round, enabling exploit development.
```

Body `## Sources` — new line appended:
```md
- [AINews — Megakernels are so dead and so back](../sources/newsletters/npm-supply-chain-compromise-2026-08-05.md)
```

### wiki/history/state-of/cybersecurity.md (updated)

Prepend the spilled entry to the existing "## Archived from current page on 2026-09-07" block (above its current first entry):

```md
## Archived from current page on 2026-09-07

- [2026-07-09] Added Claude Fable 5 and GPT-5.6 Sol to the offensive frontier-model section; both carry the `cybersecurity` domain and neither had been listed. Softened the GPT-5.5 line to a point-in-time claim now that GPT-5.6 Sol has shipped.
- [2026-07-02] Cognition launched Devin Security Swarm, pushing AI-assisted vulnerability detection toward parallel agent workflows that validate exploitability and generate fix PRs.
- [2026-06-22] Gray Swan interview adds AI-native security framing: agents should be treated as untrusted systems; indirect prompt injection, identity, permissions, guardrails, and automated red teaming are core deployment concerns.
- [2026-05-23] Anthropic reported Project Glasswing and partners found 10,000+ high/critical-severity vulnerabilities in essential software within a month of launch; added as a program-wide figure to the Claude Mythos Preview entry (industry-adaptation framing attributed to AINews' recap).
```

(At apply time, if other proposals in this batch have already added entries to this page and pushed the cap further, the actual spilled entry may differ from the one shown here — apply the entry that is actually oldest on the live page at that time, per the rebase rules.)

### wiki/sources/newsletters/npm-supply-chain-compromise-2026-08-05.md (new)

```md
---
title: AINews — Megakernels are so dead and so back
type: source
source_type: newsletter
source_file: raw/newsletters/2026-08-05-ainews-megakernels-are-so-dead-and-so-back.md
url: https://www.latent.space/p/ainews-megakernels-are-so-dead-and
published: 2026-08-05
ingested: 2026-09-07
domains: [cybersecurity]
---

# AINews — Megakernels are so dead and so back

AINews recap covering an Inference Engineering Masterclass podcast segment on why hand-fused "megakernel" inference is a declining research direction, alongside the day's Twitter recap. The cybersecurity-relevant item: a compromised npm maintainer account was used to plant a `preinstall` credential-harvesting hook (npm, GitHub, AWS, Kubernetes, Vault credentials), which then propagated maintainer-to-maintainer, reaching 868 packages with 2B+ combined monthly installs by report time (via @IntCyberDigest). Used here only for that supply-chain item; the megakernel/inference-systems content was triaged separately and recommended skip.

## Influenced pages

- [state-of/cybersecurity](../../state-of/cybersecurity.md) — new npm preinstall-stealer campaign entry under AI developer supply chain attacks

## Key claims extracted

- npm supply-chain attack: compromised maintainer account, malicious `preinstall` hook
- Credentials harvested: npm, GitHub, AWS, Kubernetes, HashiCorp Vault
- Propagation: maintainer-to-maintainer, using stolen credentials to compromise further packages
- Scope at time of report: 868 npm packages, 2B+ combined monthly installs
- Source: @IntCyberDigest via AINews Twitter recap (secondary sourcing, no primary incident report reviewed)
```

## Open questions

- If a primary incident report or registry-side confirmation (npm Inc., Socket, Snyk, etc.) surfaces later, the entry may need updating with named packages, a timeline, or a revised scope figure.
