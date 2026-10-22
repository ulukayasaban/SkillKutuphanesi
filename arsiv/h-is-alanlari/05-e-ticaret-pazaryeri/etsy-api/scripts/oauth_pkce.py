"""OAuth 2.0 + PKCE helper utilities for Etsy Open API v3.

This module focuses on Etsy's Authorization Code flow with PKCE.

Commands:
- generate      -> output code_verifier + code_challenge
- auth-url      -> output an authorization URL (includes PKCE + state)
- exchange-code -> exchange authorization code for tokens
- refresh-token -> refresh tokens using refresh_token
- token-exchange-> exchange legacy OAuth 1.0 token for OAuth 2.0 token
"""

from __future__ import annotations

import argparse
import base64
import hashlib
import json
import os
import secrets
import string
import sys
from typing import Any, Dict, Optional

from etsy_http import EtsyHttpClient


AUTH_URL = "https://www.etsy.com/oauth/connect"
TOKEN_PATH = "/v3/public/oauth/token"


_PKCE_CHARS = string.ascii_letters + string.digits + "-._~"


def generate_code_verifier(length: int = 64) -> str:
    if not (43 <= length <= 128):
        raise ValueError("PKCE code_verifier length must be 43..128")
    return "".join(secrets.choice(_PKCE_CHARS) for _ in range(length))


def code_challenge_s256(code_verifier: str) -> str:
    digest = hashlib.sha256(code_verifier.encode("utf-8")).digest()
    return base64.urlsafe_b64encode(digest).rstrip(b"=").decode("ascii")


def _get_env(name: str, *, required: bool = True) -> Optional[str]:
    val = os.getenv(name)
    if required and not val:
        raise SystemExit(f"Missing required environment variable: {name}")
    return val


def cmd_generate(args: argparse.Namespace) -> int:
    verifier = generate_code_verifier(args.length)
    challenge = code_challenge_s256(verifier)
    out = {"code_verifier": verifier, "code_challenge": challenge, "method": "S256"}
    sys.stdout.write(json.dumps(out, indent=2) + "\n")
    return 0


def cmd_auth_url(args: argparse.Namespace) -> int:
    client_id = args.client_id or _get_env("ETSY_KEYSTRING")
    redirect_uri = args.redirect_uri or _get_env("ETSY_REDIRECT_URI")
    scopes = args.scopes.strip()
    if not scopes:
        raise SystemExit("--scopes is required and must be non-empty")

    state = args.state or secrets.token_urlsafe(24)
    verifier = generate_code_verifier(args.verifier_length)
    challenge = code_challenge_s256(verifier)

    params = {
        "response_type": "code",
        "client_id": client_id,
        "redirect_uri": redirect_uri,
        "scope": scopes,
        "state": state,
        "code_challenge": challenge,
    }
    # Some OAuth servers require this; Etsy docs focus on challenge generation,
    # but S256 is the de-facto PKCE method. Included for interoperability.
    if not args.no_challenge_method:
        params["code_challenge_method"] = "S256"

    import urllib.parse

    url = AUTH_URL + "?" + urllib.parse.urlencode(params, quote_via=urllib.parse.quote)

    out = {
        "auth_url": url,
        "state": state,
        "code_verifier": verifier,
        "code_challenge": challenge,
    }
    if args.write_verifier:
        with open(args.write_verifier, "w", encoding="utf-8") as f:
            f.write(verifier)
    sys.stdout.write(json.dumps(out, indent=2) + "\n")
    return 0


def cmd_exchange_code(args: argparse.Namespace) -> int:
    code = args.code
    if not code:
        raise SystemExit("--code is required")

    client_id = args.client_id or _get_env("ETSY_KEYSTRING")
    redirect_uri = args.redirect_uri or _get_env("ETSY_REDIRECT_URI")

    verifier = args.verifier
    if not verifier and args.verifier_file:
        with open(args.verifier_file, "r", encoding="utf-8") as f:
            verifier = f.read().strip()
    if not verifier:
        raise SystemExit("Provide --verifier or --verifier-file (PKCE code_verifier is required).")

    # Token endpoint is on api.etsy.com; include x-api-key header as per request standards.
    client = EtsyHttpClient(api_base_url=args.api_base_url or "https://api.etsy.com")

    form = {
        "grant_type": "authorization_code",
        "client_id": client_id,
        "redirect_uri": redirect_uri,
        "code": code,
        "code_verifier": verifier,
    }

    resp = client.request("POST", TOKEN_PATH, form_body=form, use_oauth=False, max_retries=args.max_retries)
    sys.stdout.write(resp.text() + "\n")
    return 0


def cmd_refresh_token(args: argparse.Namespace) -> int:
    client_id = args.client_id or _get_env("ETSY_KEYSTRING")
    refresh_token = args.refresh_token or os.getenv("ETSY_OAUTH_REFRESH_TOKEN")
    if not refresh_token:
        raise SystemExit("Provide --refresh-token or set ETSY_OAUTH_REFRESH_TOKEN")

    client = EtsyHttpClient(api_base_url=args.api_base_url or "https://api.etsy.com")
    form = {
        "grant_type": "refresh_token",
        "client_id": client_id,
        "refresh_token": refresh_token,
    }
    resp = client.request("POST", TOKEN_PATH, form_body=form, use_oauth=False, max_retries=args.max_retries)
    sys.stdout.write(resp.text() + "\n")
    return 0


def cmd_token_exchange(args: argparse.Namespace) -> int:
    client_id = args.client_id or _get_env("ETSY_KEYSTRING")
    legacy_token = args.legacy_token
    if not legacy_token:
        raise SystemExit("--legacy-token is required")

    client = EtsyHttpClient(api_base_url=args.api_base_url or "https://api.etsy.com")
    form = {
        "grant_type": "token_exchange",
        "client_id": client_id,
        "legacy_token": legacy_token,
    }
    resp = client.request("POST", TOKEN_PATH, form_body=form, use_oauth=False, max_retries=args.max_retries)
    sys.stdout.write(resp.text() + "\n")
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="oauth_pkce.py", description="Etsy OAuth 2.0 + PKCE helpers")
    sub = p.add_subparsers(dest="cmd", required=True)

    p_gen = sub.add_parser("generate", help="Generate PKCE code_verifier and code_challenge")
    p_gen.add_argument("--length", type=int, default=64, help="code_verifier length (43..128)")
    p_gen.set_defaults(func=cmd_generate)

    p_auth = sub.add_parser("auth-url", help="Generate an Etsy OAuth authorization URL (includes PKCE)")
    p_auth.add_argument("--client-id", help="Override client_id (default: ETSY_KEYSTRING)")
    p_auth.add_argument("--redirect-uri", help="Override redirect_uri (default: ETSY_REDIRECT_URI)")
    p_auth.add_argument("--scopes", required=True, help="Space-separated scopes (e.g. 'shops_r shops_w')")
    p_auth.add_argument("--state", help="Optional state parameter (CSRF protection)")
    p_auth.add_argument("--verifier-length", type=int, default=64, help="PKCE verifier length")
    p_auth.add_argument("--write-verifier", help="Write code_verifier to a file for later exchange")
    p_auth.add_argument("--no-challenge-method", action="store_true", help="Do not include code_challenge_method=S256")
    p_auth.set_defaults(func=cmd_auth_url)

    p_ex = sub.add_parser("exchange-code", help="Exchange an authorization code for OAuth tokens")
    p_ex.add_argument("--code", required=True, help="Authorization code returned to your redirect_uri")
    p_ex.add_argument("--verifier", help="PKCE code_verifier")
    p_ex.add_argument("--verifier-file", help="Read PKCE code_verifier from a file")
    p_ex.add_argument("--client-id", help="Override client_id (default: ETSY_KEYSTRING)")
    p_ex.add_argument("--redirect-uri", help="Override redirect_uri (default: ETSY_REDIRECT_URI)")
    p_ex.add_argument("--api-base-url", help="Override base URL for token endpoint (default: https://api.etsy.com)")
    p_ex.add_argument("--max-retries", type=int, default=3, help="Retries on 429")
    p_ex.set_defaults(func=cmd_exchange_code)

    p_rt = sub.add_parser("refresh-token", help="Refresh an OAuth token using refresh_token")
    p_rt.add_argument("--refresh-token", help="Refresh token (default: ETSY_OAUTH_REFRESH_TOKEN)")
    p_rt.add_argument("--client-id", help="Override client_id (default: ETSY_KEYSTRING)")
    p_rt.add_argument("--api-base-url", help="Override base URL for token endpoint (default: https://api.etsy.com)")
    p_rt.add_argument("--max-retries", type=int, default=3, help="Retries on 429")
    p_rt.set_defaults(func=cmd_refresh_token)

    p_tx = sub.add_parser("token-exchange", help="Exchange legacy OAuth 1.0 token for OAuth 2.0 token")
    p_tx.add_argument("--legacy-token", required=True, help="Legacy OAuth 1.0 token")
    p_tx.add_argument("--client-id", help="Override client_id (default: ETSY_KEYSTRING)")
    p_tx.add_argument("--api-base-url", help="Override base URL for token endpoint (default: https://api.etsy.com)")
    p_tx.add_argument("--max-retries", type=int, default=3, help="Retries on 429")
    p_tx.set_defaults(func=cmd_token_exchange)

    return p


def main(argv: Optional[list[str]] = None) -> int:
    args = build_parser().parse_args(argv)
    return int(args.func(args))


if __name__ == "__main__":
    raise SystemExit(main())
