from __future__ import annotations

from requests import Response


def assert_status_code(response: Response, expected_status_code: int) -> None:
    assert response.status_code == expected_status_code, (
        f"Expected HTTP {expected_status_code}, got {response.status_code}. "
        f"Response body: {response.text[:500]}"
    )


def assert_status_code_in(response: Response, expected_status_codes: set[int]) -> None:
    assert response.status_code in expected_status_codes, (
        f"Expected one of {sorted(expected_status_codes)}, got {response.status_code}. "
        f"Response body: {response.text[:500]}"
    )


def assert_json_has_keys(payload: dict, expected_keys: set[str]) -> None:
    missing_keys = expected_keys.difference(payload.keys())
    assert not missing_keys, f"Missing expected keys: {sorted(missing_keys)}. Payload: {payload}"


def assert_not_empty(value: object, message: str) -> None:
    assert value, message
