"""Example: list active listings (public endpoint example from Etsy docs).

Requirements:
- ETSY_KEYSTRING
- ETSY_SHARED_SECRET

Run:
    python skills/etsy-api/examples/list_active_listings.py
"""

import os
import sys
from pathlib import Path

# Add scripts/ to import path
scripts_dir = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(scripts_dir))

from etsy_http import EtsyHttpClient  # noqa: E402


def main() -> None:
    client = EtsyHttpClient()
    resp = client.request("GET", "/v3/application/listings", query={"state": "active"})
    print(resp.status_code)
    print(resp.text())


if __name__ == "__main__":
    main()
