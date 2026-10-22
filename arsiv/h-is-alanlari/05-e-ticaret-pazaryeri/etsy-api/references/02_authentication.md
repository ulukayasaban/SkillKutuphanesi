# Authentication (OAuth 2.0 Authorization Code + PKCE)

Etsy Open API v3 uses **OAuth 2.0 Authorization Code Grants** for user-scoped access.

## Key facts

- Authorization endpoint (user approval):
  - `https://www.etsy.com/oauth/connect`

- Token endpoint (access token, refresh token, token exchange):
  - `https://api.etsy.com/v3/public/oauth/token`

- PKCE is required:
  - Generate a `code_verifier`
  - Create a `code_challenge` = base64url(SHA256(code_verifier))
  - Send `code_challenge` with the auth request, and `code_verifier` when exchanging the code

## Required inputs

- `client_id`: your Etsy app keystring
- `redirect_uri`: must be HTTPS and must match the app configuration
- `scope`: space-separated scopes (URL-encoded in the auth URL)
- `state`: CSRF protection value
- `code_challenge`: PKCE challenge

## Refresh tokens

- Etsy supports refresh grants.
- You cannot change scopes when refreshing; refresh token scope is fixed to the original grant.

## Token exchange (OAuth 1.0 → OAuth 2.0)

Etsy supports exchanging legacy OAuth 1.0 tokens for OAuth 2.0 tokens via the same token endpoint.

## Environment variables used by scripts

- `ETSY_KEYSTRING`
- `ETSY_SHARED_SECRET`
- `ETSY_OAUTH_USER_ID`
- `ETSY_OAUTH_ACCESS_TOKEN`
- `ETSY_OAUTH_REFRESH_TOKEN`
- `ETSY_REDIRECT_URI`

See `scripts/oauth_pkce.py` for helper commands.
