# Giant growth block forced by the exceptional first-length minimum

Consider the exceptional branch for

```text
p = 177780727155637125193,
m = 1672312375827977333.
```

The minimum dichotomy certificate proves that the edge entering `m` has
full-order layer at least

```text
q>=33.
```

Let

```text
k=#{i:q_i>=1},
Q=sum_i q_i.
```

Since every positive-layer edge contributes at least one and one contributes
at least `33`,

```text
Q>=k+32.
```

The retained full-layer budget gives `Q<=6257`, hence

```text
k<=6225.                                          (1)
```

## 1. Strengthened deficit over zero-layer blocks

The `k` positive-layer edges split the remaining edges into `k` zero-layer
blocks.  For block `j`, put

```text
D_j=133*L_j-2*S_j,
```

where `L_j` is its length and `S_j` its valuation sum.

As in the giant compensating growth theorem,

```text
sum_j D_j >= 2*O*Q-131*k-1.
```

Using `Q>=k+32`,

```text
sum_j D_j
 >= k*(2*O-131)+64*O-1.
```

By (1), one block satisfies

```text
D_j >= 2*O-131+ceil((64*O-1)/6225)
     = 3740753004121136066.                       (2)
```

Since each summand `133-2*s` is at most `131`, (2) forces

```text
L_j >= 28555366443672795.                         (3)
```

## 2. Growth along the block

Every edge in this block has full layer zero.  Therefore

```text
n_end/n_start > X^L/2^S > 2^(D_j/2).
```

In particular,

```text
n_end/n_start > 2^1870376502060568033.            (4)
```

## 3. Meaning

If the first remaining cycle uses its unique possible `a_out=56` minimum, it
must also contain a consecutive zero-layer block of at least

```text
28555366443672795
```

steps with growth exceeding (4).  This is stronger than the generic
positive-layer growth block because the explicit minimum consumes at least
`33` full layers on its incoming edge.

The result is not yet a contradiction: the same incoming edge can provide an
enormous compensating contraction.  It gives a precise branch-specific height
target for a signed global potential.

Run

```text
python tools/verify_exceptional_minimum_growth_block.py
```

for the exact arithmetic certificate.
