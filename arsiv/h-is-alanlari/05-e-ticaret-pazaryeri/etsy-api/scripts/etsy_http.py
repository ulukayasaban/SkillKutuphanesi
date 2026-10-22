"""Low-dependency Etsy Open API v3 HTTP utilities.

Design goals:
- stdlib-first, but uses `requests` if available
- correct Etsy headers (x-api-key with keystring:secret, Authorization Bearer user_id.token)
- rate-limit aware retries for HTTP 429 (honor retry-after + exponential backoff)
- avoid logging secrets
"""

from __future__ import annotations

import base64
import json
import os
import random
import time
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass
from typing import Any, Dict, Iterable, Mapping, MutableMapping, Optional, Tuple, Union


def _get_env(name: str, *, required: bool = True) -> Optional[str]:
    val = os.getenv(name)
    if required and not val:
        raise RuntimeError(f"Missing required environment variable: {name}")
    return val


def build_x_api_key_header(keystring: str, shared_secret: str) -> str:
    # Etsy expects: keystring:shared_secret
    return f"{keystring}:{shared_secret}"


def build_bearer_header(user_id: str, access_token: str) -> str:
    # Etsy expects: Bearer <numeric_user_id>.<access_token>
    return f"{user_id}.{access_token}"


def _coerce_headers(headers: Mapping[str, str]) -> Dict[str, str]:
    # Normalize header keys to their canonical casing is not required, but helpful.
    return {str(k): str(v) for k, v in headers.items()}


def _parse_retry_after(headers: Mapping[str, str]) -> Optional[float]:
    ra = None
    for k, v in headers.items():
        if k.lower() == "retry-after":
            ra = v
            break
    if not ra:
        return None
    try:
        return float(ra)
    except ValueError:
        return None


def _rate_limit_snapshot(headers: Mapping[str, str]) -> Dict[str, str]:
    # Etsy documents these headers, but some docs renderings truncate names.
    # Treat keys case-insensitively and include anything that looks relevant.
    interesting_prefixes = (
        "x-limit",
        "x-remaining",
        "x-ratelimit",
        "retry-after",
    )
    out: Dict[str, str] = {}
    for k, v in headers.items():
        lk = k.lower().strip()
        if any(lk.startswith(p) for p in interesting_prefixes):
            out[k] = v
    return out


@dataclass
class EtsyResponse:
    status_code: int
    headers: Dict[str, str]
    body_bytes: bytes

    def text(self, encoding: str = "utf-8") -> str:
        try:
            return self.body_bytes.decode(encoding, errors="replace")
        except Exception:
            return repr(self.body_bytes)

    def json(self) -> Any:
        return json.loads(self.text())

    def rate_limit_headers(self) -> Dict[str, str]:
        return _rate_limit_snapshot(self.headers)


class EtsyHttpClient:
    def __init__(
        self,
        *,
        api_base_url: Optional[str] = None,
        keystring: Optional[str] = None,
        shared_secret: Optional[str] = None,
        oauth_user_id: Optional[str] = None,
        oauth_access_token: Optional[str] = None,
        timeout_s: float = 30.0,
    ) -> None:
        self.api_base_url = (api_base_url or os.getenv("ETSY_API_BASE_URL") or "https://api.etsy.com").rstrip("/")
        self.keystring = keystring or _get_env("ETSY_KEYSTRING")
        self.shared_secret = shared_secret or _get_env("ETSY_SHARED_SECRET")
        self.oauth_user_id = oauth_user_id or os.getenv("ETSY_OAUTH_USER_ID")
        self.oauth_access_token = oauth_access_token or os.getenv("ETSY_OAUTH_ACCESS_TOKEN")
        self.timeout_s = timeout_s

    def _build_headers(
        self,
        *,
        use_oauth: bool,
        extra_headers: Optional[Mapping[str, str]] = None,
        content_type: Optional[str] = None,
    ) -> Dict[str, str]:
        headers: Dict[str, str] = {
            "x-api-key": build_x_api_key_header(self.keystring, self.shared_secret),
            "accept": "application/json",
            "user-agent": "etsy-api-skill/1.0 (+https://github.com/)",
        }
        if content_type:
            headers["content-type"] = content_type

        if use_oauth:
            if not self.oauth_user_id or not self.oauth_access_token:
                raise RuntimeError(
                    "OAuth requested but ETSY_OAUTH_USER_ID / ETSY_OAUTH_ACCESS_TOKEN are not set."
                )
            headers["authorization"] = f"Bearer {build_bearer_header(self.oauth_user_id, self.oauth_access_token)}"

        if extra_headers:
            headers.update(_coerce_headers(extra_headers))

        return headers

    def request(
        self,
        method: str,
        path_or_url: str,
        *,
        use_oauth: bool = False,
        query: Optional[Mapping[str, str]] = None,
        json_body: Optional[Any] = None,
        form_body: Optional[Mapping[str, str]] = None,
        raw_body: Optional[bytes] = None,
        extra_headers: Optional[Mapping[str, str]] = None,
        max_retries: int = 3,
        backoff_base_s: float = 1.0,
        backoff_cap_s: float = 30.0,
    ) -> EtsyResponse:
        """Perform an HTTP request.

        - If `path_or_url` starts with http(s):// it is treated as an absolute URL.
        - Otherwise it is treated as a path relative to `api_base_url`.
        """
        method_u = method.upper().strip()
        if path_or_url.startswith("http://") or path_or_url.startswith("https://"):
            url = path_or_url
        else:
            path = path_or_url if path_or_url.startswith("/") else "/" + path_or_url
            url = f"{self.api_base_url}{path}"

        if query:
            parsed = urllib.parse.urlsplit(url)
            q = urllib.parse.parse_qsl(parsed.query, keep_blank_values=True)
            for k, v in query.items():
                q.append((k, v))
            new_query = urllib.parse.urlencode(q)
            url = urllib.parse.urlunsplit((parsed.scheme, parsed.netloc, parsed.path, new_query, parsed.fragment))

        body_bytes: Optional[bytes] = None
        content_type: Optional[str] = None

        if raw_body is not None:
            body_bytes = raw_body
        elif json_body is not None:
            body_bytes = json.dumps(json_body).encode("utf-8")
            content_type = "application/json; charset=utf-8"
        elif form_body is not None:
            body_bytes = urllib.parse.urlencode({k: str(v) for k, v in form_body.items()}).encode("utf-8")
            content_type = "application/x-www-form-urlencoded; charset=utf-8"

        headers = self._build_headers(use_oauth=use_oauth, extra_headers=extra_headers, content_type=content_type)

        # Prefer requests if present (nicer ergonomics, fewer edge cases).
        try:
            import requests  # type: ignore
            return self._request_requests(
                method_u,
                url,
                headers=headers,
                body_bytes=body_bytes,
                timeout_s=self.timeout_s,
                max_retries=max_retries,
                backoff_base_s=backoff_base_s,
                backoff_cap_s=backoff_cap_s,
            )
        except Exception:
            return self._request_urllib(
                method_u,
                url,
                headers=headers,
                body_bytes=body_bytes,
                timeout_s=self.timeout_s,
                max_retries=max_retries,
                backoff_base_s=backoff_base_s,
                backoff_cap_s=backoff_cap_s,
            )

    def _request_requests(
        self,
        method: str,
        url: str,
        *,
        headers: Mapping[str, str],
        body_bytes: Optional[bytes],
        timeout_s: float,
        max_retries: int,
        backoff_base_s: float,
        backoff_cap_s: float,
    ) -> EtsyResponse:
        import requests  # type: ignore

        for attempt in range(max_retries + 1):
            resp = requests.request(
                method=method,
                url=url,
                headers=dict(headers),
                data=body_bytes,
                timeout=timeout_s,
            )
            headers_out = {k: v for k, v in resp.headers.items()}
            if resp.status_code != 429:
                return EtsyResponse(resp.status_code, headers_out, resp.content)

            wait_s = _parse_retry_after(headers_out)
            if wait_s is None:
                wait_s = min(backoff_cap_s, backoff_base_s * (2 ** attempt))
            # small jitter
            wait_s = wait_s + random.random() * 0.25
            time.sleep(wait_s)

        # last response returned in loop; unreachable
        return EtsyResponse(429, {}, b"")

    def _request_urllib(
        self,
        method: str,
        url: str,
        *,
        headers: Mapping[str, str],
        body_bytes: Optional[bytes],
        timeout_s: float,
        max_retries: int,
        backoff_base_s: float,
        backoff_cap_s: float,
    ) -> EtsyResponse:
        for attempt in range(max_retries + 1):
            req = urllib.request.Request(url=url, data=body_bytes, method=method, headers=dict(headers))
            try:
                with urllib.request.urlopen(req, timeout=timeout_s) as resp:
                    body = resp.read()
                    headers_out = dict(resp.headers.items())
                    return EtsyResponse(resp.status, headers_out, body)
            except urllib.error.HTTPError as e:
                body = e.read() if hasattr(e, "read") else b""
                headers_out = dict(e.headers.items()) if e.headers else {}
                if e.code != 429:
                    return EtsyResponse(int(e.code), headers_out, body)

                wait_s = _parse_retry_after(headers_out)
                if wait_s is None:
                    wait_s = min(backoff_cap_s, backoff_base_s * (2 ** attempt))
                wait_s = wait_s + random.random() * 0.25
                time.sleep(wait_s)
            except Exception as e:
                # Network error; backoff and retry
                wait_s = min(backoff_cap_s, backoff_base_s * (2 ** attempt)) + random.random() * 0.25
                time.sleep(wait_s)
                if attempt >= max_retries:
                    raise

        return EtsyResponse(429, {}, b"")

