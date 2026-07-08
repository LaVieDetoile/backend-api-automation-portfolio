from __future__ import annotations

from datetime import date, timedelta
from random import randint

from backend_api_automation.models.booking_models import Booking, BookingDates


def build_booking(
    first_name: str | None = None,
    last_name: str | None = None,
    total_price: int | None = None,
    deposit_paid: bool = True,
    additional_needs: str = "Breakfast",
) -> Booking:
    unique_number = randint(1000, 9999)
    checkin = date.today() + timedelta(days=7)
    checkout = checkin + timedelta(days=3)
    return Booking(
        firstname=first_name or f"Portfolio{unique_number}",
        lastname=last_name or "Tester",
        totalprice=total_price or randint(100, 500),
        depositpaid=deposit_paid,
        bookingdates=BookingDates(checkin=checkin, checkout=checkout),
        additionalneeds=additional_needs,
    )


def build_partial_booking_update() -> dict[str, object]:
    return {
        "firstname": "UpdatedPortfolio",
        "additionalneeds": "Late checkout",
    }
