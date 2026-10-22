# Webhooks

Etsy Open API v3 supports webhooks to notify your system about events.

## Concepts

- **Endpoints**: destination URLs where Etsy delivers webhook messages.
- **Events**: actions/changes that trigger a webhook delivery.
- **Deliveries**: each occurrence of an event causes a delivery to your endpoint.
- **Signing secrets**: validate authenticity of webhook requests.
- **Retries**: Etsy retries delivery if your endpoint fails to acknowledge.

## Signature verification (Etsy-documented approach)

Etsy provides:

- a signing secret with prefix `whsec_...`
- a signature header `x-etsy-signature`
- additional headers:
  - `x-etsy-webhook-id`
  - `x-etsy-webhook-timestamp`

High-level algorithm:

1. Remove `whsec_` prefix and Base64-decode the remaining secret.
2. Build `signed_content`:

   `webhook-id + "." + webhook-timestamp + "." + raw_body`

3. Compute HMAC-SHA256 over `signed_content` using the decoded secret.
4. Base64-encode the digest.
5. Compare to the `x-etsy-signature` header using a constant-time comparison.

See `scripts/webhook_verify.py`.
