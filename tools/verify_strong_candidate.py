#!/usr/bin/env python3
"""Verify the finite arithmetic certificate for Q=759250131."""
from __future__ import annotations

from fractions import Fraction
import json
import math

from xn1 import odd_step


Q = 759_250_131
ORDER = 6_762_420
ORDER_PRIME_FACTORS = (2, 3, 5, 7, 1789)
MAX_EXCLUDED_CYCLE_LENGTH = 41_500_000
POWER_EXPONENT = 59

# (Q+1/3)^2 = 2^59 * (1 + Y_NUM/Y_DEN)
Y_NUM = 86_636_343_844
Y_DEN = 5_188_146_770_730_811_392

# A rational exponent just below log(2^30/(Q+1/3)).
EXPONENT_BOUND = Fraction(6_931, 20_000)


def verify_order() -> None:
    if pow(2, ORDER, Q) != 1:
        raise AssertionError("claimed exponent is not an order multiple")
    for prime in ORDER_PRIME_FACTORS:
        if ORDER % prime != 0:
            raise AssertionError("bad factor list")
        if pow(2, ORDER // prime, Q) == 1:
            raise AssertionError("claimed multiplicative order is not minimal")


def verify_wieferich_condition() -> int:
    residue = pow(2, ORDER, Q * Q)
    if (residue - 1) % Q != 0:
        raise AssertionError("order congruence failed modulo Q")
    common_factor = math.gcd(Q, (residue - 1) // Q)
    if common_factor <= 1:
        raise AssertionError("Q is not certified as a Wieferich number")
    return common_factor


def verify_near_half_power() -> None:
    if Q * Q - (1 << POWER_EXPONENT) != 9_120_093_673:
        raise AssertionError("near-half-power identity failed")

    numerator = (3 * Q + 1) ** 2 - 9 * (1 << POWER_EXPONENT)
    denominator = 9 * (1 << POWER_EXPONENT)
    if (numerator, denominator) != (Y_NUM, Y_DEN):
        raise AssertionError("exact y certificate failed")


def exp_upper_bound(x: Fraction, terms_through: int = 8) -> Fraction:
    """Rigorous upper bound for exp(x), for 0<=x<1.

    Sum through x^N/N!.  The remaining term ratios are at most
    x/(N+2), so the tail is bounded by a geometric series.
    """
    if not 0 <= x < 1:
        raise ValueError("require 0 <= x < 1")
    term = Fraction(1)
    total = term
    for k in range(1, terms_through + 1):
        term *= x / k
        total += term
    first_omitted = term * x / (terms_through + 1)
    ratio_bound = x / (terms_through + 2)
    return total + first_omitted / (1 - ratio_bound)


def verify_cycle_length_obstruction() -> dict[str, int]:
    even_r = MAX_EXCLUDED_CYCLE_LENGTH // 2
    odd_r = (MAX_EXCLUDED_CYCLE_LENGTH - 1) // 2

    # For both parity cases, r*y is below the rational constant c.
    if not even_r * Y_NUM * EXPONENT_BOUND.denominator < (
        Y_DEN * EXPONENT_BOUND.numerator
    ):
        raise AssertionError("even r*y bound failed")
    if not odd_r * Y_NUM * EXPONENT_BOUND.denominator < (
        Y_DEN * EXPONENT_BOUND.numerator
    ):
        raise AssertionError("odd r*y bound failed")

    # Prove exp(c) < H exactly, where H=2^30/(Q+1/3).
    h = Fraction(3 * (1 << 30), 3 * Q + 1)
    exp_upper = exp_upper_bound(EXPONENT_BOUND)
    if not exp_upper < h:
        raise AssertionError("rational exponential bound is not strong enough")
    if not h < 2:
        raise AssertionError("even-cycle headroom check failed")

    return {
        "maximum_even_r": even_r,
        "maximum_odd_r": odd_r,
        "exponent_bound_numerator": EXPONENT_BOUND.numerator,
        "exponent_bound_denominator": EXPONENT_BOUND.denominator,
        "exp_upper_numerator": exp_upper.numerator,
        "exp_upper_denominator": exp_upper.denominator,
        "headroom_numerator": h.numerator,
        "headroom_denominator": h.denominator,
    }


def verify_certificate() -> dict[str, object]:
    if Q != 3 * 29 * 271 * 32_203:
        raise AssertionError("factorization certificate failed")
    verify_order()
    common_factor = verify_wieferich_condition()
    verify_near_half_power()
    obstruction = verify_cycle_length_obstruction()

    first, first_a = odd_step(Q, 1)
    if (first, first_a) != (189_812_533, 2):
        raise AssertionError("unexpected first accelerated step")
    if math.gcd(first, Q) != 1:
        raise AssertionError("accelerated output is not coprime to Q")

    return {
        "Q": Q,
        "factorization": [3, 29, 271, 32_203],
        "order_of_2_mod_Q": ORDER,
        "wieferich_common_factor": common_factor,
        "Q_squared_minus_2_to_59": Q * Q - (1 << 59),
        "first_accelerated_value_from_1": first,
        "first_v2": first_a,
        "excluded_nontrivial_cycle_lengths_through": MAX_EXCLUDED_CYCLE_LENGTH,
        "obstruction_details": obstruction,
        "proved_dichotomy": (
            "the orbit tends to positive infinity or enters a nontrivial "
            "positive cycle longer than 41,500,000 accelerated steps"
        ),
    }


def main() -> None:
    print(json.dumps(verify_certificate(), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
