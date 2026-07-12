#!/usr/bin/env python3
"""Verify local CRT compatibility at a near-power block boundary."""
from __future__ import annotations


def v2(value: int) -> int:
    assert value > 0
    return (value & -value).bit_length() - 1


def odd_step(X: int, n: int) -> tuple[int, int]:
    numerator = X * n + 1
    a = v2(numerator)
    return numerator >> a, a


def word_constants(X: int, pattern: tuple[int, ...]) -> tuple[int, int]:
    total = 0
    additive = 0
    length = len(pattern)
    for j, a in enumerate(pattern):
        additive += X ** (length - 1 - j) * (1 << total)
        total += a
    return total, additive


def coding_residue(X: int, pattern: tuple[int, ...]) -> tuple[int, int]:
    total, additive = word_constants(X, pattern)
    modulus = 1 << (total + 1)
    residue = (
        ((1 << total) - additive) * pow(X, -len(pattern), modulus)
    ) % modulus
    assert residue % 2 == 1
    return residue, modulus


def crt_pair(
    odd_residue: int,
    odd_modulus: int,
    two_residue: int,
    two_modulus: int,
) -> int:
    assert odd_modulus % 2 == 1
    assert two_modulus > 0 and two_modulus & (two_modulus - 1) == 0
    multiplier = (
        (two_residue - odd_residue) * pow(odd_modulus, -1, two_modulus)
    ) % two_modulus
    value = odd_residue + odd_modulus * multiplier
    assert value % odd_modulus == odd_residue % odd_modulus
    assert value % two_modulus == two_residue % two_modulus
    return value


def observe(X: int, n: int, length: int) -> tuple[int, tuple[int, ...]]:
    valuations: list[int] = []
    for _ in range(length):
        n, a = odd_step(X, n)
        valuations.append(a)
    return n, tuple(valuations)


def ordinary_boundary(
    m: int,
    d: int,
    ell: int,
    deficit: int,
    pattern: tuple[int, ...],
    lift: int,
) -> tuple[int, int]:
    B = 1 << m
    X = B - d
    code, two_modulus = coding_residue(X, pattern)
    odd_modulus = X**ell
    boundary_class = (
        (1 << deficit) * pow(d, -1, odd_modulus)
    ) % odd_modulus
    boundary = crt_pair(
        boundary_class, odd_modulus, code, two_modulus
    )
    boundary += lift * odd_modulus * two_modulus
    if boundary <= 0:
        boundary += odd_modulus * two_modulus

    core_numerator = d * boundary - (1 << deficit)
    assert core_numerator > 0 and core_numerator % odd_modulus == 0
    core = core_numerator // odd_modulus
    assert core % 2 == 1

    source_numerator = (B**ell) * core // (1 << deficit) + 1
    assert source_numerator % d == 0
    source = source_numerator // d
    assert source > 0 and source % 2 == 1

    endpoint, incoming = observe(X, source, ell)
    assert endpoint == boundary
    assert incoming == (m,) * (ell - 1) + (m - deficit,)
    _, outgoing = observe(X, boundary, len(pattern))
    assert outgoing == pattern
    return source, boundary


def exceptional_boundary(
    m: int,
    d: int,
    ell: int,
    excess: int,
    pattern: tuple[int, ...],
    lift: int,
) -> tuple[int, int]:
    B = 1 << m
    X = B - d
    code, two_modulus = coding_residue(X, pattern)
    odd_modulus = X**ell
    boundary_class = pow(d * (1 << excess), -1, odd_modulus)
    boundary = crt_pair(
        boundary_class, odd_modulus, code, two_modulus
    )
    boundary += lift * odd_modulus * two_modulus
    if boundary <= 0:
        boundary += odd_modulus * two_modulus

    core_numerator = d * (1 << excess) * boundary - 1
    assert core_numerator > 0 and core_numerator % odd_modulus == 0
    core = core_numerator // odd_modulus
    assert core % 2 == 1

    source_numerator = (B**ell) * core + 1
    assert source_numerator % d == 0
    source = source_numerator // d
    assert source > 0 and source % 2 == 1

    endpoint, incoming = observe(X, source, ell)
    assert endpoint == boundary
    assert incoming == (m,) * (ell - 1) + (m + excess,)
    _, outgoing = observe(X, boundary, len(pattern))
    assert outgoing == pattern
    return source, boundary


def verify_small_grid() -> int:
    checked = 0
    for m in range(3, 8):
        B = 1 << m
        for d in range(1, B // 2, 2):
            X = B - d
            if X < 5:
                continue
            patterns = ((1,), (1, 2), (m, 1), (m + 1, 2))
            for ell in (1, 2):
                for deficit in sorted({1, m - 1}):
                    for pattern in patterns:
                        ordinary_boundary(
                            m, d, ell, deficit, pattern, lift=2
                        )
                        checked += 1
                for excess in (1, 2):
                    for pattern in patterns:
                        exceptional_boundary(
                            m, d, ell, excess, pattern, lift=2
                        )
                        checked += 1
    return checked


def verify_primary_candidate() -> None:
    m = 4501
    d = 349 * (1 << 500) - 347
    cases = (
        ("ordinary", 1, 1, (1, 2, 3), 0),
        ("ordinary", 2, 7, (m, 13), 1),
        ("ordinary", 3, 4500, (2, 1), 2),
        ("exceptional", 1, 1, (2, 1, 4), 0),
        ("exceptional", 2, 5, (m, m + 7), 1),
    )
    for kind, ell, credit, pattern, lift in cases:
        if kind == "ordinary":
            source, boundary = ordinary_boundary(
                m, d, ell, credit, pattern, lift
            )
        else:
            source, boundary = exceptional_boundary(
                m, d, ell, credit, pattern, lift
            )
        assert source.bit_length() > 4000
        assert boundary.bit_length() > 4000


def main() -> None:
    checked = verify_small_grid()
    verify_primary_candidate()
    print("fixed local endpoint congruence no-go verified")
    print(f"small exact constructions checked={checked}")
    print("primary ordinary and exceptional constructions=5")
    print(
        "every tested incoming block is compatible with its prescribed outgoing word"
    )


if __name__ == "__main__":
    main()
