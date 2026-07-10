#!/usr/bin/env python3
"""Verify the permanent mod-3 predecessor sieve with exact arithmetic."""
from __future__ import annotations

from collections import Counter
from math import gcd

X = 104350542602662257699
M = 15099
H = 2154
D = 2 * M
REFINED_MODULUS = 6 * M


def class_representatives() -> list[int]:
    inv2 = pow(2, -1, M)
    representatives: list[int] = []
    residue = 1
    for _t in range(1, H + 1):
        residue = residue * inv2 % M
        representative = residue if residue & 1 else residue + M
        if representative == 1:
            # The fixed orbit cannot return to the literal value 1.
            representative += D
        representatives.append(representative)
    return representatives


def predecessor_residue_mod3(t: int, n: int) -> int:
    """Residue modulo 3 of every direct predecessor of this refined lift."""
    assert (pow(2, t, 3) * (n % 3)) % 3 == 1
    numerator_mod9 = (pow(2, t, 9) * (n % 9) - 1) % 9
    assert numerator_mod9 % 3 == 0
    y = X // 3
    return (numerator_mod9 // 3) * pow(y, -1, 3) % 3


def verify() -> None:
    assert X == M * 6911089648497401
    assert X % 9 == 3
    assert (X // 3) % 3 == 1
    assert H % 6 == 0
    assert pow(2, H, M) == 1
    assert gcd(X // 3, 3) == 1
    assert REFINED_MODULUS == 90594

    representatives = class_representatives()
    assert len(representatives) == H
    assert len({rho % D for rho in representatives}) == H

    types: Counter[tuple[int, int]] = Counter()
    dead = 0
    surviving = 0
    refined_residues: set[int] = set()

    for t, rho in enumerate(representatives, start=1):
        local_dead = 0
        local_surviving = 0
        for j in range(3):
            n = rho + j * D
            refined_residues.add(n % REFINED_MODULUS)
            b = predecessor_residue_mod3(t, n)
            r = n % 3
            types[(b, r)] += 1
            if b == 0:
                local_dead += 1
                dead += 1
            else:
                local_surviving += 1
                surviving += 1

        # Exactly one of the three compatible lifts modulo 9 has only
        # predecessors divisible by 3.
        assert local_dead == 1
        assert local_surviving == 2

    assert len(refined_residues) == 3 * H
    assert dead == H == 2154
    assert surviving == 2 * H == 4308

    # Exact uniform type count before deleting the b=0 classes.
    for b in (0, 1, 2):
        for r in (1, 2):
            assert types[(b, r)] == 1077

    # Regression checks on explicit representatives.  The literal 1 is dead;
    # 25 survives and every predecessor has residue 1 modulo 3.
    assert predecessor_residue_mod3(H, 1) == 0
    assert predecessor_residue_mod3(904, 25) == 1

    # The two-state circulation consequence is elementary: every finite closed
    # directed walk has the same number of 1->2 and 2->1 crossings.
    sample_closed_walk = (1, 1, 2, 2, 1, 2, 1)
    crossings_12 = 0
    crossings_21 = 0
    for source, target in zip(sample_closed_walk, sample_closed_walk[1:] + sample_closed_walk[:1]):
        crossings_12 += source == 1 and target == 2
        crossings_21 += source == 2 and target == 1
    assert crossings_12 == crossings_21

    print("permanent mod-3 predecessor sieve verified")
    print(f"dead refined classes={dead}")
    print(f"surviving refined classes={surviving}")
    print("each of the four surviving oriented residue types has 1077 classes")


if __name__ == "__main__":
    verify()
