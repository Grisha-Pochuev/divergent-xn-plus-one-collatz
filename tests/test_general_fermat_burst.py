from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tools"))

from verify_general_fermat_burst import verify


def test_general_burst_formula_grid() -> None:
    for m in range(2, 7):
        for length in range(1, 8):
            for core in range(1, 20, 2):
                report = verify(m, length, core)
                assert report["exit_v2"] >= 1


def test_general_burst_growth_example() -> None:
    report = verify(3, 30, 3)
    # This particular exact example has a small exit valuation and keeps the gain.
    assert report["endpoint_greater_than_start"]


def test_prescribed_exit_class() -> None:
    m, length, r = 4, 11, 5
    x = (1 << m) + 1
    modulus = 1 << (r + 1)
    core = (pow(pow(x, length, modulus), -1, modulus) * ((1 << r) + 1)) % modulus
    if core == 0:
        core += modulus
    report = verify(m, length, core)
    assert report["exit_v2"] == r
