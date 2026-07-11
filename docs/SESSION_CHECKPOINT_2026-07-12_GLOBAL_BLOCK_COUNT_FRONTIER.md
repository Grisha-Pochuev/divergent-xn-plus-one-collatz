# Session checkpoint: global ordinary-block frontier

Date: 2026-07-12

The strict prize problem remains open.  The primary candidate is unchanged:

```text
X=2^4501-349*2^500+347,
n0=1.
```

## New global theorem

Every hypothetical nontrivial positive cycle, regardless of the number of
exceptional contractions, must contain at least

```text
245833 ordinary complete blocks.                    (1)
```

This supersedes the earlier branch-specific small-block frontiers.

## Proof structure

Let `J` be the number of ordinary blocks, `R` the number of exceptional blocks,
`E` the sum of ordinary deficits, `F` the sum of exceptional excesses, and

```text
D=E-F>=1.
```

Exact signed elimination of all block cores gives one closure identity. Ordinary
blocks contribute positive terms and exceptional blocks contribute negative
terms. Dropping the negative terms gives, for a selected ordinary block of
length `L`,

```text
Delta_D(p)*u<J*B^(p-L+J+1),
```

and for a selected exceptional block of length `k`,

```text
Delta_D(p)*v<J*B^(p-k+J).
```

For `J<=245832`, the existing continued-fraction certificate applies because

```text
D<=4500*J-1<1106246945.
```

It forces

```text
Delta_D(p)>2^(4501*p-D-22206).
```

Comparison proves:

```text
every ordinary block length <=2J+6;
every exceptional block length <=2J+5.
```

Also

```text
R<=F<=4500J-1.
```

Thus for `J<=245832`,

```text
p<=J*(2J+6)+(4500J-1)*(2J+5)
 <=544026748963771<10^15.
```

This contradicts the retained elementary cycle barrier

```text
p>10^1201.
```

## Files

```text
docs/GLOBAL_ORDINARY_BLOCK_COUNT_FRONTIER.md
tools/verify_global_ordinary_block_count_frontier.py
```

The checker was run independently in the chat environment and passed. It is
included in `run_checks.py`. A complete repository-wide run was not executed.

## New decisive target

All surviving hypothetical cycles have at least `245833` ordinary blocks. The
next useful theorem must exploit the many-block population itself:

1. repeated ordinary deficits among only `4500` possible types;
2. exact block-boundary classes modulo `X` and `2^500-1`;
3. the exceptional credit budget `F=E-D`;
4. the full `X`-adic ladder inside long blocks.

Do not merely extend the continued-fraction denominator for a larger finite
record.