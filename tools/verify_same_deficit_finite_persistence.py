#!/usr/bin/env python3
from __future__ import annotations

from math import gcd


def v2(n: int) -> int:
    if n <= 0:
        raise ValueError("v2 requires n>0")
    return (n & -n).bit_length() - 1


def word_constant(X: int, word: list[int]) -> tuple[int, int]:
    A = 0
    Q = 0
    for a in word:
        Q = X * Q + (1 << A)
        A += a
    return A, Q


def source_residue(X: int, word: list[int]) -> tuple[int, int]:
    A, Q = word_constant(X, word)
    modulus = 1 << (A + 1)
    residue = ((1 << A) - Q) * pow(X, -len(word), modulus) % modulus
    assert residue & 1
    return residue, modulus


def step(X: int, n: int) -> tuple[int, int]:
    z = X * n + 1
    a = v2(z)
    return z >> a, a


def block_word(m: int, e: int, ell: int) -> list[int]:
    assert 1 <= e <= m - 1
    assert ell >= 1
    return [m] * (ell - 1) + [m - e]


def geometric_factor(B: int, X: int, d: int, ell: int) -> int:
    numerator = pow(B, ell) - pow(X, ell)
    assert numerator % d == 0
    return numerator // d


def construct_instance(
    m: int,
    d: int,
    e: int,
    lengths: list[int],
    lift: int = 1,
) -> tuple[int, list[int], list[int], list[int]]:
    B = 1 << m
    X = B - d
    assert X >= 5 and X & 1 and d & 1 and gcd(X, d) == 1

    # One prepended block produces the first retained same-type boundary.
    all_lengths = [1] + lengths
    word: list[int] = []
    boundary_step_indices: list[int] = []
    total = 0
    for ell in all_lengths:
        word.extend(block_word(m, e, ell))
        total += ell
        boundary_step_indices.append(total)

    residue, modulus = source_residue(X, word)
    source = residue + lift * modulus
    assert source > 0 and source & 1

    n = source
    actual_word: list[int] = []
    boundaries: list[int] = []
    for j in range(1, len(word) + 1):
        n, a = step(X, n)
        actual_word.append(a)
        if j in boundary_step_indices:
            boundaries.append(n)

    assert actual_word == word
    assert len(boundaries) == len(all_lengths)
    target = pow(2, e, X)
    for x in boundaries:
        assert x > 0 and x & 1
        assert (d * x - target) % X == 0

    # The retained segment is boundaries[0] -> ... -> boundaries[-1].
    assert len(boundaries) == len(lengths) + 1
    return source, boundaries, actual_word, all_lengths


def verify_primary_depth_ladder(e: int, lengths: list[int]) -> None:
    m = 4501
    B = 1 << m
    N = (1 << 500) - 1
    d = 349 * (1 << 500) - 347
    X = B - d
    assert X % N == 0
    assert d % N == 2

    source, boundaries, _, all_lengths = construct_instance(m, d, e, lengths)
    block_sources = [source] + boundaries[:-1]

    target_mod_N = pow(2, e - 1, N)
    for endpoint in boundaries:
        assert endpoint % N == target_mod_N

    for block_source, endpoint, ell in zip(block_sources, boundaries, all_lengths):
        S = geometric_factor(B, X, d, ell)
        A = m * ell - e
        # When s<=ell, X^ell vanishes modulo N^s, so the endpoint is fixed
        # independently of the block source.
        for s in range(1, ell + 1):
            modulus = pow(N, s)
            predicted = S * pow(pow(2, A, modulus), -1, modulus) % modulus
            assert endpoint % modulus == predicted
        # Also verify the complete-block affine identity exactly.
        assert (1 << A) * endpoint == pow(X, ell) * block_source + S


def main() -> None:
    tested = 0
    for m in range(3, 9):
        B = 1 << m
        for d in range(3, B // 2, 2):
            X = B - d
            if X < 5:
                continue
            for e in range(1, m):
                for lengths in ([1], [2], [1, 2], [3, 1, 2], [2, 4, 1, 3]):
                    construct_instance(m, d, e, list(lengths), lift=1)
                    tested += 1

    # Explicit 5n+1 regression: B=8, d=3, e=2 means terminal valuation 1.
    source, boundaries, word, _ = construct_instance(3, 3, 2, [2, 4, 3, 1], lift=2)
    assert source == 47150705
    assert word == [1, 3, 1, 3, 3, 3, 1, 3, 3, 1, 1]
    assert boundaries == [117876763, 184182443, 112416043, 109781293, 274453233]

    for e, lengths in [
        (1, [1, 2, 1]),
        (500, [2, 1, 3]),
        (1093, [1, 1, 2]),
        (4500, [3, 2, 1]),
    ]:
        verify_primary_depth_ladder(e, lengths)

    print(
        f"PASS: {tested} small same-deficit constructions, "
        "the explicit 5n+1 regression, and 4 primary depth-ladder regressions"
    )


if __name__ == "__main__":
    main()
