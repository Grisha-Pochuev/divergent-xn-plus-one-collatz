#!/usr/bin/env python3
"""Verify the two-generation reciprocal bound below one million."""
from __future__ import annotations

from fractions import Fraction
from math import prod

from verify_index_eight_small_sieve import (
    CUTOFF,
    D,
    H,
    M,
    ORDER_P,
    P,
    X,
    class_rep,
    log_bounds,
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

TARGET = 177780727155637125195
EXPECTED_TOTAL_VALUATION = 11822418355849868825468
EXPECTED_CANDIDATES = 71318
EXPECTED_GENUINE = 8727
EXPECTED_DEAD = 2903
EXPECTED_SURVIVING = 5824
EXPECTED_FULL_ITEMS = 2362
BOUNDARY_N = 106255
BOUNDARY_S = 1741820788677582842
BOUNDARY_DELAY = 10
BOUNDARY_WEIGHT = 20349929667256832342
PH_FACTORS = (25, 2677, 15137, 852763)


def pohlig_hellman_data() -> tuple[dict[int, dict[int, int]], dict[int, int]]:
    """Tables for exact base-2 discrete logarithms in the smooth subgroup."""
    assert prod(PH_FACTORS) == ORDER_P
    tables: dict[int, dict[int, int]] = {}
    coefficients: dict[int, int] = {}

    for q in PH_FACTORS:
        generator = pow(2, ORDER_P // q, P)
        table: dict[int, int] = {}
        value = 1
        for exponent in range(q):
            assert value not in table
            table[value] = exponent
            value = value * generator % P
        assert value == 1
        assert len(table) == q
        tables[q] = table

        complementary = ORDER_P // q
        coefficients[q] = (
            complementary * pow(complementary, -1, q)
        ) % ORDER_P

    return tables, coefficients


def discrete_log_2(
    value: int,
    tables: dict[int, dict[int, int]],
    coefficients: dict[int, int],
) -> int:
    exponent = 0
    for q in PH_FACTORS:
        projected = pow(value, ORDER_P // q, P)
        residue = tables[q].get(projected)
        if residue is None:
            raise AssertionError("value is outside the base-2 subgroup")
        exponent = (exponent + residue * coefficients[q]) % ORDER_P
    assert pow(2, exponent, P) == value
    return exponent


def full_label(
    n: int,
    small_label: int,
    tables: dict[int, dict[int, int]],
    coefficients: dict[int, int],
) -> int:
    """Least positive s<=ord_X(2) with 2^s*n == 1 (mod X)."""
    exponent_mod_p = discrete_log_2(pow(n, -1, P), tables, coefficients)
    inverse_h = pow(H, -1, ORDER_P)
    lift = ((exponent_mod_p - small_label) * inverse_h) % ORDER_P
    label = small_label + H * lift
    assert 1 <= label <= O
    assert pow(2, label, X) * (n % X) % X == 1
    return label


def verify() -> None:
    verify_group_data()
    labels = output_label_map()
    admissible = [one_generation_admissible(state, labels) for state in range(R)]
    distances = state_distances(admissible)
    tables, coefficients = pohlig_hellman_data()

    candidate_count = 0
    genuine_count = 0
    dead_count = 0
    items: list[tuple[int, int, int, int]] = []

    for small_label in range(1, H + 1):
        rho = class_rep(small_label)
        for n in range(rho, CUTOFF + 1, D):
            candidate_count += 1
            if pow(n, ORDER_P, P) != 1:
                continue
            genuine_count += 1

            label = full_label(n, small_label, tables, coefficients)
            state = initial_predecessor_state(n, label)
            delay = distances[state]
            if delay < 0:
                dead_count += 1
                continue

            weight = label + O * delay
            items.append((n, weight, label, delay))

    assert candidate_count == EXPECTED_CANDIDATES
    assert genuine_count == EXPECTED_GENUINE
    assert dead_count == EXPECTED_DEAD
    assert len(items) == EXPECTED_SURVIVING

    total_valuation = 133 * ((TARGET - 1) // 2) + 67
    assert total_valuation == EXPECTED_TOTAL_VALUATION

    ordered = sorted(items, key=lambda item: item[0] * item[1])
    spent = 0
    full_items = 0
    boundary: tuple[int, int, int, int] | None = None
    for item in ordered:
        if spent + item[1] <= total_valuation:
            spent += item[1]
            full_items += 1
        else:
            boundary = item
            break

    assert full_items == EXPECTED_FULL_ITEMS
    assert boundary == (
        BOUNDARY_N,
        BOUNDARY_WEIGHT,
        BOUNDARY_S,
        BOUNDARY_DELAY,
    )

    # Exact Lagrange dual.  With lambda=1/(n_boundary*w_boundary),
    # x/n <= lambda*w*x + max(0,1/n-lambda*w) for every 0<=x<=1.
    boundary_efficiency_denominator = BOUNDARY_N * BOUNDARY_WEIGHT
    reciprocal_bound = Fraction(
        total_valuation,
        boundary_efficiency_denominator,
    )
    positive_dual_terms = 0
    for n, weight, _label, _delay in items:
        if n * weight < boundary_efficiency_denominator:
            reciprocal_bound += Fraction(1, n)
            reciprocal_bound -= Fraction(weight, boundary_efficiency_denominator)
            positive_dual_terms += 1

    assert positive_dual_terms == EXPECTED_FULL_ITEMS
    assert reciprocal_bound < Fraction(99005753, 1_000_000_000)

    # Exact lower bound on the correction required by the target length.
    log2_lower, _ = log_bounds(Fraction(2, 1), 40)
    energy = Fraction(X * X, 1 << 133)
    _, eta_upper = log_bounds(energy, 4)
    assert TARGET * eta_upper < log2_lower
    gap_lower = (log2_lower - TARGET * eta_upper) / 2
    required_reciprocal = X * gap_lower
    residual = required_reciprocal - reciprocal_bound

    assert residual > Fraction(928, 1_000_000)
    # Each distinct value above one million contributes strictly less than
    # 10^-6, so at least 929 such values are necessary to cover the residual.
    minimum_large_values = 929
    assert (minimum_large_values - 1) * Fraction(1, CUTOFF) <= Fraction(928, 1_000_000)
    assert minimum_large_values * Fraction(1, CUTOFF) > Fraction(928, 1_000_000)

    print("two-generation small reciprocal bound verified")
    print(f"target={TARGET}")
    print(f"genuine representatives below cutoff={genuine_count}")
    print(f"permanently dead representatives={dead_count}")
    print(f"two-generation survivors={len(items)}")
    print(f"fractional boundary after {full_items} complete items")
    print(f"reciprocal bound approximately {float(reciprocal_bound):.15f}")
    print(f"required threshold approximately {float(required_reciprocal):.15f}")
    print(f"strict residual approximately {float(residual):.15f}")
    print(f"necessary distinct values above cutoff>={minimum_large_values}")


if __name__ == "__main__":
    verify()
