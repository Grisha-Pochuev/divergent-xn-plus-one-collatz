#!/usr/bin/env python3
"""Verify the giant zero-layer block theorem for the final two lengths."""
from __future__ import annotations

TARGETS = (
    177780727155637125193,
    177780727155637125195,
)
ORDER_X = 1860810887857924950
EXPECTED_LAYER_BUDGET = 6257
EXPECTED_BLOCK = 28413093679980362


def exact_total_valuation(p: int) -> int:
    assert p % 2 == 1
    return 133 * ((p - 1) // 2) + 67


def ceil_div(a: int, b: int) -> int:
    return (a + b - 1) // b


def verify() -> None:
    for p in TARGETS:
        total = exact_total_valuation(p)
        excess = total - p
        layer_budget = excess // ORDER_X
        assert layer_budget == EXPECTED_LAYER_BUDGET

        block = ceil_div(p - layer_budget, layer_budget)
        assert block == EXPECTED_BLOCK

        # The cyclic gap lower bound decreases with the number k of positive
        # layer positions, so k=layer_budget is the worst permitted case.
        for k in (1, 2, 3, 100, 1000, layer_budget):
            assert ceil_div(p - k, k) >= EXPECTED_BLOCK

    print("giant zero-layer block verified")
    print(f"positive-layer positions<={EXPECTED_LAYER_BUDGET}")
    print(f"consecutive zero-layer block>={EXPECTED_BLOCK}")


if __name__ == "__main__":
    verify()
