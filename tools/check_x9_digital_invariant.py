#!/usr/bin/env python3
"""Finite reconnaissance for the X=9, n0=1 digital-invariant route.

This script does NOT prove divergence.  It verifies, with exact integer
arithmetic, the identity

    S_t = 2^A_t * n_t,
    S_(t+1) = 9*S_t + 2^v2(S_t),

where A_t is the cumulative halving count of the accelerated 9n+1 orbit.
It then checks the finite-prefix inequality A_t <= 3*t-2.
"""
from __future__ import annotations

import argparse
import json


def v2(value: int) -> int:
    if value <= 0:
        raise ValueError("v2 requires a positive integer")
    return (value & -value).bit_length() - 1


def check_prefix(steps: int) -> dict[str, int | bool]:
    if steps < 1:
        raise ValueError("steps must be positive")

    n = 1
    cumulative = 0
    s_value = 1
    minimum_slack = 10**30
    minimum_slack_step = 0

    for t in range(1, steps + 1):
        numerator = 9 * n + 1
        valuation = v2(numerator)
        n = numerator >> valuation
        cumulative += valuation

        s_value = 9 * s_value + (1 << v2(s_value))

        if v2(s_value) != cumulative:
            raise AssertionError("v2(S_t) != cumulative halving count")
        if s_value != (1 << cumulative) * n:
            raise AssertionError("S_t != 2^A_t * n_t")

        slack = 3 * t - cumulative
        if slack < minimum_slack:
            minimum_slack = slack
            minimum_slack_step = t

    return {
        "X": 9,
        "n0": 1,
        "steps_checked": steps,
        "final_orbit_value_bits": n.bit_length(),
        "final_cumulative_halvings": cumulative,
        "minimum_slack_3t_minus_A": minimum_slack,
        "minimum_slack_step": minimum_slack_step,
        "finite_inequality_A_le_3t_minus_2": minimum_slack >= 2,
        "is_proof_of_infinite_divergence": False,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--steps", type=int, default=10_000)
    args = parser.parse_args()
    print(json.dumps(check_prefix(args.steps), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
