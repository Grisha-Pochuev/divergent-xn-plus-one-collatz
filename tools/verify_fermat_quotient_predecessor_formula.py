#!/usr/bin/env python3
"""Verify the Fermat-quotient full-predecessor formula exactly."""
from __future__ import annotations

from math import gcd

X = 104350542602662257699
M = 15099
P = 6911089648497401
O = 1860810887857924950
ORDER_P = 863886206062175
FULL_STEP = 63726582940809041391
EXPECTED_Q2 = 16863502182285
EXPECTED_STEP_P = 6336381663004171


def fermat_quotient(value: int) -> int:
    assert gcd(value, P) == 1
    numerator = pow(value % (P * P), P - 1, P * P) - 1
    assert numerator % P == 0
    return (numerator // P) % P


def predecessor_formula(n: int, s: int, q: int) -> int:
    return (
        -pow(M, -1, P)
        * (fermat_quotient(n) + (s + q * O) * EXPECTED_Q2)
    ) % P


def predecessor_direct(n: int, s: int, q: int) -> int:
    modulus = P * P
    numerator = (
        pow(2, s + q * O, modulus) * (n % modulus) - 1
    ) % modulus
    assert numerator % P == 0
    return (numerator // P) * pow(M, -1, P) % P


def verify() -> None:
    assert X == M * P
    assert pow(2, ORDER_P, P) == 1
    assert O % ORDER_P == 0

    q2 = fermat_quotient(2)
    assert q2 == EXPECTED_Q2
    assert q2 != 0

    step_p = (-pow(M, -1, P) * (O % P) * q2) % P
    assert step_p == EXPECTED_STEP_P
    assert FULL_STEP % P == step_p

    examples = (
        (25, 1208196370322173126, 0),
        (25, 1208196370322173126, 50),
        (2766317, 28862735489522559, 0),
        (33223, 549750138304358466, 25),
    )
    for n, s, q in examples:
        assert pow(2, s, X) * n % X == 1
        formula = predecessor_formula(n, s, q)
        direct = predecessor_direct(n, s, q)
        assert formula == direct

        next_formula = predecessor_formula(n, s, q + 1)
        assert (next_formula - formula) % P == step_p

    # Independently verify the product law used in the derivation.
    for u, v in ((2, 3), (25, 163), (2766317, 33223)):
        assert fermat_quotient(u * v) == (
            fermat_quotient(u) + fermat_quotient(v)
        ) % P

    print("Fermat-quotient predecessor formula verified")
    print(f"Q_P(2)={q2}")
    print(f"predecessor layer increment modulo P={step_p}")
    print(f"examples checked={len(examples)}")


if __name__ == "__main__":
    verify()
