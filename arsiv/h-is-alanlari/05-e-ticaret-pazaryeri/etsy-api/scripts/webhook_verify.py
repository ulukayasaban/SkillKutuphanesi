"""Verify Etsy webhook signatures.

Etsy webhook requests include (headers are case-insensitive):

- x-etsy-signature
- x-etsy-webhook-id
- x-etsy-webhook-timestamp

Signing secret:
- Provided by Etsy, often prefixed with 'whsec_'.

Algorithm (as documented by Etsy):
1) Remove 'whsec_' prefix (if present) and Base64-decode the secret.
2) signed_content = webhook_id + '.' + webhook_timestamp + '.' + raw_body
3) signature = Base64Encode(HMAC_SHA256(secret_bytes, signed_content_bytes))
4) Constant-time compare signature to header x-etsy-signature
"""

from __future__ import annotations

import argparse
import base64
import hashlib
import hmac
import json
import sys
from typing import Any, Dict, Mapping


def _lower_keys(d: Mapping[str, Any]) -> Dict[str, Any]:
    return {str(k).lower(): v for k, v in d.items()}


def compute_signature(signing_secret: str, webhook_id: str, webhook_timestamp: str, raw_body: bytes) -> str:
    secret = signing_secret.strip()
    if secret.startswith("whsec_"):
        secret = secret[len("whsec_") :]

    secret_bytes = base64.b64decode(secret)

    signed_content = webhook_id + "." + webhook_timestamp + "."
    signed_bytes = signed_content.encode("utf-8") + raw_body

    digest = hmac.new(secret_bytes, signed_bytes, hashlib.sha256).digest()
    return base64.b64encode(digest).decode("ascii")


def verify_signature(signing_secret: str, headers: Mapping[str, str], raw_body: bytes) -> bool:
    h = _lower_keys(headers)
    sig = str(h.get("x-etsy-signature", "")).strip()
    webhook_id = str(h.get("x-etsy-webhook-id", "")).strip()
    ts = str(h.get("x-etsy-webhook-timestamp", "")).strip()

    if not (sig and webhook_id and ts):
        raise ValueError("Missing required webhook headers (x-etsy-signature, x-etsy-webhook-id, x-etsy-webhook-timestamp)")

    expected = compute_signature(signing_secret, webhook_id, ts, raw_body)
    return hmac.compare_digest(sig, expected)


def cmd_verify(args: argparse.Namespace) -> int:
    with open(args.headers_json, "r", encoding="utf-8") as f:
        headers = json.load(f)
    if not isinstance(headers, dict):
        raise SystemExit("headers.json must be a JSON object (dictionary)")

    with open(args.body_file, "rb") as f:
        body = f.read()

    ok = verify_signature(args.secret, {str(k): str(v) for k, v in headers.items()}, body)
    sys.stdout.write("VALID\n" if ok else "INVALID\n")
    return 0 if ok else 1


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="webhook_verify.py", description="Verify Etsy webhook signatures")
    sub = p.add_subparsers(dest="cmd", required=True)

    v = sub.add_parser("verify", help="Verify a webhook signature")
    v.add_argument("--secret", required=True, help="Webhook signing secret (whsec_...)")
    v.add_argument("--headers-json", required=True, help="Path to JSON file containing webhook headers")
    v.add_argument("--body-file", required=True, help="Path to raw request body file")
    v.set_defaults(func=cmd_verify)

    return p


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    return int(args.func(args))


if __name__ == "__main__":
    raise SystemExit(main())
