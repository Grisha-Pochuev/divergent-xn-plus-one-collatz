# No ordinary one-block cycle exists

Use the primary candidate

```text
m=4501,
B=2^4501,
d=349*2^500-347,
X=B-d.
```

This note excludes every hypothetical positive cycle consisting of exactly one
complete ordinary near-power block. Both the cycle length and the terminal
deficit are unrestricted within their natural ranges:

```text
p>=1,
1<=e<=4500.
```

The earlier small-credit proof covered only `e<=500`. The present argument
covers all `4500` ordinary terminal deficits.

## 1. Exact one-block equation

A one-block ordinary cycle of length `p` and terminal deficit `e` has valuation
word, up to cyclic rotation,

```text
m,m,...,m,m-e,
```

with `p-1` copies of `m`. Its source coordinate has the form

```text
d*n-1=2^(m*p-e)*u,
u positive and odd.                                   (1)
```

The complete-block endpoint formula is

```text
C_X^p(n)=(X^p*u+2^e)/d.                              (2)
```

Cycle closure gives

```text
Delta_e(p)*u=2^e-1,                                 (3)
```

where

```text
Delta_e(p)=2^(m*p-e)-X^p.                           (4)
```

Thus a cycle would require

```text
0<Delta_e(p)<=2^e-1.                                (5)
```

## 2. The first positive gap

Put

```text
delta=log2(B/X)=ln(1+d/X)/ln(2).
```

Then

```text
Delta_e(p)>0
```

is equivalent to

```text
p*delta>e.                                          (6)
```

Define the first positive-gap length

```text
L_e=floor(e/delta)+1.                               (7)
```

For `p<L_e`, the gap is nonpositive and (5) is impossible. For `p>=L_e`, use

```text
Delta_e(p+1)=B*Delta_e(p)+d*X^p.                    (8)
```

Once the gap is positive, (8) makes it strictly increase. Therefore it is
enough to prove

```text
Delta_e(L_e)>2^e-1.                                 (9)
```

for every `e=1,...,4500`.

## 3. Exact logarithmic certificate

Let

```text
y=d/X.
```

Use the exact rational bounds

```text
y-y^2/2 < ln(1+y) < y-y^2/2+y^3/3                 (10)
```

and the positive series

```text
ln(2)=2*sum_(j>=0) [1/(2j+1)*3^(-(2j+1))].         (11)
```

Truncating (11) after `2200` terms and bounding its positive remainder gives
exact rational numbers

```text
ln2_lo<ln(2)<ln2_hi.
```

For each of the `4500` deficits, exact integer/rational comparison verifies

```text
(L_e-1)*lny_hi < e*ln2_lo,
e*ln2_hi < L_e*lny_lo.                               (12)
```

Hence `L_e` in (7) is certified without relying on floating-point rounding.

Set

```text
z_e=L_e*ln(B/X)-e*ln(2)>0.                          (13)
```

The rational lower bound

```text
z_e>L_e*lny_lo-e*ln2_hi=:z_e^-.                     (14)
```

is positive for every `e`. All denominators `z_e^-` divide one fixed common
denominator of binary length at most

```text
22206.
```

Since a positive rational with such a denominator is greater than
`2^(-22206)`, we have

```text
z_e>2^(-22206).                                     (15)
```

## 4. The first positive gap already exceeds the additive term

From (4) and (13),

```text
Delta_e(L_e)
 =X^L_e*(exp(z_e)-1)
 >X^L_e*z_e.                                        (16)
```

Here

```text
X>2^4500,
L_e>=6.
```

Combining this with (15),

```text
Delta_e(L_e)
 >2^(4500*L_e-22206)
 >=2^4794
 >2^4501=B.                                         (17)
```

Because `e<=4500`,

```text
B>2^e-1.                                            (18)
```

Thus (9) holds for every ordinary deficit. By the recurrence (8), all later
positive gaps are even larger.

Therefore equation (3) has no solution.

## 5. Theorem

```text
For X=2^4501-349*2^500+347,
there is no positive cycle consisting of exactly one ordinary complete block.
```

This excludes all

```text
1<=e<=4500
```

and every cycle length `p`. It is an infinite structural exclusion, not a
finite cycle barrier.

## 6. Next extension

The next target is two ordinary blocks. For deficits `e_1,e_2`, exact closure
has a two-term additive numerator rather than the one-term equation (3). The
N-adic ladder and the small number of boundary values should allow the same
strategy to be organized by

```text
D=e_1+e_2
```

and the cyclic order of the two deficits.

## 7. Verification

```text
python tools/verify_no_exceptional_one_block_all_credits.py
```

The checker certifies all `4500` thresholds with exact rational inequalities
and proves the uniform lower bound (17). The decimal calculation is used only
to propose each integer `L_e`; every proposal is independently certified by
(12).
