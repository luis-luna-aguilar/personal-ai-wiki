#!/usr/bin/env python3
"""T9 / C3 — production DRS→TTL compiler (thin wrapper over drs2ttl_v3.compile_page).
Reads a .ace file, compiles to a CANDIDATE .ttl via the canonical lexicon-map.yaml.
HARD-ERRORS on any unmapped term (no silent minting).

The candidate defaults to <repo>/tmp/drs2ttl/<stem>.generated.ttl — never the wiki
sidecar path, because rebuild.sh sweeps every wiki/**/*.ttl into the graph. Review
the candidate diff, then promote deliberately (cp, or drs2ttl_v3.py --in-place).
Companions are compiled alongside: <stem>.generated.shapes.ttl (SHACL) and
<stem>.generated.swrl (SWRL). See drs2ttl_v3.py's docstring for the settled
routing/merge/scoping decisions.

Usage: python3 drs2ttl.py <page.ace> [out.ttl]"""
import sys, importlib
v3 = importlib.import_module("drs2ttl_v3")
v3.gen_ulex()  # ensure the parser lexicon matches the canonical map

def main(ace_path, out_path=None):
    r = v3.compile_page(ace_path, out_path, merge=True, shapes=True, swrl=True, strict=True)
    print(f"wrote {r['out']} — {r['triples']} triples, "
          f"{r['annots']} merged annotation(s), {r['canon_only']} canon-only fact(s), 0 unmapped")

if __name__=="__main__":
    if len(sys.argv)<2: sys.exit(__doc__)
    main(sys.argv[1], sys.argv[2] if len(sys.argv)>2 else None)
