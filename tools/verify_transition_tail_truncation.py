#!/usr/bin/env python3
"""Verify the exact large-valuation tail truncation for the fixed candidate."""
from __future__ import annotations

X = 104350542602662257699
BARRIER = 176022359338834903228
THRESHOLD = 200
TAIL_DENOMINATOR = 10**19
H = 2154
M = 15099


def verify() -> None:
    assert X % M == 0
    assert pow(2, H, M) == 1
    for prime in (2, 3, 359):
        assert pow(2, H // prime, M) != 1

    # For every step with exact valuation a>=T,
    # n >= (2^a-1)/X, hence 1/n <= X/(2^a-1).
    # At most BARRIER cycle elements contribute.
    lhs = BARRIER * X * TAIL_DENOMINATOR
    rhs = (1 << THRESHOLD) - 1
    assert lhs < rhs

    # Every high layer q>=1 has a=t+H*q>=H+1>THRESHOLD.
    assert H + 1 > THRESHOLD

    print("transition tail truncation verified")
    print(f"X={X}")
    print(f"barrier={BARRIER}")
    print(f"all a>={THRESHOLD} contribute less than 1/{TAIL_DENOMINATOR}")
    print(f"retained oriented cells={H*(THRESHOLD-1)}")


if __name__ == "__main__":
    verify()
