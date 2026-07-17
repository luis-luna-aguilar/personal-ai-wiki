# Sync & Source-of-Truth Model (Phase 0 / T2)

**Status:** Confirmed by the user. Destined for a section in `knowledge-graph/governance/validation-architecture.md` at adoption.

After adoption, one wiki content page is **three files**: `page.md` (human prose), `page.ace` (controlled English), `page.ttl` (graph triples). This document defines who is authoritative and how the others stay current, so the three can never silently disagree.

## The one-way pathway

```
   Markdown  ──(prose→ACE sub-agent, APE-gated)──▶  ACE  ──(deterministic compiler)──▶  TTL + SHACL
   human edits                                      committed,                          pure build output,
   (source of truth                                 human-auditable                     never hand-edited
    for narrative + facts)
```

| File | Role | Who/what writes it | Hand-editable? |
|---|---|---|---|
| `.md` | **Source of truth** for narrative *and* facts | humans (and ingestion) | **Yes** — this is where you change anything |
| `.ace` | Canonical machine-readable statement of the page's facts | the prose→ACE sub-agent; **must pass APE** before commit | No — to change a fact, edit the `.md` and regenerate |
| `.ttl` (+ shapes) | Graph triples / validation | the DRS→TTL / DRS→SHACL compilers | **No** — pure build artifact |

## Why one-way (and why ACE isn't auto-regenerated every build)

- `MD → ACE` is an **LLM step → non-deterministic.** So ACE is **not** regenerated on every build (that would churn). It is regenerated **deliberately**, when the Markdown's *facts* change, then committed and frozen — with APE as the gate that the committed ACE is valid.
- `ACE → TTL/SHACL` is **deterministic.** It may be re-run anytime and must always reproduce the committed output.

## The drift guard — `validate-sync.sh`

Runs in `rebuild.sh` and in pre-commit/CI:
1. **TTL freshness:** recompile `page.ttl` from `page.ace`; **fail if it differs** from the committed `.ttl`. This catches hand-edited or stale TTL.
2. **ACE validity:** run `validate-ace.sh` on every `.ace` (APE must accept it).
3. **ACE↔MD facts:** the auditor agent confirms the ACE asserts the same facts the Markdown states (no additions, no drops) — the one check that can't be purely mechanical, because the MD→ACE step is the LLM one.

## Conflict resolution

There is no two-way merge. If the `.md` and a sidecar disagree, the **`.md` wins**: regenerate the `.ace` from it (sub-agent + APE), then recompile the `.ttl`. You never "fix data" by editing the `.ttl` or hand-patching the `.ace`.

## Edge: vocabulary changes

If the *lexicon map* changes (a term's IRI/role), the `.ace` text may be unaffected but the `.ttl` changes — `validate-sync.sh`'s recompile-and-diff catches the staleness and forces a TTL regen. The map is itself drift-guarded by `gen-ulex` (the `.ulex` is regenerated from it).

## Edge: hand-authored blank-node enrichment

ACE's flat grammar can't express nested/reified structured values (`schema:MonetaryAmount`, `schema:PropertyValue`, `schema:PostalAddress`, etc.). `AGENTS.md` §2 sanctions a small, permanent hand-authored `.ttl` enrichment block for exactly these facts — content with no ACE form to regenerate from. `drs2ttl_v3.py`'s `merge_from_canon` already skips any triple touching a blank node when recompiling in place, for the same reason (blank nodes have no stable identity to de-dupe against across repeated compiles). `validate-sync.sh` applies the identical skip to both the committed and recompiled graphs before comparing, so this sanctioned content is never reported as drift — only genuine ACE/TTL divergence fails the gate.

A second, narrower exemption covers `xsd:gYearMonth`/`xsd:gYear` literals: when a source states only year-month or year precision for a property whose confirmed lexicon datatype is day-precision `xsd:date`, the coarser literal has no ACE form under that mapping either (documented on the `date-created` row of `lexicon-map.yaml`) and is hand-authored the same way. `validate-sync.sh` strips both exemptions before comparing. **Neither exemption is a license to skip ACE** — any fact ACE *can* express (a plain datatype value, a relation to a named individual) belongs in the `.ace`, not the enrichment block; the exemption exists only for what the grammar structurally cannot state.
