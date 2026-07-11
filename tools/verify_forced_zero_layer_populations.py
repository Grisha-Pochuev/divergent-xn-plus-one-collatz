#!/usr/bin/env python3
"""Verify the forced zero-layer target populations exactly."""
from __future__ import annotations

LAYER_POSITION_CAP = 6257
FIRST_REQUIRED = 355687
SECOND_REQUIRED = 799470
EXPECTED_FIRST_ZERO = 349430
EXPECTED_SECOND_ZERO = 793213


def verify() -> None:
    first_zero = FIRST_REQUIRED - LAYER_POSITION_CAP
    second_zero = SECOND_REQUIRED - LAYER_POSITION_CAP

    assert first_zero == EXPECTED_FIRST_ZERO
    assert second_zero == EXPECTED_SECOND_ZERO
    assert first_zero > 0 and second_zero > 0

    print("forced zero-layer populations verified")
    print(f"first length: zero-layer expensive targets in (10^6,X)>={first_zero}")
    print(f"second length: zero-layer targets above 6*10^7>={second_zero}")


if __name__ == "__main__":
    verify()
