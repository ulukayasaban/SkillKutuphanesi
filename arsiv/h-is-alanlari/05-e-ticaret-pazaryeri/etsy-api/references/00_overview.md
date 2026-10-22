# Etsy Open API v3 — Skill Reference Overview

This `references/` folder is designed to be **agent-readable**.

Start with:

1. `02_authentication.md` — OAuth 2.0 + PKCE + header formats
2. `03_request_standards.md` — required headers, base URLs, encoding
3. `04_rate_limits.md` — QPS/QPD, sliding window, 429 retry strategy
4. `08_common_workflows.md` — practical API flows (listings, inventory, receipts)
5. `05_webhooks.md` — webhook concepts + signature verification

If you need a full endpoint list, use the live OpenAPI reference and/or download the spec via `scripts/fetch_openapi_spec.py`.
