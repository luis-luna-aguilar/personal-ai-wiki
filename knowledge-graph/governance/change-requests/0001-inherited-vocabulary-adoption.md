# VCR 0001 — Inherited Vocabulary Adoption (`swe:`, `biz:`)

**Status:** Implemented · **Date:** 2026-07-16
**Modules:** `swe:` (`https://musclepoints.com/ontology/swe#`), `biz:` (`https://musclepoints.com/ontology/biz#`) — reused verbatim, IRIs unchanged
**Triggered by:** Deploying the MUSCLE company-brain knowledge-graph layer onto the AI Wiki (unattended overnight execution per user authorization; plan: company-brain `tmp/plan-kg-layer-port.md`)

Governed by [`vocabulary-policy.md`](../vocabulary-policy.md). This VCR documents an **admission-ladder rung 2 (upstream reuse)** decision at repo-portability scale: rather than re-deriving generic software/business vocabulary from scratch, this wiki reuses the MUSCLE project's already-vetted `swe:`/`biz:` modules wholesale, pruned of MUSCLE-domain content.

---

## Provenance

Source repo: `/Users/luis/Code/GitHub/muscle/company-brain`
Source commit: `d2c4919` (see `knowledge-graph/LINEAGE.md` for the exact stamp)
Packaged via: `knowledge-graph/scripts/package-layer.sh`

## Why reuse instead of author

`swe:` and `biz:` were built and hardened against MUSCLE's real content (SaaS/travel-platform architecture, business relations) and already passed the admission ladder there (VCR-0001/0002 of the source repo: no catalog match, no upstream fit, full research notes). An AI-technology wiki's tools/models/benchmarks are, at the infrastructure and commercial-relations level, the same *kind* of thing a SaaS platform is: `schema:SoftwareApplication` instances with providers, integrations, deployment environments, and datastores; organizations with clients and offerings. Re-deriving this from scratch would duplicate work with no benefit — the classes are domain-general software-engineering/business vocabulary, not MUSCLE-specific by construction (that's what `vocabulary-policy.md` §6b's portability test already established for everything *except* `muscle:PricingStrategy`, which is why this VCR does NOT carry `muscle:`).

## What is adopted

**`swe:` — carried in full (77 classes/properties).** Directly applicable to AI tools: `swe:API`, `swe:Database`/`Datalake`/`Datastore`, `swe:HostingPlatform`, `swe:MonitoringTool`, `swe:DeploymentEnvironment`, `swe:ABTest`+`abTestStatus`, `swe:integratesWith`/`embeds`/`embeddedIn`/`manages`/`managedBy`, `swe:usesDatastore`/`exposesAPI`/`consumesAPI`/`hostedOn`/`monitoredBy`, `swe:hasUserRole`, `swe:DeploymentModel`, `swe:IntegrationModel`, `swe:AiModel` (a MUSCLE-authored class for "the core AI decisioning logic" — reused as-is; this wiki's `aiw:FoundationModel`, minted in VCR-0003, is declared `rdfs:subClassOf swe:AiModel`, treating it as the general "AI model" concept an AI tool integrates with, which is exactly this wiki's subject matter), plus infra classes (`ApiFirstFramework`, `ContainerOrchestrator`, `ContainerRegistry`, `DockerImage`, `AuthenticationService`, `EmailService`, etc.).

**`biz:` — carried in full (91 terms), pruned of zero terms at the class/property level.** MUSCLE-domain-specific *individuals* (the `retail-banking`/`insurance`/`wealth-management` skos:Concept instances, `PricingModality` enum members, `LoyaltyProgramType`, `TravelVertical`, etc.) are inert until an AI-wiki page actually asserts them — they are not deleted, since deleting live vocabulary the class definitions still support would be destructive for zero gain; a future VCR may prune truly dead individuals once backfill (Phase C) shows which are never used. Generic relations directly useful here: `biz:clientOf`/`hasClient`, `biz:offers`, `biz:usesProduct`, `biz:subsidiaryOf`, `biz:operatesIn`.

**Not adopted:** `muscle.ttl` (the single MUSCLE-specific class `PricingStrategy` and all ABox instance data), `travel.ttl` (travel-vertical-specific), `muscle-shapes.ttl`'s MUSCLE-domain shapes (banking, pricing-strategy, corporate-legal-entity — see VCR-0003 for what shape library this wiki starts with instead).

**`alignments.ttl` and `disjointness.ttl` — carried in full, no pruning needed.** Both are pure cross-ontology bridges/axioms with zero MUSCLE-specific content already (verified: no `muscle:` references in either file).

**`lexicon-map.yaml` — filtered mechanically.** 599 rows → 446 kept (generic + upstream + swe:/biz: mappings), 153 dropped (any row referencing a `muscle:` or `travel:` IRI). Regenerated `aiw-lexicon.ulex` from the filtered map (285 nouns · 15 mass nouns · 135 verbs · 11 adjectives).

## Namespace note

`swe:`/`biz:` **keep their original `musclepoints.com` IRIs.** Per `vocabulary-policy.md` §5 (IRI permanence) — these are the *same* upstream-reused vocabulary terms as they exist in the source repo, not a fork; minting parallel `aiw:`-namespaced copies of `swe:integratesWith` etc. would violate "one concept, one term" (policy §3) by creating synonym IRIs for identical concepts. This wiki's own namespace (`aiw:`) is reserved for instance data and genuinely new AI-domain terms (VCR-0003).

## Implementation checklist

- [x] Copy `swe.ttl`, `biz.ttl`, `alignments.ttl`, `disjointness.ttl` verbatim via `package-layer.sh`.
- [x] Filter `lexicon-map.yaml`: drop all `muscle:`/`travel:`-referencing rows (599 → 446).
- [x] Regenerate `aiw-lexicon.ulex` from the filtered map.
- [x] Register both modules in `kg.config.yaml` → `namespaces.modules` and `ontology.tbox_modules`.
- [x] Confirm `alignments.ttl`/`disjointness.ttl` carry no MUSCLE-specific content (grep clean).

## Amendment (2026-07-16, same-day checker review)

A checker-review pass (per the deployment's unattended-mode audit process) found this VCR's central claim — "not adopted: `muscle.ttl` ... pruned of MUSCLE-domain content" — was **false as shipped**: `swe.ttl`/`biz.ttl` still hard-referenced `muscle:PricingStrategy` in ~24 `rdfs:domain`/`rdfs:range` positions, and `biz:PricingModality`'s `owl:oneOf` enumerated three `muscle:` individuals that were never declared anywhere in this repo (a dangling enum). The `package-layer.sh` copy step correctly excluded `muscle.ttl` itself, but nothing had pruned the *dependent* properties/classes in `swe.ttl`/`biz.ttl` that existed only to reference it.

**Fixed:** removed 21 properties/classes from `biz.ttl` (`hasPricingModality`, `PricingModality`, `appliesToSegment`, `prioritizedOver`, `hasBudget`, `hasFiatValueReference`, `hasMinimumPointUsage`, `hasRedemptionLimit`, `hasRedemptionValueLimit`, `hasSharingPercentage`, `hasTotalItemCap`, `hasWaitTime`, `hasValidityPeriod`, `ValidityPeriod`, `permanent`, `temporary`, `applies`, `appliesToChannel`, `appliesToSku`, `qualifiesFor`, `hasActiveStrategy`) and 3 from `swe.ttl` (`evaluates`, `hasControlStrategy`, `hasTrialStrategy`) — every one existed solely to reference the excluded `muscle:PricingStrategy`, making them irrecoverably dead weight with zero applicability to this wiki's subject matter. Removed the now-unused `@prefix muscle:` from both files and the `muscle:PricingStrategy` stub declaration from `swe.ttl`. Softened four remaining prose-only comment mentions (a `biz:sku` definition, a `biz:filtersBy` comment, and the `org:Role`-placement rationale comment) that described shapes/individuals as if they existed in this deployment when they were the source project's own precedent. Re-verified: both files parse clean via rdflib (497/1213 triples), no remaining `muscle:` structural references (only labeled historical-lineage comments), full `rebuild.sh` green after the fix.

**Not touched:** generically-reusable inherited vocabulary with no dangling reference (`biz:Segment`, `biz:TravelVertical` + its 4 individuals, `biz:Configuration`, etc.) — these are unused-but-valid vocabulary in this deployment's current content, the same category as any inherited term this wiki hasn't needed yet, not a structural defect.
