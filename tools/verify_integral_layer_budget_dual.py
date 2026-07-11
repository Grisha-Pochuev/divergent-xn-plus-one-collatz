#!/usr/bin/env python3
"""Verify the integral full-layer budget reciprocal dual exactly."""
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

LEFT_Q = 6152
RIGHT_Q = 6153
LEFT_BOUNDARY_N = (821125, 92383, 14771)
RIGHT_BOUNDARY_N = (108397, 14771, 21779)
EXPECTED_LEFT_POSITIVE = 205
EXPECTED_RIGHT_POSITIVE = 203

SMALL_UPPER = Fraction(85_226_583, 1_000_000_000)
MIDDLE_UPPER = Fraction(1_185_304, 1_000_000_000)
COMBINED_UPPER = Fraction(86_411_887, 1_000_000_000)


def solve_three(
    rows: tuple[tuple[int, int, int], ...],
    values: tuple[Fraction, ...],
) -> tuple[Fraction, Fraction, Fraction]:
    matrix = [
        [Fraction(value) for value in row] + [rhs]
        for row, rhs in zip(rows, values)
    ]
    for column in range(3):
        pivot = next(
            index for index in range(column, 3)
            if matrix[index][column] != 0
        )
        matrix[column], matrix[pivot] = matrix[pivot], matrix[column]
        scale = matrix[column][column]
        matrix[column] = [entry / scale for entry in matrix[column]]
        for index in range(3):
            if index == column:
                continue
            scale = matrix[index][column]
            if scale:
                matrix[index] = [
                    matrix[index][j] - scale * matrix[column][j]
                    for j in range(4)
                ]
    return tuple(matrix[index][3] for index in range(3))  # type: ignore[return-value]


def exact_dual(
    items: list[tuple[int, int, int, int]],
    by_n: dict[int, tuple[int, int, int, int]],
    boundary_n: tuple[int, int, int],
    q_value: int,
) -> tuple[Fraction, Fraction, Fraction, Fraction, Fraction, int]:
    boundary = tuple(by_n[n] for n in boundary_n)
    rows = tuple((label_cost, h3, flow_cost) for _n, label_cost, h3, flow_cost in boundary)
    values = tuple(Fraction(1, n) for n in boundary_n)
    alpha, beta, gamma = solve_three(rows, values)
    assert alpha >= 0 and beta >= 0 and gamma >= 0

    correction = Fraction(0, 1)
    positive = 0
    for n, label_cost, h3, flow_cost in items:
        reduced = (
            Fraction(1, n)
            - alpha * label_cost
            - beta * h3
            - gamma * flow_cost
        )
        if reduced > 0:
            correction += reduced
            positive += 1

    slope = -alpha * O + 3 * beta
    objective = (
        alpha * (BUDGET - O * q_value)
        + beta * (3 * q_value)
        + gamma * (2 * BUDGET)
        + correction
    )
    return alpha, beta, gamma, slope, objective, positive


def verify() -> None:
    verify_group_data()
    assert BUDGET == (133 * TARGET + 1) // 2 - TARGET
    assert BUDGET // O == LAYER_BUDGET

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
        small = small_labels.get(value % M)
        assert small is not None and pow(value % P, ORDER_P, P) == 1
        return full_label(value % X, small, tables, coefficients)

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

    items: list[tuple[int, int, int, int]] = []
    target_labels: set[int] = set()
    source_labels: set[int] = set()
    genuine = 0
    dead = 0
    h3_sum = 0
    h3_max = 0

    for small_label in range(1, H + 1):
        rho = class_rep(small_label)
        for n in range(rho, CUTOFF + 1, D):
            if pow(n % P, ORDER_P, P) != 1:
                continue
            genuine += 1
            target_label = full_label(
                n, small_label, tables, coefficients
            )
            state = initial_predecessor_state(n, target_label)
            if distances[state] < 0:
                dead += 1
                continue

            h3 = minimum_layer_sum(
                n, target_label, 3, LAYER_BUDGET
            )
            assert h3 <= LAYER_BUDGET
            h3_sum += h3
            h3_max = max(h3_max, h3)

            numerator = (
                pow(2, target_label, modulus_x2) * n - 1
            ) % modulus_x2
            assert numerator % X == 0
            predecessor = (numerator // X) % X
            delay = 0
            while not is_full(predecessor):
                predecessor = (predecessor + full_step) % X
                delay += 1
                assert delay <= LAYER_BUDGET

            source_label = label_of_output(predecessor)
            assert target_label not in target_labels
            assert source_label not in source_labels
            target_labels.add(target_label)
            source_labels.add(source_label)

            flow_cost = (
                2 * (source_label + target_label - 2)
                + 2 * O * delay
            )
            items.append((n, target_label - 1, h3, flow_cost))

    assert genuine == 8727
    assert dead == 2903
    assert len(items) == EXPECTED_SURVIVORS
    assert len(target_labels) == len(items)
    assert len(source_labels) == len(items)
    assert target_labels.isdisjoint(source_labels)
    assert h3_max == EXPECTED_H3_MAX
    assert h3_sum == EXPECTED_H3_SUM

    by_n = {item[0]: item for item in items}
    assert len(by_n) == len(items)

    left = exact_dual(items, by_n, LEFT_BOUNDARY_N, LEFT_Q)
    right = exact_dual(items, by_n, RIGHT_BOUNDARY_N, RIGHT_Q)

    left_slope, left_objective, left_positive = left[3], left[4], left[5]
    right_slope, right_objective, right_positive = right[3], right[4], right[5]

    # The left dual increases with Q and therefore covers 0..6152.
    assert left_slope > 0
    assert left_positive == EXPECTED_LEFT_POSITIVE
    # The right dual decreases with Q and therefore covers 6153..6257.
    assert right_slope < 0
    assert right_positive == EXPECTED_RIGHT_POSITIVE

    assert left_objective < SMALL_UPPER
    assert right_objective < SMALL_UPPER
    assert right_objective > left_objective

    assert SMALL_UPPER + MIDDLE_UPPER == COMBINED_UPPER

    log2_lower, _ = log_bounds(Fraction(2, 1), 40)
    energy = Fraction(X * X, 1 << 133)
    _, eta_upper = log_bounds(energy, 4)
    required = X * (log2_lower - TARGET * eta_upper) / 2
    residual = required - COMBINED_UPPER
    assert residual > Fraction(13_522_319, 1_000_000_000)

    minimum_large = (residual * 60_000_000).numerator // (
        residual * 60_000_000
    ).denominator + 1
    assert minimum_large == 811_340
    minimum_zero = minimum_large - LAYER_BUDGET
    assert minimum_zero == 805_083

    print("integral full-layer budget dual verified")
    print(f"items={len(items)}")
    print(f"left objective approximately {float(left_objective):.15f}")
    print(f"right objective approximately {float(right_objective):.15f}")
    print(f"small-range upper={float(SMALL_UPPER):.15f}")
    print(f"combined upper={float(COMBINED_UPPER):.15f}")
    print(f"mandatory values above sixty million>={minimum_large}")
    print(f"mandatory zero-layer values above sixty million>={minimum_zero}")


if __name__ == "__main__":
    verify()
