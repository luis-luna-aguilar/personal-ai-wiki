---
type: proposal
source: raw/articles/2026-11-23-anthropiccom-threat-intelligence-report-september-2026.md
status: pending
created: 2026-11-24
---

# Proposal: Anthropic's September 2026 threat report — AI-run intrusion campaigns and seven labs distilling Claude

## Summary

### In short
Attackers of every size now hand whole intrusion campaigns to agents, so sophistication no longer tells investigators who is behind one. That is the core finding of Anthropic's September 2026 misuse report. The report also names seven China-based labs it caught distilling Claude through proxy "transfer stations". The proposal adds a short attacker-side section to **State of Cybersecurity**, a distillation subsection to **Model sovereignty**, one caveat line on **Kimi K3**, and a source page. The reason to hesitate is length: State of Cybersecurity would rise to about 117% of its ceiling.

[[#Open questions|Open questions: 1 to answer.]]

- [x] **Approve all** — checking this box approves every item in `## Intended changes` and `## Schema / vocabulary additions` below; the individual boxes may stay empty.

### The source
On 10 September 2026 Anthropic's Threat Intelligence team published "Detecting and countering misuse of AI: September 2026", its largest report so far. It covers operations Anthropic disrupted between December 2025 and August 2026 in seven harm areas: cyber operations, influence operations, surveillance, scams and fraud, biological misuse, conventional weapons, and illicit distillation (copying a model's abilities by training on its outputs without permission). All of the misuse ran on Haiku, Sonnet or Opus. None ran on Fable or the Mythos models, except one distillation attempt.

The cyber section argues that the agent-run attack Anthropic first saw in one suspected state campaign in November 2025 has spread to every kind of attacker: agents handle reconnaissance, exploitation and data theft while humans pick targets, and public frameworks such as PentAGI hand the scaffolding to anyone. The clearest case is GTG-20006, which Anthropic says is consistent with Midnight Blizzard. Driven by Claude Code skills, it ran phishing, hijacked hotel-WiFi DNS, took over WhatsApp accounts and stole drone-supply-chain data; when a security product flagged its malware, agents rebuilt it until it went undetected, shifting the cost back onto defenders. Criminal groups now treat AI API keys as loot in themselves. They find them by scraping code, containers and apps (one operator scanned 1.8 million Android APKs), run their own attacks on the victims' keys, and resell access through fake discount-Claude sites.

The distillation section names Alibaba, Moonshot, DeepSeek, Zhipu, Xiaomi, SenseTime and MiniMax. Alibaba ran the largest campaign Anthropic has measured: more than 151 million exchanges between May and July. Moonshot and DeepSeek quietly relayed their own customers' requests to Claude Opus and kept the reasoning, which exposed those customers' data. The report also has five biology case studies, which Anthropic calls the first such evidence any company has published.

### What changes
State of Cybersecurity covers attack surfaces, supply-chain attacks, offensive model capability and misbehaving agents, but says nothing about threat actors using AI to run campaigns. Model sovereignty records distillation only as the July accusation by Michael Kratsios, the US Tech & Science Advisor, against Moonshot.

- **State of Cybersecurity** gains a four-bullet "AI-enabled threat actors" section: autonomous kill chains across all actor classes, agents that re-tool malware when it is detected, the criminal market in AI API keys, and a pointer for distillation. The new Recent-changes entry dated 10 September is older than everything in the full list, so it goes straight to history. The page date stays 23 November.
- **Model sovereignty** gains a subsection on Anthropic's seven-lab disclosure: how the proxy networks work, the largest campaigns, and the countermeasures. It notes that the first lab-side evidence against Moonshot concerns Opus, not Fable. Page date moves to 10 September.
- **Kimi K3** gains one sentence in its distillation caveat. Page date moves to 10 September.
- `wiki/index.md` refreshes the Model sovereignty and Kimi K3 lines.
- One new source page for the report.

### What to weigh
Scope is the main choice. The drafts leave out the influence, surveillance, weapons, scams and biology sections because they fall outside the cybersecurity and model pages. The biology cases could later go to AI in biology if you want them. The publication date of 10 September is taken from the triage because the fetched page shows no date. With the new section, State of Cybersecurity sits at about 117% of its ceiling. That is a split candidate, but it is not required.

## Intended changes

- [ ] **Update** `wiki/state-of/cybersecurity.md` — add `### AI-enabled threat actors` subsection after "AI developer supply chain attacks"; add `anthropic-threat-report-sep-2026` to `sources:` and body `## Sources`; `as_of` stays 2026-11-23; adds one Recent-changes entry dated 2026-09-10
- [ ] **Spill** `wiki/state-of/cybersecurity.md` → `wiki/history/state-of/cybersecurity.md` — the list is at its cap of 10 and the new 2026-09-10 entry is the oldest by date, so it goes straight to history; the live list is unchanged
- [ ] **Update** `wiki/trends/model-sovereignty.md` — new `###` subsection on Anthropic's seven-lab distillation disclosure; `Current signal (as of …)` and `as_of` → 2026-09-10; add one Recent-changes entry dated 2026-09-10; add source to `sources:` and `## Sources`
- [ ] **Update** `wiki/models/kimi-k3.md` — one sentence appended to the distillation caveat; `as_of` → 2026-09-10; add one Recent-changes entry dated 2026-09-10; add source
- [ ] **Update** `wiki/index.md` — refresh the `trends/model-sovereignty` and `models/kimi-k3` lines
- [ ] **Create** `wiki/sources/articles/anthropic-threat-report-sep-2026.md` — source summary

## Page drafts

### wiki/state-of/cybersecurity.md (updated)

Frontmatter: append `anthropic-threat-report-sep-2026` to `sources:`. `as_of` unchanged (2026-11-23).

New subsection, inserted after the `**Mitigations**` block that closes "AI developer supply chain attacks" and before `### AI-assisted vulnerability detection`:

```
### AI-enabled threat actors

How attackers themselves use AI, as distinct from attacks on AI tooling (above) and from agents misbehaving on their own (below).

- **Autonomous kill chains across every actor class** — in Anthropic's September 2026 misuse report, most disrupted cyber operations ran through multi-agent frameworks (recon, exploitation, exfiltration) with humans picking targets; public frameworks like PentAGI give anyone the scaffolding, so sophistication no longer identifies the attacker *(as of 2026-09-10)*
- **Malware that re-tools itself on detection** — GTG-20006 (consistent with Midnight Blizzard) ran phishing, hotel-WiFi DNS hijacking and WhatsApp takeovers through Claude Code skills; when security products flagged its implants, agents rebuilt them until undetected *(as of 2026-09-10)*
- **A criminal market in AI API keys** — keys are farmed from code, containers and apps (one operator scanned 1.8M Android APKs), used to run attacks on the victim's account, and resold through fake discount-Claude sites *(as of 2026-09-10)*
- **Illicit distillation** — seven China-based labs distilled Claude through proxy "transfer stations"; detail on [Model sovereignty](../trends/model-sovereignty.md) *(as of 2026-09-10)*
```

`## Recent changes`: adds one entry dated 2026-09-10 (below). It is the oldest-dated of eleven, so it spills straight to history and the live list keeps its current ten entries.

```
- [2026-09-10] Added "AI-enabled threat actors" from Anthropic's September 2026 misuse report: autonomous kill chains across actor classes, GTG-20006's self-re-tooling malware, the criminal AI-key market, and a pointer to the seven-lab distillation disclosure.
```

`## Sources`: append

```
- [Anthropic — Detecting and countering misuse of AI: September 2026](../sources/articles/anthropic-threat-report-sep-2026.md)
```

### wiki/history/state-of/cybersecurity.md (updated)

Append at the end of the file:

```
## Archived from current page on <apply date>

- [2026-09-10] Added "AI-enabled threat actors" from Anthropic's September 2026 misuse report: autonomous kill chains across actor classes, GTG-20006's self-re-tooling malware, the criminal AI-key market, and a pointer to the seven-lab distillation disclosure.
```

### wiki/trends/model-sovereignty.md (updated)

Frontmatter: `as_of: 2026-09-10`; append `anthropic-threat-report-sep-2026` to `sources:`.

Heading change: `## Current signal (as of 2026-07-29)` → `## Current signal (as of 2026-09-10)`.

New subsection, inserted after `### A named sanctions target: Moonshot and Kimi K3` and before `### The industry response: NVIDIA's Open Secure AI Alliance`:

```
### Anthropic names seven labs distilling Claude

Anthropic's 2026-09-10 misuse report says it has disrupted distillation campaigns from seven China-based labs since February: Alibaba (Qwen), Moonshot, DeepSeek, Zhipu (Z.ai), Xiaomi, SenseTime and MiniMax. All of them targeted generally available models, not Mythos. Access ran through proxy "transfer stations", networks of thousands of accounts opened with false identities, stolen cards and stolen API keys. Some proxies also log and resell users' transcripts, and MiniMax ran its own proxy through a shell company. Alibaba's campaign was the largest Anthropic has measured: more than 151M exchanges from May to July, peaking near 3M a day from over 3,500 accounts. Moonshot and DeepSeek silently relayed their own customers' requests to Claude Opus and harvested the reasoning, which exposed those customers' data. Zhipu abandoned Fable for Opus 4.6 because Fable's cyber safeguards were stronger. Anthropic's countermeasures are to attribute proxy networks to an organization instead of banning accounts one by one, to run extraction classifiers, to summarize Claude's reasoning, to use Fable 5.1's "preserved thinking", and to require identity checks for suspected resale or use from unsupported countries. For the Kratsios accusation above, this is the first lab-side evidence that Moonshot distilled Claude, but it concerns Opus (over 23M exchanges, May–July), not Fable.
```

`## Recent changes`: adds one entry dated 2026-09-10, inserted in date order (newest first) between the 2026-10-19 and 2026-07-29 entries:

```
- [2026-09-10] Anthropic disclosed distillation campaigns by seven China-based labs (Alibaba, Moonshot, DeepSeek, Zhipu, Xiaomi, SenseTime, MiniMax) run through proxy "transfer stations"; Moonshot's campaign targeted Opus, not Fable.
```

`## Sources`: append

```
- [Anthropic — Detecting and countering misuse of AI: September 2026](../sources/articles/anthropic-threat-report-sep-2026.md)
```

### wiki/models/kimi-k3.md (updated)

Frontmatter: `as_of: 2026-09-10`; append `anthropic-threat-report-sep-2026` to `sources:`.

`## Caveats`, the "Disputed:" bullet, with one sentence appended at the end:

```
- Disputed: US Tech & Science Advisor Michael Kratsios accused Moonshot of "large-scale, covert industrial distillation" of Anthropic's Fable, citing GB300 chip access in Thailand; Treasury has signaled possible Entity List sanctions. Technical critics note only ~15 days separated Fable's release from K3's announcement, making full distillation-driven capability transfer implausible on that timeline — unresolved as of this writing. Anthropic's September 2026 misuse report later attributed over 23M distillation exchanges (May–July 2026) to Moonshot, mostly against Opus rather than Fable, including customer requests Moonshot silently relayed to Claude; see [Model sovereignty](../trends/model-sovereignty.md).
```

`## Recent changes`: adds one entry dated 2026-09-10 at the top:

```
- [2026-09-10] Anthropic's misuse report attributes 23M+ Claude distillation exchanges to Moonshot (May–July), mostly against Opus, and says Moonshot silently relayed customer requests to Claude
```

`## Sources`: append

```
- [Anthropic — Detecting and countering misuse of AI: September 2026](../sources/articles/anthropic-threat-report-sep-2026.md)
```

### wiki/index.md (updated)

```
- [models/kimi-k3](models/kimi-k3.md) — Moonshot AI's 2.8T flagship; Intelligence Index 57; #1 Frontend Code Arena; supersedes Kimi K2.7-Code; disputed distillation (Kratsios accusation, Anthropic's 23M-exchange attribution against Opus) *(as_of: 2026-09-10)*
- [trends/model-sovereignty](trends/model-sovereignty.md) — not being architecturally dependent on any single frontier model: the Fable 5 ban as trigger, open weights as escape hatch, US pressure on Chinese open models, the Kratsios/Moonshot distillation accusation, Anthropic's seven-lab distillation disclosure, and NVIDIA's Open Secure AI Alliance *(as_of: 2026-09-10)*
```

### wiki/sources/articles/anthropic-threat-report-sep-2026.md (new)

```
---
title: 'Anthropic — Detecting and countering misuse of AI: September 2026'
type: source
source_type: article
source_file: raw/articles/2026-11-23-anthropiccom-threat-intelligence-report-september-2026.md
url: https://www.anthropic.com/threat-intelligence-report-september-2026
published: 2026-09-10
ingested: 2026-11-24
domains: [cybersecurity, models]
---

# Anthropic — Detecting and countering misuse of AI: September 2026

Anthropic's largest threat-intelligence report covers operations it disrupted between December 2025 and August 2026 in seven harm areas: cyber operations, influence operations, surveillance, scams and fraud, biological misuse, conventional weapons and illicit distillation. Its cyber argument is that AI-orchestrated attacks have spread from one suspected state campaign to every class of actor, so sophistication no longer identifies the attacker, and that agents now rebuild malware when it is detected, shifting cost back to defenders. The distillation section names seven China-based labs and describes the proxy "transfer station" networks they used. Most of the page is IOC tables. The five biology case studies are, per Anthropic, the first such evidence a company has published.

## Influenced pages
- [State of Cybersecurity](../../state-of/cybersecurity.md) — new "AI-enabled threat actors" section
- [Model sovereignty](../../trends/model-sovereignty.md) — new subsection on the seven-lab distillation disclosure
- [Kimi K3](../../models/kimi-k3.md) — distillation caveat extended

## Key claims extracted
- Covers December 2025–August 2026; all misuse used Claude Haiku, Sonnet or Opus, none Fable or Mythos, except one distillation case
- The November 2025 autonomous-attack operating model has spread to every class of actor; public offensive-agent frameworks such as PentAGI reproduce the scaffolding; most operations used AI via direct execution or multi-agent orchestration, with humans setting targets and reviewing exfiltration
- GTG-20006 (consistent with Midnight Blizzard) automated development, infrastructure, phishing, command-and-control and exfiltration through Claude Code skills; targeted 20+ organizations (Ukraine, Europe, drone supply chains); compromised hotel-WiFi vendors for DNS hijacking; took over WhatsApp accounts; agents rebuilt malware until undetected
- Suspected ShinyHunters affiliates ran opportunistic mass scanning; one operator downloaded 1.8M Android APKs and scanned them for hardcoded secrets
- A criminal AI supply chain farms and validates stolen AI API keys and session tokens, runs attacks on victims' keys, and resells access through fake AI-reseller sites; some actors targeted AI vendors and evaluation sandboxes for production keys
- Five biology case studies, described as the first evidence of real-world biological misuse a company has published
- Illicit distillation since February 2026 by seven China-based labs (Alibaba, Moonshot, DeepSeek, Zhipu, Xiaomi, SenseTime, MiniMax) via proxy "transfer stations" using false identities, stolen cards and stolen API keys; Alibaba 151M+ exchanges May–July (peak ~3M/day, 3,500+ accounts); Moonshot 23M+; DeepSeek 12.1M+ over 14 days; Zhipu 3.4M+ over 17 days; Xiaomi 400K+
- Moonshot and DeepSeek silently relayed customer requests to Claude Opus and harvested reasoning via cross-session replay of "thinking signatures"; Zhipu switched from Fable to Opus 4.6 because Fable's cyber safeguards were stronger; MiniMax ran a proxy service through a shell company
- Countermeasures: proxy-network attribution, extraction classifiers, summarized reasoning, Fable 5.1 preserved thinking, identity verification for suspected resale or unsupported-country use
```

## Schema / vocabulary additions

None.

## Open questions
- With the new section, State of Cybersecurity's body grows from about 2,160 to about 2,340 words, roughly 117% of the 2,000-word state-of ceiling. That makes it a split candidate, though the split is not required. One natural split is to move "Agentic misalignment incidents" and "Agents acting in the wild" onto [Agent incidents in the wild](../wiki/trends/agent-incidents-in-the-wild.md) and leave a one-paragraph pointer. Split now, as a separate refactor, or leave it?
	- Before i already agreed on split
