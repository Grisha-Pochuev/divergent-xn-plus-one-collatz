# Session checkpoint: first one-exception no-go theorem

Date: 2026-07-12

Read this after

```text
docs/SESSION_CHECKPOINT_2026-07-12_NO_EXCEPTIONAL_BLOCK_FRONTIER.md
```

The strict prize problem remains open. The primary candidate is unchanged:

```text
X=2^4501-349*2^500+347,
n0=1.
```

## New strict result

A cycle containing exactly

```text
one exceptional complete block
+
one ordinary complete block
```

is impossible for every choice of lengths and every admissible pair

```text
1<=b<e<=4500,
D=e-b.
```

The proof uses two dual source-core closure equations. One equation has an
additive numerator controlled by the exceptional block length; the other is
controlled by the ordinary block length. Choosing the shorter of the two blocks
gives the uniform upper bound

```text
2*B^(floor(p/2)+1).
```

Exact rational logarithmic bounds prove that the positive cycle gap is larger
than this quantity for every

```text
D=1,...,4499.
```

Hence any cycle with exactly one exceptional block must contain at least two
ordinary blocks.

Files:

```text
docs/ONE_EXCEPTION_ONE_ORDINARY_NO_GO.md
tools/verify_one_exception_one_ordinary_no_go.py
```

The checker is included in `run_checks.py`. The exact threshold calculations
were also run in the chat Python environment. A complete repository-wide run
was not executed.

## Current strict split

Every still-possible cycle belongs to one of these branches:

```text
A. no exceptional blocks and at least 245833 ordinary blocks;
B. exactly one exceptional block and at least two ordinary blocks;
C. at least two exceptional blocks.
```

## Exact next target

For branch B, derive a general closure formula for

```text
one exceptional block + J ordinary blocks,
J>=2.
```

The desired bound should choose a longest ordinary block or use the exact
1505-digit exceptional source, then combine it with the full `X`-adic ladder.
Do not merely extend the finite continued-fraction denominator.
