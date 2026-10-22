"""Search a cached Etsy OpenAPI spec for endpoints and schemas.

Requires that you have downloaded the spec using:
    python fetch_openapi_spec.py

Usage:
    python openapi_search.py endpoint listing inventory
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Dict, List, Tuple


def load_spec(path: Path) -> Dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def normalize(s: str) -> str:
    return s.lower()


def main(argv: List[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="Search cached Etsy OpenAPI spec")
    p.add_argument(
        "--spec",
        default=None,
        help="Path to spec JSON (default: references/openapi/etsy-openapi-3.0.0.json)",
    )
    p.add_argument("terms", nargs="+", help="Search terms")
    args = p.parse_args(argv)

    skill_root = Path(__file__).resolve().parents[1]  # skills/etsy-api/scripts -> skills/etsy-api
    default_spec = skill_root / "references" / "openapi" / "etsy-openapi-3.0.0.json"
    spec_path = Path(args.spec) if args.spec else default_spec

    spec = load_spec(spec_path)

    terms = [normalize(t) for t in args.terms]
    paths = spec.get("paths", {})

    matches: List[Tuple[str, str, str]] = []

    for path, methods in paths.items():
        for method, op in methods.items():
            if method.lower() not in {"get", "post", "put", "patch", "delete", "options", "head"}:
                continue
            op_id = str(op.get("operationId", ""))
            desc = str(op.get("description", ""))
            hay = normalize(" ".join([path, method, op_id, desc, " ".join(op.get("tags", []) or [])]))
            if all(t in hay for t in terms):
                matches.append((method.upper(), path, op_id))

    if not matches:
        print("No matches.")
        return 1

    for method, path, op_id in matches:
        print(f"{method:6} {path}  ({op_id})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
