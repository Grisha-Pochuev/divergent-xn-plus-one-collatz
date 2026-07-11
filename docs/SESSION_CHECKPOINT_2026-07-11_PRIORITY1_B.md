# Extended Priority 1 checkpoint — 2026-07-11

The strict prize problem remains open for

```text
X  = 104350542602662257699,
n0 = 1.
```

All cycle lengths through

```text
355561454311274250377
```

are excluded except

```text
177780727155637125193
177780727155637125195.
```

## 1. Exact full-layer coordinates

Write every edge as

```text
a_i=s_(i+1)+O*q_i,
O=1860810887857924950.
```

For either remaining length,

```text
Q=sum q_i<=6257.
```

The exact symmetric edge budget is

```text
sum_i [(s_i-1)+(s_(i+1)-1)+2*O*q_i]=2*(A-p).
```

## 2. Signed-label potential through sixty million

The global extremal signed-label potential is valid for all `358103` retained
targets through sixty million:

```text
all target labels are distinct,
all least-source labels are distinct,
the two label sets are disjoint.
```

The potential telescopes on the actual cycle and does not identify the
least-cost source with the actual source.  It proves

```text
sum_(1000000<n_i<=60000000)1/n_i <0.001185304.
```

## 3. Integral-Q and coupled-range duals

Keeping `Q` as an integer and separating the label, inverse-layer, and
signed-potential resources gives

```text
sum_(n_i<=1000000)1/n_i <0.085226583.
```

Coupling the small and middle ranges through the same `Q` gives the stronger
uniform finite-range bound

```text
sum_(n_i<=60000000)1/n_i <0.086152495.
```

The exact maximum occurs at

```text
Q=5841.
```

Updated mandatory tails:

```text
p=177780727155637125193:
  values above 60000000 >=25237969,
  zero-layer values there >=25231712;

p=177780727155637125195:
  values above 60000000 >=826903,
  zero-layer values there >=820646.
```

## 4. Expensive zero-layer localization

The cheap transition majority contributes less than `2.216*10^(-13)`, and at
most `6257` positions have positive layer.  Therefore the mandatory tail may be
localized to expensive zero-layer transitions.

For the first remaining length, at least

```text
22537952
```

distinct expensive zero-layer targets already lie in the finite interval

```text
60000000<n<X.
```

This is a direct finite target for a distribution or harmonic-sum theorem.

## 5. Finite-state potential no-go

For every `L`, exact valuation-word coding and CRT produce a positive orbit
segment of length `L` with

```text
q_i=0,
s_i=s_(i+1)=1,
transition cost=0
```

on every edge.  Consequently no fixed finite-state quotient can support a
universal telescoping inequality with a positive constant mean cost on all
zero-layer transitions.  A sufficiently long zero-cost segment repeats a
projected state and contradicts any such positive `delta`.

This closes the proposed finite-state positive-minimum-mean route.

## 6. Retained new certificate files

```text
docs/SIGNED_LABEL_SPLIT_RANGE_DUAL.md
tools/verify_signed_label_split_range_dual.py

docs/INTEGRAL_LAYER_BUDGET_DUAL.md
tools/verify_integral_layer_budget_dual.py

docs/BOTH_LENGTHS_SPLIT_RANGE_TAIL.md
tools/verify_both_lengths_split_range_tail.py

docs/EXPENSIVE_ZERO_LAYER_TAIL.md
tools/verify_expensive_zero_layer_tail.py

docs/FIRST_LENGTH_FINITE_ZERO_LAYER_MASS.md
tools/verify_first_length_finite_zero_layer_mass.py

docs/FINITE_STATE_ZERO_LAYER_POTENTIAL_NO_GO.md
tools/verify_finite_state_zero_layer_no_go.py

docs/COUPLED_Q_SPLIT_RANGE_DUAL.md
tools/verify_coupled_q_split_range_dual.py
```

## 7. Audit boundary

The former argument that treated the least-cost predecessor label as the actual
cycle source remains invalid.  The numerical figures `0.085226905`,
`0.086412209`, `811320`, and `805063` were later recovered by independent
signed-potential proofs and are now superseded by the stronger bounds above.
The invalid endpoint-identification premise must never be reused.

## 8. Exact next proof node

Do not return to a finite positive-mean automaton and do not enlarge trajectory
cutoffs blindly.

The next useful theorem must do one of the following:

1. give a rigorous harmonic-sum or counting bound for expensive zero-layer pair
   representatives in `(60000000,X)`;
2. exploit the exact Fermat-quotient formula for the least-layer predecessor
   with explicit constants;
3. build an unbounded value/height-dependent potential whose endpoint term can
   absorb arbitrarily long all-label-one zero-cost segments;
4. couple the forced finite zero-layer population to the global affine or
   reciprocal identities.

A finite barrier, a huge maximum, or a long growing block is still not a proof
of divergence.
