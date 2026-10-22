# OpenAPI reference and spec snapshot

Etsy publishes an OpenAPI specification and an online API reference.

## Online API reference

- https://developers.etsy.com/documentation/reference

## OpenAPI spec JSON

- https://www.etsy.com/openapi/generated/oas/3.0.0.json

## Offline snapshot

This repo includes `scripts/fetch_openapi_spec.py` to download and cache the spec locally for offline agent usage.

The spec (if downloaded) is stored at:

- `references/openapi/etsy-openapi-3.0.0.json`

You can then build your own local search tooling (e.g., grep, jq, small Python scripts) to find endpoints and schemas.
