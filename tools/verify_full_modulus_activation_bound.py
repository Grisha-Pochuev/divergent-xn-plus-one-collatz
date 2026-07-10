#!/usr/bin/env python3
"""Verify elimination of the second sparse-window exceptional length."""
from __future__ import annotations

from fractions import Fraction
from math import gcd, isqrt

X = 104350542602662257699
M = 15099
H = 2154
D = 2 * M
ORDER_X = 1860810887857924950
TARGET = 177780727155637125185
EXPECTED_ACTIVE_CLASSES = 153768776777
EXPECTED_THRESHOLD = 2155761151909
SCALE_BITS = 80
SCALE = 1 << SCALE_BITS
UPPER_TERMS = 16


def is_prime_64(n: int) -> bool:
    if n < 2:
        return False
    small = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37)
    for p in small:
        if n % p == 0:
            return n == p
    d = n - 1
    s = 0
    while d % 2 == 0:
        d //= 2
        s += 1
    for a in (2, 325, 9375, 28178, 450775, 9780504, 1795265022):
        if a % n == 0:
            continue
        x = pow(a, d, n)
        if x in (1, n - 1):
            continue
        for _ in range(s - 1):
            x = x * x % n
            if x == n - 1:
                break
        else:
            return False
    return True


def log_bounds(z: Fraction, terms: int) -> tuple[Fraction, Fraction]:
    assert z >= 1
    y = (z - 1) / (z + 1)
    y2 = y * y
    power = y
    partial = Fraction(0, 1)
    for j in range(terms):
        partial += power / (2 * j + 1)
        power *= y2
    lower = 2 * partial
    upper = lower + 2 * power / (2 * terms + 1) / (1 - y2)
    return lower, upper


def ceil_scaled(value: Fraction) -> int:
    return (value.numerator * SCALE + value.denominator - 1) // value.denominator


_, LOG2_UPPER = log_bounds(Fraction(2, 1), UPPER_TERMS)
LOG2_UPPER_UNITS = ceil_scaled(LOG2_UPPER)


def log_upper_units(q: Fraction) -> int:
    """Return U such that log(q)<=U/2^SCALE_BITS."""
    assert q >= 1
    if q == 1:
        return 0
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
    _, upper = log_bounds(u, UPPER_TERMS)
    return k * LOG2_UPPER_UNITS + ceil_scaled(upper)


def class_rep(t: int) -> int:
    residue = pow(pow(2, t, M), -1, M)
    rep = residue if residue & 1 else residue + M
    if rep == 1:
        rep += D
    return rep


def count_allowed_at_most(limit: int, reps: list[int]) -> int:
    return sum(
        0 if limit < rho else (limit - rho) // D + 1
        for rho in reps
    )


def verify_order() -> None:
    prime_factors = (2, 3, 5, 359, 2677, 15137, 852763)
    assert ORDER_X == 2 * 3 * 5**2 * 359 * 2677 * 15137 * 852763
    assert all(is_prime_64(q) for q in prime_factors)
    assert gcd(2, X) == 1
    assert pow(2, ORDER_X, X) == 1
    for q in prime_factors:
        assert pow(2, ORDER_X // q, X) != 1


def verify() -> None:
    verify_order()
    assert X % M == 0
    assert pow(2, H, M) == 1

    r = (TARGET - 1) // 2
    exact_total_valuation = 133 * r + 67

    # Check that the target lies below the first odd crossing and that the
    # cycle product cannot reach the following power. Hence A is exact.
    log2_lower, _ = log_bounds(Fraction(2, 1), 40)
    energy = Fraction(X * X, 1 << 133)
    _, eta_upper = log_bounds(energy, 4)
    assert TARGET * eta_upper < log2_lower
    assert X > (1 << 66)
    assert Fraction(TARGET, 25 * X) < log2_lower

    active = (isqrt(1 + 8 * exact_total_valuation) - 1) // 2
    assert active == EXPECTED_ACTIVE_CLASSES
    assert active * (active + 1) // 2 <= exact_total_valuation
    assert (active + 1) * (active + 2) // 2 > exact_total_valuation

    reps = sorted(class_rep(t) for t in range(1, H + 1))
    assert len(set(rho % D for rho in reps)) == H
    assert min(reps) == 25

    low = 1
    high = D * ((active + H - 1) // H) + max(reps)
    while low < high:
        middle = (low + high) // 2
        if count_allowed_at_most(middle, reps) >= active:
            high = middle
        else:
            low = middle + 1
    threshold = low
    assert threshold == EXPECTED_THRESHOLD

    counts = [
        0 if threshold < rho else (threshold - rho) // D + 1
        for rho in reps
    ]
    assert sum(counts) == active

    first_bound = Fraction(0, 1)
    for rho, count in zip(reps, counts):
        if count == 0:
            continue
        q = Fraction(rho + D * (count - 1), rho)
        first_bound += Fraction(1, rho)
        first_bound += Fraction(log_upper_units(q), D * SCALE)

    # Repetitions in one full class are spaced by 2X. This deliberately
    # allows every active class as many as TARGET elements.
    tail_q = Fraction(25 + 2 * X * (TARGET - 1), 25)
    tail_bound = Fraction(
        active * log_upper_units(tail_q),
        2 * X * SCALE,
    )
    reciprocal_bound = first_bound + tail_bound

    gap_lower = (log2_lower - TARGET * eta_upper) / 2
    margin = gap_lower - reciprocal_bound / X
    assert margin > 0

    print("full-modulus activation bound verified")
    print(f"ord_X(2)={ORDER_X}")
    print(f"target={TARGET}")
    print(f"exact total valuation={exact_total_valuation}")
    print(f"active full classes<={active}")
    print(f"allowed-union threshold={threshold}")
    print(f"first-representative bound approximately {float(first_bound):.15f}")
    print(f"full-class tail bound approximately {float(tail_bound):.15e}")
    print(f"total reciprocal bound approximately {float(reciprocal_bound):.15f}")
    print(f"required reciprocal threshold approximately {float(gap_lower*X):.15f}")
    print(f"strict margin approximately {float(margin):.15e}")


if __name__ == "__main__":
    verify()
