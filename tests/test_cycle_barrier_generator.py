from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tools"))

from generate_cycle_barrier import choose_k, construct_multiplier, verify_construction


def test_small_barriers() -> None:
    for barrier in (1, 10, 1000, 1_000_000):
        report = verify_construction(barrier)
        assert report["requested_cycle_barrier"] == barrier
        assert report["Q"] % 21 == 0
        assert report["Q_minus_floor_half_power"] <= 84


def test_large_symbolic_barrier() -> None:
    barrier = 10**100
    report = verify_construction(barrier)
    assert report["requested_cycle_barrier"] == barrier
    assert report["Q_decimal_digits"] > 100
    assert report["Q"] % 9 != 0


def test_minimal_k_condition() -> None:
    for barrier in (1, 12345, 10**20):
        k = choose_k(barrier)
        assert (1 << k) > 255 * barrier
        if k > 8:
            assert (1 << (k - 1)) <= 255 * barrier


def test_constructed_multiplier_above_half_power() -> None:
    k, q, _ = construct_multiplier(10**12)
    assert q * q > (1 << (2 * k + 1))
