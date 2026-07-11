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

The last item is now impossible: arbitrarily long realizable all-label-one
segments have exactly zero layer and transition cost.

## Immediate target A: finite expensive zero-layer harmonic bound

For the first length, at least `22537952` distinct targets satisfy

```text
60000000<n<X,
q=0,
s_source+s_target>=5002.
```

Seek a rigorous upper bound for the harmonic sum of all such possible targets.
A proof that their total possible reciprocal mass is below the required
`0.375...` finite-interval correction would eliminate `...193`.

Concrete tasks:

1. express every zero-layer pair class as

```text
n == 2^(-s)*(1+X*2^(-u)) (mod X^2);
```

2. exploit that `n<X` selects at most one ordinary representative per target
   full label;
3. translate the predecessor condition to the exact Fermat-quotient formula
   modulo the large prime divisor;
4. prove a counting or harmonic estimate with explicit constants;
5. apply partial summation only after a verified counting bound is available.

## Immediate target B: explicit Fermat-quotient distribution

The least-layer predecessor modulo the large prime can be written as an affine
expression in a Fermat quotient.  Search for a theorem controlling the joint
conditions

```text
target in <2>,
least predecessor in <2>,
target in a short ordinary interval.
```

Requirements:

- the theorem must be applicable to the actual prime
  `P=6911089648497401`;
- all constants and threshold hypotheses must be explicit;
- the numerical conclusion must beat the current reciprocal gap;
- generic asymptotic equidistribution is not enough.

Standard direct Pólya--Vinogradov bounds appear far too weak at the cutoff; a
successful result probably needs the special Fermat-quotient structure or a
strong subgroup/interval double-sum estimate.

## Immediate target C: unbounded height-dependent potential

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

A useful potential must eventually convert a large maximum/minimum ratio into a
contradiction, not merely prove an even larger maximum.

## Secondary target: optimize the signed-label potential

The current finite-range dual is already coupled through the same integer `Q`.
Further numerical optimization is secondary unless it produces a qualitative
change, such as a finite interval whose entire possible zero-layer harmonic
mass can be bounded below the required correction.

## Restrictions

No long trajectory scans, large parameter searches, or large Actions matrices
without explicit approval. Exact modular checks, compact deterministic
certificates, and short analytic calculations are allowed.

## Final-proof checklist

A valid prize solution must provide an explicit pair, exclude every positive
cycle, exclude repetition, invoke the positive-orbit dichotomy, and supply
independently runnable exact certificates.

## Recommended next session

> Work on a rigorous harmonic/counting bound for expensive zero-layer pair
> representatives in `(60000000,X)`, using the exact Fermat-quotient formula or
> an unbounded height potential. Do not return to finite positive-mean automata
> or blind cutoff growth.
