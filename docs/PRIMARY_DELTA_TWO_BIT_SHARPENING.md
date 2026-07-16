# Two-bit sharpening of the primary logarithmic drift

Date: 2026-07-17

## Scope

Use the primary candidate

```text
B=2^4501,
d=349*2^500-347,
X=B-d.
```

Put

```text
u=d/B,
delta=log2(B/X)=-ln(1-u)/ln(2).
```

The previously retained elementary estimate was

```text
delta<2^-3990.
```

This note sharpens it by two binary orders:

```text
delta<2^-3992.                                        (1)
```

The proof uses only exact rational comparisons and the first two positive terms
of the standard series for `ln(2)`.

## 1. Upper-bound the numerator

For `0<u<1`,

```text
-ln(1-u)<u/(1-u)=d/X.                                 (2)
```

We have

```text
d<349*2^500.                                          (3)
```

Also

```text
512*d<B.                                              (4)
```

Indeed, `d<2^509`, while `B=2^4501`. Equation (4) gives

```text
X=B-d>511*B/512.                                      (5)
```

Combining (3)--(5),

```text
2^3992*d/X
 <2^3992*(349*2^500)/(511*B/512)
 =349/511.                                            (6)
```

The exact rational comparison

```text
349/511<11/16                                         (7)
```

follows from

```text
349*16=5584<5621=511*11.
```

## 2. Lower-bound `ln(2)`

Use

```text
ln(2)=2*[1/3+1/(3*3^3)+1/(5*3^5)+...].               (8)
```

All terms are positive, so the first two give

```text
ln(2)>2*(1/3+1/81)=56/81.                             (9)
```

A second exact rational comparison gives

```text
56/81>11/16,                                          (10)
```

because

```text
56*16=896>891=81*11.
```

Equations (6)--(10) prove

```text
2^3992*d/X<ln(2).                                     (11)
```

## 3. Sharpened drift bound

From (2) and (11),

```text
2^3992*[-ln(1-u)]
 <2^3992*d/X
 <ln(2).
```

Dividing by `2^3992*ln(2)` proves (1):

```text
delta=-ln(1-u)/ln(2)<2^-3992.
```

No floating-point approximation is used.

## 4. Consequence for every contracting positive-credit segment

Consider any actual consecutive segment of complete blocks with

```text
C = net credit,
L = accelerated length,
x = source,
y = endpoint,
K = positive sum of block corrections.
```

Its exact base-2 height equation is

```text
log2(y/x)=C-L*delta+K.                                (12)
```

If

```text
C>=1,
y<x,
```

then the left side of (12) is negative and `K>0`, so

```text
L*delta>C+K>C.                                        (13)
```

Using (1),

```text
L>C/delta>C*2^3992.                                   (14)
```

Thus every positive-credit segment that actually contracts is individually
astronomically long.

For a zero-credit sponsor arch, the exact domination theorem already proves
strict contraction, but (14) does not apply because `C=0`.

## 5. Sharpened surviving return

The sponsored macro-exit theorem leaves an actual return with

```text
R>=1,
y>z,
log2(z/y)=R-L_return*delta+K_return<0.
```

Applying (14) gives the stronger retained conclusion

```text
L_return>R*2^3992>=2^3992.                            (15)
```

This replaces the former weaker statement `L_return>2^3990`.

It does not by itself exclude the return: the total credit `R` is not yet
uniformly bounded. Its value is that any proposed contracting positive-credit
macroblock now comes with a credit-proportional length lower bound.

## 6. Combined macroblock dichotomy

For a maximal sponsor arch or uncovered ordinary macroblock of positive credit
`C`, the local nondecreasing-segment theorem gives

```text
y>=x  =>  L < 2*C*B*X/[d*(X-d)].                      (16)
```

The present theorem gives

```text
y<x   =>  L > C*2^3992.                               (17)
```

Thus every positive-credit macroblock is forced onto one of two explicitly
quantified sides. The remaining special objects are zero-credit sponsor arches,
which always contract.

The next target is to combine this dichotomy with the permanent residue labels
and the exceptional-source floor.

## 7. Verification

Run

```text
python tools/verify_primary_delta_two_bit_sharpening.py
```

The checker verifies every rational inequality above, the series lower bound,
the exact primary comparison `delta<2^-3992`, and the symbolic consequences
(14)--(17).
