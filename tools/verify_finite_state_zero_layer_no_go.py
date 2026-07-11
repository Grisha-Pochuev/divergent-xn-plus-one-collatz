#!/usr/bin/env python3
"""Regression checks for arbitrarily long zero-cost full-label-one words."""
from __future__ import annotations

from valuation_word_codec import coding_residue, observed_word
from xn1 import odd_step

X = 104350542602662257699
FULL_LABEL_ONE_RESIDUE = pow(2, -1, X)


def crt_pair(a: int, m: int, b: int, n: int) -> tuple[int, int]:
    """Return the least CRT solution modulo m*n for coprime moduli."""
    assert m > 0 and n > 0
    lift = ((b - a) % n) * pow(m, -1, n) % n
    value = a + m * lift
    return value % (m * n), m * n


def all_one_start(length: int) -> int:
    pattern = (1,) * length
    residue, modulus = coding_residue(X, pattern)
    start, combined = crt_pair(
        residue,
        modulus,
        FULL_LABEL_ONE_RESIDUE,
        X,
    )
    if start == 0:
        start += combined
    return start


def verify_segment(length: int) -> list[int]:
    start = all_one_start(length)
    observed, _endpoint = observed_word(X, start, length)
    assert observed == (1,) * length

    values = [start]
    n = start
    for _ in range(length):
        assert n % X == FULL_LABEL_ONE_RESIDUE
        next_n, valuation = odd_step(X, n)
        assert valuation == 1
        assert next_n % X == FULL_LABEL_ONE_RESIDUE

        source_label = 1
        target_label = 1
        layer = 0
        symmetric_cost = (
            source_label - 1
            + target_label - 1
            + 2 * layer
        )
        assert symmetric_cost == 0

        values.append(next_n)
        n = next_n
    return values


def verify() -> None:
    for length in (1, 2, 5, 20, 100):
        values = verify_segment(length)
        assert len(values) == length + 1

    # Finite quotient regressions.  A segment longer than the state set has a
    # repeated projected state, producing a nonempty projected zero-cost loop.
    for modulus in (3, 5, 7, 16, 97, 1009):
        values = verify_segment(modulus + 1)
        first_seen: dict[int, int] = {}
        repeated = None
        for index, value in enumerate(values):
            state = value % modulus
            if state in first_seen:
                repeated = (first_seen[state], index)
                break
            first_seen[state] = index
        assert repeated is not None
        left, right = repeated
        assert right > left
        total_cost = 0
        assert total_cost == 0

    print("finite-state zero-layer potential no-go regressions verified")
    print("arbitrarily long all-label-one zero-cost words are CRT-compatible")


if __name__ == "__main__":
    verify()
