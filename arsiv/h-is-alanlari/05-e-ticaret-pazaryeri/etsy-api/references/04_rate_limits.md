# Rate limits

Etsy Open API v3 uses **application-based** rate limits, consisting of:

- QPS: Queries Per Second
- QPD: Queries Per Day

## Important mechanics

- QPS and QPD apply:
  - per API key (public auth)
  - per OAuth access token (private auth)
- QPD uses a **rolling 24-hour sliding window** rather than a fixed midnight reset.

## Rate limit headers (from Etsy docs)

Etsy documents headers on successful responses such as:

- `x-limit-per-second`
- `x-remaining-this-second` (Etsy docs page displays this label truncated in some renderings)
- `x-limit-per-day`
- `x-remaining-today`

When you exceed limits, Etsy returns:

- HTTP `429`
- `retry-after` header with estimated seconds to wait

## Recommended client behavior

- Read the remaining-per-second header and throttle proactively.
- On 429, honor `retry-after`, and also apply exponential backoff + jitter to prevent retry storms.
- Cache frequently-read resources (shops, shipping profiles, taxonomy, etc.) to reduce QPD usage.
