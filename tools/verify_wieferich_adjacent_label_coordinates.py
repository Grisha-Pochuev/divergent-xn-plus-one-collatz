#!/usr/bin/env python3
"""Verify adjacent-label residue coordinates at the Wieferich prime 1093."""
from __future__ import annotations

import json

Q = 1093
Q2 = Q * Q
H = 364


def label_residue(previous: int, current: int, c_mod_q: int) -> int:
    return (
        pow(2, -current, Q2)
        * (1 + Q * c_mod_q * pow(2, -previous, Q))
    ) % Q2


def verify_candidate(m: int, d: int, expected_c: int) -> dict[str, int]:
    x = (1 << m) - d
    if x % Q != 0 or x % Q2 == 0:
        raise AssertionError("q must divide X exactly once")
    c_mod_q = (x // Q) % Q
    if c_mod_q != expected_c:
        raise AssertionError((m, d, c_mod_q, expected_c))

    residues: dict[int, tuple[int, int]] = {}
    for previous in range(1, H + 1):
        for current in range(1, H + 1):
            residue = label_residue(previous, current, c_mod_q)
            if residue in residues:
                raise AssertionError((residue, residues[residue], (previous, current)))
            residues[residue] = (previous, current)

            if residue % Q != pow(2, -current, Q):
                raise AssertionError("target label recovery failed")
            lifted = ((pow(2, current, Q2) * residue - 1) // Q) % Q
            recovered_previous_power = (lifted * pow(c_mod_q, -1, Q)) % Q
            if recovered_previous_power != pow(2, -previous, Q):
                raise AssertionError("previous label recovery failed")

    if len(residues) != H * H:
        raise AssertionError("wrong adjacent-label class count")

    # Directly reproduce equation (5) for a sample of ordinary sources and
    # arbitrary full-order layers.  The result modulo q^2 is layer-independent.
    samples = 0
    for previous in range(1, H + 1, 37):
        source_mod_q = pow(2, -previous, Q)
        for lift in (0, 1, 17, Q - 1):
            source = source_mod_q + Q * lift
            for current in range(1, H + 1, 41):
                expected = label_residue(previous, current, c_mod_q)
                for layer in (0, 1, 5):
                    a = current + H * layer
                    actual = (pow(2, -a, Q2) * (1 + x * source)) % Q2
                    if actual != expected:
                        raise AssertionError("layer-independent transition failed")
                    samples += 1

    return {
        "m": m,
        "d": d,
        "X_mod_q_squared": x % Q2,
        "c_mod_q": c_mod_q,
        "adjacent_label_classes": len(residues),
        "transition_samples_checked": samples,
    }


def main() -> None:
    if pow(2, H, Q) != 1 or pow(2, H, Q2) != 1:
        raise AssertionError("Wieferich order certificate failed")
    for prime in (2, 3, 7, 13):
        if H % prime == 0 and pow(2, H // prime, Q) == 1:
            raise AssertionError("order is not minimal")

    reports = [
        verify_candidate(156, 9, 151),
        verify_candidate(260, 3, 936),
    ]
    print(json.dumps({
        "q": Q,
        "q_squared": Q2,
        "order": H,
        "one_step_output_classes": H * Q,
        "two_step_adjacent_label_classes": H * H,
        "retained_fraction_of_output_lifts": "1/3",
        "candidates": reports,
        "strict_prize_solution": False,
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
