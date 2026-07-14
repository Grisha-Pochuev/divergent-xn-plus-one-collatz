# Nonpositive returns force doubly exponentially many ordinary blocks

> **Status update, 2026-07-14.** The conditional theorem below remains valid,
> but every nonpositive return has now been excluded by
> `NONPOSITIVE_RETURN_BLOCK_CORRECTION_EXCLUSION.md`. The repeated-type
> population is therefore no longer an active surviving branch.

Date: 2026-07-14

## Scope

Use the retained primary candidate

```text
m=4501,
B=2^4501,
d=349*2^500-347,
X=B-d.
```

Assume a hypothetical nontrivial positive cycle exists and that the actual return
from the minimum-boundary expanding exit has nonpositive credit.  Let

```text
p = full accelerated cycle length,
J = number of ordinary complete blocks,
T = number of exceptional complete blocks,
D = total cycle credit.
```

The retained return theorem gives

```text
1<=D<=4500.                                             (1)
```

This note proves

```text
J>2^(2^973-7).                                          (2)
```

If in addition the gcd `h` of all complete-block lengths satisfies `h>=2`, then

```text
J>2^(2^4978-7).                                         (3)
```

These are lower bounds on the number of ordinary complete blocks, not merely on
the number of accelerated steps.

## 1. Uniform lower bound for the cyclic gap

Put

```text
Delta_D(p)=2^(m*p-D)-X^p,
z=p*ln(B/X)-D*ln(2).
```

For a positive cycle `z>0`.  The retained one-sided continued-fraction
certificate is valid for every integer `1<=D<=4500` and gives

```text
z>2^-4023.                                               (4)
```

Also

```text
Delta_D(p)=2^(m*p-D)*(1-exp(-z)).                        (5)
```

For every `z>0`, the elementary inequality `exp(z)>1+z` implies

```text
1-exp(-z)>z/(1+z).
```

If `z<=1`, the right side is greater than `z/2`; if `z>1`, it is greater than
`1/2`.  Combining this with (4) yields

```text
Delta_D(p)>2^(m*p-D-4024).                               (6)
```

## 2. Signed elimination bounds every complete-block length

The signed complete-block elimination theorem applies with arbitrary ordinary and
exceptional blocks.  For every selected ordinary block of length `L`, it gives

```text
0<Delta_D(p)*u<J*B^(p-L+J+1),                            (7)
```

where `u` is a positive odd integer.  For every selected exceptional block of
length `k`, it gives

```text
0<Delta_D(p)*v<J*B^(p-k+J),                              (8)
```

where `v` is a positive odd integer.

Combining (6)--(8) and using `u,v>=1` gives

```text
2^[m*(L-J-1)-D-4024]<J,                                  (9)
2^[m*(k-J)-D-4024]<J.                                   (10)
```

These inequalities are the new leverage supplied by the small credit range (1).
The earlier global theorem had to allow `D` to grow like `4500*J`; here `D` is
uniformly at most `4500`.

## 3. A reusable tower lemma

Suppose, for some integer `K>=974`, that an independent theorem gives

```text
p>2^(2^K).                                              (11)
```

Define

```text
H=2^(K-1)-7,
U=2^(K-12).
```

Assume for contradiction that

```text
J<=2^H.                                                 (12)
```

Then `log2(J)<=H`.  Since `m=4501>2^12`,

```text
m*U>2^K>H+4500+4024.                                   (13)
```

If an ordinary block had `L>=J+1+U`, equation (9) and (13) would give
`J>2^H`, contradicting (12).  If an exceptional block had `k>=J+U`, equation
(10) gives the same contradiction.  Therefore every complete block has length
at most

```text
J+U.                                                    (14)
```

Let `E` be the ordinary-deficit sum and `F` the exceptional-excess sum.  Since
`D=E-F>=1`, every ordinary deficit is at most `4500`, and every exceptional
block has excess at least `1`,

```text
T<=F<=E-1<=4500*J-1.
```

Thus the total number of complete blocks is less than `4501*J<2^13*J`.  By
(14),

```text
p<2^13*J*(J+U).                                        (15)
```

There are two cases.

If `J<U`, then

```text
p<2^14*U^2=2^(2*K-10)<2^(2^K).
```

If `J>=U`, then `J+U<=2*J`, and (12) gives

```text
p<2^14*J^2
 <=2^(14+2*H)
 =2^(2^K).                                              (16)
```

Both cases contradict (11).  Hence the reusable conclusion is

```text
p>2^(2^K)  =>  J>2^(2^(K-1)-7).                        (17)
```

## 4. Primary consequences

For every nonpositive return, the retained actual-return barrier gives

```text
p>L_return>2^(2^974).
```

Applying (17) with `K=974` proves (2):

```text
J>2^(2^973-7).
```

If `h>=2`, the global phase-harmonic theorem gives the stronger full-cycle
frontier

```text
p>2^(2^4979).
```

Applying (17) with `K=4979` proves (3):

```text
J>2^(2^4978-7).
```

## 5. Repeated ordinary boundary type

An ordinary terminal deficit has only `4500` possible values.  Therefore one
deficit type occurs more than `J/4500` times.  Since `4500<2^13`, the preceding
bounds imply:

```text
any nonpositive return:
  one ordinary deficit type occurs >2^(2^973-20) times;

nonpositive return with h>=2:
  one ordinary deficit type occurs >2^(2^4978-20) times. (18)
```

All boundaries of one deficit type satisfy the same exact congruence

```text
d*n==2^e (mod X).
```

Thus (18) converts the conditional cycle problem into an enormous repeated
population inside one explicit boundary class modulo `X`.

## 6. Meaning and current status

The theorem is a valid conditional consequence of `R<=0`, but that hypothesis is
now impossible. The active proof problem has moved to the sole surviving branch

```text
R>=1,
L_return>2^3990.
```

The repeated-type theorem remains useful as an audited example of how much
structure the former branch would have forced, but it should not be used as the
next research target.

## 7. Verification

Run

```text
python tools/verify_nonpositive_return_ordinary_block_explosion.py
```

The checker independently reconstructs the exact continued-fraction gap for
`1<=D<=4500` and verifies all exponent margins for `K=974` and `K=4979`,
including the repeated-type exponents.
