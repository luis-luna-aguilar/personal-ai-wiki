#!/usr/bin/env python3
"""T11 / C6 — constraint-coherence checker. For each cardinality constraint, verify the object's
class matches the verb-property's declared RANGE in the map. Catches the iteration-4 bug class
(a property given two conflicting ranges). Usage: python3 coherence-check.py <page.ace>"""
import sys, importlib
ds = importlib.import_module("drs2shacl"); v3 = ds.v3
is_c, aval, conds_of, BY_ID = v3.is_c, v3.aval, v3.conds_of, v3.BY_ID
IRI2TERM = {t["onto"].get("iri"): t for t in BY_ID.values()}

def check(ace_path):
    conflicts=0; checked=0
    for line in open(ace_path):
        s=line.strip()
        if not s or s.startswith("#"): continue
        drs=v3.run_ape(s)
        if not drs: continue
        conds=conds_of(v3.parse_drs(drs))
        impl=next((c for c in conds if is_c(c,"=>")),None)
        if not impl: continue
        card=ds.find_card_property(impl[1][1])
        if not card: continue
        verb,ycls,op,n=card; checked+=1
        prop=BY_ID.get(verb)
        if not prop: continue
        declared_range=prop["onto"].get("range")
        obj_iri=v3.class_iri(ycls)
        if declared_range and obj_iri and declared_range!=obj_iri:
            print(f"  CONFLICT: '{s.strip()}'")
            print(f"            property {prop['onto'].get('iri')} range is {declared_range}, but the constraint targets {obj_iri}")
            conflicts+=1
    if conflicts: print(f"FAIL: {conflicts} coherence conflict(s) in {ace_path}"); return 1
    print(f"OK: {checked} cardinality constraint(s) coherent with the map in {ace_path}"); return 0

if __name__=="__main__":
    sys.exit(check(sys.argv[1]))
