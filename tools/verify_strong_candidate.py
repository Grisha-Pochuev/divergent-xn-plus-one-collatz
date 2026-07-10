#!/usr/bin/env python3
"""Verify the finite arithmetic certificate for Q=759250131."""
from __future__ import annotations

import json
import math

from xn1 import odd_step


Q = 759_250_131
ORDER = 6_762_420
ORDER_PRIME_FACTORS = (2, 3, 5, 7, 1789)
MAX_EXCLUDED_CYCLE_LENGTH = 35_000_000
POWER_EXPONENT = 59

# (Q+1/3)^2 = 2^59 * (1 + Y_NUM/Y_DEN)
Y_NUM = 86_636_343_844
Y_DEN = 5_188_146_770_730_811_392


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


def verify_cycle_length_obstruction() -> dict[str, int]:
    # Even p=2r <= 35,000,000.  The sufficient inequality is r*y < 1/2.
    even_r = MAX_EXCLUDED_CYCLE_LENGTH // 2
    if not 2 * even_r * Y_NUM < Y_DEN:
        raise AssertionError("even cycle inequality failed")

    # Odd p=2r+1 <= 35,000,000.  The sufficient inequality is
    # r*y < 1-(Q+1/3)/2^30.
    odd_r = (MAX_EXCLUDED_CYCLE_LENGTH - 1) // 2
    headroom_num = 3 * (1 << 30) - (3 * Q + 1)
    headroom_den = 3 * (1 << 30)
    if headroom_num <= 0:
        raise AssertionError("Q is not below 2^30-1/3")
    if not odd_r * Y_NUM * headroom_den < Y_DEN * headroom_num:
        raise AssertionError("odd cycle inequality failed")

    return {
        "maximum_even_r": even_r,
        "maximum_odd_r": odd_r,
        "odd_headroom_numerator": headroom_num,
        "odd_headroom_denominator": headroom_den,
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
            "positive cycle longer than 35,000,000 accelerated steps"
        ),
    }


def main() -> None:
    print(json.dumps(verify_certificate(), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
