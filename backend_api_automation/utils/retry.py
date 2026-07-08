from __future__ import annotations

from collections.abc import Callable
from time import monotonic, sleep
from typing import TypeVar

T = TypeVar("T")


def retry_until(
    action: Callable[[], T],
    condition: Callable[[T], bool],
    timeout_seconds: float = 5,
    interval_seconds: float = 0.25,
) -> T:
    """Retry a small API assertion without arbitrary sleeps."""

    deadline = monotonic() + timeout_seconds
    result = action()
    while monotonic() < deadline:
        if condition(result):
            return result
        sleep(interval_seconds)
        result = action()
    return result
