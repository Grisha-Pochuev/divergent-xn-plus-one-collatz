#!/usr/bin/env python3
"""Exact checks for WIEFERICH_Q_ADIC_LIFT_SATURATION_NO_GO.md."""

from math import gcd


Q = 1093
H = 364
M = 125
N = 2**500 - 1
B = 2**4501
D = 349 * 2**500 - 347
X = B - D
C = X // Q


def multiplicative_order(a: int, modulus: int) -> int:
    if gcd(a, modulus) != 1:
        raise ValueError("arguments must be coprime")
    value = 1
    for exponent in range(1, modulus + 1):
        value = value * a % modulus
        if value == 1:
            return exponent
    raise AssertionError("order not found")


def inv_pow2(exponent: int, modulus: int) -> int:
    return pow(pow(2, exponent, modulus), -1, modulus)


def base_q2_word(s_word: list[int]) -> list[int]:
    q2 = Q * Q
    length = len(s_word)
    residues = [0] * length
    for i, s_i in enumerate(s_word):
        previous_s = s_word[(i - 1) % length]
        residues[(i + 1) % length] = (
            inv_pow2(s_i, q2)
            * (1 + Q * (C % Q) * inv_pow2(previous_s, Q))
        ) % q2
    return residues


INV_91_MOD_125 = pow(91, -1, 125)


def base_layer(s_i: int, t_i: int) -> int:
    assert (t_i - s_i) % 4 == 0
    return ((t_i - s_i) // 4 * INV_91_MOD_125) % 125


def verify_level(
    s_word: list[int],
    t_word: list[int],
    residues: list[int],
    layers: list[int],
    level: int,
) -> None:
    modulus = Q**level
    length = len(s_word)
    for i in range(length):
        next_i = (i + 1) % length
        exponent = s_word[i] + H * layers[i]
        assert exponent % 500 == t_word[i] % 500
        assert (
            pow(2, exponent, modulus) * residues[next_i]
            - ((X % modulus) * residues[i] + 1)
        ) % modulus == 0


def lift_one_level(
    s_word: list[int],
    residues: list[int],
    layers: list[int],
    level: int,
    w: int,
) -> None:
    """Lift q^level to q^(level+1), keeping residue digits fixed."""
    next_modulus = Q ** (level + 1)
    length = len(s_word)
    for i in range(length):
        next_i = (i + 1) % length
        exponent = s_word[i] + H * layers[i]
        lhs = pow(2, exponent, next_modulus) * residues[next_i] % next_modulus
        rhs = ((X % next_modulus) * residues[i] + 1) % next_modulus
        defect = (lhs - rhs) % next_modulus
        assert defect % (Q**level) == 0
        defect_digit = defect // (Q**level) % Q

        coefficient = (
            pow(2, exponent, Q)
            * (M % Q)
            * w
            * (residues[next_i] % Q)
        ) % Q
        assert coefficient != 0
        new_layer_digit = -defect_digit * pow(coefficient, -1, Q) % Q
        layers[i] += M * Q ** (level - 2) * new_layer_digit


def main() -> None:
    assert X % N == 0
    assert X % Q == 0
    assert X % (Q * Q) != 0
    assert C % Q != 0

    assert multiplicative_order(2, Q) == H
    assert pow(2, H, Q * Q) == 1
    assert pow(2, H, Q**3) != 1
    w = (pow(2, H, Q**3) - 1) // (Q * Q) % Q
    assert w == 891

    assert gcd(500, H) == 4
    assert M == 500 // gcd(500, H)
    assert H * H * M == 16_562_000

    # Exhaust the informative q^2 adjacent-label classes.
    seen: set[int] = set()
    q2 = Q * Q
    for previous_s in range(1, H + 1):
        for s_i in range(1, H + 1):
            residue = (
                inv_pow2(s_i, q2)
                * (1 + Q * (C % Q) * inv_pow2(previous_s, Q))
            ) % q2
            seen.add(residue)
    assert len(seen) == H * H == 132_496

    regression_words = [
        [1],
        [1, 2, 3, 4],
        [364, 1, 181, 182, 17],
        [7, 91, 203, 364, 128, 55, 4],
    ]

    for s_word in regression_words:
        # Least representatives in 1..500 with matching residue modulo 4.
        t_word = [4 if s_i % 4 == 0 else s_i % 4 for s_i in s_word]
        residues = base_q2_word(s_word)
        layers = [base_layer(s_i, t_i) for s_i, t_i in zip(s_word, t_word)]

        for level in range(2, 11):
            verify_level(s_word, t_word, residues, layers, level)
            if level < 10:
                lift_one_level(s_word, residues, layers, level, w)

    print("PASS: all finite 1093-adic cyclic label lifts are saturated")
    print(f"Wieferich lift coefficient w={w}")
    print(f"base q^2 classes={len(seen)}")
    print(f"combined N*q^2 classes={H * H * M}")


if __name__ == "__main__":
    main()
