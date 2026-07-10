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
- every element of a nontrivial cycle reached by it is at least `25`;
- no nontrivial positive cycle has accelerated length

```text
p <= 177780727155637125192;
```

- more strongly, every length through

```text
355561454311274250377
```

is impossible except the two odd values

```text
177780727155637125193
177780727155637125195.
```

The strict problem remains open.

## Priority 1 structure

Use

```text
M = 15099,
H = ord_M(2)=2154,
P = 6911089648497401,
X=M*P,
ord_P(2)=(P-1)/8,
O = ord_X(2)=1860810887857924950.
```

Proved facts:

1. The graph on the `2154` output classes is complete, including loops. Every compatible finite word remains realizable even with exact finite valuation layers. Local forbidden-word searches cannot work.
2. Hypothetical cycle occupancies satisfy

```text
sum c_t=p,
sum t*c_t<=67p-1,
```

and cycle closure gives exact source/target flow balance.
3. The full class label is paid by every occurrence, not merely when the class is first activated. Writing

```text
a_i=s_(i+1)+O*q_i,
1<=s_i<=O,
```

gives exactly

```text
A=sum_i s_i+O*sum_i q_i.
```

For either remaining length,

```text
sum_i q_i <= 6257.
```
4. The permanent predecessor sieve modulo `9` removes exactly one third of the refined small-class lifts: `2154` dead and `4308` surviving classes modulo `6M`.
5. Possible predecessors of a fixed full representative form the exact progression

```text
m_q == m_0+q*63726582940809041391 (mod X).
```

A predecessor occurring in a reached cycle must itself lie in the full output subgroup.
6. Below one million, the exact full predecessor delays range from `0` to `347`; only `133` of the `5824` permanent-sieve survivors have delay zero.
7. Through sixty million, `358103` representatives survive the permanent sieve, only `9462` have full delay zero, and the maximum delay is `558`.
8. For the harder remaining length `177780727155637125195`, exact fractional duals prove

```text
sum_(n_i<=60000000) 1/n_i < 0.087618737,
```

while the cycle identity requires a total greater than `0.099934206`. Hence more than `0.012315` must come from values above sixty million, requiring at least `738929` such distinct values.
9. Finite inverse-window charging strengthens the small-value bound further:

```text
depth 1: <0.087551912
depth 2: <0.085634587
depth 3: <0.085243521
```

below one million.

## Current certificate chain

```text
docs/FIRST_SPARSE_CYCLE_WINDOW.md
tools/verify_first_sparse_cycle_window.py
docs/FIRST_EXCEPTION_ELIMINATION.md
tools/verify_first_exception_elimination.py
docs/FULL_MODULUS_ACTIVATION_BOUND.md
tools/verify_full_modulus_activation_bound.py
docs/INDEX_EIGHT_SMALL_REPRESENTATIVE_SIEVE.md
tools/verify_index_eight_small_sieve.py
docs/THIRD_EXCEPTION_SUBGROUP_SIEVE.md
tools/verify_third_exception_subgroup_sieve.py
docs/PERMANENT_PREDECESSOR_MOD3_SIEVE.md
tools/verify_permanent_predecessor_mod3_sieve.py
docs/FULL_LABEL_OCCUPANCY_BUDGET.md
tools/verify_full_label_occupancy_budget.py
docs/FULL_PREDECESSOR_DELAY.md
tools/verify_full_predecessor_delay.py
docs/FULL_PREDECESSOR_RECIPROCAL_BOUND.md
tools/verify_full_predecessor_reciprocal_bound.py
docs/FINITE_INVERSE_WINDOW_CHARGING.md
tools/verify_finite_inverse_window_charging.py
```

## Exact next step

Do not enlarge the cutoff blindly. The remaining obstruction is the large zero-delay tail. Seek one of:

1. a finite-state or rational dual potential proving a positive mean full-order layer cost for long inverse windows;
2. a rigorous discrepancy bound for the initial full-class sequence `2^(-s) mod X` strong enough to control zero-delay representatives;
3. a source/target circulation inequality coupling the full predecessor progression with the two global height/reciprocal identities.

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
- Do not run long trajectory or parameter searches without explicit approval.
- A finite or sparse barrier is not divergence.

## Reproduction

```text
python run_checks.py
```
