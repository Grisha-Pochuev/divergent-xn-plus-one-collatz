#!/usr/bin/env python3
"""Verify the finite arithmetic for the hybrid Wieferich near-power candidate."""
from __future__ import annotations

import json

M = 260
B = 1 << M
X = B - 3
N0 = 1
Q = 1093
ORDER = 364
Q_MINUS_ONE_PRIMES = (2, 3, 7, 13)
FIRST = (1 << 259) - 1
BARRIER = (2 * X) // 9


def v2(value: int) -> int:
    if value <= 0:
        raise ValueError("v2 requires a positive integer")
    return (value & -value).bit_length() - 1


def odd_step(n: int) -> tuple[int, int]:
    numerator = X * n + 1
    a = v2(numerator)
    return numerator >> a, a


def multiplicative_order_2_mod_q() -> int:
    order = Q - 1
    for prime in Q_MINUS_ONE_PRIMES:
        while order % prime == 0 and pow(2, order // prime, Q) == 1:
            order //= prime
    return order


def verify_wieferich_structure() -> dict[str, int]:
    order = multiplicative_order_2_mod_q()
    if order != ORDER:
        raise AssertionError(f"unexpected order {order}")
    if pow(2, ORDER, Q * Q) != 1:
        raise AssertionError("Wieferich congruence failed")

    residue_q = pow(2, M, Q)
    residue_q2 = pow(2, M, Q * Q)
    if residue_q != 3:
        raise AssertionError("2^260 is not 3 modulo 1093")
    if residue_q2 != 1_023_051:
        raise AssertionError("unexpected residue modulo 1093^2")
    if X % Q != 0 or X % (Q * Q) == 0:
        raise AssertionError("1093 must divide X exactly once")
    if X % (Q * Q) != 1_023_048:
        raise AssertionError("unexpected X residue modulo q^2")
    if 1_023_048 != 936 * Q:
        raise AssertionError("q-adic quotient certificate failed")

    return {
        "order_of_2_mod_1093": order,
        "pow_2_364_mod_1093_squared": pow(2, ORDER, Q * Q),
        "pow_2_260_mod_1093": residue_q,
        "pow_2_260_mod_1093_squared": residue_q2,
        "X_mod_1093_squared": X % (Q * Q),
        "v_1093_of_X": 1,
    }


def verify_first_step() -> dict[str, int]:
    first, a = odd_step(N0)
    if (first, a) != (FIRST, 1):
        raise AssertionError("unexpected first accelerated step")
    if first == 1:
        raise AssertionError("orbit did not leave 1")
    if first % Q == 0:
        raise AssertionError("accelerated output cannot be divisible by q")
    return {"first_value": first, "first_valuation": a}


def verify_direct_predecessor_mechanism() -> list[dict[str, int]]:
    samples: list[dict[str, int]] = []
    # If a is a positive multiple of ord_q(2), q^2 divides 2^a-1.
    # Since q divides X exactly once, every integral direct predecessor is
    # divisible by q.  The samples reproduce the divisibility when X divides.
    for k in range(1, 9):
        a = ORDER * k
        numerator = pow(2, a) - 1
        if numerator % (Q * Q):
            raise AssertionError("Wieferich multiple lost q^2 divisibility")
        if numerator % X == 0:
            predecessor = numerator // X
            if predecessor % Q:
                raise AssertionError("direct predecessor is not divisible by q")
            samples.append({
                "k": k,
                "a": a,
                "predecessor_mod_1093": predecessor % Q,
                "predecessor_bits": predecessor.bit_length(),
            })
    return samples


def verify_cycle_barrier_arithmetic() -> dict[str, int]:
    if BARRIER != 411_705_206_177_124_250_394_919_057_808_668_116_811_626_612_144_499_783_251_404_743_139_246_683_164_216:
        raise AssertionError("unexpected barrier")
    if not 9 * BARRIER <= 2 * X:
        raise AssertionError("barrier floor lower inequality failed")
    if not 2 * X < 9 * (BARRIER + 1):
        raise AssertionError("barrier floor upper inequality failed")

    # The analytic proof uses ln(1+y)<y and ln(2)>2/3.  The finite checker
    # verifies the exact integer endpoint to which those inequalities apply.
    return {
        "X": X,
        "two_X": 2 * X,
        "floor_two_X_over_nine": BARRIER,
        "excluded_cycle_lengths_through": BARRIER,
    }


def verify_near_power_samples() -> int:
    checked = 0
    for r in list(range(1, 20)) + [M - 1, M, M + 1, M + 7, 2 * M, 2 * M + 3]:
        for u in range(1, 40, 2):
            value = (1 + (1 << r) * u)
            # This parameterization is for 3*n-1 rather than n-1.  Construct
            # integral n only when possible.
            numerator = (1 << r) * u + 1
            if numerator % 3:
                continue
            n = numerator // 3
            if n <= 0 or n % 2 == 0:
                continue
            nxt, a = odd_step(n)
            if r < M:
                expected = (1 << (M - r)) * n - u
                if (a, nxt) != (r, expected):
                    raise AssertionError("low near-power case failed")
            elif r > M:
                expected = n - (1 << (r - M)) * u
                if (a, nxt) != (M, expected):
                    raise AssertionError("high near-power case failed")
            else:
                core_num = X * u + 1
                core_a = v2(core_num)
                expected = (core_num >> core_a) // 3
                if a != M + core_a or nxt != expected:
                    raise AssertionError("exceptional near-power case failed")
            checked += 1
    return checked


def main() -> None:
    report = {
        "candidate": {"X": X, "n0": N0, "m": M, "d": 3},
        "wieferich": verify_wieferich_structure(),
        "first_step": verify_first_step(),
        "integral_direct_predecessor_samples": verify_direct_predecessor_mechanism(),
        "cycle_barrier": verify_cycle_barrier_arithmetic(),
        "near_power_samples_checked": verify_near_power_samples(),
        "proved_no_return_to_1": True,
        "strict_prize_solution": False,
        "remaining_alternative": "a nontrivial positive cycle longer than the barrier",
    }
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
