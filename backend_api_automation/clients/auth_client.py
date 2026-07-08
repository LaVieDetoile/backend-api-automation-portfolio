from __future__ import annotations

from requests import Response

from backend_api_automation.clients.base_client import BaseApiClient
from backend_api_automation.config.settings import settings
from backend_api_automation.models.auth_models import AuthRequest, AuthResponse
from backend_api_automation.utils.assertions import assert_status_code


class AuthClient(BaseApiClient):
    def __init__(self) -> None:
        super().__init__(settings.booking_api_base_url)

    def create_token_response(self, username: str, password: str) -> Response:
        payload = AuthRequest(username=username, password=password).model_dump()
        return self.request("POST", "/auth", json=payload)

    def create_token(self) -> str:
        response = self.create_token_response(settings.booking_api_username, settings.booking_api_password)
        assert_status_code(response, 200)
        return AuthResponse.model_validate(response.json()).token
