#!/usr/bin/env python3
"""Open a HEADED Chromium browser against the same persistent profile that
scripts/fetch_url.py uses, so you can log in to sites (Twitter/X, paywalled
subs, etc.) by hand. Once you log in and press Enter in this terminal, the
cookies and localStorage are flushed to the profile directory and every
subsequent headless run of fetch_url.py will be authenticated.

Dependencies:
    pip install playwright
    playwright install chromium

Usage:
    # Default: opens x.com/login
    python scripts/browser_login.py

    # Log into any site
    python scripts/browser_login.py --url https://substack.com/sign-in
    python scripts/browser_login.py --url https://news.ycombinator.com/login

    # Override the profile directory (rare)
    python scripts/browser_login.py --profile-dir ~/.cache/some-other-profile

The browser stays open until you press Enter in the terminal. Log in normally
in the real browser window, then come back here and hit Enter.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from _lib import load_config  # type: ignore


DEFAULT_LOGIN_URL = "https://x.com/login"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--url",
        default=DEFAULT_LOGIN_URL,
        help=f"URL to open in the headed browser (default: {DEFAULT_LOGIN_URL}).",
    )
    parser.add_argument(
        "--profile-dir",
        default=None,
        help="Override the profile directory from config.yml.",
    )
    args = parser.parse_args()

    cfg = load_config()
    fetch_cfg = cfg.get("fetch_url") or {}
    raw_profile = (
        args.profile_dir
        or fetch_cfg.get("profile_dir")
        or "~/.cache/ai-wiki-playwright"
    )
    profile_dir = Path(str(raw_profile)).expanduser()
    profile_dir.mkdir(parents=True, exist_ok=True)

    try:
        from playwright.sync_api import sync_playwright  # type: ignore
    except ImportError:
        print(
            "error: playwright is not installed. Run:\n"
            "    pip install playwright\n"
            "    playwright install chromium",
            file=sys.stderr,
        )
        return 2

    print(f"Profile dir: {profile_dir}", file=sys.stderr)
    print(f"Opening:     {args.url}", file=sys.stderr)
    print(
        "A Chromium window will open. Log in manually, then CLOSE THE "
        "BROWSER WINDOW to save cookies and exit (Ctrl+C here also works).",
        file=sys.stderr,
    )

    with sync_playwright() as p:
        context = p.chromium.launch_persistent_context(
            user_data_dir=str(profile_dir),
            headless=False,
            viewport={"width": 1280, "height": 900},
            user_agent=(
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/125.0.0.0 Safari/537.36"
            ),
        )
        page = context.new_page()
        try:
            page.goto(args.url, timeout=60_000, wait_until="domcontentloaded")
        except Exception as e:  # noqa: BLE001
            print(f"warn: initial navigation failed ({e}); browser is still open.", file=sys.stderr)

        # Block until the user closes the window. We cannot rely on
        # stdin/input(): when this script is run via Claude Code's `!` prefix
        # (or any non-interactive shell), stdin is not a TTY and input()
        # returns EOF instantly, closing the browser before the user can log
        # in. Waiting for the page "close" event is stdin-independent.
        try:
            # timeout=0 disables the timeout in Playwright, giving an
            # effectively infinite wait.
            page.wait_for_event("close", timeout=0)
        except KeyboardInterrupt:
            print("", file=sys.stderr)
        except Exception as e:  # noqa: BLE001
            # Browser may have been closed out from under us; that's fine.
            print(f"(browser event loop ended: {e})", file=sys.stderr)

        try:
            context.close()
        except Exception:
            pass

    print("Done. Cookies and storage saved to the profile directory.", file=sys.stderr)
    print(
        "Next step: run `python scripts/fetch_url.py --type tweet --url <tweet-url>`.",
        file=sys.stderr,
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
