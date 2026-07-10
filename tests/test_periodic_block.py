from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tools"))

from analyze_periodic_block import (
    actual_repetitions,
    block_constants,
    repetition_bound,
)


def test_known_5n1_cycle_block() -> None:
    pattern = (1, 1, 5)
    total, b, d = block_constants(5, pattern)
    assert (total, b, d) == (7, 39, -3)
    assert -b // d == 13
    assert repetition_bound(5, 13, pattern) is None
    assert actual_repetitions(5, 13, pattern, 10) == 10


def test_finite_positive_drift_repetition_bound() -> None:
    m, length = 5, 7
    x = (1 << m) + 1
    n = (1 << (m * length)) - 1
    pattern = (m,)
    total, b, d = block_constants(x, pattern)
    assert (total, b, d) == (m, 1, 1)
    assert repetition_bound(x, n, pattern) == length - 1
    assert actual_repetitions(x, n, pattern, length + 2) == length - 1


def test_zero_repeat_bound() -> None:
    # For X=5 and n=1 the first exact valuation is 1, not 2.
    assert repetition_bound(5, 1, (2,)) == 0
    assert actual_repetitions(5, 1, (2,), 10) == 0
