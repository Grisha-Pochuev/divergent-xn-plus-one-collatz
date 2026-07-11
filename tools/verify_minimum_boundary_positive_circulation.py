#!/usr/bin/env python3
from __future__ import annotations

from fractions import Fraction

M = 4501
B = 1 << M
D0 = 349 * (1 << 500) - 347
X = B - D0
N = (1 << 500) - 1


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


def main() -> None:
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
    p_star = p7 + p8
    q_star = q7 + q8
    assert q9 == 1_106_246_945

    eta_lower = Fraction(p_star, 1) - q_star * beta_hi
    z_lower = lny_lo * eta_lower
    assert z_lower > Fraction(1, 1 << 4023)

    max_types = 4500
    max_credit = 4500 * max_types
    max_complete_blocks = 4501 * max_types - 1
    assert max_credit == 20_250_000
    assert max_complete_blocks == 20_254_499
    assert max_credit < q9

    correction_upper = (
        Fraction(max_complete_blocks, X * N)
        + Fraction(max_complete_blocks * D0, X * X)
    )
    assert correction_upper < Fraction(1, 1 << 4023)

    # Used in the proof that each block correction is below ell*ln(B/X).
    assert lny_lo > Fraction(D0, 2 * X)

    print("minimum-boundary positive circulation verified")
    print(f"maximum terminal types={max_types}")
    print(f"maximum positive credit={max_credit}")
    print(f"maximum selected complete blocks={max_complete_blocks}")
    print("continued-fraction natural-log gap exceeds 2^-4023")
    print("selected-circulation correction is below 2^-4023")
    print("therefore every selected circulation has 1<=C and L*delta<C")


if __name__ == "__main__":
    main()
