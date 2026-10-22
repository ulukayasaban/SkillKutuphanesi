# Terms and policies (highlights)

This is **not** legal advice. It is a practical summary of key operational constraints.

## API Testing Policy (high-level)

Etsy’s testing policy is designed to let you test on production while reducing fraud-like behavior.
Key guidelines include:

- Enable Developer Mode for your shop when testing.
- Create listings in **draft** state when possible.
- Use very low prices (e.g., < $1) for test listings and deactivate them after.
- Mark test listings clearly (e.g., include “test” in title/description).
- Avoid stock images in test listings.
- If a buyer accidentally purchases a test listing, cancel the transaction promptly and contact Etsy Support if needed.

## API Terms of Use (data freshness)

Etsy’s API terms include requirements around data freshness when you display Etsy content:
- listing content should not be displayed more than ~6 hours older than the Etsy site/app
- other Etsy content should not be displayed more than ~24 hours older than the Etsy site/app

Agent guidance:
- Cache aggressively to protect QPD, but design caches with policy-aware TTLs.
