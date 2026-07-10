#!/usr/bin/env python3
"""Regression checks for the exact global transition balance identities."""
from __future__ import annotations

from fractions import Fraction


def v2(value: int) -> int:
    assert value > 0
    return (value & -value).bit_length() - 1


def verify_cycle(x: int, cycle: tuple[int, ...]) -> None:
    p = len(cycle)
    valuations: list[int] = []
    for i, n in enumerate(cycle):
        raw = x * n + 1
        a = v2(raw)
        nxt = raw >> a
        assert nxt == cycle[(i + 1) % p]
        valuations.append(a)

    height_left = 0
    for i, n in enumerate(cycle):
        incoming = valuations[(i - 1) % p]
        height_left += ((1 << incoming) - x) * n
    assert height_left == p

    reciprocal_left = Fraction(0, 1)
    reciprocal_right = Fraction(0, 1)
    for i, n in enumerate(cycle):
        nxt = cycle[(i + 1) % p]
        reciprocal_left += Fraction((1 << valuations[i]) - x, n)
        reciprocal_right += Fraction(1, n * nxt)
    assert reciprocal_left == reciprocal_right
    assert reciprocal_right > 0


def verify() -> None:
    verify_cycle(5, (1, 3))
    verify_cycle(5, (13, 33, 83))
    verify_cycle(5, (17, 43, 27))
    print("global transition balance identities verified")
    print("cycles checked=3")


if __name__ == "__main__":
    verify()
