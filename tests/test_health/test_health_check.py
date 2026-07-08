import pytest

from backend_api_automation.clients.booking_client import BookingClient
from backend_api_automation.clients.health_client import HealthClient
from backend_api_automation.models.booking_models import BookingId
from backend_api_automation.utils.assertions import assert_status_code


@pytest.mark.smoke
def test_booking_api_ping_is_healthy(health_client: HealthClient) -> None:
    response = health_client.ping()

    assert_status_code(response, 201)
    assert response.text == "Created", "Expected Restful Booker ping endpoint to return Created"


@pytest.mark.regression
def test_booking_ids_endpoint_returns_stable_options_shape(booking_client: BookingClient) -> None:
    response = booking_client.get_booking_ids()

    assert_status_code(response, 200)
    booking_ids = [BookingId.model_validate(item) for item in response.json()]
    assert booking_ids, "Expected booking options/list endpoint to return at least one booking id"
