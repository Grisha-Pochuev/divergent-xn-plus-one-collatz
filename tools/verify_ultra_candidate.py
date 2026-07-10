#!/usr/bin/env python3
"""Verify the 120-quintillion cycle barrier with exact arithmetic."""
from __future__ import annotations

from fractions import Fraction
from math import isqrt
import json
import math

from verify_strong_candidate import EXPONENT_BOUND, exp_upper_bound
from xn1 import odd_step


X = 104_350_542_602_662_257_699
COFACTOR = 4_969_073_457_269_631_319
K = 66
HALF_POWER_EXPONENT = 133
BARRIER = 120_000_000_000_000_000_000
MINIMUM_NONTRIVIAL_OUTPUT = 11
SQUARE_EXCESS = 42_455_133_039_302_008_009
Y_NUM = 7_432_783_035_014_112_638_468
Y_DEN = 1_317_573_324_717_873_730_530_186_479_975_806_514_757_632


def verify_structure() -> None:
    if X != 21 * COFACTOR:
        raise AssertionError("factor-21 certificate failed")
    if COFACTOR % 6 != 1:
        raise AssertionError("cofactor must be 1 modulo 6")
    if X % 9 == 0:
        raise AssertionError("3 must divide X exactly once")

    target = 1 << HALF_POWER_EXPONENT
    root = isqrt(target)
    if root != X - 1:
        raise AssertionError("X is not floor(2^66*sqrt(2))+1")
    if X * X - target != SQUARE_EXCESS:
        raise AssertionError("square-excess identity failed")


def verify_output_residue_bound() -> None:
    inverse_residues = tuple(pow(2, -a, 21) for a in range(6))
    if inverse_residues != (1, 11, 16, 8, 4, 2):
        raise AssertionError("inverse-power residues modulo 21 changed")

    least_odd_representatives = []
    for residue in inverse_residues:
        value = residue
        while value % 2 == 0:
            value += 21
        least_odd_representatives.append(value)
    if tuple(least_odd_representatives) != (1, 11, 37, 29, 25, 23):
        raise AssertionError("least odd representative calculation failed")

    nontrivial_minimum = min(value for value in least_odd_representatives if value != 1)
    if nontrivial_minimum != MINIMUM_NONTRIVIAL_OUTPUT:
        raise AssertionError("wrong nontrivial output lower bound")


def verify_near_half_power() -> None:
    d = MINIMUM_NONTRIVIAL_OUTPUT
    numerator = (d * X + 1) ** 2 - d * d * (1 << HALF_POWER_EXPONENT)
    denominator = d * d * (1 << HALF_POWER_EXPONENT)
    if (numerator, denominator) != (Y_NUM, Y_DEN):
        raise AssertionError("exact y identity failed")


def verify_cycle_barrier() -> dict[str, int]:
    even_r = BARRIER // 2
    odd_r = (BARRIER - 1) // 2

    for label, r in (("even", even_r), ("odd", odd_r)):
        if not r * Y_NUM * EXPONENT_BOUND.denominator < (
            Y_DEN * EXPONENT_BOUND.numerator
        ):
            raise AssertionError(f"{label} r*y bound failed")

    d = MINIMUM_NONTRIVIAL_OUTPUT
    headroom = Fraction(d * (1 << (K + 1)), d * X + 1)
    exponential_upper = exp_upper_bound(EXPONENT_BOUND)
    if not exponential_upper < headroom < 2:
        raise AssertionError("rational exponential headroom failed")

    return {
        "maximum_even_r": even_r,
        "maximum_odd_r": odd_r,
        "minimum_nontrivial_cycle_element": MINIMUM_NONTRIVIAL_OUTPUT,
        "headroom_numerator": headroom.numerator,
        "headroom_denominator": headroom.denominator,
        "exp_upper_numerator": exponential_upper.numerator,
        "exp_upper_denominator": exponential_upper.denominator,
    }


def verify_certificate() -> dict[str, object]:
    verify_structure()
    verify_output_residue_bound()
    verify_near_half_power()
    obstruction = verify_cycle_barrier()

    first, first_a = odd_step(X, 1)
    if (first, first_a) != (26_087_635_650_665_564_425, 2):
        raise AssertionError("unexpected first accelerated step")
    if math.gcd(first, X) != 1:
        raise AssertionError("accelerated output must be coprime to X")

    return {
        "X": X,
        "n0": 1,
        "cofactor_after_21": COFACTOR,
        "X_squared_minus_2_to_133": SQUARE_EXCESS,
        "first_accelerated_value": first,
        "first_v2": first_a,
        "minimum_nontrivial_cycle_element": MINIMUM_NONTRIVIAL_OUTPUT,
        "excluded_nontrivial_cycle_lengths_through": BARRIER,
        "obstruction_details": obstruction,
        "proved_dichotomy": (
            "the orbit tends to positive infinity or enters a nontrivial "
            "positive cycle longer than 120,000,000,000,000,000,000 steps"
        ),
    }


def main() -> None:
    print(json.dumps(verify_certificate(), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
