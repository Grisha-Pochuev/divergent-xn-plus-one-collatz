# Current status

The strict target is to exhibit odd integers `X >= 5` and `n0 >= 1` whose accelerated odd-only orbit tends to positive infinity.

## Established in this repository

1. Exact implementation of the accelerated map.
2. Exact iterate formula and the standard sufficient average-valuation criterion.
3. A valuation lemma for `X = 2^m + 1`.
4. A construction of rigorously increasing orbit segments of any prescribed finite length.
5. A finite repetition bound for every exact valuation block.
6. The periodic-valuation obstruction: an eventually periodic sequence of exact halving counts forces an eventually periodic integer orbit, so it cannot describe a divergent positive orbit.
7. An exact formula for the **complete** `X=2^m+1` macroblock, including its exceptional final exit.
8. A sufficient inequality proving that the accumulated growth of a complete macroblock can survive that exit.
9. A 2-adic isometry theorem for macroblock endpoints and a unique regeneration target modulo every power of two.

## Complete macroblock theorem

For

```text
X = 2^m+1,
n0 = 2^(mL)-1,
k = v2(L),
```

the orbit has `L-1` ordinary valuation-`m` steps and one exceptional final step. After all `L` accelerated steps its exact endpoint is

```text
E_m(L) = (X^L-1) / 2^(m+k).
```

Let

```text
delta_m = log2(1+2^(-m)).
```

If

```text
L*delta_m > m+v2(L)+1,
```

then the complete endpoint is already larger than its start:

```text
E_m(L) > 2^(mL)-1.
```

Thus the exceptional division need not erase the accumulated gain.

## Exact regeneration map

Write `L=2^k*u` with `u` odd and fix `m,k`. The endpoint as a function of `u` satisfies

```text
v2(E(u)-E(v)) = v2(u-v)
```

for all distinct positive odd `u,v`. Therefore, for every precision `S`, there is exactly one odd residue class

```text
u_S mod 2^S
```

for which

```text
E(u_S) == -1 mod 2^S.
```

Equivalently, the endpoint regenerates at least `S` bits of `v2(n+1)` precision. The target classes lift uniquely with `S`, so arbitrary finite regeneration is possible, but it follows one single 2-adic target rather than a freely chosen family.

A reproducible example is

```text
m=3, X=9, L=599:
v2(E_3(599)+1)=17,
```

and the complete macroblock grows from 1797 bits to 1896 bits.

## Not established

- No explicit infinite divergent orbit has been proved.
- A long computed trajectory is not treated as a proof.
- The nested finite regeneration targets have not yet been converted into one ordinary positive starting integer supporting infinitely many regenerations.

## Current frontier

The search is no longer a blind search for long growth. For the family `X=2^m+1`, both the complete gain and the precision transfer are now explicit.

The main unresolved question is whether one can chain the unique finite regeneration targets into an infinite sequence of complete macroblocks while keeping one fixed ordinary positive start and a positive accumulated growth margin. A successful proof must either:

1. construct such an aperiodic regenerative chain and prove that its capital tends to infinity; or
2. use the isometry theorem to build a different finite certificate whose allowed branches all preserve enough growth.

The final goal remains a checkable proof of

```text
A_N = sum_{t < N} v2(X*n_t + 1)
A_N <= (log2(X)-epsilon)N
```

on one infinite positive orbit.

See `docs/FERMAT_MACROBLOCK_REGENERATION.md`, `docs/PERIODIC_VALUATION_OBSTRUCTION.md`, `tools/analyze_fermat_macroblock.py`, and `tools/analyze_periodic_block.py`.
