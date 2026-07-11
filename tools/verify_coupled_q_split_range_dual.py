#!/usr/bin/env python3
"""Verify the coupled-Q split-range reciprocal dual exactly."""
from __future__ import annotations

from fractions import Fraction
import sys
from typing import Any, Callable

import verify_integral_layer_budget_dual as small_certificate
import verify_signed_label_split_range_dual as middle_certificate

O = small_certificate.O
BUDGET = small_certificate.BUDGET
LAYER_BUDGET = small_certificate.LAYER_BUDGET
X = small_certificate.X
P2 = 177780727155637125195
P1 = 177780727155637125193
CUTOFF = 60_000_000

EXPECTED_MAX_Q = 5841
EXPECTED_MIDDLE_RIGHT_POSITIVE = 1219
UNIFORM_UPPER = Fraction(86_152_495, 1_000_000_000)
EXPECTED_TAILS = {
    P1: (25_237_969, 25_231_712),
    P2: (826_903, 820_646),
}


def capture_return_locals(
    function: Callable[[], None],
    names: tuple[str, ...],
) -> dict[str, Any]:
    """Run an exact component verifier and capture named final local values.

    The component verifiers deliberately keep their large generated item lists
    local.  Tracing only at the return event lets this integration certificate
    reuse those already-verified exact lists without duplicating hundreds of
    lines of modular-generation code.
    """
    captured: dict[str, Any] = {}
    code = function.__code__

    def tracer(frame: Any, event: str, arg: Any) -> Any:
        if event == "return" and frame.f_code is code:
            for name in names:
                assert name in frame.f_locals
                captured[name] = frame.f_locals[name]
        return tracer

    previous = sys.gettrace()
    sys.settrace(tracer)
    try:
        function()
    finally:
        sys.settrace(previous)

    assert set(captured) == set(names)
    return captured


def two_resource_middle_dual(
    items: list[tuple[int, int, int, int, int]],
) -> tuple[Fraction, Fraction, int]:
    """Return (objective at Q=6153, Q-slope, positive reduced terms)."""
    by_n = {item[0]: item for item in items}
    assert len(by_n) == len(items)

    first_n = 1_250_453
    second_n = 1_454_471
    first = by_n[first_n]
    second = by_n[second_n]

    first_label = first[2] - 1
    second_label = second[2] - 1
    first_cost = first[1]
    second_cost = second[1]

    determinant = (
        first_label * second_cost
        - second_label * first_cost
    )
    assert determinant != 0

    alpha = (
        Fraction(1, first_n) * second_cost
        - Fraction(1, second_n) * first_cost
    ) / determinant
    gamma = (
        first_label * Fraction(1, second_n)
        - second_label * Fraction(1, first_n)
    ) / determinant
    assert alpha > 0 and gamma > 0

    correction = Fraction(0, 1)
    positive = 0
    for n, potential_cost, target_label, _delay, _source_label in items:
        reduced = (
            Fraction(1, n)
            - alpha * (target_label - 1)
            - gamma * potential_cost
        )
        if reduced > 0:
            correction += reduced
            positive += 1

    q_value = 6153
    objective = (
        alpha * (BUDGET - O * q_value)
        + gamma * (2 * BUDGET)
        + correction
    )
    slope = -alpha * O

    assert slope < 0
    assert positive == EXPECTED_MIDDLE_RIGHT_POSITIVE
    assert objective < Fraction(595_183, 1_000_000_000)
    return objective, slope, positive


def verify() -> None:
    small = capture_return_locals(
        small_certificate.verify,
        (
            "left_objective",
            "left_slope",
            "right_objective",
            "right_slope",
        ),
    )
    middle = capture_return_locals(
        middle_certificate.verify,
        ("middle_bound", "middle_items"),
    )

    left_objective: Fraction = small["left_objective"]
    left_slope: Fraction = small["left_slope"]
    right_objective: Fraction = small["right_objective"]
    right_slope: Fraction = small["right_slope"]
    middle_constant: Fraction = middle["middle_bound"]
    middle_items = middle["middle_items"]

    assert left_slope > 0
    assert right_slope < 0
    assert middle_constant < Fraction(1_185_304, 1_000_000_000)

    middle_right, middle_right_slope, _ = two_resource_middle_dual(
        middle_items
    )

    rows: list[tuple[Fraction, int]] = []
    for q_value in range(LAYER_BUDGET + 1):
        if q_value <= 6152:
            small_upper = (
                left_objective
                + left_slope * (q_value - 6152)
            )
        else:
            small_upper = (
                right_objective
                + right_slope * (q_value - 6153)
            )

        decreasing_middle = (
            middle_right
            + middle_right_slope * (q_value - 6153)
        )
        middle_upper = min(middle_constant, decreasing_middle)
        rows.append((small_upper + middle_upper, q_value))

    maximum, maximizing_q = max(rows)
    assert maximizing_q == EXPECTED_MAX_Q
    assert maximum < UNIFORM_UPPER

    # The two middle certificates cross between these adjacent integers.
    at_5841 = middle_right + middle_right_slope * (5841 - 6153)
    at_5842 = middle_right + middle_right_slope * (5842 - 6153)
    assert middle_constant <= at_5841
    assert at_5842 < middle_constant

    log2_lower, _ = middle_certificate.log_bounds(Fraction(2, 1), 40)
    energy = Fraction(X * X, 1 << 133)
    _, eta_upper = middle_certificate.log_bounds(energy, 4)

    for target, (expected_large, expected_zero) in EXPECTED_TAILS.items():
        required = X * (log2_lower - target * eta_upper) / 2
        residual = required - UNIFORM_UPPER
        assert residual > 0
        scaled = residual * CUTOFF
        minimum_large = scaled.numerator // scaled.denominator + 1
        minimum_zero = minimum_large - LAYER_BUDGET
        assert minimum_large == expected_large
        assert minimum_zero == expected_zero

    print("coupled-Q split-range reciprocal dual verified")
    print(f"global maximizing Q={maximizing_q}")
    print(f"exact maximum approximately {float(maximum):.15f}")
    print(f"uniform upper={float(UNIFORM_UPPER):.15f}")
    for target, values in EXPECTED_TAILS.items():
        print(
            f"target={target}: values above sixty million>={values[0]}, "
            f"zero-layer>={values[1]}"
        )


if __name__ == "__main__":
    verify()
