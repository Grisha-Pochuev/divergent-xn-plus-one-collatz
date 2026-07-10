#!/usr/bin/env python3
"""Verify sample augmented residue/valuation paths by exact CRT coding."""
from __future__ import annotations

X = 104350542602662257699
M = 15099
H = 2154


def v2(value: int) -> int:
    assert value > 0
    return (value & -value).bit_length() - 1


def class_rep(label: int) -> int:
    residue = pow(pow(2, label, M), -1, M)
    return residue if residue & 1 else residue + M


def coding_residue(pattern: tuple[int, ...]) -> tuple[int, int]:
    total = sum(pattern)
    cumulative = 0
    affine = 0
    length = len(pattern)
    for j, a in enumerate(pattern):
        affine += X ** (length - 1 - j) * (1 << cumulative)
        cumulative += a
    modulus = 1 << (total + 1)
    residue = (((1 << total) - affine) * pow(X, -length, modulus)) % modulus
    return residue, modulus


def realize(source_label: int, pattern: tuple[int, ...]) -> int:
    code, modulus = coding_residue(pattern)
    source = class_rep(source_label)

    # Solve code + modulus*k == source (mod 2M).  Both residues are odd,
    # so division by 2 leaves one invertible congruence modulo M.
    rhs = ((source - code) // 2) % M
    k = (rhs * pow(modulus // 2, -1, M)) % M
    start = code + modulus * k

    assert start > 0 and start & 1
    assert start % (2 * M) == source % (2 * M)

    value = start
    for a in pattern:
        raw = X * value + 1
        observed = v2(raw)
        assert observed == a
        value = raw >> observed
        target = ((a - 1) % H) + 1
        assert value % M == pow(pow(2, target, M), -1, M)
    return start


def verify() -> None:
    assert pow(2, H, M) == 1
    cases = (
        (1, (1, 2, 3)),
        (17, (H + 17, 2, 2 * H + 5)),
        (H, (H, 1, H + 1)),
        (100, (2 * H + 1, H + 100, 67, 1)),
    )
    bit_lengths = []
    for source, pattern in cases:
        start = realize(source, pattern)
        bit_lengths.append(start.bit_length())

    print("augmented transition no-go samples verified")
    print(f"cases={len(cases)}")
    print(f"start bit lengths={bit_lengths}")


if __name__ == "__main__":
    verify()
