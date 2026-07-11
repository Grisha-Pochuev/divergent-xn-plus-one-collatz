# Minimum-boundary positive circulation

Use the primary candidate

```text
m=4501,
B=2^4501,
d=349*2^500-347,
X=B-d,
N=2^500-1.
```

This note extracts a bounded positive-credit circulation from every hypothetical
cycle, even though the full cycle must contain at least `245833` ordinary
blocks.

## 1. Ordinary boundary types

Every ordinary complete block has a terminal deficit

```text
1<=e<=4500.
```

Immediately after such a block, the next cycle value satisfies

```text
d*n==2^e (mod X).                                    (1)
```

Thus the boundary type is exactly the deficit `e`.

For each type `e` that occurs in a hypothetical cycle, choose the smallest cycle
value of that type and call it

```text
x_e.
```

Follow the actual orbit from `x_e` to the next ordinary boundary.  Let that next
boundary have type `f(e)` and value `y_e`.  Between them there may be zero or
more exceptional complete blocks, followed by one ordinary complete block.

Since `x_(f(e))` is the smallest value of type `f(e)`,

```text
y_e>=x_(f(e)).                                       (2)
```

The map `e -> f(e)` is a function on the finite set of occurring types.
Therefore its directed graph contains a directed cycle

```text
e_1 -> e_2 -> ... -> e_q -> e_1,
q<=4500.                                             (3)
```

Multiplying (2) around this graph cycle gives

```text
product_(i=1)^q y_(e_i)/x_(e_i) >=1.                 (4)
```

The selected orbit intervals are disjoint elementary intervals between
successive ordinary boundaries.

## 2. Credit and length of the selected circulation

For the interval from type `e_i` to type `e_(i+1)`, define its net credit as

```text
w_i=e_(i+1)-sum exceptional excesses in that interval.
```

Let

```text
C=sum_i w_i,
L=sum selected accelerated lengths,
Kappa=sum selected natural-logarithmic block corrections.
```

The exact block ratio identity gives

```text
sum_i ln(y_(e_i)/x_(e_i))
 =C*ln(2)-L*ln(B/X)+Kappa.                            (5)
```

Every block correction is strictly smaller than

```text
ell*ln(B/X),
```

because

```text
kappa_nat<ell*d/(2*X^ell)
          <=ell*d/(2*X)
          <ell*ln(B/X).                              (6)
```

Combining (4)--(6), `C` cannot be nonpositive.  Hence

```text
C>=1.                                                (7)
```

There are only `q<=4500` selected ordinary blocks, so

```text
C<=sum selected ordinary deficits
 <=4500*q
 <=20250000.                                         (8)
```

The total selected exceptional excess is smaller than the selected ordinary
deficit sum.  Since every exceptional block has excess at least `1`, the total
number `T` of selected complete blocks satisfies

```text
T<=q+(4500*q-1)
 <=20254499.                                         (9)
```

## 3. The selected base multiplier must already expand

Put

```text
z=L*ln(B/X)-C*ln(2).                                 (10)
```

Suppose for contradiction that `z>0`.  Then

```text
L/C>ln(2)/ln(B/X).
```

Since `1<=C<=20250000<1106246945`, the exact one-sided continued-fraction
certificate applies.  Exact rational interval arithmetic gives the sharper
bound

```text
z>2^(-4023).                                         (11)
```

On the other hand, every cycle value is greater than

```text
N=2^500-1.
```

For a selected complete block of length `1`, its natural-logarithmic correction
is less than

```text
1/(X*N).                                             (12)
```

For a selected complete block of length at least `2`, the structural block bound
gives

```text
kappa_nat<ell*d/(2*X^ell)<=d/X^2.                   (13)
```

Using (9),

```text
Kappa
 <20254499/(X*N)+20254499*d/X^2
 <2^(-4023).                                         (14)
```

But (4)--(5) and `z>0` require

```text
Kappa>=z,
```

contradicting (11)--(14).  Therefore

```text
L*ln(B/X)<C*ln(2),
```

or equivalently

```text
L*delta<C,
delta=log2(B/X).                                    (15)
```

Equality is impossible because it would imply that the odd integer `X^L` is a
power of two.

## 4. Theorem

Every hypothetical nontrivial positive cycle contains a collection of disjoint
ordinary-to-ordinary orbit intervals such that

```text
number of ordinary intervals q <=4500;
number of all selected complete blocks <=20254499;
1<=total credit C<=20250000;
product of actual height ratios >=1;
L*delta<C.
```

Thus the selected formal concatenation has base multiplier

```text
2^C*(X/B)^L>1.                                       (16)
```

This is a genuine bounded circulation extracted from the unavoidable many-block
population.  It is not yet a divergence proof because the selected intervals
need not be consecutive in the original orbit and their two-adic cylinders need
not concatenate.

## 5. Next target

The missing step is a regeneration or splicing theorem.  One must use the fact
that the selected interval endpoints have matching boundary classes modulo `X`
and `N` to show either:

1. the selected valuation words can be concatenated into an admissible positive
   orbit segment;
2. the mismatch values create a strict height descent;
3. or the lifted closure modulo `X^2` is impossible.

## 6. Verification

```text
python tools/verify_minimum_boundary_positive_circulation.py
```

The checker verifies the exact continued-fraction gap `2^-4023`, the maximum
credit and block counts, and the correction upper bound.