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
