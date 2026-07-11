# Validated Priority 1 results addendum — 2026-07-11

This addendum records retained results obtained after the last full update of
`docs/VALIDATED_RESULTS.md`.  Every listed result has a precise derivation and
an exact checker.

## A. Signed-label potential through sixty million

For all `358103` retained targets through `60000000`, target full labels and
least-source full labels form disjoint sets.  A global signed-label potential
therefore telescopes on the actual cycle and proves

```text
sum_(1000000<n_i<=60000000)1/n_i <0.001185304.
```

The proof does not identify the least-cost source with the actual source.

Files:

```text
docs/SIGNED_LABEL_SPLIT_RANGE_DUAL.md
tools/verify_signed_label_split_range_dual.py
```

## B. Integral full-layer budget

For fixed integer

```text
Q=sum q_i,
```

the exact resources are

```text
sum(s_i-1)=B-OQ,
sum h_3(n_i)<=3Q,
sum signed_potential_cost<=2B.
```

Two exact rational duals cover all `Q=0,...,6257` and prove

```text
sum_(n_i<=1000000)1/n_i <0.085226583.
```

Files:

```text
docs/INTEGRAL_LAYER_BUDGET_DUAL.md
tools/verify_integral_layer_budget_dual.py
```

## C. Coupled-Q split-range dual

The small and middle ranges share the same actual integer `Q`.  Coupling their
piecewise exact duals gives

```text
sum_(n_i<=60000000)1/n_i <0.086152495.
```

The exact maximizing integer is `Q=5841`.

Consequences:

```text
p=177780727155637125193:
  values above 60000000 >=25237969,
  zero-layer values there >=25231712;

p=177780727155637125195:
  values above 60000000 >=826903,
  zero-layer values there >=820646.
```

Files:

```text
docs/COUPLED_Q_SPLIT_RANGE_DUAL.md
tools/verify_coupled_q_split_range_dual.py
```

## D. Finite expensive zero-layer population

For the first remaining length, after charging the finite-range contribution,
all cheap targets, all positive-layer positions, and the maximal contribution
from expensive targets at least `X`, at least

```text
22537952
```

distinct expensive zero-layer targets must lie in

```text
60000000<n<X.
```

Files:

```text
docs/FIRST_LENGTH_FINITE_ZERO_LAYER_MASS.md
tools/verify_first_length_finite_zero_layer_mass.py
```

## E. Expensive zero-layer tail localization

The mandatory tail populations may be counted specifically among expensive
zero-layer transitions because the entire cheap reciprocal contribution is
less than `2.216*10^(-13)` and at most `6257` positions have positive layer.

Files:

```text
docs/EXPENSIVE_ZERO_LAYER_TAIL.md
tools/verify_expensive_zero_layer_tail.py
```

## F. Finite-state positive-mean no-go

For every length `L`, exact valuation-word coding and CRT realize a positive
segment with

```text
q=0,
source label=target label=1,
transition cost=0
```

on all `L` edges.  Hence no fixed finite-state projection admits a universal
telescoping inequality with a positive constant mean layer or symmetric cost.

Files:

```text
docs/FINITE_STATE_ZERO_LAYER_POTENTIAL_NO_GO.md
tools/verify_finite_state_zero_layer_no_go.py
```

## G. Scope

These results do not exclude the final two lengths and do not prove divergence.
They reduce the remaining Priority 1 obstruction to a global counting,
harmonic-distribution, or unbounded-height potential theorem for expensive
zero-layer pair classes.
