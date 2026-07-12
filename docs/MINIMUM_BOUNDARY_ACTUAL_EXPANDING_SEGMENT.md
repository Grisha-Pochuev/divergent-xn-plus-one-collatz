# The minimum ordinary boundary starts an actual expanding segment

Use the primary candidate

```text
m=4501,
B=2^4501,
d=349*2^500-347,
X=B-d,
N=2^500-1.
```

This note extracts one actual consecutive expanding segment from every
hypothetical positive cycle.

## 1. Choose the minimum ordinary boundary

A hypothetical cycle must contain at least one ordinary complete block because
its total credit satisfies

```text
D=sum ordinary deficits-sum exceptional excesses>=1.
```

Among all cycle values immediately following an ordinary complete block, choose
the least and call it `x`.

Follow the actual orbit from `x` to the next value `y` immediately following an
ordinary complete block.  The intervening complete blocks consist of:

1. zero or more exceptional blocks;
2. one terminal ordinary block of deficit `e`, where `1<=e<=4500`.

By minimality,

```text
y>=x.                                                (1)
```

Let `F` be the sum of the exceptional excess valuations in this segment, and put

```text
C=e-F.
```

Let `L` be its accelerated length and `Kappa` the sum of its natural-logarithmic
block corrections.  The exact ratio identity gives

```text
ln(y/x)=C*ln(2)-L*ln(B/X)+Kappa.                     (2)
```

## 2. The net credit is positive

Every complete block satisfies

```text
0<kappa_block<ell*ln(B/X).
```

Hence

```text
0<Kappa<L*ln(B/X).                                   (3)
```

If `C<=0`, equations (2)--(3) give `ln(y/x)<0`, contradicting (1). Therefore

```text
1<=C<=e<=4500.                                       (4)
```

Consequently

```text
F=e-C<=4499.                                         (5)
```

Every exceptional block has excess at least `1`, so the segment contains at
most `4499` exceptional blocks and at most

```text
4500 complete blocks in total.                       (6)
```

## 3. The base multiplier is already expanding

Put

```text
z=L*ln(B/X)-C*ln(2).
```

Suppose `z>0`. Since `C<=4500<1106246945`, the exact one-sided
continued-fraction certificate applies and gives

```text
z>2^(-4023).                                         (7)
```

Every cycle value is greater than `N`. For a length-one complete block,

```text
kappa_block<1/(X*N).
```

For a block of length at least two,

```text
kappa_block<d/X^2.
```

Using (6),

```text
Kappa<4500/(X*N)+4500*d/X^2<2^(-4023).              (8)
```

Equations (2), (7), and (8) would imply `ln(y/x)<0`, contradicting (1). Thus
`z<=0`. Equality is impossible because it would give

```text
X^L=2^(4501*L-C),
```

with an odd left side and a power of two on the right. Therefore

```text
L*log2(B/X)<C.                                       (9)
```

The base multiplier satisfies

```text
2^C*(X/B)^L>1.                                      (10)
```

Since `Kappa>0`, equations (2) and (10) also sharpen (1) to

```text
y>x.                                                 (11)
```

## 4. Theorem

Every hypothetical nontrivial positive cycle contains an actual consecutive
orbit segment which:

```text
starts at the least ordinary boundary value;
ends at the next ordinary boundary value;
contains at most 4500 complete blocks;
has net credit 1<=C<=4500;
has strictly expanding base multiplier;
strictly increases the boundary value.
```

This avoids the splicing issue for one segment. It is not yet a divergence proof:
the remaining orbit could, in principle, later contract and return to the
minimum boundary.

## 5. Next target

Use the exact endpoint classes and exceptional descent to prove that a cycle
cannot return from `y>x` to the minimum ordinary boundary `x`. Candidate routes:

1. a return-segment credit lower bound;
2. an inverse `X`-adic descent from `x` through the return word;
3. an incompatibility modulo `X^2` between the expanding exit and the final
   return block.

## 6. Verification

```text
python tools/verify_minimum_boundary_actual_expanding_segment.py
```

The checker verifies the continued-fraction gap, the `4500`-block correction
bound, and the strict exponent inequalities.