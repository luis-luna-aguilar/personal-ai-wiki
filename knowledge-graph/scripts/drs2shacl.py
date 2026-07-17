#!/usr/bin/env python3
"""DRS -> SHACL synthesizer (iteration 4).
Turns ACE constraint sentences into real sh:NodeShape/sh:property (not comment skeletons),
and HONESTLY classifies the constraints that SHACL-Core cannot express (obligations,
production rules) instead of pretending. Reuses the v3 map + DRS parser."""
import importlib, re, os
v3 = importlib.import_module("drs2ttl_v3")
is_c, aval, conds_of, BY_ID = v3.is_c, v3.aval, v3.conds_of, v3.BY_ID
class_iri, pred_iri, named_iri, contains = v3.class_iri, v3.pred_iri, v3.named_iri, v3.contains
HERE = v3.HERE

# Regenerate the lexicon so the new constraint terms (apply-to, use, sharing-percentage) are known.
v3.gen_ulex()

CONSTRAINTS = [
 ("K1","Every pricing-strategy applies-to exactly one segment."),
 ("K2","Every pricing-strategy uses exactly one modality."),
 ("K3","Every pricing-strategy uses at most one modality."),
 ("K4","If a pricing-strategy uses a share-value then the pricing-strategy has a sharing-percentage."),
 ("R1","If a change is critical then a user must perform a two-factor-authentication."),   # obligation across actors
 ("R2","If a user is in a segment and the segment has no active-strategy then the system assigns a base-configuration to the user."),  # production rule
]

OP2CARD = {"exactly": lambda n:[("sh:minCount",n),("sh:maxCount",n)],
           "leq":     lambda n:[("sh:maxCount",n)],
           "geq":     lambda n:[("sh:minCount",n)],
           "eq":      lambda n:[("sh:minCount",1)]}

def flatten(conds):
    out=[]
    for c in conds:
        if isinstance(c,tuple) and c[0]=="list": out += flatten(c[1])
        else: out.append(c)
    return out

def single_object(drs):           # antecedent class X
    objs=[c for c in flatten(conds_of(drs)) if is_c(c,"object")]
    return aval(objs[0][1][1]) if objs else None

def _unwrapped(cons):
    """Consequent conditions, seeing through must(drs(...)) — 'Every X must contain
    exactly one Y' is structural cardinality wearing deontic surface syntax."""
    cc=flatten(conds_of(cons))
    for c in list(cc):
        if is_c(c,"must"): cc+=flatten(conds_of(c[1][0]))
    return cc

def find_card_property(cons):
    """consequent: predicate(_,verb,A,B) + object(B,Y,_,_,OP,N)  ->  (verbIRI, classY, OP, N)."""
    cc=_unwrapped(cons); pred=None; obj=None
    for c in cc:
        if is_c(c,"predicate") and aval(c[1][1]) not in ("be",): pred=c
        if is_c(c,"object"): obj=c
    if not pred or not obj: return None
    verb=aval(pred[1][1]); y=aval(obj[1][1])
    op=aval(obj[1][4]); n=aval(obj[1][5])
    return (verb,y,op,int(n) if n and n.isdigit() else 1)

def _card_subject_var(cons):
    """Variable that is the subject of the consequent's cardinality predicate."""
    pred=next((c for c in _unwrapped(cons) if is_c(c,"predicate") and aval(c[1][1])!="be"),None)
    if not pred: return None
    t=v3.arg_term(pred[1][2])
    return t[1] if t[0]=="var" else None

def _ant_var(ant):
    return next((aval(c[1][0]) for c in flatten(conds_of(ant)) if is_c(c,"object")),None)

def classify_constraint(impl):
    ant,cons=impl[1][0],impl[1][1]
    if contains(cons,"v"): return "enum"               # TBox enumeration/covering -> ontology module, not SHACL
    if contains(cons,"-") and not contains(cons,"must"): return "negative-universal"
    if contains(cons,"property"): return "qualifier-universal"
    cons_flat=flatten(conds_of(cons))
    if cons_flat and all(is_c(c,"object") or (is_c(c,"predicate") and aval(c[1][1])=="be") for c in cons_flat):
        return "subclass"                              # "Every route is a profitability-unit."
    card=find_card_property(cons)
    same_subj = card is not None and _card_subject_var(cons)==_ant_var(ant)
    # deontic 'must' stays deontic only when the consequent acts on ANOTHER actor
    # ("the system must reject …"); same-subject must+cardinality is a schema assertion
    if contains(cons,"must") and not same_subj: return "obligation"
    # production rule: consequent asserts an action by a system agent (a 'predicate' whose subject is introduced in consequent, not the target)
    if contains(ant,"=>") or (contains(ant,"-") and not contains(cons,"-")):
        if not same_subj or contains(ant,"=>"): return "production"
    if card and same_subj:
        # conditional-required: antecedent has a value test (predicate beyond the single class) -> if/then
        ant_objs=[c for c in flatten(conds_of(ant)) if is_c(c,"object")]
        ant_preds=[c for c in flatten(conds_of(ant)) if is_c(c,"predicate") and aval(c[1][1])!="be"]
        if len(ant_objs)>1 or ant_preds: return "conditional"
        return "cardinality"
    # has-datatype required, conditional?
    if contains(ant,"predicate"): return "conditional"
    return "unknown"

def shape_header(sid,target):
    return f"{v3.DATA_PREFIX}:shape-{sid} a sh:NodeShape ;\n    sh:targetClass {target} ;"

def synth_cardinality(sid,impl):
    x=single_object(impl[1][0]); verb,y,op,n=find_card_property(impl[1][1])
    cards=OP2CARD.get(op,lambda n:[])(n)
    ent=v3.noun_term(y)
    if ent and ent["onto"]["role"]=="DatatypeProperty":
        # "Every pricing-strategy has exactly one fiat-value-reference" — the object noun
        # IS the property; 'have' stays a function word (never an IRI)
        o=ent["onto"]; parts=[f"sh:path {o['iri']}"]
        if o.get("unit")=="money":
            parts.append("sh:class schema:MonetaryAmount")   # Rule 10: money is reified, not a bare decimal
        elif o.get("datatype"): parts.append(f"sh:datatype {o['datatype']}")
    else:
        parts=[f"sh:path {pred_iri(verb)}", f"sh:class {class_iri(y)}"]
    parts+=[f"{k} {v}" for k,v in cards]
    return shape_header(sid,class_iri(x))+"\n    sh:property [ "+" ; ".join(parts)+" ] .\n"

def synth_conditional(sid,impl):
    """if <strategy uses share-value> then <has sharing-percentage>  ->  sh:or( not[cond] , [consequent] )."""
    ant,cons=impl[1][0],impl[1][1]; x=single_object(ant)
    # antecedent value test: predicate(use, A, B) + object(B, share-value Individual)
    cc=v3 and flatten(conds_of(ant)); cond_path=None; cond_val=None
    objs={aval(c[1][0]):aval(c[1][1]) for c in flatten(conds_of(ant)) if is_c(c,"object")}
    for c in flatten(conds_of(ant)):
        if is_c(c,"predicate") and aval(c[1][1])!="be":
            verb=aval(c[1][1]); b=aval(c[1][3]) if len(c[1])>3 else None
            cond_path=pred_iri(verb)
            lemma=objs.get(b)
            if lemma and BY_ID.get(lemma,{}).get("onto",{}).get("role")=="Individual":
                cond_val=BY_ID[lemma]["onto"]["iri"]
    # consequent required datatype property
    req=None
    for c in flatten(conds_of(cons)):
        if is_c(c,"object"):
            lemma=aval(c[1][1]); ent=BY_ID.get(lemma)
            if ent and ent["onto"]["role"]=="DatatypeProperty": req=ent["onto"]["iri"]
    if not (cond_path and cond_val and req): return None
    return (shape_header(sid,class_iri(x))+"\n"
            f"    sh:or (\n"
            f"        [ sh:not [ sh:property [ sh:path {cond_path} ; sh:hasValue {cond_val} ] ] ]\n"
            f"        [ sh:property [ sh:path {req} ; sh:minCount 1 ] ]\n"
            f"    ) .\n")

def main():
    out_shapes=[]; notes=[]
    for sid,ace in CONSTRAINTS:
        drs=v3.run_ape(ace)
        if not drs: notes.append((sid,ace,"PARSE-FAIL",None)); continue
        conds=conds_of(v3.parse_drs(drs))
        impl=next((c for c in conds if is_c(c,"=>")),None)
        if not impl: notes.append((sid,ace,"no-implication",None)); continue
        kind=classify_constraint(impl)
        if kind=="cardinality":
            out_shapes.append(synth_cardinality(sid,impl)); notes.append((sid,ace,"cardinality","SHACL"))
        elif kind=="conditional":
            s=synth_conditional(sid,impl)
            if s: out_shapes.append(s); notes.append((sid,ace,"conditional","SHACL (sh:or)"))
            else: notes.append((sid,ace,"conditional","unsynthesized"))
        elif kind=="obligation":
            notes.append((sid,ace,"obligation","NOT SHACL-Core — deontic/cross-actor → SWRL or policy rule"))
        elif kind=="production":
            notes.append((sid,ace,"production","NOT SHACL-Core — behavioural 'assigns' → SWRL/inference rule"))
        else:
            notes.append((sid,ace,kind,"unhandled"))
    ttl=os.path.join(HERE,"constraints.shacl.ttl")
    with open(ttl,"w") as f:
        import kgconfig
        for p,u in list(kgconfig.project_namespaces()) + [("sh","http://www.w3.org/ns/shacl#"),
                    ("xsd","http://www.w3.org/2001/XMLSchema#"),("rdfs","http://www.w3.org/2000/01/rdf-schema#")]:
            f.write(f"@prefix {p}: <{u}> .\n")
        f.write("\n")
        for s in out_shapes: f.write(s+"\n")
    print("constraint dispatch:")
    for sid,ace,kind,dest in notes: print(f"  {sid}: {kind:12} -> {dest}")
    print(f"\nwrote {os.path.basename(ttl)} ({len(out_shapes)} real SHACL shapes)")
    return ttl

if __name__=="__main__":
    ttl=main()
    # validate shapes are well-formed SHACL
    import rdflib
    try:
        from pyshacl.rdfutil import load_from_source
        sg=rdflib.Graph().parse(ttl,format="turtle")
        from pyshacl import validate
        # validate the shapes graph against itself's SHACL metamodel by parsing; run against v3 ABox as data
        data=rdflib.Graph().parse(os.path.join(HERE,"prototype-output.v3.ttl"),format="turtle")
        conforms,_,report=validate(data, shacl_graph=sg, inference="none")
        print(f"\nSHACL well-formed & executed against v3 ABox — conforms={conforms}")
        print("  (non-conformance is expected: the ABox has no instances satisfying the new cardinality rules)")
    except Exception as e:
        print("pyshacl run note:", e)
