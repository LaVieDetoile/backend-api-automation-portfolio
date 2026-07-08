from __future__ import annotations

import os
from dataclasses import dataclass

from dotenv import load_dotenv

load_dotenv()


@dataclass(frozen=True)
class Settings:
    booking_api_base_url: str = os.getenv("BOOKING_API_BASE_URL", "https://restful-booker.herokuapp.com")
    users_api_base_url: str = os.getenv("USERS_API_BASE_URL", "https://jsonplaceholder.typicode.com")
    booking_api_username: str = os.getenv("BOOKING_API_USERNAME", "admin")
    booking_api_password: str = os.getenv("BOOKING_API_PASSWORD", "password123")
    request_timeout_seconds: float = float(os.getenv("REQUEST_TIMEOUT_SECONDS", "15"))


settings = Settings()
