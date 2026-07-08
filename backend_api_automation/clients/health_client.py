from __future__ import annotations

from requests import Response

from backend_api_automation.clients.base_client import BaseApiClient
from backend_api_automation.config.settings import settings


class HealthClient(BaseApiClient):
    def __init__(self) -> None:
        super().__init__(settings.booking_api_base_url)

    def ping(self) -> Response:
        return self.request("GET", "/ping")
