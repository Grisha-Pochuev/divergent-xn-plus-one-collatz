#!/usr/bin/env python3
"""Verify arithmetic identities used by the transition-balanced reduction."""
from __future__ import annotations

from collections import Counter

X = 104350542602662257699
M = 15099
H = 2154
MIN_CYCLE_VALUE = 25


def v2(n: int) -> int:
    assert n > 0
    return (n & -n).bit_length() - 1


def canonical_index(a: int, order: int = H) -> int:
    assert a >= 1
    return ((a - 1) % order) + 1


def class_rep(t: int) -> int:
    residue = pow(pow(2, t, M), -1, M)
    rep = residue if residue & 1 else residue + M
    if rep == 1:
        rep += 2 * M
    return rep


def class_index(n: int) -> int:
    residue = n % M
    for t in range(1, H + 1):
        if pow(pow(2, t, M), -1, M) == residue:
            return t
    raise AssertionError("not an allowed output class")


def binary_rep(t: int) -> int:
    modulus = 1 << t
    residue = (-pow(X, -1, modulus)) % modulus
    if residue == 0:
        residue = modulus
    if residue < MIN_CYCLE_VALUE:
        residue += ((MIN_CYCLE_VALUE - residue + modulus - 1) // modulus) * modulus
    assert residue >= MIN_CYCLE_VALUE
    assert (X * residue + 1) % modulus == 0
    return residue


def odd_step(x: int, n: int) -> tuple[int, int]:
    z = x * n + 1
    a = v2(z)
    return z >> a, a


def verify_known_cycle(x: int, modulus: int, order: int, cycle: tuple[int, ...]) -> None:
    source_counts: Counter[int] = Counter()
    target_counts: Counter[int] = Counter()
    for i, n in enumerate(cycle):
        nxt, a = odd_step(x, n)
        assert nxt == cycle[(i + 1) % len(cycle)]

        source_residue = n % modulus
        source_t = None
        for t in range(1, order + 1):
            if pow(pow(2, t, modulus), -1, modulus) == source_residue:
                source_t = t
                break
        assert source_t is not None
        target_t = canonical_index(a, order)
        source_counts[source_t] += 1
        target_counts[target_t] += 1

        assert nxt % modulus == pow(pow(2, target_t, modulus), -1, modulus)
        assert (x * n + 1) % (1 << target_t) == 0

    assert source_counts == target_counts


def verify() -> None:
    assert M == 3 * 7 * 719
    assert X % M == 0
    assert pow(2, H, M) == 1
    assert X + 1 < (1 << 67)

    raw_residue_to_index: dict[int, int] = {}
    for t in range(1, H + 1):
        raw = pow(pow(2, t, M), -1, M)
        assert raw not in raw_residue_to_index
        raw_residue_to_index[raw] = t

        rho = class_rep(t)
        assert rho >= MIN_CYCLE_VALUE
        assert rho % M == raw

        eta = binary_rep(t)
        assert eta >= MIN_CYCLE_VALUE
        assert (X * eta + 1) % (1 << t) == 0

    # Directly check sigma(C_X(n))=theta(n) on a finite prefix.  This checks
    # the modular identity only and is not evidence of divergence.
    n = 1
    for _ in range(10000):
        nxt, a = odd_step(X, n)
        target_t = canonical_index(a)
        assert raw_residue_to_index[nxt % M] == target_t
        assert (X * n + 1) % (1 << target_t) == 0
        n = nxt

    # Regression on two genuine accelerated 5n+1 cycles.  The second cycle
    # uses more than one class and checks nontrivial flow balance.
    verify_known_cycle(5, 5, 4, (13, 33, 83))
    verify_known_cycle(5, 5, 4, (17, 43, 27))

    print("transition-balance reduction arithmetic verified")
    print(f"X={X}")
    print(f"M={M}, order={H}")
    print("source/target class identity checked on 10000 exact steps")
    print("flow balance checked on two known 5n+1 cycles")


if __name__ == "__main__":
    verify()
