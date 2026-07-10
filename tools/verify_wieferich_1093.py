#!/usr/bin/env python3
"""Verify the finite arithmetic certificate behind the 1093 reduction."""
from __future__ import annotations

import json

from xn1 import odd_step


Q = 1093
Q_MINUS_ONE_FACTORS = (2, 3, 7, 13)
EXPECTED_ORDER = 364


def multiplicative_order_2_mod_q() -> int:
    """Compute ord_Q(2) by reducing the known exponent Q-1."""
    order = Q - 1
    for prime in Q_MINUS_ONE_FACTORS:
        while order % prime == 0 and pow(2, order // prime, Q) == 1:
            order //= prime
    return order


def verify_certificate() -> dict[str, object]:
    order = multiplicative_order_2_mod_q()
    if order != EXPECTED_ORDER:
        raise AssertionError(f"unexpected order: {order}")
    if pow(2, order, Q) != 1:
        raise AssertionError("order certificate fails modulo q")
    if pow(2, order, Q * Q) != 1:
        raise AssertionError("Wieferich certificate fails modulo q^2")

    first, first_a = odd_step(Q, 1)
    if (first, first_a) != (547, 1):
        raise AssertionError("unexpected first accelerated step")
    if first % Q == 0:
        raise AssertionError("an accelerated output should be coprime to q")

    # A direct predecessor associated with exponent order*k is divisible by q.
    # These finite samples only reproduce the algebra; the proof in the note
    # covers every k by the congruence modulo q^2.
    sample_quotients: list[dict[str, int]] = []
    for k in range(1, 5):
        predecessor = (pow(2, order * k) - 1) // Q
        if predecessor % Q != 0:
            raise AssertionError("sample predecessor is not divisible by q")
        sample_quotients.append({
            "k": k,
            "predecessor_mod_q": predecessor % Q,
            "predecessor_bit_length": predecessor.bit_length(),
        })

    return {
        "q": Q,
        "order_of_2_mod_q": order,
        "pow_2_order_mod_q_squared": pow(2, order, Q * Q),
        "first_accelerated_value_from_1": first,
        "first_v2": first_a,
        "sample_direct_predecessors": sample_quotients,
        "proved_reduction": (
            "the orbit from 1 never returns to 1; it either enters a "
            "nontrivial positive cycle or tends to positive infinity"
        ),
    }


def main() -> None:
    print(json.dumps(verify_certificate(), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
