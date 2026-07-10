# Current status

The strict target is to exhibit odd integers `X>=5` and `n0>=1` whose accelerated odd-only orbit tends to positive infinity.

## Main valid fixed candidate

The strongest fixed candidate currently retained is

```text
X  = 104350542602662257699,
n0 = 1.
```

For this pair the repository validly proves:

1. the orbit leaves `1` and can never return to `1`;
2. every possible element of a nontrivial cycle reached by the orbit is at least `25`;
3. every nontrivial positive cycle of accelerated length at most

```text
148557456445856651509
```

is impossible by the direct interval certificate in `ULTRA_STRONG_CANDIDATE.md`.

Therefore the orbit either tends to positive infinity or enters a nontrivial cycle longer than that finite barrier.

## Retraction of the `10^37` claim

The later continued-fraction claim excluding cycles through `10^37` is retracted.

It incorrectly asserted that a cycle with total halving count `A` satisfies

```text
2^A == 1 (mod X).
```

For a cycle, multiplication of the step equations gives the correct relation

```text
2^A * product_i(n_i) == 1 (mod X).
```

The accelerated `5n+1` cycle

```text
13 -> 33 -> 83 -> 13
```

has exact valuations `(1,1,5)`, so `A=7`, but

```text
2^7 == 3 (mod 5),
```

not `1`. Thus `ord_X(2)` need not divide `A`, and the continued-fraction reduction based on `A=ord_X(2)*q` is invalid.

See `docs/AUDIT_INVALID_ORDER_CONDITION.md`. The verifier now checks this counterexample instead of claiming the retracted barrier.

## General logarithmic cycle-height reduction

For every fixed odd `X>=5`, the exact cycle identity gives

```text
0 < A*log(2)-p*log(X) <= p/(X*m),
```

where `p` is the cycle length and `m` its minimum element. Effective lower bounds for the nonzero logarithmic linear form imply a computable polynomial upper bound

```text
m <= K_X*p^D_X.
```

This remains a valid structural reduction, but it does not by itself exclude cycles.

## Exact valuation-word coding

Every finite exact valuation word has exactly one coding class modulo `2^(A+1)`, and every positive representative follows that word. Positive-drift finite words therefore always have infinitely many rigorously growing starts.

Compatible prefixes define one 2-adic integer. They come from an ordinary nonnegative integer exactly when their least representatives eventually stabilize.

See `docs/VALUATION_WORD_CODING.md`.

## General Fermat-burst reduction

For

```text
X=2^m+1,
n_0=2^(mL)*u-1,
```

with positive odd `u`, the first `L-1` accelerated steps have valuation exactly `m`. If

```text
r=v2(X^L*u-1),
```

then the final valuation is `m+r`, and the exact endpoint is

```text
T_(m,L)(u)=(X^L*u-1)/2^r.
```

If

```text
L*log2(1+2^(-m)) > r+1,
```

then the complete burst ends above its start. Every prescribed finite exit valuation `r` is represented by the unique odd core class

```text
u == X^(-L)*(1+2^r)  (mod 2^(r+1)).
```

See `docs/GENERAL_FERMAT_BURST_REDUCTION.md` and `tools/verify_general_fermat_burst.py`.

## Other established results

1. Exact accelerated map and iterate formula.
2. Average-valuation criterion for exponential divergence.
3. Arbitrarily long rigorously increasing finite orbit segments.
4. Finite repetition bound for every exact valuation block.
5. Eventually periodic exact valuations force an eventually periodic orbit.
6. Complete `X=2^m+1` macroblocks whose accumulated growth can survive the exit.
7. A 2-adic isometry and a unique regeneration target at every finite precision.
8. Exact coordinate normal forms around `n=-1` and `n=1` for Fermat- and Mersenne-type multipliers.
9. Positive integer orbits are either eventually periodic or tend to positive infinity.
10. For `(X,n0)=(1093,1)`, the orbit never returns to `1`.
11. Exact inverse coding of every finite valuation word.
12. General arbitrary-core burst reduction for `X=2^m+1`.
13. Direct fixed cycle barrier `148557456445856651509` for the main candidate.
14. Effective polynomial upper bound on the minimum element of a hypothetical cycle in terms of its length.

## Not established

- No explicit orbit has yet been proved to tend to infinity.
- Cycles longer than the retained direct barrier remain logically possible for the main candidate.
- No ordinary positive integer supporting infinitely many net-positive regenerative bursts has yet been constructed.
- No low-average infinite valuation word with an eventually stable positive coding residue has yet been constructed.

## Current frontier

### Route A: repair the fixed-candidate attack

Any new modular cycle argument must retain the factor

```text
product_i(n_i)
```

in the cycle congruence. A valid completion needs a new global modular or descent obstruction.

### Route B: infinite regenerative chain

For `X=2^m+1`, use the exact arbitrary-core return map

```text
u -> odd_part(X^L*u-1)
```

to construct one ordinary positive start producing infinitely many net-positive bursts.

### Route C: stabilized low-average code

Construct an infinite valuation word with average below `log2(X)` whose exact coding residues eventually stabilize at a positive integer.

### Route D: combine cycle-height bounds

Make the logarithmic cycle-height constants explicit and combine the resulting polynomial upper bound with a modular lower bound that grows faster.

Any route would finish the strict prize problem.

## Reproducibility

Run

```text
python run_checks.py
```

to execute the retained certificates and the regression test preventing the invalid order condition from being reintroduced.
