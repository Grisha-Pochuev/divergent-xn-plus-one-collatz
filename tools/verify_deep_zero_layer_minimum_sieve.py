#!/usr/bin/env python3
"""Verify the four-generation zero-layer minimum sieve exactly."""
from __future__ import annotations

from math import prod

X = 104350542602662257699
M = 15099
H = 2154
P = 6911089648497401
ORDER_P = 863886206062175
O = 1860810887857924950
PH_FACTORS = (25, 2677, 15137, 852763)
DEPTH = 4

CASES = (
    (
        5106101578294348744,
        {
            37: (2650031, 331524, 5946, 91, 1, 0),
            38: (1325003, 165762, 2910, 58, 0, 0),
            39: (662514, 83254, 1553, 32, 1, 0),
            40: (331257, 41211, 750, 14, 0, 0),
            41: (165610, 20705, 392, 7, 0, 0),
            42: (82809, 10390, 179, 2, 0, 0),
            43: (41388, 5396, 96, 2, 0, 0),
            44: (20705, 2580, 48, 1, 0, 0),
            45: (10354, 1251, 20, 0, 0, 0),
            46: (5182, 680, 15, 0, 0, 0),
            47: (2590, 312, 10, 0, 0, 0),
            48: (1302, 160, 6, 1, 0, 0),
            49: (654, 75, 1, 0, 0, 0),
        },
        36,
        1518500249,
    ),
    (
        25894009212734490968,
        {
            40: (1679845, 210393, 3735, 70, 0, 0),
            41: (839908, 105252, 1901, 28, 0, 0),
            42: (419959, 52518, 869, 16, 0, 0),
            43: (209966, 26716, 436, 8, 1, 0),
            44: (104989, 13104, 237, 5, 0, 0),
            45: (52510, 6524, 101, 2, 0, 0),
            46: (26235, 3349, 66, 0, 0, 0),
            47: (13141, 1644, 34, 1, 0, 0),
            48: (6560, 820, 16, 1, 0, 0),
            49: (3280, 394, 11, 0, 0, 0),
            50: (1644, 214, 2, 0, 0, 0),
            51: (814, 104, 3, 0, 0, 0),
        },
        39,
        189812531,
    ),
)


def output_label_map() -> dict[int, int]:
    inv2 = pow(2, -1, M)
    residue = 1
    labels: dict[int, int] = {}
    for t in range(1, H + 1):
        residue = residue * inv2 % M
        labels[residue] = t
    assert len(labels) == H
    return labels


def pohlig_hellman_data() -> tuple[dict[int, dict[int, int]], dict[int, int]]:
    assert prod(PH_FACTORS) == ORDER_P
    tables: dict[int, dict[int, int]] = {}
    coefficients: dict[int, int] = {}
    for q in PH_FACTORS:
        generator = pow(2, ORDER_P // q, P)
        table: dict[int, int] = {}
        value = 1
        for exponent in range(q):
            assert value not in table
            table[value] = exponent
            value = value * generator % P
        assert value == 1
        tables[q] = table
        complementary = ORDER_P // q
        coefficients[q] = (
            complementary * pow(complementary, -1, q)
        ) % ORDER_P
    return tables, coefficients


def discrete_log_2(
    value: int,
    tables: dict[int, dict[int, int]],
    coefficients: dict[int, int],
) -> int:
    exponent = 0
    for q in PH_FACTORS:
        projected = pow(value, ORDER_P // q, P)
        residue = tables[q].get(projected)
        if residue is None:
            raise AssertionError("value outside the base-2 subgroup")
        exponent = (exponent + residue * coefficients[q]) % ORDER_P
    assert pow(2, exponent, P) == value
    return exponent


def full_label(
    value: int,
    labels: dict[int, int],
    tables: dict[int, dict[int, int]],
    coefficients: dict[int, int],
) -> int:
    small = labels[value % M]
    exponent_mod_p = discrete_log_2(
        pow(value % P, -1, P), tables, coefficients
    )
    lift = ((exponent_mod_p - small) * pow(H, -1, ORDER_P)) % ORDER_P
    result = small + H * lift
    assert 1 <= result <= O
    assert pow(2, result, X) * (value % X) % X == 1
    return result


def exact_small_candidates(
    a: int,
    bound: int,
    allowed_residues: tuple[int, ...],
):
    power_modulus = 1 << (a + 1)
    exact_residue = (
        ((1 << a) - 1) * pow(X, -1, power_modulus)
    ) % power_modulus
    inverse = pow(power_modulus, -1, M)
    combined_modulus = power_modulus * M

    for residue_m in allowed_residues:
        lift = ((residue_m - exact_residue) % M) * inverse % M
        start = exact_residue + power_modulus * lift
        if start == 0:
            start = combined_modulus
        yield from range(start, bound + 1, combined_modulus)


def verify() -> None:
    labels = output_label_map()
    allowed_residues = tuple(sorted(labels))
    tables, coefficients = pohlig_hellman_data()

    def is_full(value: int) -> bool:
        return (
            value % M in labels
            and pow(value % P, ORDER_P, P) == 1
        )

    for bound, expected_rows, final_a, growth_factor in CASES:
        for a, expected in expected_rows.items():
            counts = [0] * (DEPTH + 2)
            for target in exact_small_candidates(a, bound, allowed_residues):
                counts[0] += 1
                if pow(target % P, ORDER_P, P) != 1:
                    continue
                counts[1] += 1

                modulus = X ** (DEPTH + 1)
                current = target % modulus
                for depth in range(1, DEPTH + 1):
                    label = full_label(
                        current % X, labels, tables, coefficients
                    )
                    numerator = (
                        pow(2, label, modulus) * current - 1
                    ) % modulus
                    assert numerator % X == 0
                    current = numerator // X
                    modulus //= X
                    if not is_full(current % X):
                        break
                    counts[depth + 1] += 1

            assert tuple(counts) == expected, (a, counts, expected)
            assert counts[-1] == 0

        assert X > growth_factor * (1 << final_a)
        print(f"bound={bound}")
        print(f"outgoing valuation<={final_a}")
        print(f"next value>{growth_factor}*minimum")

    print("deep zero-layer minimum sieve verified")


if __name__ == "__main__":
    verify()
