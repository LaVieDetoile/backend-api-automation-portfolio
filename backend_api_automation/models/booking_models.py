from __future__ import annotations

from datetime import date

from pydantic import BaseModel, Field


class BookingDates(BaseModel):
    checkin: date
    checkout: date


class Booking(BaseModel):
    firstname: str = Field(min_length=1)
    lastname: str = Field(min_length=1)
    totalprice: int = Field(gt=0)
    depositpaid: bool
    bookingdates: BookingDates
    additionalneeds: str | None = None


class CreatedBooking(BaseModel):
    bookingid: int = Field(gt=0)
    booking: Booking


class BookingId(BaseModel):
    bookingid: int = Field(gt=0)
