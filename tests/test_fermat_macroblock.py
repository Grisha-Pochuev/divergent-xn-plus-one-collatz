from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tools"))

from analyze_fermat_macroblock import (
    endpoint_mod_for_odd_part,
    hensel_target_odd_part,
    macro_endpoint,
)
from xn1 import odd_step, v2


def test_complete_macroblock_formula() -> None:
    m, length = 2, 3
    x = (1 << m) + 1
    n = (1 << (m * length)) - 1
    for _ in range(length):
        n, _ = odd_step(x, n)
    assert n == macro_endpoint(m, length) == 31
    assert v2(n + 1) == 5


def test_net_growth_survives_exit() -> None:
    m, length = 2, 7
    start = (1 << (m * length)) - 1
    assert macro_endpoint(m, length) == 19531
    assert macro_endpoint(m, length) > start


def test_precision_transfer_congruence() -> None:
    for m in range(2, 7):
        modulus = 1 << m
        for length in range(1, 80):
            k = v2(length)
            u = length >> k
            endpoint = macro_endpoint(m, length)
            expected = u if k == 0 else u + (1 << (m - 1))
            assert endpoint % modulus == expected % modulus


def test_endpoint_isometry() -> None:
    for m in range(2, 6):
        for k in range(4):
            for u in range(1, 32, 2):
                for w in range(u + 2, 34, 2):
                    eu = macro_endpoint(m, (1 << k) * u)
                    ew = macro_endpoint(m, (1 << k) * w)
                    assert v2(abs(eu - ew)) == v2(w - u)


def test_unique_hensel_targets() -> None:
    assert hensel_target_odd_part(3, 0, 17) == 599
    assert hensel_target_odd_part(4, 1, 10) == 39
    for m in range(2, 6):
        for k in range(3):
            bits = 8
            target = hensel_target_odd_part(m, k, bits)
            assert (endpoint_mod_for_odd_part(m, k, target, bits) + 1) % (1 << bits) == 0
            solutions = [
                u for u in range(1, 1 << bits, 2)
                if (endpoint_mod_for_odd_part(m, k, u, bits) + 1) % (1 << bits) == 0
            ]
            assert solutions == [target]
