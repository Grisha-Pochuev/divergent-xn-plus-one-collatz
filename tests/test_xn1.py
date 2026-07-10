from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tools"))

from xn1 import odd_step, v2


def test_v2() -> None:
    assert v2(1) == 0
    assert v2(8) == 3
    assert v2(416) == 5


def test_known_5n1_cycle() -> None:
    n = 13
    values = []
    for _ in range(3):
        n, _ = odd_step(5, n)
        values.append(n)
    assert values == [33, 83, 13]


def test_finite_growth_identity() -> None:
    m, length = 5, 7
    x = (1 << m) + 1
    n = (1 << (m * length)) - 1
    for j in range(length - 1):
        assert n == (1 << (m * (length - j))) * (x**j) - 1
        nxt, a = odd_step(x, n)
        assert a == m
        assert nxt > n
        n = nxt
