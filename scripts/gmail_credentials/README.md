# Gmail credentials

Place your OAuth2 credentials here. Tokens are gitignored.

## Files expected

| File | What it is | How to get it |
|---|---|---|
| `ai-client.json` | OAuth2 Desktop app credentials for the AI Gmail account | Google Cloud Console → APIs & Services → Credentials → Create → OAuth client ID → Desktop app |
| `ai-token.json` | Cached OAuth token (auto-generated on first run) | Created automatically |

## Required Gmail API scope

Uses `gmail.modify`.

**Why not a narrower scope?** Applying a label to a message and removing it from the inbox both require the `messages.modify` API method, which needs `gmail.modify`. There is no narrower Gmail API scope that covers this.

**Note on Google's consent screen description:** Google describes `gmail.modify` as "Read, compose, and send emails." This is misleading — the script only calls read and `messages.modify` methods. It never calls compose or send. You can verify this by reading the source.

## Setup steps

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a project (or use an existing one)
3. Enable the **Gmail API**
4. Create OAuth2 credentials → Desktop app type
5. Copy `.env.example` to `.env` at the repo root and fill in `AI_GMAIL_CLIENT_ID` and `AI_GMAIL_CLIENT_SECRET`
6. Run `python scripts/gmail_fetch.py --days 1` — it will open a browser for consent on first run
