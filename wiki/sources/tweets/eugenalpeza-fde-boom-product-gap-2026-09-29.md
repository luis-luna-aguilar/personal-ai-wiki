---
title: Eugen Alpeza on X — The FDE boom is a product gap
type: source
source_type: tweet
source_file: raw/tweets/2026-10-26-eugenalpeza-2104936003282546913.md
url: https://x.com/EugenAlpeza/status/2104936003282546913
published: 2026-09-29
ingested: 2026-10-26
domains: [agents]
---

# Eugen Alpeza on X — The FDE boom is a product gap

X Article (464K views) by Eugen Alpeza, co-founder and CEO of Edra and former co-lead of forward-deployed AI engineering at Palantir. Argues that FDE demand is a product gap: the FDE's job is translating operators' judgment into agent instructions, and context graphs of company history don't replace it because history mixes mistakes with legitimate undocumented practice. Proposes ContextOps (turning operational evidence and expert judgment into tested, approved, versioned instructions and keeping them current), executable coverage as the metric, and an escalation → resolution → procedure-update learning loop; rejects fine-tuning on company history. Illustrated with a telecom supply-chain engagement. Edra builds a "GitHub for operators" for this workflow.

## Influenced pages
- [Forward-deployed engineering](../../training/forward-deployed-engineering.md) — new "The product-gap argument" section and Current-status bullet
- [Knowledge term map](../../concepts/knowledge-term-map.md) — "ContextOps" mapped to the Knowledge layer as a maintenance practice (row added to the Knowledge architectures hub, then moved here in the 2026-11-23 split)
- [Knowledge layer](../../concepts/knowledge-layer.md) — operating-rules layer gains a named discipline

## Key claims extracted
- Enterprises hire FDEs because agents don't know how the company operates and operators can't easily teach them
- A context graph of company records is more scalable but insufficient: it records both mistakes and legitimate exceptions
- Telecom example: an equipment-replacement voltage rule with exceptions that were partly non-compliance and partly legitimate regional practice
- AI lowers the cost of building and maintaining an agent-friendly procedure base and raises the return on owning one
- ContextOps: turning operational evidence and expert judgment into tested, approved instructions and maintaining them as the business changes; the process owner is accountable, engineering maintains execution
- Executable coverage: share of a process's cases an agent handles correctly with current approved procedures; start by sampling ~100 cases
- Learning loop: escalation → operator resolution with recorded reasoning → agent-proposed procedure update with evidence → owner approval → test and deploy
- Fine-tuning on company history is rejected: it can learn bad habits and must be redone as the business changes
- Agent instructions need an owner, a version, evidence-backed change proposals, tests, deployment, and rollback; operators need to see the cases behind a proposed rule, not only a text diff
