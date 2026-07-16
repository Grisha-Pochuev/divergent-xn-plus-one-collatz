#!/usr/bin/env python3
"""Exact checks for PERMANENT_LABEL_CYCLIC_CLOSURE_NO_GO.md."""

from math import gcd


def multiplicative_order(a: int, m: int) -> int:
    if gcd(a, m) != 1:
        raise ValueError("a and m must be coprime")
    x = 1
    for k in range(1, m + 1):
        x = (x * a) % m
        if x == 1:
            return k
    raise AssertionError("order not found")


def inv_pow2(exp: int, modulus: int) -> int:
    return pow(pow(2, exp, modulus), -1, modulus)


def q_residue(prev_s: int, s: int, q: int, c: int) -> int:
    q2 = q * q
    return (
        inv_pow2(s, q2)
        * (1 + q * c * inv_pow2(prev_s, q))
    ) % q2


def check_cyclic_word(s_word: list[int], t_word: list[int], q: int, c: int, n_mod: int, x: int) -> None:
    assert len(s_word) == len(t_word) > 0
    q2 = q * q
    p = len(s_word)

    rq = [0] * p
    rn = [0] * p
    for i in range(p):
        prev = (i - 1) % p
        # r_(i+1) is indexed at (i+1) mod p.
        rq[(i + 1) % p] = q_residue(s_word[prev], s_word[i], q, c)
        rn[(i + 1) % p] = inv_pow2(t_word[i], n_mod)

    for i in range(p):
        nxt = (i + 1) % p
        assert t_word[i] % 4 == s_word[i] % 4
        assert (pow(2, s_word[i], q2) * rq[nxt] - (x * rq[i] + 1)) % q2 == 0
        assert (pow(2, t_word[i], n_mod) * rn[nxt] - (x * rn[i] + 1)) % n_mod == 0


def main() -> None:
    q = 1093
    h = 364
    n_mod = 2**500 - 1
    b = 2**4501
    d = 349 * 2**500 - 347
    x = b - d

    assert x % n_mod == 0
    assert x % q == 0
    assert x % (q * q) != 0
    c = x // q
    assert c % q != 0

    assert multiplicative_order(2, q) == h
    assert pow(2, h, q * q) == 1
    assert pow(2, 500, n_mod) == 1
    # Exact order modulo N: any proper divisor of 500 is among these maximal ones.
    for prime in (2, 5):
        assert pow(2, 500 // prime, n_mod) != 1

    # Exhaust all adjacent q-label pairs.
    seen = set()
    q2 = q * q
    for prev_s in range(1, h + 1):
        for s in range(1, h + 1):
            r_next = q_residue(prev_s, s, q, c)
            r_current_mod_q = inv_pow2(prev_s, q)
            assert (pow(2, s, q2) * r_next - (q * c * r_current_mod_q + 1)) % q2 == 0
            seen.add(r_next)
    assert len(seen) == h * h

    assert gcd(500, h) == 4
    compatible_t_per_s = 500 // 4
    assert compatible_t_per_s == 125
    assert h * h * compatible_t_per_s == 16_562_000

    # Every t-label has the automatic N-coordinate transition identity.
    for t in range(1, 501):
        r_next = inv_pow2(t, n_mod)
        assert (pow(2, t, n_mod) * r_next - 1) % n_mod == 0

    # Deterministic cyclic regression words, including wraparound.
    words = [
        [1],
        [1, 2, 3, 4],
        [364, 1, 181, 182, 17],
        [7, 91, 203, 364, 128, 55, 4],
    ]
    for s_word in words:
        # Choose the least t in 1..500 with the same residue modulo 4.
        t_word = [4 if s % 4 == 0 else s % 4 for s in s_word]
        check_cyclic_word(s_word, t_word, q, c, n_mod, x)

    print("PASS: permanent labels are cyclically closure-compatible")
    print(f"q-label classes: {h*h}")
    print(f"combined classes: {h*h*compatible_t_per_s}")


if __name__ == "__main__":
    main()
