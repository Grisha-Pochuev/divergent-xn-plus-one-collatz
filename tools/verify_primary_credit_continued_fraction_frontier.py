#!/usr/bin/env python3
from __future__ import annotations

from fractions import Fraction
from math import gcd, lcm

K_BITS = 500
M_BITS = 4501
Q = 1093
H = 364
CF_COUNT = 554
PCAP_BITS = 4991

N = (1 << K_BITS) - 1
D0 = 349 * (1 << 500) - 347
B = 1 << M_BITS
X = B - D0
MODULUS = N * Q * Q
CLASS_COUNT = H * lcm(K_BITS, H)
LAYERS = H * H // gcd(K_BITS, H)

Q_FRONTIER = 924679364903952241768234680715310598867316370441120757898246831506500507205080014535351439406991342585993538327845986892977536682537320095988153612270886695873966778097766981798062925612878469213187733241206117142814414961418054803443235355123715316220902421623921086365374327267387194352877014114959


def harmonic(n: int) -> Fraction:
    out = Fraction()
    for j in range(1, n + 1):
        out += Fraction(1, j)
    return out


def ln2_bounds(terms: int = 2200) -> tuple[Fraction, Fraction]:
    z = Fraction(1, 3)
    z2 = z * z
    power = z
    lower = Fraction()
    for j in range(terms):
        lower += power / (2 * j + 1)
        power *= z2
    lower *= 2
    remainder = 2 * power / (2 * terms + 1) / (1 - z2)
    return lower, lower + remainder


def ln_b_over_x_bounds() -> tuple[Fraction, Fraction]:
    y = Fraction(D0, X)
    lower = y - y * y / 2
    upper = lower + y * y * y / 3
    return lower, upper


def common_continued_fraction(
    lower: Fraction, upper: Fraction, count: int
) -> list[int]:
    coefficients: list[int] = []
    lo, hi = lower, upper
    for _ in range(count):
        a_lo = lo.numerator // lo.denominator
        a_hi = hi.numerator // hi.denominator
        assert a_lo == a_hi
        a = a_lo
        coefficients.append(a)
        lo, hi = 1 / (hi - a), 1 / (lo - a)
    return coefficients


def convergents(coefficients: list[int]) -> list[tuple[int, int]]:
    p_minus_2, p_minus_1 = 0, 1
    q_minus_2, q_minus_1 = 1, 0
    out: list[tuple[int, int]] = []
    for a in coefficients:
        p = a * p_minus_1 + p_minus_2
        q = a * q_minus_1 + q_minus_2
        out.append((p, q))
        p_minus_2, p_minus_1 = p_minus_1, p
        q_minus_2, q_minus_1 = q_minus_1, q
    return out


def verify_credit_frontier() -> None:
    ln2_lo, ln2_hi = ln2_bounds()
    lny_lo, lny_hi = ln_b_over_x_bounds()
    beta_lo = ln2_lo / lny_hi
    beta_hi = ln2_hi / lny_lo

    coefficients = common_continued_fraction(beta_lo, beta_hi, CF_COUNT)
    assert coefficients[553] == 36
    conv = convergents(coefficients)

    # Index 553 is odd, hence its intermediate convergents are upper
    # one-sided best approximations. t=26 is the final such approximation
    # before the t=27 denominator Q_FRONTIER.
    p551, q551 = conv[551]
    p552, q552 = conv[552]
    p_prev = p551 + 26 * p552
    q_prev = q551 + 26 * q552
    p_front = p551 + 27 * p552
    q_front = q551 + 27 * q552

    assert q_front == Q_FRONTIER
    assert q_prev < q_front
    assert Fraction(p_prev, q_prev) > beta_hi
    assert Fraction(p_front, q_front) > beta_hi
    assert abs(p_front * q_prev - p_prev * q_front) == 1

    # For every 1<=D<q_front, the one-sided continued-fraction lemma gives
    # p-D*beta >= p_prev-q_prev*beta whenever p-D*beta>0.
    gap_lower = lny_lo * (Fraction(p_prev) - q_prev * beta_hi)
    assert gap_lower > 0

    # If D<q_front, the global correction theorem gives p<2^4991.
    assert 2 * q_front * B * X < (1 << PCAP_BITS) * D0 * (X - D0)

    # Harmonic packing for the remaining return, now using p<2^4991
    # rather than the much looser historical tower cutoff.
    base_reciprocal = Fraction(K_BITS, N) * (
        1 + harmonic(LAYERS) / 2
    )
    tail_coefficient = Fraction(CLASS_COUNT, 2 * MODULUS)
    harmonic_cap = 1 + PCAP_BITS * ln2_hi
    return_correction_upper = (
        base_reciprocal + tail_coefficient * harmonic_cap
    ) / X

    exit_correction_upper = (
        Fraction(4500, X * N) + Fraction(4500 * D0, X * X)
    )
    total_correction_upper = (
        return_correction_upper + exit_correction_upper
    )

    assert gap_lower > total_correction_upper

    print("primary credit continued-fraction frontier verified")
    print(f"D >= {Q_FRONTIER}")
    print("assuming D below the frontier forces p<2^4991")
    print("continued-fraction gap exceeds the full correction upper bound")


if __name__ == "__main__":
    verify_credit_frontier()
