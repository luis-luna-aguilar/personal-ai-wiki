#!/usr/bin/env python3
"""kgconfig.py — single loader for kg.config.yaml (the project-identity config).

Python scripts:   import kgconfig; P = kgconfig.prefix()
Bash scripts:     source kg-env.sh   (which evals `python3 kgconfig.py --env`)

Every project-specific name (prefix, IRIs, artifact filenames, Fuseki
coordinates) lives in kg.config.yaml; pipeline scripts must not hard-code
them. Config resolution: $KG_CONFIG if set, else ../kg.config.yaml relative
to this file.
"""
import os
import sys

import yaml

HERE = os.path.dirname(os.path.abspath(__file__))

_cache = None


def _config_path():
    return os.environ.get("KG_CONFIG") or os.path.join(HERE, "..", "kg.config.yaml")


def cfg():
    global _cache
    if _cache is None:
        p = _config_path()
        with open(p) as f:
            c = yaml.safe_load(f)
        c["_config_path"] = os.path.abspath(p)
        kg_root = os.path.dirname(os.path.abspath(p))  # knowledge-graph/
        c["_kg_root"] = kg_root
        c["_repo_root"] = os.path.dirname(kg_root)
        c["_ontology_dir"] = os.path.join(kg_root, "ontology")
        c["_wiki_dir"] = os.path.join(c["_repo_root"], c["paths"]["wiki_root"])
        _cache = c
    return _cache


def prefix():
    return cfg()["project"]["prefix"]


def data_iri():
    return cfg()["namespaces"]["data"]


def project_namespaces():
    """[(prefix, iri)] — data namespace first, then authored module namespaces."""
    c = cfg()
    return [(c["project"]["prefix"], c["namespaces"]["data"])] + sorted(
        (c["namespaces"].get("modules") or {}).items()
    )


def named_aliases():
    return (cfg().get("compiler") or {}).get("named_aliases") or {}


def fallback_class_prefix():
    return (cfg().get("compiler") or {}).get("fallback_class_prefix", prefix())


def ontology_path(key):
    c = cfg()
    return os.path.join(c["_ontology_dir"], c["ontology"][key])


def ulex_path():
    return ontology_path("lexicon_ulex")


def merged_tbox_path():
    return ontology_path("merged_tbox")


def shapes_path():
    return ontology_path("shapes_file")


def abox_seed_paths():
    c = cfg()
    return [os.path.join(c["_ontology_dir"], s) for s in c["ontology"].get("abox_seeds") or []]


def build_dir():
    return cfg()["build"]["dir"]


def fuseki():
    c = cfg()
    f = dict(c["fuseki"])
    f.setdefault("url", f"http://localhost:{f['port']}/{f['dataset']}")
    f.setdefault("container_name", f"{prefix()}-fuseki")
    f.setdefault("compose_project", f"{prefix()}-kg")
    return f


def _shq(s):
    return "'" + str(s).replace("'", "'\\''") + "'"


def _emit_array(name, items):
    # Emitted as a real bash array (NOT exported — arrays can't cross the
    # export boundary anyway) so consumers iterate with "${NAME[@]}"
    # instead of word-splitting a joined string, which breaks the moment
    # any path element (repo root, wiki dir, ...) contains a space.
    quoted = " ".join(_shq(i) for i in items)
    print(f"{name}=({quoted})")


def _emit_env():
    c = cfg()
    f = fuseki()
    kv = {
        "KG_PROJECT_NAME": c["project"]["name"],
        "KG_PREFIX": prefix(),
        "KG_DATA_IRI": data_iri(),
        "KG_REPO_ROOT": c["_repo_root"],
        "KG_WIKI_DIR": c["_wiki_dir"],
        "KG_ONTOLOGY_DIR": c["_ontology_dir"],
        "KG_MERGED_TBOX": merged_tbox_path(),
        "KG_SHAPES_FILE": shapes_path(),
        "KG_ULEX": ulex_path(),
        "KG_BUILD_DIR": build_dir(),
        "KG_GRAPH_FILE": os.path.join(build_dir(), "graph.ttl"),
        "KG_FUSEKI_URL": f["url"],
        "KG_FUSEKI_PORT": str(f["port"]),
        "KG_FUSEKI_DATASET": f["dataset"],
        "KG_FUSEKI_PASS": f["admin_password"],
        "KG_CONTAINER_NAME": f["container_name"],
        "KG_COMPOSE_PROJECT": f["compose_project"],
    }
    for k, v in kv.items():
        print(f"export {k}={_shq(v)}")
    # Array-valued config: iterate as "${KG_TBOX_MODULES[@]}" / "${KG_ABOX_SEEDS[@]}",
    # never as unquoted `for x in $KG_TBOX_MODULES` (breaks on spaces in paths).
    _emit_array("KG_TBOX_MODULES", c["ontology"]["tbox_modules"])
    _emit_array("KG_ABOX_SEEDS", abox_seed_paths())


if __name__ == "__main__":
    if "--env" in sys.argv:
        _emit_env()
    else:
        print(cfg()["_config_path"])
