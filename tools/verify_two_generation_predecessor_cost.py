#!/usr/bin/env python3
"""Verify the finite two-generation predecessor-cost certificate."""
from __future__ import annotations

from collections import Counter
from math import gcd

X = 104350542602662257699
M = 15099
H = 2154
O = 1860810887857924950
R = 3 * M
STEP = 22062


def output_label_map() -> dict[int, int]:
    inv2 = pow(2, -1, M)
    residue = 1
    labels: dict[int, int] = {}
    for t in range(1, H + 1):
        residue = residue * inv2 % M
        labels[residue] = t
    return labels


def one_generation_admissible(state: int, labels: dict[int, int]) -> bool:
    t = labels.get(state % M)
    if t is None:
        return False
    numerator_mod9 = (pow(2, t, 9) * (state % 9) - 1) % 9
    if numerator_mod9 % 3:
        return False
    predecessor_mod3 = (numerator_mod9 // 3) * pow(X // 3, -1, 3) % 3
    return predecessor_mod3 != 0


def state_distances(admissible: list[bool]) -> list[int]:
    distances = [-2] * R
    for residue_mod3 in (0, 1, 2):
        cycle: list[int] = []
        state = residue_mod3
        while not cycle or state != cycle[0]:
            cycle.append(state)
            state = (state + STEP) % R
        assert len(cycle) == R // 3

        if not any(admissible[state] for state in cycle):
            for state in cycle:
                distances[state] = -1
            continue

        length = len(cycle)
        temporary = [0] * length
        next_distance = 10**9
        # Two backwards passes make the circular next-admissible distance exact.
        for index in range(2 * length - 1, -1, -1):
            position = index % length
            if admissible[cycle[position]]:
                next_distance = 0
            else:
                next_distance += 1
            if index < length:
                temporary[position] = next_distance

        for state, distance in zip(cycle, temporary):
            distances[state] = distance

    assert all(distance >= -1 for distance in distances)
    return distances


def initial_predecessor_state(n: int, s: int) -> int:
    modulus = R * X
    numerator = (pow(2, s, modulus) * (n % modulus) - 1) % modulus
    assert numerator % X == 0
    return (numerator // X) % R


def verify() -> None:
    assert R == 45297
    assert O == 2 * 3 * 5**2 * 359 * 2677 * 15137 * 852763
    assert pow(2, O, X) == 1

    lifted_modulus = R * X
    power = pow(2, O, lifted_modulus)
    assert (power - 1) % X == 0
    assert power % R == 1
    quotient_step = ((power - 1) // X) % R
    assert quotient_step == STEP
    assert gcd(STEP, R) == 3

    labels = output_label_map()
    assert len(labels) == H
    admissible = [one_generation_admissible(state, labels) for state in range(R)]
    assert sum(admissible) == 4308
    assert sum(admissible[state] for state in range(R) if state % 3 == 1) == 2154
    assert sum(admissible[state] for state in range(R) if state % 3 == 2) == 2154
    assert not any(admissible[state] for state in range(R) if state % 3 == 0)

    distances = state_distances(admissible)
    distribution = Counter(distances)
    assert distribution[-1] == 15099
    assert distribution[0] == 4308
    assert max(distances) == 41
    assert distribution[41] == 1
    assert sum(distribution.values()) == R

    examples = (
        (25, 1208196370322173126, 13),
        (163, 1014347647263805892, 1),
        (547, 1820296293532601562, 0),
        (457, 423689776084813778, -1),
    )
    for n, s, expected_distance in examples:
        assert pow(2, s, X) * (n % X) % X == 1
        state = initial_predecessor_state(n, s)
        assert distances[state] == expected_distance
        if expected_distance >= 0:
            reached_state = (state + STEP * expected_distance) % R
            assert admissible[reached_state]
            for earlier in range(expected_distance):
                assert not admissible[(state + STEP * earlier) % R]

    print("two-generation predecessor cost verified")
    print(f"state modulus={R}")
    print(f"admissible states={sum(admissible)}")
    print(f"dead states={distribution[-1]}")
    print(f"maximum finite full-order delay={max(distances)}")


if __name__ == "__main__":
    verify()
