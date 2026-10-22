"""CLI utility for making Etsy Open API v3 calls with correct headers.

Examples:

    # Public endpoint (x-api-key only)
    python etsy_cli.py request GET /v3/application/listings?state=active

    # Scoped endpoint (requires ETSY_OAUTH_USER_ID + ETSY_OAUTH_ACCESS_TOKEN)
    python etsy_cli.py request GET /v3/application/users/me --oauth

"""

from __future__ import annotations

import argparse
import json
import os
import sys
from typing import Any, Dict, List, Mapping, Optional, Tuple

from etsy_http import EtsyHttpClient, EtsyResponse


def _read_at_path(value: str) -> str:
    if value.startswith("@"):
        path = value[1:]
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    return value


def _parse_headers(items: Optional[List[str]]) -> Dict[str, str]:
    out: Dict[str, str] = {}
    if not items:
        return out
    for item in items:
        if ":" in item:
            k, v = item.split(":", 1)
        elif "=" in item:
            k, v = item.split("=", 1)
        else:
            raise SystemExit(f"Invalid --header value (expected key:value): {item}")
        out[k.strip()] = v.strip()
    return out


def _parse_form(items: Optional[List[str]]) -> Dict[str, str]:
    out: Dict[str, str] = {}
    if not items:
        return out
    for item in items:
        if "=" not in item:
            raise SystemExit(f"Invalid --form value (expected key=value): {item}")
        k, v = item.split("=", 1)
        out[k.strip()] = v.strip()
    return out


def _print_response(resp: EtsyResponse, *, pretty: bool = True) -> None:
    sys.stdout.write(f"Status: {resp.status_code}\n")
    rl = resp.rate_limit_headers()
    if rl:
        sys.stdout.write("Rate-limit / control headers:\n")
        for k, v in sorted(rl.items(), key=lambda kv: kv[0].lower()):
            sys.stdout.write(f"  {k}: {v}\n")

    body_text = resp.text()
    # Try pretty JSON first
    if pretty:
        try:
            data = json.loads(body_text)
            sys.stdout.write(json.dumps(data, indent=2, ensure_ascii=False))
            sys.stdout.write("\n")
            return
        except Exception:
            pass

    sys.stdout.write(body_text)
    if not body_text.endswith("\n"):
        sys.stdout.write("\n")


def cmd_request(args: argparse.Namespace) -> int:
    client = EtsyHttpClient(api_base_url=args.base_url)

    json_body: Optional[Any] = None
    form_body: Optional[Dict[str, str]] = None
    raw_body: Optional[bytes] = None

    if args.body_file:
        with open(args.body_file, "rb") as f:
            raw_body = f.read()
    elif args.data:
        data_str = _read_at_path(args.data)
        try:
            json_body = json.loads(data_str)
        except Exception as e:
            raise SystemExit(f"--data must be valid JSON (or @file containing JSON). Error: {e}")
    elif args.form:
        form_body = _parse_form(args.form)

    extra_headers = _parse_headers(args.header)

    resp = client.request(
        method=args.method,
        path_or_url=args.path,
        use_oauth=bool(args.oauth),
        json_body=json_body,
        form_body=form_body,
        raw_body=raw_body,
        extra_headers=extra_headers,
        max_retries=args.max_retries,
    )

    _print_response(resp, pretty=not args.no_pretty)
    return 0


def cmd_env(args: argparse.Namespace) -> int:
    required = ["ETSY_KEYSTRING", "ETSY_SHARED_SECRET"]
    optional = ["ETSY_OAUTH_USER_ID", "ETSY_OAUTH_ACCESS_TOKEN", "ETSY_OAUTH_REFRESH_TOKEN", "ETSY_REDIRECT_URI"]
    missing = [k for k in required if not os.getenv(k)]
    sys.stdout.write("Required env vars:\n")
    for k in required:
        sys.stdout.write(f"  {k}: {'SET' if os.getenv(k) else 'MISSING'}\n")
    sys.stdout.write("Optional env vars:\n")
    for k in optional:
        sys.stdout.write(f"  {k}: {'SET' if os.getenv(k) else 'MISSING'}\n")
    if missing:
        sys.stdout.write("\nMissing required env vars: " + ", ".join(missing) + "\n")
        return 2
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="etsy_cli.py", description="Etsy Open API v3 CLI (rate-limit aware)")
    sub = p.add_subparsers(dest="cmd", required=True)

    p_req = sub.add_parser("request", help="Make an Etsy API request")
    p_req.add_argument("method", help="HTTP method (GET, POST, PUT, DELETE, etc)")
    p_req.add_argument("path", help="Path (e.g. /v3/application/listings?state=active) or full URL")
    p_req.add_argument("--base-url", default=None, help="Override API base URL (default: ETSY_API_BASE_URL or https://api.etsy.com)")
    p_req.add_argument("--oauth", action="store_true", help="Include Authorization: Bearer user_id.token")
    p_req.add_argument("--data", help="JSON body as string, or @file.json")
    p_req.add_argument("--form", action="append", help="Form field key=value (repeatable)")
    p_req.add_argument("--body-file", help="Raw body file to send as-is")
    p_req.add_argument("--header", action="append", help="Extra header key:value (repeatable)")
    p_req.add_argument("--max-retries", type=int, default=3, help="Max retries on HTTP 429 / transient errors")
    p_req.add_argument("--no-pretty", action="store_true", help="Do not pretty-print JSON responses")
    p_req.set_defaults(func=cmd_request)

    p_env = sub.add_parser("env", help="Show required environment variables (redacted)")
    p_env.set_defaults(func=cmd_env)

    return p


def main(argv: Optional[list[str]] = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    return int(args.func(args))


if __name__ == "__main__":
    raise SystemExit(main())
