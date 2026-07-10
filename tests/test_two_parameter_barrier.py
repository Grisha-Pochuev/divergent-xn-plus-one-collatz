from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tools"))

from generate_two_parameter_barrier import (
    choose_k,
    choose_m,
    construct_multiplier,
    verify_construction,
)


def test_two_parameter_small_cases() -> None:
    for length, height in ((1, 1), (1000, 100), (1_000_000, 1_000_000)):
        report = verify_construction(length, height)
        assert report["requested_cycle_length_barrier"] == length
        assert report["requested_cycle_height_barrier"] == height
        assert report["M"] > height
        assert report["Q"] % 3 == 0
        assert report["Q"] % report["M"] == 0


def test_two_parameter_large_case() -> None:
    length = 10**50
    height = 10**40
    report = verify_construction(length, height)
    assert report["M"] > height
    assert report["Q_decimal_digits"] > 80


def test_two_parameter_mersenne_choice() -> None:
    for height in (1, 10**6, 10**30):
        m = choose_m(height)
        assert m % 6 == 3
        assert (1 << m) - 1 > height
        if m > 3:
            assert (1 << (m - 6)) - 1 <= height


def test_two_parameter_closeness() -> None:
    m, mersenne, k, q, root = construct_multiplier(10**9, 10**7)
    assert k == choose_k(10**9, mersenne)
    assert q - root <= 12 * mersenne
    assert q * q > (1 << (2 * k + 1))
    assert m % 6 == 3
