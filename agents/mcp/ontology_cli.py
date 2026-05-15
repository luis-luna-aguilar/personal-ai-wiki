from __future__ import annotations

import argparse
import json

from .config import load_config
from .ontology.compiler import OntologyCompiler, default_paths


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Compile Luis's AI Wiki into a Neo4j ontology graph.")
    parser.add_argument(
        "--extractor",
        choices=["manual", "llm", "heuristic"],
        default="manual",
        help="Use manual for Codex-produced extraction packets, llm for OpenRouter automation, or heuristic for smoke tests.",
    )
    subcommands = parser.add_subparsers(dest="command", required=True)
    subcommands.add_parser("status", help="Show clean, dirty, failed, and deleted wiki files.")
    subcommands.add_parser("rebuild", help="Clear this ontology namespace and process all eligible wiki files.")
    subcommands.add_parser("sync", help="Process dirty, failed, new, and deleted files.")

    prepare_parser = subcommands.add_parser("prepare", help="Create manual extraction work packets for dirty files.")
    prepare_parser.add_argument("--limit", type=int, default=None)
    prepare_parser.add_argument("--all", action="store_true", help="Prepare all eligible wiki files, not just dirty files.")

    import_parser = subcommands.add_parser("import", help="Import filled manual extraction artifact(s) into Neo4j.")
    import_parser.add_argument("path", help="Artifact JSON file or directory of artifact JSON files.")

    inspect_parser = subcommands.add_parser("inspect", help="Run extraction for one wiki file without writing it.")
    inspect_parser.add_argument("path", help="Repo-relative wiki file path, for example wiki/concepts/mcp.md.")

    query_parser = subcommands.add_parser("query", help="Search ontology entities in Neo4j.")
    query_parser.add_argument("text", help="Search text.")
    query_parser.add_argument("--limit", type=int, default=10)

    expand_parser = subcommands.add_parser("expand", help="Expand relationships around one entity.")
    expand_parser.add_argument("name", help="Entity name.")
    expand_parser.add_argument("--depth", type=int, default=2)
    expand_parser.add_argument("--limit", type=int, default=30)

    actions_parser = subcommands.add_parser("actions", help="Search kinetic-layer actions and workflows.")
    actions_parser.add_argument("goal", help="Goal or action search text.")
    actions_parser.add_argument("--limit", type=int, default=10)
    return parser


def main() -> None:
    args = build_parser().parse_args()
    config = load_config()
    compiler = OntologyCompiler(
        paths=default_paths(config.paths.repo_root),
        model=config.model,
        extractor_mode=args.extractor,
    )
    try:
        if args.command == "status":
            status = compiler.status()
            print(json.dumps(status.__dict__, indent=2))
        elif args.command == "rebuild":
            print(json.dumps(compiler.rebuild(), indent=2))
        elif args.command == "sync":
            print(json.dumps(compiler.sync(), indent=2))
        elif args.command == "prepare":
            print(json.dumps(compiler.prepare(limit=args.limit, process_all=args.all), indent=2))
        elif args.command == "import":
            print(json.dumps(compiler.import_artifacts(config.paths.repo_root / args.path), indent=2))
        elif args.command == "inspect":
            print(json.dumps(compiler.inspect_file(args.path), indent=2))
        elif args.command == "query":
            print(json.dumps(compiler.query(args.text, limit=args.limit), indent=2))
        elif args.command == "expand":
            print(json.dumps(compiler.expand(args.name, depth=args.depth, limit=args.limit), indent=2))
        elif args.command == "actions":
            print(json.dumps(compiler.actions(args.goal, limit=args.limit), indent=2))
    finally:
        compiler.close()


if __name__ == "__main__":
    main()
