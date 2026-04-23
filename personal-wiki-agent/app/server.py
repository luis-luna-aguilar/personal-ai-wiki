from __future__ import annotations

import argparse
import sys

from mcp.server.fastmcp import FastMCP

from .engine import PersonalWikiAgent

mcp = FastMCP("personal-wiki-agent")
_agent = PersonalWikiAgent()


@mcp.tool()
def use_personal_wiki(
    prompt: str,
    context: str = "",
    include_personal_views: bool = False,
) -> dict:
    """Use Luis's personal wiki to answer questions, analyze situations, evaluate claims, surface relevant pages, and summarize recent changes."""
    response = _agent.answer(
        prompt=prompt,
        context=context,
        include_personal_views=include_personal_views,
    )
    return response.to_dict()


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Run the Personal Wiki Agent MCP server.")
    parser.add_argument(
        "--transport",
        choices=["stdio", "sse", "streamable-http"],
        default="stdio",
        help="MCP transport to run. Use stdio for Claude Desktop subprocess integration, or streamable-http for manual local testing.",
    )
    parser.add_argument(
        "--host",
        default=None,
        help="Host to bind for HTTP-based transports.",
    )
    parser.add_argument(
        "--port",
        type=int,
        default=None,
        help="Port to bind for HTTP-based transports.",
    )
    parser.add_argument(
        "--mount-path",
        default=None,
        help="Optional mount path for SSE transport.",
    )
    return parser


def main() -> None:
    args = build_parser().parse_args()
    if args.host:
        mcp.settings.host = args.host
    if args.port:
        mcp.settings.port = args.port

    if args.transport == "stdio":
        print(
            "Starting Personal Wiki Agent MCP server in stdio mode.",
            file=sys.stderr,
        )
        print(
            "This mode is for MCP clients that launch the server as a subprocess, such as Claude Desktop.",
            file=sys.stderr,
        )
        print(
            "For a connectable local URL, rerun with: personal-wiki-agent-mcp --transport streamable-http",
            file=sys.stderr,
        )
        mcp.run(transport="stdio")
        return

    if args.transport == "sse":
        print(
            f"Starting Personal Wiki Agent MCP server in SSE mode at http://{mcp.settings.host}:{mcp.settings.port}{mcp.settings.sse_path}",
            file=sys.stderr,
        )
        mcp.run(transport="sse", mount_path=args.mount_path)
        return

    print(
        f"Starting Personal Wiki Agent MCP server in streamable HTTP mode at http://{mcp.settings.host}:{mcp.settings.port}{mcp.settings.streamable_http_path}",
        file=sys.stderr,
    )
    mcp.run(transport="streamable-http")


if __name__ == "__main__":
    main()
