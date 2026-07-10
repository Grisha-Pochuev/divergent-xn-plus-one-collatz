#!/usr/bin/env python3
"""Verify the massive repeated full-transition class theorem exactly."""
from __future__ import annotations

X = 104350542602662257699
O = 1860810887857924950
TARGETS = (
    177780727155637125193,
    177780727155637125195,
)
K = 197
PAIR_COUNT = 19503
EXPECTED_COMMON_LOW = 59561055798335280522
EXPECTED_REPEAT = 3053943280435589
EXPECTED_DIAMETER = (
    66508995066170702555770104858896894988802023536957800776
)


def odd_transition_class(u: int, v: int) -> int:
    """Odd target class modulo 2*X^2 for a zero-layer u->v edge."""
    modulus = X * X
    source_residue = pow(2, -u, X)
    target_residue = (
        pow(2, -v, modulus) * (1 + X * source_residue)
    ) % modulus
    return target_residue if target_residue & 1 else target_residue + modulus


def verify() -> None:
    assert X % 2 == 1
    assert pow(2, O, X) == 1
    assert K < 2 * O
    assert PAIR_COUNT == K * (K + 1) // 2

    minimum_low = None
    for p in TARGETS:
        assert p & 1
        A = (133 * p + 1) // 2
        total_edge_cost = 2 * (A - p)
        expensive_cap = total_edge_cost // K
        cheap_edges = p - expensive_cap
        repeated = (cheap_edges + PAIR_COUNT - 1) // PAIR_COUNT

        assert cheap_edges >= EXPECTED_COMMON_LOW
        assert repeated >= EXPECTED_REPEAT
        minimum_low = cheap_edges if minimum_low is None else min(minimum_low, cheap_edges)

    assert minimum_low == EXPECTED_COMMON_LOW

    # Distinct cheap ordered pairs give distinct odd target classes modulo 2*X^2.
    classes: dict[int, tuple[int, int]] = {}
    for u in range(1, K + 1):
        for v in range(1, K + 2 - u):
            assert u + v <= K + 1
            residue = odd_transition_class(u, v)
            assert 0 < residue < 2 * X * X
            assert residue & 1
            assert residue not in classes
            classes[residue] = (u, v)

            # The least representative really gives an exact zero-layer edge.
            source = ((1 << v) * residue - 1) // X
            assert X * source + 1 == (1 << v) * residue
            assert source > 0 and source & 1
            assert source % X == pow(2, -u, X)

    assert len(classes) == PAIR_COUNT

    diameter = 2 * X * X * (EXPECTED_REPEAT - 1)
    assert diameter == EXPECTED_DIAMETER

    print("massive repeated transition class verified")
    print(f"targets={TARGETS}")
    print(f"cheap-edge threshold K={K}")
    print(f"cheap ordered pairs={PAIR_COUNT}")
    print(f"common cheap-edge lower bound={EXPECTED_COMMON_LOW}")
    print(f"forced repetitions in one class={EXPECTED_REPEAT}")
    print(f"forced cycle diameter>={diameter}")


if __name__ == "__main__":
    verify()
