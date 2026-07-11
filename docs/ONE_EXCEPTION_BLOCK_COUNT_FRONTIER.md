# One-exception cycles need at least 245833 ordinary blocks

Use the primary candidate

```text
m=4501,
B=2^4501,
d=349*2^500-347,
X=B-d.
```

This note proves the cycle-length-independent frontier

```text
Any positive cycle with exactly one exceptional complete block
must contain at least 245833 ordinary complete blocks.          (1)
```

The exceptional and ordinary block lengths remain unrestricted.

## 1. Block coordinates

Suppose a hypothetical cycle has exactly one exceptional block and `J` ordinary
blocks.  For an ordinary block put

```text
ell_i>=1,
1<=e_i<=4500,
h_i=2^e_i,
r_i=1,
a_i=h_i-1.
```

For the exceptional block put

```text
ell_exc=k>=1,
h_exc=1,
r_exc=2^b,
a_exc=-(2^b-1),
b>=1.
```

For every block source `n_i`, define its positive odd core `u_i` by

```text
d*n_i-1=B^ell_i*u_i/h_i.                            (2)
```

The exact complete-block formulas give

```text
r_i*B^ell_(i+1)*u_(i+1)
 =h_(i+1)*X^ell_i*u_i+h_(i+1)*a_i.                  (3)
```

Let

```text
E=sum ordinary e_i,
D=E-b,
p=sum all block lengths.
```

Cycle closure requires

```text
D>=1,
Delta_D(p)=2^(m*p-D)-X^p>0.                          (4)
```

Also

```text
D<=E<=4500*J.                                        (5)
```

## 2. General signed closure bound

Choose any ordinary block as block `0`.  Put

```text
A_i=r_i*B^ell_(i+1),
C_i=h_(i+1)*X^ell_i,
f_i=h_(i+1)*a_i.
```

Eliminating all other cores from (3) gives

```text
[(product A_i)-(product C_i)]*u_0
 =sum_j f_j*(product_(i<j) A_i)*(product_(i>j) C_i). (6)
```

The products on the left are

```text
product A_i=2^b*B^p,
product C_i=2^E*X^p.
```

Since `E=b+D`, equation (6) becomes

```text
2^E*Delta_D(p)*u_0=signed additive sum.              (7)
```

There is exactly one negative term, from the exceptional block.  Discarding it
can only increase the right side.  There are `J` positive ordinary terms.

If the selected ordinary block has length `L`, the `B`- and `X`-length factors
in each positive term contain every block length except `L`.  After division by
`2^E`, its remaining power-of-two coefficient is less than

```text
2^(b+e_0)<B^(J+1),                                   (8)
```

because `b<=4500*J-1` and `e_0<=4500`.  Hence

```text
0<Delta_D(p)*u_0<J*B^(p-L+J+1).                      (9)
```

If block `0` is specifically the first ordinary block after the exceptional
block, the exceptional factor `2^b` is absent from every positive term before
closure.  The sharper bound is

```text
0<Delta_D(p)*u_0<J*B^(p-L+1).                        (10)
```

## 3. Uniform lower bound for the positive gap

The continued-fraction certificate from
`NO_EXCEPTIONAL_BLOCK_COUNT_FRONTIER.md` depends only on `(p,D)`, not on block
types.  It proves that whenever

```text
0<D<1106246945,
Delta_D(p)>0,
```

then

```text
Delta_D(p)>2^(m*p-D-22206).                          (11)
```

Assume for contradiction that

```text
J<=245832.
```

Then by (5),

```text
D<=4500*J-1<=1106243999<1106246945,                  (12)
```

so (11) applies.

## 4. Every ordinary block is short

Let `L` be the longest ordinary block and use it as block `0` in (9).  If

```text
L>=2*J+7,
```

then (5) and (11) give the exponent margin

```text
m*L-D-22206-m*(J+1)
 >=m*(2*J+7)-(4500*J-1)-22206-m*(J+1)
 =J+4801.                                            (13)
```

Thus the lower bound (11) is already larger than the upper bound (9), since
`2^(J+4801)>J`.  This is impossible.  Therefore

```text
L<=2*J+6.                                            (14)
```

The total length `S` of all ordinary blocks consequently satisfies

```text
S<=J*(2*J+6).                                        (15)
```

## 5. The exceptional block is also short

Let the exceptional block have length `k` and excess `b`.  Let the immediately
following ordinary block have length `ell`, deficit `e`, and core `u`; let `v`
be the exceptional source core.  The exact source relation is

```text
2^b*2^(m*ell-e)*u=X^k*v-(2^b-1).                    (16)
```

Use the sharp closure bound (10).

### Case 1: `X^k<2^(b+1)`

Since

```text
X>B/2=2^(m-1),
b+1<=E<=4500*J=(m-1)*J,
```

we obtain

```text
(m-1)*k<b+1<=(m-1)*J,
```

and hence

```text
k<=J-1.                                              (17)
```

### Case 2: `X^k>=2^(b+1)`

Equation (16) gives

```text
u>X^k/[2^(b+1)*2^(m*ell-e)].                         (18)
```

Combining (18), (10), and (11), and cancelling the common powers of `B`, gives

```text
X^k<J*2^(m+E+22206).                                 (19)
```

Now `J<2^18`, `E<=4500*J`, and `X>2^4500`.  If `k>=J+6`, the exponent on the
left exceeds the exponent upper bound on the right by at least

```text
4500*6-4501-22206-18=275.                            (20)
```

Therefore

```text
k<=J+5.                                              (21)
```

Both cases are covered by (21).

## 6. Final contradiction

From (15) and (21),

```text
p=S+k
 <=J*(2*J+6)+J+5.
```

At `J=245832` the right side is exactly

```text
120868465277<10^12.                                  (22)
```

But the independently proved elementary cycle barrier for the primary
candidate gives

```text
p>2*X/(3*d)>10^1201.                                 (23)
```

Equations (22)--(23) contradict one another.  Hence no cycle with exactly one
exceptional block and at most `245832` ordinary blocks exists, proving (1).

## 7. Meaning

This is not a trajectory cutoff and not a bound on the individual block
lengths.  It excludes, at once, every one-exception cycle having up to `245832`
ordinary complete blocks, even when the proposed cycle length is arbitrarily
large.

The remaining one-exception branch is

```text
exactly one exceptional block + at least 245833 ordinary blocks.
```

Its next useful target is a population theorem for repeated ordinary deficits,
combined with the exact exceptional source class and the `X`-adic ladder.

## 8. Verification

```text
python tools/verify_one_exception_block_count_frontier.py
```

The checker certifies the continued-fraction denominator frontier, the gap-loss
constant, the longest-ordinary-block inequality, the exceptional-length
inequality, the polynomial length upper bound, and comparison with the existing
cycle barrier.