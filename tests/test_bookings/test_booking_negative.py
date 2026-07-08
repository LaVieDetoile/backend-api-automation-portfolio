import pytest

from backend_api_automation.clients.booking_client import BookingClient
from backend_api_automation.models.booking_models import CreatedBooking
from backend_api_automation.utils.assertions import assert_status_code, assert_status_code_in
from test_data.booking_payloads import (
    INCOMPLETE_BOOKING_PAYLOAD,
    updated_booking_payload,
    valid_booking_payload,
)


@pytest.mark.negative
def test_update_without_valid_auth_is_rejected(
    booking_client: BookingClient,
    created_booking_ids: list[int],
) -> None:
    create_response = booking_client.create_booking(valid_booking_payload())
    assert_status_code(create_response, 200)
    booking_id = CreatedBooking.model_validate(create_response.json()).bookingid
    created_booking_ids.append(booking_id)

    response = booking_client.update_booking(booking_id, updated_booking_payload(), token=None)

    assert_status_code(response, 403)


@pytest.mark.negative
def test_delete_without_valid_auth_is_rejected(
    booking_client: BookingClient,
    created_booking_ids: list[int],
) -> None:
    create_response = booking_client.create_booking(valid_booking_payload())
    assert_status_code(create_response, 200)
    booking_id = CreatedBooking.model_validate(create_response.json()).bookingid
    created_booking_ids.append(booking_id)

    response = booking_client.delete_booking(booking_id, token=None)

    assert_status_code(response, 403)


@pytest.mark.negative
def test_non_existing_booking_lookup_is_handled(booking_client: BookingClient) -> None:
    response = booking_client.get_booking(999_999_999)

    assert_status_code_in(response, {404, 405})


@pytest.mark.negative
def test_incomplete_booking_payload_is_rejected_or_not_created(booking_client: BookingClient) -> None:
    response = booking_client.request(
        "POST",
        "/booking",
        headers=booking_client.auth_headers(),
        json=INCOMPLETE_BOOKING_PAYLOAD,
    )

    assert response.status_code >= 400, (
        "Expected incomplete booking payload to be rejected. "
        f"Got HTTP {response.status_code}: {response.text[:300]}"
    )
