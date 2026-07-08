from __future__ import annotations

from collections.abc import Generator

import pytest

from backend_api_automation.clients.auth_client import AuthClient
from backend_api_automation.clients.booking_client import BookingClient
from backend_api_automation.clients.health_client import HealthClient
from backend_api_automation.clients.users_client import UsersClient


@pytest.fixture(scope="session")
def auth_client() -> AuthClient:
    return AuthClient()


@pytest.fixture(scope="session")
def booking_client() -> BookingClient:
    return BookingClient()


@pytest.fixture(scope="session")
def health_client() -> HealthClient:
    return HealthClient()


@pytest.fixture(scope="session")
def users_client() -> UsersClient:
    return UsersClient()


@pytest.fixture(scope="session")
def auth_token(auth_client: AuthClient) -> str:
    return auth_client.create_token()


@pytest.fixture()
def created_booking_ids(booking_client: BookingClient, auth_token: str) -> Generator[list[int], None, None]:
    booking_ids: list[int] = []
    yield booking_ids
    for booking_id in booking_ids:
        booking_client.delete_booking(booking_id, auth_token)
