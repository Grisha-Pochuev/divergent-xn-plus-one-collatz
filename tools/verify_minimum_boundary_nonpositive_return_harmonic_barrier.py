#!/usr/bin/env python3
from __future__ import annotations

from fractions import Fraction
from math import gcd, lcm

K_BITS = 500
M_BITS = 4501
Q = 1093
H = 364
RETURN_TOWER_EXPONENT = 974

N = (1 << K_BITS) - 1
Q2 = Q * Q
MODULUS = N * Q2
CLASS_COUNT = H * lcm(K_BITS, H)
D0 = 349 * (1 << 500) - 347
B = 1 << M_BITS
X = B - D0
LAYERS = H * H // gcd(K_BITS, H)


def harmonic(n: int) -> Fraction:
    out = Fraction(0, 1)
    for j in range(1, n + 1):
        out += Fraction(1, j)
    return out


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
    p_minus_2, p_minus_1 = 0, 1
    q_minus_2, q_minus_1 = 1, 0
    out: list[tuple[int, int]] = []
    for coefficient in coefficients:
        p = coefficient * p_minus_1 + p_minus_2
        q = coefficient * q_minus_1 + q_minus_2
        out.append((p, q))
        p_minus_2, p_minus_1 = p_minus_1, p
        q_minus_2, q_minus_1 = q_minus_1, q
    return out


def verify() -> None:
    # One-sided continued-fraction gap for every integer credit 1<=D<=4500.
    ln2_lo, ln2_hi = ln2_bounds()
    assert ln2_hi < Fraction(3, 4)
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
    p_star = p7 + p8
    q_star = q7 + q8
    assert q9 == 1_106_246_945
    assert 4500 < q9
    eta_lower = Fraction(p_star, 1) - q_star * beta_hi
    gap_lower = lny_lo * eta_lower
    assert gap_lower > Fraction(1, 1 << 4023)

    # Permanent-class harmonic packing constants.
    assert CLASS_COUNT == 16_562_000
    base_reciprocal = Fraction(K_BITS, N) * (
        1 + harmonic(LAYERS) / 2
    )
    tail_coefficient = Fraction(CLASS_COUNT, 2 * MODULUS)
    assert base_reciprocal < Fraction(1, 1 << 488)
    assert tail_coefficient < Fraction(1, 1 << 497)

    # If L<=2^(2^974), then ceil(L/CLASS_COUNT)<=L and
    # H_ceil(L/CLASS_COUNT) <= 1+ln L < 2^974.
    harmonic_cap = 1 << RETURN_TOWER_EXPONENT
    assert 1 + 3 * (1 << (RETURN_TOWER_EXPONENT - 2)) < harmonic_cap

    return_reciprocal_upper = (
        base_reciprocal + tail_coefficient * harmonic_cap
    )
    return_correction_upper = return_reciprocal_upper / X

    # The expanding exit segment has at most 4500 complete blocks.
    exit_correction_upper = (
        Fraction(4500, X * N) + Fraction(4500 * D0, X * X)
    )

    total_correction_upper = (
        return_correction_upper + exit_correction_upper
    )
    assert return_correction_upper < Fraction(1, 1 << 4024)
    assert exit_correction_upper < Fraction(1, 1 << 4024)
    assert total_correction_upper < Fraction(1, 1 << 4023)
    assert total_correction_upper < gap_lower

    print("nonpositive-return harmonic barrier verified")
    print("return credit R<=0 forces L>2^(2^974)")
    print(f"permanent classes={CLASS_COUNT}")
    print(f"continued-fraction denominator frontier={q9}")
    print(
        "scaled correction upper="
        f"{float(total_correction_upper * (1 << 4023)):.15f}"
    )
    print(f"scaled gap lower={float(gap_lower * (1 << 4023)):.15f}")


if __name__ == "__main__":
    verify()
