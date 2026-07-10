# Current status

The strict target is to exhibit odd integers `X >= 5` and `n0 >= 1` whose accelerated odd-only orbit tends to positive infinity.

## Established in this repository

1. Exact implementation of the accelerated map.
2. Exact iterate formula and the standard sufficient average-valuation criterion.
3. A valuation lemma for `X = 2^m + 1`.
4. A construction of rigorously increasing orbit segments of any prescribed finite length.

## Not established

- No explicit infinite divergent orbit has been proved.
- A long computed trajectory is not treated as a proof.
- No finite automaton or certificate controlling an infinite orbit has yet been found.

## Current frontier

The most promising direction is a finite independently checkable certificate that controls cumulative valuation

```text
A_N = sum_{t < N} v2(X*n_t + 1)
```

and proves `A_N <= (log2(X)-epsilon)N` on an infinite orbit.
