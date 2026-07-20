from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tools"))

from xn1 import odd_step, v2


def oddpart(value: int) -> int:
    return value >> v2(value)


def test_fermat_coordinate_cases() -> None:
    for m in range(2, 9):
        x = (1 << m) + 1
        for s in range(1, 3 * m + 2):
            for h in range(1, 40, 2):
                n = (1 << s) * h - 1
                nxt, a = odd_step(x, n)
                if s < m:
                    assert a == s
                    assert nxt == x * h - (1 << (m - s))
                elif s > m:
                    assert a == m
                    assert nxt == (1 << (s - m)) * x * h - 1
                else:
                    assert a == m + v2(x * h - 1)
                    assert nxt == oddpart(x * h - 1)


def test_fermat_grouped_exits() -> None:
    for m in range(2, 7):
        x = (1 << m) + 1
        for s in range(1, 4 * m + 1):
            length, remainder = divmod(s, m)
            for h in range(1, 20, 2):
                n = (1 << s) * h - 1
                steps = length if remainder == 0 else length + 1
                current = n
                for _ in range(steps):
                    current, _ = odd_step(x, current)
                if remainder == 0:
                    expected = oddpart((x**length) * h - 1)
                else:
                    expected = (x ** (length + 1)) * h - (1 << (m - remainder))
                assert current == expected


def test_mersenne_coordinate_cases_and_self_similarity() -> None:
    # m=2 gives X=3, outside this project's strict X>=5 domain.
    for m in range(3, 9):
        q = (1 << m) - 1
        for s in range(1, 3 * m + 2):
            for h in range(1, 40, 2):
                n = 1 + (1 << s) * h
                nxt, a = odd_step(q, n)
                if s < m:
                    assert a == s
                    assert nxt == q * h + (1 << (m - s))
                elif s > m:
                    assert a == m
                    assert nxt == 1 + q * (1 << (s - m)) * h
                else:
                    smaller, _ = odd_step(q, h)
                    assert nxt == smaller
                    assert a == m + v2(q * h + 1)
