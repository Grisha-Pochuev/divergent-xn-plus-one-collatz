#!/usr/bin/env python3
"""Verify the large-divisor valuation-split cycle barrier exactly."""
from __future__ import annotations

from fractions import Fraction

X = 104350542602662257699
M = 15099
P = 6911089648497401
H = 2154
D = 2 * M
K = 400_000
BARRIER = 176022359338834903234
SCALE_BITS = 70
SCALE = 1 << SCALE_BITS
SERIES_TERMS = 12


def main_class_rep(t: int) -> int:
    residue = pow(pow(2, t, M), -1, M)
    rep = residue if residue & 1 else residue + M
    if rep == 1:
        rep += 2 * M
    return rep


def atanh_log_upper(z: Fraction) -> Fraction:
    assert 1 <= z <= 2
    y = (z - 1) / (z + 1)
    y2 = y * y
    power = y
    partial = Fraction(0, 1)
    for j in range(SERIES_TERMS):
        partial += power / (2 * j + 1)
        power *= y2
    remainder = power / (2 * SERIES_TERMS + 1) / (1 - y2)
    return 2 * (partial + remainder)


def ceil_scaled(value: Fraction) -> int:
    return (value.numerator * SCALE + value.denominator - 1) // value.denominator


LOG2_UNITS = ceil_scaled(atanh_log_upper(Fraction(2, 1)))


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
    return k * LOG2_UNITS + ceil_scaled(atanh_log_upper(u))


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


def reciprocal_bound(
    length_cap: int,
    reps: list[int],
    s0: Fraction,
    sum_reps: int,
    low_first_units: int,
    low_minimum: int,
) -> tuple[Fraction, Fraction, Fraction, int]:
    high_count = (67 * length_cap - 1) // (K + 1)
    assert high_count > 0

    high_log_units = 0
    for rho in reps:
        q = Fraction(D * high_count, H * rho)
        assert q > 1
        high_log_units += log_upper_units(q)

    high = (
        s0
        + Fraction(high_log_units, D * SCALE)
        + Fraction(H * sum_reps, D * D * high_count)
    )

    low_q = Fraction(low_minimum + 2 * P * (length_cap - 1), low_minimum)
    low_log_units = log_upper_units(low_q)
    low = (
        Fraction(low_first_units, SCALE)
        + Fraction(K * low_log_units, 2 * P * SCALE)
    )
    return high + low, high, low, high_count


def interval_margins(
    length_cap: int,
    reps: list[int],
    s0: Fraction,
    sum_reps: int,
    low_first_units: int,
    low_minimum: int,
) -> tuple[Fraction, Fraction, Fraction, Fraction, Fraction, int]:
    reciprocal, high, low, high_count = reciprocal_bound(
        length_cap, reps, s0, sum_reps, low_first_units, low_minimum
    )
    epsilon = Fraction(X * X - (1 << 133), 1 << 133)
    even_margin = Fraction(2, 3) - (length_cap // 2) * epsilon - reciprocal / X

    q_num = 1 << 67
    odd_log_lower = Fraction(2 * (q_num - X), q_num + X)
    odd_margin = (
        odd_log_lower
        - ((length_cap - 1) // 2) * epsilon
        - reciprocal / X
    )
    return even_margin, odd_margin, reciprocal, high, low, high_count


def verify() -> None:
    assert X == M * P
    assert M == 3 * 7 * 719
    assert pow(2, H, M) == 1
    for prime in (2, 3, 359):
        assert pow(2, H // prime, M) != 1
    assert X + 1 < (1 << 67)
    assert X * X > (1 << 133)

    reps = [main_class_rep(t) for t in range(1, H + 1)]
    assert len(set(r % D for r in reps)) == H
    assert min(reps) == 25
    s0 = sum((Fraction(1, r) for r in reps), Fraction(0, 1))
    sum_reps = sum(reps)

    low_first_units, low_minimum = low_residue_data()
    assert low_minimum == 18989746471

    even, odd, reciprocal, high, low, high_count = interval_margins(
        BARRIER, reps, s0, sum_reps, low_first_units, low_minimum
    )
    assert even > 0
    assert odd > 0

    next_even, next_odd, *_ = interval_margins(
        BARRIER + 1, reps, s0, sum_reps, low_first_units, low_minimum
    )
    assert next_even > 0
    assert next_odd <= 0

    print("large-divisor valuation split verified")
    print(f"K={K}, low minimum={low_minimum}")
    print(f"high-count cap={high_count}")
    print(f"barrier={BARRIER}")
    print(f"high reciprocal bound approximately {float(high):.15f}")
    print(f"low reciprocal bound approximately {float(low):.15e}")
    print(f"total reciprocal bound approximately {float(reciprocal):.15f}")
    print(f"odd margin approximately {float(odd):.15e}")
    print(f"next odd margin approximately {float(next_odd):.15e}")


if __name__ == "__main__":
    verify()
