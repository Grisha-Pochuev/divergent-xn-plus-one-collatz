#!/usr/bin/env python3
"""Verify the exact full-label occupancy decomposition."""
from __future__ import annotations

from math import gcd

X = 104350542602662257699
O = 1860810887857924950
TARGETS = (
    177780727155637125193,
    177780727155637125195,
)
EXPECTED_LAYER_BUDGET = 6257


def exact_total_valuation(p: int) -> int:
    assert p % 2 == 1
    return 133 * ((p - 1) // 2) + 67


def full_label(a: int, order: int) -> tuple[int, int]:
    """Return unique (s,q) with a=s+order*q and 1<=s<=order."""
    assert a >= 1 and order >= 1
    residue = a % order
    if residue == 0:
        return order, a // order - 1
    return residue, a // order


def verify_known_5n1_cycle() -> None:
    x = 5
    order = 4
    cycle = (13, 33, 83)
    valuations = (1, 1, 5)

    labels: list[int] = []
    layers: list[int] = []
    for index, (n, a) in enumerate(zip(cycle, valuations)):
        target = cycle[(index + 1) % len(cycle)]
        assert x * n + 1 == (1 << a) * target
        s, q = full_label(a, order)
        assert pow(2, s, x) * (target % x) % x == 1
        labels.append(s)
        layers.append(q)

    assert sum(valuations) == sum(labels) + order * sum(layers)
    assert labels == [1, 1, 1]
    assert layers == [0, 0, 1]


def verify() -> None:
    assert gcd(2, X) == 1
    assert pow(2, O, X) == 1
    for prime in (2, 3, 5, 359, 2677, 15137, 852763):
        assert O % prime == 0
        assert pow(2, O // prime, X) != 1

    for p in TARGETS:
        total = exact_total_valuation(p)
        excess = total - p
        assert excess > 0
        assert excess // O == EXPECTED_LAYER_BUDGET
        assert (EXPECTED_LAYER_BUDGET + 1) * O > excess

        # Formula (6): an occurrence with label >=K+1 spends at least K
        # units above the universal baseline label 1.
        for k in (1, 2, 66, 1000, 10**6, O - 1):
            cap = excess // k
            assert cap * k <= excess
            assert (cap + 1) * k > excess

    verify_known_5n1_cycle()

    print("full-label occupancy budget verified")
    print(f"ord_X(2)={O}")
    for p in TARGETS:
        total = exact_total_valuation(p)
        print(f"target={p}, A={total}, floor((A-p)/O)={((total-p)//O)}")
    print("known 5n+1 cycle regression passed")


if __name__ == "__main__":
    verify()
