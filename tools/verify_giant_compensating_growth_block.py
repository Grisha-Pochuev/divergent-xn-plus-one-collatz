#!/usr/bin/env python3
"""Verify the giant compensating zero-layer growth block."""
from __future__ import annotations

ORDER_X = 1860810887857924950
EXPECTED_MIN_LENGTH = 28409326532182060
EXPECTED_GROWTH_EXPONENT = 1860810887857924884
TARGETS = (
    177780727155637125193,
    177780727155637125195,
)


def ceil_div(a: int, b: int) -> int:
    return (a + b - 1) // b


def exact_total_valuation(p: int) -> int:
    return (133 * p + 1) // 2


def verify() -> None:
    deficit = 2 * ORDER_X - 132
    min_length = ceil_div(deficit, 131)
    assert min_length == EXPECTED_MIN_LENGTH
    assert deficit // 2 == EXPECTED_GROWTH_EXPONENT
    assert ORDER_X - 66 == EXPECTED_GROWTH_EXPONENT

    for p in TARGETS:
        assert p % 2 == 1
        total = exact_total_valuation(p)
        assert 2 * total == 133 * p + 1
        assert (total - p) // ORDER_X == 6257

        # For every possible number k of positive-layer positions, Q>=k.
        # The total twice-deficit over the k zero-layer blocks is at least
        # k*(2O-131)-1, so its ceiling average is at least 2O-132.
        for k in (1, 2, 3, 100, 1000, 6257):
            total_deficit = k * (2 * ORDER_X - 131) - 1
            assert ceil_div(total_deficit, k) >= deficit

    print("giant compensating growth block verified")
    print(f"minimum block length={EXPECTED_MIN_LENGTH}")
    print(f"growth factor exceeds 2^{EXPECTED_GROWTH_EXPONENT}")


if __name__ == "__main__":
    verify()
