#!/usr/bin/env python3
"""Verify completeness of the 2154-class transition abstraction.

The mathematical proof is in docs/RESIDUE_TRANSITION_NO_GO.md.  This script
checks the fixed arithmetic data, constructs exact CRT witnesses for every
possible target class from representative source classes, and checks several
longer prescribed class words by direct accelerated iteration.
"""
from __future__ import annotations

from math import gcd

X = 104350542602662257699
M = 15099
H = 2154


def v2(n: int) -> int:
    assert n > 0
    return (n & -n).bit_length() - 1


def odd_step(n: int) -> tuple[int, int]:
    z = X * n + 1
    a = v2(z)
    return z >> a, a


def class_rep(a: int) -> int:
    """Odd lift modulo 2M of 2^(-a) modulo M."""
    residue = pow(pow(2, a, M), -1, M)
    return residue if residue & 1 else residue + M


def word_constants(pattern: tuple[int, ...]) -> tuple[int, int]:
    total = 0
    b = 0
    length = len(pattern)
    for j, a in enumerate(pattern):
        assert a >= 1
        b += X ** (length - 1 - j) * (1 << total)
        total += a
    return total, b


def coding_residue(pattern: tuple[int, ...]) -> tuple[int, int]:
    """Return the exact valuation-word residue and its power-of-two modulus."""
    total, b = word_constants(pattern)
    modulus = 1 << (total + 1)
    residue = (((1 << total) - b) * pow(X, -len(pattern), modulus)) % modulus
    assert residue & 1
    return residue, modulus


def impose_source_class(source: int, pattern: tuple[int, ...]) -> int:
    """Combine exact binary coding with one prescribed odd class modulo 2M."""
    residue, modulus = coding_residue(pattern)
    assert source & 1
    assert gcd(modulus, 2 * M) == 2
    assert (source - residue) % 2 == 0

    # n = residue + modulus*q.  Divide the congruence modulo 2M by 2.
    rhs = ((source - residue) // 2) % M
    coefficient = (modulus // 2) % M
    q = rhs * pow(coefficient, -1, M) % M
    n = residue + modulus * q

    assert n > 0 and n & 1
    assert n % (2 * M) == source % (2 * M)
    return n


def verify_word(source: int, pattern: tuple[int, ...]) -> None:
    n = impose_source_class(source, pattern)
    assert n % (2 * M) == source
    for expected_a in pattern:
        n, observed_a = odd_step(n)
        assert observed_a == expected_a
        assert n % (2 * M) == class_rep(expected_a)


def verify() -> None:
    assert M == 3 * 7 * 719
    assert X % M == 0
    assert pow(2, H, M) == 1
    for prime in (2, 3, 359):
        assert H % prime == 0
        assert pow(2, H // prime, M) != 1

    classes = [class_rep(a) for a in range(1, H + 1)]
    assert len(set(classes)) == H
    assert all(0 < r < 2 * M and r & 1 for r in classes)
    assert class_rep(H) == 1
    assert class_rep(904) == 25

    # Algebraically every source class is compatible with every exact binary
    # valuation residue because the only common modulus factor is 2 and both
    # residues are odd.  Directly instantiate every target class from three
    # structurally different source classes as a regression check.
    source_samples = (class_rep(H), class_rep(1), class_rep(904))
    for source in source_samples:
        for target_a in range(1, H + 1):
            verify_word(source, (target_a,))

    # Finite-word witnesses, including repeated classes, loops, and the class
    # 1 represented by exponent H.
    samples = (
        (class_rep(904), (1, 2, 3, 4, 5)),
        (class_rep(1), (H, H, H)),
        (class_rep(H), (904, 1, H, 359, 718)),
        (class_rep(777), (2153, 2, 2153, 2)),
    )
    for source, pattern in samples:
        verify_word(source, pattern)

    print("residue-transition no-go theorem verified")
    print(f"X={X}")
    print(f"M={M}, order={H}, classes={len(classes)}")
    print("all 2154 target classes realized from each of 3 source classes")
    print("sample finite class words realized exactly")


if __name__ == "__main__":
    verify()
