import pytest

from backend_api_automation.clients.auth_client import AuthClient
from backend_api_automation.config.settings import settings
from backend_api_automation.models.auth_models import AuthResponse
from backend_api_automation.utils.assertions import assert_status_code


@pytest.mark.smoke
def test_valid_auth_returns_token(auth_client: AuthClient) -> None:
    response = auth_client.create_token_response(settings.booking_api_username, settings.booking_api_password)

    assert_status_code(response, 200)
    token = AuthResponse.model_validate(response.json()).token
    assert token, "Expected valid auth to return a non-empty token"


@pytest.mark.negative
def test_invalid_auth_is_rejected(auth_client: AuthClient) -> None:
    response = auth_client.create_token_response("invalid-user", "invalid-password")

    assert_status_code(response, 200)
    assert response.json() == {"reason": "Bad credentials"}, "Expected invalid credentials to be rejected"
