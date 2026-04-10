#!/usr/bin/env python3
"""Fetch a URL using a real browser (Playwright / Chromium) and save it as
markdown into the appropriate raw/ subfolder.

Unlike plain HTTP fetch, this runs a full Chromium instance with JS execution,
which avoids most bot blocks. With --profile, it uses a persistent profile dir,
so logged-in sites (Twitter, paywalled subs) keep working across runs.

Dependencies:
    pip install playwright markdownify readability-lxml pyyaml
    playwright install chromium

Usage:
    python scripts/fetch_url.py --type article --url https://example.com/post
    python scripts/fetch_url.py --type tweet --url https://twitter.com/handle/status/123
    python scripts/fetch_url.py --type repo --url https://github.com/owner/repo
    python scripts/fetch_url.py --type paper --url https://arxiv.org/abs/1234.5678

The script prints the saved file's relative path (from vault root) as its
last line on success, so the LLM can pick it up with `tail -1`.
"""

from __future__ import annotations

import argparse
import re
import sys
import unicodedata
from datetime import date
from pathlib import Path
from urllib.parse import urlparse

from _lib import VAULT_ROOT, load_config, relativize, resolve_path  # type: ignore


SOURCE_TYPE_FOLDERS = {
    "article": "raw/articles",
    "tweet": "raw/tweets",
    "paper": "raw/papers",
    "podcast": "raw/podcasts",
    "repo": "raw/repos",
    "newsletter": "raw/newsletters",
    "note": "raw/notes",
}


# ---------------------------------------------------------------------------
# Slug / filename helpers
# ---------------------------------------------------------------------------


def slugify(value: str, max_len: int = 60) -> str:
    value = unicodedata.normalize("NFKD", value).encode("ascii", "ignore").decode("ascii")
    value = re.sub(r"[^\w\s-]", "", value).strip().lower()
    value = re.sub(r"[-\s]+", "-", value)
    return value[:max_len].strip("-") or "untitled"


def default_slug_for_url(url: str, source_type: str) -> str:
    parsed = urlparse(url)
    host = parsed.netloc.replace("www.", "")
    path = parsed.path.strip("/").replace("/", "-")
    if source_type == "repo":
        # github.com/owner/repo -> owner-repo
        parts = [p for p in parsed.path.strip("/").split("/") if p]
        if len(parts) >= 2:
            return slugify(f"{parts[0]}-{parts[1]}")
    if source_type == "tweet":
        parts = [p for p in parsed.path.strip("/").split("/") if p]
        if parts:
            return slugify(f"{parts[0]}-{parts[-1]}")
    if path:
        return slugify(f"{host}-{path}")
    return slugify(host)


def build_filename(source_type: str, slug: str) -> str:
    today = date.today().isoformat()
    if source_type == "repo":
        # Repos don't get a date prefix — the slug IS owner-repo.
        return f"{slug}.md"
    return f"{today}-{slug}.md"


# ---------------------------------------------------------------------------
# HTML -> Markdown
# ---------------------------------------------------------------------------


# Length-based fallback thresholds. If readability returns markdown shorter
# than READABILITY_MIN_CHARS while body.innerText is at least
# INNERTEXT_MIN_CHARS *and* substantially longer than the readability output,
# we assume readability mis-identified the main article container and fall
# back to body.innerText. This trades formatting (headings, links) for
# accuracy on JS-rendered SPAs that confuse readability-lxml.
READABILITY_MIN_CHARS = 500
INNERTEXT_MIN_CHARS = 2000
INNERTEXT_RATIO = 4


def html_to_markdown(
    html: str,
    body_text: str,
    url: str,
    source_type: str,
) -> tuple[str, str]:
    """Return (title, markdown_body). Falls back gracefully if libs are missing.

    `body_text` is the rendered `document.body.innerText` from Playwright; it
    is used as a last-resort fallback when readability mis-extracts the page.
    """
    title = ""
    body_html = html

    try:
        from readability import Document  # type: ignore

        doc = Document(html)
        title = (doc.short_title() or "").strip()
        body_html = doc.summary(html_partial=True)
    except ImportError:
        pass
    except Exception as e:  # noqa: BLE001
        print(f"warn: readability failed: {e}", file=sys.stderr)

    try:
        from markdownify import markdownify as md  # type: ignore

        markdown = md(body_html, heading_style="ATX", strip=["script", "style"])
    except ImportError:
        # Fallback: crude tag strip.
        markdown = re.sub(r"<[^>]+>", "", body_html)

    # Tidy: collapse triple blank lines.
    markdown = re.sub(r"\n{3,}", "\n\n", markdown).strip()

    # Length-based fallback: readability sometimes returns only the footer or
    # a sidebar on JS-rendered SPAs (observed on harvey.ai). When that
    # happens, prefer body.innerText. We lose heading/link structure but get
    # the actual article body.
    if (
        len(markdown) < READABILITY_MIN_CHARS
        and len(body_text) >= INNERTEXT_MIN_CHARS
        and len(body_text) >= len(markdown) * INNERTEXT_RATIO
    ):
        print(
            f"warn: readability returned only {len(markdown)} chars but "
            f"body.innerText has {len(body_text)} chars — falling back to "
            "innerText. Heading and link structure will be lost; consider "
            "manually cleaning the raw file.",
            file=sys.stderr,
        )
        markdown = body_text.strip()

    return title, markdown


# ---------------------------------------------------------------------------
# Playwright fetch
# ---------------------------------------------------------------------------


def fetch_with_playwright(
    url: str,
    profile_dir: Path | None,
    timeout: int,
    wait_for: str,
) -> tuple[str, str, str]:
    """Return (page_title, raw_html, body_inner_text).

    `body_inner_text` is `document.body.innerText` after the page has
    settled — used as a fallback when readability mis-identifies the main
    content container on JS-rendered SPAs.
    """
    try:
        from playwright.sync_api import sync_playwright  # type: ignore
    except ImportError:
        print(
            "error: playwright is not installed. Run:\n"
            "    pip install playwright markdownify readability-lxml\n"
            "    playwright install chromium",
            file=sys.stderr,
        )
        sys.exit(2)

    with sync_playwright() as p:
        if profile_dir is not None:
            profile_dir.mkdir(parents=True, exist_ok=True)
            context = p.chromium.launch_persistent_context(
                user_data_dir=str(profile_dir),
                headless=True,
                viewport={"width": 1280, "height": 900},
                user_agent=(
                    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                    "AppleWebKit/537.36 (KHTML, like Gecko) "
                    "Chrome/125.0.0.0 Safari/537.36"
                ),
            )
            page = context.new_page()
        else:
            browser = p.chromium.launch(headless=True)
            context = browser.new_context(
                viewport={"width": 1280, "height": 900},
                user_agent=(
                    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                    "AppleWebKit/537.36 (KHTML, like Gecko) "
                    "Chrome/125.0.0.0 Safari/537.36"
                ),
            )
            page = context.new_page()

        page.goto(url, timeout=timeout * 1000, wait_until=wait_for)
        # Some sites lazy-load; give them a breath.
        try:
            page.wait_for_load_state("networkidle", timeout=5000)
        except Exception:
            pass
        title = page.title() or ""
        html = page.content()
        try:
            body_text = page.evaluate("() => document.body ? document.body.innerText : ''") or ""
        except Exception as e:  # noqa: BLE001
            print(f"warn: body.innerText extraction failed: {e}", file=sys.stderr)
            body_text = ""
        context.close()
        return title, html, body_text


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--type",
        required=True,
        choices=sorted(SOURCE_TYPE_FOLDERS.keys()),
        help="Source type — determines which raw/ subfolder the file goes into.",
    )
    parser.add_argument("--url", required=True, help="URL to fetch.")
    parser.add_argument(
        "--slug",
        default=None,
        help="Override the auto-generated slug. Otherwise derived from URL or title.",
    )
    parser.add_argument(
        "--no-profile",
        action="store_true",
        help="Disable the persistent Chromium profile (useful for CI or one-off runs).",
    )
    parser.add_argument(
        "--profile-dir",
        default=None,
        help="Override the profile directory from config.yml.",
    )
    parser.add_argument(
        "--wait-until",
        default=None,
        choices=["load", "domcontentloaded", "networkidle", "commit"],
        help=(
            "Override Playwright's wait_until strategy. Default: networkidle "
            "for most types, domcontentloaded for tweets (x.com never settles "
            "to networkidle because of long-poll connections)."
        ),
    )
    args = parser.parse_args()

    cfg = load_config()
    fetch_cfg = cfg.get("fetch_url") or {}
    timeout = int(fetch_cfg.get("timeout", 30))
    # Per-type wait strategy: tweets need domcontentloaded because x.com
    # holds long-poll connections open and never reaches networkidle.
    if args.wait_until:
        wait_for = args.wait_until
    elif args.type == "tweet":
        wait_for = "domcontentloaded"
    else:
        wait_for = str(fetch_cfg.get("wait_for", "networkidle"))

    if args.no_profile:
        profile_dir: Path | None = None
    else:
        raw_profile = args.profile_dir or fetch_cfg.get("profile_dir") or "~/.cache/ai-wiki-playwright"
        profile_dir = Path(str(raw_profile)).expanduser()

    target_dir = VAULT_ROOT / SOURCE_TYPE_FOLDERS[args.type]
    target_dir.mkdir(parents=True, exist_ok=True)

    print(f"Fetching {args.url} ...", file=sys.stderr)
    page_title, html, body_text = fetch_with_playwright(args.url, profile_dir, timeout, wait_for)

    title, body_md = html_to_markdown(html, body_text, args.url, args.type)
    if not title:
        title = page_title or "Untitled"

    slug = args.slug or default_slug_for_url(args.url, args.type)
    filename = build_filename(args.type, slug)
    out_path = target_dir / filename

    frontmatter = (
        "---\n"
        f"title: {title}\n"
        f"type: source\n"
        f"source_type: {args.type}\n"
        f"url: {args.url}\n"
        f"fetched: {date.today().isoformat()}\n"
        "---\n\n"
    )

    out_path.write_text(frontmatter + f"# {title}\n\n" + body_md + "\n", encoding="utf-8")

    print(f"Saved: {relativize(out_path)}", file=sys.stderr)
    # Last stdout line = path, so callers can capture it with tail -1.
    print(relativize(out_path))
    return 0


if __name__ == "__main__":
    sys.exit(main())
