#!/usr/bin/env python3
"""Verify the combined depth-three and symmetric-edge reciprocal dual."""
from __future__ import annotations

from fractions import Fraction
from functools import lru_cache

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
BUDGET = 11644637628694231700273
LAYER_BUDGET = 6257
INF = LAYER_BUDGET + 1
EXPECTED_SURVIVORS = 5824
EXPECTED_H3_MAX = 519
EXPECTED_H3_SUM = 685875
EXPECTED_FULL = 203
EXPECTED_BOUNDARY = (
    18439,
    13761316206075706083144,
    1588577149097258286,
    140,
    265279255747401267855,
    259745073615874626969,
    69,
    1364593942383725585,
)


def verify() -> None:
    verify_group_data()
    assert BUDGET == (133 * TARGET + 1) // 2 - TARGET

    small_labels = output_label_map()
    allowed_mod_m = set(small_labels)
    admissible = [
        one_generation_admissible(state, small_labels)
        for state in range(R)
    ]
    distances = state_distances(admissible)
    tables, coefficients = pohlig_hellman_data()

    def is_full(value: int) -> bool:
        return (
            value % M in allowed_mod_m
            and pow(value % P, ORDER_P, P) == 1
        )

    def label_of_output(value: int) -> int:
        t = small_labels.get(value % M)
        assert t is not None and pow(value % P, ORDER_P, P) == 1
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
        predecessor = base_predecessor(target, label, depth)
        best = INF
        for q in range(limit + 1):
            if q >= best:
                break
            residue = predecessor % X
            if is_full(residue):
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

    modulus_x2 = X * X
    full_power = pow(2, O, modulus_x2)
    full_step = ((full_power - 1) // X) % X

    candidates: list[tuple[int, int]] = []
    genuine = 0
    dead = 0
    for t in range(1, H + 1):
        rho = class_rep(t)
        for n in range(rho, CUTOFF + 1, D):
            if pow(n, ORDER_P, P) != 1:
                continue
            genuine += 1
            label = full_label(n, t, tables, coefficients)
            state = initial_predecessor_state(n, label)
            if distances[state] < 0:
                dead += 1
                continue
            candidates.append((n, label))

    assert genuine == 8727
    assert dead == 2903
    assert len(candidates) == EXPECTED_SURVIVORS

    items: list[tuple[int, int, int, int, int, int, int, int]] = []
    h3_sum = 0
    h3_max = 0

    for n, label in candidates:
        h3 = minimum_layer_sum(n, label, 3, LAYER_BUDGET)
        assert h3 <= LAYER_BUDGET
        h3_sum += h3
        h3_max = max(h3_max, h3)
        c3 = 3 * (label - 1) + O * h3

        numerator = (pow(2, label, modulus_x2) * n - 1) % modulus_x2
        assert numerator % X == 0
        predecessor = (numerator // X) % X
        delay = 0
        while not is_full(predecessor):
            predecessor = (predecessor + full_step) % X
            delay += 1
            assert delay <= LAYER_BUDGET

        source_label = label_of_output(predecessor)
        edge_cost = (
            source_label - 1
            + label - 1
            + 2 * O * delay
        )
        combined = 46 * c3 + 6 * edge_cost
        items.append((
            n,
            combined,
            label,
            h3,
            c3,
            edge_cost,
            delay,
            source_label,
        ))

    assert h3_max == EXPECTED_H3_MAX
    assert h3_sum == EXPECTED_H3_SUM

    combined_budget = 150 * BUDGET
    ordered = sorted(items, key=lambda item: item[0] * item[1])
    spent = 0
    full = 0
    boundary = None
    for item in ordered:
        if spent + item[1] <= combined_budget:
            spent += item[1]
            full += 1
        else:
            boundary = item
            break

    assert full == EXPECTED_FULL
    assert boundary == EXPECTED_BOUNDARY
    assert boundary is not None

    denominator = boundary[0] * boundary[1]
    reciprocal_bound = Fraction(combined_budget, denominator)
    positive = 0
    for item in items:
        n, cost = item[0], item[1]
        if n * cost < denominator:
            reciprocal_bound += Fraction(1, n) - Fraction(cost, denominator)
            positive += 1
    assert positive == EXPECTED_FULL
    assert reciprocal_bound < Fraction(85_239_095, 1_000_000_000)
    assert reciprocal_bound >= Fraction(85_239_094, 1_000_000_000)

    log2_lower, _ = log_bounds(Fraction(2, 1), 40)
    energy = Fraction(X * X, 1 << 133)
    _, eta_upper = log_bounds(energy, 4)
    required = X * (log2_lower - TARGET * eta_upper) / 2
    residual = required - reciprocal_bound
    assert residual > Fraction(14_695_112, 1_000_000_000)
    needed = (residual * CUTOFF).numerator // (
        residual * CUTOFF
    ).denominator + 1
    assert needed == 14696

    print("two-constraint inverse-window dual verified")
    print(f"survivors={len(candidates)}")
    print(f"h3 maximum={h3_max}, h3 sum={h3_sum}")
    print(f"combined boundary after {full} items")
    print(f"reciprocal bound approximately {float(reciprocal_bound):.15f}")
    print(f"required threshold approximately {float(required):.15f}")
    print(f"necessary values above one million>={needed}")


if __name__ == "__main__":
    verify()
