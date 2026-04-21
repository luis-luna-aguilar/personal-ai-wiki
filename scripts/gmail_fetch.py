#!/usr/bin/env python3
"""Fetch emails from a Gmail account and save each as an individual raw/ file.

Each email becomes its own markdown file:
  - Newsletters → raw/newsletters/YYYY-MM-DD-<slug>.md
  - Email Me URL forwards → raw/articles/ or raw/tweets/ (stub with URL, not yet fetched)

After saving, every fetched email is labelled "AI-Wiki-Processed" and moved out
of the inbox in a single Gmail API call. A triage file is generated at
proposals/triage/ referencing all saved source files.

Scope used: gmail.modify (required to apply labels and remove INBOX label).
The script never calls compose or send methods.

Dependencies:
    pip install google-auth-oauthlib google-api-python-client beautifulsoup4 markdownify

Setup:
    1. In Google Cloud Console: enable Gmail API, create OAuth2 Desktop credentials.
    2. Save the downloaded JSON to:
         scripts/gmail_credentials/ai-client.json       (AI Gmail account)
         scripts/gmail_credentials/personal-client.json (personal Gmail account)
    3. First run opens a browser for OAuth consent. Token is cached automatically at
         scripts/gmail_credentials/ai-token.json
         scripts/gmail_credentials/personal-token.json

Usage:
    python scripts/gmail_fetch.py --account ai --days 1
    python scripts/gmail_fetch.py --account personal --week 2026-W15
"""

from __future__ import annotations

import argparse
import base64
import re
import sys
import unicodedata
from datetime import date, datetime, timedelta, timezone
from email import message_from_bytes
from email.header import decode_header as _decode_header
from pathlib import Path
from urllib.parse import urlparse

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _lib import VAULT_ROOT, load_config  # type: ignore


CREDS_DIR = VAULT_ROOT / "scripts" / "gmail_credentials"
TRIAGE_DIR = VAULT_ROOT / "proposals" / "triage"

GMAIL_SCOPES = ["https://www.googleapis.com/auth/gmail.modify"]
PROCESSED_LABEL_NAME = "AI-Wiki-Processed"

TWEET_URL_RE = re.compile(r"https?://(twitter\.com|x\.com)/\w+/status/\d+")
VIDEO_URL_RE = re.compile(
    r"https?://("
    r"(?:www\.)?youtube\.com/watch"
    r"|youtu\.be/"
    r"|(?:www\.)?vimeo\.com/\d"
    r"|(?:www\.)?twitch\.tv/"
    r"|(?:www\.)?loom\.com/share/"
    r"|(?:www\.)?wistia\.com/"
    r"|(?:www\.)?dailymotion\.com/video/"
    r")",
    re.IGNORECASE,
)
URL_RE = re.compile(r"https?://[^\s>\"'<\)]+")


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def slugify(value: str, max_len: int = 60) -> str:
    value = unicodedata.normalize("NFKD", value).encode("ascii", "ignore").decode("ascii")
    value = re.sub(r"[^\w\s-]", "", value).strip().lower()
    value = re.sub(r"[-\s]+", "-", value)
    return value[:max_len].strip("-") or "untitled"


def decode_header_str(raw: str | None) -> str:
    if not raw:
        return ""
    parts = _decode_header(raw)
    decoded = []
    for chunk, charset in parts:
        if isinstance(chunk, bytes):
            decoded.append(chunk.decode(charset or "utf-8", errors="replace"))
        else:
            decoded.append(chunk)
    return " ".join(decoded).strip()


def unique_path(path: Path) -> Path:
    if not path.exists():
        return path
    stem, suffix = path.stem, path.suffix
    counter = 1
    while True:
        candidate = path.with_name(f"{stem}-{counter}{suffix}")
        if not candidate.exists():
            return candidate
        counter += 1


# ---------------------------------------------------------------------------
# Gmail auth
# ---------------------------------------------------------------------------


def get_credentials(account: str):
    try:
        from google.auth.transport.requests import Request
        from google.oauth2.credentials import Credentials
        from google_auth_oauthlib.flow import InstalledAppFlow
    except ImportError:
        sys.exit(
            "Missing dependencies. Run:\n"
            "  pip install google-auth-oauthlib google-api-python-client"
        )

    client_file = CREDS_DIR / f"{account}-client.json"
    token_file = CREDS_DIR / f"{account}-token.json"

    if not client_file.exists():
        sys.exit(
            f"Client credentials not found: {client_file}\n"
            "Download OAuth2 Desktop credentials from Google Cloud Console and save there."
        )

    creds = None
    if token_file.exists():
        creds = Credentials.from_authorized_user_file(str(token_file), GMAIL_SCOPES)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(str(client_file), GMAIL_SCOPES)
            creds = flow.run_local_server(port=0)
        CREDS_DIR.mkdir(parents=True, exist_ok=True)
        token_file.write_text(creds.to_json())

    return creds


# ---------------------------------------------------------------------------
# Date range helpers
# ---------------------------------------------------------------------------


def parse_week(week_str: str) -> tuple[date, date]:
    """Parse 'YYYY-WNN' → (monday, sunday)."""
    year_str, week_str = week_str.split("-W")
    monday = date.fromisocalendar(int(year_str), int(week_str), 1)
    return monday, monday + timedelta(days=6)


def gmail_date_query(start: date, end: date) -> str:
    after = start.strftime("%Y/%m/%d")
    before = (end + timedelta(days=1)).strftime("%Y/%m/%d")
    return f"in:inbox after:{after} before:{before}"


# ---------------------------------------------------------------------------
# Email body extraction
# ---------------------------------------------------------------------------


def html_to_text(html_content: str) -> str:
    try:
        import markdownify
        return markdownify.markdownify(html_content, heading_style="ATX")
    except ImportError:
        pass
    clean = re.sub(r"<[^>]+>", " ", html_content)
    for entity, char in [("&nbsp;", " "), ("&amp;", "&"), ("&lt;", "<"), ("&gt;", ">"), ("&#39;", "'")]:
        clean = clean.replace(entity, char)
    return re.sub(r" {2,}", " ", clean).strip()


def get_email_body(msg) -> str:
    if msg.is_multipart():
        for part in msg.walk():
            if part.get_content_type() == "text/plain":
                payload = part.get_payload(decode=True)
                if payload:
                    return payload.decode(part.get_content_charset() or "utf-8", errors="replace")
        for part in msg.walk():
            if part.get_content_type() == "text/html":
                payload = part.get_payload(decode=True)
                if payload:
                    return html_to_text(payload.decode(part.get_content_charset() or "utf-8", errors="replace"))
    else:
        payload = msg.get_payload(decode=True)
        if payload:
            text = payload.decode(msg.get_content_charset() or "utf-8", errors="replace")
            return html_to_text(text) if msg.get_content_type() == "text/html" else text
    return ""


# ---------------------------------------------------------------------------
# Email type detection
# ---------------------------------------------------------------------------


def load_email_me_config() -> dict:
    cfg = load_config().get("gmail", {}).get("email_me", {})
    return {"senders": cfg.get("senders", [])}


def load_whitelist() -> list[str]:
    senders = load_config().get("gmail", {}).get("whitelist", {}).get("senders", [])
    return [s.lower() for s in senders]


def is_whitelisted(sender: str, whitelist: list[str]) -> bool:
    sender_lower = sender.lower()
    return any(addr in sender_lower for addr in whitelist)


def detect_email_type(sender: str, body: str, email_me_cfg: dict) -> str:
    """Return 'email_me' or 'newsletter'."""
    sender_lower = sender.lower()
    for pattern in email_me_cfg["senders"]:
        if pattern.lower() in sender_lower:
            return "email_me"

    # Body is essentially a bare URL (fallback for unlisted senders)
    stripped = body.strip()
    if len(stripped) < 250 and URL_RE.search(stripped):
        non_url = URL_RE.sub("", stripped).strip()
        if len(non_url) < 30:
            return "email_me"

    return "newsletter"


def extract_primary_url(subject: str, body: str) -> str | None:
    for text in (subject, body):
        urls = URL_RE.findall(text)
        meaningful = [
            u for u in urls
            if not re.search(r"unsubscribe|tracking|pixel|mailchimp|sendgrid|list-manage|click\.", u, re.I)
        ]
        if meaningful:
            return meaningful[0]
    return None


# ---------------------------------------------------------------------------
# Saving files
# ---------------------------------------------------------------------------


def save_newsletter(sender: str, subject: str, date_received: date, body: str, msg_id: str) -> Path:
    target = VAULT_ROOT / "raw" / "newsletters"
    target.mkdir(parents=True, exist_ok=True)

    slug = slugify(subject[:50])
    path = unique_path(target / f"{date_received.isoformat()}-{slug}.md")

    path.write_text(
        f"""---
title: "{subject.replace('"', "'")}"
type: newsletter
sender: "{sender.replace('"', "'")}"
received: {date_received.isoformat()}
gmail_id: {msg_id}
---

# {subject}

**From:** {sender}
**Date:** {date_received.isoformat()}

{body.strip()}
""",
        encoding="utf-8",
    )
    return path


def save_email_me(url: str, subject: str, date_received: date, body: str, msg_id: str) -> tuple[Path, str]:
    if TWEET_URL_RE.search(url):
        target = VAULT_ROOT / "raw" / "tweets"
        raw_type = "tweet"
    else:
        target = VAULT_ROOT / "raw" / "articles"
        raw_type = "article"

    target.mkdir(parents=True, exist_ok=True)
    parsed = urlparse(url)
    domain_slug = slugify(parsed.netloc.replace("www.", ""), max_len=20)
    path_slug = slugify(parsed.path.strip("/"), max_len=30) or domain_slug
    combined = f"{domain_slug}-{path_slug}" if path_slug != domain_slug else domain_slug
    path = unique_path(target / f"{date_received.isoformat()}-{combined}.md")

    display_title = subject or url
    path.write_text(
        f"""---
title: "{display_title.replace('"', "'")}"
type: {raw_type}
url: {url}
received: {date_received.isoformat()}
gmail_id: {msg_id}
fetched: false
---

# {display_title}

**URL:** {url}
**Forwarded:** {date_received.isoformat()}

{body.strip()}
""",
        encoding="utf-8",
    )
    return path, raw_type


# ---------------------------------------------------------------------------
# Triage generation
# ---------------------------------------------------------------------------


def generate_digest_manifest(
    saved_files: list[tuple[Path, str, str]],  # (path, email_type, subject)
    skipped_videos: list[tuple[str, str]],       # (url, subject)
    start: date,
    end: date,
    account: str,
    args_week: str | None = None,
) -> Path:
    """Write a skeleton manifest listing all saved sources.

    The signals section is intentionally left empty. Claude fills it in
    during the 'triage this digest' workflow: fetching all URLs, reading
    all newsletters, grouping by topic, and writing consolidated entries.
    """
    TRIAGE_DIR.mkdir(parents=True, exist_ok=True)

    if start == end:
        label = start.isoformat()
        slug = f"{start.isoformat()}-{account}-digest"
    elif args_week:
        _, week_num, _ = start.isocalendar()
        label = f"{start.isoformat()} to {end.isoformat()}"
        slug = f"{start.year}-W{week_num:02d}-{account}-digest"
    else:
        label = f"{start.isoformat()} to {end.isoformat()}"
        slug = f"{start.isoformat()}-to-{end.isoformat()}-{account}-digest"

    manifest_path = unique_path(TRIAGE_DIR / f"{slug}.md")

    sources_block = "\n".join(
        f"  - {p.relative_to(VAULT_ROOT)}" for p, _, _ in saved_files
    )

    source_lines = []
    for path, email_type, subject in saved_files:
        rel = path.relative_to(VAULT_ROOT)
        tag = "url-fwd" if email_type == "email_me" else "newsletter"
        source_lines.append(f"- `{rel}` ({tag})")
    for url, subject in skipped_videos:
        source_lines.append(f"- {url} (video — skipped)")

    source_list = "\n".join(source_lines) if source_lines else "_none_"
    total = len(saved_files) + len(skipped_videos)

    manifest_path.write_text(
        f"""---
type: triage
sources:
{sources_block}
status: pending-analysis
period: "{label}"
account: {account}
---

# Email Digest — {account.capitalize()} — {label}

{total} sources fetched ({len(saved_files)} saved, {len(skipped_videos)} videos skipped).
Say **"triage this digest"** to have Claude fetch all URLs, read all newsletters,
group by topic, and generate a comprehensive triage with consolidated signals.

## Sources

{source_list}

## Signals

<!-- Claude fills this in during triage -->
""",
        encoding="utf-8",
    )
    return manifest_path


# ---------------------------------------------------------------------------
# Gmail API helpers
# ---------------------------------------------------------------------------


def fetch_all_message_ids(service, query: str) -> list[dict]:
    messages = []
    page_token = None
    while True:
        kwargs: dict = {"userId": "me", "q": query, "maxResults": 500}
        if page_token:
            kwargs["pageToken"] = page_token
        result = service.users().messages().list(**kwargs).execute()
        messages.extend(result.get("messages", []))
        page_token = result.get("nextPageToken")
        if not page_token:
            break
    return messages


def fetch_raw_message(service, msg_id: str) -> dict:
    return service.users().messages().get(userId="me", id=msg_id, format="raw").execute()


def get_or_create_label(service, name: str) -> str:
    """Return the label ID for `name`, creating it if it doesn't exist."""
    result = service.users().labels().list(userId="me").execute()
    for label in result.get("labels", []):
        if label["name"] == name:
            return label["id"]
    created = service.users().labels().create(
        userId="me",
        body={
            "name": name,
            "labelListVisibility": "labelShow",
            "messageListVisibility": "show",
        },
    ).execute()
    return created["id"]


def process_message(service, msg_id: str, processed_label_id: str) -> None:
    """Apply AI-Wiki-Processed label and remove from inbox in one call."""
    service.users().messages().modify(
        userId="me",
        id=msg_id,
        body={
            "addLabelIds": [processed_label_id],
            "removeLabelIds": ["INBOX"],
        },
    ).execute()


def internal_date_to_date(internal_date: str | int) -> date:
    ts = int(internal_date) / 1000
    return datetime.fromtimestamp(ts, tz=timezone.utc).date()


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def main() -> None:
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("--account", required=True, choices=["ai", "personal"])
    parser.add_argument("--days", type=int, help="Fetch last N days (1 = today only)")
    parser.add_argument("--week", help="Fetch a specific ISO week, e.g. 2026-W15")
    parser.add_argument("--no-triage", action="store_true", help="Skip triage file generation")
    args = parser.parse_args()

    if not args.days and not args.week:
        parser.error("Provide --days N or --week YYYY-WNN")

    today = date.today()
    if args.week:
        start, end = parse_week(args.week)
    else:
        end = today
        start = today - timedelta(days=args.days - 1)

    creds = get_credentials(args.account)

    try:
        from googleapiclient.discovery import build
    except ImportError:
        sys.exit("Run: pip install google-api-python-client")

    service = build("gmail", "v1", credentials=creds)
    email_me_cfg = load_email_me_config()
    whitelist = load_whitelist()

    processed_label_id = get_or_create_label(service, PROCESSED_LABEL_NAME)
    print(f"Label '{PROCESSED_LABEL_NAME}' ready (id: {processed_label_id})", file=sys.stderr)

    query = gmail_date_query(start, end)
    print(f"Querying {args.account} Gmail: {query}", file=sys.stderr)

    message_ids = fetch_all_message_ids(service, query)
    print(f"Found {len(message_ids)} messages", file=sys.stderr)

    saved: list[tuple[Path, str, str]] = []   # (path, type, subject)
    skipped_videos: list[tuple[str, str]] = []  # (url, subject)

    for item in message_ids:
        msg_id = item["id"]
        raw_msg = fetch_raw_message(service, msg_id)
        raw_bytes = base64.urlsafe_b64decode(raw_msg["raw"])
        msg = message_from_bytes(raw_bytes)

        subject = decode_header_str(msg.get("Subject", "")) or "(no subject)"
        sender = decode_header_str(msg.get("From", ""))
        date_received = internal_date_to_date(raw_msg.get("internalDate", 0)) or today

        if not is_whitelisted(sender, whitelist):
            print(f"  [ignored] {sender[:50]} — {subject[:50]}", file=sys.stderr)
            continue

        body = get_email_body(msg)
        email_type = detect_email_type(sender, body, email_me_cfg)

        if email_type == "email_me":
            url = extract_primary_url(subject, body)
            if not url:
                print(f"  [skip]       No URL found in: {subject}", file=sys.stderr)
                continue
            if VIDEO_URL_RE.search(url):
                skipped_videos.append((url, subject))
                print(f"  [video-skip] {subject[:60]}", file=sys.stderr)
                process_message(service, msg_id, processed_label_id)
            else:
                path, _ = save_email_me(url, subject, date_received, body, msg_id)
                saved.append((path, "email_me", subject))
                print(f"  [url-fwd]    {path.name}", file=sys.stderr)
        else:
            path = save_newsletter(sender, subject, date_received, body, msg_id)
            saved.append((path, "newsletter", subject))
            print(f"  [newsletter] {path.name}", file=sys.stderr)

        process_message(service, msg_id, processed_label_id)

    print(f"\nSaved {len(saved)} files, skipped {len(skipped_videos)} videos.", file=sys.stderr)

    if not args.no_triage and (saved or skipped_videos):
        manifest_path = generate_digest_manifest(saved, skipped_videos, start, end, args.account, args_week=args.week)
        print(manifest_path.relative_to(VAULT_ROOT))
    elif not saved and not skipped_videos:
        print("No emails matched — nothing to triage.")


if __name__ == "__main__":
    main()
