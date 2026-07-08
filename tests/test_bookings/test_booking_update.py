import pytest

from backend_api_automation.clients.booking_client import BookingClient
from backend_api_automation.models.booking_models import Booking, CreatedBooking
from backend_api_automation.utils.assertions import assert_status_code
from backend_api_automation.utils.data_builder import build_partial_booking_update
from test_data.booking_payloads import updated_booking_payload, valid_booking_payload


@pytest.mark.regression
def test_update_booking_and_verify_updated_values(
    booking_client: BookingClient,
    auth_token: str,
    created_booking_ids: list[int],
) -> None:
    create_response = booking_client.create_booking(valid_booking_payload())
    assert_status_code(create_response, 200)
    booking_id = CreatedBooking.model_validate(create_response.json()).bookingid
    created_booking_ids.append(booking_id)

    updated_payload = updated_booking_payload()
    update_response = booking_client.update_booking(booking_id, updated_payload, auth_token)
    assert_status_code(update_response, 200)

    updated_booking = Booking.model_validate(update_response.json())
    assert updated_booking == updated_payload, "PUT response should contain the fully updated booking"


@pytest.mark.regression
def test_partial_update_booking_preserves_unchanged_fields(
    booking_client: BookingClient,
    auth_token: str,
    created_booking_ids: list[int],
) -> None:
    original_payload = valid_booking_payload()
    create_response = booking_client.create_booking(original_payload)
    assert_status_code(create_response, 200)
    booking_id = CreatedBooking.model_validate(create_response.json()).bookingid
    created_booking_ids.append(booking_id)

    patch_payload = build_partial_booking_update()
    patch_response = booking_client.partial_update_booking(booking_id, patch_payload, auth_token)
    assert_status_code(patch_response, 200)
    patched_booking = Booking.model_validate(patch_response.json())

    assert patched_booking.firstname == patch_payload["firstname"], "Expected firstname to be patched"
    assert (
        patched_booking.additionalneeds == patch_payload["additionalneeds"]
    ), "Expected additional needs to be patched"
    assert (
        patched_booking.lastname == original_payload.lastname
    ), "Expected unchanged lastname to be preserved"
    assert (
        patched_booking.totalprice == original_payload.totalprice
    ), "Expected unchanged total price to be preserved"
    assert (
        patched_booking.bookingdates == original_payload.bookingdates
    ), "Expected unchanged booking dates to be preserved"
