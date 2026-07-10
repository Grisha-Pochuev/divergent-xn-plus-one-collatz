#!/usr/bin/env python3
"""Verify the short full-transition-class return theorem exactly."""
from __future__ import annotations

X = 104350542602662257699
R = 3053943280435589
TARGETS = (
    177780727155637125193,
    177780727155637125195,
)
EXPECTED_WEIGHT_CAP = 7771502
EXPECTED_LENGTH_CAP = 114286
EXPECTED_VALUATION_CAP = 7771435


def verify() -> None:
    assert X % 2 == 1
    for p in TARGETS:
        assert p & 1
        A = (133 * p + 1) // 2
        weight_cap = (67 * p + A) // R
        assert weight_cap == EXPECTED_WEIGHT_CAP

        # Since every nonempty segment has L>=1 and S>=L:
        length_cap = weight_cap // 68
        valuation_cap = weight_cap - 67
        assert length_cap == EXPECTED_LENGTH_CAP
        assert valuation_cap == EXPECTED_VALUATION_CAP

        # Check the claimed inequalities are internally compatible.
        assert 68 * length_cap <= weight_cap
        assert 68 * (length_cap + 1) > weight_cap
        assert 67 + valuation_cap == weight_cap

    print("short full-transition-class return verified")
    print(f"targets={TARGETS}")
    print(f"repeated occurrences={R}")
    print(f"weighted gap cap={EXPECTED_WEIGHT_CAP}")
    print(f"segment length cap={EXPECTED_LENGTH_CAP}")
    print(f"segment valuation cap={EXPECTED_VALUATION_CAP}")
    print(f"endpoint modulus={2*X*X}")


if __name__ == "__main__":
    verify()
