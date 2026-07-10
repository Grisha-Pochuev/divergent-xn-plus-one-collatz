# Retractions and audit registry

This file records invalid, superseded, or currently unusable arguments so that later work does not silently reintroduce them.

## 1. Retracted `10^37` cycle barrier

### Discarded claim

A former argument claimed that a positive accelerated cycle with total halving count `A` must satisfy

```text
2^A == 1 (mod X),
```

and therefore that `ord_X(2)` divides `A`.

This is false.

### Correct relation

Multiplying the cycle equations gives

```text
2^A * product_i(n_i) == 1 (mod X).
```

The product of the cycle elements cannot be deleted.

### Regression counterexample

For the accelerated `5n+1` cycle

```text
13 -> 33 -> 83 -> 13
```

the exact valuations are

```text
(1,1,5),
A=7.
```

But

```text
2^7 == 3 (mod 5),
```

not `1`. The correct congruence holds only after multiplying by

```text
13*33*83 == 2 (mod 5).
```

### Consequence

All continued-fraction conclusions that required `A=ord_X(2)*q`, including the former `10^37` barrier, are retracted.

Audit files:

```text
docs/AUDIT_INVALID_ORDER_CONDITION.md
tools/verify_continued_fraction_barrier.py
tests/test_continued_fraction_barrier.py
```

The current valid finite barrier is independent of this discarded condition.

## 2. Published Mersenne-cycle claim not accepted as a project theorem

A literature claim that certain Mersenne multipliers have only the trivial positive cycle is not currently usable. A key supporting lemma admits the counterexample

```text
m=3, q=7, k=9, c=2:
7 divides 9*2^2-1=35,
```

although `9` is not a power of two.

Until the external argument is repaired and independently checked, it may be used only as a source of ideas, not as a theorem in this project.

File:

```text
docs/LITERATURE_AUDIT_SANTOS.md
```

## 3. Claims that are evidence but not proofs

The following must never be promoted to a proof of divergence:

- a trajectory becoming extremely large after finitely many steps;
- positive average drift in a random model;
- a finite cycle barrier, regardless of its size;
- existence of arbitrarily long finite growing blocks;
- existence of compatible 2-adic regeneration targets without an ordinary positive integer realization;
- a cycle that avoids `1`.

## 4. Rules after an error is found

When a mathematical error is discovered:

1. identify the exact false premise;
2. add a small explicit counterexample when possible;
3. replace the old verifier by an audit or regression test;
4. remove the invalid conclusion from `CURRENT_STATUS.md`, `VALIDATED_RESULTS.md`, and `START_HERE.md`;
5. record the retraction here;
6. rebuild only from the last retained valid statement.

Do not delete the history of the error. Keeping a precise audit is part of reproducibility.
