# Error handling patterns

## Common HTTP status codes

- `200/201`: success
- `400`: malformed request (missing/invalid parameters)
- `401`: missing/invalid authentication
- `403`: insufficient scope or permission
- `404`: resource not found
- `409`: conflict
- `429`: rate limit exceeded (honor `retry-after`)
- `500`: server error

## 429 retry strategy

1. Parse `retry-after` (seconds)
2. Sleep for that duration (plus small jitter)
3. Retry with exponential backoff (cap retries)

Agent guidance:
- Never tight-loop on 429; always back off.
- Watch both QPS and QPD.
