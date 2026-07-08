from __future__ import annotations

from pydantic import BaseModel, EmailStr, Field, HttpUrl


class Geo(BaseModel):
    lat: str
    lng: str


class Address(BaseModel):
    street: str
    suite: str
    city: str
    zipcode: str
    geo: Geo


class Company(BaseModel):
    name: str
    catchPhrase: str
    bs: str


class User(BaseModel):
    id: int = Field(gt=0)
    name: str = Field(min_length=1)
    username: str = Field(min_length=1)
    email: EmailStr
    address: Address
    phone: str
    website: str | HttpUrl
    company: Company
