#!/usr/bin/env python3
"""Verify elimination of the first sparse-window exceptional length."""
from __future__ import annotations

from fractions import Fraction

X = 104350542602662257699
M = 15099
P = 6911089648497401
H = 2154
D = 2 * M
K = 5_000_000
TARGET = 177780727155637125183
SCALE_BITS = 70
SCALE = 1 << SCALE_BITS
UPPER_SERIES_TERMS = 12


def class_rep(t: int) -> int:
    residue = pow(pow(2, t, M), -1, M)
    rep = residue if residue & 1 else residue + M
    if rep == 1:
        rep += D
    return rep


def log_upper_series(z: Fraction) -> Fraction:
    assert 1 <= z <= 2
    y = (z - 1) / (z + 1)
    y2 = y * y
    power = y
    partial = Fraction(0, 1)
    for j in range(UPPER_SERIES_TERMS):
        partial += power / (2 * j + 1)
        power *= y2
    return 2 * (
        partial + power / (2 * UPPER_SERIES_TERMS + 1) / (1 - y2)
    )


def log_lower_series(z: Fraction, terms: int) -> Fraction:
    assert z > 1
    y = (z - 1) / (z + 1)
    y2 = y * y
    power = y
    partial = Fraction(0, 1)
    for j in range(terms):
        partial += power / (2 * j + 1)
        power *= y2
    return 2 * partial


def ceil_scaled(value: Fraction) -> int:
    return (value.numerator * SCALE + value.denominator - 1) // value.denominator


LOG2_UPPER_UNITS = ceil_scaled(log_upper_series(Fraction(2, 1)))


def log_upper_units(q: Fraction) -> int:
    assert q > 1
    numerator = q.numerator
    denominator = q.denominator
    k = numerator.bit_length() - denominator.bit_length()
    while numerator < (denominator << k):
        k -= 1
    while numerator >= (denominator << (k + 1)):
        k += 1
    assert k >= 0
    u = q / (1 << k)
    assert 1 <= u < 2
    return k * LOG2_UPPER_UNITS + ceil_scaled(log_upper_series(u))


def low_residue_data() -> tuple[int, int]:
    inverse_two = pow(2, -1, P)
    residue = 1
    first_units = 0
    minimum = 2 * P + 1
    for _a in range(1, K + 1):
        residue = (residue * inverse_two) % P
        rep = residue if residue & 1 else residue + P
        if rep == 1:
            rep += 2 * P
        first_units += (SCALE + rep - 1) // rep
        if rep < minimum:
            minimum = rep
    return first_units, minimum


def reciprocal_bound(length: int) -> tuple[Fraction, Fraction, Fraction, int, int]:
    reps = [class_rep(t) for t in range(1, H + 1)]
    s0 = sum((Fraction(1, r) for r in reps), Fraction(0, 1))

    high_count = (67 * length - 1) // (K + 1)
    high_log_units = 0
    midpoint_base_sum = 0
    for rho in reps:
        midpoint_base = rho + M
        q = Fraction(D * high_count, H * midpoint_base)
        assert q > 1
        high_log_units += log_upper_units(q)
        midpoint_base_sum += midpoint_base

    high = (
        s0
        + Fraction(high_log_units, D * SCALE)
        + Fraction(H * midpoint_base_sum, D * D * high_count)
    )

    low_first_units, low_minimum = low_residue_data()
    low_q = Fraction(low_minimum + 2 * P * (length - 1), low_minimum)
    low = (
        Fraction(low_first_units, SCALE)
        + Fraction(K * log_upper_units(low_q), 2 * P * SCALE)
    )
    return high + low, high, low, low_minimum, high_count


def verify() -> None:
    assert X == M * P
    assert X * X > (1 << 133)
    assert X < (1 << 67)

    reciprocal, high, low, low_minimum, high_count = reciprocal_bound(TARGET)
    assert low_minimum == 4493203551

    energy = Fraction(X * X, 1 << 133)
    gap_lower = (
        log_lower_series(Fraction(2, 1), 30)
        - TARGET * log_upper_series(energy)
    ) / 2
    margin = gap_lower - reciprocal / X
    assert margin > 0

    print("first sparse-window exception eliminated")
    print(f"target={TARGET}")
    print(f"K={K}, low minimum={low_minimum}")
    print(f"high-count cap={high_count}")
    print(f"high reciprocal bound approximately {float(high):.15f}")
    print(f"low reciprocal bound approximately {float(low):.15e}")
    print(f"total reciprocal bound approximately {float(reciprocal):.15f}")
    print(f"strict margin approximately {float(margin):.15e}")


if __name__ == "__main__":
    verify()
