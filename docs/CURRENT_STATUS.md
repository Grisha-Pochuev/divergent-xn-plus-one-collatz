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
O=ord_X(2)=1860810887857924950,
Q=sum_i q_i.
```

For either remaining length,

```text
Q<=6257.
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

## Signed-label and coupled-Q reciprocal bounds

The exact modular classification through `60000000` contains

```text
4279760 small-class candidates,
536735 genuine full representatives,
178632 permanent predecessor rejections,
358103 surviving targets.
```

Across all survivors, target labels and least-source labels are separately
distinct and the two sets are disjoint. This defines a valid telescoping
signed-label potential on the actual cycle.

Keeping `Q` as an integer and coupling the small and middle ranges through their
common `Q` proves

```text
sum_(n_i<=60000000)1/n_i <0.086152495.
```

The finite-range certificate is maximized at

```text
Q=5841.
```

Mandatory tails:

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

## High-Q harmonic packing exclusion

The permanent predecessor sieve leaves exactly `4308` refined target classes
modulo

```text
6M=90594.
```

For fixed `Q`, the exact label budget is

```text
sum_i(s_i-1)=B-O*Q.
```

Distinct targets below `X` have distinct full labels. Therefore a set of `m`
finite zero-layer targets satisfies

```text
m*(m-1)/2<=B-O*Q.
```

Packing at most `4308` possible targets into every interval of length `90594`
and applying a rigorous harmonic bound gives

```text
U(6241)>0.377086594,
U(6242)<0.375630659.
```

The required finite expensive zero-layer reciprocal mass for the first length
is greater than

```text
0.375632520964.
```

Consequently

```text
Q=6242,6243,...,6257
```

are impossible for

```text
p=177780727155637125193,
```

and every remaining cycle of that length satisfies

```text
Q<=6241.
```

This is the first strict exclusion of an interval of possible full-order layer
totals.

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

These remain height statements, not contradictions.

## Finite-state no-go

Arbitrarily long positive orbit segments exist with

```text
q=0,
source label=target label=1,
edge cost=0.
```

Therefore no fixed finite quotient can support a universal telescoping
inequality with a positive constant mean cost on all zero-layer transitions.

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

docs/HIGH_Q_MOD3_HARMONIC_EXCLUSION.md
tools/verify_high_q_mod3_harmonic_exclusion.py

docs/FINITE_STATE_ZERO_LAYER_POTENTIAL_NO_GO.md
tools/verify_finite_state_zero_layer_no_go.py
```

## Not established

- No explicit orbit is proved divergent.
- The two displayed cycle lengths are not excluded.
- Cycles beyond the sparse cap remain possible.
- The first length still permits `Q=0,...,6241`.
- The forced expensive zero-layer populations have not yet been bounded by a
  sufficiently strong global distribution theorem.
- Finite certificates do not prove divergence.

## Exact next step

1. Combine the `Q`-dependent finite-range dual with harmonic packing rather than
   using uniform worst-case constants.
2. Attack the boundary `Q=6241`; only a small improvement over the mod-3 packing
   relaxation is needed.
3. Seek an explicit large-prime subgroup or Fermat-quotient estimate with usable
   constants.
4. Alternatively use an unbounded value-dependent height potential.
5. Do not enlarge raw trajectory or representative cutoffs blindly.

## Reproduction

```text
python run_checks.py
```
