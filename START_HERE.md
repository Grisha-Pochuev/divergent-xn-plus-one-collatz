# START HERE

This file is the durable entry point for every new work session.

## Strict target

Find explicit positive odd integers `X>=5` and `n0>=1` such that

```text
C_X(n)=(X*n+1)/2^v2(X*n+1)
```

satisfies `C_X^t(n0) -> +infinity`.  A cycle, avoidance of `1`, or any finite barrier is not a solution.

## Read first

```text
START_HERE.md
docs/CURRENT_STATUS.md
docs/VALIDATED_RESULTS.md
docs/RETRACTIONS.md
docs/NEXT_STEPS.md
docs/SESSION_CHECKPOINT_2026-07-11.md
run_checks.py
```

GitHub files are the durable source of truth.

## Main fixed candidate

```text
X  = 104350542602662257699,
n0 = 1.
```

Retained rigorous conclusions:

- the orbit leaves `1` and cannot return to `1`;
- every element of a reached nontrivial cycle is at least `25`;
- every cycle length

```text
p <= 177780727155637125192
```

is impossible;
- every length through

```text
355561454311274250377
```

is impossible except

```text
177780727155637125193
177780727155637125195.
```

The strict problem remains open.

## Full-layer coordinates

Use

```text
O=ord_X(2)=1860810887857924950,
a_i=s_(i+1)+O*q_i,
1<=s_i<=O,
q_i>=0.
```

For either remaining length,

```text
sum_i q_i<=6257.
```

Thus almost every edge uses its least full-order layer.

The exact symmetric edge cost

```text
c_i=(s_i-1)+(s_(i+1)-1)+2*O*q_i
```

satisfies

```text
sum_i c_i=2*(A-p).
```

Possible predecessors of a full representative form the exact progression

```text
m_q == m_0+q*63726582940809041391 (mod X).
```

A reached predecessor must itself be a full output.

## Current retained transition picture

With `K=5000`, more than `97.38%` of all edges satisfy

```text
q_i=0,
s_i+s_(i+1)<=5001.
```

Every target in that cheap majority is at least

```text
781563824454394220933608138645145,
```

so the whole cheap majority contributes less than `2.216*10^(-13)` to `sum 1/n_i`.

The reciprocal correction is therefore forced into expensive transitions:

```text
p=...193: at least 355687 expensive targets in (10^6,X),
p=...195: at least 5 expensive targets below X.
```

Since at most `6257` positions have positive layer,

```text
p=...193: at least 349430 zero-layer expensive targets in (10^6,X),
p=...195: at least 793213 zero-layer targets above 60000000.
```

The second number uses the retained split-range requirement of at least `799470` values above sixty million.

## Repetition and height structure

One exact zero-layer transition pair occurs at least

```text
3053943280435589
```

times in one class modulo `2*X^2`.  This forces cycle diameter at least

```text
66508995066170702555770104858896894988802023536957800776.
```

It also forces a nonempty segment with

```text
length <=114286,
total valuation <=7771435,
endpoints equal modulo 2*X^2.
```

Higher-power repetition:

```text
2-edge word: >=3114290401257 repetitions modulo 2*X^3
3-edge word: >=2918613523 repetitions modulo 2*X^4
4-edge word: >=2251677 repetitions modulo 2*X^5
5-edge word: >=1500 repetitions modulo 2*X^6.
```

These are bounds on the maximum or diameter, not on the minimum, so they do not yet contradict the logarithmic minimum-height theorem.

## All-zero-layer branch

If every edge has `q=0`, the four-generation inverse sieve proves

```text
p=...193: a_out<=36 and n_next>1518500249*m,
p=...195: a_out<=39 and n_next>189812531*m,
```

where `m` is the cycle minimum.  Later compensating contractions are not yet excluded.

## Strongest retained reciprocal information

For `p=...195`, the cycle identity requires

```text
sum_i 1/n_i >0.099934206.
```

The valid signed-label potential combined with depth-three inverse charging gives

```text
sum_(n_i<=1000000) 1/n_i <0.085226905.
```

The strongest retained split-range bound is

```text
sum_(n_i<=60000000) 1/n_i <0.086609720,
```

forcing at least `799470` values above sixty million and at least `793213` zero-layer values there.

Important audit distinction:

- the old endpoint-identification proof of `0.085226905` remains invalid;
- the same numerical bound is now independently re-established by `SIGNED_LABEL_POTENTIAL_DUAL`;
- `0.086412209`, `811320`, and `805063` remain retracted.

## Main current certificates

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

## Exact next step

Do not enlarge trajectory or residue cutoffs blindly.

1. Extend the valid signed-label potential to a larger target range while keeping every admissible layer logically separate.
2. Alternatively construct a finite-state potential on zero-layer predecessor carry states.
3. Couple the mandatory zero-layer populations to the global reciprocal or height identities.
4. Use the short return only with extra affine information; endpoint labels alone are tautological.

## Critical retractions

Never reintroduce

```text
2^A == 1 (mod X).
```

The correct cycle relation is

```text
2^A * product_i(n_i) == 1 (mod X).
```

Also never identify the least-cost predecessor source label with the source label chosen by the actual cycle.  A valid argument must keep layer choices separate or use a genuine telescoping potential.

## Working rules

- Separate theorems from evidence.
- Test every theorem against known cycles or an explicit regression example.
- Add an exact checker where practical.
- Short symbolic and modular computations are allowed; large searches require explicit approval.
- Commit every rigorous result or decisive refutation separately.
- A finite or sparse barrier is not divergence.

## Reproduction

```text
python run_checks.py
```
