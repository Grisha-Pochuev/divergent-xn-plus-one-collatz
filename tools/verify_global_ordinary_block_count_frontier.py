#!/usr/bin/env python3
from __future__ import annotations

from fractions import Fraction

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

    cf_lo = continued_fraction(beta_lo, 10)
    cf_hi = continued_fraction(beta_hi, 10)
    assert cf_lo == cf_hi
    assert cf_lo[1:] == [1, 1, 145_062, 23, 1, 4, 1, 12, 2]

    conv = convergents(cf_lo)
    p7, q7 = conv[7]
    p8, q8 = conv[8]
    _, q9 = conv[9]
    p_star = p7 + p8
    q_star = q7 + q8
    assert q_star == 573_867_416
    assert q9 == 1_106_246_945

    eta_lower = Fraction(p_star, 1) - q_star * beta_hi
    assert eta_lower > 0
    z_lower = lny_lo * eta_lower
    assert z_lower > 0
    z_bits = z_lower.denominator.bit_length()
    assert z_bits <= 22_205
    gap_loss = z_bits + 1
    assert gap_loss <= 22_206

    max_ordinary_blocks = (q9 - 1) // (M - 1)
    assert max_ordinary_blocks == 245_832
    max_total_deficit = (M - 1) * max_ordinary_blocks - 1
    assert max_total_deficit == 1_106_243_999
    assert max_total_deficit < q9

    # General signed block closure:
    # - selecting an ordinary block of length L gives
    #     Delta*u < J*B^(p-L+J+1);
    # - selecting an exceptional block of length k gives
    #     Delta*v < J*B^(p-k+J).
    # At the proposed forbidden thresholds, the gap exponent wins uniformly.
    for j in (1, 2, 10, 1000, max_ordinary_blocks):
        d_max = (M - 1) * j - 1

        ordinary_margin = (
            M * (2 * j + 7)
            - d_max
            - gap_loss
            - M * (j + 1)
        )
        assert ordinary_margin == j + 4_801
        assert ordinary_margin > 0

        exceptional_margin = (
            M * (2 * j + 6)
            - d_max
            - gap_loss
            - M * j
        )
        assert exceptional_margin == j + 4_801
        assert exceptional_margin > 0

    # Therefore ordinary lengths are <=2J+6 and exceptional lengths <=2J+5.
    # The number R of exceptional blocks obeys R<=sum b_i<=4500J-1.
    j = max_ordinary_blocks
    max_exceptional_blocks = (M - 1) * j - 1
    p_upper = (
        j * (2 * j + 6)
        + max_exceptional_blocks * (2 * j + 5)
    )
    assert p_upper == 544_026_748_963_771
    assert p_upper < 10**15

    barrier = (2 * X) // (3 * D0)
    assert barrier > 10**1201
    assert p_upper < barrier

    print("global ordinary-block count frontier verified")
    print(f"continued-fraction denominator frontier={q9}")
    print(f"excluded ordinary-block counts=1..{max_ordinary_blocks}")
    print(f"maximum exceptional-block count in excluded range={max_exceptional_blocks}")
    print(f"universal cycle-length upper={p_upper}")
    print("every hypothetical cycle needs at least 245833 ordinary blocks")


if __name__ == "__main__":
    main()
