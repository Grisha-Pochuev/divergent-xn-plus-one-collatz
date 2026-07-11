#!/usr/bin/env python3
"""Verify the strengthened growth block forced by the exceptional minimum."""
from __future__ import annotations

O = 1860810887857924950
Q_CAP = 6257
EXCEPTIONAL_LAYER = 33
EXPECTED_K_CAP = 6225
EXPECTED_EXTRA = 19131228405286297
EXPECTED_DEFICIT = 3740753004121136066
EXPECTED_LENGTH = 28555366443672795
EXPECTED_INTEGER_EXPONENT = 1870376502060568033


def ceil_div(a: int, b: int) -> int:
    return (a + b - 1) // b


def verify() -> None:
    k_cap = Q_CAP - (EXCEPTIONAL_LAYER - 1)
    assert k_cap == EXPECTED_K_CAP

    extra = ceil_div(64 * O - 1, k_cap)
    assert extra == EXPECTED_EXTRA

    deficit = 2 * O - 131 + extra
    assert deficit == EXPECTED_DEFICIT

    length = ceil_div(deficit, 131)
    assert length == EXPECTED_LENGTH

    integer_exponent = deficit // 2
    assert integer_exponent == EXPECTED_INTEGER_EXPONENT
    assert 2 * integer_exponent <= deficit

    print("exceptional-minimum growth block verified")
    print(f"positive-layer edge count<={k_cap}")
    print(f"forced deficit>={deficit}")
    print(f"forced zero-layer block length>={length}")
    print(f"forced growth>2^{integer_exponent}")


if __name__ == "__main__":
    verify()
