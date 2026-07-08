import pytest

from backend_api_automation.clients.booking_client import BookingClient
from backend_api_automation.models.booking_models import Booking, BookingId, CreatedBooking
from backend_api_automation.utils.assertions import assert_status_code
from test_data.booking_payloads import valid_booking_payload


@pytest.mark.regression
def test_booking_ids_response_shape(booking_client: BookingClient) -> None:
    response = booking_client.get_booking_ids()

    assert_status_code(response, 200)
    payload = response.json()
    assert isinstance(payload, list), "Expected booking ids response to be a list"
    assert payload, "Expected at least one booking id in public demo API"
    BookingId.model_validate(payload[0])


@pytest.mark.regression
def test_filter_bookings_by_first_name(
    booking_client: BookingClient,
    created_booking_ids: list[int],
) -> None:
    booking_payload = valid_booking_payload()
    create_response = booking_client.create_booking(booking_payload)
    assert_status_code(create_response, 200)
    booking_id = CreatedBooking.model_validate(create_response.json()).bookingid
    created_booking_ids.append(booking_id)

    filter_response = booking_client.get_booking_ids(firstname=booking_payload.firstname)
    assert_status_code(filter_response, 200)
    filtered_ids = [BookingId.model_validate(item).bookingid for item in filter_response.json()]

    assert (
        booking_id in filtered_ids
    ), f"Expected booking {booking_id} in firstname filter results: {filtered_ids}"


@pytest.mark.regression
def test_filter_bookings_by_date_range(
    booking_client: BookingClient,
    created_booking_ids: list[int],
) -> None:
    booking_payload = valid_booking_payload()
    create_response = booking_client.create_booking(booking_payload)
    assert_status_code(create_response, 200)
    booking_id = CreatedBooking.model_validate(create_response.json()).bookingid
    created_booking_ids.append(booking_id)

    date_filter_response = booking_client.get_booking_ids(
        checkin=booking_payload.bookingdates.checkin.isoformat(),
        checkout=booking_payload.bookingdates.checkout.isoformat(),
    )
    assert_status_code(date_filter_response, 200)
    filtered_ids = [BookingId.model_validate(item).bookingid for item in date_filter_response.json()]
    assert isinstance(filtered_ids, list), "Expected date filter response to preserve booking id list shape"

    fetched_booking_response = booking_client.get_booking(booking_id)
    assert_status_code(fetched_booking_response, 200)
    fetched_booking = Booking.model_validate(fetched_booking_response.json())
    assert (
        fetched_booking.bookingdates == booking_payload.bookingdates
    ), "Expected fetched booking dates to match filter"
