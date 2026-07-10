#!/usr/bin/env python3
"""Verify exact inverse-window charging at depths two and three."""
from __future__ import annotations

from functools import lru_cache
from fractions import Fraction

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
from verify_two_generation_small_reciprocal import (
    full_label,
    pohlig_hellman_data,
)

TARGET = 177780727155637125195
TOTAL_VALUATION = 11822418355849868825468
INCREMENTAL_BUDGET = 11644637628694231700273
LAYER_BUDGET = 6257
INF = LAYER_BUDGET + 1

EXPECTED_SURVIVORS = 5824
EXPECTED_H2_MAX = 490
EXPECTED_H2_SUM = 478043
EXPECTED_H3_MAX = 519
EXPECTED_H3_SUM = 685875


def fractional_dual(
    items: list[tuple[int, int, int, int]],
    budget: int,
    expected_full: int,
    expected_boundary: tuple[int, int, int, int],
) -> Fraction:
    """Items are (n, scaled_cost, label, h_L)."""
    ordered = sorted(items, key=lambda item: item[0] * item[1])
    spent = 0
    full = 0
    boundary: tuple[int, int, int, int] | None = None
    for item in ordered:
        if spent + item[1] <= budget:
            spent += item[1]
            full += 1
        else:
            boundary = item
            break

    assert full == expected_full
    assert boundary == expected_boundary
    assert boundary is not None
    denominator = boundary[0] * boundary[1]

    bound = Fraction(budget, denominator)
    positive_terms = 0
    for n, cost, _label, _window in items:
        if n * cost < denominator:
            bound += Fraction(1, n) - Fraction(cost, denominator)
            positive_terms += 1
    assert positive_terms == expected_full
    return bound


def verify() -> None:
    verify_group_data()
    assert TOTAL_VALUATION == 133 * ((TARGET - 1) // 2) + 67
    assert INCREMENTAL_BUDGET == TOTAL_VALUATION - TARGET
    assert INCREMENTAL_BUDGET // O == LAYER_BUDGET

    small_labels = output_label_map()
    allowed_mod_m = set(small_labels)
    small_admissible = [
        one_generation_admissible(state, small_labels)
        for state in range(R)
    ]
    small_distances = state_distances(small_admissible)
    tables, coefficients = pohlig_hellman_data()

    def is_full_output_residue(value: int) -> bool:
        return (
            value % M in allowed_mod_m
            and pow(value % P, ORDER_P, P) == 1
        )

    def label_of_output(value: int) -> int:
        t = small_labels.get(value % M)
        if t is None or pow(value % P, ORDER_P, P) != 1:
            raise AssertionError("residue is not a full output")
        return full_label(value % X, t, tables, coefficients)

    max_depth = 3
    moduli = [1] + [X**power for power in range(1, max_depth + 2)]
    multipliers: dict[int, int] = {}
    increments: dict[int, int] = {}
    for depth in range(1, max_depth + 1):
        power = pow(2, O, moduli[depth + 1])
        assert (power - 1) % X == 0
        multipliers[depth] = power % moduli[depth]
        increments[depth] = ((power - 1) // X) % moduli[depth]

    def base_predecessor(target: int, label: int, depth: int) -> int:
        modulus = moduli[depth + 1]
        numerator = (
            pow(2, label, modulus) * (target % modulus) - 1
        ) % modulus
        assert numerator % X == 0
        return (numerator // X) % moduli[depth]

    @lru_cache(maxsize=None)
    def minimum_layer_sum(
        target: int,
        label: int,
        depth: int,
        limit: int,
    ) -> int:
        """Minimum layer sum in a depth-edge inverse window, truncated at limit."""
        assert 1 <= depth <= max_depth
        assert 0 <= limit <= LAYER_BUDGET
        predecessor = base_predecessor(target, label, depth)
        best = INF

        for q in range(limit + 1):
            if q >= best:
                break
            residue = predecessor % X
            if is_full_output_residue(residue):
                if depth == 1:
                    candidate = q
                else:
                    next_label = label_of_output(residue)
                    remaining = limit - q
                    sub = minimum_layer_sum(
                        predecessor,
                        next_label,
                        depth - 1,
                        remaining,
                    )
                    candidate = INF if sub > remaining else q + sub
                if candidate < best:
                    best = candidate
                    if best == 0:
                        break

            predecessor = (
                multipliers[depth] * predecessor + increments[depth]
            ) % moduli[depth]

        return best

    candidates: list[tuple[int, int]] = []
    genuine = 0
    small_dead = 0
    for t in range(1, H + 1):
        rho = class_rep(t)
        for n in range(rho, CUTOFF + 1, D):
            if pow(n, ORDER_P, P) != 1:
                continue
            genuine += 1
            label = full_label(n, t, tables, coefficients)
            state = initial_predecessor_state(n, label)
            if small_distances[state] < 0:
                small_dead += 1
                continue
            candidates.append((n, label))

    assert genuine == 8727
    assert small_dead == 2903
    assert len(candidates) == EXPECTED_SURVIVORS

    h2_items: list[tuple[int, int, int, int]] = []
    h3_items: list[tuple[int, int, int, int]] = []
    h2_sum = 0
    h3_sum = 0
    h2_maximum = 0
    h3_maximum = 0

    for n, label in candidates:
        h2 = minimum_layer_sum(n, label, 2, LAYER_BUDGET)
        h3 = minimum_layer_sum(n, label, 3, LAYER_BUDGET)
        assert h2 <= LAYER_BUDGET
        assert h3 <= LAYER_BUDGET

        h2_sum += h2
        h3_sum += h3
        h2_maximum = max(h2_maximum, h2)
        h3_maximum = max(h3_maximum, h3)

        cost2 = 2 * (label - 1) + O * h2
        cost3 = 3 * (label - 1) + O * h3
        h2_items.append((n, cost2, label, h2))
        h3_items.append((n, cost3, label, h3))

    assert h2_maximum == EXPECTED_H2_MAX
    assert h2_sum == EXPECTED_H2_SUM
    assert h3_maximum == EXPECTED_H3_MAX
    assert h3_sum == EXPECTED_H3_SUM

    h2_bound = fractional_dual(
        h2_items,
        2 * INCREMENTAL_BUDGET,
        expected_full=258,
        expected_boundary=(
            48_497,
            68_225_419_084_474_722_250,
            1_548_519_004_723_674_501,
            35,
        ),
    )
    assert h2_bound < Fraction(85_634_587, 1_000_000_000)

    h3_bound = fractional_dual(
        h3_items,
        3 * INCREMENTAL_BUDGET,
        expected_full=205,
        expected_boundary=(
            17_669,
            294_001_978_938_214_713_492,
            618_223_181_506_832_115,
            157,
        ),
    )
    assert h3_bound < Fraction(85_243_521, 1_000_000_000)

    log2_lower, _ = log_bounds(Fraction(2, 1), 40)
    energy = Fraction(X * X, 1 << 133)
    _, eta_upper = log_bounds(energy, 4)
    required = X * (log2_lower - TARGET * eta_upper) / 2

    residual2 = required - h2_bound
    residual3 = required - h3_bound
    assert residual2 > Fraction(14_299, 1_000_000)
    assert residual3 > Fraction(14_690, 1_000_000)

    needed2 = (residual2 * CUTOFF).numerator // (
        residual2 * CUTOFF
    ).denominator + 1
    needed3 = (residual3 * CUTOFF).numerator // (
        residual3 * CUTOFF
    ).denominator + 1
    assert needed2 == 14_300
    assert needed3 == 14_691

    print("finite inverse-window charging verified")
    print(f"survivors below cutoff={len(candidates)}")
    print(f"h2 maximum={h2_maximum}, h2 sum={h2_sum}")
    print(f"h3 maximum={h3_maximum}, h3 sum={h3_sum}")
    print(f"depth-two reciprocal bound approximately {float(h2_bound):.15f}")
    print(f"depth-three reciprocal bound approximately {float(h3_bound):.15f}")
    print(f"required threshold approximately {float(required):.15f}")
    print(f"necessary values above cutoff at depth two>={needed2}")
    print(f"necessary values above cutoff at depth three>={needed3}")


if __name__ == "__main__":
    verify()
