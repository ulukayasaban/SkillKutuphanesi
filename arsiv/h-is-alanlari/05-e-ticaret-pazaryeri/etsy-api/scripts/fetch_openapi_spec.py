"""Download Etsy Open API v3 OpenAPI spec JSON for offline use.

Default source:
- https://www.etsy.com/openapi/generated/oas/3.0.0.json

Output:
- skills/etsy-api/references/openapi/etsy-openapi-3.0.0.json
- skills/etsy-api/references/openapi/etsy-openapi-3.0.0.json.sha256

Note:
- This script requires outbound internet access.
"""

from __future__ import annotations

import argparse
import hashlib
import os
import sys
import urllib.request
from pathlib import Path


DEFAULT_URL = "https://www.etsy.com/openapi/generated/oas/3.0.0.json"


def download(url: str) -> bytes:
    req = urllib.request.Request(url, headers={"accept": "application/json", "user-agent": "etsy-api-skill/1.0"})
    with urllib.request.urlopen(req, timeout=60) as resp:
        return resp.read()


def sha256_hex(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="Fetch Etsy OpenAPI spec JSON")
    p.add_argument("--url", default=DEFAULT_URL, help="Spec URL")
    p.add_argument(
        "--out",
        default=None,
        help="Output path (default: skills/etsy-api/references/openapi/etsy-openapi-3.0.0.json)",
    )
    args = p.parse_args(argv)

    repo_root = Path(__file__).resolve().parents[2]  # skills/etsy-api/scripts -> repo root
    default_out = repo_root / "skills" / "etsy-api" / "references" / "openapi" / "etsy-openapi-3.0.0.json"
    out_path = Path(args.out) if args.out else default_out
    out_path.parent.mkdir(parents=True, exist_ok=True)

    sys.stdout.write(f"Downloading: {args.url}\n")
    data = download(args.url)

    out_path.write_bytes(data)
    digest = sha256_hex(data)
    (out_path.with_suffix(out_path.suffix + ".sha256")).write_text(digest + "\n", encoding="utf-8")

    sys.stdout.write(f"Wrote: {out_path}\n")
    sys.stdout.write(f"SHA256: {digest}\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
