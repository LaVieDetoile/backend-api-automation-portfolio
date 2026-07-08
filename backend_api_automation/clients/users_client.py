from __future__ import annotations

from requests import Response

from backend_api_automation.clients.base_client import BaseApiClient
from backend_api_automation.config.settings import settings


class UsersClient(BaseApiClient):
    def __init__(self) -> None:
        super().__init__(settings.users_api_base_url)

    def list_users(self) -> Response:
        return self.request("GET", "/users")

    def get_user(self, user_id: int) -> Response:
        return self.request("GET", f"/users/{user_id}")

    def get_user_posts(self, user_id: int) -> Response:
        return self.request("GET", f"/users/{user_id}/posts")
