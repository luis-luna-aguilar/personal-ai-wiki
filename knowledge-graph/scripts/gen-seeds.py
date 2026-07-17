#!/usr/bin/env python3
"""Generate knowledge-graph/ontology/seeds/*.txt from what our own TTL files
actually reference — not hand-maintained. Run from rebuild.sh, before
extract-upstream.sh, so a newly-adopted upstream term is picked up
automatically on the next rebuild instead of silently going stale.

Why: the old seeds/*.txt files were hand-maintained lists of upstream IRIs
to pull into each extracted module. They drifted from reality (e.g.
schema:MobileApplication/AutomatedTeller/Airline/... were adopted by VCR-0012
but never added here, so the extracted schema module never contained them —
found during a lexicon-vs-ontology audit, 2026-07-06). lexicon-map.yaml is
the canonical word<->IRI catalog, but it doesn't capture every upstream term
either (plenty are used directly in hand-authored wiki sidecars, never
routed through an ACE word). The actual ground truth for "what upstream
terms do we depend on" is every authored .ttl file (central ontology +
wiki sidecars) — this scans those directly.

Usage: python3 gen-seeds.py
"""
import glob
import os
import sys

import rdflib

import kgconfig

HERE = os.path.dirname(os.path.abspath(__file__))
ONTOLOGY_DIR = kgconfig.cfg()["_ontology_dir"]
REPO_ROOT = kgconfig.cfg()["_repo_root"]
SEEDS_DIR = os.path.join(ONTOLOGY_DIR, "seeds")

# name -> namespace prefix. One seed file per vocabulary; extract-upstream.sh
# passes each file to a single `robot extract --lower-terms` call (MIREOT
# pulls in each term's own ancestor chain automatically, so listing only the
# terms we actually use — not their superclasses — is sufficient).
VOCABS = {
    "org": "http://www.w3.org/ns/org#",
    "prov": "http://www.w3.org/ns/prov#",
    "foaf": "http://xmlns.com/foaf/0.1/",
    "skos": "http://www.w3.org/2004/02/skos/core#",
    "schema": "https://schema.org/",
    "fibo-fbc-fct-fse": "https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/FinancialServicesEntities/",
    "fibo-fnd-utl-alx": "https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/Analytics/",
    "time": "http://www.w3.org/2006/time#",
    "dct": "http://purl.org/dc/terms/",
    # VCR-0020 (2026-07-07): ownership alignment + legal-form adoption.
    "fibo-be-oc-op": "https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/OwnershipParties/",
    "fibo-be-le-lei": "https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/LEIEntities/",
}

# Our own authored TTL — excludes extracts/ (upstream modules themselves)
# and the merged-TBox build artifact combining the two, both of which would
# pollute the signal with everything MIREOT pulled in last time.
OWN_TTL_GLOBS = [
    os.path.join(ONTOLOGY_DIR, "*.ttl"),
    os.path.join(kgconfig.cfg()["_wiki_dir"], "**", "*.ttl"),
]
EXCLUDE_BASENAMES = {os.path.basename(kgconfig.merged_tbox_path())}


def own_ttl_files():
    files = []
    for pattern in OWN_TTL_GLOBS:
        files.extend(glob.glob(pattern, recursive=True))
    return sorted(f for f in files if os.path.basename(f) not in EXCLUDE_BASENAMES)


def main():
    g = rdflib.Graph()
    ok, fail = 0, 0
    for f in own_ttl_files():
        try:
            g.parse(f, format="turtle")
            ok += 1
        except Exception as e:
            fail += 1
            print(f"PARSE FAIL: {f}: {e}", file=sys.stderr)
    print(f"Parsed {ok} authored TTL files ({fail} failures), {len(g)} triples.")

    used = {name: set() for name in VOCABS}
    for s, p, o in g:
        for term in (s, p, o):
            if not isinstance(term, rdflib.URIRef):
                continue
            s_str = str(term)
            for name, ns in VOCABS.items():
                if s_str.startswith(ns):
                    used[name].add(s_str)

    os.makedirs(SEEDS_DIR, exist_ok=True)
    for name in VOCABS:
        out_path = os.path.join(SEEDS_DIR, f"{name}-seeds.txt")
        terms = sorted(used[name])
        with open(out_path, "w") as f:
            f.write("\n".join(terms) + ("\n" if terms else ""))
        print(f"  {name}-seeds.txt: {len(terms)} terms")


if __name__ == "__main__":
    main()
