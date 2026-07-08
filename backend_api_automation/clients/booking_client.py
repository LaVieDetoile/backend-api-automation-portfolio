from __future__ import annotations

from collections.abc import Mapping
from typing import Any

from pydantic import BaseModel
from requests import Response

from backend_api_automation.clients.base_client import BaseApiClient
from backend_api_automation.config.settings import settings
from backend_api_automation.models.booking_models import Booking


class BookingClient(BaseApiClient):
    def __init__(self) -> None:
        super().__init__(settings.booking_api_base_url)

    @staticmethod
    def auth_headers(token: str | None = None) -> dict[str, str]:
        headers = {"Accept": "application/json", "Content-Type": "application/json"}
        if token:
            headers["Cookie"] = f"token={token}"
        return headers

    @staticmethod
    def _payload(model_or_payload: BaseModel | Mapping[str, Any]) -> dict[str, Any]:
        if isinstance(model_or_payload, BaseModel):
            return model_or_payload.model_dump(mode="json", exclude_none=True)
        return dict(model_or_payload)

    def create_booking(self, booking: Booking) -> Response:
        return self.request("POST", "/booking", headers=self.auth_headers(), json=self._payload(booking))

    def get_booking(self, booking_id: int) -> Response:
        return self.request("GET", f"/booking/{booking_id}", headers={"Accept": "application/json"})

    def get_booking_ids(self, **filters: str) -> Response:
        return self.request("GET", "/booking", params=filters or None)

    def update_booking(self, booking_id: int, booking: Booking, token: str | None = None) -> Response:
        return self.request(
            "PUT", f"/booking/{booking_id}", headers=self.auth_headers(token), json=self._payload(booking)
        )

    def partial_update_booking(
        self,
        booking_id: int,
        payload: Mapping[str, Any],
        token: str | None = None,
    ) -> Response:
        return self.request(
            "PATCH", f"/booking/{booking_id}", headers=self.auth_headers(token), json=self._payload(payload)
        )

    def delete_booking(self, booking_id: int, token: str | None = None) -> Response:
        return self.request("DELETE", f"/booking/{booking_id}", headers=self.auth_headers(token))
