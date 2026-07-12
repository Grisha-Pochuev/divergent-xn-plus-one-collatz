# Return-credit dichotomy after the minimum-boundary expanding segment

Use the primary candidate

```text
B=2^4501,
d=349*2^500-347,
X=B-d.
```

Assume a hypothetical nontrivial positive cycle exists. Let `x` be the least
cycle value immediately following an ordinary complete block, and let `y>x` be
the next such boundary supplied by
`MINIMUM_BOUNDARY_ACTUAL_EXPANDING_SEGMENT.md`.

Follow the actual remaining orbit from `y` back to `x`. Write

```text
R = (sum of ordinary deficits) - (sum of exceptional excesses)
L = accelerated length of the return segment
delta = log2(B/X).
K = sum of the positive base-2 additive block corrections.
```

The exact block-ratio identity on the return segment is

```text
log2(x/y) = R - L*delta + K,                    (1)
```

where `K>0`. Since `x<y`, the left side is negative. Therefore

```text
R < L*delta.                                    (2)
```

## Explicit smallness of delta

Put `u=d/B`. Direct integer comparison gives

```text
d < 2^509,
u < 2^-3992,
2u < 1.
```

For `0<u<1/2`,

```text
-ln(1-u) < u/(1-u) < 2u.
```

Also `ln(2)>1/2`, hence `1/ln(2)<2`. Consequently

```text
delta = -ln(1-u)/ln(2) < 4u < 2^-3990.         (3)
```

## Theorem

The actual return segment from `y` to `x` satisfies the following strict
dichotomy.

1. If `R>=1`, then

   ```text
   L > 2^3990.
   ```

   Indeed, (2)--(3) give `1<=R<L*delta<L*2^-3990`.

2. If `L<=2^3990`, then `R<=0`. Equivalently, on every such shorter return,
   the total exceptional excess is at least the total ordinary deficit.

This does not yet exclude a cycle: a return with zero or negative net credit is
still possible, and a positive-credit return could in principle be astronomically
long. It does, however, close the short positive-credit return branch completely.
Any successful return obstruction may now split into exactly two cases:

```text
short return  -> exceptional excess >= ordinary deficit sum;
positive-credit return -> accelerated length > 2^3990.
```

The statement concerns the actual consecutive return segment, not a splice and
not a finite trajectory experiment.

## Verification

```text
python tools/verify_minimum_boundary_return_credit_dichotomy.py
```

The checker verifies the exact integer inequalities used to obtain
`delta<2^-3990` and the symbolic integer implication from `R<L*delta`.