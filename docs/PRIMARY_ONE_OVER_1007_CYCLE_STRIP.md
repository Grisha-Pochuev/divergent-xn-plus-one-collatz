# Primary one-over-1007 cycle strip

Date: 2026-07-17

## Scope

Use the retained primary candidate

```text
N=2^500-1,
B=2^4501,
d=349*2^500-347,
X=B-d.
```

Assume, for contradiction, that a nontrivial positive accelerated `Xn+1` cycle
exists.  For its complete-block decomposition write

```text
p = full accelerated length,
A = total valuation,
D = 4501*p-A >= 1.
```

For an actual consecutive complete-block segment write

```text
C = net credit,
L = accelerated length,
x = source,
y = endpoint.
```

The retained exact segment identity is

```text
log2(y/x)=C-L*delta+K,
delta=log2(B/X),
0<K<L*epsilon,
epsilon=1/(X*N*ln(2)).                              (1)
```

This note sharpens both sides of the drift scale by exact rational arithmetic.

## 1. Exact rational bracket for `ln(2)`

Use

```text
ln(2)=2*sum_(j>=0) 1/[(2*j+1)*3^(2*j+1)].             (2)
```

All terms are positive, so the first three terms give

```text
ln(2)>842/1215.                                        (3)
```

For `j>=4`, consecutive terms have ratio

```text
[(2*j+1)/(2*j+3)]/9 < 1/9.
```

Therefore the tail beginning at `j=4` is smaller than `9/8` times its first
term.  The first four terms plus this geometric tail bound give

```text
ln(2)<1910051/2755620.                                 (4)
```

No floating-point estimate is used.

## 2. Two-sided primary drift sharpening

Put `u=d/B`.  The elementary inequalities

```text
-ln(1-u)>u,
-ln(1-u)<u/(1-u)=d/X                                  (5)
```

and (3)--(4) imply

```text
delta-epsilon
 >[d/B-1/(X*N)]/[1910051/2755620]
 >1007*2^-4002,                                        (6)
```

and

```text
delta
 <(d/X)/[842/1215]
 <1008*2^-4002.                                        (7)
```

Both final comparisons are exact integer/rational comparisons checked by the
companion script.

## 3. Unified segment consequences

From (1) and (6), every actual consecutive complete-block segment satisfies

```text
log2(y/x)<C-1007*L*2^-4002.                            (8)
```

For a positive-credit segment `C>=1`:

```text
if y>=x, then L<C*2^4002/1007;                         (9)
if y<x,  then L>C/delta>C*2^4002/1008.                (10)
```

Thus the two possible length regimes are separated at two adjacent integer
coefficients, `1007` and `1008`, on the common scale `2^4002`.

For a zero-credit sponsor arch, (8) gives the strengthened quantitative loss

```text
log2(source/endpoint)>1007*L*2^-4002.                 (11)
```

## 4. Full-cycle strip

For the full cycle, (1) becomes

```text
0=D-p*delta+K.
```

Since `K>0`, equation (7) gives

```text
p>D/delta>D*2^4002/1008.                              (12)
```

Since `K<p*epsilon`, equation (6) gives

```text
p<D*2^4002/1007.                                      (13)
```

Therefore every hypothetical primary cycle must satisfy

```text
D*2^4002/1008
 <p
 <D*2^4002/1007.                                      (14)
```

The ratio of the upper endpoint to the lower endpoint is `1008/1007`, so the
relative width is exactly

```text
1008/1007-1=1/1007<0.001.                             (15)
```

Thus the surviving length-per-credit window is narrower than `0.1%`.  The
previous retained window had relative width `27/997`, about `2.71%`; (14)
shrinks that scalar window by more than a factor of `27`.

## 5. Exit-return specialization

For the retained initial macro-exit and remaining return, write

```text
D=C+R,
1<=C<=4500,
R>=1,
p=L_macro+L_return.
```

The initial nondecreasing macro-exit obeys

```text
L_macro<C*2^4002/1007<2^4005.                         (16)
```

The contracting positive-credit return obeys

```text
L_return>R*2^4002/1008,                               (17)
```

while the full-cycle upper bound gives

```text
L_return<p<(C+R)*2^4002/1007
              <=(R+4500)*2^4002/1007.                (18)
```

## 6. Meaning and limitation

This is an infinite proof restriction, not a finite trajectory computation.  It
forces every hypothetical positive cycle into an exceptionally thin scalar
window and strengthens the quantitative charge on every zero-credit arch.

It does not yet exclude the positive-credit return, because neither `D` nor `R`
is bounded.  Gate G3 therefore remains open.  The next step must use arithmetic
information not present in the scalar drift alone: permanent `N` and `1093^2`
labels, exceptional-source floors, exact adjacent-label lifts, or the global
common-boundary divisor.

## 7. Verification

Run

```text
python tools/verify_primary_one_over_1007_cycle_strip.py
```

The checker uses only Python standard-library exact integers and `Fraction`.  It
verifies the series bracket (3)--(4), the drift comparisons (6)--(7), the strip
ratio (15), the initial-exit comparison, and the strengthened return coefficient.
