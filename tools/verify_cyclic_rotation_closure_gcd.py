#!/usr/bin/env python3
"""Verify the cyclic-rotation gcd criterion with exact integer arithmetic."""
from __future__ import annotations

from itertools import product
from math import gcd
from typing import Iterable, Sequence


def v2(n: int) -> int:
    if n <= 0:
        raise ValueError("v2 expects a positive integer")
    return (n & -n).bit_length() - 1


def word_constant(X: int, word: Sequence[int]) -> int:
    if X < 3 or X % 2 == 0:
        raise ValueError("X must be odd and at least 3")
    if not word or any(a <= 0 for a in word):
        raise ValueError("word must contain positive valuations")
    p = len(word)
    prefix = 0
    total = 0
    for j, a in enumerate(word):
        total += pow(X, p - 1 - j) << prefix
        prefix += a
    return total


def rotations(word: Sequence[int]) -> list[tuple[int, ...]]:
    w = tuple(word)
    return [w[k:] + w[:k] for k in range(len(w))]


def gcd_many(values: Iterable[int]) -> int:
    answer = 0
    for value in values:
        answer = gcd(answer, value)
    return answer


def exact_step(X: int, n: int) -> tuple[int, int]:
    value = X * n + 1
    a = v2(value)
    return value >> a, a


def verify_word(X: int, word: Sequence[int]) -> bool:
    p = len(word)
    A = sum(word)
    delta = (1 << A) - pow(X, p)
    qs = [word_constant(X, rot) for rot in rotations(word)]

    assert delta % 2 == 1
    assert all(q > 0 and q % 2 == 1 for q in qs)

    for k, a in enumerate(word):
        q_next = qs[(k + 1) % p]
        assert (q_next << a) == X * qs[k] + delta
        assert gcd(qs[k], q_next) == gcd(qs[k], delta)

    assert gcd_many(qs) == gcd(qs[0], delta)

    for split in range(1, p):
        W = word[:split]
        V = word[split:]
        rhs = pow(X, len(V)) * word_constant(X, W)
        rhs += (1 << sum(W)) * word_constant(X, V)
        assert rhs == qs[0]

    closes = delta > 0 and qs[0] % delta == 0
    if closes:
        states = [q // delta for q in qs]
        assert all(n > 0 and n % 2 == 1 for n in states)
        assert gcd_many(qs) == delta
        for k, (n, a) in enumerate(zip(states, word)):
            n_next, exact_a = exact_step(X, n)
            assert exact_a == a
            assert n_next == states[(k + 1) % p]
            assert gcd(qs[k], qs[(k + 1) % p]) == delta
            assert qs[(k + 1) % p] - qs[k] == delta * (
                states[(k + 1) % p] - states[k]
            )
    else:
        assert not (delta > 0 and gcd_many(qs) == delta)

    return closes


def verify_known_cycles() -> None:
    examples = [
        (5, (1, 4), (1, 3)),
        (5, (1, 1, 5), (13, 33, 83)),
        (5, (1, 3, 3), (17, 43, 27)),
    ]
    for X, word, expected_states in examples:
        assert verify_word(X, word)
        delta = (1 << sum(word)) - pow(X, len(word))
        qs = [word_constant(X, rot) for rot in rotations(word)]
        states = tuple(q // delta for q in qs)
        assert states == expected_states
        assert min(range(len(states)), key=states.__getitem__) == min(
            range(len(qs)), key=qs.__getitem__
        )

    # Positive closure coefficient alone is not sufficient.
    X = 5
    word = (2, 3)
    delta = (1 << sum(word)) - pow(X, len(word))
    q0 = word_constant(X, word)
    assert delta == 7 and q0 == 9 and q0 % delta != 0
    assert not verify_word(X, word)


def verify_primary_large_identities() -> None:
    B = 1 << 4501
    d = 349 * (1 << 500) - 347
    X = B - d
    words = [
        (4500, 4501, 4502),
        (1, 4501, 9002, 17),
        (4499, 2, 4503, 1, 4501),
    ]
    for word in words:
        verify_word(X, word)


def main() -> None:
    checked = 0
    closing = 0
    for X in (3, 5, 7, 9, 11):
        for length in range(1, 6):
            for word in product(range(1, 5), repeat=length):
                closing += int(verify_word(X, word))
                checked += 1

    verify_known_cycles()
    verify_primary_large_identities()

    print("cyclic-rotation closure gcd verified")
    print(f"exhaustive small words checked={checked}")
    print(f"closing words reconstructed={closing}")
    print("known 5n+1 cycles checked=3")
    print("primary-multiplier large word checks=3")


if __name__ == "__main__":
    main()
