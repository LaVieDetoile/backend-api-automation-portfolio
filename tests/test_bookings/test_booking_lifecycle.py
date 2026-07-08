import pytest

from backend_api_automation.clients.booking_client import BookingClient
from backend_api_automation.models.booking_models import Booking, CreatedBooking
from backend_api_automation.utils.assertions import assert_status_code, assert_status_code_in
from test_data.booking_payloads import valid_booking_payload


@pytest.mark.smoke
@pytest.mark.regression
def test_create_and_fetch_booking(
    booking_client: BookingClient,
    created_booking_ids: list[int],
) -> None:
    booking_payload = valid_booking_payload()

    create_response = booking_client.create_booking(booking_payload)
    assert_status_code(create_response, 200)
    created_booking = CreatedBooking.model_validate(create_response.json())
    created_booking_ids.append(created_booking.bookingid)

    fetch_response = booking_client.get_booking(created_booking.bookingid)
    assert_status_code(fetch_response, 200)
    fetched_booking = Booking.model_validate(fetch_response.json())

    assert fetched_booking == booking_payload, "Fetched booking should match the booking that was created"


@pytest.mark.regression
def test_delete_booking_and_verify_it_can_no_longer_be_fetched(
    booking_client: BookingClient,
    auth_token: str,
) -> None:
    create_response = booking_client.create_booking(valid_booking_payload())
    assert_status_code(create_response, 200)
    booking_id = CreatedBooking.model_validate(create_response.json()).bookingid

    delete_response = booking_client.delete_booking(booking_id, auth_token)
    assert_status_code(delete_response, 201)

    fetch_response = booking_client.get_booking(booking_id)
    assert_status_code_in(fetch_response, {404, 405})
