---
title: State of Cybersecurity
type: state-of
domains: [cybersecurity]
tags: []
as_of: 2026-11-23
sources: [slopcop-repo, glasswing, openai-gpt-5-5-launch, ai-security-scanners-2026-05-01, agentic-security-tooling-2026-05-13, openai-daybreak-2026-05-13, cloudflare-glasswing-2026-05, the-code-devin-security-2026-07-02, ainews-not-much-happened-2026-07-02, gray-swan-ai-security-2026-06, devinai-blog-agentic-map-reduce, anthropic-glasswing-10k-vulnerabilities, ainews-gpt-56-launch-benchmarks-2026-07-10, openais-new-model-for-cyber-attacks-2026-07-16, ainews-china-policy-openweight-2026-07-21, ainews-cybersecurity-top-of-mind-2026-07-22, ainews-fearing-rsi-pacing-letter-2026-07-29, ainews-not-much-happened-2026-08-01, zawinskis-law-multiagents-2026-08-08, anthropic-riemann-hypothesis-2026-08-11, agents-find-a-way-2026-08-12, unsloth-desktop-chatgpt-linux-2026-08-12, ainews-openai-agi-bar-2026-08-28, ainews-openai-shuts-off-cursor-2026-08-29, cloudflare-vulnerability-discovery-remediation-2026-09, claude-security-product-page, ainews-opencode-attack-oss-scanner-2026-10-20, ainews-transluce-field-reports-2026-10-17, ainews-gemini-4-argon-launch-2026-10-01, ainews-argon-fairwind-rollout-2026-10-10, ainews-devday-agent-safety-roundup-2026-09-30, openai-introducing-gpt-6-2-astra-sol, openai-cisco-shirudo, openai-cybersecurity-solutions-page, anthropic-attack-surface-reduction-2026-10-20, anthropic-formal-verification-2026-10-22, anthropic-threat-report-sep-2026, anthropic-claude-fable-mythos-5-2, google-introducing-gemini-4-carbon, google-introducing-gemini-4-neon, openai-patch-the-planet-php2shell, ainews-php2shell-patch-the-planet-2026-10-22]
---

# State of Cybersecurity

Current state of AI applied to cybersecurity: AI-specific attack surfaces, vulnerability detection, and security tooling for development workflows.

## Subcategories

### AI-specific attack surfaces

Attack vectors unique to or amplified by AI systems in development workflows.

- **Indirect prompt injection** — tool-using agents fetch untrusted content while holding private context and action authority, a new exploit class for systems like Codex, Claude Code, OpenClaw, and computer-use agents. See [Prompt injection](../concepts/prompt-injection.md). *(as of 2026-06-22)*
- **Slopsquatting** — LLMs hallucinate ~20% of package names (USENIX Security 2025, 576k samples); attackers pre-register those names on PyPI/npm with malicious `postinstall` payloads. Mitigation: `slopcop` CLI checks registry age, download count, postinstall scripts, and Levenshtein distance before install. See [Slopsquatting](../concepts/slopsquatting.md). *(as of 2026-04-22)*
- **Coding-agent local-data upload** — [Grok Build](../tools/grok-build.md)'s CLI agent was caught uploading entire local directories, including SSH keys, to xAI's servers; a different failure mode from indirect prompt injection, since the risk is the agent's own default behavior, not injected instructions *(as of 2026-07-16)*
- **Reasoning-trace leakage** — encrypted/signed chain-of-thought from Claude, GPT, and Gemini APIs can be decoded and replayed onto a different model, session, or user, exposing secrets hidden inside reasoning blocks that never appear in the visible transcript. See [Reasoning trace leakage](../concepts/reasoning-trace-leakage.md). *(as of 2026-08-12)*

### AI developer supply chain attacks

Coordinated attacks on the packages, editor extensions and deployment platforms AI developers depend on (Mini Shai-Hulud, the Hugging Face `transformers` impersonator, GitHub's VS Code extension breach, the npm preinstall stealer, Railway's environment-variable breach) and their mitigations are tracked on [AI developer supply chain attacks](../trends/ai-developer-supply-chain-attacks.md) *(as of 2026-10-21)*.

### AI-enabled threat actors

How attackers themselves use AI, as distinct from attacks on AI tooling (above) and from agents misbehaving on their own (below).

- **Autonomous kill chains across every actor class** — in Anthropic's September 2026 misuse report, most disrupted cyber operations ran through multi-agent frameworks (recon, exploitation, exfiltration) with humans picking targets; public frameworks like PentAGI give anyone the scaffolding, so sophistication no longer identifies the attacker *(as of 2026-09-10)*
- **Malware that re-tools itself on detection** — GTG-20006 (consistent with Midnight Blizzard) ran phishing, hotel-WiFi DNS hijacking and WhatsApp takeovers through Claude Code skills; when security products flagged its implants, agents rebuilt them until undetected *(as of 2026-09-10)*
- **A criminal market in AI API keys** — keys are farmed from code, containers and apps (one operator scanned 1.8M Android APKs), used to run attacks on the victim's account, and resold through fake discount-Claude sites *(as of 2026-09-10)*
- **Illicit distillation** — seven China-based labs distilled Claude through proxy "transfer stations"; detail on [Model sovereignty](../trends/model-sovereignty.md) *(as of 2026-09-10)*

### AI-assisted vulnerability detection

Coding agents extended into security review and vulnerability validation.

- [Codex](../tools/codex.md) — OpenAI; Codex Security now spans a CLI, CI scans, a TypeScript SDK and PR review, plus the Daybreak plugin (local scans and patches in Codex) and Daybreak Defense Factory (remote scan-to-patch runs), framed as a discover, validate, prioritize, assign, patch and verify loop *(as of 2026-11-23)*
- **Claude Security** — Anthropic; public beta for Claude Enterprise, scanning with Anthropic's most capable models, now including Claude Mythos 5.2, self-verifying findings and proposing patches; Claude Code plugin in beta — details on [Claude Code](../tools/claude-code.md) *(as of 2026-11-09)*
- **Anthropic OSS Scanner** — Anthropic; free periodic vulnerability scans of critical open-source projects, delivered with proofs of concept and patches; the first week reported 77 critical and 803 high model-rated findings, including a fix in curl *(as of 2026-10-20)*
- **Attack-surface reduction** — Anthropic; Claude maps reachable code and gates what a deployment does not need, lowering the severity of bugs nobody has found. Across 25 projects (5M+ lines) it found 493 issues, including 93 unnecessary pre-auth surfaces and 94 setting combinations that silently turn a security control off *(as of 2026-10-20)*
- **OpenSSH case** — ~4,500 lines of experimental ML-DSA-44 code were reachable before authentication even when disabled; the fix (OpenSSH 10.6) checks key types before parsing and removed about a fifth of the pre-auth reachable code. The three-pass skill is being folded into OSS Scanner *(as of 2026-10-20)*
- **Formal verification at scale** — Anthropic and Theorem had Claude prove 239 OSS-Fuzz entry points in 123 libraries crash-free on RISC-V builds; detail and limits on [AI formal verification](../trends/ai-formal-verification.md) *(as of 2026-10-22)*
- **Cursor Security Review** — Cursor; reported always-on PR review plus scheduled codebase scans; source is AINews secondary coverage *(as of 2026-05-01)*
- **Vercel DeepSec** — secondary May 2026 coverage describes security scanning/review for agent-built applications; pending primary verification *(as of 2026-05-04)*
- [Devin](../tools/devin.md) — Cognition; Security Swarm now documented as Agentic MapReduce, benchmarked at 72% recall on a CVE-pinned ground-truth set vs. rival scanners *(as of 2026-07-14)*

The category is shifting from one-off scanners toward agent-compatible security loops: vulnerability monitoring, fix validation, supply-chain checks, and deployment-risk review inside coding-agent workflows.

### AI security tooling

- **Gray Swan** — AI-native security company focused on adversarial testing and guardrails for models and agents. Its Shade automated red-teaming system is described as finding more breaks than human red teamers in fixed windows; Cygnal is positioned as a guardrail model for policy enforcement. Current source is Latent Space interview coverage. *(as of 2026-06-22)*
- **GPT-Red** — OpenAI; a model purpose-built to craft prompt-injection attacks hidden in emails, webpages, and tool outputs, used in-house to surface and patch vulnerabilities before a model ships. GPT-5.6 was trained against GPT-Red's attacks and now falls for only 0.05% of them, per OpenAI via secondary newsletter coverage. *(as of 2026-07-16)*
- [OpenAI Privacy Filter](../models/openai-privacy-filter.md) — OpenAI; open-weight (Apache 2.0) PII redaction model, small enough to run on-device before data reaches cloud AI *(as of 2026-04-23)*
- **Sakana Fugu-Cyber** — Sakana AI; update to its orchestration-style security model, claimed state-of-the-art on real-world security benchmarks, matching cyber-focused frontier systems like GPT-5.5-Cyber and Claude Mythos Preview; vendor-claimed, no independent verification named. *(as of 2026-07-22)*
- **Gemini 3.5 Flash Cyber** — Google; specialized model used inside CodeMender, called up to 5x per task with outputs aggregated; found 55 confirmed vulnerabilities in V8 vs. 47 for general-purpose Gemini 3.5 Flash and 36 for Claude Opus 4.6 run the same way — an example of specialization plus repeated attempts outperforming raw model scale. *(as of 2026-07-22)*
- [NVIDIA OpenShell](../tools/nvidia-openshell.md) — open-source sandbox that enforces runtime limits on local and open agents instead of relying on prompt rules; 100+ firms joined the surrounding safety platform, OpenAI did not; telemetry is on by default (opt-out) *(as of 2026-09-30)*
- [Shirudo](../tools/shirudo.md) — OpenAI and Cisco; open-source runtime that deploys signed eBPF "shields" on running Linux systems to block a vulnerable code path until the patch lands, no restart needed; a Codex-generated shield blocked a Java4Shell exploit on live Elasticsearch in a controlled test *(as of 2026-11-23)*

**Cloudflare Project Glasswing harness (May 2026):** Cloudflare's eight-stage harness around Mythos Preview for large-scale repo security research: recon, ~50 concurrent narrow-scope hunters, adversarial validation, gapfill, dedupe, reachability trace, feedback and report. Stage table on [Claude Mythos Preview](../models/claude-mythos-preview.md); design lessons on [Multi-agent coordination](../workflows/multi-agent-coordination.md).

**Productized as Vulnerability Discovery and Remediation (September 2026):** Cloudflare shipped the harness as an early-access, invitation-only service under Cloudflare Managed Defense, running OpenAI Daybreak's GPT-5.6 Cyber for reconnaissance, hunting, and validation against a customer's authorized codebase. New over the research harness is production context: findings are matched against live traffic, security events, and existing WAF rules (via Web Assets and Workers Observability) to become evidence-backed priorities, and validated proposals surface as a code patch plus a scoped WAF Custom rule for human review. No model inference runs at Cloudflare's edge; the model only proposes changes, never applies them.

### Frontier model capabilities (offensive)

Frontier models operating above public tiers, deployed selectively for cybersecurity research.

- [Claude Mythos Preview](../models/claude-mythos-preview.md) — Anthropic; restricted preview; autonomously found thousands of zero-days via exploit chain construction; Cloudflare's Project Glasswing and partners found 10,000+ high/critical-severity vulnerabilities within a month of launch *(as of 2026-05-23)*
- [Claude Fable 5.2 / Mythos 5.2](../models/claude-fable-5-2.md) — Anthropic; one model, two safeguard levels; Mythos 5.2 is its strongest cyber model (+10.2% CVE Rediscovery vs Opus 5.5) for vetted Cyber Verification Program members; Fable 5.2 blocks most cyber tasks. Supersedes [Fable 5](../history/models/claude-fable-5.md) and [5.1](../history/models/claude-fable-5-1.md) *(as of 2026-11-09)*
- [GPT-5.6 Sol](../history/models/gpt-5-6-sol.md) — OpenAI; "most capable model yet" for cybersecurity per OpenAI, competitive with Claude Mythos Preview on ExploitBench at about 1/3 the output tokens; does not cross the Cyber Critical threshold under OpenAI's Preparedness Framework; superseded 2026-09-22 by GPT-6 Sol, now [GPT-6.2 Sol](../models/gpt-6-2-sol.md) *(as of 2026-07-10)*
- [GPT-5.5](../models/gpt-5-5.md) — OpenAI; CyberGym 81.8% in its own launch comparison table, above GPT-5.4 and Claude Opus 4.7 among publicly available models at the time of its April 2026 launch; publicly deployed with tighter safeguards rather than restricted-access-only release *(as of 2026-04-23)*
- [GPT-6.2 Astra](../models/gpt-6-2-astra.md) and [GPT-6.2 Sol](../models/gpt-6-2-sol.md) — OpenAI; both meet the Preparedness Framework's Critical cyber threshold, as [GPT-6 Astra](../history/models/gpt-6-astra.md) did; better at finding, exploiting and patching vulnerabilities; shipped publicly with tighter safeguards *(as of 2026-11-23)*
- **Open-weight gap** — Epoch estimates open-weight cyber capability trails the closed frontier by 6–7 months; [GLM-5.3](../models/glm-5-3.md) scores 160 on Epoch's Cyber ECI, above GPT-5.4 *(as of 2026-10-17)*
- [GLM-5.3](../models/glm-5-3.md) — Z.ai, open weights; Anthropic's report says it built end-to-end V8 exploits on ExploitBench in 50/410 attempts vs. Claude Mythos Preview's 56/410, and that abliteration (removing refusals) cost ~$4.4K and cut refusals from >90% to ~3% *(as of 2026-09-30)*

### Trusted defensive access

Provider programs that expand access to higher-risk cyber capabilities for verified defenders rather than to the general public.

- **OpenAI Trusted Access for Cyber** — verified defenders protecting critical infrastructure can apply for broader GPT-5.5 cyber capability access with fewer restrictions *(as of 2026-04-23)*
- **OpenAI Daybreak** — OpenAI's approved-access program for cyber work, in two tiers: **Blue**, defensive work with fewer refusals (GPT-6 Sol, GPT-6 Astra alpha), and **Red**, specialized cyber models (GPT-6 Cyber) for authorized exploit work behind extra verification; GPT-6.2 promised; see [OpenAI frontier gating](../trends/openai-frontier-gating.md) *(as of 2026-11-23)*
- **Google Fairwind Program** — Google's vetted-defender access for Gemini 4: [Argon](../models/gemini-4-argon.md) first (2026-09-30, GA 2026-10-13), [Carbon](../models/gemini-4-carbon.md) from 2026-10-28 (SEC-bench Pro 88.2%), a cyber variant of [Neon](../models/gemini-4-neon.md) since 2026-11-18 *(as of 2026-11-18)*
- **Daybreak for Frontline Defenders** — OpenAI's $1B commitment of subsidized Daybreak access for organizations with limited security resources that protect essential services; PHP2Shell (below) was found through the related Patch the Planet initiative *(as of 2026-10-21)*

### Agent incidents

Models and deployed agents acting outside their boundaries on their own initiative, as opposed to the external attackers above: eval-time incidents (OpenAI–Hugging Face, Mythos 5 in UK AISI testing), real-use incidents (Services Australia, OpenCode's agent-swarm attack, the first rogue agent fleet, Transluce's field reports) and the containment tools built in response (Perplexity SPACE, Microsoft Project Perception) are tracked on [Agent incidents in the wild](../trends/agent-incidents-in-the-wild.md) *(as of 2026-10-26)*.

### Coordinated cyber-defense initiatives

- **OpenAI-led cyber-defense coalition (August 2026)** — OpenAI published an open letter co-signed by 116 organizations, including Anthropic, AWS, Google, Microsoft, and Oracle, calling for a coordinated industry surge against AI-enabled cyberattacks. One of the clearest cross-industry coordination moves tracked on this page to date. *(as of 2026-08-28)*
- **PHP2Shell (October 2026)** — two memory-corruption flaws in PHP's engine (CVE-2026-109618/109619) allowed pre-auth RCE on WordPress, Drupal and Joomla; found independently by Calif with GPT-5.6 Sol under OpenAI's Patch the Planet initiative and by Wiz (Google Cloud), which credits Gemini 4 Argon *(as of 2026-10-21)*
- **Patch the Planet response** — OpenAI led two months of remediation with PHP's maintainers, security providers and US agencies before the 2026-10-21 patch; Cloudflare shipped free WAF rules ahead of it and the NSA advised taking unpatchable systems offline. OpenAI calls it a "Defender's Window" case and proposes a five-stage response framework *(as of 2026-10-21)*

## Recent changes

- [2026-11-24] Split: "AI developer supply chain attacks" (campaign write-ups, the Railway breach and mitigations) moved to [AI developer supply chain attacks](../trends/ai-developer-supply-chain-attacks.md), leaving a one-paragraph pointer.
- [2026-11-24] Split: "Agentic misalignment incidents" and "Agents acting in the wild" moved to [Agent incidents in the wild](../trends/agent-incidents-in-the-wild.md), leaving a one-paragraph pointer under "Agent incidents".
- [2026-11-23] OpenAI's cybersecurity solutions page defines Daybreak's two access tiers (Blue for defensive work, Red for authorized offensive research) and lists the Codex Security surfaces (CLI, CI, SDK, PR review, Daybreak plugin, Defense Factory); Daybreak and Codex lines refreshed, OpenCode line's "undefined" note resolved.
- [2026-11-23] OpenAI and Cisco open-sourced Shirudo, an eBPF runtime that shields running Linux services from a known exploit while the patch is prepared; added to AI security tooling.
- [2026-11-23] GPT-6.2 Astra and Sol replace the pre-launch GPT-6 Astra line: both meet OpenAI's Critical cyber threshold and shipped publicly with tighter safeguards, while Daybreak still serves GPT-6-generation models.
- [2026-11-09] Claude Fable 5.2 / Mythos 5.2 replace the Fable 5 line under offensive capabilities: Mythos 5.2 finds 10.2% more vulnerabilities than Opus 5.5 on Anthropic's CVE Rediscovery eval and now powers Claude Security; Fable 5.2 makes about 60% fewer unnecessary cyber blocks than 5.1.
- [2026-10-28] Fairwind Program extended to Gemini 4 Carbon (defenders first, SEC-bench Pro 88.2%) and, from 2026-11-18, a cyber variant of Gemini 4 Neon.
- [2026-10-22] Anthropic and Theorem used Claude to formally verify 239 OSS-Fuzz entry points across 123 libraries (no crash on any input up to 64 MB, RISC-V builds), finding bugs fuzzers miss; one-line pointer under AI-assisted vulnerability detection, detail on the new [AI formal verification](../trends/ai-formal-verification.md) page.
- [2026-10-21] PHP2Shell: two PHP-engine flaws with pre-auth RCE on major CMSs, found independently via GPT-5.6 Sol (Calif, Patch the Planet) and Gemini 4 Argon (Wiz), disclosed after two months of OpenAI-coordinated remediation; Daybreak for Frontline Defenders ($1B subsidy) added to trusted access.
- [2026-10-20] Anthropic OSS Scanner added to vulnerability detection (77 critical / 803 high findings in week one, including curl).

## Sources

- [Gray Swan on AI-native security and prompt injection](../sources/newsletters/gray-swan-ai-security-2026-06.md)
- [Anthropic on X — Project Glasswing finds 10,000+ vulnerabilities](../sources/tweets/anthropic-glasswing-10k-vulnerabilities.md)
- [The Code — OpenAI's new model for cyber attacks (Grok Build open-source segment)](../sources/newsletters/openais-new-model-for-cyber-attacks-2026-07-16.md)
- [AINews — Open-weight competition, Chinese model policy, and the new geopolitics of AI (sandbox-escape recap segment)](../sources/newsletters/ainews-china-policy-openweight-2026-07-21.md)
- [AINews — AI Cybersecurity becomes top of mind](../sources/newsletters/ainews-cybersecurity-top-of-mind-2026-07-22.md)
- [AINews — Fearing RSI: OpenAI, Anthropic, GDM, Meta cosign letter to "pace" AI development](../sources/newsletters/ainews-fearing-rsi-pacing-letter-2026-07-29.md)
- [AINews — not much happened today](../sources/newsletters/ainews-not-much-happened-2026-08-01.md)
- [AINews — Zawinski's Law of MultiAgents](../sources/newsletters/zawinskis-law-multiagents-2026-08-08.md)
- [AINews — Anthropic's Riemann Hypothesis bound improvement](../sources/newsletters/anthropic-riemann-hypothesis-2026-08-11.md)
- ["Agents Find a Way" — Every newsletter](../sources/newsletters/agents-find-a-way-2026-08-12.md)
- [AINews — How to Steal a Reasoning Trace](../sources/newsletters/unsloth-desktop-chatgpt-linux-2026-08-12.md)
- [AINews — OpenAI to reach AGI bar by end-2026](../sources/newsletters/ainews-openai-agi-bar-2026-08-28.md)
- [AINews — OpenAI shuts off Cursor](../sources/newsletters/ainews-openai-shuts-off-cursor-2026-08-29.md)
- [Claude Security product page](../sources/articles/claude-security-product-page.md)
- [AINews — OpenCode agent-swarm attack and Anthropic OSS Scanner](../sources/newsletters/ainews-opencode-attack-oss-scanner-2026-10-20.md)
- [AINews — Transluce field reports and Epoch's cyber gap](../sources/newsletters/ainews-transluce-field-reports-2026-10-17.md)
- [AINews — Gemini 4 Argon launch](../sources/newsletters/ainews-gemini-4-argon-launch-2026-10-01.md)
- [AINews — Argon Fairwind rollout](../sources/newsletters/ainews-argon-fairwind-rollout-2026-10-10.md)
- [AINews — DevDay week agent-safety roundup](../sources/newsletters/ainews-devday-agent-safety-roundup-2026-09-30.md)
- [OpenAI and Cisco introduce Shirudo](../sources/articles/openai-cisco-shirudo.md)
- [OpenAI — AI for Cybersecurity Teams solutions page](../sources/articles/openai-cybersecurity-solutions-page.md)
- [Anthropic — Using Claude to reduce the attack surface of code](../sources/articles/anthropic-attack-surface-reduction-2026-10-20.md)
- [Anthropic — LLMs are making formal software verification feasible at a much larger scale](../sources/articles/anthropic-formal-verification-2026-10-22.md)
- [Anthropic — Detecting and countering misuse of AI: September 2026](../sources/articles/anthropic-threat-report-sep-2026.md)
- [Anthropic — Introducing Claude Fable 5.2 and Claude Mythos 5.2](../sources/articles/anthropic-claude-fable-mythos-5-2.md)
- [OpenAI — Patch the Planet: global response coordination as agents uncover critical vulnerabilities](../sources/articles/openai-patch-the-planet-php2shell.md)
- [AINews — PHP2Shell chronology and Patch the Planet](../sources/newsletters/ainews-php2shell-patch-the-planet-2026-10-22.md)
