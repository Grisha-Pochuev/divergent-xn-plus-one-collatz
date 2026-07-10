#!/usr/bin/env python3
"""Audit the retracted continued-fraction barrier and record the valid frontier."""
from __future__ import annotations

import json

CURRENT_RETAINED_BARRIER = 177780727155637125192
CURRENT_SPARSE_CAP = 355561454311274250377
CURRENT_SPARSE_EXCEPTIONS = (
    177780727155637125193,
    177780727155637125195,
)


def audit() -> dict[str, object]:
    x = 5
    cycle = (13, 33, 83)
    valuations = (1, 1, 5)
    total = sum(valuations)
    product = 1
    for n in cycle:
        product *= n

    false_left = pow(2, total, x)
    correct_left = (false_left * (product % x)) % x
    assert false_left != 1
    assert correct_left == 1

    return {
        "status": "retracted",
        "discarded_claim": "2^A == 1 (mod X) for every cycle",
        "counterexample_X": x,
        "counterexample_cycle": list(cycle),
        "counterexample_valuations": list(valuations),
        "A": total,
        "2^A_mod_X": false_left,
        "product_cycle_mod_X": product % x,
        "correct_relation_mod_X": correct_left,
        "correct_formula": "2^A * product(n_i) == 1 (mod X)",
        "current_retained_fixed_barrier": CURRENT_RETAINED_BARRIER,
        "current_sparse_cap": CURRENT_SPARSE_CAP,
        "sparse_exceptions": list(CURRENT_SPARSE_EXCEPTIONS),
    }


def main() -> None:
    print(json.dumps(audit(), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
