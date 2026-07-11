# Priority 1 checkpoint C — 2026-07-11

The strict prize problem remains open.  The fixed candidate is

```text
X  = 104350542602662257699,
n0 = 1.
```

Through the current sparse cap, only the two cycle lengths

```text
177780727155637125193
177780727155637125195
```

remain unexcluded.

## Strongest retained finite-range bound

For either remaining length, write

```text
O=ord_X(2)=1860810887857924950,
a_i=s_(i+1)+O*q_i,
Q=sum_i q_i.
```

The coupled integer-`Q` dual gives

```text
sum_(n_i<=60000000) 1/n_i <0.086152495.
```

Consequently:

```text
p=177780727155637125193:
  values above 60000000 >=25237969,
  zero-layer values there >=25231712;

p=177780727155637125195:
  values above 60000000 >=826903,
  zero-layer values there >=820646.
```

For the first length, at least

```text
22537952
```

distinct expensive zero-layer targets lie in

```text
60000000<n<X.
```

## New high-Q exclusion

The permanent predecessor sieve modulo `3` leaves exactly `4308` refined target
classes modulo

```text
6M=90594.
```

For fixed `Q`, the exact label budget is

```text
sum_i(s_i-1)=B-O*Q.
```

Distinct targets below `X` have distinct full labels.  Hence the number `m` of
possible finite zero-layer targets satisfies

```text
m*(m-1)/2<=B-O*Q.
```

Packing at most `4308` possible targets into every interval of length `90594`
and applying a rigorous harmonic integral bound gives

```text
U(6241)>0.377086594,
U(6242)<0.375630659.
```

The first-length cycle requires more than

```text
0.375632520964...
```

of reciprocal mass from expensive zero-layer targets in `(60000000,X)`.
Therefore every integer

```text
6242<=Q<=6257
```

is impossible, and any remaining cycle of length

```text
177780727155637125193
```

must satisfy

```text
Q<=6241.
```

This is the first strict exclusion of a nonempty interval of possible full-order
layer totals.

Certificate files:

```text
docs/HIGH_Q_MOD3_HARMONIC_EXCLUSION.md
tools/verify_high_q_mod3_harmonic_exclusion.py
```

## Closed and unfinished routes

The fixed finite-state positive-mean route remains impossible because arbitrarily
long realizable zero-cost all-label-one segments exist.

A possible next strengthening would use a quantitative large-prime subgroup or
Fermat-quotient estimate.  That analytic line is not yet a theorem and is not
recorded as a result.

## Exact next node

1. Combine the `Q`-dependent finite-range dual with the harmonic packing bound,
   instead of using uniform worst-case constants.
2. Improve the packing density below `4308/90594` using a rigorously explicit
   large-prime subgroup or zero-layer predecessor condition.
3. The immediate numerical target is `Q=6241`: only a small improvement over the
   mod-3 packing relaxation is required.
4. Do not enlarge raw trajectory or representative cutoffs blindly.

A finite barrier or finite cycle-window obstruction is not yet divergence.
