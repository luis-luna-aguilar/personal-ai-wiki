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
