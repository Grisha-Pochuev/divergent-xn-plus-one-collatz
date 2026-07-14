# Global block corrections exclude every nonpositive return

Date: 2026-07-14

## Scope

Let

```text
B=2^m,
d positive odd,
1<=d<B/2,
X=B-d>=5.
```

Use the accelerated map

```text
C_X(n)=(X*n+1)/2^v2(X*n+1).
```

For a hypothetical positive cycle let

```text
p = accelerated cycle length,
A = total valuation,
D = m*p-A >=1.
```

This note proves the general upper bound

```text
p < 2*D*B*X/[d*(X-d)].                                (1)
```

For the retained primary candidate, the minimum-boundary return theorem gives
`1<=D<=4500` whenever the actual return has nonpositive credit.  Equation (1)
then gives

```text
p<2^4006,                                               (2)
```

contradicting the already proved return lower bound

```text
p>L_return>2^(2^974).                                   (3)
```

Therefore the nonpositive-return branch is impossible.

## 1. Exact block-correction identity

Partition the cyclic valuation word into complete near-power blocks.  For block
`j`, let

```text
ell_j = its accelerated length,
n_j   = its source,
q_j   = ((B/X)^ell_j-1)/(d*n_j).
```

The retained complete-block ratio identity gives

```text
sum_j ln(1+q_j)=p*ln(B/X)-D*ln(2).                     (4)
```

Also

```text
sum_j ell_j=p.                                         (5)
```

## 2. A uniform upper bound on every correction

For an ordinary block with terminal deficit `e`,

```text
d*n_j-1=B^ell_j*u/2^e,
1<=e<=m-1,
u positive odd.
```

Hence

```text
d*n_j-1>=2*B^(ell_j-1).
```

For an exceptional block,

```text
d*n_j-1=B^ell_j*u>=B^ell_j>=2*B^(ell_j-1).
```

Thus both block types satisfy

```text
d*n_j>2*B^(ell_j-1).                                   (6)
```

The difference-of-powers identity gives

```text
B^ell_j-X^ell_j
 =d*sum_(r=0)^(ell_j-1) B^(ell_j-1-r)*X^r
 <ell_j*d*B^(ell_j-1).                                 (7)
```

Combining (6)--(7),

```text
0<q_j<ell_j*d/(2*X^ell_j)
       <=ell_j*d/(2*X).                                (8)
```

Since `ln(1+z)<z` for `z>0`, equations (4), (5), and (8) imply

```text
p*ln(B/X)-D*ln(2)
 <sum_j q_j
 <p*d/(2*X).                                           (9)
```

Therefore

```text
p*[ln(B/X)-d/(2*X)]<D*ln(2).                           (10)
```

## 3. Eliminate logarithms with an elementary rational bound

For `t>0`,

```text
ln(1+t)>t/(1+t).
```

Taking `t=d/X` and using `B=X+d`,

```text
ln(B/X)>d/B.                                           (11)
```

Because `d<B/2`, we have `X-d=B-2*d>0`, and

```text
d/B-d/(2*X)=d*(X-d)/(2*B*X)>0.                        (12)
```

Equations (10)--(12), together with `ln(2)<1`, yield

```text
p*d*(X-d)/(2*B*X)<D*ln(2)<D.
```

This proves the general theorem (1):

```text
p < 2*D*B*X/[d*(X-d)].
```

The result is cycle-wide.  It does not rely on a finite trajectory cutoff,
random drift, or local source matching.

## 4. Primary-candidate specialization

Use

```text
m=4501,
B=2^4501,
d=349*2^500-347,
X=B-d.
```

If the actual return from the minimum-boundary expanding exit has credit `R<=0`,
then the retained exit theorem gives an exit credit `1<=C<=4500`, while total
cycle credit is

```text
D=C+R.
```

Every positive cycle has `D>=1`, so

```text
1<=D<=4500.                                            (13)
```

Exact integer arithmetic verifies

```text
2*4500*B*X < 2^4006*d*(X-d).                           (14)
```

Applying (1) and (13)--(14),

```text
p<2^4006.                                              (15)
```

But the retained nonpositive-return harmonic theorem proves

```text
L_return>2^(2^974).
```

Since the return is a proper part of the full cycle,

```text
p>L_return>2^(2^974)>2^4006,                           (16)
```

contradicting (15).

Hence:

```text
A hypothetical positive cycle cannot have R<=0.        (17)
```

## 5. New surviving branch

The minimum-boundary dichotomy is now reduced to one branch:

```text
R>=1,
L_return>2^3990.
```

The strict prize problem is not yet solved because a positive-credit return has
not been excluded.  However, the entire nonpositive branch, including its
`h=1` and `h>=2` subdivisions, is closed.

The next target is therefore the positive-credit return itself.  A successful
argument must exploit more than the sign `R>=1`; likely inputs are the exact
minimum-boundary height gain, the global block correction identity, or a
cycle-closing restriction on where the positive return credit can occur.

## 6. Regression and verification

Run

```text
python tools/verify_nonpositive_return_block_correction_exclusion.py
```

The checker verifies:

- the correction inequality on a grid of exact complete blocks;
- the general cycle inequality on all three known accelerated `5n+1` cycles;
- the exact primary-candidate comparison (14);
- the exponent comparison `2^974>4006` used in (16).

No external literature theorem is used as an unchecked dependency.
