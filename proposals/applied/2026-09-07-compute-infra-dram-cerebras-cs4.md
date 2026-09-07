---
type: proposal
source: raw/newsletters/2026-08-19-ainews-memory-prices-up-500-in-12-months.md
status: pending
created: 2026-09-07
---

# Proposal: Compute infrastructure squeeze — DRAM prices up 500%, Cerebras doubles inference throughput

## Summary

### The source
AINews's 2026-08-19 issue relays a Tom's Hardware report that DRAM/memory pricing has become "entirely divorced from reality": 128GB DDR5 kits now cost roughly 10x their lowest-ever price, hyperscale buyers have reportedly pre-committed most of 2027's global DRAM production capacity with advance deposits, and mainstream DRAM is now worth over half as much per kilogram as solid gold — a reversal of the usual price-decline curve for memory specifically. The same issue covers Cerebras announcing CS-4: the same 5nm wafer, 4 trillion transistors, and 900k AI cores as WSE-3, but with redesigned power delivery and cooling that roughly double per-wafer throughput — 250 PFLOPs per WSE-3 Turbo chip, 750 PFLOPs for a 3-wafer rack — with a claimed 4,400+ tokens/sec per user serving GPT-OSS-120B, described as up to 30x faster than GPU-based systems.

### What changes
The wiki's compute-infrastructure trend page already tracks compute-moat signals and counterforces (open-weight competition, runtime efficiency, outputmaxxing) but has no line on memory pricing or this specific Cerebras generation.

- **Compute infrastructure as decisive competitive moat** gains one new Current-status bullet covering the DRAM shortage and the CS-4 announcement together (two axes of the same infrastructure-economics story), a new Recent-changes entry, and its page date moves to 19 August.
- The AINews issue's source page is created by a companion proposal for the Qwen3.8-27B signal, whose draft already lists this page under its Influenced pages — no separate action needed here.

### What to weigh
Both figures (the DRAM pricing multiples and the Cerebras throughput claims) are vendor/press-relayed numbers via a newsletter, not independently benchmarked — consistent with how this page already treats similarly-sourced claims (it explicitly caveats the AMD/Taalas and outputmaxxing entries the same way).

## Intended changes

- [x] **Approve all**

- [ ] **Update** `wiki/trends/compute-infrastructure.md` — new Current-status bullet, Recent-changes entry, as_of bump
    > See draft below

## Page drafts

### wiki/trends/compute-infrastructure.md (updated)

```md
Frontmatter changes: as_of: 2026-08-19; sources: append ainews-memory-prices-openai-pause-2026-08-19

## Current status (as of 2026-08-19) — new bullet appended

- Memory pricing has reversed its usual decline: 128GB DDR5 kits reportedly cost ~10x their lowest-ever price, hyperscalers have pre-committed most of 2027's global DRAM production capacity, and DRAM is now worth over half as much per kilogram as gold (Tom's Hardware, via AINews). In the same window, Cerebras announced CS-4 — same 5nm wafer/4T transistors/900k cores as WSE-3, but redesigned power delivery and cooling roughly double per-wafer throughput (250 PFLOPs per WSE-3 Turbo, 750 PFLOPs for a 3-wafer rack), with a claimed 4,400+ tok/s per user on GPT-OSS-120B, up to 30x faster than GPU-based systems. Together the two data points show compute-infrastructure economics diverging on two axes at once: memory getting structurally more expensive while specialized inference silicon gets structurally faster.

## Recent changes (new entry, prepended)

- [2026-08-19] DRAM/memory prices reportedly up to ~10x their lowest-ever level, with 2027 production capacity largely pre-committed by hyperscalers; Cerebras announces CS-4, roughly doubling per-wafer inference throughput over WSE-3 (4,400+ tok/s/user on GPT-OSS-120B, claimed up to 30x faster than GPUs).
```

## Open questions

None beyond the sourcing caveat above.
