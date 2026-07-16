# The least complete-block boundary has a pure ordinary exit

Date: 2026-07-17

## Scope

Use the primary candidate

```text
m=4501,
B=2^4501,
d=349*2^500-347,
X=B-d,
N=2^500-1.
```

Assume a hypothetical nontrivial positive cycle exists and use its canonical
complete-block partition. Let `z` be the least value occurring at any
complete-block boundary.

This note strengthens the previous minimum-ordinary-boundary decomposition. It
proves that the actual first exit from `z` is one pure ordinary complete block,
that this block already has an expanding base multiplier, and that the entire
remaining actual return has positive credit. In addition, the credit ballot
from `MINIMUM_BLOCK_BOUNDARY_CREDIT_BALLOT.md` controls every return prefix.

## 1. The first block is ordinary

For every complete block with source `n`, endpoint `n'`, and credit `c`, the
exact height-credit domination theorem gives

```text
n'/n<2^c.                                             (1)
```

Let `z'` be the endpoint of the first complete block after `z`. By minimality,

```text
z'>=z.                                                (2)
```

If the first block were exceptional, then `c=-b<=-1`, and (1) would give

```text
z'/z<2^-b<1,
```

contradicting (2). Therefore the first block is ordinary, with

```text
c=e,
1<=e<=4500.                                           (3)
```

No exceptional block occurs in this exit: it consists of exactly one complete
ordinary block.

## 2. Its base multiplier already expands

Let `L_exit` be the accelerated length of the first block and `K_exit` its
natural-logarithmic correction. The exact ratio identity is

```text
ln(z'/z)=e*ln(2)-L_exit*ln(B/X)+K_exit.                (4)
```

Put

```text
w=L_exit*ln(B/X)-e*ln(2).                             (5)
```

Suppose `w>0`. Because `1<=e<=4500`, the retained one-sided
continued-fraction certificate gives

```text
w>2^-4023.                                            (6)
```

The exit contains only one complete block. Since every cycle value is greater
than `N`, its correction satisfies

```text
K_exit<1/(X*N)    if L_exit=1,
K_exit<d/X^2      if L_exit>=2.                       (7)
```

Exact integer comparison gives both bounds in (7) below `2^-4024`, hence below
(6). Equations (4)--(7) would imply `ln(z'/z)<0`, contradicting (2).
Equality `w=0` is impossible because it would make the odd integer `X^L_exit` a
power of two. Therefore

```text
L_exit*log2(B/X)<e.                                  (8)
```

The base multiplier is strictly expanding:

```text
2^e*(X/B)^L_exit>1.                                  (9)
```

Since `K_exit>0`, equation (4) now also gives

```text
z'>z.                                                (10)
```

Thus the least complete-block boundary starts an actual, consecutive, pure
ordinary expanding block.

## 3. The remaining actual return has positive credit

Follow the actual remaining orbit from `z'>z` back to `z`. Write

```text
R = return ordinary-deficit sum - return exceptional-excess sum,
L_return = accelerated return length.
```

The total cycle credit is

```text
D=e+R>=1.                                             (11)
```

Assume for contradiction that `R<=0`. Then (3) and (11) give

```text
1<=D<=e<=4500.                                        (12)
```

For this bounded total credit, the retained continued-fraction and permanent
class harmonic-packing argument applies with an even smaller exit correction
than before. If

```text
L_return<=2^(2^974),                                  (13)
```

then the return correction is below `2^-4024`, the one-block exit correction is
below `2^-4024`, and their sum is below the mandatory cycle gap `2^-4023`.
Therefore

```text
R<=0  =>  L_return>2^(2^974).                         (14)
```

On the other hand, the global block-correction theorem and (12) give

```text
p<2^4006.                                             (15)
```

But the return is a proper part of the cycle, so (14) gives

```text
p>L_return>2^(2^974)>2^4006,                          (16)
```

contradicting (15). Hence

```text
R>=1.                                                 (17)
```

The exact return equation and the retained estimate

```text
log2(B/X)<2^-3990
```

then imply

```text
L_return>2^3990.                                      (18)
```

## 4. Prefix debt on the surviving return

The credit-ballot theorem says that, when complete blocks are read from `z`,
every nonempty block-boundary prefix has cumulative credit at least `1`.
After the first ordinary block contributes `e`, let `Q_j` be the credit of any
prefix of the remaining return ending at a complete-block boundary. Then

```text
e+Q_j>=1,
Q_j>=1-e>=-4499.                                      (19)
```

Thus the surviving return has all of the following simultaneous properties:

```text
it is actual and consecutive;
it begins after one pure ordinary expanding block;
R>=1;
L_return>2^3990;
return-prefix credit never drops below -4499 at a block boundary.
```

This is stronger than knowing only the final sign `R>=1`: the return cannot
front-load an arbitrarily large exceptional debt.

## 5. New decisive target

The strict prize problem remains open. Every hypothetical cycle is now reduced
to a particularly rigid form:

1. start at the least complete-block boundary `z`;
2. take one pure ordinary block of deficit `1<=e<=4500` whose base multiplier
   expands;
3. make an astronomically long positive-credit return;
4. keep the running return debt above `-4499` at every complete-block boundary;
5. match every exceptional excess unit to an earlier ordinary deficit unit.

The strongest next step is to combine this ordered matching with the permanent
`N` and `1093^2` labels or with the exceptional-source floor. A successful
argument should show that an exceptional block cannot be sponsored by an earlier
ordinary unit without forcing either an impossible source repetition or too much
harmonic correction.

## 6. Verification

Run

```text
python tools/verify_minimum_block_boundary_pure_ordinary_exit.py
```

The checker verifies the bounded-credit continued-fraction gap, the sharper
one-block exit correction, the permanent-class harmonic return bound, the global
length contradiction for `R<=0`, the `R>=1` return-length bound, and the primary
`-4499` prefix-debt constant.
