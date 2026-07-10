#!/usr/bin/env python3
"""Verify full-modulus predecessor delays below one million."""
from __future__ import annotations

from collections import Counter
from math import gcd

from verify_index_eight_small_sieve import (
    CUTOFF,
    D,
    H,
    M,
    ORDER_P,
    P,
    X,
    class_rep,
    verify_group_data,
)
from verify_two_generation_predecessor_cost import (
    O,
    R,
    initial_predecessor_state,
    one_generation_admissible,
    output_label_map,
    state_distances,
)
from verify_two_generation_small_reciprocal import (
    full_label,
    pohlig_hellman_data,
)

EXPECTED_GENUINE = 8727
EXPECTED_SMALL_DEAD = 2903
EXPECTED_SURVIVORS = 5824
EXPECTED_ZERO_DELAY = 133
EXPECTED_MAX_DELAY = 347
EXPECTED_DELAY_SUM = 207287
MAX_N = 753215
MAX_S = 1542129314381891391
GLOBAL_LAYER_BUDGET = 6257


def base_predecessor_mod_x(n: int, label: int) -> int:
    modulus = X * X
    numerator = (pow(2, label, modulus) * (n % modulus) - 1) % modulus
    assert numerator % X == 0
    return (numerator // X) % X


def verify() -> None:
    verify_group_data()
    small_labels = output_label_map()
    allowed_mod_m = set(small_labels)
    small_admissible = [
        one_generation_admissible(state, small_labels)
        for state in range(R)
    ]
    small_distances = state_distances(small_admissible)
    tables, coefficients = pohlig_hellman_data()

    x_squared = X * X
    power = pow(2, O, x_squared)
    assert (power - 1) % X == 0
    step = ((power - 1) // X) % X
    assert step == 63726582940809041391
    assert gcd(step, X) == 3

    def is_full_output_residue(value: int) -> bool:
        return (
            value % M in allowed_mod_m
            and pow(value % P, ORDER_P, P) == 1
        )

    genuine = 0
    small_dead = 0
    delays: Counter[int] = Counter()
    maximum_item: tuple[int, int, int] | None = None

    for t in range(1, H + 1):
        rho = class_rep(t)
        for n in range(rho, CUTOFF + 1, D):
            if pow(n, ORDER_P, P) != 1:
                continue
            genuine += 1
            label = full_label(n, t, tables, coefficients)

            # Preserve the earlier permanent/small-modulus rejection exactly.
            small_state = initial_predecessor_state(n, label)
            if small_distances[small_state] < 0:
                small_dead += 1
                continue

            state = base_predecessor_mod_x(n, label)
            delay: int | None = None
            for q in range(GLOBAL_LAYER_BUDGET + 1):
                if is_full_output_residue(state):
                    delay = q
                    break
                state = (state + step) % X

            assert delay is not None
            delays[delay] += 1
            if maximum_item is None or delay > maximum_item[2]:
                maximum_item = (n, label, delay)

    assert genuine == EXPECTED_GENUINE
    assert small_dead == EXPECTED_SMALL_DEAD
    assert sum(delays.values()) == EXPECTED_SURVIVORS
    assert delays[0] == EXPECTED_ZERO_DELAY
    assert max(delays) == EXPECTED_MAX_DELAY
    assert sum(delay * count for delay, count in delays.items()) == EXPECTED_DELAY_SUM
    assert maximum_item == (MAX_N, MAX_S, EXPECTED_MAX_DELAY)

    print("full-modulus predecessor delay verified")
    print(f"genuine representatives below cutoff={genuine}")
    print(f"small-modulus dead representatives={small_dead}")
    print(f"full-delay survivors={sum(delays.values())}")
    print(f"zero-delay representatives={delays[0]}")
    print(f"maximum delay={max(delays)}")
    print(f"sum of listed delays={sum(d*c for d,c in delays.items())}")
    print(f"maximum-delay item={maximum_item}")


if __name__ == "__main__":
    verify()
