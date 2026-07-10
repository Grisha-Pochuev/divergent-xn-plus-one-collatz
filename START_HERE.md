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
ord_X(2)=1860810887857924950.
```

Proved facts:

1. The graph on the `2154` output classes is complete, including loops.
2. Every compatible finite word remains realizable even with exact valuations and finite layers `q=(a-t)/H`; local forbidden-word searches cannot work.
3. Hypothetical cycle occupancies satisfy

```text
sum c_t=p,
sum t*c_t<=67p-1.
```

4. Cycle closure gives exact source/target flow balance.
5. Full output classes modulo `2X` have distinct minimum activation costs. If `m` full classes occur, then

```text
A >= p + m*(m-1)/2.
```

6. Since powers of two form an index-eight subgroup modulo `P`, small genuine full representatives can be exactly sieved.
7. Every cycle satisfies

```text
sum_i (2^a_(i-1)-X)*n_i = p,
```

and

```text
sum_i (2^a_i-X)/n_i
 = sum_i 1/(n_i*n_(i+1)) > 0.
```

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
```

## Exact next step

Attack the two remaining lengths separately. Their exact total valuation is fixed. The most promising route is to use exact full-class activation prices or the global height/reciprocal balance identities, rather than increasing the small-representative sieve to billions of tests.

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