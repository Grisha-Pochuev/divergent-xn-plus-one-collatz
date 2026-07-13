#!/usr/bin/env python3
"""Verify the odd-h phase harmonic barrier for the primary near-power candidate."""
from __future__ import annotations

import json
from fractions import Fraction
from math import gcd


def harmonic(n: int) -> Fraction:
    return sum((Fraction(1, k) for k in range(1, n + 1)), Fraction(0, 1))


def verify_phase_packing_regressions() -> int:
    """Check the phase-wise spacing inequality on exact synthetic examples."""
    checked = 0
    for g in (3, 5, 9, 15, 43):
        for h in (1, 2, 3, 5):
            for q in (1, 2, 4, 7):
                minima = [2 * j + 1 for j in range(h)]
                phases = [
                    [u + 2 * g * k for k in range(q)]
                    for u in minima
                ]
                lhs = sum(
                    (Fraction(1, n) for phase in phases for n in phase),
                    Fraction(0, 1),
                )
                rhs = sum((Fraction(1, u) for u in minima), Fraction(0, 1))
                rhs += Fraction(h, 2 * g) * harmonic(q - 1)
                if lhs > rhs:
                    raise AssertionError((g, h, q, lhs, rhs))
                checked += 1
    return checked


def verify_x5_phase_regression() -> dict[str, object]:
    """Reproduce the h=3 phase partition of 43 -> 27 -> 17 -> 43."""
    x = 5
    B = 8
    cycle = [43, 27, 17]
    valuations = [3, 3, 1]
    h = 3
    if gcd(*cycle) != 1:
        raise AssertionError("unexpected state gcd")
    boundary_g = 43
    residues = []
    for j in range(h):
        Sj = 0 if j == 0 else (B**j - x**j) // (B - x)
        residues.append(0 if j == 0 else (pow(B, -j, boundary_g) * Sj) % boundary_g)
    if residues != [0, 27, 17]:
        raise AssertionError(residues)
    if [n % boundary_g for n in cycle] != residues:
        raise AssertionError("phase regression failed")
    return {
        "cycle": cycle,
        "valuations": valuations,
        "h": h,
        "boundary_g": boundary_g,
        "phase_residues": residues,
    }


def primary_certificate() -> dict[str, object]:
    m = 4501
    B = 1 << m
    N = (1 << 500) - 1
    d = 349 * (1 << 500) - 347
    X = B - d

    # Bounds used to turn h distinct phase minima into a uniform 2^11 contribution.
    if not (N > (1 << 499)):
        raise AssertionError("N lower bound failed")
    if not (1 + (1 << 3508) < (1 << 3509)):
        raise AssertionError("phase-minimum logarithm bound failed")
    if not (3509 < (1 << 12)):
        raise AssertionError("phase-minimum reciprocal bound failed")

    # Primary arithmetic: X is large enough for the odd-h divisor-per-phase bound.
    if not (X > (1 << 4500)):
        raise AssertionError("X lower bound failed")

    # Under p <= 2^(2^4979), the phase tail is < 2^9479/X^2.
    K = 4979
    tail_numerator_exponent = K + 4500
    if tail_numerator_exponent != 9479:
        raise AssertionError("tail exponent bookkeeping failed")

    # Exact final contradiction:
    #   2^11 + 2^9479/X^2 < X/2^4023.
    lhs = (1 << 4034) * X * X + (1 << 13502)
    rhs = X**3
    if not (lhs < rhs):
        raise AssertionError("odd-h harmonic contradiction inequality failed")

    # The exit is negligible compared with the claimed full-cycle frontier.
    # It suffices that 2^4006 < 2^(2^4978).
    if not (4006 < (1 << 4978)):
        raise AssertionError("return subtraction bound failed")

    return {
        "X_bits": X.bit_length(),
        "N_bits": N.bit_length(),
        "phase_minima_upper": "sum_j 1/u_j < 2^11",
        "odd_h_divisor_per_phase": "g/h > X^2/2^4500",
        "conditional_full_cycle_frontier": "p > 2^(2^4979)",
        "conditional_return_frontier": "L_return > 2^(2^4978)",
        "exact_final_inequality": True,
        "strict_prize_solution": False,
    }


def main() -> None:
    report = {
        "phase_packing_regressions": verify_phase_packing_regressions(),
        "x5_regression": verify_x5_phase_regression(),
        "primary": primary_certificate(),
    }
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
