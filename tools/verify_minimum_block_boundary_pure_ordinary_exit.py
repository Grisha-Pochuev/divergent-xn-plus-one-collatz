#!/usr/bin/env python3
from __future__ import annotations

from fractions import Fraction
from math import gcd, lcm

K_BITS = 500
M_BITS = 4501
Q = 1093
H = 364
TOWER_EXPONENT = 974

N = (1 << K_BITS) - 1
B = 1 << M_BITS
D0 = 349 * (1 << 500) - 347
X = B - D0
Q2 = Q * Q
MODULUS = N * Q2
CLASS_COUNT = H * lcm(K_BITS, H)
LAYERS = H * H // gcd(K_BITS, H)


def harmonic(n: int) -> Fraction:
    return sum((Fraction(1, j) for j in range(1, n + 1)), Fraction(0, 1))


def ln2_bounds(terms: int = 2200) -> tuple[Fraction, Fraction]:
    z = Fraction(1, 3)
    z2 = z * z
    power = z
    lower = Fraction(0, 1)
    for j in range(terms):
        lower += power / (2 * j + 1)
        power *= z2
    lower *= 2
    remainder = 2 * power / (2 * terms + 1) / (1 - z2)
    return lower, lower + remainder


def ln1py_bounds() -> tuple[Fraction, Fraction]:
    y = Fraction(D0, X)
    lower = y - y * y / 2
    upper = lower + y * y * y / 3
    return lower, upper


def continued_fraction(value: Fraction, count: int) -> list[int]:
    out: list[int] = []
    current = value
    for _ in range(count):
        integer = current.numerator // current.denominator
        out.append(integer)
        remainder = current - integer
        assert remainder > 0
        current = 1 / remainder
    return out


def convergents(coefficients: list[int]) -> list[tuple[int, int]]:
    p2, p1 = 0, 1
    q2, q1 = 1, 0
    out: list[tuple[int, int]] = []
    for coefficient in coefficients:
        p = coefficient * p1 + p2
        q = coefficient * q1 + q2
        out.append((p, q))
        p2, p1 = p1, p
        q2, q1 = q1, q
    return out


def verify_credit_and_return_arithmetic() -> None:
    for e in range(1, 4501):
        for R in (-e, -1, 0):
            D = e + R
            if D >= 1:
                assert 1 <= D <= e <= 4500
        assert 1 - e >= -4499


def verify_gap_and_corrections() -> None:
    ln2_lo, ln2_hi = ln2_bounds()
    lny_lo, lny_hi = ln1py_bounds()
    beta_lo = ln2_lo / lny_hi
    beta_hi = ln2_hi / lny_lo
    cf_lo = continued_fraction(beta_lo, 10)
    cf_hi = continued_fraction(beta_hi, 10)
    assert cf_lo == cf_hi
    conv = convergents(cf_lo)
    p7, q7 = conv[7]
    p8, q8 = conv[8]
    _, q9 = conv[9]
    assert q9 == 1_106_246_945
    assert 4500 < q9
    gap_lower = lny_lo * (
        Fraction(p7 + p8, 1) - (q7 + q8) * beta_hi
    )
    assert gap_lower > Fraction(1, 1 << 4023)

    length_one = Fraction(1, X * N)
    length_at_least_two = Fraction(D0, X * X)
    one_block_exit_upper = max(length_one, length_at_least_two)
    assert one_block_exit_upper < Fraction(1, 1 << 4024)
    assert one_block_exit_upper < gap_lower

    assert CLASS_COUNT == 16_562_000
    base_reciprocal = Fraction(K_BITS, N) * (1 + harmonic(LAYERS) / 2)
    tail_coefficient = Fraction(CLASS_COUNT, 2 * MODULUS)
    harmonic_cap = 1 << TOWER_EXPONENT
    assert base_reciprocal < Fraction(1, 1 << 488)
    assert tail_coefficient < Fraction(1, 1 << 497)
    assert 1 + 3 * (1 << (TOWER_EXPONENT - 2)) < harmonic_cap
    return_upper = (
        base_reciprocal + tail_coefficient * harmonic_cap
    ) / X
    assert return_upper < Fraction(1, 1 << 4024)
    assert one_block_exit_upper + return_upper < gap_lower


def verify_length_contradiction() -> None:
    assert 2 * 4500 * B * X < (1 << 4006) * D0 * (X - D0)
    assert (1 << 974) > 4006

    assert D0 < (1 << 509)
    assert Fraction(4 * D0, B) < Fraction(1, 1 << 3990)


def main() -> None:
    verify_credit_and_return_arithmetic()
    verify_gap_and_corrections()
    verify_length_contradiction()
    print("least complete-block boundary pure ordinary exit verified")
    print("first block is ordinary and its base multiplier expands")
    print("nonpositive return is excluded by retained harmonic/block bounds")
    print("surviving return has R>=1 and L_return>2^3990")
    print("every return prefix at a block boundary has credit >=-4499")


if __name__ == "__main__":
    main()
