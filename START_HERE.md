# START HERE

This file is the durable entry point for every new work session.

## Strict target

Find explicit positive odd integers `X>=5` and `n0>=1` such that

```text
C_X(n)=(X*n+1)/2^v2(X*n+1)
```

satisfies `C_X^t(n0) -> +infinity`. A cycle, avoidance of `1`, or any finite barrier is not a solution.

## Read first

```text
START_HERE.md
docs/CURRENT_STATUS.md
docs/VALIDATED_RESULTS.md
docs/RETRACTIONS.md
docs/NEXT_STEPS.md
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
O=ord_X(2)=1860810887857924950.
```

Every edge has the unique form

```text
a_i=s_(i+1)+O*q_i,
1<=s_i<=O,
q_i>=0.
```

For either remaining length,

```text
sum_i q_i<=6257.
```

Thus almost every edge uses the least full-order layer. The full predecessor progression is

```text
m_q == m_0+q*63726582940809041391 (mod X).
```

A reached predecessor must itself be a full output.

## Exact transition-cost frontier

Define

```text
c_i=(s_i-1)+(s_(i+1)-1)+2*O*q_i.
```

Every hypothetical cycle satisfies exactly

```text
sum_i c_i=2*(A-p).
```

This identity now drives Priority 1.

### Cheap/high versus expensive/small

With `K=5000`, at least `97.38%` of all edges satisfy

```text
q_i=0,
s_i+s_(i+1)<=5001.
```

Every target of such an edge is at least

```text
781563824454394220933608138645145,
```

so the entire cheap majority contributes less than `2.216*10^(-13)` to `sum 1/n_i`.

Therefore the required reciprocal correction is concentrated in expensive edges. One expensive target is forced below

```text
9190982840926584716   for p=...193,
46609216582838682965  for p=...195.
```

Both are below `X`.

### Repeated exact transition classes

With `K=197`, one zero-layer label pair occurs at least

```text
3053943280435589
```

times in one odd class modulo `2*X^2`. This forces cycle diameter at least

```text
66508995066170702555770104858896894988802023536957800776.
```

The repeated occurrences also force a nonempty segment with

```text
length <=114286,
total valuation <=7771435,
```

whose endpoints lie in the same class modulo `2*X^2`.

### Higher-power repetition ladder

```text
2-edge word: >=3114290401257 repetitions modulo 2*X^3
3-edge word: >=2918613523 repetitions modulo 2*X^4
4-edge word: >=2251677 repetitions modulo 2*X^5
5-edge word: >=1500 repetitions modulo 2*X^6.
```

The five-edge word forces a diameter above `3.87*10^123`.

These are bounds on the maximum/diameter, not the minimum, so they do not yet contradict the logarithmic minimum-height ceiling.

## Retained reciprocal information

For `p=...195`, the cycle identity requires

```text
sum_i 1/n_i >0.099934206.
```

The strongest retained finite inverse-window bound below one million is

```text
<0.085243521
```

at depth three. The new symmetric depth-one edge cost gives `<0.087543786` and supplies the correct cost functional for future circulation duals.

## Current certificate additions

```text
docs/MASSIVE_REPEATED_TRANSITION_CLASS.md
tools/verify_massive_repeated_transition_class.py
docs/CHEAP_TRANSITION_MASS_CONCENTRATION.md
tools/verify_cheap_transition_mass_concentration.py
docs/SHORT_FULL_CLASS_RETURN.md
tools/verify_short_full_class_return.py
docs/SYMMETRIC_EDGE_COST_DUAL.md
tools/verify_symmetric_edge_cost_dual.py
docs/MULTI_EDGE_REPETITION_LADDER.md
tools/verify_multi_edge_repetition_ladder.py
```

## Exact next step

Do not enlarge trajectory or residue cutoffs blindly.

1. Attack the forced small expensive target using its full predecessor delay and neighbouring labels.
2. Build a depth-two or multi-constraint rational dual using the symmetric edge cost.
3. Use the short return modulo `2*X^2` only together with extra affine information; the endpoint labels alone are tautological.
4. Seek a rigorous distribution bound for zero-layer pair classes modulo `X^2`.

## Critical retraction

The former `10^37` barrier is invalid. It used the false condition

```text
2^A == 1 (mod X).
```

The correct relation is

```text
2^A * product_i(n_i) == 1 (mod X).
```

The accelerated `5n+1` cycle `13 -> 33 -> 83 -> 13` is the regression counterexample. Never reintroduce the discarded order argument.

## Working rules

- Separate theorems from evidence.
- Test every theorem against known cycles.
- Add an exact checker where practical.
- Short symbolic and modular computations are allowed; large searches require explicit approval.
- Commit every rigorous result separately.
- A finite or sparse barrier is not divergence.

## Reproduction

```text
python run_checks.py
```
