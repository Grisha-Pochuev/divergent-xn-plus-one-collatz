# Retractions and audit registry

This file records invalid, superseded, or currently unusable arguments so that
later work does not silently reintroduce them.

## 1. Retracted `10^37` cycle barrier

### Discarded claim

A former argument claimed that a positive accelerated cycle with total halving
count `A` must satisfy

```text
2^A==1 (mod X),
```

and therefore that `ord_X(2)` divides `A`. This is false.

### Correct relation

Multiplying the cycle equations gives

```text
2^A*product_i(n_i)==1 (mod X).
```

The product of the cycle elements cannot be deleted.

### Regression counterexample

For the accelerated `5n+1` cycle

```text
13 -> 33 -> 83 -> 13
```

with exact valuations `(1,1,5)`, one has `A=7` and

```text
2^7==3 (mod 5),
```

not `1`. The correct congruence holds only after multiplying by the cycle
product.

### Consequence

All conclusions requiring `A=ord_X(2)*q`, including the former `10^37`
barrier, remain retracted.

Audit files:

```text
docs/AUDIT_INVALID_ORDER_CONDITION.md
tools/verify_continued_fraction_barrier.py
tests/test_continued_fraction_barrier.py
```

The current finite barrier is independent of this discarded premise.

## 2. Published Mersenne-cycle claim not accepted

A literature claim that certain Mersenne multipliers have only the trivial
positive cycle is not currently usable. A supporting lemma admits

```text
m=3, q=7, k=9, c=2:
7 divides 9*2^2-1=35,
```

although `9` is not a power of two.

Until the external proof is repaired and independently checked, it may be used
only as a source of ideas.

File:

```text
docs/LITERATURE_AUDIT_SANTOS.md
```

## 3. Retracted least-source endpoint identification

### Discarded claim

For a target `n`, let `d_X(n)` be its least admissible full-order predecessor
layer and `u_min(n)` the source label at that layer. A former argument treated
`u_min(n)` as the source endpoint selected by the actual cycle and used the
listed least-source labels directly in a circulation-balance argument.

This is invalid. A target may be entered through a higher admissible layer with
a different source label.

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

### What remains valid

The scalar least-layer cost

```text
u_min(n)-1+s(n)-1+2*O*d_X(n)
```

is a valid lower bound on the ordinary symmetric cost: every higher layer adds
`2O`, more than any possible reduction of the source-label term. What is not
valid is using `u_min(n)` as an actual endpoint in a flow equation.

### Numerical history and repair

The invalid proof originally claimed

```text
small reciprocal bound 0.085226905,
combined bound through 60000000 equal to 0.086412209,
811320 mandatory values above 60000000,
805063 mandatory zero-layer values above 60000000.
```

Those conclusions were retracted when the endpoint error was found.

Later, the same numerical values were independently re-established by a
different proof: a signed-label potential is defined on all labels, telescopes
around the **actual** cycle, and proves that the least admissible layer
minimizes the modified scalar cost without identifying its source with the
actual source.

Files:

```text
docs/SIGNED_LABEL_POTENTIAL_DUAL.md
tools/verify_signed_label_potential_dual.py
docs/SIGNED_LABEL_SPLIT_RANGE_DUAL.md
tools/verify_signed_label_split_range_dual.py
```

The recovered numbers are now superseded by stronger valid bounds:

```text
sum_(n_i<=60000000)1/n_i <0.086152495,

p=...193:
  values above 60000000 >=25237969,
  zero-layer >=25231712;

p=...195:
  values above 60000000 >=826903,
  zero-layer >=820646.
```

The original endpoint-identification proof remains permanently invalid even
though some of its numerical outputs were later recovered by a new theorem.
Never cite the old proof as justification.

## 4. Finite-state positive-mean zero-layer route closed

A proposed future route sought a fixed finite quotient and a telescoping
inequality with a positive constant cost on every zero-layer transition.

Exact valuation-word coding and CRT produce arbitrarily long positive orbit
segments with

```text
q=0,
source label=target label=1,
transition cost=0
```

on every edge. Any fixed finite projection repeats a state on a sufficiently
long such segment. Summing a positive-mean telescoping inequality between the
repeated states would give `0>=delta*L`, a contradiction.

Thus no fixed finite-state positive-minimum-mean certificate of this form can
exist. This is a no-go theorem, not an error in a committed proof.

Files:

```text
docs/FINITE_STATE_ZERO_LAYER_POTENTIAL_NO_GO.md
tools/verify_finite_state_zero_layer_no_go.py
```

## 5. Claims that are evidence but not proofs

The following must never be promoted to a proof of divergence:

- a trajectory becoming extremely large after finitely many steps;
- positive average drift in a random model;
- a finite cycle barrier, regardless of size;
- existence of arbitrarily long finite growing blocks;
- existence of compatible 2-adic regeneration targets without an ordinary
  positive integer realization;
- a cycle that avoids `1`;
- a large lower bound on the cycle maximum when the available upper theorem
  controls only the minimum.

## 6. Rules after an error is found

When a mathematical error is discovered:

1. identify the exact false premise;
2. add a small explicit counterexample when possible;
3. replace the old verifier by an audit or regression test;
4. remove the invalid conclusion from durable status files;
5. record the retraction here;
6. rebuild only from the last retained valid statement.

Do not delete the history of an error. Precise audit history is part of
reproducibility.
