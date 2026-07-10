"""Exact accelerated Xn+1 arithmetic for positive odd integers."""
from __future__ import annotations


def v2(value: int) -> int:
    """Return the exponent of 2 dividing a positive integer."""
    if value <= 0:
        raise ValueError("value must be positive")
    return (value & -value).bit_length() - 1


def odd_step(x: int, n: int) -> tuple[int, int]:
    """Return (next odd value, number of halvings)."""
    if x < 5 or x % 2 == 0:
        raise ValueError("X must be odd and at least 5")
    if n <= 0 or n % 2 == 0:
        raise ValueError("n must be a positive odd integer")
    value = x * n + 1
    a = v2(value)
    return value >> a, a


def trajectory(x: int, n0: int, steps: int):
    """Yield (t, n_t, a_t, n_(t+1)) for exactly `steps` accelerated steps."""
    if steps < 0:
        raise ValueError("steps must be non-negative")
    n = n0
    for t in range(steps):
        nxt, a = odd_step(x, n)
        yield t, n, a, nxt
        n = nxt
