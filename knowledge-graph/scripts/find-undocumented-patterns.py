#!/usr/bin/env python3
"""
Finds recurring multi-property compositions across wiki/**/*.ttl and flags
any that aren't yet covered by a system/authoring-guides/*.md guide.

Why this exists: lexicon-map.yaml catalogs individual word<->IRI mappings.
It does not, and should not, catalog *structural patterns* -- a fact modeled
by composing several already-confirmed terms together (e.g. the KPI-metric
shape: fibo:KeyPerformanceIndicator + biz:metricValue + biz:metricUnit +
biz:changeDirection + biz:associatedMetric). Those patterns can only be
found by looking at how terms are actually used together in the .ttl files,
not by reading the term catalog. This script automates that look, so it
doesn't depend on someone happening to notice a pattern during a review.

Run it periodically (e.g. before starting a VCR, or as part of a wiki-wide
audit) -- not only when a specific mistake prompts it. Any NEW recurring
signature it reports that isn't in COVERED_SIGNATURES below is a candidate
for a new system/authoring-guides/*.md file: the pattern is real, it's just
not written down yet. When you add a guide for one, add its signature to
COVERED_SIGNATURES so future runs don't re-report it.

Usage: python3 knowledge-graph/scripts/find-undocumented-patterns.py
"""

import collections
import glob
import os
import sys

import rdflib

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
IGNORE_PRED_LOCALNAMES = {"label", "comment"}  # present almost everywhere; not pattern-defining alone
MIN_PREDICATES = 2       # a signature with fewer predicates isn't a "composition"
MIN_OCCURRENCES = 2      # a signature seen only once isn't "recurring"

# Signatures already covered by an authoring guide. Keys are
# (sorted tuple of type local-names, sorted tuple of predicate local-names).
# Update this whenever a new guide is added, so this script only reports
# genuinely new gaps on the next run.
COVERED_SIGNATURES = {
    (("Concept",), ("definition", "prefLabel")): "skos-concept.md",
    (("Concept",), ("broader", "definition", "prefLabel")): "skos-concept.md",
    (("Concept",), ("definition", "prefLabel", "related")): "skos-concept.md",
    (("Concept",), ("altLabel", "definition", "prefLabel", "related")): "skos-concept.md",
    (("KeyPerformanceIndicator",), ("associatedMetric", "changeDirection", "measuredInYear", "metricUnit", "metricValue")): "kpi-metric.md",
    (("SoftwareApplication",), ("embeds", "hasDeploymentModel", "provider")): "software-application.md",
    (("Activity", "HowTo"), ("step", "used", "wasAssociatedWith")): "numbered-process-steps.md",
    (("HowToStep", "ProtocolStep"), ("position", "precedes")): "numbered-process-steps.md",
    (("HowToStep", "ProtocolStep"), ("position", "precedes", "wasAssociatedWith")): "numbered-process-steps.md",
    (("Concept", "KeyPerformanceIndicator"), ("definition", "metricUnit", "prefLabel")): "metric-concept.md",
    (("RetailCategory",), ("definition", "prefLabel")): "retail-category.md",
    (("Role",), ("definition", "prefLabel")): "org-role.md",
    (("Concept", "PricingModality"), ("broader", "definition", "prefLabel")): "enum-member-concept.md",
    (("Concept", "PricingModality"), ("definition", "prefLabel")): "enum-member-concept.md",  # broader now derived via skos inverse axiom (VCR-0019)
    (("Concept", "FormalOrganization"), ("definition", "exposesAPI", "integratesWith", "prefLabel")): "api-vendor.md",
    (("Concept", "PaymentGateway"), ("definition", "integratesWith", "prefLabel")): "payment-gateway.md",
    (("Entity",), ("date", "wasDerivedFrom")): "record-page.md",
    # Corporate legal-entity composite pattern (VCR-0020, 6-entity corporate-structure
    # ingestion, 2026-07-06/08) — all variants below are one pattern, see corporate-legal-entity.md.
    (("DigitalDocument",), ("dateCreated", "name")): "corporate-legal-entity.md",
    (("AdvisoryEngagement",), ("advisoryRole", "primaryContact", "providedBy")): "corporate-legal-entity.md",
    (("Person",), ("email", "telephone")): "corporate-legal-entity.md",
    (("ComplianceObligation",), ("hasComplianceObligationFrequency", "hasDeadlineDescription", "providedBy", "regulatedBy")): "corporate-legal-entity.md",
    (("ComplianceObligation",), ("hasComplianceObligationFrequency", "hasDeadlineDescription", "hasObligationCost", "providedBy", "regulatedBy")): "corporate-legal-entity.md",
    (("Membership",), ("member", "organization", "role")): "corporate-legal-entity.md",
    (("ComplianceObligation",), ("hasComplianceObligationFrequency", "hasDeadlineDescription", "regulatedBy")): "corporate-legal-entity.md",
    (("OwnershipStake",), ("heldBy", "ownershipPercentage")): "corporate-legal-entity.md",
    (("Membership",), ("member", "organization", "role", "signingScope")): "corporate-legal-entity.md",
    (("ComplianceObligation",), ("hasComplianceObligationFrequency", "hasDeadlineDescription", "providedBy")): "corporate-legal-entity.md",
    (("FinancingInstrument",), ("cardLastFourDigits", "facilityLimit", "instrumentType", "providedBy")): "corporate-legal-entity.md",
    (("BankAccount",), ("accountHolderBank", "accountNumber", "accountStatus", "authorizedSignatory", "primaryContact")): "corporate-legal-entity.md",
    (("BankAccount",), ("accountCurrency", "accountHolderBank", "accountNumber", "accountStatus", "authorizedSignatory", "iban")): "corporate-legal-entity.md",
    (("ComplianceObligation",), ("hasComplianceObligationFrequency", "providedBy", "regulatedBy")): "corporate-legal-entity.md",
    (("AdvisoryEngagement",), ("advisoryRole", "engagementFee", "primaryContact", "providedBy")): "corporate-legal-entity.md",
    (("BankAccount",), ("abaRoutingNumber", "accountHolderBank", "accountStatus", "beneficiaryReference", "brokerIntermediary", "swiftCode")): "corporate-legal-entity.md",
    (("ComplianceObligation",), ("hasComplianceObligationFrequency", "hasDeadlineDescription", "hasObligationCost", "regulatedBy")): "corporate-legal-entity.md",
    (("AdvisoryEngagement",), ("advisoryRole", "providedBy")): "corporate-legal-entity.md",
}


def local_name(uri):
    s = str(uri)
    return s.rsplit("#", 1)[-1].rsplit("/", 1)[-1]


def main():
    g = rdflib.Graph()
    ttl_files = sorted(glob.glob(os.path.join(REPO_ROOT, "wiki", "**", "*.ttl"), recursive=True))
    ok, fail = 0, 0
    for f in ttl_files:
        try:
            g.parse(f, format="turtle")
            ok += 1
        except Exception as e:
            fail += 1
            print(f"PARSE FAIL: {f}: {e}", file=sys.stderr)

    print(f"Parsed {ok}/{len(ttl_files)} wiki .ttl files ({fail} failures), {len(g)} triples total.\n")

    subjects = collections.defaultdict(lambda: {"types": set(), "preds": set()})
    for s, p, o in g:
        if isinstance(s, rdflib.BNode):
            continue
        if p == rdflib.RDF.type:
            subjects[s]["types"].add(local_name(o))
        else:
            pn = local_name(p)
            if pn.lower() not in IGNORE_PRED_LOCALNAMES:
                subjects[s]["preds"].add(pn)

    sig_to_subjects = collections.defaultdict(list)
    for s, data in subjects.items():
        if len(data["preds"]) < MIN_PREDICATES:
            continue
        sig = (tuple(sorted(data["types"])), tuple(sorted(data["preds"])))
        sig_to_subjects[sig].append(s)

    recurring = {sig: subs for sig, subs in sig_to_subjects.items() if len(subs) >= MIN_OCCURRENCES}

    covered = {sig: subs for sig, subs in recurring.items() if sig in COVERED_SIGNATURES}
    uncovered = {sig: subs for sig, subs in recurring.items() if sig not in COVERED_SIGNATURES}

    print(f"{len(recurring)} recurring signature(s) found ({len(covered)} already covered, {len(uncovered)} NOT covered).\n")

    if uncovered:
        print("=== UNCOVERED — candidates for a new system/authoring-guides/*.md ===\n")
        for sig, subs in sorted(uncovered.items(), key=lambda kv: -len(kv[1])):
            types, preds = sig
            print(f"  {len(subs)} individuals | types={list(types)} | predicates={list(preds)}")
            print(f"    examples: {[local_name(s) for s in subs[:5]]}")
        print()

    if covered:
        print("=== Covered (for reference) ===\n")
        for sig, subs in sorted(covered.items(), key=lambda kv: -len(kv[1])):
            types, preds = sig
            print(f"  {len(subs)} individuals | types={list(types)} -> {COVERED_SIGNATURES[sig]}")

    return 1 if uncovered else 0


if __name__ == "__main__":
    sys.exit(main())
