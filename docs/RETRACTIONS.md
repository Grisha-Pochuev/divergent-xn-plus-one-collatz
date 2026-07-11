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

## 3. Retracted least-source flow-completion charge

### Discarded claim

For each possible target `n`, let `d_X(n)` be the least admissible full-order predecessor layer and let `u_min(n)` be the source label at that layer. A former argument used disjointness of the listed `u_min(n)` labels and target labels to charge an additional circulation-completion cost.

The scalar item cost

```text
u_min(n)-1+s(n)-1+2*O*d_X(n)
```

is a valid lower bound on the cost of an edge entering `n`: every higher layer adds `2*O`, more than any possible reduction of the source-label term.

However, `u_min(n)` is not necessarily the source label of the actual cycle edge. A target may be entered through a higher admissible layer with a different source label. Therefore minimum-cost source labels cannot be treated as actual circulation endpoints.

### Explicit regression example

For

```text
n=25,
target label=1208196370322173126,
```

the following admissible layers have different source labels:

```text
q=50  -> source label 1417145250304345366
q=58  -> source label 1528337129047052390
q=72  -> source label 1031609925039487316
q=114 -> source label 246249236019459722
q=118 -> source label 188856312470187702.
```

Thus one target does not determine one actual source endpoint.

### Numerical status

The following conclusions remain invalid and retracted:

```text
combined bound through 60000000 equal to 0.086412209,
811320 mandatory values above 60000000,
805063 mandatory zero-layer values above 60000000.
```

The retained valid figures are

```text
combined bound through 60000000 equal to 0.086609720,
799470 mandatory values above 60000000,
793213 mandatory zero-layer values above 60000000.
```

The numerical small-value bound

```text
0.085226905
```

was originally claimed using the invalid endpoint-identification argument above, so that original proof remains retracted.  The same numerical value has since been independently re-established by a different argument: a signed potential on all full labels whose contribution telescopes around the actual cycle and whose modified edge costs remain nonnegative for every admissible layer.

The recovered theorem is recorded separately in

```text
docs/SIGNED_LABEL_POTENTIAL_DUAL.md
tools/verify_signed_label_potential_dual.py
```

This recovery does not rehabilitate the discarded premise and does not recover the stronger sixty-million figures.

Audit files for the invalid argument:

```text
docs/FLOW_BALANCED_TWO_CONSTRAINT_DUAL.md
tools/verify_flow_balanced_two_constraint_dual.py
```

A future circulation dual must keep every admissible layer as a separate edge choice, or use a genuine potential whose sum telescopes for the actual chosen edges.

## 4. Claims that are evidence but not proofs

The following must never be promoted to a proof of divergence:

- a trajectory becoming extremely large after finitely many steps;
- positive average drift in a random model;
- a finite cycle barrier, regardless of its size;
- existence of arbitrarily long finite growing blocks;
- existence of compatible 2-adic regeneration targets without an ordinary positive integer realization;
- a cycle that avoids `1`.

## 5. Rules after an error is found

When a mathematical error is discovered:

1. identify the exact false premise;
2. add a small explicit counterexample when possible;
3. replace the old verifier by an audit or regression test;
4. remove the invalid conclusion from `CURRENT_STATUS.md`, `VALIDATED_RESULTS.md`, and `START_HERE.md`;
5. record the retraction here;
6. rebuild only from the last retained valid statement.

Do not delete the history of the error. Keeping a precise audit is part of reproducibility.
