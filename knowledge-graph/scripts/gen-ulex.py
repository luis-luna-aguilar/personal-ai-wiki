#!/usr/bin/env python3
"""T7 / C7 — generate the APE lexicon (.ulex) from the canonical lexicon-map.yaml.
Single source of truth → parser lexicon. Run from rebuild.sh; a no-op regen must be an empty diff.
Usage: python3 gen-ulex.py [lexicon-map.yaml] [out.ulex]"""
import sys, yaml, os
import kgconfig
HERE = os.path.dirname(os.path.abspath(__file__))
# Canonical lexicon lives in ../ontology/lexicon-map.yaml (single source of truth).
DEF_SRC = os.path.join(HERE, "..", "ontology", "lexicon-map.yaml")
DEF_OUT = kgconfig.ulex_path()   # kg.config.yaml → ontology.lexicon_ulex
SRC = sys.argv[1] if len(sys.argv) > 1 else (DEF_SRC if os.path.exists(DEF_SRC) else os.path.join(HERE, "lexicon-map.yaml"))
OUT = sys.argv[2] if len(sys.argv) > 2 else (DEF_OUT if os.path.isdir(os.path.dirname(DEF_OUT)) else os.path.join(HERE, "lexicon.gen.ulex"))
HUMAN = {"super-admin","admin","analyst","bank-administrator","user","cardholder","customer"}

terms = yaml.safe_load(open(SRC))["terms"]
lines = ["% GENERATED from lexicon-map.yaml by gen-ulex.py — do not edit by hand.",
         f"% {len(terms)} terms."]
n_noun=n_mass=n_tv=n_adj=0
for t in terms:
    a = t["ace"]; pos = a["pos"]; tid = t["id"]
    if pos == "noun":
        g = "human" if tid in HUMAN else "neutr"
        lines.append(f"noun_sg('{a['sg']}', '{tid}', {g})."); n_noun+=1
    elif pos == "noun_mass":
        lines.append(f"noun_mass('{a['sg']}', '{tid}', neutr)."); n_mass+=1
    elif pos == "tv":
        lines.append(f"tv_finsg('{a['finsg']}', '{a['infpl']}'). tv_infpl('{a['infpl']}', '{a['infpl']}')."); n_tv+=1
    elif pos == "adj":
        lines.append(f"adj_itr('{a['positive']}', '{a['positive']}')."); n_adj+=1
    else:
        sys.stderr.write(f"WARN unknown pos {pos!r} for {tid}\n")
open(OUT, "w").write("\n".join(lines) + "\n")
print(f"wrote {os.path.basename(OUT)} — {n_noun} noun_sg · {n_mass} noun_mass · {n_tv} tv · {n_adj} adj")
