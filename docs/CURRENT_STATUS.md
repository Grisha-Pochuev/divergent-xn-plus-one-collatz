# Current status

## Strict target

Find explicit odd positive `X>=5,n0` whose accelerated odd-only orbit tends to
positive infinity. The strict problem is not solved.

## Main candidate and finite frontier

```text
X  = 104350542602662257699,
n0 = 1.
```

The repository proves:

```text
all cycle lengths p<=177780727155637125192 are impossible;
all lengths through 355561454311274250377 are impossible except
177780727155637125193 and 177780727155637125195.
```

The orbit cannot return to `1`, and every reached nontrivial cycle element is at
least `25`.

## Exact full-layer budget

Write

```text
a_i=s_(i+1)+O*q_i,
O=ord_X(2)=1860810887857924950.
```

For either remaining length,

```text
Q=sum_i q_i<=6257.
```

The exact edge cost

```text
c_i=(s_i-1)+(s_(i+1)-1)+2*O*q_i
```

satisfies

```text
sum_i c_i=2*(A-p).
```

## Cheap versus expensive transitions

With threshold `K=5000`, more than `97.38%` of all edges are zero-layer edges
with adjacent-label sum at most `5001`. Every target in this cheap majority is
at least

```text
781563824454394220933608138645145,
```

and all cheap targets together contribute less than `2.216*10^(-13)` to
`sum 1/n_i`.

Thus the reciprocal correction is concentrated in expensive zero-layer
transitions.

## Signed-label potential through sixty million

The exact modular classification through `60000000` contains

```text
4279760 small-class candidates,
536735 genuine full representatives,
178632 permanent predecessor rejections,
358103 surviving targets.
```

Across all survivors:

```text
all target full labels are distinct,
all least-source full labels are distinct,
the two label sets are disjoint.
```

This defines a global signed-label potential. It telescopes on the actual cycle
and proves a valid lower cost for every actual layer choice; it does not treat
the least-cost source as the actual source.

## Integral-Q and coupled-range reciprocal bounds

Keeping `Q` as an integer separates the exact resources

```text
sum(s_i-1)=B-O*Q,
sum h_3(n_i)<=3Q,
sum signed_potential_cost<=2B.
```

Two rational duals cover all `Q=0,...,6257`. Coupling the small and middle
ranges through their common `Q` gives the strongest retained finite-range
bound:

```text
sum_(n_i<=60000000)1/n_i <0.086152495.
```

The global maximum of the certificate occurs at

```text
Q=5841.
```

The mandatory tails are therefore

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

## Repetition and height structure

One zero-layer transition pair occurs at least

```text
3053943280435589
```

times in one odd class modulo `2*X^2`. It forces an enormous diameter and a
nonempty segment with

```text
length<=114286,
total valuation<=7771435,
endpoints equal modulo 2*X^2.
```

Repeated words are also forced modulo `2*X^3` through `2*X^6`.

If every edge has `q=0`, the four-generation minimum sieve proves

```text
p=...193: a_out<=36 and n_next>1518500249*m,
p=...195: a_out<=39 and n_next>189812531*m.
```

These are not contradictions because later contractions remain possible.

## Finite-state no-go

Arbitrarily long positive orbit segments exist with

```text
q=0,
source label=target label=1,
edge cost=0.
```

Therefore no fixed finite quotient can support a universal telescoping
inequality with a positive constant mean cost on all zero-layer transitions.
The proposed finite-state minimum-mean route is closed.

## Main current certificates

```text
docs/SIGNED_LABEL_SPLIT_RANGE_DUAL.md
tools/verify_signed_label_split_range_dual.py

docs/INTEGRAL_LAYER_BUDGET_DUAL.md
tools/verify_integral_layer_budget_dual.py

docs/COUPLED_Q_SPLIT_RANGE_DUAL.md
tools/verify_coupled_q_split_range_dual.py

docs/BOTH_LENGTHS_SPLIT_RANGE_TAIL.md
tools/verify_both_lengths_split_range_tail.py

docs/EXPENSIVE_ZERO_LAYER_TAIL.md
tools/verify_expensive_zero_layer_tail.py

docs/FIRST_LENGTH_FINITE_ZERO_LAYER_MASS.md
tools/verify_first_length_finite_zero_layer_mass.py

docs/FINITE_STATE_ZERO_LAYER_POTENTIAL_NO_GO.md
tools/verify_finite_state_zero_layer_no_go.py
```

The earlier sparse-window, subgroup, predecessor-delay, inverse-window,
transition-concentration, repetition, and audit certificates remain retained.

## Not established

- No explicit orbit is proved divergent.
- The two displayed cycle lengths are not excluded.
- Cycles beyond the sparse cap remain possible.
- The forced expensive zero-layer populations have not yet been bounded by a
  sufficiently strong global distribution theorem.
- The height ladder controls maxima, while the logarithmic theorem currently
  controls minima.
- Finite certificates do not prove divergence.

## Exact next step

The remaining node is a global distribution/height problem:

1. bound the count or harmonic sum of expensive zero-layer pair representatives
   in `(60000000,X)`;
2. exploit the exact Fermat-quotient predecessor formula with explicit usable
   constants;
3. or construct an unbounded value-dependent potential, not a fixed finite
   positive-mean automaton.

Do not enlarge raw trajectory or representative cutoffs blindly.

## Reproduction

```text
python run_checks.py
```
