#!/usr/bin/env python3
"""Verify the finite counterexample to the Tremblay 5x+1 count."""
from __future__ import annotations

import json


def step(n: int) -> int:
    return n // 2 if n % 2 == 0 else (5 * n + 1) // 2


def path(n: int, k: int) -> tuple[list[int], list[int]]:
    values = [n]
    parities: list[int] = []
    current = n
    for _ in range(k):
        parities.append(current & 1)
        current = step(current)
        values.append(current)
    return values, parities


def verify_certificate() -> dict[str, object]:
    values, parities = path(2, 3)
    if values != [2, 1, 3, 8]:
        raise AssertionError("unexpected counterexample trajectory")
    if parities != [0, 1, 1]:
        raise AssertionError("unexpected parity word")

    odd_steps = sum(parities)
    if odd_steps != 2:
        raise AssertionError("wrong number of odd steps")
    if not 5**odd_steps > 2**3:
        raise AssertionError("final-expansion condition should hold")
    if not values[-1] > values[0]:
        raise AssertionError("final value should exceed the start")
    if not values[1] < values[0]:
        raise AssertionError("first iterate should already be below the start")

    selected_by_endpoint: list[int] = []
    true_survivors: list[int] = []
    details: list[dict[str, object]] = []
    for n in range(1, 9):
        n_values, n_parities = path(n, 3)
        n_odd_steps = sum(n_parities)
        endpoint_selected = 5**n_odd_steps > 2**3
        survives = all(value >= n for value in n_values[1:])
        if endpoint_selected:
            selected_by_endpoint.append(n)
        if survives:
            true_survivors.append(n)
        details.append({
            "n": n,
            "path": n_values,
            "parities": n_parities,
            "odd_steps": n_odd_steps,
            "endpoint_condition": endpoint_selected,
            "stopping_time_greater_than_3": survives,
        })

    if selected_by_endpoint != [1, 2, 5, 7]:
        raise AssertionError("wrong endpoint-selected residue block")
    if true_survivors != [1, 5, 7]:
        raise AssertionError("wrong true stopping-time survivors")

    return {
        "counterexample_start": 2,
        "trajectory": values,
        "parity_word": parities,
        "odd_steps": odd_steps,
        "five_to_odd_steps": 5**odd_steps,
        "two_to_k": 2**3,
        "endpoint_selected_starts_mod_8": selected_by_endpoint,
        "true_survivors_mod_8": true_survivors,
        "overcounted_start": 2,
        "full_block_details": details,
        "status": "endpoint growth does not imply stopping time greater than k",
    }


def main() -> None:
    print(json.dumps(verify_certificate(), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
