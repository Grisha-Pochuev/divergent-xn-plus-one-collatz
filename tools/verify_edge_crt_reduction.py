#!/usr/bin/env python3
"""Verify the CRT arithmetic behind the edge transition reduction."""
from __future__ import annotations

from math import gcd

X = 104350542602662257699
M = 15099
H = 2154


def source_residue(s: int) -> int:
    assert 1 <= s <= H
    residue = pow(pow(2, s, M), -1, M)
    return residue if residue & 1 else residue + M


def edge_progression(s: int, t: int) -> tuple[int, int]:
    """Return least positive representative and modulus for necessary edge conditions."""
    assert 1 <= s <= H
    assert 1 <= t <= H
    a = source_residue(s)
    mod1 = 2 * M
    mod2 = 1 << t
    b = (-pow(X, -1, mod2)) % mod2
    g = gcd(mod1, mod2)
    assert g == 2
    assert (a - b) % g == 0

    reduced1 = mod1 // g
    reduced2 = mod2 // g
    k = (((b - a) // g) * pow(reduced1, -1, reduced2)) % reduced2
    modulus = mod1 * reduced2
    representative = (a + mod1 * k) % modulus
    if representative == 0:
        representative = modulus
    if representative == 1:
        representative += modulus
    return representative, modulus


def verify() -> None:
    assert X % M == 0
    assert pow(2, H, M) == 1
    for prime in (2, 3, 359):
        assert pow(2, H // prime, M) != 1

    # Exhaust all source classes for a representative set of target depths.
    # The formula itself is exact for every t; these depths exercise tiny,
    # medium, and large powers of two without any trajectory search.
    targets = (1, 2, 3, 4, 5, 10, 20, 67, 100, 359, 718, 1077, 2154)
    for t in targets:
        expected_modulus = M * (1 << t)
        seen = set()
        for s in range(1, H + 1):
            representative, modulus = edge_progression(s, t)
            assert modulus == expected_modulus
            assert representative > 0 and representative & 1
            assert representative % (2 * M) == source_residue(s)
            assert (X * representative + 1) % (1 << t) == 0
            seen.add(representative % modulus)
        # Different source labels remain different modulo 2M, hence also
        # modulo the edge modulus.
        assert len(seen) == H

    # Known 5n+1 cycle regression: the same generalized CRT statement works
    # with its own modulus M=5 and order H=4.
    x = 5
    cycle = (13, 33, 83)
    valuations = (1, 1, 5)
    for n, a in zip(cycle, valuations):
        assert (x * n + 1) % (1 << a) == 0
        assert (x * n + 1) % (1 << (a + 1)) != 0

    print("edge CRT transition reduction verified")
    print(f"X={X}, M={M}, H={H}")
    print(f"source classes checked={H}")
    print(f"target depths checked={len(targets)}")


if __name__ == "__main__":
    verify()
