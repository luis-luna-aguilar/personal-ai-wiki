from __future__ import annotations

import argparse
import json

from .engine import PersonalWikiAgent


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Query Luis's personal wiki.")
    parser.add_argument("prompt", help="Question, claim, or situation to evaluate.")
    parser.add_argument("--context", default="", help="Additional context for the query.")
    parser.add_argument(
        "--include-personal-views",
        action="store_true",
        help="Allow the agent to use Luis's personal notes and takes.",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Print the full structured response as JSON.",
    )
    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    agent = PersonalWikiAgent()
    response = agent.answer(
        prompt=args.prompt,
        context=args.context,
        include_personal_views=args.include_personal_views,
    )

    if args.json:
        print(json.dumps(response.to_dict(), indent=2))
        return

    print(response.answer)
    print("\nConsulted pages:")
    for page in response.consulted_pages:
        print(f"- {page.path} ({page.as_of or 'no as_of'})")
    print("\nGaps:")
    for gap in response.gaps:
        print(f"- [{gap.type}] {gap.message}")


if __name__ == "__main__":
    main()

