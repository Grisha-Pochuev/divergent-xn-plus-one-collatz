#!/usr/bin/env python3
"""Finite exact reconnaissance for the accelerated X=31 orbit from n0=3.

This script checks the conjectural binary-weight inequality

    A_t + popcount(n_t) <= 4*t + 2,

where A_t is the cumulative halving count. A finite check is evidence only and
is not a proof of divergence.
"""
from __future__ import annotations

import argparse
import json


def v2(value: int) -> int:
    if value <= 0:
        raise ValueError("v2 requires a positive integer")
    return (value & -value).bit_length() - 1


def check_prefix(steps: int) -> dict[str, int | bool | None]:
    if steps < 1:
        raise ValueError("steps must be positive")

    x = 31
    n = 3
    cumulative_halvings = 0
    minimum_slack: int | None = None
    minimum_slack_step: int | None = None
    first_failure_step: int | None = None

    for t in range(1, steps + 1):
        numerator = x * n + 1
        valuation = v2(numerator)
        n = numerator >> valuation
        cumulative_halvings += valuation

        slack = 4 * t + 2 - (cumulative_halvings + n.bit_count())
        if minimum_slack is None or slack < minimum_slack:
            minimum_slack = slack
            minimum_slack_step = t
        if slack < 0 and first_failure_step is None:
            first_failure_step = t

    assert minimum_slack is not None
    assert minimum_slack_step is not None
    return {
        "X": x,
        "n0": 3,
        "steps_checked": steps,
        "final_orbit_value_bits": n.bit_length(),
        "final_cumulative_halvings": cumulative_halvings,
        "final_binary_weight": n.bit_count(),
        "minimum_slack": minimum_slack,
        "minimum_slack_step": minimum_slack_step,
        "first_failure_step": first_failure_step,
        "finite_inequality_holds": first_failure_step is None,
        "is_proof_of_infinite_divergence": False,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--steps", type=int, default=100_000)
    args = parser.parse_args()
    print(json.dumps(check_prefix(args.steps), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
