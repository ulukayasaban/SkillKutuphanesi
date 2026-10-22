# Request standards

## Base URLs

Etsy Open API v3 endpoints are accessible at:

- `https://api.etsy.com/v3/`
- `https://openapi.etsy.com/v3/`

The hostnames are considered equivalent in Etsy documentation.

Many examples use the “application” context:

- `https://api.etsy.com/v3/application/<resource>...`

## Required headers

Every request to a v3 endpoint must include:

1) API key header (required for all endpoints):

- `x-api-key: <keystring>:<shared-secret>`

2) OAuth header (required for endpoints that require scopes):

- `Authorization: Bearer <numeric_user_id>.<access_token>`

## Encoding and payload formats

- UTF-8 is used for network communication.
- Many write endpoints expect `application/x-www-form-urlencoded`.
- Some endpoints accept JSON payloads; consult the OpenAPI reference for the specific operation.

## Practical gotchas

- Missing the shared secret in `x-api-key` will fail on v3.
- The Authorization header is **not** just the access token; it must be `user_id.access_token`.
