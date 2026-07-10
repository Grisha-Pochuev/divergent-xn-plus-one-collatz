# Current status

The strict target is to exhibit odd integers `X >= 5` and `n0 >= 1` whose accelerated odd-only orbit tends to positive infinity.

## Established in this repository

1. Exact implementation of the accelerated map.
2. Exact iterate formula and the standard sufficient average-valuation criterion.
3. A valuation lemma for `X = 2^m + 1`.
4. A construction of rigorously increasing orbit segments of any prescribed finite length.
5. A finite repetition bound for every exact valuation block.
6. The periodic-valuation obstruction: an eventually periodic sequence of exact halving counts forces an eventually periodic integer orbit, so it cannot describe a divergent positive orbit.

The new obstruction also explains the finite construction quantitatively. For `X=2^m+1`, a start `n` can repeat the exact one-symbol block `(m)` at most

```text
floor((v2(n+1)-1)/m)
```

times. The start `n=2^(m*L)-1` attains the bound `L-1`.

## Not established

- No explicit infinite divergent orbit has been proved.
- A long computed trajectory is not treated as a proof.
- No finite certificate controlling an infinite orbit has yet been found.

## Current frontier

A successful certificate cannot merely prescribe an eventually repeating exact valuation pattern. It must control a genuinely aperiodic orbit, most plausibly by one of two mechanisms:

1. a branching finite abstraction in which every allowed cycle has sufficient net growth, while exact valuations depend on finer information; or
2. an aperiodic chain of different growth blocks, with a rigorous capital/height inequality showing that every exit loss is paid for by earlier gain.

The immediate computational target is therefore **regenerative block chaining**. For a block `a=(a_0,...,a_(p-1))`, compute

```text
A = sum a_i,
B = sum X^(p-1-j) * 2^(a_0+...+a_(j-1)),
D = X^p - 2^A.
```

The rational center `-B/D` and the precision `v2(D*n+B)` measure how long the block can repeat. Search should study where an orbit lands when this precision is exhausted and whether the exit creates even greater precision for a different positive-drift block.

The final goal remains a checkable proof of

```text
A_N = sum_{t < N} v2(X*n_t + 1)
A_N <= (log2(X)-epsilon)N
```

on one infinite positive orbit.

See `docs/PERIODIC_VALUATION_OBSTRUCTION.md` and `tools/analyze_periodic_block.py`.