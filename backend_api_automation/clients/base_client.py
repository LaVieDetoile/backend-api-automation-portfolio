from __future__ import annotations

from collections.abc import Mapping
from typing import Any

import requests
from requests import Response, Session

from backend_api_automation.config.settings import settings
from backend_api_automation.utils.logger import get_logger


class BaseApiClient:
    def __init__(self, base_url: str, session: Session | None = None) -> None:
        self.base_url = base_url.rstrip("/")
        self.session = session or requests.Session()
        self.timeout = settings.request_timeout_seconds
        self.logger = get_logger(self.__class__.__name__)

    def request(
        self,
        method: str,
        path: str,
        *,
        headers: Mapping[str, str] | None = None,
        params: Mapping[str, Any] | None = None,
        json: Mapping[str, Any] | None = None,
    ) -> Response:
        url = f"{self.base_url}{path}"
        response = self.session.request(
            method=method,
            url=url,
            headers=headers,
            params=params,
            json=json,
            timeout=self.timeout,
        )
        self.logger.info("%s %s -> %s", method.upper(), path, response.status_code)
        return response
