---
title: Cognition — Factoring RSA-260
type: source
source_type: article
source_file: raw/articles/2026-11-23-cognitioncom-blog-factoring-rsa-260.md
url: https://cognition.com/blog/factoring-rsa-260
published: 2026-09-09
ingested: 2026-11-24
domains: [science, coding, agents]
---

# Cognition — Factoring RSA-260

Cognition researcher Eric Lu describes using parallel Devin Cloud sessions to rebuild CADO-NFS, the open-source general number field sieve (GNFS) implementation, for GPUs, and using it to factor RSA-260 and 2^1277−1. The first prompt (13 August 2026) asked for a GPU drop-in for CADO's CPU lattice siever; nine hours later it handled RSA-250 parameters. Over three weeks Devin rewrote nearly every pipeline stage. RSA-260 took about 15.6 days of wall time (finishing 2026-09-03); 2^1277−1 (385 digits) followed on 2026-09-08 as what Cognition calls an SNFS record. Lu details the human's share of the work and how much the agents depended on CADO-NFS's existing decomposition. A long appendix gives per-stage timings, parameters and polynomials for every factorization. Published 2026-09-09.

## Influenced pages

- [AI in mathematics](../../trends/ai-in-mathematics.md) — new computational-number-theory case
- [Multi-agent coordination: evidence](../../workflows/multi-agent-coordination-evidence.md) — human share of a long-running swarm
- [Devin](../../tools/devin.md) — research-swarm line

## Key claims extracted

- GPU lattice siever (`glas`) handled RSA-250 parameters about 9 hours after the first prompt.
- Average 3, peak 18 concurrent Devin sessions over three weeks; GPU polynomial selection (with msieve components), GPU lattice siever, optimized CADO head, parallel dup/purge and fused merge/replay, GPU block Wiedemann, GPU square root; only `cado-nfs.py`, `polyselect_ropt`, `makefb` and `dup1` untouched.
- Scaling ladder: within five days, a 190-digit number took as long as a 157-digit one at the start (a little over 3 hours); C311 = (179^139−1)/178 in about 14.3 hours.
- RSA-260: 2026-08-18 to 2026-09-03, 1,344,878 s wall time, about 4,923 GPU-days; 8.3 billion relations from sieving; sieving 7.9 days on B200/GB200/GB300 nodes.
- C385 = 2^1277−1 factored 2026-09-03 to 2026-09-08 (455,206 s, 2,423 GPU-days) into p106 × p117 × p163; called a new SNFS record.
- Human share: 82,702 words in 3,328 messages across 192 of 233 sessions (14,450 ACUs); Devins started 101 child sessions, 36 with no human intervention.
- Human supplied executive function and a unified benchmark/measurement system; agents grew more confused as code diverged from upstream CADO-NFS; the author does not understand much of the underlying mathematics.
