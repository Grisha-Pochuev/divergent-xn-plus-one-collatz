#!/usr/bin/env python3
"""Verify the symmetric full-transition edge-cost dual below one million."""
from __future__ import annotations

from fractions import Fraction
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

TARGETS = (
    177780727155637125193,
    177780727155637125195,
)
EXPECTED_CANDIDATES = 71_318
EXPECTED_GENUINE = 8_727
EXPECTED_DEAD = 2_903
EXPECTED_SURVIVORS = 5_824
EXPECTED_FULL = 562
EXPECTED_BOUNDARY = (
    33_223,
    93_701_439_040_142_322_396,
    549_750_138_304_358_466,
    25,
    111_144_508_941_716_432,
)


def base_predecessor_mod_x(n: int, label: int) -> int:
    modulus = X * X
    numerator = (pow(2, label, modulus) * (n % modulus) - 1) % modulus
    assert numerator % X == 0
    return (numerator // X) % X


def fractional_dual(
    items: list[tuple[int, int, int, int, int]],
    budget: int,
) -> tuple[Fraction, int, tuple[int, int, int, int, int]]:
    """Items are (n, edge_cost, target_label, delay, source_label)."""
    ordered = sorted(items, key=lambda item: item[0] * item[1])
    spent = 0
    full = 0
    boundary = None
    for item in ordered:
        if spent + item[1] <= budget:
            spent += item[1]
            full += 1
        else:
            boundary = item
            break
    assert boundary is not None

    denominator = boundary[0] * boundary[1]
    bound = Fraction(budget, denominator)
    positive = 0
    for n, cost, _v, _q, _u in items:
        if n * cost < denominator:
            bound += Fraction(1, n) - Fraction(cost, denominator)
            positive += 1
    assert positive == full
    return bound, full, boundary


def verify() -> None:
    verify_group_data()
    small_labels = output_label_map()
    allowed_mod_m = set(small_labels)
    admissible = [
        one_generation_admissible(state, small_labels)
        for state in range(R)
    ]
    distances = state_distances(admissible)
    tables, coefficients = pohlig_hellman_data()

    modulus = X * X
    power = pow(2, O, modulus)
    assert (power - 1) % X == 0
    step = ((power - 1) // X) % X
    assert step == 63_726_582_940_809_041_391
    assert gcd(step, X) == 3

    def is_full_output_residue(value: int) -> bool:
        return (
            value % M in allowed_mod_m
            and pow(value % P, ORDER_P, P) == 1
        )

    candidate_count = 0
    genuine_count = 0
    dead_count = 0
    items: list[tuple[int, int, int, int, int]] = []

    for small_target_label in range(1, H + 1):
        rho = class_rep(small_target_label)
        for n in range(rho, CUTOFF + 1, D):
            candidate_count += 1
            if pow(n, ORDER_P, P) != 1:
                continue
            genuine_count += 1

            target_label = full_label(
                n, small_target_label, tables, coefficients
            )
            state = initial_predecessor_state(n, target_label)
            if distances[state] < 0:
                dead_count += 1
                continue

            predecessor = base_predecessor_mod_x(n, target_label)
            delay = None
            for q in range(6_258):
                if is_full_output_residue(predecessor):
                    delay = q
                    break
                predecessor = (predecessor + step) % X
            assert delay is not None

            predecessor_small_label = small_labels[predecessor % M]
            source_label = full_label(
                predecessor,
                predecessor_small_label,
                tables,
                coefficients,
            )
            edge_cost = (
                source_label - 1
                + target_label - 1
                + 2 * O * delay
            )
            assert edge_cost > 0
            items.append(
                (n, edge_cost, target_label, delay, source_label)
            )

    assert candidate_count == EXPECTED_CANDIDATES
    assert genuine_count == EXPECTED_GENUINE
    assert dead_count == EXPECTED_DEAD
    assert len(items) == EXPECTED_SURVIVORS

    for target in TARGETS:
        total_valuation = (133 * target + 1) // 2
        budget = 2 * (total_valuation - target)
        bound, full, boundary = fractional_dual(items, budget)
        assert full == EXPECTED_FULL
        assert boundary == EXPECTED_BOUNDARY
        assert bound < Fraction(87_543_786, 1_000_000_000)

        print(f"target={target}")
        print(f"symmetric edge bound approximately {float(bound):.15f}")
        print(f"fractional boundary after {full} complete items")

    print("symmetric edge-cost dual verified")
    print(f"surviving representatives={len(items)}")


if __name__ == "__main__":
    verify()
