#!/usr/bin/env python3
"""Verify complete-block gcd compression and its local no-go theorem."""
from __future__ import annotations

from itertools import product
from math import gcd
from typing import Sequence


def v2(value: int) -> int:
    if value <= 0:
        raise ValueError("v2 expects a positive integer")
    return (value & -value).bit_length() - 1


def odd_step(X: int, n: int) -> tuple[int, int]:
    value = X * n + 1
    a = v2(value)
    return value >> a, a


def word_constant(X: int, word: Sequence[int]) -> int:
    p = len(word)
    prefix = 0
    total = 0
    for j, a in enumerate(word):
        total += pow(X, p - 1 - j) << prefix
        prefix += a
    return total


def exact_start_residue(X: int, word: Sequence[int]) -> tuple[int, int]:
    A = sum(word)
    modulus = 1 << (A + 1)
    q = word_constant(X, word)
    residue = ((1 << A) - q) * pow(pow(X, len(word), modulus), -1, modulus)
    return residue % modulus, modulus


def follow_word(X: int, n: int, word: Sequence[int]) -> int:
    current = n
    valuations: list[int] = []
    for _ in word:
        current, a = odd_step(X, current)
        valuations.append(a)
    if tuple(valuations) != tuple(word):
        raise AssertionError((X, n, word, tuple(valuations)))
    return current


def crt_with_zero(residue: int, power_two_modulus: int, odd_modulus: int) -> int:
    if odd_modulus <= 0 or odd_modulus % 2 == 0:
        raise ValueError("odd_modulus must be positive and odd")
    t = (-residue * pow(power_two_modulus, -1, odd_modulus)) % odd_modulus
    answer = residue + power_two_modulus * t
    if answer <= 0:
        answer += power_two_modulus * odd_modulus
    return answer


def verify_exact_blocks() -> tuple[int, int]:
    exact_cases = 0
    full_factor_cases = 0

    for m in range(3, 9):
        B = 1 << m
        for d in range(3, B // 2, 2):
            X = B - d
            if X < 5:
                continue
            for ell in range(1, 5):
                terminals = list(range(1, m)) + list(range(m + 1, m + 4))
                for terminal in terminals:
                    word = (m,) * (ell - 1) + (terminal,)
                    A = sum(word)
                    S = (pow(B, ell) - pow(X, ell)) // d

                    assert S % 2 == 1
                    assert word_constant(X, word) == S
                    if ell >= 2:
                        assert S > pow(X, ell - 1)

                    residue, modulus = exact_start_residue(X, word)
                    assert residue % 2 == 1

                    for lift in range(3):
                        n = residue + lift * modulus
                        if n <= 0:
                            n += modulus
                        endpoint = follow_word(X, n, word)
                        assert (1 << A) * endpoint == pow(X, ell) * n + S
                        assert gcd(n, endpoint) == gcd(n, S)
                        exact_cases += 1

                    if S > 1:
                        n = crt_with_zero(residue, modulus, S)
                        endpoint = follow_word(X, n, word)
                        assert n % S == 0
                        assert endpoint % S == 0
                        assert gcd(n, endpoint) == S
                        full_factor_cases += 1

    return exact_cases, full_factor_cases


def verify_cyclic_compression() -> tuple[int, int]:
    checked = 0
    closing = 0

    for X in (5, 7, 9, 11, 13, 15):
        m = X.bit_length()
        B = 1 << m
        d = B - X
        for ell in range(1, 4):
            terminals = list(range(1, m)) + [m + 1, m + 2]
            for terminal in terminals:
                W = (m,) * (ell - 1) + (terminal,)
                A_W = sum(W)
                S = (pow(B, ell) - pow(X, ell)) // d
                for tail_length in range(1, 4):
                    for V in product(range(1, 5), repeat=tail_length):
                        U = W + V
                        p = len(U)
                        Delta = (1 << sum(U)) - pow(X, p)
                        Q_i = word_constant(X, U)
                        Q_j = word_constant(X, V + W)

                        assert (1 << A_W) * Q_j == pow(X, ell) * Q_i + Delta * S
                        assert gcd(Q_i, Q_j) == gcd(Q_i, abs(Delta * S))

                        if Delta > 0 and Q_i % Delta == 0:
                            n_i = Q_i // Delta
                            n_j = Q_j // Delta
                            assert gcd(Q_i, Q_j) == Delta * gcd(n_i, S)
                            assert (1 << A_W) * n_j == pow(X, ell) * n_i + S
                            closing += 1
                        checked += 1

    return checked, closing


def verify_regression() -> None:
    X = 5
    B = 8
    d = 3
    word = (3, 1)
    ell = 2
    S = (pow(B, ell) - pow(X, ell)) // d
    residue, modulus = exact_start_residue(X, word)
    n = crt_with_zero(residue, modulus, S)
    endpoint = follow_word(X, n, word)

    assert S == 13
    assert residue == 27
    assert modulus == 32
    assert n == 91
    assert endpoint == 143
    assert gcd(n, endpoint) == 13

    middle, first_a = odd_step(X, n)
    final, second_a = odd_step(X, middle)
    assert (middle, final) == (57, 143)
    assert (first_a, second_a) == word


def main() -> None:
    exact_cases, full_factor_cases = verify_exact_blocks()
    cyclic_cases, closing_cases = verify_cyclic_compression()
    verify_regression()

    print("complete-block gcd compression no-go verified")
    print(f"exact block lifts checked={exact_cases}")
    print(f"full geometric-factor CRT blocks checked={full_factor_cases}")
    print(f"cyclic compression cases checked={cyclic_cases}")
    print(f"closing cyclic cases checked={closing_cases}")
    print("regression=91 -> 57 -> 143 with gcd 13")


if __name__ == "__main__":
    main()
