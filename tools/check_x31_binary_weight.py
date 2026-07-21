#!/usr/bin/env python3
"""Finite exact reconnaissance for the accelerated X=31 orbit from n0=3.

This script checks the conjectural binary-weight inequality

    A_t + popcount(n_t) <= 4*t + 2,

and the exact equivalent zero-bit formulation

    zero_bits(n_t) + sum_{j<t} delta_j >= t,

where

    delta_j = bit_length(n_j) + 5 - bit_length(31*n_j + 1) in {0,1}.

It also checks the stronger conjectural inequality

    zero_bits(n_t) >= t.

Every computation is exact integer arithmetic. A finite check is evidence only
and is not a proof of divergence.
"""
from __future__ import annotations

import argparse
import json


def v2(value: int) -> int:
    if value <= 0:
        raise ValueError("v2 requires a positive integer")
    return (value & -value).bit_length() - 1


def update_minimum(
    value: int,
    step: int,
    current_value: int | None,
    current_step: int | None,
) -> tuple[int, int]:
    if current_value is None or value < current_value:
        return value, step
    assert current_step is not None
    return current_value, current_step


def check_prefix(steps: int) -> dict[str, int | bool | None]:
    if steps < 1:
        raise ValueError("steps must be positive")

    x = 31
    n = 3
    cumulative_halvings = 0
    cumulative_length_defects = 0

    minimum_original_slack: int | None = None
    minimum_original_slack_step: int | None = None
    minimum_strong_zero_slack: int | None = None
    minimum_strong_zero_slack_step: int | None = None

    first_original_failure_step: int | None = None
    first_strong_zero_failure_step: int | None = None

    for t in range(1, steps + 1):
        source_bit_length = n.bit_length()
        numerator = x * n + 1
        valuation = v2(numerator)

        length_defect = source_bit_length + 5 - numerator.bit_length()
        if length_defect not in (0, 1):
            raise AssertionError(
                f"unexpected length defect {length_defect} at step {t}"
            )
        cumulative_length_defects += length_defect

        n = numerator >> valuation
        cumulative_halvings += valuation

        binary_weight = n.bit_count()
        zero_bits = n.bit_length() - binary_weight

        original_slack = 4 * t + 2 - (cumulative_halvings + binary_weight)
        equivalent_slack = zero_bits + cumulative_length_defects - t
        if original_slack != equivalent_slack:
            raise AssertionError(
                "exact slack identity failed at step "
                f"{t}: {original_slack} != {equivalent_slack}"
            )

        strong_zero_slack = zero_bits - t

        minimum_original_slack, minimum_original_slack_step = update_minimum(
            original_slack,
            t,
            minimum_original_slack,
            minimum_original_slack_step,
        )
        minimum_strong_zero_slack, minimum_strong_zero_slack_step = update_minimum(
            strong_zero_slack,
            t,
            minimum_strong_zero_slack,
            minimum_strong_zero_slack_step,
        )

        if original_slack < 0 and first_original_failure_step is None:
            first_original_failure_step = t
        if strong_zero_slack < 0 and first_strong_zero_failure_step is None:
            first_strong_zero_failure_step = t

    assert minimum_original_slack is not None
    assert minimum_original_slack_step is not None
    assert minimum_strong_zero_slack is not None
    assert minimum_strong_zero_slack_step is not None

    final_binary_weight = n.bit_count()
    final_zero_bits = n.bit_length() - final_binary_weight

    return {
        "X": x,
        "n0": 3,
        "steps_checked": steps,
        "final_orbit_value_bits": n.bit_length(),
        "final_cumulative_halvings": cumulative_halvings,
        "final_binary_weight": final_binary_weight,
        "final_zero_bits": final_zero_bits,
        "final_cumulative_length_defects": cumulative_length_defects,
        "minimum_original_slack": minimum_original_slack,
        "minimum_original_slack_step": minimum_original_slack_step,
        "first_original_failure_step": first_original_failure_step,
        "original_inequality_holds": first_original_failure_step is None,
        "minimum_strong_zero_slack": minimum_strong_zero_slack,
        "minimum_strong_zero_slack_step": minimum_strong_zero_slack_step,
        "first_strong_zero_failure_step": first_strong_zero_failure_step,
        "strong_zero_inequality_holds": first_strong_zero_failure_step is None,
        "exact_slack_identity_holds": True,
        "is_proof_of_infinite_divergence": False,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--steps", type=int, default=100_000)
    args = parser.parse_args()
    print(json.dumps(check_prefix(args.steps), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
