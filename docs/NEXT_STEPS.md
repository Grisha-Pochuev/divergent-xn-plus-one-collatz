# Prioritized next steps

The strict prize problem remains open.

## Priority 1: eliminate the final two lengths

Current candidate:

```text
X  = 104350542602662257699,
n0 = 1.
```

Only two lengths remain through the current sparse cap:

```text
177780727155637125193
177780727155637125195.
```

## Current exact picture

Use

```text
O=ord_X(2)=1860810887857924950,
a_i=s_(i+1)+O*q_i,
Q=sum q_i<=6257.
```

The exact transition budget is

```text
sum_i[(s_i-1)+(s_(i+1)-1)+2*O*q_i]=2*(A-p).
```

More than `97.38%` of the cycle is forced into cheap zero-layer transitions,
but their total reciprocal contribution is less than `2.216*10^(-13)`.

The coupled integer-`Q` certificate proves

```text
sum_(n_i<=60000000)1/n_i <0.086152495.
```

Mandatory populations:

```text
p=...193:
  values above 60000000 >=25237969,
  zero-layer values there >=25231712,
  expensive zero-layer values in (60000000,X) >=22537952;

p=...195:
  values above 60000000 >=826903,
  zero-layer values there >=820646.
```

## New strict boundary for the first length

The permanent mod-3 predecessor sieve leaves `4308` possible refined target
classes modulo `90594`. Distinct targets below `X` have distinct full labels,
and for fixed `Q` their cardinality is bounded by

```text
m*(m-1)/2<=B-O*Q.
```

A rigorous harmonic packing certificate excludes

```text
Q=6242,6243,...,6257
```

for

```text
p=177780727155637125193.
```

Therefore the first remaining length now satisfies

```text
Q<=6241.
```

The boundary is narrow:

```text
packing upper at Q=6241 >0.377086594,
packing upper at Q=6242 <0.375630659,
required finite zero-layer mass >0.375632520964.
```

## Closed routes

Do not repeat:

- forbidden finite-word searches on the `2154` small classes;
- bounded layer-word enumeration as a global obstruction;
- blind enlargement of trajectory or representative cutoffs;
- the retracted assumption `ord_X(2)|A`;
- identification of the least-cost predecessor source with the actual source;
- comparison of a maximum lower bound with a theorem that bounds only the
  minimum;
- a fixed finite-state positive-minimum-mean potential on all zero-layer
  transitions.

Arbitrarily long realizable all-label-one segments have exactly zero layer and
transition cost, so the last route is impossible.

## Immediate target A: couple packing to the exact Q-dependent dual

The current high-`Q` exclusion uses a uniform finite-range upper bound. Replace
it by the exact affine dual value at each integer `Q`.

Tasks:

1. expose the small-range and middle-range dual objectives as exact affine
   functions of `Q`;
2. add the mod-3 harmonic packing upper for the finite interval `(60000000,X)`;
3. add the exact allowances for cheap targets, positive-layer positions, and
   targets at least `X`;
4. maximize the resulting total over `Q=0,...,6241`;
5. retain only a contradiction proved with rational arithmetic.

This is the most direct route to excluding more values of `Q` without new
number theory.

## Immediate target B: break the Q=6241 boundary

At `Q=6241`, the crude packing relaxation exceeds the required mass only
slightly. A very small rigorous density improvement may suffice.

Possible sources:

1. use the exact positions of the `4308` surviving residue classes modulo
   `90594`, rather than replacing every block by its `4308` smallest points;
2. impose the expensive-pair condition

```text
s_source+s_target>=5002;
```

3. impose the large-prime subgroup condition modulo

```text
P=6911089648497401;
```

4. exploit the exact zero-layer predecessor relation, not only target
   admissibility.

## Immediate target C: explicit subgroup or Fermat-quotient estimate

The least-layer predecessor modulo the large prime is an affine expression in a
Fermat quotient. Seek a theorem controlling the joint conditions

```text
target in <2>,
zero-layer predecessor in <2>,
target in a short ordinary interval.
```

Requirements:

- all constants must be explicit;
- threshold hypotheses must hold for the actual prime `P`;
- the numerical conclusion must improve the `Q=6241` packing bound;
- generic asymptotic equidistribution is not enough.

Standard direct Pólya--Vinogradov estimates appear too weak. A useful result
probably needs the special Fermat-quotient structure, a Burgess-type estimate
with explicit constants, or a strong subgroup/interval double-sum bound.

## Immediate target D: unbounded height-dependent potential

The finite-state positive-mean route is closed, but an unbounded potential may
still work. Seek

```text
cost(segment) >= endpoint_potential_change + global_charge
```

where the endpoint term grows with the actual integer height and can absorb
arbitrarily long zero-cost all-label-one segments.

Possible ingredients:

- `log n` or a piecewise logarithmic potential;
- the exact affine iterate on the short return segment;
- the minimum-valley growth factors in the all-zero-layer branch;
- the global reciprocal identities;
- the giant zero-layer growth block forced when any positive layer occurs.

A useful potential must convert a large maximum/minimum ratio into a
contradiction, not merely prove an even larger maximum.

## Restrictions

No long trajectory scans, large parameter searches, or large Actions matrices
without explicit approval. Exact modular checks, compact deterministic
certificates, and short analytic calculations are allowed.

## Final-proof checklist

A valid prize solution must provide an explicit pair, exclude every positive
cycle, exclude repetition, invoke the positive-orbit dichotomy, and supply
independently runnable exact certificates.

## Recommended next session

> First combine the exact `Q`-dependent reciprocal dual with the mod-3 harmonic
> packing bound. Then attack the first surviving boundary `Q=6241` using exact
> refined residue locations or an explicit subgroup/Fermat-quotient estimate.
> Do not return to finite positive-mean automata or blind cutoff growth.
