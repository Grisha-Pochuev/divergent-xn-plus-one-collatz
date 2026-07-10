#!/usr/bin/env python3
"""Verify the fixed arithmetic behind the global residue valuation budget."""
from __future__ import annotations

X = 104350542602662257699
M = 15099
H = 2154


def v2(n: int) -> int:
    assert n > 0
    return (n & -n).bit_length() - 1


def canonical_index(a: int) -> int:
    assert a >= 1
    return ((a - 1) % H) + 1


def class_rep(index: int) -> int:
    assert 1 <= index <= H
    residue = pow(pow(2, index, M), -1, M)
    return residue if residue & 1 else residue + M


def verify() -> None:
    assert M == 3 * 7 * 719
    assert X % M == 0
    assert pow(2, H, M) == 1
    for prime in (2, 3, 359):
        assert pow(2, H // prime, M) != 1

    assert X + 1 < (1 << 67)

    reps = [class_rep(t) for t in range(1, H + 1)]
    assert len(set(reps)) == H

    # The class of every output is the canonical residue of the exact
    # valuation, and the exact valuation is never smaller than its index.
    for a in range(1, 3 * H + 1):
        t = canonical_index(a)
        assert a >= t
        assert class_rep(t) % M == pow(pow(2, a, M), -1, M)
        assert (a - t) % H == 0

    # Direct arithmetic regression over a short exact prefix.  This is not
    # trajectory evidence for divergence; it only checks the class identity.
    n = 1
    for _ in range(10000):
        z = X * n + 1
        a = v2(z)
        n = z >> a
        t = canonical_index(a)
        assert n % (2 * M) == class_rep(t)
        assert a >= t

    # Frequency corollary checks for representative lengths.
    for p in (1, 2, 10, 10**6, 170000000000000000000):
        budget = 67 * p - 1
        for threshold in (1, 2, 68, 134, H):
            cap = budget // threshold
            assert threshold * cap <= budget
            assert threshold * (cap + 1) > budget

    print("residue valuation budget arithmetic verified")
    print(f"X={X}")
    print(f"M={M}, order={H}, classes={len(reps)}")
    print("X+1 < 2^67")
    print("class index is never larger than the exact valuation")


if __name__ == "__main__":
    verify()
