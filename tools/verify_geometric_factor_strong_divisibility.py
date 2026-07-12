#!/usr/bin/env python3
"""Verify strong divisibility and persistent block-boundary gcd factors.

For B=2^m, X=B-d, and S_l=(B^l-X^l)/d, the script checks:
  * gcd(S_r,S_s)=S_gcd(r,s);
  * gcd(S_l,BX)=1 and gcd(S_l,d)=gcd(l,d);
  * exact complete-block endpoint gcd identities;
  * CRT constructions in which one odd prime divides every boundary of an
    arbitrarily prescribed finite list of complete blocks whose lengths have
    a common divisor >1;
  * the primary-candidate specialization modulo N*1093^2.
"""
from __future__ import annotations

import json
from math import gcd


def v2(value: int) -> int:
    if value <= 0:
        raise ValueError("v2 requires a positive integer")
    return (value & -value).bit_length() - 1


def odd_step(x: int, n: int) -> tuple[int, int]:
    numerator = x * n + 1
    a = v2(numerator)
    return numerator >> a, a


def geometric_factor(b: int, x: int, ell: int) -> int:
    if ell < 1:
        raise ValueError("ell must be positive")
    d = b - x
    if d <= 0:
        raise ValueError("requires B>X")
    return (b**ell - x**ell) // d


def complete_word(m: int, ell: int, terminal: int) -> tuple[int, ...]:
    if ell < 1 or terminal < 1 or terminal == m:
        raise ValueError("invalid complete block")
    return (m,) * (ell - 1) + (terminal,)


def word_constants(x: int, word: tuple[int, ...]) -> tuple[int, int]:
    total = 0
    q = 0
    p = len(word)
    for j, a in enumerate(word):
        q += x ** (p - 1 - j) * (1 << total)
        total += a
    return total, q


def coding_residue(x: int, word: tuple[int, ...]) -> tuple[int, int]:
    total, q = word_constants(x, word)
    modulus = 1 << (total + 1)
    residue = (((1 << total) - q) * pow(x, -len(word), modulus)) % modulus
    return residue, modulus


def crt_coprime(a: int, m: int, b: int, n: int) -> tuple[int, int]:
    if gcd(m, n) != 1:
        raise ValueError("CRT moduli must be coprime")
    value = (a + ((b - a) * pow(m, -1, n) % n) * m) % (m * n)
    return value, m * n


def observed_word(x: int, n: int, length: int) -> tuple[tuple[int, ...], list[int]]:
    word: list[int] = []
    states = [n]
    for _ in range(length):
        n, a = odd_step(x, n)
        word.append(a)
        states.append(n)
    return tuple(word), states


def smallest_odd_prime_factor(value: int) -> int:
    if value <= 1 or value % 2 == 0:
        raise ValueError("value must be odd and greater than one")
    p = 3
    while p * p <= value:
        if value % p == 0:
            return p
        p += 2
    return value


def verify_lucas_grid() -> int:
    checked = 0
    for m in range(3, 10):
        b = 1 << m
        for d in range(1, b - 4, 2):
            x = b - d
            if x < 5:
                continue
            if gcd(b, x) != 1:
                raise AssertionError("B and X should be coprime")
            values = {ell: geometric_factor(b, x, ell) for ell in range(1, 13)}
            for ell, s_ell in values.items():
                if s_ell % 2 != 1:
                    raise AssertionError("S_ell must be odd")
                if gcd(s_ell, b * x) != 1:
                    raise AssertionError("S_ell must be coprime to B*X")
                if gcd(s_ell, d) != gcd(ell, d):
                    raise AssertionError("gap gcd formula failed")
                for other, s_other in values.items():
                    expected = values[gcd(ell, other)]
                    if gcd(s_ell, s_other) != expected:
                        raise AssertionError("strong divisibility failed")
                    checked += 1
    return checked


def verify_exact_block_grid() -> int:
    checked = 0
    for m in range(3, 9):
        b = 1 << m
        for d in range(1, min(b - 4, 25), 2):
            x = b - d
            if x < 5:
                continue
            for ell in range(1, 6):
                for terminal in range(1, m + 3):
                    if terminal == m:
                        continue
                    word = complete_word(m, ell, terminal)
                    residue, modulus = coding_residue(x, word)
                    n = residue if residue > 0 else modulus
                    observed, states = observed_word(x, n, ell)
                    if observed != word:
                        raise AssertionError("exact word coding failed")
                    endpoint = states[-1]
                    s_ell = geometric_factor(b, x, ell)
                    total = sum(word)
                    if (1 << total) * endpoint != x**ell * n + s_ell:
                        raise AssertionError("complete-block affine identity failed")
                    if gcd(n, endpoint) != gcd(n, s_ell):
                        raise AssertionError("complete-block endpoint gcd failed")
                    checked += 1
    return checked


def persistent_boundary_example(
    m: int,
    d: int,
    lengths: tuple[int, ...],
    terminals: tuple[int, ...],
) -> dict[str, object]:
    if len(lengths) != len(terminals) or not lengths:
        raise ValueError("length and terminal lists must agree")
    b = 1 << m
    x = b - d
    common = 0
    for ell in lengths:
        common = gcd(common, ell)
    if common < 2:
        raise ValueError("block lengths must have gcd at least two")

    s_common = geometric_factor(b, x, common)
    q = smallest_odd_prime_factor(s_common)
    blocks = [complete_word(m, ell, terminal)
              for ell, terminal in zip(lengths, terminals)]
    word = tuple(a for block in blocks for a in block)
    residue, power_two_modulus = coding_residue(x, word)
    n, combined_modulus = crt_coprime(residue, power_two_modulus, 0, q)
    if n == 0:
        n = combined_modulus

    observed, states = observed_word(x, n, len(word))
    if observed != word:
        raise AssertionError("concatenated exact word failed")

    offsets = [0]
    for ell in lengths:
        offsets.append(offsets[-1] + ell)
    boundaries = [states[offset] for offset in offsets]
    if any(value % q for value in boundaries):
        raise AssertionError("persistent prime missing at a block boundary")

    defects: list[int] = []
    for i, ell in enumerate(lengths):
        s_ell = geometric_factor(b, x, ell)
        defect = gcd(boundaries[i], boundaries[i + 1])
        if defect != gcd(boundaries[i], s_ell):
            raise AssertionError("boundary defect identity failed")
        if defect % q:
            raise AssertionError("persistent prime missing from defect")
        defects.append(defect)

    return {
        "X": x,
        "common_length_divisor": common,
        "persistent_prime": q,
        "start": n,
        "boundaries": boundaries,
        "boundary_gcd_defects": defects,
        "word_length": len(word),
    }


def verify_persistence_grid() -> tuple[int, dict[str, object]]:
    checked = 0
    regression: dict[str, object] | None = None
    length_lists = (
        (2, 2),
        (2, 4, 6),
        (3, 6, 9),
        (4, 8, 12, 16),
    )
    for m in range(3, 8):
        b = 1 << m
        for d in range(1, min(b - 4, 15), 2):
            x = b - d
            if x < 5:
                continue
            for lengths in length_lists:
                terminal_choices = tuple(1 + (i % (m - 1)) for i in range(len(lengths)))
                result = persistent_boundary_example(m, d, lengths, terminal_choices)
                checked += 1
                if m == 3 and d == 3 and lengths == (2, 4, 6):
                    regression = result
    if regression is None:
        raise AssertionError("missing X=5 persistence regression")
    expected = {
        "X": 5,
        "common_length_divisor": 2,
        "persistent_prime": 13,
        "start": 2620090395,
        "boundaries": [2620090395, 4093891243, 1249356459, 297869793],
        "boundary_gcd_defects": [13, 13, 39],
        "word_length": 12,
    }
    if regression != expected:
        raise AssertionError((regression, expected))
    return checked, regression


def verify_primary_specialization() -> int:
    n_modulus = (1 << 500) - 1
    b = 1 << 4501
    d = 349 * (1 << 500) - 347
    x = b - d
    if x % n_modulus != 0 or x % 1093 != 0 or x % (1093**2) == 0:
        raise AssertionError("primary factorization markers failed")
    sieve_modulus = n_modulus * 1093**2
    checked = 0
    for ell in range(1, 25):
        s_ell = geometric_factor(b, x, ell)
        if gcd(s_ell, sieve_modulus) != 1:
            raise AssertionError("S_ell meets the permanent-sieve modulus")
        if s_ell % n_modulus != pow(2, ell - 1, n_modulus):
            raise AssertionError("primary N residue failed")
        if s_ell % 1093 != pow(b, ell - 1, 1093):
            raise AssertionError("primary 1093 residue failed")
        checked += 1
    return checked


def main() -> None:
    lucas_cases = verify_lucas_grid()
    exact_blocks = verify_exact_block_grid()
    persistence_cases, regression = verify_persistence_grid()
    primary_cases = verify_primary_specialization()
    print(json.dumps({
        "lucas_pair_checks": lucas_cases,
        "exact_complete_blocks": exact_blocks,
        "persistent_boundary_constructions": persistence_cases,
        "primary_specialization_lengths": primary_cases,
        "regression": regression,
        "strict_prize_solution": False,
        "status": (
            "geometric factors form a strong divisibility sequence; "
            "a common defect prime can persist through any prescribed finite "
            "block list with nontrivial common length divisor"
        ),
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
