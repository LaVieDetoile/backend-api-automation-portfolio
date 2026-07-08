from __future__ import annotations

from backend_api_automation.models.booking_models import Booking
from backend_api_automation.utils.data_builder import build_booking


def valid_booking_payload() -> Booking:
    return build_booking(additional_needs="Breakfast")


def updated_booking_payload() -> Booking:
    return build_booking(
        first_name="Updated",
        last_name="Guest",
        total_price=275,
        deposit_paid=False,
        additional_needs="Airport pickup",
    )


INCOMPLETE_BOOKING_PAYLOAD = {
    "firstname": "MissingFields",
    "lastname": "Tester",
}
