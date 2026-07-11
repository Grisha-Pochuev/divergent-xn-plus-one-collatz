#!/usr/bin/env python3
from __future__ import annotations

M = 156
B = 1 << M
D = 9
X = B - D
Q = 1093
Q2 = Q * Q
H = 364
C = (X // Q) % Q


def v2(n: int) -> int:
    assert n > 0
    return (n & -n).bit_length() - 1


def main() -> None:
    assert X % Q == 0
    assert X % Q2 != 0
    assert pow(2, H, Q) == 1
    assert pow(2, H, Q2) == 1
    assert C == 151

    n_exc = (17 * B + 1) // D
    modulus_even = 2 * B
    combined_modulus = modulus_even * Q2
    inverse_even = pow(modulus_even, -1, Q2)

    assert D * n_exc - 1 == 17 * B
    assert v2(D * n_exc - 1) == M

    residues: set[int] = set()
    best: int | None = None
    best_data: tuple[int, int, int, int] | None = None

    for previous_label in range(1, H + 1):
        inverse_previous = pow(pow(2, previous_label, Q2), -1, Q2)
        for current_label in range(1, H + 1):
            inverse_current = pow(pow(2, current_label, Q2), -1, Q2)
            residue = (
                inverse_current
                * (1 + Q * C * inverse_previous)
            ) % Q2
            residues.add(residue)

            layer = ((residue - n_exc) % Q2) * inverse_even % Q2
            candidate = n_exc + modulus_even * layer

            assert candidate % Q2 == residue
            assert (candidate - n_exc) % modulus_even == 0
            assert v2(D * candidate - 1) == M

            if best is None or candidate < best:
                best = candidate
                best_data = (
                    previous_label,
                    current_label,
                    residue,
                    layer,
                )

    expected_best = (125 * B + 1) // D
    expected_data = (61, 64, 1_097_740, 6)

    assert len(residues) == H * H
    assert best == expected_best
    assert best_data == expected_data
    assert combined_modulus == (
        218247683691965730041139235214959349143617519566716928
    )

    print("verified X156 exceptional-source q^2 sieve")
    print(f"surviving adjacent-label classes={len(residues)}")
    print(f"least exceptional cycle source={best}")
    print(f"attaining data={best_data}")
    print(f"combined modulus={combined_modulus}")


if __name__ == "__main__":
    main()
