#!/usr/bin/env python3
from __future__ import annotations

from fractions import Fraction
from math import lcm

M = 4501
B = 1 << M
D0 = 349 * (1 << 500) - 347
X = B - D0


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
    assert beta_lo < beta_hi

    cf_lo = continued_fraction(beta_lo, 10)
    cf_hi = continued_fraction(beta_hi, 10)
    assert cf_lo == cf_hi
    assert cf_lo[1:] == [1, 1, 145_062, 23, 1, 4, 1, 12, 2]

    conv = convergents(cf_lo)
    p7, q7 = conv[7]
    p8, q8 = conv[8]
    p9, q9 = conv[9]

    # Because a_9=2, the last upper semiconvergent before the next upper
    # convergent p9/q9 is (p7+p8)/(q7+q8).
    p_star = p7 + p8
    q_star = q7 + q8
    assert q7 == 41_487_887
    assert q8 == 532_379_529
    assert q_star == 573_867_416
    assert q9 == 1_106_246_945
    assert Fraction(p_star, q_star) > beta_hi
    assert Fraction(p9, q9) > beta_hi

    eta_lower = Fraction(p_star, 1) - q_star * beta_hi
    assert eta_lower > 0
    z_lower = lny_lo * eta_lower
    assert z_lower > 0
    z_bits = z_lower.denominator.bit_length()
    assert z_bits <= 22_205

    max_total_deficit = q9 - 1
    max_blocks = max_total_deficit // (M - 1)
    assert max_total_deficit == 1_106_246_944
    assert max_blocks == 245_832
    assert (M - 1) * max_blocks <= max_total_deficit
    assert (M - 1) * (max_blocks + 1) > max_total_deficit

    beta_floor = cf_lo[0]
    first_length = beta_floor + 1
    assert Fraction(first_length - 1, 1) < beta_lo
    assert Fraction(first_length, 1) > beta_hi

    # For any J<=max_blocks, D<=4500J<=max_total_deficit.  A positive
    # cycle gap has p/D>beta, so the longest block has length at least
    # ceil(p/J)>=ceil(beta)=first_length.  The following exponent comparison
    # makes the positive gap larger than the entire J-term additive numerator.
    log2_block_count_upper = 18  # max_blocks < 2^18
    assert max_blocks < 1 << log2_block_count_upper
    assert (
        M * first_length
        - max_total_deficit
        - (z_bits + 1)
        - log2_block_count_upper
        - M
        > 0
    )

    print("ordinary block-count frontier verified")
    print(f"continued-fraction prefix={cf_lo[1:]}")
    print(f"best upper semiconvergent denominator={q_star}")
    print(f"next upper convergent denominator={q9}")
    print(f"uniform logarithmic denominator bits<={z_bits}")
    print(f"excluded ordinary block counts=1..{max_blocks}")


if __name__ == "__main__":
    main()
