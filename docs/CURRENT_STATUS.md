# Current status

## Strict target

Find explicit odd positive `X>=5,n0` whose accelerated odd-only orbit tends to positive infinity. The strict problem is not solved.

## Main candidate

```text
X  = 104350542602662257699,
n0 = 1.
```

The repository proves:

1. the orbit cannot return to `1`;
2. every element of a reached nontrivial cycle is at least `25`;
3. every cycle length

```text
p <= 177780727155637125192
```

is impossible;
4. every length through

```text
355561454311274250377
```

is impossible except

```text
177780727155637125193
177780727155637125195.
```

## Full-layer and transition budgets

Put

```text
O=ord_X(2)=1860810887857924950,
a_i=s_(i+1)+O*q_i.
```

For either remaining length,

```text
sum_i q_i<=6257.
```

The exact symmetric edge cost

```text
c_i=(s_i-1)+(s_(i+1)-1)+2*O*q_i
```

satisfies

```text
sum_i c_i=2*(A-p).
```

Possible predecessors of a full representative satisfy

```text
m_q == m_0+q*63726582940809041391 (mod X).
```

A reached predecessor must itself lie in the full output subgroup.

## Cheap-transition concentration

With `K=5000`, more than `97.38%` of all cycle edges satisfy

```text
q_i=0,
s_i+s_(i+1)<=5001.
```

Every target in this cheap majority is at least

```text
781563824454394220933608138645145,
```

and the whole cheap majority contributes less than `2.216*10^(-13)` to `sum 1/n_i`.

The reciprocal correction is therefore forced into the expensive transitions. Exact consequences:

```text
p=...195: at least 5 distinct expensive targets below X,
p=...193: at least 355687 distinct expensive targets in (10^6,X).
```

Since at most `6257` positions have positive layer,

```text
p=...193: at least 349430 zero-layer expensive targets in (10^6,X).
```

For `p=...195`, the retained split-range reciprocal bound requires at least

```text
799470
```

distinct values above sixty million, at least

```text
793213
```

of which are zero-layer targets.

## Repeated transition classes and exact returns

One zero-layer label pair occurs at least

```text
3053943280435589
```

times in a single odd class modulo `2*X^2`. Hence every remaining hypothetical cycle has diameter at least

```text
66508995066170702555770104858896894988802023536957800776.
```

There is also one nonempty segment with

```text
length <=114286,
total valuation <=7771435,
endpoints equal modulo 2*X^2.
```

The higher-power repetition ladder is

```text
2-edge word: >=3114290401257 repetitions modulo 2*X^3
3-edge word: >=2918613523 repetitions modulo 2*X^4
4-edge word: >=2251677 repetitions modulo 2*X^5
5-edge word: >=1500 repetitions modulo 2*X^6.
```

These bounds control the cycle maximum or diameter, not its minimum.

## All-zero-layer branch

If every edge has `q=0`, the four-generation inverse sieve proves

```text
p=...193: a_out<=36 and n_next>1518500249*m,
p=...195: a_out<=39 and n_next>189812531*m,
```

where `m` is the cycle minimum. This is a strong minimum valley, but later compensating contractions remain possible.

## Reciprocal bounds

For the harder remaining length

```text
p=177780727155637125195
```

the cycle identity requires

```text
sum_i 1/n_i >0.099934206.
```

The strongest retained small-range certificate is the signed-label potential combined with depth-three inverse charging:

```text
sum_(n_i<=1000000) 1/n_i <0.085226905.
```

The signed potential is defined on all full labels and telescopes around the actual cycle; it does not identify the least-cost predecessor with the actual source.

The strongest retained split-range certificate is

```text
sum_(n_i<=60000000) 1/n_i <0.086609720,
```

which forces `799470` values above sixty million.

Audit distinction:

- the original endpoint-identification proof of `0.085226905` is invalid;
- the value is now independently re-established by `SIGNED_LABEL_POTENTIAL_DUAL`;
- `0.086412209`, `811320`, and `805063` remain retracted.

## Main current certificate files

```text
docs/EXPENSIVE_SMALL_TARGET_MASS.md
tools/verify_expensive_small_target_mass.py

docs/DEEP_ZERO_LAYER_MINIMUM_SIEVE.md
tools/verify_deep_zero_layer_minimum_sieve.py

docs/TWO_CONSTRAINT_INVERSE_DUAL.md
tools/verify_two_constraint_inverse_dual.py

docs/SPLIT_RANGE_RECIPROCAL_DUAL.md
tools/verify_split_range_reciprocal_dual.py

docs/FORCED_ZERO_LAYER_POPULATIONS.md
tools/verify_forced_zero_layer_populations.py

docs/SIGNED_LABEL_POTENTIAL_DUAL.md
tools/verify_signed_label_potential_dual.py
```

The earlier sparse-window, subgroup, predecessor-delay, inverse-window, transition-concentration, and repetition certificates remain retained and are registered in `run_checks.py`.

## Not established

- No explicit orbit is proved divergent.
- The two displayed cycle lengths are not excluded.
- Cycles beyond the sparse cap remain possible.
- The mandatory zero-layer populations have not yet been converted into a global contradiction.
- The height ladder bounds maxima, while the logarithmic theorem currently bounds minima.
- Finite certificates do not prove divergence.

## Exact next step

1. Extend the valid signed-label potential to a larger target range while keeping every admissible layer logically separate.
2. Alternatively construct a finite-state potential on zero-layer predecessor carry states.
3. Couple the mandatory zero-layer populations to the global reciprocal or height identities.
4. Do not enlarge raw trajectory or representative cutoffs blindly.

## Reproduction

```text
python run_checks.py
```
